# Wiki Index

*Last updated: 2026-04-18*

This index catalogs every page in the wiki. Read this first to find relevant pages before drilling into specifics.

## Entities
*People, companies, products, and teams.*

- [[andrej-karpathy]] — AI researcher who originated the [[llm-wiki-pattern]]; token spend shifting to knowledge management. (4 sources)
- [[google-langextract]] — Open-source tool for extracting structured information from text with source grounding. (2 sources)
- [[breferrari-obsidian-mind]] — Production Obsidian vault template for Claude Code memory and multi-agent coordination. (2 sources)
- [[deepgram]] — AI speech platform: STT (Nova-3), TTS (Aura-2), text intelligence, and voice agent APIs. Primary STT provider for [[voxira]]. (1 source)
- [[livekit]] — Open-source WebRTC platform for voice, video, and AI agents. Real-time communication backbone for [[voxira]]. (1 source)
- [[mcp]] — Model Context Protocol; standardized agent ↔ tool interface developed by Anthropic. Referenced across 5+ sources. (5 sources)

## Projects
*Projects, initiatives, and workstreams.*

- [[voxira]] — Healthcare-focused conversational voice agent platform on [[livekit]]. Multi-agent system for patient identification, scheduling, consent. Uses [[deepgram]] STT, OpenAI LLM, multi-tenant clinic config. (2 sources)

## Concepts
*Ideas, frameworks, and methodologies.*

### LLM Knowledge Management
- [[schema-driven-governance]] — Schema files (CLAUDE.md, .claude/) as the actual coordination mechanism in LLM systems, not just documentation. (4 sources)
- [[idea-files-prompt-as-code]] — Prompts, schemas, and wiki structures as a codebase for ideas; maintaining them is the primary engineering work. (3 sources)
- [[llm-wiki-pattern]] — Persistent, LLM-maintained markdown wiki replacing query-time RAG; three layers (raw, wiki, schema) and workflows (ingest, query, lint). (5 sources)
- [[vectorless-retrieval]] — Alternative to embeddings: BM25, SQL, knowledge graphs, direct context injection for knowledge retrieval. (2 sources)

### Multi-Agent Systems
- [[multi-agent-orchestration]] — Design and coordination of multiple AI agents; patterns (CoT, ToT, ReAct), protocols (MCP, A2A). (5 sources)
- [[voice-agent-performance-optimization]] — Reducing latency in voice agents: silence detection tuning, prompt caching, concurrent preprocessing. (20+ sessions)
- [[langfuse-trace-analysis]] — Debugging voice agent conversations using Langfuse JSON traces: latency analysis, loop detection, routing verification. (20+ sessions)

### Application Domains
- [[healthcare-voice-agent-patterns]] — Design patterns for conversational voice agents in healthcare: HIPAA consent, patient ID, scheduling, multi-tenant config. (80+ sessions)
- [[quebec-french-stt-optimization]] — STT challenges for Quebec French: fuzzy name matching, keyword boosting, spelling fallback, language switching. (80+ sessions)

### Tools & Infrastructure
- [[obsidian-integration]] — Using Obsidian as the frontend IDE for LLM-maintained markdown knowledge bases. (3 sources)
- [[claude-code-ecosystem]] — Conventions for Claude Code projects: .claude/ folder, commands, agents, skills, hooks, memory integration. (6 sources)
- [[structured-information-extraction]] — Converting unstructured text to structured data with source grounding; enables traceable knowledge bases. (2 sources)

## Session Mining
*Synthesized knowledge from recorded development sessions.*

- [[sessions-overview]] — Index of 80 Claude Code development sessions (2026-03-12 to 2026-04-11) for [[voxira]] voice agent platform. Synthesized into 4 major concept pages by topic.

---

## Sources
*Summary pages for each ingested source document.*

### Social Posts (X)

- [[karpathy-project-origin]] — Original framing of [[llm-wiki-pattern]]; viral tweet, project blueprint. (Karpathy)
- [[shann-holmberg-post]] — Commentary on Karpathy's workflow: collect sources, point Claude at folder, knowledge management token shift. (Shann Holmberg)
- [[code-rams-post]] — Explanation of "idea files" concept; treats schema/operational documents as first-class artifacts. (code_rams)
- [[dkare1009-vectorless-rag-post]] — Vectorless RAG paradigm: BM25, SQL, knowledge graphs instead of vectors. (dkare1009)
- [[jumperz-multi-agent-post]] — Extends [[llm-wiki-pattern]] to 10-agent swarm; agents dump to raw/, compiler organizes to wiki. (jumperz)
- [[dr-cintas-claude-code-setup]] — Production system: 27 agents, 64 skills, 33 commands; Anthropic hackathon winner. (dr_cintas)
- [[explorax-20-agentic-skills]] — 20 powerful reusable agentic skills across Claude, ChatGPT, Gemini; full taxonomy with markdown templates. (explorax_)
- [[zodchiii-claude-hooks]] — 8 Claude Code hooks for automating forgotten maintenance tasks; PreToolUse/PostToolUse patterns. (zodchiii)
- [[akshay-pachaar-claude-folder]] — Complete anatomy of .claude/ folder: CLAUDE.md, commands, agents, skills, hooks, permissions, memory. (akshay_pachaar)
- [[tom-doerr-obsidian-vault]] — Pointer to [[breferrari-obsidian-mind]] for Obsidian + Claude Code memory. (tom_doerr)
- [[chenglou-pretext]] — Framework for creating AI-assisted demos and presentations. (chenglou)
- [[mdancho84-langextract]] — Discovery announcement of Google's [[google-langextract]]; "better than $100K enterprise tools". (mdancho84)
- [[nate-claude-cowork-guide]] — Comprehensive guide to Claude Cowork: delegation model, setup, skills, connectors, plugins, real workflows. (nate_google_)
- [[ruben-hassid-claude-comparison]] — Guidance on choosing right Claude tool (Chat, Code, Cowork, Projects) for the task. (rubenhassid)
- [[prince-canuma-mlx-vlm]] — MLX-VLM v0.4.3 release with multimodal vision/OCR/detection capabilities. (prince_canuma)
- [[ernesto-software-vibe-coding]] — Pointer to important prompting pattern for "vibe coding" (LLM-assisted development). (ernestosoftware)
- [[sharbel-claude-features-guide]] — 20 Claude features ranked by impact; why most users only leverage 10% of what they're paying for. (sharbel)

