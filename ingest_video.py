"""
Video Summarizer - YouTube video analysis tool

This tool downloads YouTube metadata, subtitles, and generates AI summaries.
Accepts either a file containing YouTube URLs (one per line) or a single YouTube URL directly.
VTT subtitle files are automatically converted to clean timestamp format 
with millisecond precision ([Xs.XXXs -> Ys.YYYs] Text) for consistency
with faster-whisper transcription output.

Usage:
    python ingest_video.py <file_with_urls>           # Process URLs from file
    python ingest_video.py <youtube_url>              # Process single URL
"""
import argparse
import sys
import time
import random
from typing import Optional, Any

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="File with YouTube URLs OR a single YouTube URL")
    parser.add_argument("--comments", type=int, default=100, help="Max comments to parse")
    parser.add_argument("--all-comments", action="store_true", help="Parse ALL comments")
    parser.add_argument("--no-subtitles", action="store_true", help="Skip subtitle download and directly download audio for transcription")
    parser.add_argument("--save", choices=["meta", "video", "all"], help="Save mode: meta (metadata/transcripts only), video (video file only), all (everything)")
    return parser

def validate_config(config: dict) -> None:
    """Validate configuration and check API key availability for configured providers"""
    import os
    
    # Validate required fields
    required_fields = ['transcription_provider', 'llm_provider', 'llm_model']
    for field in required_fields:
        if field not in config:
            raise ValueError(f"{field} must be specified in config.yaml")
    
    transcription_provider = config['transcription_provider'].lower()
    llm_provider = config['llm_provider'].lower()
    
    # Validate transcription provider specific config
    if transcription_provider == 'local':
        if 'local_whisper_model' not in config:
            raise ValueError("local_whisper_model must be specified when using local transcription")
        if 'local_whisper_compute_type' not in config:
            raise ValueError("local_whisper_compute_type must be specified when using local transcription")
    elif transcription_provider in ['openai', 'groq']:
        api_key = os.environ.get(f"{transcription_provider.upper()}_API_KEY")
        if not api_key:
            raise ValueError(f"{transcription_provider.upper()}_API_KEY must be provided in config.yaml api_keys section")
    else:
        raise ValueError(f"Unknown transcription provider: {transcription_provider}. Supported: local, openai, groq")
    
    # Validate LLM provider specific config
    if llm_provider == 'ollama':
        if 'ollama_base_url' not in config:
            raise ValueError("ollama_base_url must be specified when using ollama provider")
    elif llm_provider in ['openai', 'anthropic', 'openrouter', 'groq', 'gemini', 'cerebras']:
        api_key = os.environ.get(f"{llm_provider.upper()}_API_KEY")
        if not api_key:
            raise ValueError(f"{llm_provider.upper()}_API_KEY must be provided in config.yaml api_keys section")
    else:
        pass

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

    # Load API keys into environment
    for key, value in config.get('api_keys', {}).items():
        if value:
            os.environ[key] = value
    
    # Validate configuration
    validate_config(config)
    
    return config

