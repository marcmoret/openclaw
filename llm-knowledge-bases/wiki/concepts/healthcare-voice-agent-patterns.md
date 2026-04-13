---
title: Healthcare Voice Agent Patterns
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [voxira, healthcare, voice-agent, hipaa, patient-identification, scheduling, multi-tenant]
sources: [sessions-2026-03-12-onwards, voxira]
related: [voxira, quebec-french-stt-optimization]
---

# Healthcare Voice Agent Patterns

Design patterns for conversational voice agents in healthcare settings. Based on [[voxira]], a multi-tenant scheduling system for medical clinics.

## Problem Domain

Healthcare voice agents must:
1. **Comply with HIPAA** (U.S.) and equivalent privacy laws (Canada, EU)
2. **Identify patients** reliably (name, DOB, insurance, residence)
3. **Route calls** appropriately (scheduling vs. emergency vs. human handoff)
4. **Handle multi-clinic tenancy** (each clinic has different workflows, EMR integrations, languages)
5. **Work across languages** (English, French, Spanish)
6. **Maintain state** across agent handoffs (e.g., collected name → passed to scheduling agent)

---

## Common Call Flow Patterns

### Pattern 1: Simple Clinic (Linear Flow)

```
Greeting Agent (clinic hours check)
    ↓ (consent recorded)
Patient ID Agent (collect name, DOB, phone)
    ↓ (identity confirmed)
Intent Router Agent (schedule? reschedule? general question?)
    ↓ (intent detected)
Scheduling Agent (book appointment)
    ↓
End Call Agent (confirm, summarize)
```

**Voxira clinics using this**:
- PCMD (primary clinic in traces)
- Savaria (orthopedic scheduling)

**Agents required**: 5

**Configuration**: Static agent sequence in `session_stack` field.

### Pattern 2: Complex Multi-Flow Clinic (Branching)

```
Greeting Agent
    ↓
Triage Agent (symptom assessment → appointment type recommendation)
    ├─ (emergency detected) → Emergency Transfer Agent → Call 911 prompt
    ├─ (non-emergency) → Patient ID Agent → Scheduling Agent
    └─ (general inquiry) → FAQ Agent → End Call
```

**Voxira clinic using this**: PiedReseau (podiatry, requires triage before scheduling)

**Agents required**: 6–7

**Configuration**: Flow graph model with conditional edges (if emergency → emergency agent, else → patient ID)

### Pattern 3: Multi-Language Clinic

```
Language Selector Agent (detect caller language from opening phrase)
    ↓ (language determined)
[Greeting, Patient ID, Intent, Scheduling] agents × 3 (English, French, Spanish)
    ↓
End Call (in caller's language)
```

**Implementation**:
- Detect language in opening phrase (Deepgram can transcribe and identify language)
- Set `UserData.language` and pass to all downstream agents
- Each agent uses language-specific prompts (loaded from YAML)
- TTS voice selected per language (Deepgram Aura supports en-US, fr-CA, es-US)

**Voxira setup**: Uses Deepgram for language detection, OpenAI for LLM responses.

---

## HIPAA Consent Flow (Mandatory First Step)

All healthcare voice agents must obtain explicit consent before processing patient information.

### Consent Capture

```
System plays: "This call may be recorded for quality and training purposes. 
Do you consent to recording?"

Patient responds: "Yes" | "No"

If "No" → End call immediately
If "Yes" → Continue to Patient ID
```

**Implementation in Voxira**:
- `RecordingConsentAgent` handles this step
- Tool: `record_consent(consent: bool, timestamp, phone_number)`
- Consent logged to database and linked to call session
- All downstream processing requires consent = True

### Patient Privacy Considerations

1. **PII collection**: Only collect name, DOB, phone, address as needed
2. **Verification**: Always confirm identity before accessing appointment records
3. **Storage**: Encrypt PII at rest, delete after retention period (e.g., 90 days)
4. **Access logs**: Track who accessed patient data when
5. **Data minimization**: Don't ask for insurance details unless scheduling at a clinic that requires it

---

## Patient Identification Patterns

### Challenge: Accurate Name Recognition with STT Errors

Speech-to-text (STT) is error-prone, especially for:
- Non-English names
- Quebec French pronunciation (see [[quebec-french-stt-optimization]])
- Background noise (clinic environment)

### Pattern 1: Confirmation Loop

```
Agent: "What is your first name?"
Patient: "Jean-Pierre"
STT result: "John Pierre" (error)

Agent: "Did you say John Pierre?"
Patient: "No, Jean-Pierre" (spelling it out)
STT result: "J-E-A-N dash P-I-E-R-R-E"

Agent: "Jean-Pierre, is that correct?"
Patient: "Yes"

→ Proceed
```

**Tradeoff**: Safe but slow (3–4 extra turns). Frustrating for patients.

### Pattern 2: Fuzzy Name Matching (Quebec French)

