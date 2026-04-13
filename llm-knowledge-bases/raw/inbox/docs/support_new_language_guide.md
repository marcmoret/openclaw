# Supporting New Languages - Areas to Check

## Overview

This guide lists the key areas that need to be checked and updated when adding support for a new language in the Voxira voice agent system.

## Areas to Check

### 1. Time Formatting ⭐ **CRITICAL**
**File:** `src/utils/time_utils.py`

- Add a new `_format_{language}_time()` function
- Update the `iso_to_time_words()` function to handle the new language code
- Consider language-specific time conventions (12-hour vs 24-hour, special phrases)

### 2. Vocabulary and Constants
**File:** `src/configs/vocabulary.py`

- Update language-specific terms and phrases

### 3. Agent Prompts and Templates
**Files:**
- `src/prompts/system_prompt.yaml`
- Agent YAML files in each agent directory (e.g., `main_agent.yaml`, `scheduling_agent.yaml`)

- Add language-specific prompts and instructions
- Consider cultural context in conversation patterns

### 4. Voice Configuration
**File:** `src/services/voice_configs.json`

- Add appropriate TTS/STT voice models for the new language
- Configure accent and regional variations

### 5. Data Validation
**Files:** `src/validators/` modules

- Update for language-specific formats (dates, phone numbers, names)
- Consider linguistic patterns for input processing

## Dependencies to Verify

- `num2words` library support for target language
- LiveKit agent framework language compatibility
- AI service provider language support (OpenAI, Deepgram, etc.)
