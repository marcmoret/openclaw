---
title: Voice Agent Performance Optimization
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [voxira, latency, performance, optimization, voice-agent, livekit]
sources: [sessions-2026-03-17-onwards, langfuse-trace-analysis]
related: [voxira, langfuse-trace-analysis, livekit]
---

# Voice Agent Performance Optimization

Strategies for reducing latency in conversational voice agents. Based on analysis of [[voxira]] development across 20+ sessions (2026-03-17 to 2026-04-11).

## The Latency Problem

Voice agents in healthcare environments must feel responsive. Long pauses (>2–3 seconds) between user input and agent response degrade user experience and confuse callers about whether the line is still active.

### Observed Issues in Voxira

**Silence Detection Gaps (8–9 seconds)**
- After agent completes a transition phrase (e.g., routing from one agent to another), system enters LISTENING state
- User doesn't know they should speak yet
- VAD (voice activity detection) silence threshold (~8–9 seconds) triggers, firing a "Developer Turn"
- Result: ~9 second dead air before next agent greets

**LLM TTFT (Time To First Token) on Cold Starts (4–8 seconds)**
- First LLM call in a conversation: 4.64 seconds on trace-6c08cea1
- Subsequent calls faster (~1–2 seconds once prompt cache warms)
- OpenAI API calls sometimes timeout entirely (~10 seconds)
- Quebec French STT produces slower latency than English (root cause unclear; possible Deepgram model difference)

**Agent Switching Overhead**
- Routing between agents (e.g., Greeting → Triage → Scheduling) adds state transitions
- Each handoff may require new LLM context assembly

---

## Root Causes

### 1. **Silence Detection Not Tuned for Agent Transfers**

**Issue**: When `route_patient()` or `set_caller_intent()` tools fire, agent says a brief transition phrase ("transferring now") and goes silent. System waits 8–9 seconds for user input that may never come, because the caller is confused.

**Mechanism** (LiveKit VAD):
- Agent finishes speech → enters LISTENING state
- Silence threshold (default ~8 seconds) waits for voice activity
- No user input arrives within threshold → VAD fires Developer Turn
- Next agent starts speaking only after timeout

**Why it matters**: Every agent transfer loses 8–9 seconds of interactivity.

### 2. **Cold Start LLM Latency**

**Issue**: First LLM call in a session has high TTFT (first token arrival time). Subsequent calls faster due to prompt caching.

**Mechanism**:
- First OpenAI call: Model context not cached, full prompt must be tokenized and processed
- Prompt caching (OpenAI API feature): Caches up to 128K tokens of prompt, amortizes across multiple calls
- Without caching: Every call pays full latency cost
- With caching: Warmup cost on first call, then ~3x speedup on subsequent calls

**Trace Evidence** (2026-03-17):
- Trace-6c08cea1: First LLM call = 4.64s TTFT
- Subsequent calls: 1–2 seconds
- Session with cached prompt: faster overall

### 3. **STT Latency (Especially Quebec French)**

**Issue**: Deepgram STT produces slower recognition times for Quebec French vs. English.

**Mechanism**:
- Deepgram Nova-3 model may have different inference speed per language
- Quebec French rare in training data compared to North American English
- Model may require longer acoustic processing for FR-CA phonemes

**Evidence** (2026-04-09):
- Session trace-706e2c3c (French caller): Large gaps between caller speech and agent response
- Session with English caller: Noticeably quicker recognition
- Hypothesis: Deepgram model speed, not network latency

---

## Solutions & Workarounds

### 1. **Immediate Agent Transfer (No Silence Detection)**

**Best Fix**: When an agent tool (`route_patient`, `set_caller_intent`) signals a transfer, don't enter LISTENING state. Instead, trigger the next agent's turn immediately in the same LLM response.

**Implementation** (Python/LiveKit Agents):
```python
# Instead of:
self.say("Transferring to scheduling agent...")
# Then goes silent, waits for user

# Do this:
self.say("Transferring to scheduling agent...")
next_agent.process(context)  # Continue immediately
# Next agent speaks without gap
```

**Benefit**: Eliminates 8–9 second dead air on agent transitions.

**Tradeoff**: Requires careful context handoff; next agent must receive full state from previous agent.

### 2. **Prompt Caching for LLM TTFT**

**Strategy**: Use OpenAI's prompt caching feature to cache static prompt sections across calls.

