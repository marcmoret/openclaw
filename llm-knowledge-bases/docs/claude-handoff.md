# Claude Handoff

Short shared handoff for any agent (especially Claude) working on this project from another machine.

## Read first

1. `CLAUDE.md` (root of repo)
2. `wiki/index.md`
3. `wiki/log.md`
4. this file

## What this project is

A schema-driven, Obsidian-fronted, markdown-native knowledge compiler shared across multiple computers.

Core model:
- `raw/` = immutable source material (drop new sources in `raw/inbox/`)
- `wiki/` = maintained knowledge layer (63 pages as of 2026-04-12)
- `outputs/` = durable task/query artifacts
- `docs/` = operational documentation for the project itself
- `prompts/` = reusable prompts for wiki operations

## Current architecture stance

- persistent wiki over raw-document RAG
- single-agent by default for now
- vectorless retrieval first
- multi-agent later if scale demands it
- both computers write to the same repo; git is the sync layer

## Current state (2026-04-12)

- **63 wiki pages**: 16 concepts, 6 entities, 1 project (Voxira), 35 sources, 2 analyses, 1 session overview, plus index/log/overview
- **Major domains**: LLM wiki patterns, multi-agent orchestration, Claude Code ecosystem, healthcare voice agents, speech/STT optimization
- **Key project**: Voxira — healthcare voice agent on LiveKit with 15+ specialized agents
- **Recent work**: Full lint pass, broken wikilink cleanup, session mining of 80 Claude Code sessions
- **Scheduled tasks**: daily auto-ingest (9AM), daily lint (9:30AM), daily session scan (9:45AM)

## Current priorities

### Now
- continue ingesting new sources dropped in `raw/inbox/`
- keep wiki cross-linked and healthy (lint regularly)
- mine new Claude Code sessions for project knowledge

### Good next moves
- deepen entity coverage
- add concept pages when ideas recur across sources
- keep social posts and linked primary artifacts separate

## Important files

- `CLAUDE.md` — full schema and conventions
- `wiki/index.md` — master catalog
- `wiki/log.md` — chronological operation record
- `wiki/overview.md` — high-level summary
- `docs/promotion-rules.md` — when to promote outputs to wiki
- `docs/cross-agent-workflow.md` — multi-agent coordination rules

## What not to do

- do not rewrite raw sources
- do not promote every output into the wiki
- do not collapse commentary posts and primary artifacts into one note
- do not treat vector search as mandatory yet
- do not make structural changes without a log entry
