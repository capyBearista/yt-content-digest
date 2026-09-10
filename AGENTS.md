# YouTube Video Digest Instructions

## Project Shape

This is a single-file Python application. Keep application logic in
`ingest_video.py`; do not split it into a package unless the task requires it.
The file is organized as utilities, provider/transcription classes, pipeline
helpers, and `main()` near the bottom.

The pipeline is:

1. Accept a URL, playlist, channel, or file of inputs.
2. Use `yt-dlp` to fetch metadata, comments, and subtitles.
3. Prefer downloaded VTT subtitles; fall back to audio-only download, then a
	 small video download, then transcription.
4. Assemble title, description, transcript, and comments into an LLM context.
5. Generate a Markdown summary with the analysis and raw context.

## Implementation Rules

### Input and batching

- Preserve support for direct video URLs, playlists, channel handles, channel
	IDs, channel URLs, and mixed URL files.
- `classify_url()` returns `video`, `playlist`, or `channel` plus a normalized
	URL. Channel URLs are pointed at `/videos`, but returned entries are not
	independently guaranteed to exclude every Short or live video.
- Handle each video in isolation. A failure should be recorded and allow the
	rest of a batch to continue.

### Context construction

- `build_intelligent_context()` uses `tiktoken`, a 500-token safety buffer, and
	provider/model heuristics to allocate space.
- The normal priority is title and description, the configured minimum number
	of comments, then transcript. `--all-comments` requests all available
	comments and prioritizes comments over transcript.
- Do not describe the token limit as an absolute guarantee without fixing the
	implementation: oversized title/description fields and minimum comments can
	exceed the configured budget.
- YouTube may return fewer comments than requested because of API pagination
	limits.

### Transcription

- Keep the subtitle-first fallback chain and VTT cleanup/overlap merging.
- `Transcriber` supports `local`, `openai`, and `groq` transcription.
- Local transcription currently forces `device="cpu"`; the
	`local_whisper_device` config value is validated/documented but ignored.
	Do not claim CUDA support unless the implementation changes too.
- API transcription has retry/backoff handling. Local Whisper processing does
	not have a timeout.
- `ffmpeg` is an external runtime dependency for reliable media extraction and
	conversion, even though some direct downloads can work without it.

### Configuration and providers

- `config.yaml` is local runtime configuration and is ignored by Git. Never
	commit API keys, cookies, or other credentials. Prefer environment variables
	or ignored local config for secrets.
- `load_config()` injects non-empty `api_keys` values into `os.environ` and
	validates required fields: `transcription_provider`, `llm_provider`, and
	`llm_model`.
- Implemented transcription providers are `local`, `openai`, and `groq`.
	The recognized LLM providers are `ollama`, `openai`, `anthropic`,
	`openrouter`, `groq`, `gemini`, and `cerebras`; LiteLLM supports more, but
	that broader catalog is not automatically supported by this application.
- The active provider/model and context size come from `config.yaml`; do not
	assume the example config matches a user's local config.

### yt-dlp access

- Cookie paths may be supplied with `--cookies` or `yt_dlp_cookies`.
- YouTube bot checks require a fresh Netscape cookie export from an authenticated
	browser. Do not print cookie contents or commit `cookies.txt`.
- yt-dlp uses the EJS remote component `ejs:github` and looks for `node`,
	`deno`, or `bun` to solve YouTube JavaScript challenges. A stale challenge
	solver cache can require `yt-dlp --rm-cache-dir` before retrying.
- Keep yt-dlp current. Use the official yt-dlp documentation linked in
	`docs/RESOURCES.md` for extractor, cookie, EJS, and format changes.

### Output and cleanup

- Direct videos produce `SUMMARY_{video_id}.md`.
- Playlist and channel inputs produce `PLAYLIST_{id}/` or
	`CHANNEL_{username}/` directories, summary files, and collection metadata.
- Temporary files are directory-qualified, for example
	`PLAYLIST_{id}/video_{video_id}.*`.
- Default cleanup removes downloaded metadata, subtitles, transcripts,
	comments, and media, leaving the summary. `--save meta` keeps metadata and
	transcript artifacts while removing media; `--save video` keeps media while
	removing metadata artifacts; `--save all` keeps everything.

## Development Workflow

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Activation is optional when using `.venv/bin/python` directly. Before claiming
an implementation change works, run the narrowest relevant checks available:

```bash
.venv/bin/python -m compileall -q ingest_video.py
.venv/bin/python ingest_video.py --help
```

For yt-dlp changes, also perform a metadata-only smoke test with a valid URL,
fresh cookies when required, `--remote-components ejs:github`, and no media
download. There is currently no repository test suite, linter, or typechecker.

## Reference Files

- `ingest_video.py`: application logic and CLI.
- `config.yaml`: ignored local configuration; never treat it as committed
	project defaults.
- `example.config.yaml`: tracked configuration template.
- `requirements.txt`: eight Python dependencies; `ffmpeg` is installed outside
	pip.
- `docs/RESOURCES.md`: official references for yt-dlp, faster-whisper, and
	LiteLLM. Consult it before changing integrations.