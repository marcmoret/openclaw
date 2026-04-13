# Agent Configuration

This document describes how to use the agent configuration feature to customize agent behavior through configuration.

## Overview

The agent configuration feature allows you to:

1. Customize agent attributes at initialization time
2. Define preset configurations for different agent behaviors
3. Apply configurations globally or per specific agent
4. Customize agent behavior through language_config

## How It Works

The implementation follows a clean approach for agent configuration:

1. Define configuration presets in `src/utils/agent_config.py`
2. Include agent configurations in language_config under `agents_config`
3. Pass configurations to agents during initialization

## Usage Examples

### Using Preset Configurations

You can use predefined configuration presets:

```python
# In language_config or API response
{
    "agents_config": {
        "default": "patient_identification"  # Use preset for all agents
    }
}
```

### Using Custom Configurations

You can define custom configurations:

```python
# In language_config or API response
{
    "agents_config": {
        "default": {  # Custom configuration for all agents
            "ignore_transcriptions_while_processing": True,
            "repeat_on_silence": False
        }
    }
}
```

### Using Agent-Specific Configurations

You can configure different agents with different presets or custom configurations:

```python
# In language_config or API response
{
    "agents_config": {
        "default": "default",  # Global default configuration
        "PATIENT_IDENTIFICATION": "patient_identification",
        "SCHEDULING": "scheduling",
        "TECHNICAL_ISSUE": {  # Custom configuration
            "ignore_transcriptions_while_processing": True,
            "repeat_on_silence": False
        }
    }
}
```

### Using STT and TTS Configurations

You can configure STT and TTS for specific agents:

```python
# In language_config or API response
{
    "agents_config": {
        "PATIENT_IDENTIFICATION": {
            "ignore_transcriptions_while_processing": True,
            "stt": "french-deepgram",  # Use French STT
            "tts": {  # Custom TTS configuration
                "service": "elevenlabs",
                "voice_id": "custom-voice-id",
                "model": "eleven_multilingual_v2"
            }
        }
    }
}
```

## Available Configuration Presets

The following configuration presets are available:

| Preset Name | Description | Configuration |
|-------------|-------------|---------------|
| `default` | Standard configuration with normal interaction | `ignore_transcriptions_while_processing=False, repeat_on_silence=True` |
| `patient_identification` | Optimized for patient identification flow | `ignore_transcriptions_while_processing=True, repeat_on_silence=True` |
| `scheduling` | Optimized for scheduling interactions | `ignore_transcriptions_while_processing=False, repeat_on_silence=True` |
| `interactive` | Enhanced interactive mode | `ignore_transcriptions_while_processing=False, repeat_on_silence=True, is_transferring_to_another_agent=False` |
| `non_interactive` | Reduced interaction mode | `ignore_transcriptions_while_processing=True, repeat_on_silence=False, is_transferring_to_another_agent=True` |
| `recording_enabled` | Audio recording enabled | `record_frames=True` |
| `recording_disabled` | Audio recording disabled | `record_frames=False` |
| `french_agent` | Agent with French STT and TTS | `stt="french-deepgram", tts="french-elevenlabs"` |
| `custom_voice_agent` | Agent with custom voice TTS | `tts={"service": "elevenlabs", "voice_id": "custom-voice-id"}` |

## Configurable Agent Attributes

The following agent attributes can be configured:

- `ignore_transcriptions_while_processing`: Whether to ignore incoming transcriptions while processing
- `repeat_on_silence`: Whether to repeat the last message on silence
- `is_transferring_to_another_agent`: Whether the agent is transferring to another agent
- `record_frames`: Whether to record audio frames
- `stt`: Speech-to-Text service configuration (same as session config)
- `tts`: Text-to-Speech service configuration (same as session config)
- `llm`: Language Model service configuration (same as session config)

## Implementation Details

The agent configuration override feature is implemented in the following files:

- `src/utils/agent_config.py`: Contains agent configuration presets and application logic
- `src/utils/session_loader.py`: Contains stack configuration and preset updates
- `src/utils/session_utils.py`: Contains integration with session setup

## Adding New Configuration Presets

To add a new configuration preset:

1. Add the preset to `AGENT_CONFIGS` in `src/utils/agent_config.py`
2. Use the preset in your stack configuration

## Adding New Configurable Attributes

To add a new configurable attribute:

1. Make sure the attribute exists in the agent class
2. Add the attribute to the appropriate configuration presets in `AGENT_CONFIGS`
3. Use the attribute in your stack configuration
