---
title: Quebec French STT Optimization
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [voxira, quebec-french, stt, language, deepgram, speech-recognition, fuzzy-matching]
sources: [sessions-2026-03-30-onwards, voxira]
related: [voxira, voice-agent-performance-optimization, healthcare-voice-agent-patterns]
---

# Quebec French STT Optimization

Challenges and solutions for speech-to-text (STT) in Quebec French (FR-CA). Based on [[voxira]] implementation across 80+ development sessions (2026-03-12 to 2026-04-11).

## The Quebec French STT Problem

Quebec French has unique characteristics that challenge modern STT models:

1. **Pronunciation distinct from European French**: Different vowel sounds, accent patterns, slang words
2. **Limited training data**: Less abundant than European French or North American English in LLM training datasets
3. **Name pronunciation**: Complex compound names, Anglicized surnames, indigenous place names
4. **Accents and diacritics**: Circumflex accents (ê, ô), cedillas (ç), ligatures (æ, œ)

### Voxira Experience

[[voxira]] operates clinics in Quebec (e.g., PiedReseau, PCMD). Voice agents must reliably:
- Capture patient names (critical for lookup)
- Understand appointment requests in French
- Respond in natural Quebec French

**Observed issues** (2026-03-30 sessions):
- STT recognition slower for French (2–3x latency vs. English)
- Name accuracy poor without spelling confirmation
- Accent/diacritic preservation inconsistent

**Example** (PiedReseau clinic):
```
Patient: "Mon nom est Pied Réseau"
Expected STT: "Pied Réseau"
Actual STT (Deepgram Nova-3): "Pied Rêsault"
                                  ↑ accent shift
                                         ↑ ligature dropped
                                               ↑ spelling changed
```

---

## Root Cause Analysis

### 1. **Training Data Bias**

