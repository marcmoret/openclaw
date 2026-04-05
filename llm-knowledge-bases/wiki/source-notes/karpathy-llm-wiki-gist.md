---
title: karpathy/llm-wiki gist
type: source-note
status: summarized
source_type: gist
created: 2026-04-04
updated: 2026-04-04
tags:
  - foundational
  - architecture
  - wiki
related:
  - wiki/index.md
  - docs/project-origin.md
---

# Source Note: karpathy/llm-wiki gist

## Summary

Foundational source for the project. Andrej Karpathy's `llm-wiki` gist describes the exact pattern this repository is converging on: immutable raw sources, an LLM-maintained markdown wiki, and a schema/instruction layer that governs ingest, query, and lint workflows.

## Source type

- Gist / concept document
- Primary artifact

## Why relevant

This is probably the single most important written source for the project so far. It moves the idea from tweet-level inspiration into a coherent operating model.

## Most important points

- a persistent wiki is the core knowledge artifact
- the LLM should maintain the wiki, not just answer against raw docs
- `index.md` and `log.md` are key navigation structures
- outputs from queries should compound back into the system
- the schema file is essential operational infrastructure

## Open questions

- How closely should this project mirror the gist literally versus adapt it?
- Should `index.md` and `log.md` be introduced immediately as first-class files?
- Should the current prompts be consolidated into a stronger schema document?

## Sources

- [raw/repos/karpathy-llm-wiki-gist.md](../raw/repos/karpathy-llm-wiki-gist.md)
