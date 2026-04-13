## Service Layer

### HTTP Client Infrastructure
- `src/utils/api_client.py`
  - Provides synchronous and asynchronous clients with shared hooks.
  - Automatically injects Langfuse spans, timing logs, and session correlation headers.
  - `BACKEND_API_URL` environment variable is mandatory; requests are namespaced under `/api/v1`.

### AI & Dynamic Configuration
- `ai_service.py`
  - `get_dynamic_data` retrieves clinic/tenant-specific configuration (`DynamicData`).
  - `check_emr_status` asynchronously pings EMR connectivity for real-time availability.
  - `send_webhook` posts call summaries, transcripts, and analytics to the dashboard after call completion.
  - Internal `_sanitize_for_json` ensures webhook payloads are serializable.

### LLM Service
- `llm_service.py`
  - Wraps OpenAI client usage, supporting standard chat completions, reasoning mode, structured outputs via Pydantic, and JSON schema enforcement.
  - Used by agents for intent extraction, slot filling, and knowledge base responses.
  - Generates call summary and analysis artifacts for post-call reporting.

### Contact Management
- `contact_service.py`
  - Fetches patient records, creates new contacts, and performs phone-based searches.
  - Utilizes validated payloads (`validators/contact.py`) to ensure healthcare-specific data integrity (RAMQ, phone, emails).

### Scheduling APIs
- `scheduling_api.py`
  - Interfaces with backend scheduling endpoints for availability, booking, rescheduling, and cancellation.
  - Parameterizes requests with contact IDs, appointment types, staff, and locations.
  - Returns typed responses through generic models (`GetAvailabilitiesResponse`, `CreateAppointmentResponse`).
- `scheduling_service.py`
  - Provides EMR-specific formatting and grouping logic (e.g., Savaria combo appointments).
  - Formats appointment types, providers, and readable summaries for the LLM context.

### Additional Services
- `appointment_request_service.py`, `appointment_type_service.py`, `caller_request_service.py`, `staff_service.py`: Support utilities for retrieving appointment metadata, triage data, and staff listings.
- `ai_service.check_emr_status` & webhook flow ensure EMR readiness and final reporting.

### Observability
- `session/components/observability.py`
  - `SessionObserver` listens to LiveKit session events (LLM metrics, STT, TTS, VAD, user/agent state) and logs to Langfuse with redacted sensitive data.
  - Tracks custom events, speech lifecycle, errors, and ensures spans close properly on shutdown.

### Storage & Recording
- `utils/call_utils.py`
  - Handles egress recording lifecycle, transcript extraction, and call log persistence.
  - Saves conversation items for downstream analytics and optionally uploads audio to S3.
