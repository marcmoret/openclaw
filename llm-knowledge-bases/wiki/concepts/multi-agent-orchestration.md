---
title: Multi-Agent Orchestration
type: concept
created: 2026-04-10
updated: 2026-04-10
tags: [agents, llm-systems, orchestration, coordination, architecture]
sources: [jumperz-post-2040166448492900356, dr-cintas-post, explorax-m0h-post, ai-agents-cheat-sheet, voxira-architecture]
related: [claude-code-ecosystem, mcp, voxira, livekit, schema-driven-governance]
---

## Definition

Multi-agent orchestration is the design and coordination of multiple AI agents working together toward shared goals, with mechanisms for communication, task distribution, memory sharing, and failure handling.

## Core Components

From the AI Agents Cheat Sheet:

### Orchestration Patterns
- **Chain-of-Thought (CoT)** — sequential reasoning steps
- **Tree-of-Thoughts (ToT)** — exploring multiple reasoning branches
- **ReAct** — reasoning + acting in a loop

### Architecture Patterns
- **Single-agent systems** — one agent doing all work
- **Multi-agent systems with manager** — central coordinator distributes tasks
- **Decentralized multi-agent systems** — agents coordinate peer-to-peer

### Agentic Protocols
- **MCP** (Model Context Protocol) — standardized agent ↔ tools interface
- **A2A** (Agent-to-Agent) — agent ↔ agent communication

## Scaling the Wiki Pattern

jumperz extended [[llm-wiki-pattern|Karpathy's wiki pattern]] to multi-agent architectures:

1. Each agent auto-dumps its output into a `raw/` folder as it works
2. A compiler runs periodically (every few hours) and organizes everything into the wiki
3. All agents read from the same organized wiki for context

This creates a cycle:
- **Work phase**: Agents operate independently, dumping raw outputs
- **Compile phase**: LLM aggregates, deduplicates, and organizes into wiki
- **Context phase**: Agents read the wiki for shared knowledge

## Agents vs Skills vs Commands

- **Agents** — autonomous workers with goals and tools
- **Skills** — reusable capabilities (e.g., "code review", "documentation")
- **Commands** — human-triggered workflows (e.g., `/standup`, `/wrap-up`)

## Where It Appears

- jumperz — 10-agent swarm using wiki pattern
- dr-cintas — 27-agent Claude Code setup (Anthropic hackathon winner)
- explorax-m0h — 20 powerful agentic skills
- [[breferrari-obsidian-mind]] — subagents for maintenance, review, linking, profiling

## Related Concepts

- [[claude-code-ecosystem]] — Specific to Claude Code environment
- [[mcp|MCP]] — Communication standard
- [[multi-agent-orchestration]] — Orchestration and design patterns

## Open Questions & Failure Modes

From the dr_cintas thread debate, a key unresolved tension:

> "27 agents running concurrently is a race condition factory. Failure modes scale exponentially — 27 agents means 351 possible pairwise failure modes before you touch the actual work." — @ashcotXBT

> "The hard part is not spawning agents, it is managing shared state. One agent hands off mid-feature and the other has no idea what context it needs." — @ashcotXBT

Counter-argument: role separation (planning, review, testing, security) reduces coupling and failure surface. The [[llm-wiki-pattern]] approach of a shared compiled wiki may be the answer to the shared-state problem — agents read from one organized source rather than passing context between themselves.

## Production Example: [[voxira]]

The [[voxira]] healthcare voice agent platform is a production implementation of multi-agent orchestration applied to telephony. It uses 15+ specialized agents (consent, patient identification, scheduling, caller requests) orchestrated through intent-based transfer and sequential routing on [[livekit]]. Key architectural decisions:

- Agents extend a `BaseAgent` with shared tooling (prompt injection, STT boosting, variable observation)
- Routing uses both intent-based transfer (`set_caller_intent` → routing helpers) and deterministic sequential flows (patient identification steps)
- Shared state managed through `UserData` context model with observer pattern, avoiding the pairwise failure modes discussed above
- Multi-tenant dynamic configuration per clinic overrides prompts, policies, and even the AI stack (LLM/STT/TTS selection)

## See Also

- [[ai-agents-cheat-sheet]] for visual reference
- [[dr-cintas-everything-claude-code]] for production multi-agent system example with thread debate
- [[claude-code-ecosystem]] for skills and commands patterns
- [[voxira]] for production healthcare multi-agent system
