---
title: Obsidian Integration
type: concept
created: 2026-04-10
updated: 2026-04-10
tags: [obsidian, tools, knowledge-base, ux, frontend]
sources: [breferrari-obsidian-mind, tom-doerr-post, karpathy-llm-wiki-gist]
related: [llm-wiki-pattern, claude-code-ecosystem, persistent-knowledge-base]
---

## Definition

Using Obsidian.md as the frontend IDE and navigation tool for LLM-maintained markdown knowledge bases. Obsidian provides wikilinks, graph views, search, and local-first sync.

## Why Obsidian

- **Wikilinks** — `[[page-name]]` syntax for cross-linking
- **Graph view** — visual navigation of knowledge relationships
- **Local-first** — vault is just markdown files on disk
- **Extensible** — plugins for semantic search, automation, and workflows
- **Git-friendly** — works naturally with version control

## Integration with LLM Workflows

In the [[llm-wiki-pattern]]:
1. LLM maintains markdown pages with wikilinks
2. Human opens the vault in Obsidian
3. Human browses, searches, and asks questions
4. LLM reads the vault when answering or ingesting new sources

Obsidian becomes the **human interface** while the LLM does the **maintenance and synthesis**.

## Obsidian + Claude Code

[[breferrari-obsidian-mind]] shows a production integration:

- **Home.md** — vault dashboard
- **CLAUDE.md** — operating manual for the LLM agent
- **brain/** — persistent memories (goals, patterns, decisions)
- **work/** — current workstreams
- **perf/** — performance evidence and metrics
- **.claude/commands/** — slash commands (`/standup`, `/wrap-up`)
- **.claude/agents/** — subagent definitions
- **.claude/skills/** — reusable capabilities

### Lifecycle Hooks
- Session start
- Routing (which agent/skill?)
- Validation (is the vault consistent?)
- Compaction (archive old sessions)
- Backup (persist to external storage)
- Wrap-up (log what happened, update memories)

## Features Worth Borrowing

- The `.claude/` folder structure for commands, agents, and skills
- The CLAUDE.md operating manual (like our CLAUDE.md schema)
- Lifecycle hooks for session start/end
- Subagent specialization (maintenance, review, linking, profiling)
- Optional semantic search via plugins (QMD)

## Where It Appears

- [[breferrari-obsidian-mind]] — full production template
- [[tom-doerr-obsidian-vault]] — pointer to the obsidian-mind repo
- [[karpathy-llm-wiki-gist]] — mentions Obsidian as the recommended frontend

## See Also

- [[breferrari-obsidian-mind]] for detailed structure
- [[claude-code-ecosystem]] for agent integration patterns
- [[llm-wiki-pattern]] for the overall architecture
