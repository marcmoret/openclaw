# Wiki Schema — LLM Knowledge Bases

Marco's personal knowledge base, shared across multiple computers. The LLM (Claude) maintains all wiki content. Marco curates sources, directs analysis, and asks questions. Claude does the summarizing, cross-referencing, filing, and bookkeeping.

## Multi-Computer Setup

This repository is shared between multiple machines via git. Any computer with access can ingest sources, query the wiki, and run lint passes. Coordination happens through the repository itself — not agent-to-agent chat history.

**Before doing substantial work**, always read:
1. This file (`CLAUDE.md`)
2. `wiki/index.md`
3. `wiki/log.md`
4. `docs/claude-handoff.md`

**After doing substantial work**, always update:
- `wiki/log.md` — chronological record of what was done
- `wiki/index.md` — if new pages were created
- `docs/claude-handoff.md` — if priorities or architecture changed

## Directory Structure

```
llm-knowledge-bases/
├── CLAUDE.md          ← This file. Schema and conventions.
├── raw/               ← Source documents. Immutable. Claude reads but never modifies.
│   ├── x/             ← X/Twitter posts and social media captures.
│   ├── repos/         ← Repository snapshots and gists.
│   ├── inbox/         ← New sources pending ingest. Drop files here.
│   ├── images/        ← Screenshots, diagrams, visual references.
│   ├── articles/      ← Web articles, blog posts.
│   ├── papers/        ← Academic papers, whitepapers.
│   └── datasets/      ← Structured data files.
├── wiki/              ← LLM-maintained markdown pages. Claude owns this entirely.
│   ├── index.md       ← Master catalog of all wiki pages.
│   ├── log.md         ← Chronological record of all operations.
│   ├── overview.md    ← High-level summary of the entire knowledge base.
│   ├── entities/      ← Pages for people, companies, products, tools.
│   ├── projects/      ← Pages for projects, initiatives, workstreams.
│   ├── concepts/      ← Pages for ideas, frameworks, methodologies.
│   ├── sources/       ← Summary pages for each ingested source.
│   ├── analyses/      ← Comparisons, deep-dives, lint reports.
│   ├── meetings/      ← Meeting summaries and action items.
│   └── sessions/      ← Session mining overviews.
├── docs/              ← Operational documentation for the project itself.
├── prompts/           ← Reusable prompts for wiki operations.
├── tools/             ← CLI tools for wiki stats, indexing, etc.
└── outputs/           ← Task-time artifacts (reports, answers, derivations).
```

## Page Conventions

### Frontmatter
Every wiki page starts with YAML frontmatter:

```yaml
---
title: Page Title
type: entity | project | concept | source | analysis | meeting
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [relevant, tags]
sources: [list of source filenames this page draws from]
related: [bare-filenames-without-extension]
status: active | stub | stale
---
```

### Linking (Obsidian Wikilinks)
- Use Obsidian wikilinks for all internal wiki references: `[[page-name]]` or `[[page-name|Display Text]]`
- The page name is the filename without extension (e.g., `[[andrej-karpathy]]`, `[[vectorless-retrieval]]`)
- Use display text when the filename isn't human-readable: `[[dkare1009-vectorless-rag-post|Vectorless RAG post]]`
- In YAML frontmatter `related:` arrays, use bare filenames: `related: [vectorless-retrieval, persistent-knowledge-base]`
- Do NOT convert external URLs (https://) — keep those as standard markdown links
- Do NOT convert links to `raw/` source files or `docs/` — those are outside the wiki
- When mentioning an entity, project, or concept that has its own page, always link to it

### Source Handling Rules
- Treat social/X posts as first-class sources. Distinguish between commentary, lead/pointer, media source, and primary evidence.
- If a social post links to a repo/article/tool, capture that as a separate primary source.
- Treat repos and gists as primary artifacts. Summarize what it is, why it matters, and how it fits.
- Treat screenshots as conceptual references when they contain architecture, workflow, or guidance.

### Page Structure
Each page type has a standard structure:

**Entity pages** (people, companies, products):
- Summary (2-3 sentences), Key details, Timeline of mentions, Related pages, Sources

**Project pages**:
- Summary and status, Key people, Timeline/milestones, Decisions and rationale, Open questions, Related pages, Sources

**Concept pages**:
- Definition/explanation, Relevance to our work, Where it appears, Related concepts, Sources

**Source summary pages**:
- Source metadata, Key takeaways, Detailed summary, Entities and concepts mentioned, How it relates to existing wiki content

**Analysis pages**:
- Question/topic, Methodology, Findings, Implications, Related pages, Sources

**Meeting pages**:
- Date/attendees/purpose, Key discussion points, Decisions, Action items, Follow-ups

## Operations

### Ingest Workflow
When a new source arrives in `raw/`:

1. **Read** the source document completely.
2. **Create** a source summary page in `wiki/sources/`.
3. **Create or update** entity pages for any people, companies, or products mentioned.
4. **Create or update** project pages if relevant projects are discussed.
5. **Create or update** concept pages for important ideas or frameworks.
6. **Update** `wiki/index.md` with any new pages.
7. **Append** to `wiki/log.md` with a summary of what was done.
8. **Flag contradictions** — if the new source contradicts existing wiki content, note it explicitly.

### Query Workflow
When asked a question:

1. **Read** `wiki/index.md` to identify relevant pages.
2. **Read** the relevant wiki pages.
3. **Synthesize** an answer with citations to wiki pages and original sources.
4. **Offer to file** the answer as an analysis page if it's substantive enough.
5. **Append** to `wiki/log.md`.

### Lint Workflow
Periodically review the wiki for:

1. **Contradictions** between pages.
2. **Stale content** that newer sources may have superseded.
3. **Orphan pages** with no inbound links.
4. **Missing pages** — concepts or entities mentioned but lacking their own page.
5. **Missing cross-references** between related pages.
6. **Broken wikilinks** pointing to non-existent pages.
7. Report findings and fix issues. Append to `wiki/log.md`.

## Log Format

`wiki/log.md` entries use this format for parseability:

```markdown
## [YYYY-MM-DD] operation | Subject
Brief description of what was done.
Pages created: [list]
Pages updated: [list]
```

## Retrieval Philosophy

Default to lightweight retrieval first: index pages, source notes, keyword search, structured navigation, direct context injection. Do not assume embeddings or vector infrastructure are required at this scale. Those are optional enhancements for later.

## Promotion Rule

Not every output belongs in the wiki. Promote when durable, reusable, clarifying, or likely to matter again. Do not promote every transient chat answer. See `docs/promotion-rules.md`.

## Guiding Principles

1. **Compound, don't repeat.** Every interaction should leave the wiki richer. File good answers back as pages.
2. **Link aggressively.** The connections between pages are as valuable as the pages themselves.
3. **Flag contradictions.** Don't silently overwrite — note when new information conflicts with old.
4. **Stay current.** When updating a page, update its `updated` date and check linked pages are consistent.
5. **Marco decides, Claude executes.** Claude suggests; Marco approves changes to emphasis, structure, or direction.
6. **Sources are sacred.** Never modify anything in `raw/`. That's the source of truth.
7. **Repository is the shared truth.** Coordination between machines and agents happens through files, not chat history.
