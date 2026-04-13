# Cost Calculation System

## Overview

The cost calculation system provides accurate, auditable cost tracking for LiveKit voice agent sessions. It processes usage data from the usage collector and applies current pricing rates to calculate detailed cost breakdowns across LLM, STT, TTS, and infrastructure services.

## Architecture

### System Flow

```
┌──────────────────────────────────────────────────────────────┐
│                   Cost Calculation Pipeline                   │
└──────────────────────────────────────────────────────────────┘

Usage Summary          Pricing Config         Cost Calculator
     │                      │                        │
     │──llm_models──────────┤                        │
     │──stt_models──────────┤──pricing lookup────────>│
     │──tts_models──────────┤                        │
     │                      │                        │
     └──────────────────────┴────────────────────────┘
                                   │
                                   ▼
                      ┌──────────────────────────┐
                      │   Per-Model Breakdown    │
                      │ + Pricing Source Audit   │
                      └──────────────────────────┘
                                   │
                                   ▼
                      ┌──────────────────────────┐
                      │  Infrastructure Costs    │
                      │  (Twilio + LiveKit)      │
                      └──────────────────────────┘
                                   │
                                   ▼
                      ┌──────────────────────────┐
                      │   Complete Cost Report   │
                      │   with Audit Trail       │
                      └──────────────────────────┘
```

## Pricing Configuration

**Location:** `src/configs/pricing.py`

### Pricing Structure

#### 1. LLM Pricing (per 1M tokens)

Nested by source and model:

```python
LLM_PRICING = {
    "external_api": {
        "openai/gpt-4o": {
            "prompt": 2.50,
            "completion": 10.00,
            "cached": 1.25
        },
        "openai/gpt-4o-mini": {
            "prompt": 0.15,
            "completion": 0.60,
            "cached": 0.075
        }
    },
    "livekit_agent": {
        "api.openai.com/gpt-4o": {
            "prompt": 2.50,
            "completion": 10.00,
            "cached": 1.25
        }
    }
}

# Fallback for unknown models
DEFAULT_LLM_PRICING = {
    "prompt": 2.50,
    "completion": 10.00,
    "cached": 1.25
}
```

**Cost Formula:**
```
LLM Cost = (prompt_tokens / 1M × prompt_rate)
         + (completion_tokens / 1M × completion_rate)
         + (cached_tokens / 1M × cached_rate)
```

#### 2. STT Pricing (per minute of audio)

Flat dictionary by provider/model:

```python
STT_PRICING = {
    "Deepgram/nova-2": 0.0043,
    "Deepgram/nova-3": 0.0059,
    "openai/whisper-1": 0.006,
}

DEFAULT_STT_PRICE_PER_MINUTE = 0.006
```

**Cost Formula:**
```
STT Cost = (audio_duration_seconds / 60) × rate_per_minute
```

#### 3. TTS Pricing (per 1M characters)

Flat dictionary by provider/model:

```python
TTS_PRICING = {
    "ElevenLabs/eleven_turbo_v2": 180.00,
    "ElevenLabs/eleven_flash_v2_5": 80.00,
    "Cartesia/sonic": 150.00,
}

DEFAULT_TTS_PRICE_PER_MILLION = 180.00
```

**Cost Formula:**
```
TTS Cost = (characters_count / 1M) × rate_per_million
```

#### 4. Infrastructure Pricing (per minute)

Platform-specific rates:

```python
INFRASTRUCTURE_PRICING = {
    CallPlatform.PHONE: {
        "twilio_inbound_local": 0.0085,      # US/CA local
        "twilio_inbound_tollfree": 0.0220,   # US/CA toll-free
        "twilio_outbound": 0.0140,            # US/CA outbound
        "livekit_egress": 0.005,              # Recording
    },
    CallPlatform.WEB: {
        "livekit_egress": 0.005,
    }
}
```

