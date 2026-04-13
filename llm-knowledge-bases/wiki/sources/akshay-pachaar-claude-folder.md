---
title: Anatomy of the .claude Folder
type: source
created: 2026-04-10
updated: 2026-04-10
tags: [claude-code, .claude-folder, CLAUDE.md, commands, agents, skills, permissions, memory, hooks, settings]
sources: [Anatomy of the .claude folder.md]
related: [claude-code-ecosystem, zodchiii-claude-hooks, breferrai-obsidian-mind, boris-cherny-slash-commands]
---

## Source Metadata
- **Author**: akshay_pachaar
- **Date**: Early 2026
- **Type**: X post + Web Clipper version (full technical guide)
- **Format**: Comprehensive anatomy with file structures, code examples, best practices

## Executive Summary
A complete guide to the `.claude/` folder—the control center for how Claude behaves in a project. There are actually two `.claude/` directories: **project-level** (committed to git, shared with team) and **global** `~/.claude/` (personal preferences, machine-local state). This guide walks through every file and folder, from CLAUDE.md (instruction manual) to commands, agents, skills, hooks, memory, and permissions.

## Two .claude Directories, Not One

### Project-Level: `.claude/` (committed to git)
- Team configuration: shared rules, commands, permissions
- Everyone on the team gets the same setup
- Stored in version control

### Global: `~/.claude/` (user machine)
- Personal preferences and machine-local state
- Session history, auto-memory, user-specific settings
- Not shared; machine-specific

## Core Files and Folders

### CLAUDE.md: Claude's Instruction Manual
**Most important file.** When Claude Code session starts, first thing it reads is CLAUDE.md. Loaded straight into system prompt; stays in mind for entire conversation.

**What to write:**
- Build, test, lint commands (npm run test, make build, etc.)
- Key architectural decisions
- Non-obvious gotchas (TypeScript strict mode, etc.)
- Import conventions, naming patterns, error handling styles
- File/folder structure for main modules

**What NOT to write:**
- Anything that belongs in a linter/formatter config
- Full documentation you can already link to
- Long paragraphs explaining theory

**Best practice:** Keep under 200 lines. Longer files eat too much context; instruction adherence drops.

**Example minimal CLAUDE.md:**
```
# Project: Acme API

## Commands
npm run dev          # Start dev server
npm run test         # Run tests (Jest)
npm run lint         # ESLint + Prettier check
npm run build        # Production build

## Architecture
- Express REST API, Node 20
- PostgreSQL via Prisma ORM
- All handlers live in src/handlers/
- Shared types in src/types/

## Conventions
- Use zod for request validation in every handler
- Return shape is always { data, error }
- Never expose stack traces to the client
- Use the logger module, not console.log

## Watch out for
- Tests use a real local DB, not mocks. Run `npm run db:test:reset` first
- Strict TypeScript: no unused imports, ever
```

### .claude/commands/ — Slash Commands
Custom commands (e.g., `/test`, `/deploy`, `/review-pr`) that Claude can execute.

**File format:**
```
.claude/commands/test.md
```
Inside: Simple markdown defining what `/test` does, parameters, examples.

**Example:**
```markdown
# /test
Run the full test suite, report coverage, and flag untested functions.

Usage: /test [--watch] [--coverage]
```

### .claude/agents/ — Agent Definitions
If using multi-agent setup, each agent gets a definition file.

**File format:**
```
.claude/agents/plan-agent.md
.claude/agents/review-agent.md
.claude/agents/build-agent.md
```

**Contains:** Role, responsibilities, which commands/skills it has access to, personality.

### .claude/skills/ — Reusable Skills
Encapsulated workflows/knowledge that agents can apply. Think: "expertise modules."

**File format:** `.md` files following standard skill template
```
.claude/skills/tdd.md
.claude/skills/token-optimization.md
.claude/skills/security-audit.md
```

Each skill is self-contained, importable, composable with other skills.

