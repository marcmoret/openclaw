---
title: LiveKit
type: entity
created: 2026-04-11
updated: 2026-04-11
tags: [voice-ai, webrtc, realtime, agents, platform]
sources: [livekit-docs]
related: [deepgram, voxira, multi-agent-orchestration]
---

# LiveKit

Open-source platform for building voice, video, and physical AI agents. Provides both a self-hostable WebRTC SFU server and a cloud-hosted commercial offering (LiveKit Cloud).

## Core Components

- **LiveKit Server:** WebRTC Selective Forwarding Unit (SFU) for real-time media routing. Can be self-hosted or used via LiveKit Cloud.
- **Agents Framework:** High-level Python and Node.js tools for building AI agents, with a plugin system connecting to AI providers (Deepgram, OpenAI, ElevenLabs, etc.). Includes deployment environment and hosted inference service.
- **Client SDKs:** Real-time media SDKs for Web, Swift, Android, Flutter, React Native, Unity, Python, Node.js, Rust, C++, and ESP32.
- **Integration Services:** Telephony (SIP/PSTN), Egress (recording/streaming), and room management APIs.

## Architecture Pattern

LiveKit's agent framework follows a session-based model: a Worker receives `JobContext` per call, creates an `AgentSession`, and orchestrates STT→LLM→TTS pipelines. This is the foundation pattern used by [[voxira]].

## Role in [[voxira]]

LiveKit serves as the real-time communication backbone for Voxira's healthcare voice agents. The `AgentSession` manages speech synthesis, transcriptions, and function tools. Telephony integration handles inbound calls via SIP trunking (Twilio).

## Sources

- [[livekit-docs]] — Full platform documentation (2.5MB, comprehensive)
