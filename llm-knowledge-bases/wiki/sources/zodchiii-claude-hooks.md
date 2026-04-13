---
title: 8 Claude Code Hooks That Automate What You Keep Forgetting
type: source
created: 2026-04-10
updated: 2026-04-10
tags: [claude-code-hooks, automation, lifecycle, formatting, security, testing, claude-code-ecosystem]
sources: [8 Claude Code Hooks That Automate What You Keep Forgetting.md, zodchiii-post-2040000216456143002]
related: [claude-code-ecosystem, akshay-pachaar-claude-folder, breferrari-obsidian-mind]
---

## Source Metadata
- **Author**: zodchiii
- **Date**: Early 2026
- **Type**: X post + Web Clipper version (full guide)
- **Format**: Detailed technical guide with hook examples and JSON configurations

## Executive Summary
A comprehensive guide to 8 Claude Code hooks that automate commonly forgotten maintenance tasks. Hooks are automatic actions that fire on file edits, command execution, or task completion. Unlike CLAUDE.md (which is advisory, ~80% compliance), hooks are mandatory—they run every time. The guide covers how hooks work (PreToolUse for validation, PostToolUse for cleanup) and provides ready-to-copy JSON configurations for formatting, security, testing, and validation workflows.

## Core Concept: Hooks vs CLAUDE.md
- **CLAUDE.md** is a suggestion: Claude reads it and follows it ~80% of the time
- **Hooks** are automatic: They execute every time Claude edits a file, runs a command, or finishes a task
- Think of hooks as: **PreToolUse = bouncer (inspection/blocking)**, **PostToolUse = QA (cleanup/validation)**

## Hook Configuration Locations
```
.claude/settings.json         # Project-level (committed to git, shared with team)
~/.claude/settings.json       # User-level (all your projects)
.claude/settings.local.json   # Local only (not committed)
```

**Best practice**: Project-level hooks in `.claude/settings.json` ensure entire team gets same automation.

## 8 Hooks Detailed

### Hook 1: Auto-format Every File Claude Touches
**Problem**: Claude writes correct code that breaks your formatting rules
**Solution**: Prettier (or black, gofmt, rustfmt) runs automatically after every file write/edit

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write 2>/dev/null; exit 0"
          }
        ]
      }
    ]
  }
}
```
**Swap out**: `npx prettier --write` for `black` (Python), `gofmt` (Go), `rustfmt` (Rust), etc.

### Hook 2: Block Dangerous Commands
**Problem**: Claude could run `rm -rf`, `git reset --hard`, `DROP TABLE`, `curl` to untrusted URLs
**Solution**: Validation hook that blocks destructive commands before execution

Create `.claude/hooks/block-dangerous.sh`:
- Pattern: Look for dangerous patterns in command
- Return exit code 2 to block
- Log attempts for audit

### Hook 3: Run Tests After Every File Edit
**Problem**: Claude edits code but forgets to run tests
**Solution**: PostToolUse hook runs test suite automatically

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "npm run test 2>/dev/null; exit 0"
          }
        ]
      }
    ]
  }
}
```

### Hook 4: Prevent Debugging Code from Being Committed
**Problem**: `console.log()`, `print()`, `debugger`, or temporary variables slip into commits
**Solution**: PreToolUse hook scans file for debug patterns; blocks commit if found

Pattern matching:
- `console.log`, `console.error`
- `debugger` statements
- `TODO`, `FIXME` comments
- Temporary variable names (e.g., `temp_x`)

### Hook 5: Enforce Git Commit Standards
**Problem**: Commits lack proper messages or conventional commit format
**Solution**: PreToolUse validates commit message format before committing

Enforce:
- Commit messages follow Conventional Commits (feat:, fix:, refactor:, etc.)
- Message length (50-char subject, 72-char body)
- Linked issue/ticket reference

### Hook 6: Auto-increment Version on Changes
**Problem**: Version number gets out of sync with changes
**Solution**: PostToolUse hook updates version in package.json/version.py/Cargo.toml

Pattern: After edit/write to core files, bump patch/minor/major version automatically

### Hook 7: Check for Hardcoded Secrets Before Commit
**Problem**: API keys, passwords, or tokens accidentally committed
**Solution**: PreToolUse hook scans for patterns matching secrets

Patterns to detect:
- `GITHUB_TOKEN=`, `API_KEY=`
- AWS key format: `AKIA...`
- Private key headers: `-----BEGIN PRIVATE KEY-----`
- Environment variable assignments with known secrets

### Hook 8: Auto-generate Docs When Function Signatures Change
**Problem**: Docstrings, README, or API docs fall out of sync
**Solution**: PostToolUse hook detects function signature changes; regenerates relevant docs

Pattern:
- After Edit to `.ts`/`.py` file: run doc generator
- Extract function signatures
- Regenerate markdown or JSDoc

## Hook Best Practices
1. **Keep hooks fast** — Long-running hooks slow down Claude
2. **Log failures quietly** — Use `2>/dev/null; exit 0` to prevent hook crashes
3. **Test hooks locally first** — Run `.claude/hooks/` scripts manually to verify
4. **Version hooks with code** — Commit `.claude/settings.json` to git for team consistency
5. **Use PreToolUse for validation**, **PostToolUse for cleanup**
6. **Combine multiple hooks** — Chain validators and formatters in sequence

## How It Relates to Existing Wiki Content
This guide extends [[claude-code-ecosystem]] with concrete implementation patterns:
- **CLAUDE.md** is covered in [[akshay-pachaar-claude-folder]]; hooks are the automation layer above it
- **Lifecycle automation** connects to [[multi-agent-orchestration]] (agent coordination needs lifecycle hooks)
- **Team-level conventions** match [[breferrari-obsidian-mind]] (shared .claude/ config across team)

Together with [[akshay-pachaar-claude-folder]], this guide provides complete `.claude/` folder understanding.

## Practical Applications for Knowledge Base
1. **Hook 1 (Auto-format)** — Could standardize wiki markdown formatting (ensure consistent YAML, wikilink format)
2. **Hook 7 (Detect secrets)** — Critical for wiki: prevent API keys/tokens from entering sources/
3. **Hook 8 (Auto-doc)** — Could regenerate wiki index/log when wiki structure changes
4. **Hook 5 (Commit standards)** — If wiki uses git: enforce commit messages like `[2026-04-10] ingest | Source Name`

## Key Insights
- **Hooks are mandatory; CLAUDE.md is advisory** — Use hooks for hard requirements
- **Project-level hooks = team contracts** — Everyone gets the same automation
- **PostToolUse for quality**, **PreToolUse for safety** — Clear separation of concerns
- **Hooks enable fire-and-forget automation** — Once set up, they run in background

## Direct Quotes Worth Preserving
- "CLAUDE.md is a suggestion. Hooks are different. They're automatic actions that fire every time Claude edits a file, runs a command, or finishes a task."
- "Think of it as a bouncer" (PreToolUse) and "quality control on the assembly line" (PostToolUse)
- "No more 'Claude forgot to format' commits."
- "Hooks should be the default for every project."