class Transcriber:
    def __init__(self, config):
        if 'transcription_provider' not in config:
            raise ValueError("transcription_provider must be specified in config.yaml")
        self.provider = config['transcription_provider'].lower()
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

        if 'local_whisper_model' not in self.config:
            raise ValueError("local_whisper_model must be specified in config.yaml when using local transcription")
        if 'local_whisper_compute_type' not in self.config:
            raise ValueError("local_whisper_compute_type must be specified in config.yaml when using local transcription")
        
        model_size = self.config['local_whisper_model']
        # Force CPU fallback to avoid missing cuDNN issues on systems without cuDNN
        device = 'cpu'
        compute_type = self.config['local_whisper_compute_type']
 
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
        import time
        api_key = os.environ.get(f"{self.provider.upper()}_API_KEY")
        if not api_key:
            console.print(f"[red]Error: {self.provider.upper()}_API_KEY is missing in config.[/red]")
            return "[Error: Missing API Key]"

        # Choose response_format per provider (Groq does not support 'vtt')
        if self.provider == "groq":
            resp_format = "verbose_json"
        else:
            resp_format = "vtt"

        # OpenAI client
        client = OpenAI(
            api_key=api_key, 
            base_url=base_url
        )
        
        base_label = base_url or "https://api.openai.com/v1"
        console.print(f"[yellow]Sending audio to {self.provider.upper()} API (this will take several minutes for longer videos)...[/yellow]")
        console.print(f"[dim]Transcription request &#45;> provider={self.provider}, base_url={base_label}, model={model}, response_format={resp_format}[/dim]")
        
        # Retry logic with exponential backoff
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    console.print(f"[yellow]Retry attempt {attempt + 1}/{max_retries}...[/yellow]")
                
                with open(audio_path, "rb") as file:
                    start_time = time.time()
                    transcription = client.audio.transcriptions.create(
                        model=model,
                        file=file,
                        response_format=resp_format
                    )
                    
                elapsed_time = time.time() - start_time
                console.print(f"[green]Transcription completed in {elapsed_time:.1f}s[/green]")
                break  # Success, exit retry loop
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                
                # Check if this is a retryable error
                retryable_errors = [
                    "timeout", "timeouterror", "apiconnectionerror", "apitimeouterror",
                    "serviceunavailableerror", "ratelimiterror", "502", "503", "504", "429"
                ]
                
                is_retryable = any(err in error_msg.lower() or err in error_type.lower() for err in retryable_errors)
                
                if is_retryable and attempt < max_retries - 1:
                    # Exponential backoff with jitter
                    sleep_time = (2 ** attempt) + time.time() % 1  # Add jitter
                    console.print(f"[yellow]Retryable error ({error_type}): {error_msg}[/yellow]")
                    console.print(f"[yellow]Waiting {sleep_time:.1f}s before retry...[/yellow]")
                    time.sleep(sleep_time)
                    continue
                else:
                    # Non-retryable error or final attempt
                    console.print(f"[red]Transcription API failed ({error_type}): {error_msg}[/red]")
                    if attempt == max_retries - 1:
                        console.print(f"[red]All {max_retries} attempts failed[/red]")
                    return f"[Error: API transcription failed - {error_type}]"
        else:
            # This should not happen due to the break statement, but just in case
            return "[Error: Transcription failed after all retries]"

        # Debug response type and keys (non-fatal)
        try:
            t_type = type(transcription).__name__
            preview_keys = list(transcription.keys())[:5] if isinstance(transcription, dict) else []
            console.print(f"[dim]Transcription response type={t_type}, keys={preview_keys}[/dim]")
        except Exception:
            pass

        # Normalize output to plain text for downstream
        if self.provider == "groq":
            # verbose_json expected => build timestamped lines from segments
            try:
                segments = getattr(transcription, "segments", None)
                if segments is None and isinstance(transcription, dict):
                    segments = transcription.get("segments")
                if isinstance(segments, list) and len(segments) > 0:
                    lines = []
                    for seg in segments:
                        if isinstance(seg, dict):
                            s = seg.get("start")
                            e = seg.get("end")
                            txt = (seg.get("text") or "").strip()
                        else:
                            s = getattr(seg, "start", None)
                            e = getattr(seg, "end", None)
                            txt = str(getattr(seg, "text", "")).strip()
                        if txt:
                            if isinstance(s, (int, float)) and isinstance(e, (int, float)):
                                lines.append(f"[{float(s):.3f}s -> {float(e):.3f}s] {txt}")
                            else:
                                # If start/end not provided, at least include raw text
                                lines.append(txt)
                    if lines:
                        return "\n".join(lines)
                # Fallback to plain text field
                text = getattr(transcription, "text", None)
                if not text and isinstance(transcription, dict):
                    text = transcription.get("text")
                if isinstance(text, str) and text.strip():
                    return text
            except Exception:
                pass
            # Final fallback: stringify entire response
            return str(transcription)
        else:
            return str(transcription)

