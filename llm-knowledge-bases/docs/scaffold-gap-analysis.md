# Scaffold Gap Analysis vs `karpathy/llm-wiki`

This note compares the current `llm-knowledge-bases` scaffold against the architecture described in Karpathy's `llm-wiki` gist.

## What already matches well

### 1. Three-layer architecture
Current scaffold already has the right broad split:
- `raw/` for source material
- `wiki/` for compiled markdown knowledge
- prompts/docs that partially serve the schema role

### 2. Obsidian-friendly workflow
The project already assumes Obsidian as the main frontend, which matches the gist closely.

### 3. Query outputs as durable artifacts
The `outputs/` structure already matches the gist's idea that answers, reports, slides, and visuals should become durable files rather than evaporate in chat.

### 4. Social-source capture
The current scaffold extends the gist in a useful way by explicitly handling X/social posts as discovery/framing sources.

## Biggest gaps

### 1. No first-class `index.md`
Karpathy's gist treats `index.md` as a key navigation structure. The current scaffold has index *folders* and pages, but not a canonical `wiki/index.md` acting as the top-level catalog of the knowledge base.

**Recommendation:** add `wiki/index.md` soon.

### 2. No first-class `log.md`
The gist treats `log.md` as an append-only chronological record of ingests, queries, and lint passes. The current scaffold does not yet have a canonical wiki activity log.

**Recommendation:** add `wiki/log.md` soon.

### 3. Schema layer is still fragmented
Right now the schema/instruction layer is spread across:
- `README.md`
- `docs/architecture.md`
- prompt files
- source-type notes

This works, but it is weaker than a single operational schema document that the LLM can treat as the canonical wiki-maintenance manual.

**Recommendation:** create one strong schema file for the project, likely something like `WIKI-SCHEMA.md` or `AGENT-SCHEMA.md` inside `llm-knowledge-bases/`.

### 4. Ingest/query/lint are present, but not yet formalized enough
The gist frames these as the three main operations. The scaffold has prompts for compile and answer, but linting and logging are not yet as first-class or standardized.

**Recommendation:** formalize:
- ingest workflow
- query workflow
- lint workflow
- logging conventions

### 5. No canonical source registry beyond triage
`source-triage.md` is useful, but it currently mixes pipeline status with source tracking. The gist implies a more systematic wiki-wide content catalog.

**Recommendation:** keep triage, but eventually separate:
- triage/status tracking
- content catalog/indexing

## Suggested next improvements

### Near-term
1. Add `wiki/index.md`
2. Add `wiki/log.md`
3. Add a single schema file that defines wiki maintenance behavior
4. Add a dedicated lint prompt or maintenance prompt

### Medium-term
5. Define frontmatter conventions for wiki pages
6. Decide when outputs should be promoted back into the wiki
7. Add a lightweight search/helper tool once scale justifies it

## Strong conclusion

The current scaffold is directionally correct.
It is not missing the core idea.

What it lacks is not vision, but **operational consolidation**:
- a canonical index
- a canonical log
- a stronger schema file
- more formal lifecycle definitions

That means the project is in a good place. It does not need a rebuild. It needs tightening.
