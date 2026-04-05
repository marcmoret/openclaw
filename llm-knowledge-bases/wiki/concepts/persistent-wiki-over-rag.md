---
title: persistent wiki over raw-document RAG
type: concept
status: active
created: 2026-04-04
updated: 2026-04-04
tags:
  - architecture
  - retrieval
  - wiki
related:
  - wiki/source-notes/karpathy-project-origin.md
  - wiki/source-notes/karpathy-llm-wiki-gist.md
  - wiki/source-notes/dkare1009-post-2039665922185589044.md
---

# Persistent wiki over raw-document RAG

## Summary

A core idea of this project is that the LLM should not rediscover knowledge from raw sources from scratch on every query. Instead, it should maintain a persistent markdown wiki that accumulates summaries, links, contradictions, and syntheses over time.

## Key points

- raw-document RAG re-derives knowledge repeatedly
- a maintained wiki compounds understanding over time
- summaries, cross-links, and syntheses should persist
- useful query outputs can be promoted back into the wiki
- this approach is well suited to moderate-scale personal/research corpora
- the wiki should behave like a knowledge compiler, not just a retrieval layer

## Why it matters

This concept is the architectural center of the project. It explains why the repository has separate `raw/`, `wiki/`, and `outputs/` layers.

## Related

- [karpathy project origin](../source-notes/karpathy-project-origin.md)
- [karpathy/llm-wiki gist](../source-notes/karpathy-llm-wiki-gist.md)
- [dkare1009 post 2039665922185589044](../source-notes/dkare1009-post-2039665922185589044.md)

## Sources

- [karpathy project origin](../source-notes/karpathy-project-origin.md)
- [karpathy/llm-wiki gist](../source-notes/karpathy-llm-wiki-gist.md)
- [dkare1009 post 2039665922185589044](../source-notes/dkare1009-post-2039665922185589044.md)
- [LLM Wiki architecture screenshot](../source-notes/llm-wiki-architecture-screenshot.md)

## Open questions

- At what scale does this approach need stronger search tooling?
- Which query outputs should be promoted back into the wiki by default?
