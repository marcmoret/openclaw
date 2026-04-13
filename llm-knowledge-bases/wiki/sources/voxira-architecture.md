---
title: Voxira Platform Architecture Docs
type: source
created: 2026-04-11
updated: 2026-04-11
tags: [voxira, architecture, agents, healthcare, livekit]
sources: [raw/inbox/docs_full/index.md, raw/inbox/docs_full/architecture.md, raw/inbox/docs_full/agents.md, raw/inbox/docs_full/services.md, raw/inbox/docs_full/runtime.md, raw/inbox/docs_full/deployment.md, raw/inbox/docs_full/data_flows.md]
related: [voxira, livekit, deepgram, multi-agent-orchestration]
triage: summarized
---

# Voxira Platform Architecture Docs

Full architecture documentation for the [[voxira]] healthcare voice agent platform. 7 files covering system design, agent framework, services, runtime, deployment, and data flows.

## Documents

- **index.md**: Overview — healthcare-focused voice agent on [[livekit]], multi-agent dialog, dynamic multi-tenant config, Langfuse observability, telephony-aware audio pipeline.
- **architecture.md**: 7-layer architecture (Entry → Session Orchestration → Context Model → Agent Framework → Specialized Agents → Service Layer → Observability). Configuration layers: static, dynamic (per-clinic), agent-specific.
- **agents.md**: Agent lifecycle (`on_enter`/`on_exit`), 15+ specialized agents (consent, patient ID, scheduling, caller requests, name spelling, end call). Routing patterns: intent-based transfer, sequential flows, cold transfers. Tool design with `@function_tool`.
- **services.md**: HTTP client with Langfuse tracing, AI service (dynamic data, EMR status, webhooks), LLM service (OpenAI structured outputs), contact management, scheduling APIs (Savaria/Omni EMR integration).
- **runtime.md**: Audio pipeline, session orchestration, turn tracking, observability hooks.
- **deployment.md**: AWS ECS/Fargate, ECR, GitHub Actions CI/CD, Terraform IaC.
- **data_flows.md**: Call lifecycle, patient identification sequence, scheduling interaction flows.

## Key Patterns

The agent framework extends [[livekit]]'s `Agent` base class with: prompt injection, STT keyword boosting, chat context management, tool orchestration, variable observation (observer pattern), and Langfuse tracing. This is a production implementation of [[multi-agent-orchestration]] patterns applied to healthcare telephony.

## Source Files

Located in `raw/inbox/docs_full/` (7 files, ~20KB total)
