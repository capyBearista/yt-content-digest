## Speech-to-Text
OpenAI takes a LONG ASS TIME for transcription
Groq is insanely quick

need to compare the accuracy to original (downloaded) transcript though

Groq has a FREE TIER: https://console.groq.com/docs/rate-limits, BUT it doesn't like large requests
```json
Transcription API failed (APIStatusError): Error code: 413 - {'error': {'message': 'Request Entity Too Large', 'type': 'invalid_request_error', 'code': 'request_too_large'}}
```

grok-4.1-fast:free has 2,000,000 context window: https://openrouter.ai/x-ai/grok-4.1-fast:free

Haven't tested with Anthropic, Grok since they don't have free tiers and require payment.