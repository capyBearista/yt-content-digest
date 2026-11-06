# YouTube Content Digestion

Hey there! 👋

This is a simple-ish Python tool I built to help analyze YouTube content without having to watch every single video. It downloads video metadata, transcribes audio (or uses existing subtitles), and generates structured AI summaries with community insights from top comments. Think of it as your personal research assistant for YouTube rabbit holes.

### Why This Exists

I got tired of bookmarking dozens of YouTube videos that I'd never watch, or spending an hour on a video that could've been summarized in 5 minutes. This tool lets me quickly digest content from videos, playlists, or entire channels – all while keeping the flexibility to choose which AI providers I want to use (local or cloud, free or paid).

Plus, I wanted something that could scale up to more interesting analysis tasks in the future. Right now it's a video summarizer, but the foundation is here for some cool stuff down the line (more on that later!).

## What It Does Right Now

- **Process YouTube content flexibly**: Single videos, playlists, entire channels, or a mix of all three
- **Smart transcription pipeline**: Uses existing subtitles when available, falls back to audio transcription when needed
- **Multi-provider support**: Works with 100+ LLM providers via LiteLLM (OpenAI, Gemini, Groq, Ollama, etc.)
- **Intelligent context building**: Token-aware assembly that prioritizes the title, description, like-ranked top-level comments with chronological replies, and transcript
- **Batch processing**: Queue up multiple URLs and let it run

### Key Features

✨ **Input Flexibility**
```bash
python ingest_video.py urls.txt                              # File with URLs
python ingest_video.py "https://youtube.com/watch?v=..."     # Single video
python ingest_video.py @LinuxfoundationOrg                   # Channel username
python ingest_video.py UCfX55Sx5hEFjoC3cNs6mCUQ              # Channel ID
python ingest_video.py "https://youtube.com/playlist?list=..." # Playlist
```

✨ **Provider Agnostic**
- **Transcription**: Local (faster-whisper), OpenAI, Groq
- **Summarization**: Ollama (free/local), OpenAI, Gemini, OpenRouter, Groq, Cerebras

✨ **Organized Output**
```
SUMMARY_videoID.md              # Individual video summaries
PLAYLIST_playlistID/            # Playlist collection with info file
  ├── SUMMARY_video1.md
  ├── SUMMARY_video2.md
  └── PLAYLIST_playlistID_INFO.md
CHANNEL_username/               # Channel collection with info file
  ├── SUMMARY_video1.md
  ├── SUMMARY_video2.md
  └── CHANNEL_username_INFO.md
```

## Getting Started

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) for Python and dependency management.
- Python 3.12 (recommended; `uv` can install it automatically).
- `ffmpeg` for audio extraction and transcription fallback.
- API credentials for your chosen cloud provider, or a running local LLM provider such as Ollama.

### Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/capyBearista/yt-content-digest.git
   cd yt-content-digest
   ```

2. **Create a virtual environment**
   ```bash
   uv python install 3.12
   uv venv --python 3.12 .venv
   ```

3. **Install dependencies**
   ```bash
   uv pip install --python .venv/bin/python -r requirements.txt
   ```

4. **Configure the application**
   ```bash
   cp example.config.yaml config.yaml
   ```

   Edit `config.yaml` to select your transcription provider, LLM provider, model, and any required API keys. Do not overwrite an existing configuration containing your settings.

5. **Run the application**
   ```bash
   .venv/bin/python ingest_video.py "https://youtu.be/kyK-MKRLRLk"
   ```

   Activation is unnecessary when calling the virtual environment's Python directly.

   **Windows:** Use `.venv\Scripts\python.exe` instead of `.venv/bin/python`.
   **Alternative:** A standard Python virtual environment with `pip` also works, but install dependencies into the same environment used to run the application. Avoid system-wide `pip` installations.

### Configuration

The `config.yaml` file is where all the magic happens. Here's what you need to set up:

#### LLM Settings (Pick One)
```yaml
# Local (Free) - Requires Ollama running
llm_provider: ollama
llm_model: "llama3.2:3b"
ollama_base_url: "http://localhost:11434"

# Or use cloud providers:
# llm_provider: "openai"
# llm_model: "gpt-4-turbo"

# llm_provider: "gemini"  
# llm_model: "gemini-2.0-flash-exp"

# llm_provider: "groq"
# llm_model: "llama-3.3-70b-versatile"
```

#### Transcription Settings
```yaml
transcription_provider: "local"  # "local", "openai", or "groq"

