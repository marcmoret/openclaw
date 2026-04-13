---
title: AI Agents Cheat Sheet
type: source
created: 2026-04-10
updated: 2026-04-10
tags: [sources, image, reference, agents, architecture]
sources: [ai-agents-cheat-sheet-screenshot]
related: [multi-agent-orchestration, claude-code-ecosystem]
---

## Source Metadata

- **Type**: Screenshot / visual reference
- **Date captured**: April 3, 2026
- **Source file**: `/raw/assets/ai-agents-cheat-sheet-screenshot-2026-04-03.md`
- **Discovery**: [[jumperz-multi-agent-post]] (attached media)

## Key Contents

### What is an AI Agent?

An agent uses a language model to pursue a goal, understanding instructions, planning steps, and taking actions with tools or APIs.

### Core Components

- **Language Model** — LLM, SLM, or reasoning model
- **Tools** — Extensions, functions, data stores
- **Orchestration** — CoT, ToT, ReAct patterns
- **External Services** — APIs, databases, systems

### Orchestration Patterns

- **Chain-of-Thought (CoT)** — sequential reasoning
- **Tree-of-Thoughts (ToT)** — exploring multiple branches
- **ReAct** — reasoning + acting in loop
- **Single-agent** — one worker
- **Multi-agent with manager** — central coordinator
- **Decentralized multi-agent** — peer coordination

### Agentic Protocols

- **MCP** (Model Context Protocol) — standard agent ↔ tools interface
- **A2A** (Agent-to-Agent) — agent communication

### Agent Categories

- One-prompt agents
- Workflow-based agents
- Coding agents
- Agentic frameworks

## Why It Matters

This is a **comprehensive reference** for understanding:
- [[multi-agent-orchestration]] concepts and patterns
- How agents fit together architecturally
- Orchestration vs. agent categories
- Protocol standards (MCP, A2A)

Particularly useful for:
- Understanding jumperz 10-agent swarm design
- Understanding dr-cintas 27-agent system
- Framing [[claude-code-ecosystem]] agent structure

## Use Cases

- **Teaching:** Quick visual overview of agent concepts
- **Architecture:** Reference for designing multi-agent systems
- **Decision-making:** Which pattern/category for this task?
- **Communication:** Share with teams to align on terminology

## Related Concepts

- [[multi-agent-orchestration]] — detailed concept
- [[claude-code-ecosystem]] — Claude-specific implementation
- [[mcp|MCP]] — communication standard

## See Also

- [[multi-agent-orchestration]] for detailed patterns
- [[jumperz-multi-agent-post]] for application example
- [[dr-cintas-claude-code-setup]] for production example
