## System Architecture

### Core Layers
1. **Entry Layer (`main.py`)**
   - Configures environment, logging, Datadog tracing, and CLI worker options.
   - `prewarm_all_vad_configurations` loads Silero VAD models into `proc.userdata` for reuse.
   - `entrypoint(ctx: JobContext)` captures the LiveKit room, logs session metadata, attaches DTMF handlers, and starts the prepared agent session.

2. **Session Orchestration (`src/utils/session_utils.py`)**
   - Waits for the first participant to determine phone/web context and overrides caller numbers.
   - Instantiates `UserData`, background audio, and optional egress recording.
   - Pulls clinic-specific dynamic data via `ai_service.get_dynamic_data` to populate feature flags, prompts, language, and timezone.
   - Builds the session stack (`create_stack` / `get_agent_session_params`) to select LLM, STT, TTS, and VAD providers based on the caller’s language and device.
   - Creates `AgentSession[UserData]`, attaches Langfuse `SessionObserver`, and registers disconnect / shutdown handlers for cleanup and webhook delivery.
   - Initializes `TurnTracker` for silence detection and registers default silence callbacks.

3. **Context Model (`src/models/context.py`)**
   - `UserData` stores per-call state: variables, dynamic configuration, LLM/scheduling services, and call events.
   - Observers notify active agents when variables change, ensuring prompts stay synchronized.
   - Provides helper methods for feature flags, clinic open hours, call summaries, and agent retrieval.

4. **Agent Framework (`src/agents/base/base_agent.py`)**
   - Extends LiveKit’s `Agent` with prompt injection, STT keyword boosting, chat context management, and tool orchestration.
   - Handles agent lifecycle (`on_enter`, `on_exit`), variable observation, and routing via `_transfer_to_agent`.
   - Implements standard tools (`set_caller_intent`, `answer_caller_question`, `talk_to_human`, emergency handling) with feature-flag-aware filtering.
   - Integrates Langfuse tracing and conversation summarization for observability.

5. **Specialized Agents (`src/agents/**`)**
   - **Recording Consent** initializes HIPAA compliance flow.
   - **Patient Identification** coordinates name, DOB, phone, residency, and consent verification with dynamic steps via `routing/identification.py`.
   - **Main Agent** centralizes intent handling and transitions back from specialized flows.
   - **Scheduling Agents** integrate with clinic EMR APIs (Savaria, Omni) to fetch appointment types, availability, and manage bookings.
   - Additional agents handle email capture, caller requests, sales demos, technical issues, and handoffs.

6. **Service Layer (`src/services`)**
   - Encapsulates HTTP interactions with backend APIs (dynamic data, contacts, scheduling, appointment requests) using `AsyncApiClient` with tracing hooks.
   - `llm_service.py` standardizes OpenAI interaction, structured output parsing, and transcript summaries.

7. **Observability & Utilities**
   - `SessionObserver` logs speech, tool usage, metrics, and state transitions to Langfuse.
   - `logging_config.py` enforces structured logging with session correlation.
   - `turn_tracker.py` monitors user/agent states to trigger silence recovery actions.

### Configuration Layers
- **Static Config (`src/configs/config.py`)**: Global constants, feature toggles, VAD presets, audio sampling, and default models.
- **Dynamic Clinic Data (`DynamicData`)**: Per-call injection of prompts, policies, feature flags, and stack overrides.
- **Agent-Specific Config (`agents_config`)**: Optional overrides for individual agents (e.g., disabled tools, custom TTS/STT).

### Control Flow Summary
```
LiveKit Worker → entrypoint → setup_session_components_and_handlers
  → AgentSession + UserData
  → Dynamic data + stack loading
  → create_call_agents
  → Agent lifecycle (BaseAgent + specialized agents)
  → Services (AI, Scheduling, Contact)
  → Observability + Clean-up
```
