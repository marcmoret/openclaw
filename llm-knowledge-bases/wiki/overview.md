---
title: Overview
type: analysis
created: 2026-04-10
updated: 2026-04-12
tags: [overview, meta]
sources: []
---

# Knowledge Base Overview

This is Marco's business and work knowledge base — a persistent, compounding wiki maintained by Claude following the [[llm-wiki-pattern]].

## Current State

The wiki was initialized on 2026-04-10 and has grown to 60 pages. As of 2026-04-12 it contains:

- **12 concept pages**: [[llm-wiki-pattern]], [[vectorless-retrieval]], [[multi-agent-orchestration]], [[obsidian-integration]], [[claude-code-ecosystem]], [[structured-information-extraction]], [[schema-driven-governance]], [[idea-files-prompt-as-code]], [[voice-agent-performance-optimization]], [[langfuse-trace-analysis]], [[healthcare-voice-agent-patterns]], [[quebec-french-stt-optimization]]
- **6 entity pages**: [[andrej-karpathy]], [[google-langextract]], [[breferrari-obsidian-mind]], [[deepgram]], [[livekit]], [[mcp]]
- **1 project page**: [[voxira]] (healthcare voice agent platform)
- **34 source summaries** spanning X/social posts, GitHub repositories, SDK docs, project architecture docs, blog posts, and visual references
- **1 session index** with 80+ synthesized development sessions
- **1 analysis** (lint reports)

## Key Themes

1. **[[llm-wiki-pattern]]** — The foundational architecture for this wiki. Persistent, LLM-maintained markdown replacing query-time RAG. Originated by [[andrej-karpathy]].
2. **[[multi-agent-orchestration]]** — Scaling AI agent systems from single-agent to 10–27 agent swarms. Production examples: jumperz (10 agents), dr_cintas (27 agents), [[voxira]] (15+ agents).
3. **[[claude-code-ecosystem]]** — Tools, conventions, and automation for Claude Code: .claude/ folder, commands, agents, skills, hooks, memory. [[boris-cherny-slash-commands|Exemplar patterns]] for commands and [[zodchiii-claude-hooks|lifecycle automation]].
4. **[[vectorless-retrieval]]** — Paradigm shift away from embeddings toward BM25, SQL, knowledge graphs, and direct context injection.
5. **[[schema-driven-governance]]** and **[[idea-files-prompt-as-code]]** — Operational documents and prompts as executable code; CLAUDE.md and .claude/ as the control plane.
6. **[[voxira]]** — Marco's healthcare voice agent project on [[livekit]] + [[deepgram]]. First-party project with full architecture, operational docs, and 80+ development sessions synthesized into concept pages.
7. **Voice agent optimization** — Domain-specific patterns from [[voxira]] development: [[voice-agent-performance-optimization]], [[healthcare-voice-agent-patterns]], [[quebec-french-stt-optimization]], [[langfuse-trace-analysis]].

## Scope

This knowledge base covers business and work topics including:
- AI agent architectures and orchestration patterns
- LLM tooling and development workflows
- Voice AI and healthcare technology ([[voxira]])
- Knowledge management patterns and tools
- Strategic analyses and competitive intelligence

## How to Use

**To add knowledge:** Drop source files (articles, meeting notes, transcripts, reports, PDFs) into the `raw/` folder, then ask Claude to ingest them.

**To query:** Ask Claude any question. It will consult the wiki's index, read relevant pages, and synthesize an answer with citations.

**To maintain:** Periodically ask Claude to lint the wiki — it will find contradictions, orphan pages, missing links, and suggest improvements.

## Open Questions

- Should the wiki create entity pages for all X/social authors, or only high-signal contributors?
- When should superseded source stubs be archived vs. kept as redirects? (4 redirect stubs pending deletion — see lint report 2026-04-12)
- How should Voxira operational metrics (costs, call volumes) be tracked in the wiki?
- Are [[chenglou-pretext]] and [[prince-canuma-mlx-vlm]] still relevant, or should they be archived?