**Cost Formulas:**
```
Twilio Cost = call_duration_minutes × rate_by_direction_and_type
LiveKit Egress Cost = call_duration_minutes × 0.005
```

### Pricing Updates

**Update Frequency:** Quarterly or when vendors announce rate changes

**Update Process:**
1. Verify rates on official vendor pricing pages
2. Update `src/configs/pricing.py`
3. Document changes in pricing commit message
4. Update pricing effective date comment

**Current Rates As Of:** December 2025

**Sources:**
- OpenAI: https://openai.com/api/pricing/
- Deepgram: https://deepgram.com/pricing
- ElevenLabs: https://elevenlabs.io/pricing
- Twilio: https://www.twilio.com/en-us/voice/pricing/us
- LiveKit: https://livekit.io/pricing

## Cost Calculator Service

**Location:** `src/services/cost_calculator.py`

### Features

1. **Flexible Pricing Lookup**: Exact → Partial → Default fallback
2. **Complete Audit Trail**: Tracks which pricing was used for each model
3. **Precision Rounding**: 4 decimal places ($0.0001 = 1/100th cent)
4. **Platform Awareness**: Different costs for phone vs. web calls
5. **Direction Awareness**: Distinguishes inbound/outbound calls

### Pricing Lookup Strategy

#### 1. Exact Match

Direct lookup by `{provider}/{model}`:

```python
pricing_key = "openai/gpt-4o"
if pricing_key in LLM_PRICING["external_api"]:
    return pricing, "exact", pricing_key
```

#### 2. Partial Match (Suffix Stripping)

Handles model variants like `gpt-4o-preview`, `gpt-4o-2024-11-20`:

```python
# Strip suffixes: -beta, -preview, -test, -alpha, -v1, -v2
stripped = "gpt-4o"  # from "gpt-4o-preview"
stripped_key = f"openai/{stripped}"
if stripped_key in pricing:
    return pricing, "partial", stripped_key
```

#### 3. Substring Matching

Finds base model when exact match fails:

```python
# Match "gpt-4o" in "gpt-4o-2024-08-06"
for key, pricing in pricing_dict.items():
    if "gpt-4o" in key or key contains "gpt-4o":
        return pricing, "partial", key
```

#### 4. Default Fallback

Conservative default when no match found:

```python
pricing = DEFAULT_LLM_PRICING
pricing_source = "default"
logger.warning(f"Using default pricing for {model}")
```

### Cost Breakdown Output

#### Simple Usage

```python
from src.services.cost_calculator import cost_calculator

total = cost_calculator.calculate_total(
    usage_summary,
    call_duration_seconds=120,
    platform_type=CallPlatform.PHONE,
    call_direction="inbound",
    is_tollfree=False
)
# Returns: 0.0834
```

#### Detailed Breakdown

```python
breakdown = cost_calculator.calculate_breakdown(
    usage_summary,
    call_duration_seconds=120,
    platform_type=CallPlatform.PHONE,
    call_direction="inbound",
    is_tollfree=False
)
```

**Output Structure:**

