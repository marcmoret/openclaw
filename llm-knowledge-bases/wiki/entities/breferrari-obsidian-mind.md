---
title: breferrari/obsidian-mind
type: entity
created: 2026-04-10
updated: 2026-04-10
tags: [tools, repositories, obsidian, claude-code, memory]
sources: [breferrari-obsidian-mind, tom-doerr-post]
related: [obsidian-integration, claude-code-ecosystem, multi-agent-orchestration]
---

## Summary

`breferrari/obsidian-mind` is a production Obsidian vault template for engineers who use Claude Code as a thinking and automation partner. It provides a durable memory system for Claude Code sessions: persistent notes, indexes, hooks, commands, and multi-agent coordination.

## Key Structure

### Core Files
- **Home.md** — vault dashboard
- **CLAUDE.md** — operating manual governing LLM agent behavior
- **.claude/commands/** — slash commands (`/standup`, `/dump`, `/wrap-up`, `/weekly`, `/vault-audit`)
- **.claude/agents/** — subagent definitions
- **.claude/skills/** — reusable capabilities

### Content Folders
- **brain/** — persistent memories (goals, patterns, decisions, gotchas, skills)
- **work/** — current workstreams and projects
- **org/** — organizational knowledge
- **perf/** — performance evidence and metrics
- **bases/** — dynamic database-style views

## Session Lifecycle

1. **Start** — Load session context, initialize hooks
2. **Routing** — Dispatch to appropriate agent/skill
3. **Validation** — Health-check vault consistency
4. **Compaction** — Archive old sessions
5. **Backup** — Persist to external storage
6. **Wrap-up** — Log activity, update long-term memories

## Multi-Agent Design

The vault supports subagent specialization:
- **Maintenance agent** — keeps vault clean and consistent
- **Review agent** — prepares evidence for decision-making
- **Linking agent** — creates cross-references
- **Profiling agent** — tracks performance metrics
- **Migration agent** — handles structural changes

## Semantic Search Integration

Optional integration with plugins like QMD for semantic search over vault contents while maintaining the markdown-first architecture.

## Why It Matters

This is a production-grade example of:
- **[[obsidian-integration]]** with Claude Code
- **[[claude-code-ecosystem]]** patterns (commands, agents, hooks, skills)
- **[[multi-agent-orchestration]]** at scale
- Adapting [[llm-wiki-pattern]] for a single engineer's workflow

## Adaptation for This Project

Key ideas borrowed (without direct copying):
- CLAUDE.md as the operating manual (check ✓)
- Lifecycle hooks for session start/end
- Structured folders for different knowledge types
- Commands for maintenance and review
- Subagent specialization for complex tasks

This wiki diverges:
- Maintains [[llm-wiki-pattern]]'s raw/ vs wiki/ separation (more research-oriented)
- Focus on ingesting external sources, not personal session notes
- Index-and-log-driven rather than semantic-search-first

## Related Projects

- [[karpathy-llm-wiki-gist]] — foundational pattern
- [[jumperz-multi-agent-post]] — multi-agent wiki extension
- [[claude-code-ecosystem]] — broader ecosystem

## See Also

- GitHub: https://github.com/breferrari/obsidian-mind
- [[breferrari-obsidian-mind-repo]] for repository documentation
- [[tom-doerr-obsidian-vault]] for discovery
- [[obsidian-integration]] for broader context
