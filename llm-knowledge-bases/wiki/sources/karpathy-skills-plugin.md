---
title: Karpathy-Inspired Claude Code Guidelines Plugin
type: source
created: 2026-04-12
updated: 2026-04-12
tags: [claude-code, plugin, guidelines, karpathy, best-practices, coding]
sources: [andrej-karpathy-skills-main]
related: [andrej-karpathy, claude-code-ecosystem, schema-driven-governance, idea-files-prompt-as-code, prompting-patterns, boris-cherny-slash-commands]
---

## Source Metadata

- **Title**: Karpathy-Inspired Claude Code Guidelines
- **Author**: forrestchang (GitHub)
- **Type**: Claude Code plugin / repository
- **Repository**: `forrestchang/andrej-karpathy-skills`
- **License**: MIT
- **Plugin ID**: `andrej-karpathy-skills@karpathy-skills`
- **Files**: README.md, CLAUDE.md (the behavioral guidelines), EXAMPLES.md (anti-pattern gallery), SKILL.md (plugin skill definition), plugin.json, marketplace.json

## Key Takeaways

- Packages [[andrej-karpathy]]'s observations about LLM coding pitfalls into four actionable principles enforced via a `CLAUDE.md` file or installable Claude Code plugin
- The four principles are: Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution
- Includes an extensive EXAMPLES.md (500+ lines) showing before/after pairs for each principle — real anti-patterns with surgical fixes
- Distributed as both a per-project `CLAUDE.md` and a Claude Code plugin (via marketplace), demonstrating the plugin distribution model for [[schema-driven-governance]] artifacts
- Explicitly acknowledges a tradeoff: guidelines bias toward caution over speed, with judgment expected for trivial tasks

## Detailed Summary

### The Four Principles

**1. Think Before Coding** — addresses LLMs making wrong assumptions silently. Rules: state assumptions explicitly, present multiple interpretations, push back when warranted, stop when confused.

**2. Simplicity First** — combats LLM tendency to overengineer. Rules: no features beyond what was asked, no abstractions for single-use code, no speculative flexibility. The litmus test: would a senior engineer say this is overcomplicated?

**3. Surgical Changes** — prevents scope creep in edits. Rules: don't improve adjacent code, match existing style, only clean up orphans your changes created. The litmus test: every changed line should trace directly to the user's request.

**4. Goal-Driven Execution** — transforms imperative tasks into verifiable goals. Pattern: reframe "fix X" as "write test that reproduces X, then make it pass." Multi-step tasks get explicit verify steps.

### Distribution Model

The plugin offers two installation paths: a Claude Code marketplace plugin (`/plugin marketplace add forrestchang/andrej-karpathy-skills`) and a simple `curl` to download `CLAUDE.md` into any project. This dual model shows how [[schema-driven-governance]] documents can be packaged and distributed like software dependencies.

### Examples Gallery

EXAMPLES.md provides paired before/after code for each principle — over-abstracted discount calculators, drive-by refactoring in bug fixes, vague vs verifiable plans. The examples consistently show that the "wrong" LLM outputs follow recognized design patterns (Strategy, Factory) but apply them prematurely.

## Entities and Concepts Mentioned

- **[[andrej-karpathy]]** — original observations that these guidelines distill
- **forrestchang** — plugin author who packaged the guidelines
- **[[claude-code-ecosystem]]** — plugin infrastructure (marketplace, skills, `.claude-plugin/`)
- **[[schema-driven-governance]]** — CLAUDE.md as behavioral contract, now distributable as a plugin

## How This Source Relates to Existing Wiki Content

- **Directly extends [[andrej-karpathy]]** — takes Karpathy's qualitative observations and operationalizes them into enforceable rules
- **Production example of [[schema-driven-governance]]** — the CLAUDE.md file is the governance artifact; the plugin distribution is a new pattern for sharing governance across projects
- **Complements [[boris-cherny-slash-commands]]** — Boris focuses on *what* to automate (10 commands); this plugin focuses on *how the LLM should behave* (4 principles). Together they cover behavioral + procedural governance
- **Extends [[idea-files-prompt-as-code]]** — the plugin is literally prompt-as-code: behavioral guidelines packaged with version, author, license, and marketplace metadata
- **Validates this wiki's own CLAUDE.md** — several of Marco's CLAUDE.md principles (Simplicity First, Surgical Changes, Surface Confusion) closely mirror the plugin's four principles, suggesting convergent design

## Notable Quotes

- From Karpathy (quoted in README): "LLMs are exceptionally good at looping until they meet specific goals… Don't tell it what to do, give it success criteria and watch it go."
