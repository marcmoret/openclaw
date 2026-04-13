## Data & Interaction Flows

### Call Lifecycle
1. **Inbound Call**
   - LiveKit notifies worker; `entrypoint` accepts room, connects audio, and logs `session_id`.
   - Participant join triggers number extraction (SIP vs web) to configure caller identities.

2. **Dynamic Configuration Fetch**
   - `ai_service.get_dynamic_data` retrieves clinic metadata (language, prompts, feature flags, stack overrides).
   - `UserData.set_dynamic_data` populates variables and feature flags, including policies, availability toggles, and prompt text.

3. **Agent Session Initialization**
   - `create_stack` selects LLM/STT/TTS/VAD services; `AgentSession` binds them with `UserData`.
   - `create_call_agents` builds lazy factories for all potential agents using processed configs.
   - First agent determined by clinic config (`first_agent_name`) or defaults to recording consent.

4. **Conversation Loop**
   - User speech → STT → Chat context → LLM prompt.
   - Agent responses generated via prompts + `UserData.variables` → TTS output.
   - Tools invoked (e.g., scheduling) interact with backend services, updating `UserData` variables and appending call events.
   - Turn tracker monitors silence; DTMF events can trigger manual reply generation or interrupts.

5. **Completion & Cleanup**
   - Final agent (often `EndCallAgent`) ends LiveKit room; shutdown callback assembles transcripts, summaries, and logs.
   - Webhook submission includes analysis and optional recording URL for downstream systems.

### Patient Identification Flow
1. **PII Consent**: Optional message based on `pii_consent_message_status`.
2. **Patient Type / On Behalf**: Enabled via feature flags; sets `is_new_patient` and `is_on_behalf_of_someone_else`.
3. **Phone & Emergency Contact**: Emergency collection for new patients when enabled.
4. **Date of Birth & Name**: Uses either full-name or first/last split depending on audio quality and routing.
5. **Email / Address / Residency**: Gathered for new patients if respective feature flags allow.
6. **Contact Verification**: Summarizes captured data, records call event, and prepares scheduling handoff.

### Scheduling Flow
1. **Intent Setting**: `set_caller_intent` identifies scheduling vs rescheduling vs cancellation.
2. **Appointment Types**: Agents load available types (Savaria/Omni) and hierarchical providers.
3. **Availability Check**: `check_date_availability` queries backend for slots, grouping by time period.
4. **Selection & Booking**: `choose_slot` posts appointment creation; success updates call events and confirms details to caller.
5. **Reschedule / Cancel**: Dedicated tools call `scheduling_api` endpoints, updating appointment lists and summarizing results.

### Data Validation
- `validators/contact.py` enforces healthcare-specific constraints (RAMQ, phone, email, age ranges).
- Agents store standardized values in `UserData.variables`, ensuring downstream services receive clean data.

### Analytics & Reporting
- `call_analysis_utils.generate_call_summary_and_analysis` produces summary and structured `CallAnalysis` for dashboards.
- `UserData.call_events` append templated events for HIPAA audit logs and real-time prompt augmentation.
