---
title: Langfuse Trace Analysis for Voice Agents
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [voxira, langfuse, debugging, trace-analysis, observability, voice-agent]
sources: [sessions-2026-03-17-onwards, voxira]
related: [voxira, voice-agent-performance-optimization, healthcare-voice-agent-patterns]
---

# Langfuse Trace Analysis for Voice Agents

Methodology for debugging voice agent conversations using Langfuse JSON trace exports. Based on [[voxira]] development sessions where trace analysis became the primary tool for identifying latency, logic, and routing bugs.

## Why Langfuse Traces Matter

Voice agent conversations are complex: LLM calls, tool invocations, STT/TTS I/O, agent routing, and real-time speech processing happen concurrently. Traditional logging and stdout debugging are insufficient. Langfuse provides:

1. **Structured trace export** (JSON) with start/end times for every span
2. **Hierarchical context** (session → turn → LLM call → tokens)
3. **Timing analysis** (identify bottlenecks, gaps)
4. **Token accounting** (input/output/cache tokens per model)

### Voxira Integration

[[voxira]] emits Langfuse traces for every call:
- Session-level: Entire call recording
- Turn-level: One user input → agent response cycle
- Span-level: Individual tool calls, LLM calls, VAD events

Operators can export JSON traces from Langfuse UI and share with development for offline analysis.

---

## Anatomy of a Trace

### Top-Level Session Span

```json
{
  "id": "session-12345",
  "name": "call:patient-scheduling",
  "startTime": "2026-03-17T19:38:51Z",
  "endTime": "2026-03-17T19:45:30Z",
  "metadata": {
    "clinic": "PCMD",
    "patient_id": "P-001",
    "phone": "+16783254014",
    "language": "fr-CA"
  }
}
```

### Turn Spans (Nested)

One session contains multiple turns. Each turn = user input → agent response:

```json
{
  "turns": [
    {
      "id": "turn-1",
      "name": "greeting",
      "startTime": "2026-03-17T19:38:51Z",
      "endTime": "2026-03-17T19:40:00Z",
      "spans": [
        { "name": "stt_transcription", "duration_ms": 2100 },
        { "name": "llm_call", "duration_ms": 4640, "tokens": {...} },
        { "name": "tts_synthesis", "duration_ms": 800 }
      ]
    },
    {
      "id": "turn-2",
      "name": "patient_identification",
      "startTime": "2026-03-17T19:40:05Z",
      "endTime": "2026-03-17T19:42:30Z",
      "spans": [...]
    }
  ]
}
```

### Span Types in Voice Agent Traces

| Span Type | Duration | What It Means |
|-----------|----------|---------------|
| **stt_transcription** | 500–5000ms | Speech-to-text recognition (user speech → text) |
| **llm_call** | 1000–8000ms | LLM inference (prompt → response tokens) |
| **tool_call** | 100–2000ms | Tool execution (e.g., `check_schedule`, `book_appointment`) |
| **tts_synthesis** | 200–1000ms | Text-to-speech (agent response text → audio) |
| **vad_event** | N/A (event) | Voice activity detection (silence/speech boundary) |
| **agent_transfer** | 500–1000ms | Handoff between agents |
| **llm_cache_hit** | N/A (metadata) | Prompt cache hit on LLM call |

---

## Debugging Workflows

### Workflow 1: Identify Latency Bottlenecks

**Question**: "Why does the agent take 10 seconds to respond?"

**Steps**:
1. Export JSON trace from Langfuse
2. Find the turn with slow response
3. Sum up individual span durations:
   - STT: 2s
   - LLM: 4s
   - Tool calls: 2s
   - TTS: 1s
   - **Total: 9s (plus ~1s communication overhead)**

4. **Root cause identification**:
   - LLM taking 4s? → Cold start or large context
   - Tool calls 2s? → API timeout or database query
   - STT 2s? → Language-specific (French slower than English)

**Fix**: Reduce the largest contributor (see [[voice-agent-performance-optimization]]).

### Workflow 2: Detect Logic Errors (Loops, Wrong Routing)

**Question**: "The agent keeps asking about appointment type. Why isn't it moving to scheduling?"

**Symptoms in trace**:
- Multiple turns with same agent (e.g., "appointment_type_agent" appears 5 times)
- No progress in `UserData` variables (appointment_type never set)
- Tool calls to "check_availabilities" missing (expected but not present)

**Root cause analysis**:
1. Find the problematic agent's LLM calls
2. Check tool calls: Is "set_appointment_type" actually being called?
3. Check output: Does the tool return success?
4. Check next turn: Does the agent transition out (or repeat)?

**Fix**: Correct the agent's prompt or tool validation logic.

**Voxira Example** (2026-04-09, trace-e343622d):
- Scheduling agent got stuck checking appointment types
- Tool "check_availabilities" never called
- Root cause: Prompt said "ask which type" but never called tool to set type
- Fix: Updated prompt to mandate tool call before proceeding

### Workflow 3: Trace Agent Handoffs

**Question**: "Does the flow actually transition from Greeting → Triage → Scheduling?"

**Steps**:
1. List all turns in order, note the agent name for each
2. Plot the sequence:
   ```
   Turn 1: greeting_agent
   Turn 2: triage_agent (✓ transferred)
   Turn 3: triage_agent (✗ still in triage, didn't transfer)
   Turn 4: scheduling_agent (✓ eventually transferred)
   ```

3. Identify the gap: Why did Triage stay 2 turns instead of 1?
   - Check tool calls: Did "set_caller_intent" fire?
   - Check tool return: Did it return the expected intent?
   - Check next agent logic: Does it accept the intent?

