---
title: LLM Wiki Pattern
type: concept
created: 2026-04-10
updated: 2026-04-10
tags: [knowledge-base, llm-workflows, persistence, karpathy]
sources: [karpathy-llm-wiki-gist, karpathy-project-origin, shann-holmberg-post, jumperz-post]
related: [persistent-knowledge-base, vectorless-retrieval, obsidian-integration]
---

## Definition

The LLM Wiki Pattern is a system architecture for building persistent, compounding knowledge bases that replace query-time RAG with a human-curated, LLM-maintained markdown wiki.

Instead of rediscovering knowledge at query time from raw documents, this pattern stores synthesized, cross-linked, and indexed knowledge in a persistent wiki that grows richer over time.

## Core Architecture

Three layers:
1. **Raw sources** — immutable, read-only documents (articles, code, notes, images)
2. **The Wiki** — LLM-maintained markdown pages with obsidian wikilinks and YAML frontmatter
3. **Schema** — `CLAUDE.md` or equivalent operating manual that governs LLM behavior

## Three Core Workflows

1. **Ingest** — Raw source → wiki updates
   - Read source document
   - Write summary page in wiki/sources/
   - Create or update entity/project/concept pages
   - Cross-link aggressively
   - Update index and log

2. **Query** — Question → synthesized answer
   - Search wiki index
   - Synthesize answer from relevant pages
   - File substantive answers back into wiki as analysis pages
   - Append to log

3. **Lint** — Health check and consistency
   - Find contradictions between pages
   - Identify orphan pages with no inbound links
   - Flag missing cross-references
   - Suggest sources to investigate
   - Fix issues and update log

## Key Principles

- **Persistence over rediscovery**: Knowledge compounds over time instead of being rediscovered from scratch
- **Markdown as the knowledge substrate**: Git-friendly, human-readable, editor-agnostic
- **Schema-driven behavior**: A clear operating manual governs how the LLM maintains the wiki
- **Human + LLM division of labor**: Humans curate, ask questions, and decide; LLMs summarize, cross-reference, and maintain
- **Obsidian as the frontend**: The wiki is browsable and editable in a standard markdown editor
- **Indexing and logging are first-class**: `index.md` catalogs content; `log.md` records all operations

## Relationship to Vector DBs

This pattern is deliberately **vectorless** at moderate scale. Instead of embeddings + vector databases, it relies on:
- Clear index pages
- Obsidian wikilinks for navigation
- Structured YAML frontmatter for search
- Direct keyword search
- Strategic summarization and cross-linking

This reduces infrastructure cost and keeps knowledge human-readable.

## Where It Appears

- [[andrej-karpathy|Karpathy]]'s original concept and gist
- [[breferrari-obsidian-mind|breferrari/obsidian-mind]] repo (variant with Claude Code memory)
- [[jumperz-multi-agent-post|jumperz]] extending it to multi-agent architectures
- [[agent-harness-memory-ownership]] validating open memory architecture approach
- This wiki project itself

## Related Concepts

- [[vectorless-retrieval]] — Complement to this pattern
- [[persistent-knowledge-base]] — The broader goal
- [[obsidian-integration]] — Frontend tool
- [[claude-code-ecosystem]] — Integration with Claude Code

## See Also

- [[breferrari-obsidian-mind]] for a production variant
- [[karpathy-llm-wiki-gist]] for the foundational writeup
- [[llm-wiki-architecture-screenshot]] for a visual overview
