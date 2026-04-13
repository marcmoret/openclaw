---
title: Jumperz - Multi-Agent Wiki Architecture
type: source
created: 2026-04-10
updated: 2026-04-10
tags: [sources, social, architecture, multi-agent, llm-wiki]
sources: [jumperz-post-2040166448492900356]
related: [multi-agent-orchestration, llm-wiki-pattern, ai-agents-cheat-sheet]
---

## Source Metadata

- **URL**: https://x.com/jumperz/status/2040166448492900356
- **Author**: jumperz (@jumperz)
- **Type**: X / Social post
- **Date**: Unknown (early April 2026)
- **Role**: Commentary / architecture media source
- **Source file**: `/raw/x/2026-04-03-jumperz-2040166448492900356.md`

## Key Takeaways

- Extends [[llm-wiki-pattern]] to 10-agent swarm architecture
- Agents dump raw outputs to `raw/` folder
- Compiler runs every few hours, organizes into wiki
- Demonstrates raw → compile → organize cycle at scale
- Includes AI Agents Cheat Sheet as attached media

## Post Text Summary

"took karpathy's wiki pattern and wired it into my 10 agent swarm and here is what the architecture looks like when you make it multi agent:

> every agent auto dumps its output into a raw/ folder as it works
> a compiler runs every few hours and organises everything into ..."

## Detailed Summary

This post shows how to scale [[llm-wiki-pattern]] to multiple agents:

### The Flow
1. **Work phase** — Each of 10 agents operates independently
2. **Dump phase** — All agents auto-save their outputs to `raw/`
3. **Compile phase** — Compiler runs periodically (every few hours)
4. **Organize phase** — Outputs get deduplicated, organized, filed into wiki
5. **Context phase** — All agents can read the organized wiki for context

This creates a **feedback loop**:
- Agents work → raw outputs
- Compiler organizes → wiki updates
- Agents read → improved context
- Back to work with better information

### Why This Matters

It shows that the [[llm-wiki-pattern]] scales beyond single-human workflows. The key insight:
- Multiple workers (agents, humans, systems)
- Single persistent knowledge sink
- Regular compilation and organization
- All workers read from the same organized knowledge

This is exactly the pattern being followed in this wiki project at a smaller scale.

## Attached Media

The post includes "AI Agents Cheat Sheet" covering:
- Language models, tools, orchestration, data stores, extensions
- Orchestration patterns: CoT, ToT, ReAct
- Agentic protocols: MCP, A2A
- Agent categories and frameworks

See [[ai-agents-cheat-sheet]] for details.

## Concepts Introduced

- [[multi-agent-orchestration]] — the architecture pattern
- Scaling [[llm-wiki-pattern]]

## Why It Matters

- Demonstrates the pattern works at scale (10 agents)
- Shows the `raw/` folder model in action
- Proves the compiler + organization cycle is viable
- Relevant to any multi-agent knowledge-base project

## Related Sources

- [[karpathy-project-origin]] and [[karpathy-llm-wiki-gist]] — the foundational pattern
- [[shann-holmberg-post]] — simpler explanation
- [[ai-agents-cheat-sheet]] — attached concept reference

## See Also

- [[multi-agent-orchestration]] for detailed concept
- [[llm-wiki-pattern]] for the base pattern
- [[ai-agents-cheat-sheet]] for agent architecture reference
