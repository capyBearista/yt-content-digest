- [X] Remove `download_audio_if_mis if sing_subs` config line
- [X] Add SUMMARY ignore line
- [X] Make sure Groq transcription method works (test again)
- [X] Remove transcription/summarization provider and model defaults (show error if not defined in config)
- [X] Test multiple URLs input
  - [X] Confirm SUMMARY files output format (should be one for each video)
  - [X] Confirm terminal output (each video should be cleanly separated)
- [X] Test transcription providers
- [X] Test summarization providers
- [X] Clean links added to input file (remove timestamps, extra text, tracking text)
- [x] Enhance video summary and analysis prompt
- [X] Add direct URL input option (in addition to file input)
- [X] Make sure longer videos have longer summaries
  - May have to introduce different prompt if transcript or audio is longer
- [X] ~~Look into and integrate YouTube API if applicable~~
  - ~~Need to check benefits of using API~~ Not useful, requires a lot of setup for little benefit
- [X] Look into other summarization providers to add
  - [X] Cerebras
  - [X] ~~DeepSeek~~ no free tier
- [X] Look into other transcription providers to add
  - [X] ~~Cerebras~~ no transcription providers
- [ ] Add playlist input processing
- [ ] Add channel input processing

---

Future
- Make use of `rich` library (other features)?
- The project is one program that can do a variety of functions:
  - download and summarize one/multiple videos (currently working)
  - download and summarize some or all videos from a channel (TBD)
  - download and analyze the comments of some or all videos from a channel (TBD)
  - sentiment analysis, but not by using an existing LLM via API (TBD)
  - the intention is to best understand how viewers/visitors to a channel react to the creator (e.g., does the creator usually post divisive content? does the create have an overwhelmingly positive community?) 

---

Tested Transcription Providers
- [X] Local (faster-whisper)
- [X] Groq
- [X] OpenAI

Tested Summarization Providers
- [X] Local (Ollama)
- [X] OpenAI
- [X] Gemini
- [X] OpenRouter
- [X] Groq