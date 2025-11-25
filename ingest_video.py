import argparse
import sys
import time
import random
from typing import Optional, Any

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="File with YouTube URLs")
    parser.add_argument("--comments", type=int, default=100, help="Max comments to parse")
    parser.add_argument("--all-comments", action="store_true", help="Parse ALL comments")
    parser.add_argument("--no-subtitles", action="store_true", help="Skip subtitle download and directly download audio for transcription")
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
        # Force CPU fallback to avoid missing cuDNN issues on systems without cuDNN
        device = 'cpu'
        compute_type = self.config.get('local_whisper_compute_type', 'float32')
 
        console.print(f"[yellow]Loading faster-whisper model: {model_size} on {device} ({compute_type})...[/yellow]")
        
        # Check if the file is a video format and inform user
        import os
        file_ext = os.path.splitext(audio_path)[1].lower()
        if file_ext in ['.webm', '.mp4', '.mkv', '.avi']:
            console.print(f"[dim]Note: Using video file ({file_ext}) for audio transcription[/dim]")
        
        try:
            model = WhisperModel(model_size, device=device, compute_type=compute_type)
            console.print(f"[yellow]Transcribing audio (this may take 1-2 minutes for longer videos)...[/yellow]")
            
            # Add progress indication
            import time
            start_time = time.time()
            segments, info = model.transcribe(audio_path, beam_size=5)
            
            console.print(f"[dim]Detected language: {info.language} (probability {info.language_probability:.2f})[/dim]")
            console.print(f"[yellow]Processing transcription segments...[/yellow]")
            
            output = []
            segment_count = 0
            for segment in segments:
                start = int(segment.start)
                end = int(segment.end)
                text = segment.text.strip()
                output.append(f"[{start}s -> {end}s] {text}")
                segment_count += 1
                
                # Show progress every 50 segments
                if segment_count % 50 == 0:
                    elapsed = time.time() - start_time
                    console.print(f"[dim]Processed {segment_count} segments ({elapsed:.1f}s elapsed)...[/dim]")
            
            total_time = time.time() - start_time
            console.print(f"[green]Transcription completed: {segment_count} segments in {total_time:.1f}s[/green]")
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

def run_yt_dlp(url: str, output_template: str, no_subtitles: bool = False, console=None, max_retries: int = 3):
    """Run yt-dlp with robust error handling and retry logic"""
    import subprocess
    
    # Base command with enhanced reliability options
    cmd = [
        "yt-dlp",
        "--write-info-json",
        "--write-comments",
        "--remote-components", "ejs:github",  # Enable JavaScript challenge solving
        "--retries", "3",
        "--fragment-retries", "3",
        "--extractor-retries", "3",
        "--retry-sleep", "linear=1:5",
        "--no-check-certificates",  # Avoid SSL issues
        "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    ]
    
    if not no_subtitles:
        cmd.extend([
            "--write-subs",
            "--write-auto-subs",
            "--sub-lang", "en",
        ])
    else:
        cmd.extend([
            "--skip-download",
        ])
    
    cmd.extend([
        "--output", output_template,
        url
    ])
    
    last_error = None
    for attempt in range(max_retries):
        try:
            if console and attempt > 0:
                console.print(f"[yellow]Retry attempt {attempt + 1}/{max_retries}...[/yellow]")
            
            # Run with timeout to prevent hanging
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                check=True, 
                timeout=300,  # 5 minute timeout
                text=True
            )
            return result  # Success
            
        except subprocess.TimeoutExpired as e:
            last_error = f"Command timed out after 5 minutes: {e}"
            if console:
                console.print(f"[red]Timeout on attempt {attempt + 1}: {last_error}[/red]")
                
        except subprocess.CalledProcessError as e:
            error_output = e.stderr if e.stderr else e.stdout if e.stdout else "No error output"
            last_error = f"Command failed with exit code {e.returncode}: {error_output}"
            
            if console:
                console.print(f"[red]Error on attempt {attempt + 1}: {last_error}[/red]")
            
            # Check for specific error patterns that might be retryable
            if any(pattern in error_output.lower() for pattern in [
                "network", "timeout", "connection", "temporary", "rate limit", 
                "503", "502", "429", "throttling", "unavailable"
            ]):
                if attempt < max_retries - 1:
                    # Exponential backoff with jitter
                    sleep_time = (2 ** attempt) + random.uniform(0, 1)
                    if console:
                        console.print(f"[yellow]Retryable error detected, sleeping {sleep_time:.1f}s before retry...[/yellow]")
                    time.sleep(sleep_time)
                    continue
            
            # For non-retryable errors or final attempt, break immediately
            break
            
        except Exception as e:
            last_error = f"Unexpected error: {e}"
            if console:
                console.print(f"[red]Unexpected error on attempt {attempt + 1}: {last_error}[/red]")
            break
    
    # If we get here, all attempts failed
    raise subprocess.CalledProcessError(
        1, 
        cmd, 
        output=None, 
        stderr=f"All {max_retries} attempts failed. Last error: {last_error}"
    )