def run_yt_dlp(url: str, output_template: str, save_mode: Optional[str] = None, no_subtitles: bool = False, console=None, max_retries: int = 3):
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
    
    # Subtitle handling logic
    if not no_subtitles:
        cmd.extend([
            "--write-subs",
            "--write-auto-subs",
            "--sub-lang", "en",
        ])
    
    # Video download logic based on save_mode (default: no video download for optimization)
    if save_mode in ["video", "all"]:
        # Download video file (default yt-dlp behavior)
        pass
    else:
        # Default behavior: skip video download for performance optimization
        cmd.extend(["--skip-download"])
    
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

def convert_vtt_to_clean_format(vtt_file_path: str, console) -> str:
    """
    Convert VTT subtitle file to clean transcript format with millisecond precision.
    Handles YouTube's overlapping/incremental captions by deduplicating and merging.
    
    Args:
        vtt_file_path: Path to the VTT file
        console: Rich console for output
        
    Returns:
        Formatted transcript string in the format '[Xs.XXXs -> Ys.YYYs] Text content'
        
    Raises:
        Exception: If VTT parsing fails, allowing fallback to audio transcription
    """
    try:
        import webvtt
    except ImportError as e:
        raise Exception(f"webvtt-py library not available: {e}")
    
    try:
        # Parse the VTT file
        captions = webvtt.read(vtt_file_path)
        if not captions:
            raise Exception("No captions found in VTT file")
        
        # Process captions to handle YouTube's overlapping/incremental text
        processed_segments = []
        
        for caption in captions:
            start_seconds = caption.start_in_seconds
            end_seconds = caption.end_in_seconds
            
            # Clean the text content (remove VTT markup, normalize whitespace)
            text = caption.text.strip()
            text = ' '.join(text.split())  # Normalize whitespace
            
            if text and (end_seconds - start_seconds) > 0.1:  # Filter very short segments
                processed_segments.append({
                    'start': start_seconds,
                    'end': end_seconds,
                    'text': text
                })
        
        if not processed_segments:
            raise Exception("No valid captions after filtering")
        
        # Deduplicate and merge overlapping segments
        merged_segments = _merge_overlapping_captions(processed_segments, console)
        
        # Convert to final format
        transcript_lines = []
        for segment in merged_segments:
            timestamp = f"[{segment['start']:.3f}s -> {segment['end']:.3f}s]"
            transcript_lines.append(f"{timestamp} {segment['text']}")
        
        if not transcript_lines:
            raise Exception("No valid transcript lines after processing")
            
        return '\n'.join(transcript_lines)
        
    except Exception as e:
        console.print(f"[yellow]VTT parsing failed: {e}[/yellow]")
        raise Exception(f"VTT conversion failed: {e}")