```
Agent: "What is your first name?"
Patient: "Pied Réseau"
STT result: "Pied Rêsault" (incorrect accent, dropped ligature)

Agent calls: fuzzy_match(transcribed="Pied Rêsault", database=clinic_patients)
Database match: "Pied Réseau" (popularity score: 87%)

Agent: "Did you mean Pied Réseau?"
Patient: "Oui"

→ Proceed
```

**Implementation in Voxira** (see [[quebec-french-stt-optimization]]):
- Uses government name dataset (Quebec, Canada)
- Weights matches by name popularity (common names > rare names)
- Suggests top match if confidence >80%

**Benefit**: Faster, more natural.

### Pattern 3: Name Spelling Agent

```
Agent: "Please spell your last name"
Patient: "R-E-S-E-A-U"
STT result: "R-E-S-E-A-U" (usually accurate for spelled words)

Agent: "RESEAU, correct?"
Patient: "Yes"

→ Database lookup: Exact match
```

**When to use**: When fuzzy matching confidence < 60% or patient explicitly asks to spell.

---

## Multi-Tenant Configuration Patterns

### Challenge: Each Clinic Has Different Workflows

- **Clinic A**: Scheduling → Insurance → Confirmation
- **Clinic B**: Patient ID → Triage → Insurance → Scheduling
- **Clinic C**: Insurance required *only* for new patients

**Solution**: Dynamic clinic configuration, not hardcoded agent sequences.

### Voxira's Approach: Feature Flags + Flow Graph

**1. Static Feature Flags** (set once per clinic):
```json
{
  "clinic_id": "piedreseau",
  "clinic_type": "podiatry",
  "language": "fr-CA",
  "SKIP_FIRST_NAME_CONFIRMATION": "YES",
  "ENABLE_TRIAGE_AGENT": "YES",
  "REQUIRE_INSURANCE_NEW_PATIENTS_ONLY": "YES"
}
```

**2. Dynamic Flow Graph** (edited via dashboard UI):
```
┌─────────────────────┐
│ Greeting Agent      │
│ (clinic hours)      │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Triage Agent        │  ← conditional: if emergency → redirect
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Patient ID Agent    │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Appt Type Agent     │  ← show appointment types for clinic
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Scheduling Agent    │  ← call clinic's EMR API
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ End Call Agent      │
└─────────────────────┘
```

**Database schema** (simplified):
```sql
CREATE TABLE call_flows (
  id INT PRIMARY KEY,
  clinic_id INT,
  name VARCHAR(100),        -- "Default", "After Hours"
  is_active BOOLEAN
);

CREATE TABLE call_flow_nodes (
  id INT PRIMARY KEY,
  flow_id INT,
  agent_type VARCHAR(50),   -- 'greeting', 'patient_id', 'scheduling', etc.
  name VARCHAR(100),        -- User-friendly label
  prompt TEXT,              -- Agent's system prompt (can be customized)
  position_x INT, position_y INT  -- For flow diagram UI
);

CREATE TABLE call_flow_edges (
  id INT PRIMARY KEY,
  from_node_id INT,
  to_node_id INT,
  condition TEXT,           -- Optional: "if emergency" or null (always proceed)
  label VARCHAR(100)        -- "Yes", "No", "Reschedule", etc.
);
```

### Configuration Lifecycle

1. **Create flow** (via dashboard or API)
2. **Assign to clinic** in `dynamic_feature_flags`
3. **Fetch at call start**: `GET /api/v1/clinic/{clinic_id}/flow`
4. **Execute flow** in LiveKit agent (read edges, evaluate conditions, route)
5. **Update config** (zero downtime; fetches happen per-call)

---

## Appointment Scheduling Patterns

### Pattern 1: EMR-Agnostic Scheduling Service

Problem: Each EMR (Electronic Medical Record) system has different APIs.

Solution: Abstract EMR into `SchedulingService` interface:

```python
class SchedulingService(ABC):
    def get_availabilities(self, appointment_type: str, date: str) -> List[Slot]: ...
    def book_appointment(self, patient_info: Dict, appointment_type: str, slot: str) -> Confirmation: ...

class SavariaSchedulingService(SchedulingService):
    # Implements Savaria EMR API

class OmniSchedulingService(SchedulingService):
    # Implements Omni EMR API

class GoogleCalendarSchedulingService(SchedulingService):
    # For testing/fake EMR (beta)
```

**In agent**:
```python
class SchedulingAgent(BaseAgent):
    async def handle_book_appointment(self, appointment_type: str, date: str):
        service = get_scheduling_service(self.context.clinic_type)
        availabilities = await service.get_availabilities(appointment_type, date)
        # Present to user, book selected slot
```

**Benefit**: Add new EMR by implementing one interface; no agent code changes.

### Pattern 2: Appointment Type Mapping

Problem: Clinics use different terminology for appointment types.

Solution: Map appointments per clinic:

**Voxira example** (PiedReseau, from Excel):

