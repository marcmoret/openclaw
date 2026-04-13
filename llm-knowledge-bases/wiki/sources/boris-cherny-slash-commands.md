---
title: 10 Slash Commands for Claude Code (Boris Cherny Pattern)
type: source
created: 2026-04-12
updated: 2026-04-12
tags: [claude-code, commands, workflow, developer-tooling, prompts]
sources: [raw/inbox/10 Slash Commands to Use Claude Code like Boris Cherny Does (with a bonus)!.md]
related: [claude-code-ecosystem, andrej-karpathy, idea-files-prompt-as-code, schema-driven-governance]
triage: summarized
---

# 10 Slash Commands for Claude Code (Boris Cherny Pattern)

Web Clipper capture of a detailed tutorial by @_avichawla demonstrating Boris Cherny's pattern of turning repeated Claude Code prompts into version-controlled custom commands. Each command is demonstrated on a real ML inference service (FastAPI, scikit-learn, Alembic).

## Core Insight

Repeated prompts suffer from **prompt drift** — slight wording changes between sessions produce inconsistent LLM output. Custom commands (`.claude/commands/` markdown files) solve both repetition and drift. Commands are Git-versioned, so the whole team runs identical prompts.

## Command Architecture

Commands live in two places:
- **Project-scoped** (shared via Git): `your-repo/.claude/commands/cmd.md` → `/cmd`
- **User-scoped** (personal): `~/.claude/commands/cmd.md` → `/cmd`

Features: `$ARGUMENTS` placeholder for dynamic input, `` !`shell command` `` for injecting live context (git state, file listings), YAML frontmatter for tool pre-approval and model override.

## The 10 Commands

1. **`/env-check`** — Validates local dev environment: runtime versions, dependencies, env vars, running services, git hooks. Outputs a checklist with fix commands.

2. **`/orient`** — Rebuilds working context after `/clear`. Reads uncommitted changes, recent commits, TODOs in modified files, and branch state. Forces Claude to synthesize (not just load) the context.

3. **`/preflight`** — Pre-commit scan: debug statements, TODOs, commented-out code, hardcoded secrets, `.only`/`.skip` in tests, debug flags. Reports only — doesn't fix.

4. **`/dissect <file>`** — Deep structural review: error handling gaps, edge cases, race conditions, unused imports, coupling, naming. Severity-rated findings with suggested fixes. Catches things linters miss.

5. **`/testmatch <file>`** — Generates tests that match existing project conventions. Reads 2-3 existing test files first to learn framework, assertion style, mocking approach, naming patterns. Tests look like a team member wrote them.

6. **`/explain-func <function>`** — Generates "why" documentation, not "what". Explains non-obvious decisions, invariants, constraints, gotchas. Explicitly avoids restating code.

7. **`/refactor-safe <file>`** — Refactors internals with hard constraint: public API must not change. Extracts helpers, simplifies conditionals, removes dead code. Runs tests after to verify.

8. **`/ship`** — PR preparation: runs test suite first, then generates PR description with summary, changes, test instructions, and risk assessment. Doesn't create the PR — outputs for review.

9. **`/migrate-draft <description>`** — Database migration generator: reads existing migrations for ORM conventions, reads application code for required columns, generates UP + DOWN with safety checklist (table locks, backwards compatibility, partial failure).

10. **`/debt-scan`** — Full project health scan: code complexity (god objects, long functions, high coupling), dependency staleness, test coverage gaps, code smells (any casts, eslint-disable), architectural smells (business logic in routes, circular deps). Prioritized by severity with effort estimates.

**Bonus: `/changelog`** — Release notes from commits. Reads diffs to understand actual changes, groups by Added/Changed/Fixed/Removed, writes user-facing impact (not code changes).

## Design Patterns

Several commands share a "learn then generate" pattern: `/testmatch` reads existing tests before writing new ones, `/migrate-draft` reads existing migrations before generating, `/orient` reads git state before summarizing. This produces output that matches project conventions rather than generic LLM defaults.

The "guard then execute" pattern appears in `/ship` (run tests → then generate PR) and `/preflight` (scan → report only, don't fix).

This reinforces the [[schema-driven-governance]] concept: the commands ARE schema—executable specifications of how Claude should behave in different contexts.

## Relationship to Karpathy's Work

These commands embody the [[idea-files-prompt-as-code]] principle: instead of repeating prompts, version-control them as code. The project-scoped `.claude/commands/` parallels Karpathy's observation that "the primary engineering work is maintaining schema files" ([[andrej-karpathy|Karpathy's token-spend shift]]).

## Source Files

- `raw/inbox/10 Slash Commands to Use Claude Code like Boris Cherny Does (with a bonus)!.md` — Full tutorial with command templates and video demos (39KB, Web Clipper)
