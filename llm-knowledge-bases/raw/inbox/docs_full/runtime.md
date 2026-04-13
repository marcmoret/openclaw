## Runtime & Audio Pipeline

### Audio Configuration
- **Sample Rates**: Determined dynamically via `audio_utils.get_sample_rate`, considering participant type (phone vs web) for VAD, STT, TTS, and room audio.
- **VAD**: Silero models prewarmed in `main.py`; `session_loader.get_vad_instance` retrieves proper sample rate variant.
- **Noise Cancellation**: Configurable per language/clinic via `session_utils.get_noise_cancellation`, defaulting to BVCTelephony for SIP calls.
- **Background Audio**: `BackgroundAudioPlayer` configured with ambient/“thinking” sounds to reduce dead air; started alongside agent session.

### Speech & Transcription Flow
1. User audio is captured by LiveKit and fed into the session STT model (Deepgram/OpenAI/Google depending on stack).
2. `BaseAgent.boost_stt` optionally sets prompts/keywords to improve recognition for clinic-specific terms.
3. `AgentSession` aggregates transcripts into chat context items; partial transcripts are filtered when `ignore_transcriptions_during_processing` is active.
4. Tools and prompts generate assistant responses which drive TTS playback through configured provider (ElevenLabs, PlayHT).

### Turn Tracking & Silence Handling
- `TurnTracker` listens to `user_state_changed` and `agent_state_changed` events, maintaining last speaking timestamps and active silence windows.
- Default silence callbacks trigger developer messages to re-engage callers when silence exceeds configured thresholds.
- DTMF events reset silence timers and can interrupt current speech if allowed.

### Observability Workflow
- `SessionObserver` registers LiveKit metrics, speech events, tool executions, transcription updates, and errors.
- Each speech handle creates a Langfuse span; completion times and interruptions are tracked for quality metrics.
- User/agent state transitions are synchronized to avoid conflicting spans (e.g., user speaking ends agent listening span).
- Metrics collected (`LLM`, `STT`, `TTS`, `VAD`, `RealtimeModel`) are parsed for detailed usage and token accounting.

### Shutdown & Post-Call Tasks
- Disconnect handlers cancel silence checker tasks, stop egress recordings, and delete LiveKit rooms.
- `save_call_transcript` and `save_call_logs` persist conversation data.
- Optional webhook generation produces call summary, analysis, and logs for downstream dashboards.

### Error Handling
- Global logging uses JSON or plain text depending on environment, always enriched with `session_id` for traceability.
- `SessionObserver._handle_error` captures recoverable vs unrecoverable issues, storing tracebacks in Langfuse.
- Tool errors propagate as `ToolError`, prompting the LLM to recover gracefully without breaking conversation state.