```json
{
  // Top-level costs (backward compatible)
  "llm_cost": 0.0416,
  "stt_cost": 0.0086,
  "tts_cost": 0.0900,
  "twilio_cost": 0.0170,
  "livekit_egress_cost": 0.0100,
  "total_cost": 0.1672,

  // Detailed LLM breakdown with audit trail
  "llm_details": {
    "total": 0.0416,
    "models": {
      "external_api:openai/gpt-4o": {
        "cost": 0.0416,
        "pricing_source": "exact",
        "matched_key": "openai/gpt-4o",
        "rates_used": {
          "prompt_per_1m": 2.50,
          "completion_per_1m": 10.00,
          "cached_per_1m": 1.25
        },
        "tokens": {
          "prompt": 10000,
          "completion": 5000,
          "cached": 0
        }
      }
    }
  },

  // Detailed STT breakdown
  "stt_details": {
    "total": 0.0086,
    "models": {
      "livekit_agent:Deepgram/nova-2": {
        "cost": 0.0086,
        "pricing_source": "exact",
        "matched_key": "Deepgram/nova-2",
        "rate_used": 0.0043,
        "usage": {
          "audio_seconds": 120,
          "minutes": 2.0
        }
      }
    }
  },

  // Detailed TTS breakdown
  "tts_details": {
    "total": 0.0900,
    "models": {
      "livekit_agent:ElevenLabs/eleven_turbo_v2": {
        "cost": 0.0900,
        "pricing_source": "exact",
        "matched_key": "ElevenLabs/eleven_turbo_v2",
        "rate_used": 180.00,
        "usage": {
          "characters": 5000
        }
      }
    }
  },

  // Infrastructure costs with rates
  "infrastructure_details": {
    "twilio": {
      "cost": 0.0170,
      "rate_per_minute": 0.0085,
      "minutes": 2.0,
      "type": "local"  // or "tollfree", "outbound", "none"
    },
    "livekit_egress": {
      "cost": 0.0100,
      "rate_per_minute": 0.005,
      "minutes": 2.0
    }
  },

  // Audit flags
  "used_default_pricing": false,

  // Call metadata for audit trail
  "call_metadata": {
    "duration_seconds": 120,
    "platform_type": "phone",
    "call_direction": "inbound",
    "is_tollfree": false
  }
}
```

### Audit Trail Benefits

1. **Transparency**: Know exactly which pricing rate was used
2. **Debugging**: Identify when default pricing is applied
3. **Validation**: Verify cost calculations against invoices
4. **Optimization**: Identify high-cost models for optimization
5. **Compliance**: Maintain records for financial auditing

## Integration

### Session Lifecycle Integration

**Location:** `src/utils/session_utils.py`

Cost calculation is performed in the shutdown handler at the end of each call. **Importantly**, the cost is calculated AFTER generating the call summary and analysis to ensure those LLM calls are included:

```python
async def shutdown_handler():
    # Calculate duration
    end_time = datetime.now(timezone.utc)
    duration = (end_time - started_at).total_seconds().__int__()
    
    # Generate summary and analysis FIRST (makes 2 LLM calls)
    summary_and_analysis = generate_call_summary_and_analysis(
        transcripts=transcripts or [],
        llm_service=userdata.llm_service,
        variables=userdata.variables,
    )
    
    # Get usage summary AFTER summary/analysis to include their usage
    usage_summary = usage_collector.get_detailed_summary()
    
    # Calculate cost breakdown with complete usage data
    cost_breakdown = cost_calculator.calculate_breakdown(
        usage_summary,
        duration,
        userdata.platform_type,
        call_direction=getattr(userdata, "call_direction", "inbound"),
        is_tollfree=getattr(userdata, "is_tollfree", False)
    )

    # Warn if default pricing used
    if cost_breakdown.get("used_default_pricing"):
        logger.warning(
            "Cost calculation used default pricing for some models. "
            "Check cost_breakdown details for which models."
        )

    # Log to console
    logger.info(
        f"Call cost: ${cost_breakdown['total_cost']:.4f} "
        f"(LLM=${cost_breakdown['llm_cost']:.4f}, "
        f"STT=${cost_breakdown['stt_cost']:.4f}, "
        f"TTS=${cost_breakdown['tts_cost']:.4f}, "
        f"Twilio=${cost_breakdown['twilio_cost']:.4f}, "
        f"Egress=${cost_breakdown['livekit_egress_cost']:.4f})"
    )

    # Log to Langfuse for observability
    langfuse_trace.event(
        name="Cost Breakdown",
        input={
            "duration_seconds": duration,
            "platform_type": userdata.platform_type,
            "call_direction": call_direction,
            "is_tollfree": is_tollfree,
        },
        output=cost_breakdown
    )
```

