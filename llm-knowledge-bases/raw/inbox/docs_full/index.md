## Voxira LiveKit Voice Agent Platform Documentation

### Overview
- **Purpose**: Healthcare-focused conversational voice agent that orchestrates inbound calls through LiveKit, capturing consent, identifying patients, scheduling appointments, and handing off to specialized skills.
- **Entry Point**: `main.py` initializes logging, prewarms Silero VAD models, and registers the asynchronous LiveKit `entrypoint` used by deployed workers.
- **Runtime Flow**:
  1. LiveKit worker invokes `entrypoint` with a `JobContext` for each call.
  2. `session_utils.setup_session_components_and_handlers` prepares the `AgentSession`, background audio, per-call `UserData`, turn tracking, and observability hooks.
  3. Dynamic clinic configuration is fetched from the backend to determine language, prompts, feature flags, and session stack (LLM/STT/TTS/VAD).
  4. Agent factories defined in `src/agents/__init__.py` lazily construct specialized agents when they are activated in the conversation flow.
  5. Agents collaborate through `AgentSession` to manage speech synthesis, transcriptions, and function tools, while audit events and transcripts feed downstream analytics.
- **Key Features**:
  - Multi-agent, goal-oriented dialog management with patient identity and scheduling flows.
  - Dynamic multi-tenant configuration supporting clinic-specific prompts, policies, and feature flags.
  - Integrated observability via Langfuse, structured logging, and call summaries.
  - Telephony-aware audio pipeline with adaptive sample rates, background ambience, and silence tracking.

### Documentation Map
- `architecture.md`: High-level system architecture, control flow, and configuration layers.
- `agents.md`: Detailed reference for core agents, lifecycle hooks, and routing patterns.
- `services.md`: Description of service layer integrations (AI, scheduling, contact, LLM).
- `runtime.md`: Audio pipeline, session orchestration, turn tracking, and observability.
- `deployment.md`: Instructions for local development, testing, Docker images, and Terraform pointers.
- `data_flows.md`: Call lifecycle, patient identification sequence, and scheduling interactions.
