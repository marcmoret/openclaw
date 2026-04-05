# Quickstart for Another Agent

If you are a second agent entering this project for the first time, do this in order.

## 1. Read the core files
- `WIKI-SCHEMA.md`
- `wiki/home.md`
- `wiki/index.md`
- `wiki/log.md`
- `docs/claude-handoff.md`

## 2. Understand the goal
This is not a generic note vault.
It is an LLM-operated knowledge-compilation system.

The job is to:
- ingest sources
- maintain the wiki
- create durable outputs
- promote durable conclusions back into the wiki

## 3. Respect the architecture
- `raw/` = immutable inputs
- `wiki/` = maintained knowledge
- `outputs/` = reports/artifacts

## 4. Start with the strongest existing references
Review at least:
- `wiki/source-notes/karpathy-project-origin.md`
- `wiki/source-notes/karpathy-llm-wiki-gist.md`
- `wiki/concepts/recommended-operating-model.md`
- `wiki/concepts/persistent-wiki-over-rag.md`
- `wiki/concepts/vectorless-retrieval.md`
- `docs/promotion-rules.md`

## 5. Choose one useful action
Good first actions:
- ingest a strong new primary source
- deepen a concept page
- create a missing entity page
- run a lint pass
- improve cross-linking between existing high-value notes

## 6. Log what you do
Update `wiki/log.md` for meaningful work.

## 7. Do not overreach
Avoid:
- making the project more complicated than it needs to be
- defaulting to multi-agent patterns too early
- forcing heavy vector infrastructure before it is needed
- copying external templates literally when adaptation is better