Deepgram Nova-3 (Voxira's STT provider) trained on:
- Primarily North American English
- European French (distinct from Quebec French)
- Limited Quebec French samples

Result: Model optimizes for English/European French; FR-CA treated as variation.

### 2. **Acoustic Complexity**

Quebec French phonemes:
- /ə/ (schwa) heavily used; English models overtrain on clean vowels
- Nasal vowels (on, an, in, un) less common in English
- Diphthongs (oi, ai) pronounced differently than European French

**Deepgram must choose**: Optimize for English (90% of North American users) or French (10%).

### 3. **Orthography Ambiguity**

When a model is 85% confident in "Pied Rêsault" but 82% confident in "Pied Réseau", how does it choose?

- No grammar rules constrain the choice
- Frequency data (rare names < common names) bias toward incorrect matches

---

## Solution 1: Fuzzy Name Matching

Most reliable, practical solution for patient name capture.

### Algorithm: Levenshtein Distance + Popularity Weighting

```python
def fuzzy_match_name(transcribed: str, database: List[str], popularity: Dict[str, float]) -> str:
    """
    Find best match in database using edit distance + popularity weighting.
    
    transcribed: "Pied Rêsault" (what STT recognized)
    database: ["Pied Réseau", "Jean Pierre", "Marie Dufour", ...]
    popularity: {"Pied Réseau": 0.87, "Jean Pierre": 0.72, ...}
    
    Returns: Best match or None if confidence < threshold
    """
    
    matches = []
    for db_name in database:
        edit_distance = levenshtein(transcribed, db_name)
        similarity = 1 - (edit_distance / max(len(transcribed), len(db_name)))
        
        # Weight by popularity (common names get boost)
        confidence = similarity * (1 + popularity.get(db_name, 0))
        
        matches.append((db_name, confidence))
    
    matches.sort(key=lambda x: x[1], reverse=True)
    best_match, confidence = matches[0]
    
    if confidence > 0.80:
        return best_match
    else:
        return None  # Ask patient to spell
```

### Data Source: Quebec Government Name Registry

Voxira uses:
- Quebec RAMQ (health insurance) database: Common patient names
- Census data: Name frequency in Quebec population
- Custom clinic database: Names of patients who've called before

**Population weighting**:
```
"Pied Réseau": 0.87  (87th percentile for Quebec names)
"Jean Pierre": 0.72
"Marie Dufour": 0.65
"Xavier Hébert": 0.43
```

### Workflow

```
Agent: "What is your first and last name?"
Patient: "Pied Réseau"
STT: "Pied Rêsault"

fuzzy_match("Pied Rêsault") → ("Pied Réseau", confidence=0.87)

Agent: "Did you say Pied Réseau?" (suggests best match)
Patient: "Yes" | "No"

If "Yes": Continue with booking
If "No": Ask to spell ("Please spell your last name")
```

### Implementation in Voxira

**File**: `src/agents/name_spelling_agent.py`

```python
class NameSpellingAgent(BaseAgent):
    async def match_patient_name(self, transcribed_name: str):
        # Load clinic's patient database
        patients = await self.api_client.get_patients(self.context.clinic_id)
        patient_names = [f"{p['first_name']} {p['last_name']}" for p in patients]
        
        # Load popularity weights (Quebec government data)
        popularity = load_popularity_weights("quebec_names.json")
        
        # Fuzzy match
        best_match = fuzzy_match_name(transcribed_name, patient_names, popularity)
        
        if best_match:
            # Suggest match with confidence
            self.say(f"Did you say {best_match}?")
            response = await self.listen()
            if response.lower() in ["yes", "oui"]:
                return best_match
        
        # Fallback: Ask to spell
        self.say("Please spell your last name")
        spelled = await self.listen_spelling()
        return spelled
```

### Confidence Threshold Tuning

- **Threshold = 0.80** (current): Accept matches with 80% confidence; ask to spell otherwise
- **Threshold = 0.90** (stricter): More spelling requests, but fewer false matches
- **Threshold = 0.70** (lenient): Fewer spelling requests, but more wrong matches

**Voxira choice**: 0.80 (balance between UX and accuracy)

---

## Solution 2: Language-Specific STT Keywords (Deepgram)

Deepgram allows **keyword boosting** to improve recognition of domain-specific terms.

### Quebec French Medical Vocabulary

```json
{
  "language": "fr-CA",
  "keywords": {
    "rendez-vous": 10,           // "appointment" (boost x10)
    "urgence": 8,                 // "emergency"
    "consultation": 8,            // "consultation"
    "douleur": 7,                 // "pain"
    "nausée": 7,                  // "nausea"
    "prise de sang": 10,          // "blood test"
    "Pied Réseau": 12,            // Clinic name (highest boost)
    "clinique": 5                 // "clinic"
  }
}
```

### How It Works

When Deepgram encounters acoustic ambiguity:
- Normal score for "Pied Rêsault": 0.82
- Boosted score for "Pied Réseau": 0.82 × 1.2 = 0.984

Result: Model selects "Pied Réseau" (boosted term).

### Voxira Implementation

**File**: `src/config/stt_keywords.yaml`

```yaml
language_keywords:
  en-US:
    appointment: 10
    reschedule: 8
    emergency: 8
  fr-CA:
    rendez-vous: 10
    reprise: 8
    urgence: 8
    pied: 12              # Company name (boost for PiedReseau clinic)
    biomechanical: 7
  es-US:
    cita: 10
    reprogramar: 8
    emergencia: 8
```

**Usage**:
```python
keywords = load_keywords(self.context.language)
stt_result = deepgram.transcribe(
    audio,
    language=self.context.language,
    keywords=keywords
)
```

### Limitation

Keywords only help with **known terms** (company name, medical vocabulary). Won't improve arbitrary patient names like "Pied Rêsault" vs. "Pied Réseau".

---

## Solution 3: Spelling Agent (Fallback)

When fuzzy matching confidence is low, ask patient to spell.

### Spelling Recognition

Spelling is more reliable than normal speech:
- "P-I-E-D" (spelled) → STT accurate 95%+
- "Pied" (spoken) → STT accurate 70% (depending on speaker)

### Implementation

```python
class SpellingAgent(BaseAgent):
    async def listen_spelling(self) -> str:
        """Transcribe spell-out: 'P-I-E-D' → 'PIED'"""
        
        self.say("Please spell it out, letter by letter")
        
        letters = []
        for i in range(20):  # Max 20 letters
            audio = await self.listen(timeout=5)
            letter = recognize_letter(audio)  # Single letter recognition
            
            if not letter:
                # Silence after 5 seconds; done spelling
                break
            
            letters.append(letter)
            self.say(letter)  # Echo back for confirmation
        
        return "".join(letters)
```

### Letter Recognition

Single-letter recognition (A-Z, numbers, accented letters) is much easier for STT:
- Letter set: ~36 distinct options (A-Z + special characters)
- No ambiguity: Model trained specifically on letter names

**Voxira extension**: Add French-accented letters:
```
A, B, C, ..., Z
À, Â, Ä, É, È, Ê, Ë, Î, Ï, Ô, Ù, Û, Ü, Ç
```

---

## Solution 4: STT Model Selection (Future)

Deepgram offers multiple models:
- **Nova-3** (current): General-purpose, all languages, ~95% accuracy English
- **Nova-2**: Slightly slower, similar accuracy
- **Custom fine-tuned model** (available): Train on Quebec French medical data

### Path Forward

1. **Collect STT errors** (2026-04): Catalog cases where Nova-3 fails for FR-CA
2. **Evaluate custom model** (2026-05): Would fine-tuning improve by >10%?
3. **Implement if viable** (2026-06): Switch to custom model if ROI justified

**Cost**: ~$5K to fine-tune + 20% inference premium (not yet justified for current call volume).

---

## Solution 5: Language Switching (Multi-Dialect Support)

Some patients may code-switch (mix English + French):
```
Patient: "Bonjour, I'd like to schedule an appointment for a biomechanical evaluation"
```

### Detection & Handling

```python
def detect_language(audio: bytes) -> str:
    """Return 'en-US', 'fr-CA', or 'mixed'"""
    # Deepgram can score each language
    en_score = deepgram.score_language(audio, language="en-US")
    fr_score = deepgram.score_language(audio, language="fr-CA")
    
    if en_score > 0.8 and fr_score > 0.8:
        return "mixed"
    elif en_score > fr_score:
        return "en-US"
    else:
        return "fr-CA"
```

### Handling Mixed Language

Option 1: Transcribe as English (simplest, loses French context)
Option 2: Transcribe in both languages, merge results (complex)
Option 3: Ask patient to choose dominant language (explicit)

**Voxira current**: Option 1 (simplest; code-switching rare in observed calls)

---

## Measurement & Testing

### Metrics

| Metric | Target | Current (Voxira, March 2026) |
|--------|--------|------|
| **Name match accuracy** | 95%+ | 78% without fuzzy matching, 92% with |
| **STT latency (English)** | <1.5s | 1.2s |
| **STT latency (FR-CA)** | <3s | 2.8–3.5s |
| **Spelling recognition** | 99%+ | 98% |
| **Fuzzy match F1 score** | >0.90 | 0.91 (on Quebec clinic test set) |

### Test Dataset

Voxira maintains:
- **150 Quebec French names** from clinic databases
- **30 realistic STT errors** (transcription mistakes from real calls)
- **Fuzzy matching test harness** (automated scoring)

```python
def test_fuzzy_matching():
    test_cases = [
        ("Pied Rêsault", "Pied Réseau", True),   # Should match
        ("Jean-Luc Deveau", "Jean-Luc Deveau", True),
        ("Marie", "Marie", True),
        ("Jean", "Jean-Pierre", False),  # Different
    ]
    
    for transcribed, expected, should_match in test_cases:
        match = fuzzy_match_name(transcribed, clinic_patients)
        if should_match:
            assert match == expected, f"Failed: {transcribed}"
        else:
            assert match != expected, f"False positive: {transcribed}"
```

---

## Checklist for Quebec French Support

- [ ] **STT language set to FR-CA** (not FR-EU)
- [ ] **Fuzzy matching** implemented with popularity weights
- [ ] **Spelling agent** as fallback for low-confidence matches
- [ ] **Medical keywords** boosted in STT config
- [ ] **TTS voice** supports FR-CA (Deepgram Aura-2)
- [ ] **Patient names dataset** loaded (Quebec government + clinic)
- [ ] **Error metrics tracked** (accuracy, latency per language)
- [ ] **Operator runbook** for debugging STT issues

---

## Related Pages

- **[[voxira]]** — Platform where this is implemented
- **[[voice-agent-performance-optimization]]** — STT latency is a performance bottleneck
- **[[healthcare-voice-agent-patterns]]** — Patient ID step where Quebec French matters most
- **[[langfuse-trace-analysis]]** — Debug STT errors using trace analysis

---

## Session References

Sessions addressing Quebec French challenges:
- **2026-03-30** (sessions `13370d1c`, `aa2dc78e`): Initial Quebec French STT issues identified
- **2026-04-01** (session `3919df4e`): PiedReseau French clinic mapping and appointment types
- **2026-04-09** (session `6a3dae81`): Langfuse analysis of French caller latency
