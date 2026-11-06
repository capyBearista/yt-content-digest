"""Fast, offline tests for YouTube comment-thread processing and CLI extraction."""

import importlib.util
from pathlib import Path
import subprocess
from unittest.mock import patch

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "ingest_video.py"
spec = importlib.util.spec_from_file_location("ingest_video", SCRIPT)
assert spec and spec.loader
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


def comment(comment_id, parent, timestamp, likes=0, text=None):
    return {
        "id": comment_id,
        "parent": parent,
        "timestamp": timestamp,
        "like_count": likes,
        "text": text if text is not None else comment_id,
        "author": "@" + comment_id,
    }


def test_hierarchy_and_like_ranking():
    rows = [
        comment("p2", "root", 1, 1200),
        comment("a1", "p1", 11),
        comment("grand2", "a2", 50),
        comment("p1", "root", 1, 1240),
        comment("a2", "p1", 20),
        comment("grand1", "a1", 12),
        comment("great", "grand1", 13),
        comment("a3", "p1", 21),
        comment("orphan", "notfound", 2),
        comment("unknown", "p1", None),
        comment("dup", "a1", 18),
        comment("dup", "a1", 18),
    ]
    threads = app.build_comment_threads(rows, top_limit=2, reply_limit=5)
    assert [parent["id"] for parent, _ in threads] == ["p1", "p2"]
    assert [(depth, reply["id"]) for depth, reply in threads[0][1]] == [
        (1, "a1"), (2, "grand1"), (3, "great"), (2, "dup"), (1, "a2")
    ]
    assert threads[1][1] == []

    rendered = app.format_comment_thread(1, *threads[0])
    assert "         ↳" in rendered
    assert rendered.index("grand1") < rendered.index("a2")
    assert "orphan" not in rendered

    assert not app.build_comment_threads(rows, 1, 0)[0][1]
    assert len(app.build_comment_threads(rows, 1, 2)[0][1]) == 2
    assert app.build_comment_threads(rows, 1, 20)[0][1][-1][1]["id"] == "unknown"


def test_oldest_nested_reply_keeps_ancestors_within_limit():
    rows = [
        comment("p", "root", 1, 100),
        comment("a", "p", 10),
        comment("b", "a", 2),
        comment("c", "b", 3),
        comment("d", "p", 4),
    ]
    threads = app.build_comment_threads(rows, 1, 2)
    assert [(depth, reply["id"]) for depth, reply in threads[0][1]] == [
        (1, "a"), (2, "b")
    ]


def test_comment_dates_are_date_only():
    assert "time unknown" in app.format_comment(comment("x", "root", None))
    rendered = app.format_comment(comment("x", "root", 1720000000))
    assert "2024-07-03" in rendered
    assert "00:00 UTC" not in rendered


def test_context_preserves_nesting_and_token_budget():
    class Encoding:
        name = "mock"
        def encode(self, value):
            return list(value)
        def decode(self, tokens):
            return "".join(tokens)

    class Console:
        def print(self, *args):
            pass

    rows = [
        comment("p", "root", 1, 100),
        comment("a", "p", 2),
        comment("b", "a", 3),
        comment("c", "b", 4),
    ]
    data = {"title": "Title", "description": "Description", "comments": rows}
    config = {"top_comments": 1, "replies_per_comment": 3, "max_context_tokens": 2000}

    with patch.object(app, "get_encoding_for_model", return_value=Encoding()):
        context = app.build_intelligent_context(data, "Transcript", config, Console())
        assert "↳ [0 likes" in context
        assert "      ↳" in context and "         ↳" in context
        assert "Transcript" in context
        assert len(context) < 2000

        config["max_context_tokens"] = 600
        context = app.build_intelligent_context(
            {**data, "title": "T", "description": "D"},
            "abc" * 300, config, Console()
        )
        assert len(context) <= 600


@pytest.mark.parametrize(
    ("extra_args", "expected_parent_limit", "expected_reply_limit"),
    [
        ([], None, 10),
        (["--top-comments", "100", "--replies-per-comment", "20"], 100, 20),
        (["--comments", "5", "--replies-per-comment", "0"], 5, 0),
    ],
)
def test_cli_limits(extra_args, expected_parent_limit, expected_reply_limit):
    parsed = app.get_parser().parse_args(["video", *extra_args])
    assert parsed.top_comments == expected_parent_limit
    assert parsed.replies_per_comment == expected_reply_limit


@pytest.mark.parametrize("invalid_args", [
    ["--top-comments", "0"],
    ["--top-comments", "-1"],
    ["--replies-per-comment", "-1"],
    ["--replies-per-comment", "abc"],
])
def test_cli_rejects_invalid_limits(invalid_args):
    with pytest.raises(SystemExit) as exc:
        app.get_parser().parse_args(["video", *invalid_args])
    assert exc.value.code == 2


@pytest.mark.parametrize(
    ("reply_limit", "expected_depth"),
    [(20, "all"), (0, "1")],
)
def test_yt_dlp_extractor_depth(reply_limit, expected_depth):
    commands = []

    def fake_run(cmd, **kwargs):
        commands.append(cmd)
        return subprocess.CompletedProcess(cmd, 0, "", "")

    with (
        patch.object(app, "resolve_yt_dlp_command", return_value=["yt-dlp"]),
        patch.object(app, "build_yt_dlp_js_runtime_args", return_value=[]),
        patch("subprocess.run", side_effect=fake_run),
    ):
        app.run_yt_dlp(
            "https://youtu.be/id", "video_id",
            comments_limit=200, replies_per_comment=reply_limit,
        )

    assert len(commands) == 1
    cmd = commands[0]
    assert "--extractor-args" in cmd
    assert cmd[cmd.index("--extractor-args") + 1] == (
        f"youtube:comment_sort=top;max_comments=all,200,all,all,{expected_depth}"
    )
