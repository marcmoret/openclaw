---
title: Deepgram Python SDK Documentation
type: source
created: 2026-04-11
updated: 2026-04-11
tags: [deepgram, sdk, python, speech-ai, stt, tts]
sources: [raw/inbox/deepgramdeepgram-python-sdk Official Python SDK for Deepgram..md, raw/inbox/deepgramdeepgram-python-sdk Official Python SDK for Deepgram. 1.md]
related: [deepgram, livekit, voxira]
triage: summarized
---

# Deepgram Python SDK Documentation

Two Web Clipper captures of the official [[deepgram]] Python SDK repository README and v5→v6 migration guide.

## SDK Overview (v6)

The SDK provides sync and async clients for all Deepgram APIs. Key API surfaces and their SDK entry points:

- `client.listen.v1.media.transcribe_file()` / `transcribe_url()` — batch STT
- `client.listen.v1.connect()` / `client.listen.v2.connect()` — real-time WebSocket STT
- `client.speak.v1.audio.generate()` — TTS
- `client.speak.v1.connect()` — streaming TTS via WebSocket
- `client.read.v1.text.analyze()` — text intelligence (sentiment, topics, intents, summarization)
- `client.agent.v1.connect()` — conversational voice agent WebSocket

Authentication: API key or access token, with environment variable auto-discovery (`DEEPGRAM_API_KEY`, `DEEPGRAM_TOKEN`).

## v5 → v6 Migration (Breaking Changes)

The v6 release replaced hand-written socket types with Fern-generated types. Major changes:

- `deepgram.extensions.types.sockets` module removed; types moved to service-specific `types` modules
- `send_control()` replaced with dedicated methods (`send_flush()`, `send_close()`, `send_keep_alive()`, etc.)
- `send_media()` now accepts raw `bytes` instead of wrapper types
- Agent configuration types renamed and reorganized; think/speak providers moved to shared top-level types
- Event type names dropped `Event`/`Message` suffixes

## Custom Transports

The SDK supports pluggable WebSocket transports (duck-typed, no inheritance required). Notable: `deepgram-sagemaker` package provides async transport for running Deepgram models on AWS SageMaker endpoints via HTTP/2 bidirectional streaming.

## Source Files

- `raw/inbox/deepgramdeepgram-python-sdk Official Python SDK for Deepgram..md` — Full SDK README (460 lines)
- `raw/inbox/deepgramdeepgram-python-sdk Official Python SDK for Deepgram. 1.md` — v5→v6 migration guide (530 lines)
