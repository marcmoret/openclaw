# Compile Wiki Prompt

Use this prompt with an LLM agent working inside this repository.

## Objective

Incrementally compile the contents of `raw/` into the markdown wiki under `wiki/`, following `WIKI-SCHEMA.md`.

## Required first step

Read these before making changes:
1. `WIKI-SCHEMA.md`
2. `wiki/index.md`
3. `wiki/log.md`
4. `wiki/indexes/source-triage.md` (when relevant)
5. `raw/_index/sources.json` if it exists

## Instructions

1. Inspect newly added or changed raw sources.
2. Decide whether each source should:
   - create/update a source note
   - update one or more concept/entity pages
   - update an index/map page
   - create a durable synthesis page
3. Create or update:
   - `wiki/source-notes/` pages for source-level summaries
   - `wiki/concepts/` pages for recurring concepts
   - `wiki/entities/` pages for named entities, projects, orgs, people, tools, methods, or datasets when relevant
   - `wiki/indexes/` pages for topic overviews and navigation
4. Keep social posts and linked primary artifacts separate, but cross-link them.
5. Distinguish between commentary, lead/pointer, media source, and primary evidence.
6. Add markdown links generously, but meaningfully.
7. Preserve provenance. Important claims should be traceable back to one or more raw sources.
8. Prefer incremental edits over full rewrites.
9. When useful, add `Open questions` and `Missing evidence` sections.
10. Update `wiki/index.md` when a source becomes foundational or durable.
11. Append a concise entry to `wiki/log.md` for meaningful ingests.

## Frontmatter convention

For durable wiki pages, prefer YAML frontmatter like:

```yaml
---
title: Page title
type: source-note | concept | entity | index | synthesis | reference
status: draft | active | summarized
source_type: social-post | repo | gist | article | paper | image | dataset | other
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - optional-tag
related:
  - wiki/relative/path.md
---
```

Use only fields that genuinely help.

## Constraints

- Do not delete raw material.
- Do not invent facts.
- Mark uncertain inferences explicitly.
- Prefer concise pages over bloated pages.
- Prefer many linked notes over giant monoliths.
- Treat the wiki as a persistent, compounding artifact.

## Suggested article template

```md
---
title: Title
type: source-note
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Title

## Summary

## Key points

## Related

## Sources

## Open questions
```
