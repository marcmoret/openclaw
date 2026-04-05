# Claude Handoff

Short shared handoff for another agent (especially Claude) working on this project from another machine.

## Read first

1. `WIKI-SCHEMA.md`
2. `wiki/home.md`
3. `wiki/index.md`
4. `wiki/log.md`
5. this file

## What this project is

A schema-driven, Obsidian-fronted, markdown-native knowledge compiler.

Core model:
- `raw/` = immutable source material
- `wiki/` = maintained knowledge layer
- `outputs/` = durable task/query artifacts

## Current architecture stance

- persistent wiki over raw-document RAG
- single-agent by default for now
- vectorless retrieval first
- optional LangExtract for harder ingest cases
- multi-agent later if scale actually demands it

## Current priorities

### Now
- continue ingesting strong primary sources
- promote durable insights into concepts/entities/indexes
- keep `wiki/log.md` updated
- use `docs/promotion-rules.md` when deciding what enters the wiki

### Good next moves
- deepen entity coverage
- add more concept pages only when the idea recurs across sources
- keep social posts and linked primary artifacts separate

## Important files

- `WIKI-SCHEMA.md`
- `wiki/home.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/indexes/source-triage.md`
- `docs/promotion-rules.md`
- `docs/obsidian-mind-adaptation.md`
- `outputs/reports/recommended-operating-model.md`

## What not to do

- do not rewrite raw sources
- do not promote every output into the wiki
- do not collapse commentary posts and primary artifacts into one note
- do not treat vector search as mandatory yet
- do not overcomplicate with multi-agent structure before it solves a real problem

## Suggested first task for Claude

Review the current foundational notes and identify the next 2–3 high-value entity or concept pages that would most improve the wiki.
