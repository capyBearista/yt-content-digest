- [X] Remove `download_audio_if_mis if sing_subs` config line
- [X] Add SUMMARY ignore line
- [X] Make sure Groq transcription method works (test again)
- [ ] Remove transcription/summarization provider and model defaults (show error if not defined in config)
- [ ] Test multiple URLs input
  - [ ] Confirm SUMMARY files output format (should be one for each video)
  - [ ] Confirm terminal output (each video should be cleanly separated)
- [ ] Test transcription providers
- [ ] Test summarization providers
- [ ] Look into other transcription providers, add them
- [ ] Preserve summary format (like example from x-ai/grok-4.1-fast:free) via prompting
- [ ] Make sure longer videos have longer summaries
  - May have to introduce different prompt if transcript or audio is longer
- [ ] Look into and integrate YouTube API if applicable
  - Need to check benefits of using API

---

Future
- Make use of `rich` library?

---

Tested Transcription Providers
- [ ] Local (Ollama)
- [ ] Qroq
- [X] OpenAI

Tested Summarization Providers
- [ ] Local (Ollama)
- [ ] OpenAI
- [ ] Anthropic
- [ ] Gemini
- [X] OpenRouter
- [ ] Groq