### .claude/hooks/ — Lifecycle Automation
See [[zodchiii-claude-hooks]] for detailed breakdown. Hook scripts live here:
```
.claude/hooks/pre-commit.sh
.claude/hooks/block-dangerous.sh
.claude/hooks/auto-format.sh
```

### .claude/settings.json — Configuration & Hooks
Project-level settings and hook definitions in JSON.

**Contains:**
- Hook definitions (PreToolUse, PostToolUse)
- Claude Code behavior flags
- Memory settings
- Permissions configuration

### .claude/permissions.json — Access Control
Defines what Claude can access and modify:
```json
{
  "allowedDirectories": ["src/", "tests/"],
  "deniedDirectories": [".env", "secrets/"],
  "allowedCommands": ["npm run test", "git status"],
  "deniedCommands": ["rm -rf", "git reset --hard"]
}
```

### ~/.claude/memory/ — Session History (User-Level)
Auto-maintained session transcripts. Claude reads prior sessions to maintain context.

**Enables:** Multi-session continuity without manual context injection

### .claude/CLAUDE.md vs Global ~/.claude/CLAUDE.md
- **Project-level** `.claude/CLAUDE.md` — Team conventions
- **Global** `~/.claude/CLAUDE.md` — Personal preferences across all projects
- Claude reads both and combines them

Same with commands, agents, skills: can exist at project OR global level.

## Why This Folder Structure Matters

### For Teams
- **Shared `.claude/` = shared context** — Entire team starts with same instructions
- **Committed to git** — No drift; code reviews catch changes to how Claude works
- **Discoverability** — New team members can read `.claude/` to understand project conventions

### For Complex Projects
- **Agents + skills** — Each agent can have specific skills
- **Commands as contracts** — `/test`, `/deploy` become repeatable operations
- **Hooks as safety rails** — Automatic validation/formatting/testing without asking

### For Consistency
- **CLAUDE.md as source of truth** — One place to document project conventions
- **Permissions as guardrails** — Explicitly define what Claude can/cannot touch
- **Hooks as enforcement** — Rules run automatically, not advisory

## Relationship to Wiki/Knowledge Base Pattern
This folder structure mirrors the [[llm-wiki-pattern]]:
- **CLAUDE.md** = instructions (like wiki schema)
- **commands/** = custom workflows (like wiki/analyses/)
- **skills/** = reusable knowledge (like wiki/concepts/)
- **hooks/** = automation/maintenance (like wiki lifecycle)

## How It Relates to Existing Wiki Content
- **[[zodchiii-claude-hooks]]** — Details on hooks implementation
- **[[claude-code-ecosystem]]** — Broader ecosystem; this is the folder anatomy
- **[[breferrari-obsidian-mind]]** — Shows real example of `.claude/` with subagents and semantic search
- **[[multi-agent-orchestration]]** — Uses this structure for agent coordination

## Best Practices from the Guide
1. **Keep CLAUDE.md under 200 lines** — Smaller context footprint = better adherence
2. **Write only what's needed** — No theory, no redundancy with existing docs
3. **Commit `.claude/` to git** — Team consistency and version history
4. **Use hooks for hard rules** — CLAUDE.md is advisory; hooks are mandatory
5. **Organize by concern** — Commands, agents, skills, hooks each have a place
6. **Make permissions explicit** — Better to whitelist than blacklist

## Key Insights for Knowledge Bases
- `.claude/` folder can version-control how the LLM maintains the knowledge base
- **CLAUDE.md** could define wiki schema (frontmatter rules, linking conventions)
- **Hooks** could enforce wiki quality (valid YAML, wikilinks checked, etc.)
- **Skills** could standardize source summarization, entity extraction, etc.
- **Commands** could be wiki operations (/ingest, /lint, /query, /sync)

## Direct Quotes Worth Preserving
- "The .claude folder is the control center for how Claude behaves in your project."
- "Most Claude Code users treat the .claude folder like a black box."
- "Once you understand what lives where and why, you can configure Claude Code to behave exactly the way your team needs it to."
- "Keep CLAUDE.md under 200 lines. Files longer than that start eating too much context, and Claude's instruction adherence actually drops."
