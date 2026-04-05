---
title: multi-agent knowledge compilation
type: concept
status: active
created: 2026-04-04
updated: 2026-04-04
tags:
  - multi-agent
  - architecture
  - compilation
related:
  - wiki/source-notes/jumperz-post-2040166448492900356.md
  - wiki/source-notes/ai-agents-cheat-sheet-screenshot.md
---

# Multi-agent knowledge compilation

## Summary

A multi-agent extension of the persistent-wiki pattern where multiple agents contribute outputs into a shared raw/working layer and a compiler process periodically organizes the results into durable knowledge artifacts.

## Key points

- multiple agents can produce intermediate outputs in parallel
- a shared `raw/` layer can act as the common ingest surface
- periodic compilation can convert noisy fragments into stable wiki pages
- orchestration becomes important once multiple agents, tools, and stores are involved
- conceptual patterns like manager/decentralized coordination and tool/data-store separation become more relevant

## Why it matters

This concept extends the single-agent LLM wiki pattern into a more scalable system. It is especially relevant if this project later grows beyond a single agent maintaining the corpus.

## Current recommendation

Multi-agent compilation should be treated as a later scaling path, not the default starting architecture. The current project is better served by tightening the single-agent/wiki-maintenance loop first.

## Related

- [jumperz post 2040166448492900356](../source-notes/jumperz-post-2040166448492900356.md)
- [AI Agents Cheat Sheet screenshot](../source-notes/ai-agents-cheat-sheet-screenshot.md)

## Sources

- [jumperz post 2040166448492900356](../source-notes/jumperz-post-2040166448492900356.md)
- [AI Agents Cheat Sheet screenshot](../source-notes/ai-agents-cheat-sheet-screenshot.md)

## Open questions

- When does multi-agent complexity become worth it for this project?
- Should compilation happen on a schedule, on demand, or both?
- What intermediate artifacts belong in `raw/` vs `outputs/`?