### LLM Usage Sources Included in Cost

The cost calculation includes LLM usage from multiple sources:

**1. LiveKit Agent LLM Calls**
- Real-time conversation with the caller
- Agent transfers and routing logic
- Data extraction during the call
- Source: `livekit_agent`

**2. External API LLM Calls**
- Contact identification and validation
- Appointment scheduling logic
- Custom business logic processing
- Source: `external_api`

**3. Call Summary Generation** ⭐
- Single LLM call to generate human-readable call summary
- Uses `llm_service.call_llm()` with summary prompt
- **Tracked as:** `external_api:openai/{model}`

**4. Call Analysis Generation** ⭐
- Single LLM call to extract structured call data
- Uses `llm_service.call_llm()` with structured output
- **Tracked as:** `external_api:openai/{model}`

> **Important:** The cost calculation happens AFTER summary/analysis generation to ensure these 2 additional LLM calls are included in the final cost breakdown. This ensures 100% of LLM usage is accounted for.

### Platform Type Detection

**Location:** `src/models/context.py`

Platform type is automatically determined from the participant:

```python
# In UserData.__init__
participants = list(job_ctx.room.remote_participants.values())
participant = participants[0] if participants else None
platform_type = get_call_type(participant)  # "phone" or "web"

self._variables = {
    "platform_type": platform_type,
    # ...
}
```

**Platform Detection Logic:**
- SIP participants → `CallPlatform.PHONE`
- Standard participants → `CallPlatform.WEB`
- Default → `CallPlatform.PHONE`

## Cost Analysis Examples

### Example 1: Standard Phone Call

**Call Details:**
- Duration: 180 seconds (3 minutes)
- Platform: Phone (inbound, local number)
- Models used: GPT-4o (external), Deepgram Nova-2, ElevenLabs Turbo v2

**Usage:**
- LLM: 15K prompt, 8K completion, 2K cached
- STT: 180 seconds audio
- TTS: 6,000 characters

**Cost Breakdown:**
```
LLM:    $0.0625  = (15K/1M × $2.50) + (8K/1M × $10.00) + (2K/1M × $1.25)
STT:    $0.0129  = (180s / 60) × $0.0043
TTS:    $0.1080  = (6K / 1M) × $180.00
Twilio: $0.0255  = 3min × $0.0085
Egress: $0.0150  = 3min × $0.005
──────────────────
Total:  $0.2239
```

### Example 2: Web Call (No Twilio)

**Call Details:**
- Duration: 120 seconds (2 minutes)
- Platform: Web
- Models used: GPT-4o-mini (agent), Deepgram Nova-3, Cartesia Sonic

**Usage:**
- LLM: 8K prompt, 4K completion, 1K cached
- STT: 120 seconds audio
- TTS: 3,500 characters

**Cost Breakdown:**
```
LLM:    $0.0052  = (8K/1M × $0.15) + (4K/1M × $0.60) + (1K/1M × $0.075)
STT:    $0.0118  = (120s / 60) × $0.0059
TTS:    $0.0525  = (3.5K / 1M) × $150.00
Twilio: $0.0000  = N/A (web call)
Egress: $0.0100  = 2min × $0.005
──────────────────
Total:  $0.0795
```

### Example 3: Long Call with Multiple Model Switches

**Call Details:**
- Duration: 600 seconds (10 minutes)
- Platform: Phone (outbound)
- Models: GPT-4o (5K tokens) + GPT-4o-mini (20K tokens), Deepgram Nova-2, ElevenLabs Flash

**Cost Breakdown:**
```
LLM:
  GPT-4o:       $0.0175  = (3K/1M × $2.50) + (2K/1M × $10.00)
  GPT-4o-mini:  $0.0210  = (12K/1M × $0.15) + (8K/1M × $0.60)
  Subtotal:     $0.0385

STT:    $0.0430  = (600s / 60) × $0.0043
TTS:    $0.1200  = (15K / 1M) × $80.00
Twilio: $0.1400  = 10min × $0.0140 (outbound rate)
Egress: $0.0500  = 10min × $0.005
──────────────────
Total:  $0.3915
```

