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
- [ ] Make sure longer videos have longer summaries
  - May have to introduce different prompt if transcript or audio is longer
- [ ] Look into and integrate YouTube API if applicable
  - Need to check benefits of using API
- [ ] Look into other summarization providers to add
  - [ ] Cerebras
  - [ ] DeepSeek
- [ ] Look into other transcription providers to add
  - [ ] Cerebras

---

Future
- Make use of `rich` library (other features)?

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