---
title: Deepgram
type: entity
created: 2026-04-11
updated: 2026-04-11
tags: [speech-ai, stt, tts, api, sdk]
sources: [deepgram-python-sdk]
related: [livekit, voxira, multi-agent-orchestration]
---

# Deepgram

AI speech platform providing speech-to-text (STT), text-to-speech (TTS), and language understanding APIs. Used as a core provider in voice agent systems including [[voxira]].

## Key Products

The platform offers several API surfaces accessed through official SDKs (Python, JS, etc.):

- **Listen (STT):** Real-time and batch transcription. Models include Nova-3 (file/URL transcription) and Flux (real-time streaming with contextual turn detection via Listen v2).
- **Speak (TTS):** Audio generation from text. Aura-2 model family for natural voice synthesis.
- **Read (Text Intelligence):** Sentiment analysis, summarization, topic detection, intent classification.
- **Agent (Voice AI):** WebSocket-based conversational voice agent framework supporting multi-provider stacks (Deepgram STT + OpenAI/Anthropic LLM + Deepgram/ElevenLabs TTS).

## SDK Architecture

The Python SDK (v6, current) uses Fern-generated types with both sync and async clients. Key patterns: context manager WebSocket connections, event-driven message handling (`EventType.MESSAGE`, `EventType.OPEN`, etc.), and pluggable transport layer (including AWS SageMaker support via `deepgram-sagemaker`).

Authentication supports API keys and access tokens, with environment variable auto-discovery (`DEEPGRAM_API_KEY`, `DEEPGRAM_TOKEN`).

## Role in [[voxira]]

Deepgram Nova-3 serves as the primary STT provider in Voxira's LiveKit-based voice agent stack. The agent framework dynamically selects STT/TTS providers based on caller language and device context.

## Sources

- [[deepgram-python-sdk]] — Official Python SDK documentation and v5→v6 migration guide