**How it works**:
- Mark cacheable prompt sections with special tokens (OpenAI API)
- First call: Full prompt processed, ~4 seconds TTFT
- Subsequent calls: Cache hit, ~1 second TTFT (3x faster)

**Voxira Implementation** (2026-03-17 session):
- Cache agent prompts, system context, function definitions
- Only pass dynamic state (user transcript, variables) as uncached input
- Result: Warm calls 3–4x faster than cold calls

**Cost Note**: Prompt caching incurs 25% premium on cache writes but saves 90% on cache reads. Worth it for repeated intents.

### 3. **Silence Threshold Tuning**

**Short-term workaround** (while implementing immediate agent transfer):
- Reduce `silence_trigger_threshold` from 8–9 seconds to 2–3 seconds
- Caller speaks sooner; system times out earlier

**Tradeoff**: Risk of false timeouts if caller is thinking (pauses mid-sentence).

**Better**: Use **adaptive silence thresholds** — reduce threshold only after agent transfer phrases are detected.

### 4. **Concurrent Context Preprocessing**

**Strategy**: Assemble next agent's context while current agent is still speaking.

**Implementation**:
- Current agent speaks ("transferring...")
- In parallel, fetch clinic config, schedule data, patient history
- When current agent finishes, next agent context is ready
- Result: No waiting for I/O during handoff

**Benefit**: Reduces handoff latency from ~500ms (serial) to ~100ms (parallel).

### 5. **Quebec French STT Optimization**

**Workaround** (until Deepgram improves):
- Use [[quebec-french-stt-optimization|fuzzy name matching]] to recover from STT errors
- When STT confidence is low for name field, ask for spelling
- Spelling agent uses fuzzy matching against government name dataset

**Long-term**: Monitor Deepgram model updates; FR-CA model may improve over time.

---

## Measurement & Monitoring

### Key Metrics

| Metric | Target | Current (Voxira) | Notes |
|--------|--------|------------------|-------|
| **Silence Detection Gap** | <1s | 8–9s | After agent transfers |
| **LLM TTFT (Cold)** | <2s | 4–8s | First call in session |
| **LLM TTFT (Warm)** | <1s | 1–2s | With prompt caching |
| **STT Recognition Time** | <1s | 1–3s (English), 3–5s (French) | Depends on language & model |
| **Agent Handoff Latency** | <500ms | ~500ms (serial), ~100ms (concurrent) | With preprocessing |
| **End-to-End (Greeting → Schedule)** | <30s | 45–60s | Full call flow (current) |

### Langfuse Tracing

[[voxira]] uses [[langfuse-trace-analysis|Langfuse]] to track every span:
- **LLM call spans**: Input tokens, output tokens, TTFT, latency
- **Tool call spans**: Start → completion time
- **Turn spans**: User speech → agent response (wall-clock latency)
- **VAD spans**: Silence detection events, threshold triggers

**Debugging workflow**:
1. Export JSON trace from Langfuse UI
2. Search for long gaps (>2s between spans)
3. Identify bottleneck: Is it LLM? STT? Tool I/O?
4. Optimize accordingly

---

## Implementation Priority

### Phase 1 (Immediate) — High Impact, Low Effort
1. **Reduce silence threshold** (2–3s instead of 8–9s)
2. **Enable prompt caching** in OpenAI calls
3. **Monitor with Langfuse** to baseline metrics

### Phase 2 (Next Sprint) — Medium Impact, Medium Effort
4. **Implement immediate agent transfer** (no LISTENING gap)
5. **Concurrent context preprocessing** (parallel I/O during handoff)

### Phase 3 (Future) — Investigate
6. **Quebec French STT**: Monitor Deepgram model updates
7. **Custom VAD tuning**: Train or adapt VAD models for healthcare domain

---

## References & Related Pages

- **[[voxira]]** — Voice agent platform where these optimizations were identified and applied
- **[[langfuse-trace-analysis]]** — How to debug latency using Langfuse JSON traces
- **[[quebec-french-stt-optimization]]** — Language-specific STT challenges
- **LiveKit Agents Framework** — Agent framework underlying Voxira
- **OpenAI Prompt Caching** — API documentation for cache-control headers

---

## Session References

Sessions contributing to this concept:
- **2026-03-17**: Trace analysis, silence detection root cause (session `73375c38`)
- **2026-04-09**: Loop detection, trace debugging (session `6a3dae81`)
- **2026-04-10**: Performance optimization sprint (sessions `686f7885`, `7b51fa88`, `d1bd0690`, `f485d5cc`)
