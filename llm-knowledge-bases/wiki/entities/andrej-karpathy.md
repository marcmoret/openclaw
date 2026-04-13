---
title: Andrej Karpathy
type: entity
created: 2026-04-10
updated: 2026-04-12
tags: [people, ai-researchers, karpathy]
sources: [karpathy-project-origin, shann-holmberg-post, karpathy-llm-wiki-gist, code-rams-post, karpathy-skills-plugin]
related: [llm-wiki-pattern, karpathy-llm-wiki-gist]
---

## Summary

Andrej Karpathy is an AI researcher and educator who originated the [[llm-wiki-pattern]] concept. He frames building personal AI knowledge bases as a shift from query-time RAG to persistent, LLM-maintained markdown wikis.

## Key Contributions

### LLM Wiki Pattern (Original Framing)
- **Post** ([2039805659525644595](https://x.com/karpathy/status/2039805659525644595)) — original project framing and rationale
- **Gist** ([[karpathy-llm-wiki-gist]]) — foundational concept document describing the three-layer architecture (raw sources, wiki, schema), three workflows (ingest, query, lint), and the division of labor between human and LLM

### Concept: "Idea Files"
code-rams reported on a follow-up post where Karpathy emphasizes:
- Instead of sharing code, share "idea files"
- Text descriptions of what you want to build
- Schema files and operational instruction files are first-class assets
- Reinforces the importance of documents like CLAUDE.md

### Knowledge Management Workflow
shann-holmberg summarized Karpathy's knowledge-base workflow:
- Most of his token spend is shifting from code to knowledge management
- Dumps everything into one folder (articles, papers, repos, datasets, images)
- Points Claude at the folder to compile and organize
- Pure file-based organization, no vector DBs

### Claude Code Guidelines Plugin
forrestchang packaged Karpathy's LLM coding observations into a distributable Claude Code plugin ([[karpathy-skills-plugin]]). Distills the pitfalls into four enforceable principles: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. Available via Claude Code marketplace or as a standalone `CLAUDE.md`.

## Impact

- Originated the [[llm-wiki-pattern]] which is now foundational to this wiki project
- Demonstrated that markdown wikis can replace vector-database-heavy RAG at moderate scale
- Showed that operational instruction files (like CLAUDE.md) are critical infrastructure
- Inspired jumperz to extend the pattern to multi-agent architectures
- Influenced dozens of knowledge-base and LLM-agent projects

## Mentions in Sources

- [[karpathy-project-origin]] — direct social source
- [[shann-holmberg-post]] — commentary on his knowledge-base workflow
- [[code-rams-post]] — explanation of his "idea files" concept
- [[jumperz-multi-agent-post]] — "took karpathy's wiki pattern and wired it into my 10 agent swarm"
- [[karpathy-llm-wiki-gist]] — foundational concept gist
- [[karpathy-skills-plugin]] — Claude Code plugin packaging his coding guidelines into 4 principles (by forrestchang)

## See Also

- [[llm-wiki-pattern]] for detailed concept
- [[karpathy-llm-wiki-gist]] for the full writeup
- [[jumperz-multi-agent-post]] for extensions
