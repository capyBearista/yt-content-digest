## Media Retrieval (yt-dlp)
| Library | Description | Resource URL |
| :--- | :--- | :--- |
| **yt-dlp (Repo/Docs)** | **Primary Reference.** Look for the "Embedding yt-dlp" section to find Python options. Focus on `ydl_opts` dictionary keys for format selection (`bestaudio`), post-processors (FFmpegExtractAudio), and cookie handling. | `https://github.com/yt-dlp/yt-dlp` |
| **yt-dlp (PyPi)** | Installation specifics and version history. | `https://pypi.org/project/yt-dlp/` |

## Transcription (Faster Whisper)
| Library | Description | Resource URL |
| :--- | :--- | :--- |
| **Faster-Whisper (Repo)** | **Primary Reference.** Python usage of `WhisperModel` class. Look for arguments regarding `device` (cuda/cpu), `compute_type` (float16/int8), `beam_size`, and `vad_filter` (Voice Activity Detection). | `https://github.com/SYSTRAN/faster-whisper` |
| **Faster-Whisper (PyPi)** | Version compatibility and CTranslate2 dependencies. | `https://pypi.org/project/faster-whisper/` |

## LLM Inference (LiteLLM)
| Library | Description | Resource URL |
| :--- | :--- | :--- |
| **LiteLLM (Official Docs)** | **Main Reference.** Unified API syntax for `completion()`, streaming responses, and `function_calling`. Check this for mapping provider-specific parameters to the LiteLLM standard. | `https://docs.litellm.ai/docs/` |
| **LiteLLM (Repo)** | Source code and provider SDK integration details. | `https://github.com/BerriAI/litellm` |