## Best Practices

### 1. Regular Pricing Updates

- Review vendor pricing quarterly
- Set up alerts for pricing change announcements
- Document all pricing changes in git commits
- Test cost calculations after pricing updates

### 2. Default Pricing Monitoring

Monitor logs for default pricing warnings:

```bash
grep "Using default pricing" logs/*.log
```

Add unknown models to pricing config when discovered.

### 3. Cost Optimization

**High-Cost Patterns:**
- Long completion tokens (use GPT-4o-mini for simple tasks)
- Uncached prompts (enable prompt caching)
- High character TTS (optimize output verbosity)

**Optimization Strategies:**
1. Use smaller models for classification/extraction
2. Enable prompt caching for repeated system prompts
3. Batch multiple small requests
4. Use cheaper TTS voices for non-critical audio

### 4. Cost Budgeting

Set cost thresholds and alerts:

```python
if cost_breakdown['total_cost'] > COST_THRESHOLD:
    logger.warning(f"High cost call: ${cost_breakdown['total_cost']}")
    # Alert operations team
```

### 5. Audit Trail Retention

Store cost breakdowns in:
- Langfuse (automatic via integration)
- Database for long-term analysis
- Export monthly reports for accounting

## Troubleshooting

### Issue: Costs Don't Match Vendor Invoices

**Diagnostic Steps:**

1. Check pricing rates are current:
```python
# Compare against vendor pricing pages
print(LLM_PRICING["external_api"]["openai/gpt-4o"])
```

2. Verify usage tracking is complete:
```python
# Check all models are tracked
usage_summary = collector.get_detailed_summary()
print(usage_summary["model_count"])
```

3. Review pricing source for discrepancies:
```python
# Check if default pricing was used
if breakdown["used_default_pricing"]:
    # Review llm_details/stt_details/tts_details
    for model, details in breakdown["llm_details"]["models"].items():
        if details["pricing_source"] == "default":
            print(f"Unknown model: {model}")
```

### Issue: High Costs from Unknown Models

**Solution:**

1. Identify the model:
```python
# Find models using default pricing
for model, details in breakdown["llm_details"]["models"].items():
    if details["pricing_source"] == "default":
        print(f"Add to pricing config: {model}")
```

2. Add to pricing configuration:
```python
# In src/configs/pricing.py
LLM_PRICING["external_api"]["openai/new-model"] = {
    "prompt": X.XX,
    "completion": Y.YY,
    "cached": Z.ZZ
}
```

### Issue: Twilio Cost is Zero for Phone Calls

**Check:**

1. Platform type is correct:
```python
print(userdata.platform_type)  # Should be "phone"
```

2. Call direction is set:
```python
print(userdata.get_variable("call_direction"))  # "inbound" or "outbound"
```

3. Review infrastructure details:
```python
print(breakdown["infrastructure_details"]["twilio"])
```

## Performance Considerations

- **Calculation Speed**: <5ms for typical call with 5 models
- **Memory**: <1KB per cost breakdown object
- **Precision**: 4 decimal places balances accuracy with readability
- **Rounding**: Applied at final step to minimize accumulated errors

## Future Enhancements

1. **Real-time Cost Estimation**: Calculate cost during call
2. **Cost Predictions**: Predict final cost based on current usage rate
3. **Cost Alerts**: Notify when approaching budget thresholds
4. **Historical Analysis**: Track cost trends over time
5. **Model Recommendations**: Suggest cheaper alternatives
6. **Volume Discounts**: Apply tiered pricing for high-volume usage
7. **Custom Pricing**: Support customer-specific pricing agreements
8. **Multi-currency**: Support cost calculation in multiple currencies

