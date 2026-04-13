---
title: Persistent Knowledge Base
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [knowledge-management, llm-patterns, memory, architecture, retrieval]
sources: [karpathy-project-origin, karpathy-llm-wiki-gist, dkare1009-vectorless-rag-post]
related: [llm-wiki-pattern, schema-driven-governance, vectorless-retrieval]
status: active
---

## Definition

A persistent knowledge base is a durable, structured knowledge store that persists across LLM sessions, enabling continuous learning and knowledge compounding rather than per-session amnesia. The core insight: the LLM should not rediscover knowledge from raw sources on every query. It should maintain a compiled wiki that accumulates summaries, cross-links, contradictions, and syntheses over time.

## Why Wiki Over RAG

Raw-document RAG re-derives knowledge repeatedly — every query starts from scratch against unstructured sources. A maintained wiki compounds understanding over time: summaries, cross-links, and syntheses persist across sessions. Useful query outputs get promoted back into the wiki, so the system gets smarter with use rather than staying flat.

This approach is well suited to moderate-scale personal and research corpora where the knowledge graph is manageable enough for a single agent (or small team of agents) to maintain directly.

## Three-Layer Architecture

The persistent knowledge base pattern uses three layers:

1. **Raw sources** (`raw/`) — Immutable source material. Articles, papers, repos, social posts. Never modified after capture.
2. **Compiled wiki** (`wiki/`) — The maintained knowledge layer. Source notes, concept pages, entity pages, indexes, syntheses. This is what the LLM actively maintains.
3. **Outputs** (`outputs/`) — Task-time artifacts. Reports, answers, derived deliverables. Durable outputs get promoted back into the wiki.

## Key Principles

- **Durability**: Knowledge survives beyond individual sessions
- **Immutable sources**: Raw material is preserved as-is; the wiki is the derivative layer
- **Compilation over retrieval**: The wiki behaves like a knowledge compiler, not just a retrieval layer
- **Composability**: Knowledge builds on itself; new sessions benefit from past sessions' discoveries
- **Promotion**: Useful outputs flow back into the wiki when they add lasting value
- **Accessibility**: Stored in human-readable formats (markdown, YAML) that don't require specialized tools

## Open Questions

- At what scale does this approach need stronger search tooling (e.g., embeddings, BM25)?
- Which query outputs should be promoted back into the wiki by default?
- When does multi-agent compilation become worth the complexity overhead?

## Related Concepts

- [[llm-wiki-pattern]] — The concrete implementation pattern (ingest, query, lint workflows)
- [[schema-driven-governance]] — How schema files govern LLM maintenance of the knowledge base
- [[vectorless-retrieval]] — The retrieval stance: wiki-first, avoid embeddings at moderate scale
