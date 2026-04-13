---
title: Karpathy LLM Wiki Project Origin
type: source
created: 2026-04-10
updated: 2026-04-10
tags: [sources, social, karpathy, llm-wiki]
sources: [karpathy-project-origin]
related: [andrej-karpathy, llm-wiki-pattern, karpathy-llm-wiki-gist]
---

## Source Metadata

- **URL**: https://x.com/karpathy/status/2039805659525644595
- **Author**: Andrej Karpathy (@karpathy)
- **Type**: X / Social post
- **Date**: Unknown (early April 2026)
- **Role**: Project origin / canonical framing
- **Source file**: `/raw/x/2026-04-03-karpathy-2039805659525644595.md`

## Key Takeaways

- Original framing source for the LLM knowledge base project
- Provides the conceptual blueprint for the entire repository
- Establishes [[llm-wiki-pattern]] as the foundational architecture

## Detailed Summary

This is the original X post that launched the concept of building personal AI knowledge bases with LLMs. While the post text itself is referenced in `/docs/project-origin.md`, the core framing is:

**Replace query-time RAG with a persistent, LLM-maintained wiki.**

The idea: instead of asking an LLM to discover knowledge from raw documents every time you have a question, maintain a growing wiki that compounds knowledge over time. The LLM's job is not to answer from scratch, but to organize and synthesize.

## Concepts Introduced

- [[llm-wiki-pattern]] — the three-layer architecture
- Raw sources → wiki → schema workflow
- Ingest / query / lint as primary operations
- Markdown wiki as the persistent knowledge substrate

## Related Sources

- [[shann-holmberg-post]] — commentary on the workflow
- [[code-rams-post]] — explanation of follow-up ideas
- [[karpathy-llm-wiki-gist]] — the full concept document

## Entities Mentioned

- [[andrej-karpathy]] — author

## How This Source Relates to the Wiki

This post is the origin of the exact project structure we are building now. Every part of the schema, workflow, and architecture traces back to this framing.

## See Also

- [[llm-wiki-pattern]] for detailed concept expansion
- [[karpathy-llm-wiki-gist]] for the foundational writeup
- [[andrej-karpathy]] for author context
