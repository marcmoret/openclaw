# Lint Wiki Prompt

Use this prompt with an LLM agent working inside this repository.

## Objective

Health-check the wiki for contradictions, stale claims, weak cross-linking, missing pages, and maintainability issues.

## Required first step

Read:
1. `WIKI-SCHEMA.md`
2. `wiki/index.md`
3. `wiki/log.md`
4. any relevant index pages

## Instructions

Look for:
- contradictions between pages
- stale claims that newer sources may supersede
- orphan pages with weak/no inbound relevance
- important concepts that are mentioned repeatedly but lack their own page
- missing cross-references
- unsupported or weakly-supported claims
- opportunities to merge, split, or clarify pages

## Output

Write the lint pass to `outputs/reports/` or `wiki/indexes/` depending on whether it is operational or durable.

Include:
- findings
- severity / importance
- proposed fixes
- optional follow-up source collection ideas

## Logging

Add a concise entry to `wiki/log.md` for meaningful lint passes.