**Voxira Example** (2026-03-30, multi-clinic testing):
- PiedReseau flow expected: Greeting → Triage → Appointment Type → Scheduling
- Actual: Greeting → Triage → Triage → Appointment Type → Scheduling → Scheduling
- Root cause: Feature flag SKIP_APPOINTMENT_TYPE_CONFIRMATION set wrong; agent looped
- Fix: Corrected dynamic feature flag in clinic config

### Workflow 4: Language-Specific Debugging (Quebec French)

**Question**: "Why is the agent not understanding the patient's name?"

**Voxira STT errors** (French):
- STT transcription: "Bonjour, mon nom est Pied Réseau"
- Recognized as: "Bonjour, mon nom est Pied Rêsault" (name mangled)
- Tool "check_name_match" fails: No record for "Rêsault"

**Debugging**:
1. Export trace
2. Find STT span; check raw text and confidence
3. Check fuzzy_match tool: What did it try to match?
4. Check database: Does patient exist under correct spelling?

**Fix** ([[quebec-french-stt-optimization]]):
- Use fuzzy matching against government name dataset
- Weight by name popularity
- Suggest matches to agent: "Did you mean Pied Réseau (popularity: 87%)"

---

## Common Patterns & Solutions

### Pattern 1: LLM Timeout (10+ Second Latency)

**Trace appearance**:
```json
{
  "name": "llm_call",
  "startTime": "...",
  "endTime": "...",  // 10+ seconds later
  "error": "OpenAI API timeout"
}
```

**Causes**:
- OpenAI API slow/overloaded
- Network connectivity issue
- Large token count (huge context)

**Solution**:
- Check OpenAI status page (https://status.openai.com/)
- Enable prompt caching to reduce token count
- Use smaller LLM model (gpt-4o-mini vs gpt-4o)

**Voxira incident** (2026-03-20):
- Multiple traces showing 10s timeouts
- Checked OpenAI status: All nominal
- Root cause: Network flake on local machine
- Fix: Operator re-ran call, succeeded

### Pattern 2: Silence Detection Gap (8+ Seconds Dead Air)

**Trace appearance**:
```json
{
  "name": "agent_transfer_to_scheduling",
  "spans": [
    { "name": "tts_synthesis", "duration_ms": 800 },  // "Transferring..."
    { "name": "vad_silence_timeout", "duration_ms": 8000 }  // Waiting for user
  ]
}
```

**Cause**: Agent transfers but doesn't immediately trigger next agent (see [[voice-agent-performance-optimization]]).

**Solution**: Implement immediate agent transfer (next agent speaks without LISTENING gap).

### Pattern 3: Tool Call Failure

**Trace appearance**:
```json
{
  "name": "tool_call_check_schedule",
  "status": "error",
  "error": "Clinic ID not found",
  "duration_ms": 150
}
```

**Debugging**:
1. Check tool parameters: Was clinic_id passed?
2. Check clinic config: Does clinic_id exist in database?
3. Check API response: What HTTP error was returned?

**Voxira example** (PiedReseau):
- Tool failed: "Unknown clinic"
- Trace showed: clinic_id = "PIEDRESEAU" (uppercase)
- Database: Stored as "piedreseau" (lowercase)
- Fix: Normalize clinic IDs to lowercase before tool calls

### Pattern 4: Wrong Intent Detected

**Trace appearance**:
```json
{
  "name": "llm_call_detect_intent",
  "output": { "intent": "reschedule" },  // Wrong!
  "expected": "schedule"
}
```

**Debugging**:
1. Check LLM prompt: Does it mention rescheduling?
2. Check user transcript: Did user say "reschedule"?
3. Check model output: Is it hallucinating?

**Voxira solution**:
- Updated intent prompt to be more explicit
- Added examples (few-shot)
- Enabled prompt caching for fast re-runs

---

## Best Practices

### For Operators (Debugging Production Issues)

1. **Export the trace immediately** (before cache eviction)
2. **Look at turn sequence first** (identify where logic breaks)
3. **Focus on LLM calls and tool calls** (most common bugs)
4. **Check clinic config** (feature flags, dynamic data)
5. **Compare to a working trace** (side-by-side diff)

### For Developers (Improving Observability)

1. **Log all tool calls** with inputs, outputs, latency
2. **Emit turn boundaries** (mark start/end of agent involvement)
3. **Tag spans with context** (clinic_id, patient_id, agent_name)
4. **Use structured logging** (JSON, not printf)
5. **Send to Langfuse** (centralized trace repository)

### For Architecture (System Design)

1. **Design for traceability**: Every operation should emit a span
2. **Use correlation IDs**: Link related requests (session → turn → tool)
3. **Instrument tool calls**: Not just outcomes, but latency and parameters
4. **Monitor in production**: Alert on p95/p99 latency thresholds
5. **Retain traces**: Archive for analysis (SLA: 30 days minimum)

---

## Tools & Resources

- **Langfuse UI** — Web interface for trace browsing and export
- **JSON export** — Download raw trace as .json for offline analysis
- **Comparison view** — Side-by-side diff of two traces (helpful for before/after)
- **Dashboards** — Langfuse provides templates for latency, error rate, token usage

---

## Related Pages

- **[[voxira]]** — Voice agent platform emitting these traces
- **[[voice-agent-performance-optimization]]** — How to fix latency issues found via tracing
- **[[healthcare-voice-agent-patterns]]** — Common agent workflows and their trace signatures
- **[[quebec-french-stt-optimization]]** — Debugging language-specific STT errors via traces

---

## Session References

Key sessions using Langfuse trace analysis:
- **2026-03-17** (session `73375c38`): Identified 5-second conversation gaps via Langfuse
- **2026-04-09** (session `6a3dae81`): Loop detection in scheduling agent using traces
- **2026-04-10** (sessions `686f7885`, `7b51fa88`): Performance profiling with trace latency data
