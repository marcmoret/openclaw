# WIKI-SCHEMA.md

Operational schema for the `llm-knowledge-bases` project.

This file tells the LLM how to behave as the maintainer of the wiki.

## Core model

There are three layers:

1. **Raw sources** (`raw/`)
   - immutable source material
   - articles, papers, repos, datasets, images, social posts, clips, and related assets
   - do not rewrite or silently "improve" raw sources

2. **Wiki** (`wiki/`)
   - the compiled knowledge layer
   - source notes, concept pages, entity pages, indexes, maps, and syntheses
   - this is the layer the LLM is expected to maintain aggressively

3. **Outputs** (`outputs/`)
   - question-time or task-time artifacts
   - reports, answers, slides, visuals, and derived deliverables
   - promote durable outputs back into the wiki when they add lasting value

## Mission

Build and maintain a persistent markdown wiki that compounds over time.

Do not re-derive everything from scratch every time if the knowledge can be compiled once and kept current.

## Operating modes

### 1. Ingest

When a new source arrives:
- inspect the source
- determine source type
- create or update a source note
- update relevant concept/entity/index pages
- preserve provenance
- add a concise entry to `wiki/log.md`

### 2. Query

When asked a question:
- read `wiki/index.md` first when helpful
- identify relevant source notes / concept pages
- synthesize an answer from the wiki and raw sources if needed
- write durable results to `outputs/` when appropriate
- if the result adds durable knowledge, promote it back into `wiki/`
- add a log entry for meaningful query-derived artifacts

### 3. Lint

Periodically review the wiki for:
- contradictions
- stale claims
- orphan pages
- weak cross-linking
- missing concept/entity pages
- unsupported claims needing better provenance
- opportunities for new source collection or synthesis

## Source handling rules

### Social/X posts
- Treat social posts as first-class sources.
- Distinguish between:
  - commentary
  - lead / pointer
  - media source
  - primary evidence
- If a social post links to a repo/article/tool, capture that as a **separate primary source**.
- Do not collapse the post and the linked artifact into one note.

### Repositories / gists
- Treat repos and gists as primary artifacts when they contain the actual implementation or written pattern.
- Prefer source notes that summarize:
  - what it is
  - why it matters
  - how it might fit this project

### Images / screenshots
- Treat screenshots as references when they contain architecture, workflow, or conceptual guidance.
- Record whether they are:
  - conceptual references
  - implementation diagrams
  - supporting media only

## Navigation files

### `wiki/index.md`
- top-level map of the wiki
- keep concise and curated
- link to foundational sources, key indexes, and major notes

### `wiki/log.md`
- append-only chronological record
- use consistent headings:
  - `## [YYYY-MM-DD] kind | short title`
- log ingests, query artifacts, lint passes, and important structural changes

### `wiki/indexes/source-triage.md`
- operational tracking for source status
- not the same thing as `wiki/index.md`
- may include captured/resolved/summarized/blocked-style states

## Writing style for wiki pages

- concise but not skeletal
- rich in links where useful
- explicit about uncertainty
- strong on provenance
- optimized for later reuse by both humans and LLMs

## Preferred page shapes

A good page often includes:
- Summary
- Key takeaways / key points
- Related
- Sources
- Open questions

## Promotion rule

Not every answer belongs in the wiki.
Promote outputs when they are:
- durable
- reusable
- clarifying
- likely to matter again

Do not promote every transient chat answer.

See also: `docs/promotion-rules.md`

## Retrieval philosophy

Default to lightweight retrieval first.
Use:
- index pages
- source notes
- keyword search
- structured navigation
- direct context injection

Do not assume embeddings/vector infrastructure are required at this scale.
Those can remain optional enhancements.

## Strong defaults

- keep raw sources immutable
- keep wiki pages maintained
- keep outputs useful
- keep provenance visible
- keep the system compounding
