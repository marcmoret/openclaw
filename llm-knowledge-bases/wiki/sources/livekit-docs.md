---
title: LiveKit Platform Documentation
type: source
created: 2026-04-11
updated: 2026-04-11
tags: [livekit, webrtc, voice-ai, agents, platform]
sources: [raw/inbox/Untitled.md]
related: [livekit, voxira, deepgram, multi-agent-orchestration]
triage: summarized
---

# LiveKit Platform Documentation

Large (2.5MB) Web Clipper capture of the LiveKit documentation site. Covers the full platform: server architecture, agents framework, client SDKs, telephony, egress, and deployment.

## Key Content

- **Platform overview**: Open-source WebRTC SFU + cloud offering for voice, video, and AI agents
- **Agents framework**: Python and Node.js tools for building AI agents with plugin system for AI provider integration
- **Client SDKs**: Real-time media SDKs across 11+ platforms (Web, Swift, Android, Flutter, React Native, Unity, Python, Node.js, Rust, C++, ESP32)
- **Telephony integration**: SIP/PSTN connectivity for phone network access
- **Egress**: Recording and streaming capabilities

## Relevance

[[livekit]] is the real-time communication backbone for [[voxira]]. This documentation covers the platform primitives that Voxira builds on: `JobContext`, `AgentSession`, worker lifecycle, audio pipelines, and room management.

## Source Files

- `raw/inbox/Untitled.md` — Full LiveKit documentation dump (2.5MB, too large for single-pass read)