### Repositories

- [[karpathy-llm-wiki-gist]] — Foundational concept document for [[llm-wiki-pattern]]; architecture, workflows, principles. (Karpathy)
- [[breferrari-obsidian-mind-repo]] — Production template: Home.md, CLAUDE.md, lifecycle hooks, subagents, semantic search. (breferrari)
- [[chenglou-pretext-repo]] — Demo/presentation framework for AI-generated content. (chenglou)
- [[google-langextract-repo]] — Official Google extraction library with source grounding and interactive visualization. (google)

### Inbox

- [[dr-cintas-everything-claude-code]] — Full thread: 27 agents, 64 skills, 33 commands; repo `affaan-m/everything-claude-code`; includes failure-mode debate. (dr_cintas, 2026-03-30)

### SDK & Platform Documentation

- [[deepgram-python-sdk]] — Official Python SDK docs + v5→v6 migration guide. Covers Listen, Speak, Read, Agent APIs and custom transports. (Deepgram, Web Clipper)
- [[livekit-docs]] — Full LiveKit platform documentation. Server, agents framework, client SDKs, telephony, egress. (LiveKit, Web Clipper, 2.5MB)

### Project Documentation

- [[voxira-architecture]] — Voxira platform architecture: 7-layer system design, agent framework, services, runtime, deployment, data flows. (7 files, docs_full/)
- [[voxira-docs]] — Voxira operational docs: deployment, cost calculation, usage tracking, fuzzy name matching, Quebec French optimization. (9 files, docs/)

### Developer Workflows & Tooling

- [[boris-cherny-slash-commands]] — 10 custom Claude Code commands (env-check, orient, preflight, dissect, testmatch, explain-func, refactor-safe, ship, migrate-draft, debt-scan). "Learn then generate" and "guard then execute" patterns. (Web Clipper, 39KB)
- [[anthropic-opus-4-7-best-practices]] — Anthropic guidance for Opus 4.7 in Claude Code: front-load tasks, minimize user turns, default to xhigh, and explicitly request tool use or subagent fan-out when needed. (Anthropic blog)
- [[ernesto-software-vibe-coding]] — High-signal prompt for "vibe coding" (LLM-assisted development); foundational pattern for collaborative coding with Claude. (X post)
- [[ruben-hassid-claude-comparison]] — Tool selection guide: when to use Chat, Code, Cowork, or Projects; most people default to Chat for everything. (X post)

### Agent Architecture

- [[agent-harness-memory-ownership]] — "Your harness, your memory." Argues agent harnesses are inseparable from memory; closed harnesses = lost memory ownership. Validates the [[llm-wiki-pattern]] approach. (Blog post, Web Clipper)

### Plugins & Behavioral Guidelines

- [[karpathy-skills-plugin]] — Claude Code plugin packaging [[andrej-karpathy]]'s LLM coding observations into 4 principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution). Dual install: marketplace plugin or standalone CLAUDE.md. (forrestchang, GitHub repo)

### Multimodal & Vision

- [[prince-canuma-mlx-vlm]] — MLX-VLM v0.4.3 release with multimodal vision/OCR/detection capabilities (Gemma 4, Falcon-OCR, Granite Vision 4.0, SAM 3.1, RF-DETR). (X post)

### Visual References

- [[ai-agents-cheat-sheet]] — Comprehensive reference for agent concepts, patterns (CoT/ToT/ReAct), protocols (MCP/A2A). (Shared)
- [[llm-wiki-architecture-screenshot]] — Diagram of three-layer architecture and three workflows; matches this project's structure. (Captured)

## Analyses
*Comparisons, deep-dives, and filed query results.*

- [Lint Report — 2026-04-12](analyses/lint-2026-04-12.md) — 2026-04-12. Daily lint: self-referential links, stale overview, cross-reference gaps, redirect cleanup candidates.
- [Lint Report — 2026-04-11](analyses/lint-2026-04-11.md) — 2026-04-11. Wiki health-check: broken links, orphans, stale content, missing pages.

## Meetings
*Meeting summaries and action items.*

_(No meetings yet.)_
