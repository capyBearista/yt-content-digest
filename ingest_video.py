import argparse
import sys
from typing import Optional, Any

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="File with YouTube URLs")
    parser.add_argument("--comments", type=int, default=100, help="Max comments to parse")
    parser.add_argument("--all-comments", action="store_true", help="Parse ALL comments")
    return parser

def load_config(config_path="config.yaml"):
    import os
    try:
        import yaml
    except Exception:
        yaml = None

    if yaml is None:
        print("Error: PyYAML is not installed. Cannot read config.yaml.")
        sys.exit(1)

    if not os.path.exists(config_path):
        print(f"Error: {config_path} not found. Please create one.")
        sys.exit(1)

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    for key, value in config.get('api_keys', {}).items():
        if value:
            os.environ[key] = value
    return config

class Transcriber:
    def __init__(self, config):
        self.provider = config.get('transcription_provider', 'local').lower()
        self.config = config

    def transcribe(self, audio_path: str, console) -> str:
        if self.provider == "local":
            return self._transcribe_local(audio_path, console)
        elif self.provider == "openai":
            return self._transcribe_api(audio_path, console, base_url=None, model="whisper-1")
        elif self.provider == "groq":
            return self._transcribe_api(audio_path, console, base_url="https://api.groq.com/openai/v1", model="whisper-large-v3")
        else:
            raise ValueError(f"Unknown transcription provider: {self.provider}")

    def _transcribe_local(self, audio_path: str, console) -> str:
        try:
            from faster_whisper import WhisperModel
        except Exception as e:
            console.print(f"[red]faster-whisper not available: {e}[/red]")
            return "[Error: faster-whisper missing]"

        model_size = self.config.get('local_whisper_model', 'base')
        device = self.config.get('local_whisper_device', 'auto')
        compute_type = self.config.get('local_whisper_compute_type', 'int8')

        console.print(f"[yellow]Loading faster-whisper model: {model_size} on {device} ({compute_type})...[/yellow]")
        try:
            model = WhisperModel(model_size, device=device, compute_type=compute_type)
            segments, info = model.transcribe(audio_path, beam_size=5)
            console.print(f"[dim]Detected language: {info.language} (probability {info.language_probability:.2f})[/dim]")
            output = []
            for segment in segments:
                start = int(segment.start)
                end = int(segment.end)
                text = segment.text.strip()
                output.append(f"[{start}s -> {end}s] {text}")
            return "\n".join(output)
        except Exception as e:
            console.print(f"[red]Local transcription failed: {e}[/red]")
            return "[Error during local transcription]"

    def _transcribe_api(self, audio_path: str, console, base_url: Optional[str], model: str) -> str:
        try:
            from openai import OpenAI
        except Exception as e:
            console.print(f"[red]openai SDK not available: {e}[/red]")
            return "[Error: openai SDK missing]"
    
        import os
        api_key = os.environ.get(f"{self.provider.upper()}_API_KEY")
        if not api_key:
            console.print(f"[red]Error: {self.provider.upper()}_API_KEY is missing in config.[/red]")
            return "[Error: Missing API Key]"
    
        # OpenAI client accepts None for base_url in many SDKs; pass through safely
        client = OpenAI(api_key=api_key, base_url=base_url)
        console.print(f"[yellow]Sending audio to {self.provider.upper()} API...[/yellow]")
        with open(audio_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                model=model,
                file=file,
                response_format="vtt"
            )
        return str(transcription)

def run_yt_dlp(url: str, output_template: str):
    import subprocess
    cmd = [
        "yt-dlp",
        "--write-info-json",
        "--write-comments",
        "--write-subs",
        "--write-auto-subs",
        "--sub-lang", "en",
        "--skip-download",
        "--output", output_template,
        url
    ]
    subprocess.run(cmd, capture_output=True, check=True)

def download_audio(url: str, output_template: str) -> Optional[str]:
    import os, subprocess
    audio_file = f"{output_template}.mp3"
    if os.path.exists(audio_file):
        return audio_file
    cmd = [
        "yt-dlp",
        "-x", "--audio-format", "mp3",
        "--output", output_template,
        url
    ]
    try:
        subprocess.run(cmd, capture_output=True, check=True)
        return audio_file
    except subprocess.CalledProcessError:
        return None

