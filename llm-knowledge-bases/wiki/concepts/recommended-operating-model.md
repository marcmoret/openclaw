---
title: recommended operating model
type: concept
status: active
created: 2026-04-04
updated: 2026-04-04
tags:
  - operating-model
  - architecture
  - workflow
related:
  - wiki/source-notes/karpathy-llm-wiki-gist.md
  - wiki/source-notes/karpathy-project-origin.md
  - wiki/source-notes/jumperz-post-2040166448492900356.md
  - wiki/source-notes/dkare1009-post-2039665922185589044.md
---

# Recommended operating model

## Summary

The current evidence base suggests that this project should operate as a schema-driven, Obsidian-fronted, markdown-native knowledge compiler. The best near-term model is a mostly single-agent workflow with immutable raw sources, a maintained wiki, lightweight retrieval, and selective optional tooling for harder ingest cases.

## Key points

- the wiki should be the primary knowledge artifact
- raw sources remain immutable
- outputs should compound back into the wiki when durable
- single-agent discipline should come before default multi-agent scale
- vectorless retrieval should be the default stance at current scale
- LangExtract should remain optional for difficult ingest, not mandatory everywhere
- schema and prompt files are first-class implementation assets

## Why it matters

This concept turns the current source synthesis into a durable project stance, so the architecture does not have to be re-argued from scratch every session.

## Related

- [persistent wiki over raw-document RAG](persistent-wiki-over-rag.md)
- [multi-agent knowledge compilation](multi-agent-knowledge-compilation.md)
- [vectorless retrieval](vectorless-retrieval.md)
- [karpathy/llm-wiki gist](../source-notes/karpathy-llm-wiki-gist.md)

## Sources

- [karpathy/llm-wiki gist](../source-notes/karpathy-llm-wiki-gist.md)
- [karpathy project origin](../source-notes/karpathy-project-origin.md)
- [jumperz post 2040166448492900356](../source-notes/jumperz-post-2040166448492900356.md)
- [dkare1009 post 2039665922185589044](../source-notes/dkare1009-post-2039665922185589044.md)
- [LLM Wiki architecture screenshot](../source-notes/llm-wiki-architecture-screenshot.md)
- [breferrari/obsidian-mind](../source-notes/breferrari-obsidian-mind.md)
- [google/langextract](../source-notes/google-langextract.md)
