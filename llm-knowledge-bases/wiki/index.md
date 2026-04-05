# Wiki Index

Top-level catalog for the LLM Knowledge Bases wiki.

See also: [Wiki Home](home.md)

This file should stay concise and navigable. It is the first place the LLM should check when orienting itself inside the wiki.

## Purpose

- provide a high-level map of the knowledge base
- link to important pages and indexes
- make it easier to find relevant notes before drilling down
- reduce unnecessary full-wiki scanning at moderate scale

## Core navigation

### Project framing
- [Wiki Home](home.md)
- [Project Origin](../docs/project-origin.md)
- [Scaffold Gap Analysis](../docs/scaffold-gap-analysis.md)
- [Source Triage](indexes/source-triage.md)
- [Wiki Log](log.md)

### Core concepts
- [Recommended operating model](concepts/recommended-operating-model.md)
- [Persistent wiki over raw-document RAG](concepts/persistent-wiki-over-rag.md)
- [Multi-agent knowledge compilation](concepts/multi-agent-knowledge-compilation.md)
- [Vectorless retrieval](concepts/vectorless-retrieval.md)

### Source-note collections
- [Concepts](concepts/)
- [Entities](entities/)
- [Source Notes](source-notes/)
- [Indexes](indexes/)
- [Maps](maps/)

### Operational references
- [Promotion Rules](../docs/promotion-rules.md)

## Important source notes

### Foundational
- [karpathy-project-origin](source-notes/karpathy-project-origin.md) — canonical project-framing source from Karpathy's X post
- [karpathy-llm-wiki-gist](source-notes/karpathy-llm-wiki-gist.md) — foundational written articulation of the pattern

### Architecture / workflow references
- [llm-wiki-architecture-screenshot](source-notes/llm-wiki-architecture-screenshot.md) — compact architecture diagram of the exact LLM wiki pattern
- [ai-agents-cheat-sheet-screenshot](source-notes/ai-agents-cheat-sheet-screenshot.md) — broader conceptual reference for models, tools, orchestration, stores, and protocols
- [jumperz-post-2040166448492900356](source-notes/jumperz-post-2040166448492900356.md) — multi-agent adaptation of the Karpathy pattern
- [dkare1009-post-2039665922185589044](source-notes/dkare1009-post-2039665922185589044.md) — vectorless RAG argument aligned with low-infra retrieval

### Tooling references
- [breferrari-obsidian-mind](source-notes/breferrari-obsidian-mind.md) — Obsidian vault memory workflow inspiration
- [google-langextract](source-notes/google-langextract.md) — optional structured-extraction tool for difficult ingest cases
- [chenglou-pretext](source-notes/chenglou-pretext.md) — possible output/demo/presentation layer candidate

### Key entities
- [Andrej Karpathy](entities/andrej-karpathy.md)
- [Obsidian](entities/obsidian.md)
- [LangExtract](entities/langextract.md)

## Maintenance notes

- Add new important pages here when they become durable references.
- Keep this file human-readable; it is a map, not a dump.
- Prefer linking to indexes and strong source notes over listing every file.
