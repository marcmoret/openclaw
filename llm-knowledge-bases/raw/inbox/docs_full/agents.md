## Agent Framework

### Lifecycle
1. `AgentSession.update_agent` activates a lazy-loaded agent from `create_call_agents` when `_transfer_to_agent` is invoked.
2. `BaseAgent.on_enter`
   - Updates `UserData.prev_agent/current_agent` and maintains `agents_history`.
   - Optionally copies prior chat context or clears it if configured.
   - Filters function tools based on agent-level `disabled_tools` and `dynamic_feature_flags`.
   - Boosts STT prompts/keywords when configured.
   - Registers variable observers to refresh prompts in real time.
   - Calls subclass `on_enter_implement` hook.
3. `on_exit` deregisters observers and logs trace events.

### Core Agents

| Agent | Responsibility | Notable Behavior |
|-------|----------------|------------------|
| `RecodingConsentAgent` | Obtain HIPAA recording consent. | Uses clinic dynamic messages and transitions to main flow. |
| `MainAgent` | Hub for general conversation and routing. | Chooses between initial or “back to main” prompt based on previous agent, resets `caller_intent`. |
| `PatientIdentificationAgent` | Collects required identity data. | Applies clinic feature flags (`ON_BEHALF`, `EMAIL_COLLECTION`, etc.), dynamically routes subsequence via `routing.identification`. |
| `PhoneNumberAgent`, `EMERGENCY_PHONE_NUMBER`, `DateOfBirthAgent` | Capture contact details. | Leverage validators and triggers for resuming flow if data missing. |
| `FullNameAgent`, `FirstNameAgent`, `LastNameAgent` | Name acquisition fallback strategies. | Choose combined or split flows depending on audio quality and user responses. |
| `ContactVerificationAgent` | Final confirmation before exiting identification. | Summarizes collected info and records call event. |
| `SchedulingAgent` | Handles new/reschedule/cancel appointment flows. | Fetches types & availability, selects slots, interacts with `scheduling_api` services, respects clinic policies (e.g., cancellation window). |
| `SavariaSchedulingAgent`, `OmniSchedulingAgent`, `OmniAppointmentTypeAgent` | EMR-specific flows. | Use EMR-specific service models, support hierarchical appointment types, combo services, provider filtering. |
| `CallerRequestAgent` | Intake general requests or voicemail capture. | Optionally initiates cold-transfer attempts depending on feature flags. |
| `TechnicalIssueAgent` | Mitigates backend downtime. | Communicates outages and fallbacks. |
| `SalesDemoAgent`, `NameSpellingTestAgent` | QA / demo scenarios. | Provide scripted interactions for non-production use. |
| `EndCallAgent` | Graceful call termination. | Waits for speech completion then ends room. |

### Routing Patterns
- **Intent-based Transfer**: `set_caller_intent` uses `SystemFeatures` to map to scheduling, cancellation, or referral agents via routing helpers.
- **Sequential Flows**: `routing.identification.determine_next_identification_agent` builds a deterministic sequence factoring in feature flags and patient status.
- **Cold Transfers**: `BaseAgent.cold_transfer` executes SIP transfer to clinic staff when enabled by dynamic flags, coordinating turn tracker and speech.

### Tool Design
- Implemented with `@function_tool` to expose capabilities to the LLM.
- `ignore_transcriptions_during_processing` decorator prevents partial ASR from interrupting long-running operations.
- Tool outputs often trigger agent transfers, update `UserData` variables, or call downstream services (e.g., `choose_slot` booking appointments).
- Error handling raises `ToolError` to prompt the LLM for corrective instructions.

### Prompt Management
- Prompts are Jinja templates loaded via `load_agent_config` and injected with runtime variables (clinic info, policies, dynamic instructions).
- `UserData.system_prompt` plus agent-specific prompts create layered instructions, followed by optional call summary appended for context continuity.