| Appointment Type | Duration | Price | Criteria |
|------------------|----------|-------|----------|
| Biomécanique (N-BIO) | 30 min | $X | New patient, biomechanical assessment |
| Biomécanique (BIO) | 30 min | $X | Returning patient, assessment |
| Orthèses (Modification) | 20 min | $X | Modify existing orthotics |
| Follow-up (Suivi) | 20 min | Free | Post-appointment follow-up |

**Storage** (YAML or DB):
```yaml
clinic: piedreseau
appointment_types:
  - name: "Biomécanique (N-BIO)"
    duration_minutes: 30
    price: 150
    criteria: "new_patient=true"
  - name: "Suivi"
    duration_minutes: 20
    price: 0
    criteria: null
```

**Agent logic**:
```python
appointment_types = load_appointment_types(clinic_id)
# Filter by patient status (new vs. returning)
available_types = [t for t in appointment_types if matches(patient, t.criteria)]
# Present to user, get selection
```

---

## Multi-Language Support Patterns

### Pattern 1: Language Detection on First Input

```python
# User speaks: "Bonjour, je m'appelle..."
stt_result = deepgram.transcribe(audio)
language = deepgram.detect_language(audio)  # "fr-CA"

context.language = language
context.prompts = load_prompts(language)  # Load FR-CA prompts
context.tts_voice = get_tts_voice(language)  # "fr-CA-Aura-voice"
```

### Pattern 2: Language-Specific Prompts

```
prompts/
  ├─ en-US/
  │  ├─ greeting.yaml
  │  ├─ patient_id.yaml
  │  └─ scheduling.yaml
  ├─ fr-CA/
  │  ├─ greeting.yaml    ("Bonjour, bienvenue à...")
  │  ├─ patient_id.yaml
  │  └─ scheduling.yaml
  └─ es-US/
     ├─ greeting.yaml
     ├─ patient_id.yaml
     └─ scheduling.yaml
```

**Usage**:
```python
prompt = load_prompt(f"prompts/{context.language}/greeting.yaml")
agent.system_prompt = prompt
```

### Pattern 3: Language-Specific STT Keywords (Deepgram)

Boost recognition accuracy for domain-specific words:

```python
keywords = {
  "en-US": ["appointment", "reschedule", "emergency"],
  "fr-CA": ["rendez-vous", "reprise", "urgence"],
  "es-US": ["cita", "reprogramar", "emergencia"]
}

stt = deepgram.transcribe(
  audio,
  language=context.language,
  keywords=keywords[context.language]
)
```

---

## Error Handling & Fallback Patterns

### Pattern 1: Unidentified Patient

```
Agent: "I couldn't find your record. Can you say your date of birth?"
Patient: "January 15, 1985"
STT: "January 15, 1985"
Lookup: Found 3 matches (same DOB, different names)

Agent: "Is your name John Smith, Jane Smith, or Jack Smith?"
Patient: "Jane Smith"

→ Proceed
```

### Pattern 2: Emergency Detection & Transfer

```
Triage Agent listens for keywords: "chest pain", "difficulty breathing", "bleeding", etc.

If emergency detected:
  Agent: "Please call 911 immediately or go to the nearest emergency room."
  → End call (do not attempt to schedule)
```

### Pattern 3: Graceful Degradation (Fallback to Human)

```
If any step fails (schedule API timeout, patient not found, etc.):
  Agent: "Let me transfer you to a human representative."
  → Cold transfer to live clinic staff via Twilio
```

---

## Implementation Checklist

- [ ] **HIPAA consent** captured and logged per call
- [ ] **Patient ID** collected with confirmation (spelling or fuzzy match)
- [ ] **Flow graph** configurable per clinic (no hardcoded sequences)
- [ ] **Feature flags** injectable at call time
- [ ] **EMR abstraction** (SchedulingService interface)
- [ ] **Appointment mapping** per clinic (YAML or DB)
- [ ] **Language detection** on first input
- [ ] **Language-specific prompts** for all agents
- [ ] **Langfuse observability** for debugging
- [ ] **Error handling** for patient not found, schedule unavailable, emergency
- [ ] **Fallback to human** for escalation

---

## Related Pages

- **[[voxira]]** — Production platform implementing these patterns
- **[[voice-agent-performance-optimization]]** — Latency optimization during patient ID steps
- **[[quebec-french-stt-optimization]]** — Language-specific name matching
- **[[langfuse-trace-analysis]]** — Debugging patient ID failures via traces

---

## Session References

Sessions contributing to this concept:
- **2026-03-12** (sessions `884b1bc4`, `144b8b0d`): Initial architecture and multi-tenant design
- **2026-03-16** (session `b87ebc9e`): Comprehensive feature planning
- **2026-04-01** (session `3919df4e`): Clinic-specific appointment mapping (PiedReseau)
- **2026-03-30** (sessions `13370d1c`, `aa2dc78e`): Multi-clinic testing and feature flags