# If using local:
local_whisper_model: "base"      # tiny, base, small, medium, large-v3
local_whisper_device: "auto"     # "auto", "cpu", or "cuda"
local_whisper_compute_type: "int8"  # "int8" for CPU, "float16" for GPU
```

#### API Keys (When Needed)
```yaml
api_keys:
  CEREBRAS_API_KEY: "YOUR-KEY-HERE"
  GEMINI_API_KEY: "YOUR-KEY-HERE"
  GROQ_API_KEY: "YOUR-KEY-HERE"
  OPENAI_API_KEY: "YOUR-KEY-HERE"
  OPENROUTER_API_KEY: "YOUR-KEY-HERE"
```

### Usage

#### Basic Usage

Run all commands from the repository root using the project's virtual environment. On Linux/macOS:

```bash
# Process a single video
.venv/bin/python ingest_video.py "https://youtu.be/kyK-MKRLRLk"

# Process URLs from a file (one URL per line)
.venv/bin/python ingest_video.py urls.txt

# Process a playlist
.venv/bin/python ingest_video.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# Process a channel (default: 10 videos)
.venv/bin/python ingest_video.py @LinuxfoundationOrg
```

Individual video summaries are saved as `SUMMARY_<video_id>.md`. Playlist and channel summaries are organized into their respective output directories.

For additional options:

```bash
.venv/bin/python ingest_video.py --help
```

**Environment management:** Use `uv pip install --python .venv/bin/python -r requirements.txt` whenever the project dependencies change. You do not need to activate the environment or install `pip` inside it.

#### Advanced Options

```bash
# Select up to 100 top-level comments by likes, with the 20 oldest replies each
.venv/bin/python ingest_video.py urls.txt --top-comments 100 --replies-per-comment 20

# Request all available top-level comments (still subject to context limits)
.venv/bin/python ingest_video.py urls.txt --all-comments

# Process more videos from a channel
.venv/bin/python ingest_video.py @LinuxfoundationOrg --channel-limit 25

# Process ALL videos from a channel (use with caution!)
.venv/bin/python ingest_video.py @LinuxfoundationOrg --channel-limit all

# Skip subtitle download and force audio transcription
.venv/bin/python ingest_video.py urls.txt --no-subtitles

# Save mode options
.venv/bin/python ingest_video.py urls.txt --save meta    # Keep metadata/transcripts
.venv/bin/python ingest_video.py urls.txt --save video   # Keep video files
.venv/bin/python ingest_video.py urls.txt --save all     # Keep everything
```

#### Comment Threads

Comments are organized by conversation rather than flattened into one list:

- **Top-level comments**: Ranked by like count, highest first. By default, include up to **25** parents (or the `min_comments` setting in `config.yaml`). Override with `--top-comments N`. The existing `--comments N` flag remains an alias.
- **Replies**: Grouped beneath their parent and sorted by timestamp, **oldest first**. Include up to **10** per parent by default; override with `--replies-per-comment N` (use `0` to omit replies).
- **`--all-comments`**: Requests all available top-level comments and prioritizes them over transcript space. It bypasses the parent count cap, but still respects the replies-per-comment limit and the LLM context budget.

The script fetches extra parent candidates, ranks the ones retrieved by likes, and selects the oldest available replies locally. YouTube may return incomplete comments or reply threads, so these limits are **maximums**, not guarantees. Replies with missing timestamps sort after dated replies. The model's context budget may reduce the final number of comments/replies or truncate the transcript.

#### YouTube Bot-Check (Cookies)
If you see an error like "Sign in to confirm you're not a bot", YouTube is
blocking unauthenticated requests. Export cookies from youtube.com in the
Netscape cookies.txt format and pass them to yt-dlp.

```bash
.venv/bin/python ingest_video.py "https://www.youtube.com/watch?v=..." \
  --cookies /absolute/path/to/cookies.txt
```

You can also set `yt_dlp_cookies` in config.yaml so you do not have to pass
`--cookies` every time.

### Example Output

Check out [`SUMMARY_example.md`](SUMMARY_example.md) to see what a generated summary looks like! Each summary includes:
- Comprehensive content overview
- Key insights with timestamps
- Detailed feature/topic breakdown tables
- Community intelligence (positive highlights, criticisms, corrections, tips)
- Raw context used for summarization (title, description, included transcript, and threaded comments)

## Project Structure

This is intentionally kept super simple – it's basically a single-file application:

```
yt-content-digest/
├── ingest_video.py           # The whole application
├── config.yaml               # Your configuration (copy from example.config.yaml)
├── example.config.yaml       # Template configuration
├── requirements.txt          # Dependencies
├── urls.txt                  # Example input file
├── SUMMARY_*.md              # Generated summaries
├── PLAYLIST_*/               # Playlist output directories  
├── CHANNEL_*/                # Channel output directories
└── docs/
    ├── RESOURCES.md          # Links to official docs for core dependencies
    ├── TODO.md               # Project roadmap
    └── NOTES.md              # Development notes