def _merge_overlapping_captions(segments: list, console) -> list:
    """
    Merge overlapping captions and deduplicate content from YouTube VTT files.
    YouTube often creates incremental captions with heavy text overlap between consecutive segments.
    """
    if not segments:
        return []
    
    merged = []
    
    for i, current in enumerate(segments):
        if i == 0:
            # First segment becomes the base
            merged.append(current.copy())
            continue
            
        # Check for text overlap with the previous merged segment
        prev_merged = merged[-1]
        current_words = current['text'].split()
        prev_words = prev_merged['text'].split()
        
        # Find overlap between end of previous and start of current
        best_overlap = 0
        overlap_start = 0
        
        # Look for the longest overlap at the boundary
        for j in range(1, min(len(prev_words), len(current_words)) + 1):
            prev_suffix = prev_words[-j:]
            current_prefix = current_words[:j]
            
            if prev_suffix == current_prefix:
                best_overlap = j
                overlap_start = j
        
        if best_overlap > 0:
            # Remove overlapping text from current segment
            unique_words = current_words[best_overlap:]
            if unique_words:  # Only add if there's unique content
                unique_text = ' '.join(unique_words)
                merged.append({
                    'start': current['start'],
                    'end': current['end'],
                    'text': unique_text
                })
            else:
                # Current segment is entirely contained in previous, extend the time
                merged[-1]['end'] = current['end']
        else:
            # No overlap, add as new segment
            merged.append(current.copy())
    
    # Filter out very short or empty segments
    final_merged = []
    for segment in merged:
        text = segment['text'].strip()
        duration = segment['end'] - segment['start']
        
        if text and duration > 0.5:  # Must have text and be at least 0.5s
            final_merged.append(segment)
    
    console.print(f"[blue]Processed {len(segments)} captions into {len(final_merged)} clean segments[/blue]")
    return final_merged

