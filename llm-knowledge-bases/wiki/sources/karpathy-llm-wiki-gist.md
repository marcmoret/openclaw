---
title: Karpathy LLM Wiki Gist
type: source
created: 2026-04-10
updated: 2026-04-10
tags: [sources, gist, karpathy, llm-wiki, concept-document]
sources: [karpathy-llm-wiki-gist]
related: [andrej-karpathy, llm-wiki-pattern, karpathy-project-origin, schema-driven-governance]
---

## Source Metadata

- **URL**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Author**: Andrej Karpathy
- **Type**: GitHub Gist / Concept document
- **Source file**: `/raw/repos/karpathy-llm-wiki-gist.md`

## Key Takeaways

- **Most foundational written articulation** of the [[llm-wiki-pattern]]
- Lays out architecture, workflows, and rationale in one place
- More detailed than the original social post
- Establishes key principles: persistence, compounding, schema-driven behavior

## Detailed Summary

This gist is the clearest written description of building personal knowledge bases with LLMs. It establishes:

### Three Layers
1. **Raw sources** — articles, papers, repos, datasets, immutable
2. **Wiki** — persistent LLM-maintained markdown
3. **Schema** — `CLAUDE.md` or `AGENTS.md` instruction document

### Three Core Workflows

**Ingest**: Source → wiki updates
- Read the source
- Write a summary page
- Create/update entity/project/concept pages
- Cross-link aggressively
- Update index and log

**Query**: Question → synthesized answer
- Search the index
- Synthesize an answer from relevant pages
- File substantive answers back to wiki as analysis pages
- Update the log

**Lint**: Health-check and consistency
- Find contradictions
- Identify orphan pages
- Flag missing cross-references
- Suggest sources to investigate
- Fix issues and update log

### Key Principles

- **Compound, don't repeat** — knowledge accumulates over time
- **Link aggressively** — connections between pages are valuable
- **Flag contradictions** — don't silently overwrite
- **Stay current** — update dates and consistency
- **Markdown as substrate** — git-friendly, human-readable
- **Index and log are first-class** — `index.md` catalogs; `log.md` records
- **Vector DBs are optional** — at moderate scale, file organization + links suffice

## Concepts Expanded

- [[llm-wiki-pattern]] — the full architecture
- [[obsidian-integration]] — using Obsidian as the frontend
- [[vectorless-retrieval]] — no vectors needed at moderate scale

## Why It Matters

This is the **single most important reference** for this wiki project. Every convention, workflow, and structural decision is grounded in this gist.

## Strong Takeaways

- The wiki should be persistent and compounding
- Useful query outputs should be filed back into the wiki
- Indexing and logging deserve first-class treatment
- The schema file is an operational layer, not a minor detail
- Vector-heavy infrastructure is optional, not mandatory

## Relevance to This Project

Directly foundational. Our project scaffold already matches much of this pattern, but the gist sharpens:
- The importance of a strong schema document ✓ (CLAUDE.md)
- A real index.md ✓
- A real log.md ✓
- More explicit ingest/query/lint workflows ✓

## See Also

- [[llm-wiki-pattern]] for detailed concept breakdown
- [[karpathy-project-origin]] for the original post
- [[andrej-karpathy]] for author context
