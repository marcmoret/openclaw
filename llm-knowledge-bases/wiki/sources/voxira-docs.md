---
title: Voxira Operational Documentation
type: source
created: 2026-04-11
updated: 2026-04-11
tags: [voxira, deployment, cost-tracking, fuzzy-matching, operations]
sources: [raw/inbox/docs/FUZZY_NAME_MATCHING_PLAN.md, raw/inbox/docs/cost-calculation.md, raw/inbox/docs/usage-tracking.md, raw/inbox/docs/deployment.md, raw/inbox/docs/environment-variables.md, raw/inbox/docs/ProductionOptimization.md, raw/inbox/docs/agent_config_override.md, raw/inbox/docs/quebec_french_optimization_guide.md, raw/inbox/docs/support_new_language_guide.md]
related: [voxira, livekit, deepgram]
triage: summarized
---

# Voxira Operational Documentation

Operational and development documentation for the [[voxira]] voice agent platform. 9 files (+ 1 subfolder) covering deployment, cost tracking, optimization, and Quebec French language support.

## Documents

- **FUZZY_NAME_MATCHING_PLAN.md**: Implementation plan for Quebec French name fuzzy matching. Uses government name datasets (Retraite Québec first names 1980–2023, Institut de la statistique du Québec top 5000 surnames) with popularity weighting. Architecture: STT input → fuzzy matcher → confidence score → agent decision.
- **cost-calculation.md**: Per-session cost tracking pipeline. Processes usage data through pricing config to produce per-model breakdowns with audit trails. Covers LLM (per 1M tokens), STT/TTS (per audio minute/character), and infrastructure costs (Twilio + LiveKit).
- **usage-tracking.md**: `MultiModelUsageCollector` tracks token consumption, audio duration, and character counts across LLM/STT/TTS per session. `ModelKey`-based aggregation feeds into cost calculation.
- **deployment.md**: AWS ECS (Fargate) + ECR + GitHub Actions + Terraform. Environment-specific tagging (staging/production with git SHA). Container insights enabled.
- **environment-variables.md**: Required env vars for the platform.
- **ProductionOptimization.md**: Performance tuning guidance.
- **agent_config_override.md**: Per-agent configuration override patterns.
- **quebec_french_optimization_guide.md**: STT/TTS optimization for Quebec French dialect.
- **support_new_language_guide.md**: Guide for adding new language support to the platform.

## Source Files

Located in `raw/inbox/docs/` (9 files + session subfolder, ~70KB total)
