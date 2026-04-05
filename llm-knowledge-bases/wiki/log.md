# Wiki Log

Append-only record of meaningful activity in the knowledge base.

Use a consistent heading format so the log stays machine-friendly and easy to grep.

Suggested format:

```md
## [YYYY-MM-DD] kind | short title
- what happened
- what changed
- optional links
```

## [2026-04-03] scaffold | initial project setup
- Created `llm-knowledge-bases/` scaffold with `raw/`, `wiki/`, `outputs/`, `docs/`, `prompts/`, and `tools/`.
- Added starter prompts, docs, and utility scripts.

## [2026-04-03] source-capture | X/social-source workflow
- Added support for X/social-source capture.
- Added `raw/x/`, `prompts/capture-social-source.md`, and `docs/source-types.md`.

## [2026-04-03] source-capture | first tweet/repo sources
- Captured multiple X posts and created linked source notes.
- Added primary artifact seeds including `breferrari/obsidian-mind`, `google/langextract`, and `chenglou/pretext`.

## [2026-04-03] indexing | source triage
- Added `wiki/indexes/source-triage.md` to track source status, linked primary artifacts, and next actions.

## [2026-04-03] framing | project origin
- Added Karpathy's X post as the canonical project-origin source.
- Added `docs/project-origin.md`.

## [2026-04-04] primary-source | karpathy llm-wiki gist
- Added Karpathy's `llm-wiki` gist as a foundational primary source.
- Added scaffold comparison note in `docs/scaffold-gap-analysis.md`.

## [2026-04-04] structure | canonical index and log
- Added `wiki/index.md` and `wiki/log.md` as first-class navigation/chronology files.
- Added a stronger schema file for future ingest/query/lint discipline.

## [2026-04-04] prompts | schema alignment
- Updated `prompts/compile-wiki.md` to explicitly follow `WIKI-SCHEMA.md`.
- Updated `prompts/answer-question.md` with schema-aware retrieval and output logging guidance.
- Added `prompts/lint-wiki.md` as a dedicated maintenance prompt.

## [2026-04-04] ingest | first schema-aligned pass
- Upgraded several important source notes with YAML frontmatter and stronger source-note structure.
- Reinforced foundational notes for `karpathy/llm-wiki`, the JUMPERZ architecture source, and the vectorless-RAG source.

## [2026-04-04] concepts | first compiled concept pages
- Added concept pages for persistent wiki architecture, multi-agent knowledge compilation, and vectorless retrieval.
- Linked them into `wiki/index.md`.

## [2026-04-04] lint | first maintenance pass
- Added `outputs/reports/first-lint-pass-2026-04-04.md`.
- Identified uneven source-note quality, sparse concept coverage, logging discipline needs, and media-backed social-source limitations.

## [2026-04-04] frontmatter | broadened structured notes
- Added YAML frontmatter to more foundational source notes, including the Karpathy origin note, `breferrari/obsidian-mind`, and `google/langextract`.

## [2026-04-04] reference | llm wiki architecture screenshot
- Added a compact architecture screenshot specifically showing the LLM wiki pattern.
- Linked it into the persistent-wiki concept page and top-level wiki index.

## [2026-04-04] source-capture | Karpathy follow-up idea-files commentary
- Captured a commentary source explaining Karpathy's follow-up around sharing "idea files" instead of only sharing code.
- Added it as supporting evidence for treating schema/prompt/architecture docs as first-class artifacts.

## [2026-04-04] synthesis | recommended operating model
- Synthesized the strongest current sources into `outputs/reports/recommended-operating-model.md`.
- Promoted durable conclusions back into the wiki by updating concept pages and adding `wiki/concepts/recommended-operating-model.md`.
- Reinforced the stance of persistent wiki compilation, vectorless retrieval first, and single-agent discipline before multi-agent scaling.

## [2026-04-04] entities | first entity pages
- Added first entity pages for Andrej Karpathy, Obsidian, and LangExtract.
- Connected them to relevant source notes and concept pages.

## [2026-04-04] governance | output promotion rules
- Added `docs/promotion-rules.md` to define when outputs should be promoted into the wiki.
- Linked the rule into `WIKI-SCHEMA.md` and `wiki/index.md`.

## [2026-04-04] adaptation | obsidian-mind patterns
- Compared `obsidian-mind` against the current vault and documented the fit in `docs/obsidian-mind-adaptation.md`.
- Added `wiki/home.md` as a human-facing landing page inspired by the stronger dashboard/lifecycle pattern.

## [2026-04-04] coordination | cross-agent onboarding
- Added `docs/claude-handoff.md` as a short operational handoff file for another agent.
- Added `docs/cross-agent-workflow.md` for file-based agent coordination.
- Added `docs/quickstart-for-other-agent.md` so a second agent can start cleanly without guessing.
