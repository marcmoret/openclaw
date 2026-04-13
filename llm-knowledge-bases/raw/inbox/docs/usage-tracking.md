# Usage Tracking System

## Overview

The usage tracking system provides comprehensive monitoring of AI model usage across a LiveKit voice agent session. It tracks token consumption, audio duration, and character counts for LLM, STT, and TTS services, enabling accurate cost calculation and usage auditing.

## Architecture

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Usage Tracking Flow                       │
└─────────────────────────────────────────────────────────────┘

LiveKit Agent          External API          Usage Collector
     │                      │                        │
     │──metrics_collected──>│                        │
     │                      │                        │
     │                      │──track_external_llm──>│
     │                      │                        │
     └──────────────────────┴────────────────────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │  ModelKey Based │
                          │  Aggregation    │
                          └─────────────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │ Usage Summary   │
                          │ & Breakdown     │
                          └─────────────────┘
```

### 1. MultiModelUsageCollector

**Location:** `src/utils/multi_model_usage_collector.py`

The central component that aggregates usage metrics from multiple sources.

#### Key Features

- **Per-Model Tracking**: Tracks usage separately for each unique model/provider combination
- **Source Differentiation**: Distinguishes between LiveKit agent calls (`livekit_agent`) and external API calls (`external_api`)
- **Automatic Model Detection**: Detects model changes during a call session
- **Backward Compatible**: Maintains compatibility with LiveKit's `UsageCollector` API

#### Data Structures

```python
@dataclass(frozen=True)
class ModelKey:
    """Unique identifier for tracking a specific model"""
    provider: str        # e.g., "openai", "Deepgram", "ElevenLabs"
    model: str          # e.g., "gpt-4o", "nova-2", "eleven_turbo_v2"
    source: str         # "livekit_agent" or "external_api"
```

**Key Format:** `{source}:{provider}/{model}`
- Example: `external_api:openai/gpt-4o`
- Example: `livekit_agent:api.openai.com/gpt-4o-mini`

#### Usage Tracking Models

**LLM Usage:**
```python
@dataclass
class LLMUsage:
    prompt_tokens: int
    prompt_cached_tokens: int
    completion_tokens: int
    input_audio_tokens: int      # For multimodal models
    input_text_tokens: int
    input_image_tokens: int
    output_audio_tokens: int
    output_text_tokens: int
```

**STT Usage:**
```python
@dataclass
class STTUsage:
    audio_duration: float  # In seconds
```

**TTS Usage:**
```python
@dataclass
class TTSUsage:
    characters_count: int
    audio_duration: float  # In seconds
```

### 2. Integration Points

#### LiveKit Agent Metrics

The collector automatically receives metrics from LiveKit agents via the `metrics_collected` event:

```python
# In session_utils.py
usage_collector = MultiModelUsageCollector()

def _on_metrics_collected(ev: MetricsCollectedEvent):
    usage_collector.collect(ev.metrics)

agent_session.on("metrics_collected", _on_metrics_collected)
```

**Supported Metric Types:**
- `LLMMetrics` - Standard LLM completions
- `RealtimeModelMetrics` - Real-time audio/multimodal models
- `STTMetrics` - Speech-to-text transcription
- `TTSMetrics` - Text-to-speech synthesis

#### External API Tracking

For LLM calls made outside the LiveKit agent (e.g., for data extraction, analysis):

```python
# In llm_service.py
self.usage_collector.track_external_llm_usage(
    provider="openai",
    model="gpt-4o",
    prompt_tokens=prompt_tokens,
    completion_tokens=completion_tokens,
    cached_tokens=cached_tokens,
    source="external_api"  # Explicitly marks as external
)
```

### 3. Usage Summary Output

The collector provides two levels of detail:

#### Aggregated Summary

```python
summary = usage_collector.get_summary()
# Returns UsageSummary with totals across all models:
# - llm_prompt_tokens
# - llm_completion_tokens
# - llm_prompt_cached_tokens
# - stt_audio_duration
# - tts_characters_count
# - tts_audio_duration
```

#### Detailed Breakdown

```python
detailed = usage_collector.get_detailed_summary()
```

**Output Structure:**
```json
{
  "totals": {
    "llm_prompt_tokens": 15000,
    "llm_completion_tokens": 8000,
    "llm_prompt_cached_tokens": 2000,
    "stt_audio_duration": 120.5,
    "tts_characters_count": 5000,
    "tts_audio_duration": 60.2
  },
  "llm_models": {
    "external_api:openai/gpt-4o": {
      "source": "external_api",
      "provider": "openai",
      "model": "gpt-4o",
      "prompt_tokens": 10000,
      "completion_tokens": 5000,
      "prompt_cached_tokens": 0,
      "total_tokens": 15000
    },
    "livekit_agent:api.openai.com/gpt-4o-mini": {
      "source": "livekit_agent",
      "provider": "api.openai.com",
      "model": "gpt-4o-mini",
      "prompt_tokens": 5000,
      "completion_tokens": 3000,
      "prompt_cached_tokens": 2000,
      "total_tokens": 8000
    }
  },
  "stt_models": {
    "livekit_agent:Deepgram/nova-2": {
      "source": "livekit_agent",
      "provider": "Deepgram",
      "model": "nova-2",
      "audio_duration": 120.5
    }
  },
  "tts_models": {
    "livekit_agent:ElevenLabs/eleven_turbo_v2": {
      "source": "livekit_agent",
      "provider": "ElevenLabs",
      "model": "eleven_turbo_v2",
      "characters_count": 5000,
      "audio_duration": 60.2
    }
  },
  "model_count": {
    "llm": 2,
    "stt": 1,
    "tts": 1,
    "total": 4
  }
}
```

## Implementation Guide

### Setting Up Usage Tracking

**1. Initialize in Session Setup**

```python
# Create collector
usage_collector = MultiModelUsageCollector()

