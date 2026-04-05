---
title: breferrari/obsidian-mind
type: source-note
status: summarized
source_type: repo
created: 2026-04-03
updated: 2026-04-04
tags:
  - obsidian
  - memory
  - workflow
related:
  - wiki/source-notes/karpathy-llm-wiki-gist.md
  - wiki/source-notes/chenglou-pretext.md
---

# Source Note: breferrari/obsidian-mind

## Summary

GitHub repository linked from Tom Dörr's X post about an Obsidian vault for Claude Code memory. It is an Obsidian vault template for engineers using Claude Code as a thinking partner, with persistent vault-based memory, commands, hooks, subagents, and review/performance workflows.

## Source type

- Repository
- Primary artifact

## Why relevant

This is a concrete implementation example closely aligned with the knowledge-base / memory-vault workflow being explored. It is especially relevant for:
- persistent markdown-based memory
- Obsidian as the frontend
- command-driven maintenance workflows
- session lifecycle hooks
- structured agent-maintained vault organization

## Notable takeaways

- Store durable knowledge in the vault, not only in auto-loaded assistant memory files
- Use a governing instruction file (`CLAUDE.md`) to define routing and conventions
- Use maintenance commands and audit passes to keep the vault coherent
- Separate note homes from graph meaning: folders for storage, links for context

## Open questions

- Which conventions are worth borrowing directly versus adapting?
- How much of the command/hook pattern should be mirrored in this project?
- Which parts assume Claude Code specifically, versus applying to any LLM-driven knowledge vault?

## Sources

- [raw/repos/breferrari-obsidian-mind.md](../raw/repos/breferrari-obsidian-mind.md)
- [raw/x/2026-04-03-tom-doerr-2039906409387610408.md](../raw/x/2026-04-03-tom-doerr-2039906409387610408.md)