def download_audio(url: str, output_template: str, console=None) -> Optional[str]:
    import os, subprocess, glob
    
    # Look for existing audio/video files first (including webm which can contain audio)
    audio_extensions = ['*.mp3', '*.m4a', '*.aac', '*.opus', '*.webm', '*.mp4', '*.mkv']
    for ext in audio_extensions:
        candidates = glob.glob(f"{output_template}{ext}")
        if candidates:
            if console:
                console.print(f"[green]Found existing media file for transcription: {candidates[0]}[/green]")
            return candidates[0]
    
    # Strategy 1: Try to download audio-only format without conversion
    if console:
        console.print("[yellow]Attempting audio-only download (no conversion)...[/yellow]")
    
    cmd_audio_only = [
        "yt-dlp",
        "-f", "bestaudio[ext=m4a]/bestaudio[ext=mp3]/bestaudio[ext=opus]/bestaudio[ext=aac]/bestaudio",
        "--remote-components", "ejs:github",
        "--retries", "3",
        "--fragment-retries", "3",
        "--no-check-certificates",
        "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "--output", f"{output_template}.%(ext)s",
        url
    ]
    
    try:
        result = subprocess.run(
            cmd_audio_only, 
            capture_output=True, 
            check=True, 
            timeout=600,  # 10 minute timeout
            text=True
        )
        
        # Find the downloaded audio file
        for ext in audio_extensions:
            candidates = glob.glob(f"{output_template}{ext}")
            if candidates:
                if console:
                    console.print(f"[green]Audio downloaded: {candidates[0]}[/green]")
                return candidates[0]
                
    except subprocess.CalledProcessError as e:
        if console:
            console.print(f"[yellow]Audio-only download failed, trying video download...[/yellow]")
    except subprocess.TimeoutExpired:
        if console:
            console.print("[red]Audio download timed out[/red]")
        return None
    except Exception as e:
        if console:
            console.print(f"[yellow]Audio download error: {e}, trying video download...[/yellow]")
    
    # Strategy 2: Download video file (which often contains usable audio track)
    if console:
        console.print("[yellow]Downloading video file for audio extraction...[/yellow]")
    
    cmd_video = [
        "yt-dlp",
        "-f", "worst[height<=720]/worst",  # Get smaller video file to save bandwidth
        "--remote-components", "ejs:github",
        "--retries", "3",
        "--fragment-retries", "3",
        "--no-check-certificates",
        "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "--output", f"{output_template}.%(ext)s",
        url
    ]
    
    try:
        result = subprocess.run(
            cmd_video, 
            capture_output=True, 
            check=True, 
            timeout=600,
            text=True
        )
        
        # Find the downloaded video file
        for ext in audio_extensions:
            candidates = glob.glob(f"{output_template}{ext}")
            if candidates:
                if console:
                    console.print(f"[green]Video file downloaded for transcription: {candidates[0]}[/green]")
                return candidates[0]
        
        if console:
            console.print("[yellow]No media file found after download[/yellow]")
        return None
        
    except subprocess.TimeoutExpired:
        if console:
            console.print("[red]Video download timed out[/red]")
        return None
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else str(e)
        if console:
            console.print(f"[red]Video download failed: {error_msg}[/red]")
        return None
    except Exception as e:
        if console:
            console.print(f"[red]Unexpected download error: {e}[/red]")
        return None

def get_transcript(base_name: str, url: str, config: dict, console, no_subtitles: bool = False) -> str:
    import glob, os
    if not no_subtitles:
        vtt_files = glob.glob(f"{base_name}*.vtt")
        if vtt_files:
            console.print(f"[green]Subtitle file found: {os.path.basename(vtt_files[0])}[/green]")
            with open(vtt_files[0], 'r', encoding='utf-8') as f:
                lines = [l for l in f.readlines() if "WEBVTT" not in l and l.strip()]
                return "".join(lines)

    console.print("[yellow]Initiating transcription workflow...[/yellow]")
    audio_path = download_audio(url, base_name, console)
    if audio_path:
        transcriber = Transcriber(config)
        transcript = transcriber.transcribe(audio_path, console)
        
        # Save transcript to file
        transcript_path = f"{base_name}_transcript.txt"
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript)
        console.print(f"[green]Transcript saved to {transcript_path}[/green]")

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
            run_yt_dlp(url, base_name, args.no_subtitles, console)
        except Exception as e:
            console.print(f"[red]yt-dlp failed after all retries: {e}[/red]")
            continue

        json_path = glob.glob(f"{base_name}*.info.json")[0]
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        transcript = get_transcript(base_name, url, config, console, args.no_subtitles)
        comments_text = process_comments(data, args.comments, args.all_comments)

        context = f"""TITLE: {data.get('title')}
DESCRIPTION:
{data.get('description')}

TRANSCRIPT:
{transcript[:50000]}
... (truncated if too long)

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