def get_transcript(base_name: str, url: str, config: dict, console) -> str:
    import glob, os
    vtt_files = glob.glob(f"{base_name}*.vtt")
    if vtt_files:
        console.print(f"[green]Subtitle file found: {os.path.basename(vtt_files[0])}[/green]")
        with open(vtt_files[0], 'r', encoding='utf-8') as f:
            lines = [l for l in f.readlines() if "WEBVTT" not in l and l.strip()]
            return "".join(lines)

    if config.get('download_audio_if_missing_subs', True):
        console.print("[yellow]No subtitles found. Initiating transcription workflow...[/yellow]")
        audio_path = download_audio(url, base_name)
        if audio_path:
            transcriber = Transcriber(config)
            transcript = transcriber.transcribe(audio_path, console)
            if os.path.exists(audio_path):
                os.remove(audio_path)
            return transcript
    return "[No transcript available]"

def process_comments(data: dict, limit: int, fetch_all: bool) -> str:
    comments = data.get('comments', [])
    if not comments:
        return "No comments found."
    comments.sort(key=lambda x: x.get('like_count', 0) or 0, reverse=True)
    count = len(comments) if fetch_all else min(limit, len(comments))
    selected = comments[:count]
    out = []
    for i, c in enumerate(selected):
        user = c.get('author', 'Anon')
        text = c.get('text', '').replace('\n', ' ')
        likes = c.get('like_count', 0)
        out.append(f"{i+1}. [{likes} likes] {user}: {text}")
    return "\n".join(out)

def generate_summary(context: str, config: dict, console) -> str:
    provider = config.get('llm_provider', 'ollama')
    model = config.get('llm_model', 'llama3')
    custom_api_base = config.get('ollama_base_url', "http://localhost:11434")
    if provider == "ollama":
        model_id = f"ollama/{model}"
        api_base = custom_api_base
    else:
        model_id = f"{provider}/{model}"
        api_base = None

    messages = [
        {"role": "system", "content": "You are an expert analyst. Summarize the video content, extracting key insights, technical details, and community sentiment from the comments."},
        {"role": "user", "content": context}
    ]

    try:
        from litellm import completion
    except Exception:
        console.print("[red]litellm not installed; skipping LLM call.[/red]")
        return "[LLM unavailable: litellm package missing]"

    console.print(f"[blue]Requesting summary from {model_id}...[/blue]")
    try:
        response = completion(model=model_id, messages=messages, api_base=api_base)
        # Safely extract content from different response shapes (object-like or dict-like)
        try:
            # object-like (e.g., response.choices[0].message.content)
            choices = getattr(response, "choices", None)
            if choices and len(choices) > 0:
                first = choices[0]
                msg = getattr(first, "message", None)
                if msg:
                    content = getattr(msg, "content", None)
                    if isinstance(content, str):
                        return content
            # dict-like
            if isinstance(response, dict):
                choices = response.get("choices")
                if choices and isinstance(choices, list) and len(choices) > 0:
                    first = choices[0]
                    if isinstance(first, dict):
                        msg = first.get("message") or {}
                        content = msg.get("content")
                        if isinstance(content, str):
                            return content
        except Exception:
            pass
        return str(response)
    except Exception as e:
        return f"LLM Error: {str(e)}"

def main(args):
    import os, json, glob
    try:
        from rich.console import Console
    except Exception:
        Console = None

    class _FallbackConsole:
        def print(self, *args, **kwargs):
            print(*args, **kwargs)
        def rule(self, *args, **kwargs):
            print(*args, **kwargs)

    console = Console() if Console else _FallbackConsole()

    config = load_config()

    if not os.path.exists(args.input_file):
        console.print("[red]Input file not found.[/red]")
        return

    with open(args.input_file, 'r') as f:
        urls = [l.strip() for l in f if l.strip()]

    for url in urls:
        video_id = url.split("v=")[-1].split("&")[0]
        base_name = f"video_{video_id}"
        console.rule(f"[bold green]Processing {video_id}")

        try:
            run_yt_dlp(url, base_name)
        except Exception as e:
            console.print(f"[red]yt-dlp failed: {e}[/red]")
            continue

        json_path = glob.glob(f"{base_name}*.info.json")[0]
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        transcript = get_transcript(base_name, url, config, console)
        comments_text = process_comments(data, args.comments, args.all_comments)

        context = f"""TITLE: {data.get('title')}
DESCRIPTION: {data.get('description')}
TRANSCRIPT:
{transcript[:50000]} ... (truncated if too long)

COMMENTS:
{comments_text}
"""

        summary = generate_summary(context, config, console)

        out_name = f"SUMMARY_{video_id}.md"
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(summary + "\n\n" + "="*30 + "\nRAW DATA\n" + "="*30 + "\n" + context)

        console.print(f"[bold green]Done! Saved to {out_name}[/bold green]")

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    main(args)