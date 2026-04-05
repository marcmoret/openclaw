---
title: Recommended operating model
type: report
status: active
created: 2026-04-04
updated: 2026-04-04
question: What architecture pattern do the strongest current sources collectively suggest for this project?
related:
  - wiki/source-notes/karpathy-llm-wiki-gist.md
  - wiki/source-notes/karpathy-project-origin.md
  - wiki/source-notes/jumperz-post-2040166448492900356.md
  - wiki/source-notes/dkare1009-post-2039665922185589044.md
  - wiki/source-notes/llm-wiki-architecture-screenshot.md
  - wiki/source-notes/breferrari-obsidian-mind.md
  - wiki/source-notes/google-langextract.md
---

# Recommended operating model

## Short answer

The strongest current sources collectively suggest that this project should operate as a **persistent markdown knowledge wiki maintained by a mostly single-agent LLM workflow**, with:
- immutable raw sources
- a compiled wiki as the primary knowledge artifact
- a strong schema/instruction layer
- lightweight retrieval first
- optional multi-agent expansion later
- optional structured-extraction tooling for hard ingest cases

## Core recommendation

### 1. Treat the wiki as the main artifact
The project should not primarily behave like a query-time RAG system over raw files. It should behave like a **knowledge compiler**.

That means:
- raw sources are the truth layer
- the wiki is the maintained knowledge layer
- useful outputs compound back into the wiki

This is the clearest shared conclusion across the Karpathy gist, project-origin source, and architecture screenshot.

### 2. Stay mostly single-agent for now
The JUMPERZ source makes a convincing case that the pattern can scale into multi-agent knowledge compilation. But right now, the project is not bottlenecked by lack of agent parallelism. It is bottlenecked by:
- source quality
- concept synthesis
- operational discipline
- consistent maintenance

So the recommended stance is:
- **single-agent by default**
- **multi-agent later, when scale justifies it**

### 3. Use vectorless retrieval first
The vectorless-RAG source strongly supports the current low-infrastructure direction.

For this project, retrieval should prioritize:
- `wiki/index.md`
- strong source notes
- concept pages
- keyword search / index navigation
- direct context injection

Embeddings/vector DBs should remain optional, not mandatory.

### 4. Treat schema and prompts as core assets
The code_rams commentary and the gist together support the idea that architecture docs, prompts, and schema files are not secondary fluff. They are part of the implementation.

For this project, files like:
- `WIKI-SCHEMA.md`
- prompt files
- index/log conventions
- concept definitions

are first-class system assets.

### 5. Use LangExtract selectively, not everywhere
`google/langextract` is promising, but it should not become the default ingest path.

Recommended policy:
- simple source -> direct wiki compilation
- complex/long/noisy source -> optional LangExtract preprocessing

That keeps the workflow simple while preserving a stronger tool for difficult ingest cases.

### 6. Use Obsidian as the human interface, not the intelligence layer
`obsidian-mind` is useful as a concrete implementation reference. The right lesson to borrow is not its exact structure, but its seriousness about:
- persistent markdown memory
- commands and maintenance flows
- governance files
- durable note organization

The project should keep using Obsidian as the browsing/editing frontend, while the LLM remains the maintainer/programmer of the wiki.

## Recommended operating loop

### Ingest
- add a source to `raw/`
- create/update source notes
- update concepts/entities/indexes as needed
- log the ingest

### Query
- answer from the wiki first
- use raw sources when the wiki is insufficient
- write durable outputs to `outputs/`
- promote useful conclusions back into the wiki
- log meaningful query artifacts

### Lint
- check contradictions
- find sparse concepts and orphan pages
- improve cross-linking
- identify stale or weak notes
- log important maintenance passes

## Recommended near-term architecture

### Keep now
- `raw/`, `wiki/`, `outputs/`
- `WIKI-SCHEMA.md`
- `wiki/index.md`
- `wiki/log.md`
- source-triage workflow
- social-source capture
- concept promotion

### Delay until needed
- multi-agent orchestration as a default mode
- vector database infrastructure
- heavy search stack beyond simple local search/indexing
- structured extraction everywhere

### Add gradually
- more concept pages
- first entity pages
- lightweight search helpers
- stronger promotion rules for outputs -> wiki

## Strong conclusion

The project should behave like a **persistent knowledge compiler with disciplined wiki maintenance**, not like a flashy agent swarm and not like a classic embedding-first RAG stack.

The right order of ambition is:
1. get the single-agent/wiki-compilation loop really solid
2. strengthen concepts, entities, indexing, and logging
3. add selective extraction/search helpers when they actually solve a real pain point
4. only then consider multi-agent scale-up

## Recommendation in one sentence

**Build a schema-driven, Obsidian-fronted, markdown-native knowledge compiler first; treat multi-agent orchestration and heavier retrieval infrastructure as later optimizations, not the starting point.**