# Store in UserData for access across agents
userdata.set_usage_collector(usage_collector)

# Connect to agent session
def _on_metrics_collected(ev: MetricsCollectedEvent):
    usage_collector.collect(ev.metrics)

agent_session.on("metrics_collected", _on_metrics_collected)
```

**2. Track External API Calls**

```python
# In LLMService
class LLMService:
    def __init__(self, openai_client, session_id, usage_collector):
        self.usage_collector = usage_collector

    def _track_completion_usage(self, completion, model):
        if not self.usage_collector:
            return

        usage = completion.usage
        self.usage_collector.track_external_llm_usage(
            provider="openai",
            model=model,
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            cached_tokens=usage.prompt_tokens_details.cached_tokens,
            source="external_api"
        )
```

**3. Retrieve Usage Data**

```python
# At end of call (in shutdown handler)
usage_summary = usage_collector.get_detailed_summary()

# Log to Langfuse for observability
langfuse_trace.event(
    name="Usage Summary",
    input=usage_summary
)
```

## Best Practices

### 1. Source Attribution

Always explicitly set the `source` parameter:
- Use `"external_api"` for direct OpenAI API calls
- Use `"livekit_agent"` (default) for LiveKit agent usage

### 2. Error Handling

Wrap usage tracking in try-except blocks to prevent tracking failures from affecting the call:

```python
try:
    self.usage_collector.track_external_llm_usage(...)
except Exception as e:
    logger.error(f"Failed to track usage: {e}", exc_info=True)
```

### 3. Model Naming Consistency

Maintain consistent model naming across your application:
- LiveKit uses provider domains: `api.openai.com/gpt-4o`
- External calls use simple names: `openai/gpt-4o`

### 4. Cached Token Tracking

Always track cached tokens separately for accurate cost calculation:
```python
cached_tokens = usage.prompt_tokens_details.cached_tokens or 0
```

## Troubleshooting

### Issue: Missing Metadata Warning

**Symptom:**
```
WARNING: Metrics metadata missing for llm, using fallback
```

**Cause:** LiveKit metrics event missing model provider/name metadata

**Solution:** Ensure LiveKit agents are configured with proper metadata, or the fallback will use the label field.

### Issue: Duplicate Counting

**Symptom:** Token counts appear doubled

**Cause:** Same completion tracked multiple times

**Solution:** Only call `track_external_llm_usage` once per completion, immediately after the API call.

### Issue: Zero Usage for External Calls

**Symptom:** External API usage not appearing in summary

**Cause:** `usage_collector` not passed to `LLMService`

**Solution:**
```python
# In context.py
self._llm_service = create_llm_service(openai_client, session_id)

# In set_usage_collector
if hasattr(self, "_llm_service") and self._llm_service:
    self._llm_service.usage_collector = collector
```

## Performance Considerations

- **Memory Efficient**: Only stores aggregated metrics per unique model
- **Thread Safe**: Uses immutable `ModelKey` dataclass with frozen=True
- **Minimal Overhead**: Tracking adds <1ms per metric event
- **Scale**: Can handle 100+ model switches per call without performance impact

## Future Enhancements

Potential improvements to the usage tracking system:

1. **Time-based Tracking**: Track usage over time intervals
2. **Cost Estimation**: Real-time cost estimation during calls
3. **Quota Management**: Enforce usage limits per session
4. **Anomaly Detection**: Alert on unusual usage patterns
5. **Export Formats**: Support CSV/JSON export for external analysis

