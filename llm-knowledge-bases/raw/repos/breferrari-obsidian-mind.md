# Repo Source: breferrari/obsidian-mind

- URL: https://github.com/breferrari/obsidian-mind
- Host: GitHub
- Owner: breferrari
- Repo: obsidian-mind
- Type: repository
- Captured from:
  - https://x.com/tom_doerr/status/2039906409387610408?s=46

## Summary

An Obsidian vault template for engineers who use Claude Code as a thinking partner. The repository positions itself as a durable memory system for Claude Code: session context, notes, links, indexes, review evidence, and performance tracking all live in the vault rather than being trapped in chat history.

Key ideas surfaced from the repo README:
- vault-first memory, with durable knowledge stored in markdown notes
- a `CLAUDE.md` operating manual that governs behavior every session
- lifecycle hooks for session start, routing, validation, compaction backup, and wrap-up
- slash commands such as `/standup`, `/dump`, `/wrap-up`, `/weekly`, `/vault-audit`, and review-related commands
- subagents for maintenance, review prep, linking, profiling, and migration
- structured folders for work, org knowledge, performance evidence, and long-term brain notes
- optional semantic search via QMD

## Why it matters

This is directly relevant to the current project because it is a concrete example of an Obsidian-based memory vault maintained by an LLM agent. It offers strong ideas for folder structure, lifecycle hooks, review workflows, memory persistence, and the distinction between durable vault memory and lightweight auto-loaded indexes.

## Notable structure

- `Home.md` as the vault dashboard
- `CLAUDE.md` as the operating manual
- `brain/` for goals, memories, patterns, decisions, gotchas, and skills
- `work/`, `org/`, and `perf/` for operational knowledge
- `.claude/commands/`, `.claude/agents/`, and `.claude/skills/` for agent workflows
- `bases/` for dynamic database-style views

## Adaptation ideas for this project

- Use the repo as inspiration for wiki maintenance workflows, not as a direct drop-in replacement
- Borrow the ideas of lifecycle commands, maintenance/audit passes, and durable markdown memory
- Keep this project's `raw/` vs `wiki/` separation, which is more research-oriented than `obsidian-mind`
- Consider a future local equivalent of `CLAUDE.md` / operating manual specific to the knowledge-base compiler workflow

## Next action

Optionally inspect specific files like `README.md`, `CLAUDE.md`, and `Home.md` in more detail if we want to borrow conventions deliberately.
