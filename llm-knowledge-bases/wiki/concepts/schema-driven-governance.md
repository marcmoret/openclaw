---
title: Schema-Driven Governance
type: concept
created: 2026-04-11
updated: 2026-04-12
tags: [schema, governance, llm-workflows, architecture, coordination]
sources: [karpathy-llm-wiki-gist, breferrari-obsidian-mind-repo, code-rams-post, akshay-pachaar-claude-folder, karpathy-skills-plugin]
related: [llm-wiki-pattern, claude-code-ecosystem, idea-files-prompt-as-code]
---

## Definition

Schema-driven governance is the principle that schema files (like `CLAUDE.md`, `WIKI-SCHEMA.md`, or `.claude/` configurations) are the actual coordination mechanism in LLM-maintained systems, not just documentation. The schema defines behavior, enforces conventions, and serves as the contract between human intent and LLM execution.

## Relevance to Our Work

This wiki project is a direct implementation of schema-driven governance. `CLAUDE.md` is not a README — it is the operating manual that governs how Claude maintains every page, processes every source, and logs every operation. Without it, the wiki would lack consistency across sessions.

## How It Works

The schema layer sits between raw sources and the maintained wiki in the [[llm-wiki-pattern]] three-layer architecture:

1. **Raw sources** — immutable input (articles, docs, transcripts)
2. **Schema** — `CLAUDE.md` defines page conventions, frontmatter format, workflows (ingest, query, lint), and linking rules
3. **Wiki** — LLM-maintained output that follows the schema consistently

The schema is what makes the wiki reproducible across sessions. A new Claude session reads `CLAUDE.md` and immediately knows how to maintain the wiki — no context from prior sessions needed.

## Where It Appears

- **[[karpathy-llm-wiki-gist]]** — The foundational concept document describes the schema layer as essential to the architecture; the LLM needs explicit operating instructions, not just content
- **[[breferrari-obsidian-mind]]** — Production implementation with `CLAUDE.md` governing 6 subagents, lifecycle hooks, and memory compaction rules
- **akshay-pachaar-claude-folder** — The `.claude/` folder anatomy shows how schema extends beyond a single file to encompass commands, agents, skills, hooks, and permissions as governance artifacts
- **[[code-rams-post]]** — The "idea files" concept treats schema documents as first-class artifacts worthy of the same care as source code
- **[[zodchiii-claude-hooks]]** — Hooks extend schema governance from advisory (`CLAUDE.md` ~80% compliance) to mandatory (hooks enforce 100% compliance)
- **[[karpathy-skills-plugin]]** — Demonstrates distributable governance: a CLAUDE.md packaged as a Claude Code plugin with marketplace, versioning, and dual install paths (plugin vs file copy)

## Key Insight

Schema-driven governance inverts the traditional documentation relationship. In most projects, documentation describes what the system does. In schema-driven systems, the documentation *prescribes* what the system does — it is the control plane, not the observation plane.

This means maintaining the schema is as important as maintaining the wiki content itself. A stale or imprecise `CLAUDE.md` produces inconsistent wiki pages across sessions.

## See Also

- [[llm-wiki-pattern]] for the full architecture this concept supports
- [[claude-code-ecosystem]] for how `.claude/` extends governance to tooling
- [[idea-files-prompt-as-code]] for the philosophical framing of schema as code
