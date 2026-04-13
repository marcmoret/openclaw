---
title: LLM Wiki Architecture Diagram
type: source
created: 2026-04-10
updated: 2026-04-10
tags: [sources, image, architecture, llm-wiki-pattern]
sources: [llm-wiki-architecture-screenshot]
related: [llm-wiki-pattern, karpathy-llm-wiki-gist]
---

## Source Metadata

- **Type**: Screenshot / architecture diagram
- **Date captured**: April 4, 2026
- **Title**: "LLM Wiki — Karpathy's Knowledge Compilation Pattern"
- **Source file**: `/raw/assets/llm-wiki-architecture-screenshot-2026-04-04.md`

## Key Architecture

### Three Layers

1. **Raw Sources** — immutable, read-only
   - Articles, papers, code, notes, datasets, images
   
2. **The Wiki** — LLM-maintained markdown
   - Summary pages, entity pages, concept pages
   - Cross-linked with Obsidian wikilinks
   
3. **Schema** — `CLAUDE.md` or `AGENTS.md`
   - Operating manual
   - Workflow definitions
   - Conventions

### Three Core Operations

**Ingest** — source → wiki updates
- Read source
- Write summary
- Update index
- Cross-link

**Query** — question → answer
- Search index
- Synthesize
- File back to wiki

**Lint** — health-check
- Find issues
- Fix & patch
- Suggest sources

### Actors

- **Human** — curate, question, think
- **LLM Agent** — summarize, cross-ref, maintain

## Why It Matters

This diagram is one of the **clearest compact references** for the entire [[llm-wiki-pattern]]. It shows:
- The three-layer architecture at a glance
- The three workflows and their flow
- The human/LLM division of responsibility
- Raw → wiki → schema relationships

## Relationship to This Project

This diagram **exactly matches** the structure we've built:
- ✓ raw/ folder (immutable sources)
- ✓ wiki/ folder (LLM-maintained pages)
- ✓ CLAUDE.md (schema)
- ✓ ingest/query/lint workflows
- ✓ Human (Marco) + LLM (Claude) roles

## Use Cases

- **Onboarding:** Show new team members the architecture
- **Communication:** Explain the pattern to stakeholders
- **Reference:** Quick visual check of structure and flow
- **Teaching:** Illustrate the three-layer model

## Related Sources

- [[karpathy-llm-wiki-gist]] — detailed writeup
- [[karpathy-project-origin]] — original framing
- CLAUDE.md — the schema in action

## See Also

- [[llm-wiki-pattern]] for detailed concept
- [[karpathy-llm-wiki-gist]] for complete explanation
- `/wiki/` for the actual implementation
