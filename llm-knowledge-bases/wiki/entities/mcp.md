---
title: MCP (Model Context Protocol)
type: entity
created: 2026-04-11
updated: 2026-04-11
tags: [protocol, agentic, tooling, infrastructure, anthropic]
sources: [ai-agents-cheat-sheet, jumperz-multi-agent-post, dr-cintas-everything-claude-code, akshay-pachaar-claude-folder, nate-claude-cowork-guide]
related: [multi-agent-orchestration, claude-code-ecosystem, voxira]
---

## Summary

MCP (Model Context Protocol) is a standardized protocol for connecting AI agents to external tools, data sources, and services. It defines a common interface for agent-tool communication, enabling agents to discover and invoke capabilities without custom integrations. Developed by Anthropic and adopted across the Claude ecosystem.

## Key Details

MCP sits alongside A2A (Agent-to-Agent) as one of two key agentic protocols referenced in [[ai-agents-cheat-sheet]]:
- **MCP** handles agent ↔ tool communication (vertical integration)
- **A2A** handles agent ↔ agent communication (horizontal coordination)

## Where It Appears

MCP surfaces repeatedly across wiki sources as background infrastructure:

- **[[multi-agent-orchestration]]** — Listed as one of two agentic protocols alongside A2A; enables standardized tool access for multi-agent systems
- **[[claude-code-ecosystem]]** — The `.claude/` folder structure uses MCP servers for tool integration; [[akshay-pachaar-claude-folder]] documents MCP configuration in project settings
- **[[nate-claude-cowork-guide]]** — Claude Cowork uses MCP connectors to integrate with external services (Slack, GitHub, etc.)
- **[[dr-cintas-everything-claude-code]]** — The 27-agent production system relies on MCP for tool access across agents
- **[[voxira]]** — While Voxira uses its own agent framework on [[livekit]], MCP represents the standardized approach to the same problem of agent-tool connectivity

## Relevance

MCP is background infrastructure that becomes important if projects scale to multi-agent architectures. For the wiki project itself, MCP is the mechanism through which Claude Cowork sessions access the filesystem, scheduled tasks, and external services. As [[jumperz-multi-agent-post]] describes scaling to 10+ agents, standardized tool access via MCP becomes essential to avoid custom integration per agent.

## See Also

- [[multi-agent-orchestration]] for the broader agent coordination context
- [[claude-code-ecosystem]] for MCP usage within Claude Code projects
- [[ai-agents-cheat-sheet]] for visual reference of MCP vs A2A