def get_transcript(base_name: str, url: str, config: dict, console, no_subtitles: bool = False, save_mode: Optional[str] = None) -> str:
    import glob, os
    if not no_subtitles:
        vtt_files = glob.glob(f"{base_name}*.vtt")
        if vtt_files:
            console.print(f"[green]Subtitle file found: {os.path.basename(vtt_files[0])}[/green]")
            try:
                # Use VTT converter for clean formatting with millisecond precision
                transcript = convert_vtt_to_clean_format(vtt_files[0], console)
                console.print("[green]VTT file successfully converted to clean format[/green]")
                return transcript
            except Exception as e:
                # Fallback to audio transcription if VTT conversion fails
                console.print(f"[yellow]VTT processing failed, falling back to audio transcription: {e}[/yellow]")
                # Continue to audio transcription workflow below

    console.print("[yellow]Initiating transcription workflow...")
    audio_path = download_audio(url, base_name, console)
    if audio_path:
        transcriber = Transcriber(config)
        transcript = transcriber.transcribe(audio_path, console)
        
        # Save transcript to file based on save_mode
        if save_mode in ["meta", "all"]:
            transcript_path = f"{base_name}_transcript.txt"
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(transcript)
            console.print(f"[green]Transcript saved to {transcript_path}[/green]")

        # Clean up audio file (unless save_mode="all")
        if save_mode != "all" and os.path.exists(audio_path):
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
    if 'llm_provider' not in config:
        raise ValueError("llm_provider must be specified in config.yaml")
    if 'llm_model' not in config:
        raise ValueError("llm_model must be specified in config.yaml")
    
    provider = config['llm_provider']
    model = config['llm_model']
    custom_api_base = config.get('ollama_base_url')
    if provider == "ollama":
        if not custom_api_base:
            raise ValueError("ollama_base_url must be specified in config.yaml when using ollama provider")
        model_id = f"ollama/{model}"
        api_base = custom_api_base
    else:
        model_id = f"{provider}/{model}"
        api_base = None

    system_prompt = """<persona>
You are a Skeptical Content Archivist and Objective Observer. Your goal is to create a neutral, high-utility record of the video content.
You prioritize accuracy over hype. You strictly distinguish between "observable facts" (what is shown) and "subjective claims" (what the speaker argues).
</persona>

<input_data>
You will receive a raw text dump containing:
1. Video Title & Description
2. Transcript (Time-coded: [start -> end] Text)
3. Top Comments (with like counts)
</input_data>

<processing_rules>
1. **Attribution Anchoring (CRITICAL)**: Never state subjective metrics as absolute facts.
   - *Bad:* "The tool is 10x faster than the competition."
   - *Good:* "The creator argues the tool is 10x faster, demonstrating a side-by-side comparison."
   - Use attribution verbs: "Claims," "Argues," "Suggests," "Demonstrates," "Opinions."

2. **Timestamp Integration**: For every "Key Insight," you MUST cite the approximate timestamp `(Time: MM:SS)` from the transcript where the point is discussed.

3. **Community Synthesis**: Look beyond just disputes. Identify "Additive Context" (users providing tips, workarounds, or alternative tools mentioned in comments).
</processing_rules>

<output_format>
You MUST strictly follow this Markdown structure. Do not output anything else.

### Video Content Summary
[A dense, cohesive paragraph summarizing the video's narrative and purpose. Use objective language. roughly 150-250 words.]

### Key Insights
[Bullet points highlighting high-value takeaways. MUST include timestamps.]
- **[Concept Name]** (Time: [MM:SS]): [Explanation with attribution to the speaker].
- **[Concept Name]** (Time: [MM:SS]): [Explanation with attribution to the speaker].

### Detailed Breakdown
[A dynamic table adapted to the video's domain. Choose the best columns for the content type.]

*Logic for Table:*
- If **Software/Tech**: Columns = | Aspect | Details | (Focus on specs, tools, performance claims)
- If **Tutorial/How-To**: Columns = | Step/Phase | Action | (Focus on the process)
- If **Review/Product**: Columns = | Feature | Verdict | (Focus on pros/cons)
- If **News/Commentary**: Columns = | Topic | Claim/Fact | (Focus on arguments)
- If **Creative/Art**: Columns = | Element | Description | (Focus on style, composition)

| [Col 1] | [Col 2] |
|---------|---------|
| [Row 1] | [Row 1] |
| [Row 2] | [Row 2] |

### Community Intelligence
**Overall**: [Summary of the general mood: Positive, Negative, or Mixed. Mention the approximate ratio.]

**Positive Highlights**:
- [Theme]: [Quote or summary] (approx [X] likes)

**Criticisms/Negatives**:
- [Theme]: [Quote or summary] (approx [X] likes)

**Community Knowledge (Corrections, Disputes, & Tips)**
*(Only include this subsection if applicable. If no valid data exists, omit it.)*
- **[Correction/Dispute]**: [User Name] disputes the claim that [X], noting [Y].
- **[Additive Tip]**: [User Name] suggests a workaround for [Problem] using [Tool/Method].
</output_format>
"""

    messages = [
        {"role": "system", "content": system_prompt},
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

def cleanup_files(base_name: str, save_mode: Optional[str], console) -> None:
    """Clean up files based on save mode"""
    if save_mode == "all":
        # Keep everything
        return
    
    import glob
    import os
    
    def _remove_files(patterns: list):
        """Helper function to remove files matching patterns"""
        for pattern in patterns:
            files = glob.glob(pattern)
            for file_path in files:
                # Don't remove the summary file
                if file_path.startswith("SUMMARY_"):
                    continue
                try:
                    os.remove(file_path)
                except (PermissionError, FileNotFoundError, OSError) as e:
                    console.print(f"[red]Error removing {file_path}: {e}[/red]")
    
    if not save_mode:
        # Default: clean up everything except summary
        patterns_to_clean = [
            f"{base_name}*.info.json",
            f"{base_name}*.vtt",
            f"{base_name}_transcript.txt", 
            f"{base_name}*.comments.json",
            f"{base_name}",     # Video file without extension
            f"{base_name}.*"    # Other files with extensions
        ]
        _remove_files(patterns_to_clean)
        
    elif save_mode == "meta":
        # Keep: .info.json, .vtt, _transcript.txt, .comments.json
        # Remove: video files
        patterns_to_clean = [
            f"{base_name}",         # Video file without extension
            f"{base_name}.mp4",     # Common video extensions
            f"{base_name}.webm", 
            f"{base_name}.mkv",
            f"{base_name}.avi",
            f"{base_name}.m4a",
            f"{base_name}.mp3",
            f"{base_name}.opus"
        ]
        _remove_files(patterns_to_clean)
        
    elif save_mode == "video":
        # Keep: video file only  
        # Remove: everything else
        patterns_to_clean = [
            f"{base_name}*.info.json",
            f"{base_name}*.vtt",
            f"{base_name}_transcript.txt",
            f"{base_name}*.comments.json"
        ]
        _remove_files(patterns_to_clean)

def main(args):
    import os, json, glob, time, re
    try:
        from rich.console import Console
    except Exception:
        Console = None

    class _FallbackConsole:
        def print(self, *args, **kwargs):
            print(*args, **kwargs)
        def rule(self, *args, **kwargs):
            print(*args, **kwargs)

    def extract_video_id(url):
        """
        Extract YouTube video ID from various URL formats.
        
        Handles:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID
        - URLs with tracking parameters (?si=...&list=...)
        
        Returns the clean video ID (11 characters, alphanumeric + hyphens/underscores)
        """
        # Remove any whitespace
        url = url.strip()
        
        # Pattern for youtu.be/VIDEO_ID format
        youtu_be_match = re.search(r'youtu\.be/([a-zA-Z0-9_-]{11})', url)
        if youtu_be_match:
            return youtu_be_match.group(1)
        
        # Pattern for youtube.com/watch?v=VIDEO_ID format
        youtube_watch_match = re.search(r'[?&]v=([a-zA-Z0-9_-]{11})', url)
        if youtube_watch_match:
            return youtube_watch_match.group(1)
        
        # Fallback: try the old method for backward compatibility
        if 'v=' in url:
            return url.split('v=')[1].split('&')[0][:11]
        
        # If no pattern matches, return None to indicate invalid URL
        return None

    def is_youtube_url(input_str):
        """Check if input string is a YouTube URL"""
        return ('youtube.com' in input_str or 'youtu.be' in input_str) and ('http' in input_str)

    console = Console() if Console else _FallbackConsole()
    
    # Start timing the entire script execution
    script_start_time = time.time()

    config = load_config()

    # Determine if input is a file or a direct YouTube URL
    if is_youtube_url(args.input):
        # Direct YouTube URL provided
        urls = [args.input]
        console.print(f"[blue]Processing single URL: {args.input}[/blue]")
    else:
        # File path provided - check if it exists
        if not os.path.exists(args.input):
            # Check if it might be a malformed URL
            if 'http' in args.input:
                console.print(f"[red]Invalid YouTube URL: {args.input}[/red]")
                console.print("[yellow]URLs must contain 'youtube.com' or 'youtu.be'[/yellow]")
                return
            else:
                console.print(f"[red]Input file not found: {args.input}[/red]")
                return

        with open(args.input, 'r') as f:
            urls = [l.strip() for l in f if l.strip()]
        
        console.print(f"[blue]Processing {len(urls)} URLs from file: {args.input}[/blue]")

    for url in urls:
        video_id = extract_video_id(url)
        
        if not video_id:
            console.print(f"[red]Error: Could not extract video ID from URL: {url}[/red]")
            continue
            
        base_name = f"video_{video_id}"
        console.rule(f"[bold green]Processing {video_id}")

        try:
            run_yt_dlp(url, base_name, args.save, args.no_subtitles, console)
        except Exception as e:
            console.print(f"[red]yt-dlp failed after all retries: {e}[/red]")
            continue

        json_path = glob.glob(f"{base_name}*.info.json")[0]
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        transcript = get_transcript(base_name, url, config, console, args.no_subtitles, args.save)
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

        # Clean up intermediate files based on save mode
        cleanup_files(base_name, args.save, console)

        console.print(f"[bold green]Done! Saved to {out_name}[/bold green]")

    # End timing and display total execution time
    script_end_time = time.time()
    total_duration = script_end_time - script_start_time
    minutes, seconds = divmod(total_duration, 60)
    console.print(f"\n[bold blue]Script completed in {int(minutes):02d}:{seconds:05.2f}[/bold blue]")

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    main(args)