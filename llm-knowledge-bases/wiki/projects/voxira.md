---
title: Voxira
type: project
created: 2026-04-11
updated: 2026-04-11
tags: [voice-agent, healthcare, livekit, multi-agent, scheduling, hipaa]
sources: [voxira-docs, voxira-architecture]
related: [deepgram, livekit, multi-agent-orchestration]
---

# Voxira

Healthcare-focused conversational voice agent platform built on [[livekit]]. Orchestrates inbound calls through a multi-agent system that captures consent, identifies patients, schedules appointments, and hands off to specialized skills.

## Architecture

The system follows a layered architecture:

1. **Entry Layer** (`main.py`): Configures environment, logging, Datadog tracing. Prewarms Silero VAD models. LiveKit worker invokes `entrypoint` per call.
2. **Session Orchestration** (`session_utils.py`): Waits for participant, pulls clinic-specific dynamic config, builds the session stack (LLM/STT/TTS/VAD selection by language and device), creates `AgentSession`, attaches observability.
3. **Context Model** (`UserData`): Per-call state — variables, dynamic config, services, call events. Observer pattern keeps agent prompts synchronized with variable changes.
4. **Agent Framework** (`BaseAgent`): Extends LiveKit's `Agent` with prompt injection, STT keyword boosting, chat context management, tool orchestration, and Langfuse tracing.
5. **Specialized Agents**: Recording consent (HIPAA), patient identification, scheduling (Savaria/Omni EMR), caller requests, technical issues, sales demos, end call.
6. **Service Layer**: HTTP integrations with backend APIs — dynamic data, contacts, scheduling, LLM service (OpenAI), appointment management.
7. **Observability**: Langfuse `SessionObserver`, structured logging with session correlation, turn tracking for silence recovery.

## AI Stack

- **STT**: [[deepgram]] Nova-3 (primary), dynamically selected per language/device
- **TTS**: Deepgram Aura-2 (primary), with provider override support
- **LLM**: OpenAI (gpt-4o-mini and others), used for intent extraction, slot filling, call summaries
- **VAD**: Silero (prewarmed models)
- **Telephony**: Twilio SIP → [[livekit]] → agents

## Agent Roster

The system uses 15+ specialized agents orchestrated through intent-based transfer and sequential routing:

- **RecordingConsentAgent**: HIPAA compliance flow
- **PatientIdentificationAgent**: Collects name, DOB, phone, residency, consent; dynamic routing via feature flags
- **MainAgent**: Hub for general conversation and intent-based routing
- **SchedulingAgent**: New/reschedule/cancel appointments via EMR APIs
- **SavariaSchedulingAgent / OmniSchedulingAgent**: EMR-specific booking flows
- **CallerRequestAgent**: General intake, voicemail, cold-transfer attempts
- **NameSpellingAgent**: Handles STT failures with fuzzy name matching (Quebec French dataset)
- **EndCallAgent**: Graceful termination

## Key Features

- **Multi-tenant**: Dynamic clinic configuration (prompts, policies, feature flags, stack overrides) fetched per call
- **Quebec French optimization**: Fuzzy name matching using government name datasets with popularity weighting for STT error correction
- **Cost tracking**: Per-session usage tracking across LLM tokens, STT/TTS audio duration, infrastructure costs (Twilio + LiveKit)
- **Deployment**: AWS ECS (Fargate), ECR, GitHub Actions CI/CD, Terraform IaC, AWS Secrets Manager

## Configuration Layers

- **Static**: Global constants, feature toggles, VAD presets, audio sampling, default models (`src/configs/config.py`)
- **Dynamic**: Per-call clinic injection — prompts, policies, feature flags, stack overrides (`DynamicData`)
- **Agent-specific**: Optional per-agent overrides (disabled tools, custom TTS/STT) (`agents_config`)

## Development History

**Timeline of major milestones** extracted from 80 development sessions (2026-03-12 to 2026-04-11):

### Phase 1: Architecture Planning (2026-03-12 to 2026-03-16)

- **3/12**: Project kickoff. Discussed multi-tenant clinic scaling, agent flow graph design
- **3/13**: Dashboard mockup and clinic configuration strategy
- **3/16**: Comprehensive voxira-agents plan. Key decisions:
  - React Flow for UI (vs. Angular) — superior library ecosystem
  - Hybrid approach: Keep Laravel dashboard, add React SPA for flow builder at `/clinic/{id}/flow-builder`
  - Flow graph model with conditional edges (replaces hardcoded if/elif chains)
  - 3-table schema: `call_flows`, `call_flow_nodes`, `call_flow_edges`

### Phase 2: Agent Implementation & Voice Performance (2026-03-17 to 2026-03-30)

- **3/17**: Langfuse trace analysis. Identified 5–9 second silence detection gaps after agent transfers
  - Root cause: Post-agent-transfer LISTENING state waits 8–9s for user input
  - Investigated prompt caching (OpenAI API) to reduce TTFT (first token time)
- **3/18–3/25**: Agent concurrency testing, LiveKit integration, intent classification refactoring
- **3/20**: API timeout investigation. OpenAI latency vs. local network issues (resolved as network blip)
- **3/23**: Intent routing and appointment type mapping work
- **3/26**: Code review sprint across all 3 repos (voxira-dashboard, voxira-api, voxira-livekit)
- **3/30**: Most active development day. Key achievements:
  - Multi-clinic testing with dynamic feature flags
  - Identified Quebec French STT challenges (name pronunciation, accent handling)
  - Established [[langfuse-trace-analysis|Langfuse]] as primary debugging tool for voice agent conversations

### Phase 3: Multi-Tenant Configuration (2026-03-31 to 2026-04-05)

- **4/1**: PiedReseau clinic launch. Built appointment type mapping from Excel spreadsheet
  - Extracted clinical logic for appointment durations, pricing, patient criteria
  - Debated YAML vs. DB for dynamic rule storage (chose hybrid: YAML in code + DB for variations)
- **4/2**: Dashboard feature flag configuration UI
- **4/3**: Integrated test suite for multi-clinic scenarios

### Phase 4: Testing, E2E Validation & Performance (2026-04-07 to 2026-04-11)

- **4/7**: End-to-end call flow testing. Validated greeting → triage → scheduling → confirmation sequence
- **4/9**: Langfuse loop detection. Found scheduling agent stuck in appointment availability checking
- **4/10**: Performance optimization sprint
  - Reduced [[voice-agent-performance-optimization|LLM TTFT]] through prompt caching
  - Fixed silence detection gaps (immediate agent transfer implementation)
  - Optimized [[quebec-french-stt-optimization|Quebec French STT]] with fuzzy name matching
- **4/11**: Final integration and edge case handling

### Key Technical Achievements

1. **[[healthcare-voice-agent-patterns|Multi-tenant architecture]]**: Clinic-specific flows, feature flags, appointment type mappings without code redeploy
2. **[[voice-agent-performance-optimization|Performance optimization]]**: Reduced response latency from 8–9s to <3s
3. **[[langfuse-trace-analysis|Observability]]**: Established conversation debugging via JSON trace export
4. **[[quebec-french-stt-optimization|Quebec French support]]**: Fuzzy name matching, STT keyword boosting, spelling fallback
5. **React Flow integration**: UI for clinic admins to visually design call flows (drag-and-drop nodes/edges)

## Sources

- [[voxira-architecture]] — Full platform architecture documentation (docs_full/)
- [[voxira-docs]] — Operational documentation: deployment, cost calculation, usage tracking, env vars, fuzzy matching (docs/)
- [[sessions-overview]] — Index of 80 development sessions synthesized into concept pages
