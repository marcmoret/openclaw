---
title: "Your Harness, Your Memory — Agent Memory Ownership"
type: source
created: 2026-04-12
updated: 2026-04-12
tags: [agent-harness, memory, lock-in, open-source, langchain]
sources: [raw/inbox/Your harness, your memory.md]
related: [llm-wiki-pattern, multi-agent-orchestration, claude-code-ecosystem]
triage: summarized
---

# Your Harness, Your Memory — Agent Memory Ownership

Blog post arguing that agent harnesses (the scaffolding around LLMs) are inseparable from agent memory, and that using closed/proprietary harnesses means losing control of your agent's memory — creating dangerous platform lock-in.

## Core Thesis

Agent harnesses are not going away — even as models absorb some scaffolding, new scaffolding replaces it. An agent by definition is an LLM interacting with tools and data sources, requiring a system around it. Evidence: Claude Code's leaked source was 512K lines of code — that's the harness.

**Memory is not a plugin — it IS the harness.** The harness manages all context: short-term (conversation messages, tool results), long-term (cross-session memory), and everything in between (AGENTS.md loading, skill metadata, compaction decisions, filesystem exposure).

## Lock-In Spectrum

From mild to severe:
1. **Stateful APIs** (OpenAI Responses API, Anthropic server-side compaction) — state stored on their server, can't migrate threads to another model
2. **Closed harnesses** (Claude Agent SDK / Claude Code) — harness interacts with memory in unknown ways, artifacts are non-transferable
3. **Full harness behind API** (Anthropic Claude Managed Agents) — zero ownership or visibility into memory, including long-term memory. Most alarming scenario.

Model providers are incentivized to move more behind APIs because memory creates lock-in that models alone don't. Example: Codex generates encrypted compaction summaries unusable outside OpenAI ecosystem.

## Why Memory Matters

Without memory, agents are easily replicable by anyone with the same tools. With memory, you build a proprietary dataset of user interactions and preferences — a data flywheel for increasingly intelligent, personalized experiences.

Anecdote: Author's email assistant got accidentally deleted. Recreating from the same template produced a much worse experience — had to reteach preferences, tone, everything. Demonstrated how powerful and sticky memory is.

## Proposed Solution

Open harnesses with open memory. The post advocates for LangChain's Deep Agents framework: open source, model agnostic, uses open standards (agents.md, skills), pluggable memory storage (Mongo, Postgres, Redis), self-hostable deployment.

## Relevance to Wiki

This directly validates the [[llm-wiki-pattern]] approach: by maintaining memory as local markdown files (wiki/) governed by a schema (CLAUDE.md), we own our memory completely. It's model-agnostic, portable, and transparent. The wiki IS the open memory layer the post argues for — just implemented as files rather than a database.

Key people mentioned: Sarah Wooders (Letta CTO, "memory isn't a plugin"), Sydney Runkle, Harrison Chase (LangChain).

## Source Files

- `raw/inbox/Your harness, your memory.md` — Full blog post (11KB, Web Clipper)