```

## How It Works (In Case You're Curious)

1. **Input Processing**: Accepts file paths, direct URLs, channel usernames, or channel IDs. Automatically expands playlists and channels into individual video queues.

2. **Download Pipeline**: Uses `yt-dlp` to extract metadata, candidate parent comments and their available replies, and subtitles to temporary files.

3. **Transcription Strategy**: 
   - First checks for VTT subtitle files
   - Converts VTT to clean timestamp format (handles YouTube's overlapping captions)
   - Falls back to audio download + transcription if needed

4. **Context Building**: Assembles a token-budgeted LLM input:
   - Includes the title and description first (oversized metadata may exceed the configured budget).
   - Ranks fetched parent comments by likes and keeps up to the configured top-level limit (default: 25).
   - Keeps up to the configured oldest replies under each parent (default: 10), preserving thread context.
   - Allocates remaining space to the transcript; comments/replies may be omitted if the budget is insufficient.
   - Uses `tiktoken` encoding heuristics based on the configured provider/model.

5. **LLM Analysis**: Sends context to your configured LLM with a sophisticated system prompt designed to extract structured insights.

6. **Output Management**: Generates `SUMMARY_{video_id}.md` files with optional metadata preservation based on save mode.

## Future Plans (The Fun Stuff!)

This started as a video summarizer, but I've got bigger plans. The project is designed to grow into a comprehensive YouTube channel analysis suite. Here's what I'm thinking about:

### Phase 1: Enhanced Analysis 🕵️
- **Comment-based channel analysis**: Download and analyze comments from some or all videos in a channel
- **Sentiment analysis**: Not just using an existing LLM API, but more sophisticated analysis to understand:
  - Does the creator usually post divisive content?
  - What kind of community/audience does the creator build/attract?
  - How do viewers react to different types of content?
  - What trends appear in community engagement over time?

### Phase 2: Pattern Recognition 🔍
- **Creator behavior patterns**: Identify trends across a creator's content
- **Community evolution tracking**: How has a channel's community changed over time?
- **Content effectiveness metrics**: What types of videos generate the most positive engagement?
- **Controversy detection**: Automatically identify videos that sparked debate or division

### Why This Matters
Understanding YouTube communities is about more than just summarizing videos. It's about capturing the conversation, the sentiment, and the ecosystem around content creators. This tool is the foundation for that deeper analysis.

## Technical Notes

### Dependencies
This project relies on three core libraries:
- **yt-dlp**: Media retrieval and metadata extraction
- **faster-whisper**: Local transcription (optional)
- **LiteLLM**: Universal LLM interface supporting 100+ providers

See [`docs/RESOURCES.md`](docs/RESOURCES.md) for links to official documentation.

### Token Management
The tool uses `tiktoken` to count tokens accurately based on your chosen provider/model:
- OpenAI models: Uses model-specific encoding
- Claude/Anthropic: Uses `cl100k_base`
- GPT-4o/o1: Uses `o200k_base`
- Other models: Falls back to `cl100k_base`

### File Management
Temporary files follow the pattern `video_{id}.*` and are auto-cleaned based on your `--save` mode. Only `.info.json` metadata is kept by default.

## Manually Tested Providers

### Transcription
- ✅ Local (faster-whisper)
- ✅ Groq
- ✅ OpenAI

### Summarization
- ✅ Ollama (Local)
- ℹ️ llama.cpp (Local) - *Not tested yet*
- ✅ OpenAI
- ✅ Gemini
- ✅ OpenRouter
- ✅ Groq
- ✅ Cerebras

## Known Limitations

- Requires internet for cloud providers (obviously)
- Local transcription needs decent CPU/GPU for larger models
- Channel processing can take a while for large channels
- YouTube comment scraping can be incomplete very occasionally
- Some videos require cookies due to YouTube bot-checks
- Token limits vary by provider/model (manual configure `max_context_tokens` accordingly)

## Contributing

This is a personal project and it's still pretty experimental. If you find bugs or have ideas, feel free to open an issue! I'm always curious to hear what people are using this for.

---

Thanks for checking this out! If you end up using this for something cool, I'd love to hear about it. Happy summarizing! 🚀
