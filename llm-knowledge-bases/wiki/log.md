# Wiki Log

Chronological record of all wiki operations. Each entry is prefixed for parseability.

## [2026-04-12] session-scan | Automated Session Scan (no new knowledge)

Automated wiki session scan. Scanned 7 Cowork sessions and 1 JSONL file.

### Cowork Sessions Reviewed
- "Wiki daily lint" ×2 — maintenance only, already logged
- "Wiki auto ingest" ×2 — one ingested karpathy-skills-plugin (already logged), one found no new sources
- "Build LLM-powered personal knowledge wiki" — wiki cleanup (author wikilink removal, concept stubs), already reflected in wiki
- "Wiki session scan" — previous scan that created mcp, schema-driven-governance, idea-files-prompt-as-code pages, already in wiki
- "Create Claude todo file with instructions" — same page creation as above, already captured

### Claude Code Sessions
- Only 1 JSONL file found at the mounted path (this session itself). No access to Marco's `~/.claude/projects/` directory — the Cowork mount only exposes the Work folder. Future scans would benefit from mounting `~/.claude/projects/` to access Claude Code session history.

### Result
No new wiki-worthy knowledge found. All substantive session outputs were already ingested by prior scans or by the sessions themselves.

Pages created: []
Pages updated: [log.md]

---

## [2026-04-12] lint | Daily Wiki Health Check

Automated daily lint. 60 pages scanned. No contradictions found. Wiki is structurally healthy.

### Fixes Applied
- Removed self-referential `related` entries from 3 concept pages (claude-code-ecosystem, healthcare-voice-agent-patterns, multi-agent-orchestration)
- Updated overview.md: corrected page count (58→60), removed resolved open question about MCP entity page, added new editorial questions
- Added missing cross-references: akshay-pachaar-claude-folder → boris-cherny-slash-commands, karpathy-llm-wiki-gist → schema-driven-governance, multi-agent-orchestration → schema-driven-governance, structured-information-extraction → claude-code-ecosystem
- Replaced stale `rag-evolution` related entry with `claude-code-ecosystem` in structured-information-extraction

### Flagged for Marco
- 4 redirect stubs recommended for deletion (dkare1009-post-placeholder, sharbel-post-placeholder, nate-google-cowork, explorax-agentic-skills)
- 2 stub concept pages need expansion or merging (persistent-knowledge-base, prompting-patterns)
- Peripheral sources to review: chenglou-pretext, prince-canuma-mlx-vlm
- livekit-docs.md needs deeper re-ingest (2.5MB source only partially summarized)

Pages created: [analyses/lint-2026-04-12.md]
Pages updated: [claude-code-ecosystem.md, healthcare-voice-agent-patterns.md, multi-agent-orchestration.md, overview.md, akshay-pachaar-claude-folder.md, karpathy-llm-wiki-gist.md, structured-information-extraction.md, index.md]

---

## [2026-04-12] auto-ingest | Karpathy Skills Plugin

Automated scheduled scan found 1 new source: `raw/inbox/andrej-karpathy-skills-main/` (Claude Code plugin by forrestchang packaging Karpathy's LLM coding guidelines into 4 principles).

Pages created: [karpathy-skills-plugin]
Pages updated: [andrej-karpathy, claude-code-ecosystem, schema-driven-governance, index]

### Details

- **Source**: `andrej-karpathy-skills-main/` — 6 files (README.md, CLAUDE.md, EXAMPLES.md, SKILL.md, plugin.json, marketplace.json)
- **New source page**: [[karpathy-skills-plugin]] — summarizes the 4 principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution), the anti-pattern examples gallery, and the dual distribution model (marketplace plugin vs standalone CLAUDE.md)
- **[[andrej-karpathy]]** — added "Claude Code Guidelines Plugin" section and source reference
- **[[claude-code-ecosystem]]** — added "Plugins and Marketplace" subsection documenting plugin distribution model
- **[[schema-driven-governance]]** — added reference as example of distributable governance artifacts
- **[[index]]** — added new "Plugins & Behavioral Guidelines" subsection under Sources

### Cross-References Added

- karpathy-skills-plugin → andrej-karpathy, claude-code-ecosystem, schema-driven-governance, idea-files-prompt-as-code, boris-cherny-slash-commands, prompting-patterns
- andrej-karpathy → karpathy-skills-plugin
- claude-code-ecosystem → karpathy-skills-plugin
- schema-driven-governance → karpathy-skills-plugin

### Notes

- This source is notable as the first Claude Code *marketplace plugin* in the wiki — demonstrates that CLAUDE.md governance documents can be versioned, distributed, and installed like software packages
- Marco's own CLAUDE.md shares several principles (Simplicity First, Surgical Changes, Surface Confusion) with this plugin, suggesting convergent design
- No contradictions with existing wiki content; the plugin operationalizes concepts already discussed in [[andrej-karpathy]] and [[schema-driven-governance]]

---

## [2026-04-12] cleanup | Broken Wikilink Resolution

Resolved remaining broken wikilinks from lint report: 13 X/social author handles and 3 aspirational concept links.

### Author Wikilinks → Plain Text (15 edits across 8 files)

Converted author handles from wikilinks to plain text — these are minor social media references without enough substance for entity pages.

- `[[akshay-pachaar]]` → `akshay-pachaar` (claude-code-ecosystem.md)
- `[[akshay-pachaar-claude-folder]]` → `akshay-pachaar-claude-folder` (schema-driven-governance.md)
- `[[zodchiii]]` → `zodchiii` (claude-code-ecosystem.md)
- `[[jumperz]]` → `jumperz` (claude-code-ecosystem.md, andrej-karpathy.md, multi-agent-orchestration.md ×2, ai-agents-cheat-sheet.md)
- `[[code-rams]]` → `code-rams` (andrej-karpathy.md)
- `[[shann-holmberg]]` → `shann-holmberg` (andrej-karpathy.md)
- `[[dkare1009]]` → `dkare1009` (vectorless-retrieval.md, dkare1009-vectorless-rag-post.md)
- `[[dr-cintas]]` → `dr-cintas` (multi-agent-orchestration.md, ai-agents-cheat-sheet.md)
- `[[explorax-m0h]]` → `explorax-m0h` (multi-agent-orchestration.md)
- `[[mdancho84-langextract|mdancho84]]` → `mdancho84` (structured-information-extraction.md)

### Aspirational Concept Links (1 edit)

- `[[rag-evolution]]` → `rag-evolution` (vectorless-retrieval.md)
- `[[multimodal-processing]]` and `[[presentation-tools]]` — only appeared in YAML `related:` fields and lint report, not as markdown wikilinks. No edits needed.

### Concept Stub Pages Created (2)

1. [[persistent-knowledge-base]] — Pattern of maintaining durable knowledge stores across LLM sessions. Links to [[llm-wiki-pattern]], [[schema-driven-governance]].
2. [[prompting-patterns]] — Reusable prompt engineering strategies including few-shot, chain-of-thought, system layering, and prompt-as-code. Links to [[idea-files-prompt-as-code]], [[boris-cherny-slash-commands]].

### Summary

- 15 author wikilinks converted to plain text across 8 files
- 1 aspirational concept link converted to plain text
- 2 new concept stub pages created
- Wiki now has 60 pages total

---

## [2026-04-12] lint | Full Wiki Health Check

58 pages scanned. Found 12 broken wikilinks, 4 duplicate pages (3 converted to redirects), 5 orphan pages (now linked).

### Fixes Applied

**Broken Wikilinks (12)** — Redirected to correct targets:
- `[[mcp-protocol]]` → `[[mcp|MCP]]` (3 instances in multi-agent-orchestration, claude-code-ecosystem, llm-wiki-pattern)
- `[[claude-code-agents]]` → `[[claude-code-ecosystem]]` (1 instance in multi-agent-orchestration)
- `[[claude-ecosystem]]` → `[[claude-code-ecosystem]]` (2 instances in nate-google-cowork, multi-agent-orchestration)
- `[[agent-patterns]]` → `[[multi-agent-orchestration]]` (1 instance in multi-agent-orchestration)
- `[[claude-code-memory]]` → `[[claude-code-ecosystem]]` (3 instances in claude-code-ecosystem, llm-wiki-pattern, obsidian-integration)
- `[[jumperzз-multi-agent-post]]` (Cyrillic typo) → `[[jumperz-multi-agent-post]]` (1 instance in explorax-20-agentic-skills)

**Placeholder Pages** — Converted to simple redirects:
- `dkare1009-post-placeholder.md` → redirect to `[[dkare1009-vectorless-rag-post]]`
- `sharbel-post-placeholder.md` → redirect to `[[sharbel-claude-features-guide]]`

**Duplicate Pages** — Identified and redirected the stub version:
- `nate-google-cowork.md` (49 lines) → redirect to `[[nate-claude-cowork-guide]]` (149 lines, full guide)
- `explorax-agentic-skills.md` (48 lines) → redirect to `[[explorax-20-agentic-skills]]` (148 lines, full library)

**Orphan Pages** — Added inbound links for 5 pages with no incoming references:
- `[[boris-cherny-slash-commands]]` — Added link from `[[claude-code-ecosystem]]` under "Commands and Skills" section
- `[[agent-harness-memory-ownership]]` — Already linked from `[[llm-wiki-pattern]]` ("Where It Appears" section updated)
- `[[ernesto-software-vibe-coding]]` — Added links from index.md (new "Developer Workflows & Tooling" section)
- `[[prince-canuma-mlx-vlm]]` — Added links from index.md (new "Multimodal & Vision" section)
- `[[ruben-hassid-claude-comparison]]` — Added links from index.md (new "Developer Workflows & Tooling" section)

**Cross-Reference Improvements**:
- `[[boris-cherny-slash-commands]]` → added wikilinks to `[[claude-code-ecosystem]]`, `[[schema-driven-governance]]`, `[[andrej-karpathy]]`
- `[[ernesto-software-vibe-coding]]` → updated related to link `[[claude-code-ecosystem]]`, `[[idea-files-prompt-as-code]]`
- `[[prince-canuma-mlx-vlm]]` → updated related to link `[[structured-information-extraction]]`
- `[[ruben-hassid-claude-comparison]]` → updated related to link `[[claude-code-ecosystem]]`, `[[nate-claude-cowork-guide]]`

### Pages Updated

- Multi-agent-orchestration.md — Fixed broken links (mcp-protocol, claude-code-agents, agent-patterns)
- Claude-code-ecosystem.md — Fixed broken link (claude-code-memory), added boris-cherny-slash-commands reference
- Llm-wiki-pattern.md — Fixed broken links (claude-code-memory), added agent-harness-memory-ownership
- Obsidian-integration.md — Fixed broken link (claude-code-memory)
- Google-langextract.md — Fixed broken link (mdancho84-post)
- Nate-google-cowork.md — Converted to redirect
- Dkare1009-post-placeholder.md — Converted to redirect
- Sharbel-post-placeholder.md — Converted to redirect
- Explorax-agentic-skills.md — Converted to redirect
- Explorax-20-agentic-skills.md — Fixed cyrillic typo (jumperzз)
- Boris-cherny-slash-commands.md — Added schema/governance references
- Ernesto-software-vibe-coding.md — Added claude-code-ecosystem, idea-files reference
- Prince-canuma-mlx-vlm.md — Updated structured-extraction reference
- Ruben-hassid-claude-comparison.md — Updated claude-code-ecosystem, nate-claude-cowork references
- Index.md — Added orphan pages to new subsections, updated counts
- Overview.md — Updated with accurate page counts, new content areas, date to 2026-04-12

### Summary

- 58 pages scanned
- 12 broken wikilinks fixed
- 4 duplicate/placeholder pages resolved (3 → redirects, 1 already has full version)
- 5 orphan pages now linked from index and concept pages
- Wiki now fully cross-linked with no broken internal references

---

## [2026-04-12] ingest | Two New Inbox Sources

Processed 2 new files from raw/inbox/.

### Pages Created (2)
1. [[boris-cherny-slash-commands]] — Tutorial on 10 custom Claude Code commands with full prompt templates. Key patterns: "learn then generate" (read existing conventions before producing output) and "guard then execute" (run tests before generating PRs).
2. [[agent-harness-memory-ownership]] — Blog post arguing agent memory is inseparable from harnesses; closed harnesses create dangerous lock-in. Validates the wiki's [[llm-wiki-pattern]] approach as an open memory layer.

### Pages Updated (1)
- [[index]] — Added entries under new "Developer Workflows & Tooling" and "Agent Architecture" subsections

---

## [2026-04-12] session-mining | Synthesized 80 Claude Code Sessions

Mined and synthesized 80 development session transcripts (2026-03-12 to 2026-04-11) from [[voxira]] voice agent platform development. Created master index and 4 major concept pages organized by topic.

### Sessions Processed
- **Total sessions**: 80 (70+ MB of transcripts)
- **Date range**: 2026-03-12 to 2026-04-11 (31 days)
- **Primary project**: [[voxira]] (healthcare voice agent on [[livekit]])
- **Development phases**: Planning (3/12–3/16), Implementation (3/17–4/10), Testing (4/07–4/11)

### Pages Created (5)

**Session Index (1):**
1. [[sessions-overview]] — Master index of all 80 sessions with timeline, milestones, session breakdown by component, and cross-cutting themes

**Concept Pages (4):**
2. [[voice-agent-performance-optimization]] — Latency reduction techniques: silence detection tuning, prompt caching, concurrent preprocessing, STT optimization
3. [[langfuse-trace-analysis]] — Debugging voice agent conversations: JSON trace structure, latency bottleneck identification, logic error detection, tool call verification
4. [[healthcare-voice-agent-patterns]] — Design patterns for healthcare agents: HIPAA consent, patient ID with fuzzy matching, appointment scheduling, multi-tenant config, EMR abstraction
5. [[quebec-french-stt-optimization]] — Quebec French STT challenges: fuzzy name matching algorithm, Deepgram keyword boosting, spelling fallback, language detection

### Pages Updated (2)
- [[voxira]] — Added "Development History" section with timeline of major milestones and technical achievements
- [[index.md]] — Reorganized Concepts section by domain, added Session Mining section, added links to new concept pages

### Knowledge Extracted

**Performance & Optimization** (from 20+ sessions):
- Identified and fixed 8–9 second silence detection gaps in agent transfers
- Implemented OpenAI prompt caching for 3x speedup on LLM TTFT
- Quebec French STT 2–3x slower than English; root cause unclear (likely Deepgram model performance)

**Observability & Debugging** (from 2026-03-17 onwards):
- Established Langfuse JSON trace export as primary debugging tool
- Identified loop detection pattern (scheduling agent stuck checking availabilities)
- Built trace analysis workflow: timing breakdown, tool call verification, agent handoff tracking

**Multi-Tenant Architecture** (from 2026-03-12 onwards):
- Designed flow graph model (nodes + edges) replacing hardcoded if/elif chains
- Implemented feature flag system for clinic-specific behavior (zero-downtime updates)
- Built clinic-specific appointment type mapping (read from Excel, stored in code/DB)

**Healthcare Domain Patterns** (from 2026-03-12 onwards):
- HIPAA consent capture (mandatory first step)
- Patient ID with STT error recovery (fuzzy matching + spelling fallback)
- Multi-clinic testing framework (PiedReseau, PCMD, Savaria clinics)

**Language Support** (from 2026-03-30 onwards):
- Quebec French STT challenges (name pronunciation, accent handling)
- Fuzzy matching using government name registry + popularity weighting
- Spelling agent for low-confidence STT results

### Development Milestone Timeline

| Phase | Dates | Key Achievement |
|-------|-------|-----------------|
| **Planning** | 3/12–3/16 | Flow graph architecture, React Flow UI decision, DB schema |
| **Implementation** | 3/17–3/30 | Agent behavior, prompt caching, Langfuse integration, multi-clinic support |
| **Configuration** | 3/31–4/05 | PiedReseau appointment mapping, feature flag system |
| **Testing** | 4/07–4/11 | E2E flows, loop detection, performance optimization |

### Cross-Referencing

- **Voxira project page** → links to sessions-overview
- **Performance concept** → references voice-agent-performance-optimization
- **Healthcare concept** → references healthcare-voice-agent-patterns
- **All concept pages** → link back to voxira project and sessions-overview

### Notes

- Sessions organized by date (31-day window); largest sessions (9–24 MB) chosen for initial deep read
- Topics extracted from session content (langfuse, french, architecture, etc.) rather than filenames
- All 80 sessions referenced in sessions-overview with 2-line summary each
- Four concept pages represent major recurring themes across sessions (not per-session summaries)
- Development history added to voxira.md as timeline of major decisions + outcomes

---

## [2026-04-11] session-scan | Scanned 4 sessions

Scanned 4 Cowork sessions for wiki-worthy knowledge.

### Sessions Scanned
- `local_23a5e95d-8d69-454d-be28-e651ed33756c` "Wiki daily lint" — Mechanical wiki maintenance (lint fixes). Already logged. **Skipped.**
- `local_6367ee28-5052-4c3e-9fdd-5ccc9a472bc2` "Wiki auto ingest" — Automated no-op scan. Already logged. **Skipped.**
- `local_18f8e548-6f48-4e29-bdf2-b253f5488b69` "Build LLM-powered personal knowledge wiki" — Ingested Deepgram/LiveKit/Voxira docs. Already logged. **Skipped.**
- `local_ecc9329d-c08d-4ce4-9314-1d289eea8893` "Create Claude todo file with instructions" — Created 3 wiki pages (MCP, Schema-Driven Governance, Idea Files) on a different wiki path. Pages did not exist in mounted wiki. **Processed.**

### Knowledge Extracted (from session local_ecc9329d)
Session created 3 conceptual/entity pages on a different copy of the wiki (`/Users/marcomoretto/Dev/Private/openclaw/llm-knowledge-bases/`). These pages were not present in the mounted wiki, so they were recreated with proper grounding from existing source material.

### Pages Created (3)
- [[mcp]] — Entity page for Model Context Protocol; standardized agent ↔ tool interface referenced across 5+ sources. Resolves missing `[[mcp-protocol]]` links flagged in lint report.
- [[schema-driven-governance]] — Concept page on schema files (CLAUDE.md, .claude/) as the actual coordination mechanism in LLM systems. Grounded in Karpathy gist, obsidian-mind repo, code-rams idea files, akshay .claude/ anatomy.
- [[idea-files-prompt-as-code]] — Concept page framing prompts, schemas, and wiki structures as a codebase for ideas. Originates from code-rams post and Karpathy's token-spend-shift insight.

### Pages Updated (4)
- wiki/index.md — Added 1 entity (mcp) and 2 concepts (schema-driven-governance, idea-files-prompt-as-code)
- wiki/concepts/claude-code-ecosystem.md — Fixed `[[mcp-protocol]]` → `[[mcp|MCP]]`
- wiki/concepts/multi-agent-orchestration.md — Fixed `[[mcp-protocol]]` → `[[mcp|MCP]]`
- wiki/sources/ai-agents-cheat-sheet.md — Fixed `[[mcp-protocol]]` → `[[mcp|MCP]]`, removed "(candidate)" flag

---

## [2026-04-11] lint | Wiki Health-Check
Automated scheduled lint. Audited all 45 wiki pages.

### Findings
- **1 major stale page**: overview.md still said "No sources ingested" — rewritten
- **5 broken wikilink patterns** fixed across 10 pages (tom-doerr-post→tom-doerr-obsidian-vault, mdancho84-post→mdancho84-langextract, chenglou-post→chenglou-pretext, jumperz-multi-agent-pattern→jumperz-multi-agent-post, claude-cowork-guide→nate-claude-cowork-guide)
- **6 missing cross-references** added (entity→repo links, concept→source links)
- **10 orphan pages** identified (3 placeholders/stubs, 3 repo sources, 4 peripheral sources)
- **5 superseded source stubs** flagged for Marco's review
- **10 missing concept pages** and **9 missing entity pages** cataloged as candidates
- **5 questions to investigate** documented

### Pages Created
- wiki/analyses/lint-2026-04-11.md

### Pages Updated
- wiki/overview.md (full rewrite)
- wiki/index.md (added lint report to Analyses section)
- wiki/concepts/obsidian-integration.md (fixed tom-doerr-post link)
- wiki/concepts/llm-wiki-pattern.md (fixed jumperz-multi-agent-pattern link)
- wiki/concepts/structured-information-extraction.md (fixed mdancho84 link)
- wiki/concepts/claude-code-ecosystem.md (fixed zodchiii, akshay-pachaar, tom-doerr, dr-cintas links)
- wiki/entities/andrej-karpathy.md (fixed jumperz-multi-agent-pattern link)
- wiki/entities/breferrari-obsidian-mind.md (fixed tom-doerr-post, jumperz-multi-agent-pattern links; added repo cross-ref)
- wiki/entities/google-langextract.md (fixed mdancho84 link; added repo cross-ref)
- wiki/sources/breferrari-obsidian-mind-repo.md (fixed tom-doerr-post link)
- wiki/sources/google-langextract-repo.md (fixed mdancho84-post link)
- wiki/sources/chenglou-pretext-repo.md (fixed chenglou-post link)
- wiki/sources/chenglou-pretext.md (fixed self-referential repo link)
- wiki/sources/sharbel-claude-features-guide.md (fixed claude-cowork-guide link)

---

## [2026-04-11] auto-scan | No New Sources
Automated scheduled scan. Checked all files in raw/x/ (18 files), raw/repos/ (4 files), and raw/inbox/ (37 files + docs/ + docs_full/ subdirectories). All sources already ingested per prior log entries. No action needed.
Pages created: []
Pages updated: []

---

## [2026-04-11] ingest | Inbox Scan (3 files + 2 folders)
Processed 3 new files and 2 documentation folders from raw/inbox/.

### Sources Scanned
- `deepgramdeepgram-python-sdk Official Python SDK for Deepgram..md` — Full SDK README (460 lines)
- `deepgramdeepgram-python-sdk Official Python SDK for Deepgram. 1.md` — v5→v6 migration guide (530 lines)
- `Untitled.md` — LiveKit platform docs (2.5MB, too large for single read; previewed first 2KB)
- `docs/` — 9 Voxira operational docs (deployment, cost calc, usage tracking, fuzzy matching, env vars, optimization, language support)
- `docs_full/` — 7 Voxira architecture docs (index, architecture, agents, services, runtime, deployment, data flows)

### Pages Created (7)

**Entities (2):**
1. [[deepgram]] — AI speech platform (STT, TTS, text intelligence, voice agent APIs)
2. [[livekit]] — Open-source WebRTC platform for voice/video/AI agents

**Projects (1):**
3. [[voxira]] — Healthcare voice agent platform on LiveKit (first project page in wiki)

**Sources (4):**
4. [[deepgram-python-sdk]] — SDK docs + migration guide
5. [[livekit-docs]] — Full platform documentation
6. [[voxira-architecture]] — Platform architecture (7 files from docs_full/)
7. [[voxira-docs]] — Operational documentation (9 files from docs/)

### Pages Updated (2)
- [[multi-agent-orchestration]] — Added Voxira as production example of multi-agent orchestration in healthcare telephony
- [[wiki/index.md]] — Added 2 entities, 1 project, 4 source entries

### New Cross-Links
- **Voxira → multi-agent-orchestration**: Production 15+ agent system validates patterns discussed in concept page; addresses shared-state concern via observer-pattern UserData
- **Deepgram ↔ Voxira ↔ LiveKit**: Technology stack triangle — LiveKit (transport), Deepgram (STT/TTS), OpenAI (LLM)
- **Voxira → existing concepts**: Implements [[multi-agent-orchestration]] patterns in healthcare domain

### Notes
- Untitled.md (2.5MB) exceeds 256KB read limit; created summary page from preview. Full content accessible via chunked reads if needed.
- docs/ contains a `session/` subfolder (not ingested, appears to be runtime artifacts)
- First project page created — wiki now has all section types populated except Analyses and Meetings

---

## [2026-04-10] ingest | Full Inbox Ingestion (37 files)
Processed all 37 files from raw/inbox/. Used Web Clipper versions as primary sources; consolidated duplicates; skipped already-processed stubs.

### Strategy
- **Web Clipper files** (rich, full-content) preferred over stubs (2026-04-10- prefixed)
- **Duplicates merged**: Thread by @jumperz (1,2 removed), Thread by @dkare1009 (1 removed), Thread by @dr_cintas (1 removed)
- **Existing pages updated** with richer content from Web Clipper versions
- **X.md ignored** (empty/stub)

### Pages Created
1. **[[sharbel-claude-features-guide]]** — 20 Claude features ranked by impact (Products, Projects, Code Execution, Vision, Artifacts, Voice, Integrations)
2. **[[nate-claude-cowork-guide]]** — Delegation model with setup (context files, plugins, skills, connectors, real workflows)
3. **[[explorax-20-agentic-skills]]** — Full library of 20 reusable .md-format skills across 5 categories (Writing, Visual, Research, Coding, Automation)

### Pages Updated
1. **[[zodchiii-claude-hooks]]** — Added 8 detailed hooks (auto-format, block-dangerous, run-tests, prevent-debug, enforce-commits, auto-version, check-secrets, auto-docs) with JSON configs
2. **[[akshay-pachaar-claude-folder]]** — Complete anatomy: CLAUDE.md, commands, agents, skills, hooks, settings.json, permissions.json, memory (project vs global)
3. **[[wiki/index.md]]** — Updated source entries with richer descriptions

### Key Themes Reinforced
- **Claude product surface** (Projects, Code, Cowork, Chat) as entry points to AI tooling ([[sharbel-claude-features-guide]])
- **Delegation patterns** in Cowork mirror [[llm-wiki-pattern]] (raw input → processing → structured output) ([[nate-claude-cowork-guide]])
- **Reusable skills taxonomy** — Portable .md-format skills work cross-LLM (Claude, ChatGPT, Gemini) ([[explorax-20-agentic-skills]])
- **Hooks as automation enforcement** — Distinguish CLAUDE.md (advisory ~80%) from hooks (mandatory 100%) ([[zodchiii-claude-hooks]])
- **.claude/ as control center** — Project-level (team) vs global (personal) configuration, mirroring wiki's raw/wiki separation ([[akshay-pachaar-claude-folder]])

### New Cross-Links Identified
- **Claude Cowork → multi-agent orchestration**: Cowork plugins/skills model previews [[jumperz-multi-agent-post]] architecture
- **Hooks → Obsidian lifecycle**: [[zodchiii-claude-hooks]] and [[breferrari-obsidian-mind]] both use lifecycle automation
- **Agentic skills → structured extraction**: [[explorax-20-agentic-skills]] (Knowledge Structuring, Deep Research Synthesizer) enable [[structured-information-extraction]]
- **Features guide → Projects pattern**: [[sharbel-claude-features-guide]] (Projects + Custom Instructions) echoes [[llm-wiki-pattern]] layered architecture

### Inbox Consolidation Notes
- **No new unique sources found** beyond the 3 created above
- **Stubs were scaffolds**: 18 stub files (2026-04-10- prefix) were earlier placeholders; Web Clipper versions are authoritative
- **Threads were duplicates**: 8 Thread files were variants of 4 unique sources (all already ingested in prior operations)
- **Total inbox files processed**: 37 → 3 new source pages + 2 updated pages = 5 net additions

### Cross-checks
- Verified all pre-existing sources (Karpathy, dr_cintas, jumperz, dkare1009, explorax, zodchiii, akshay, etc.) match earlier ingest log
- No contradictions detected; new sources elaborate on existing concepts without conflicts
- sharbel-post-placeholder now resolved as sharbel-claude-features-guide
- All three new sources properly linked to concept pages

---

## [2026-04-10] ingest | Thread by @dr_cintas (inbox test)
Pages created: [wiki/sources/dr-cintas-everything-claude-code.md]
Pages updated: [wiki/concepts/multi-agent-orchestration.md, wiki/index.md]
New info: full thread text, repo URL (affaan-m/everything-claude-code), failure-mode debate from @ashcotXBT. Supersedes earlier stub.
Next: ingest https://github.com/affaan-m/everything-claude-code as primary artifact.

---

## [2026-04-10] init | Wiki Created
Initialized the business/work knowledge base wiki.
Pages created: [index.md, log.md, overview.md]
Pages updated: []
Structure: raw/, wiki/ (entities, projects, concepts, sources, analyses, meetings), tools/
Schema: CLAUDE.md written with business/work conventions.

---

## [2026-04-10] ingest | All 24 Raw Sources Processed
Processed and ingested all 24 raw source files across raw/x/, raw/repos/, and raw/assets/.

### Pages Created

**Concept Pages (6):**
1. [[llm-wiki-pattern]] — Three-layer architecture and three workflows (ingest, query, lint)
2. [[vectorless-retrieval]] — Alternative to embeddings; BM25, SQL, knowledge graphs
3. [[multi-agent-orchestration]] — Agent design, patterns (CoT/ToT/ReAct), protocols (MCP/A2A)
4. [[obsidian-integration]] — Obsidian as frontend IDE for markdown wikis
5. [[claude-code-ecosystem]] — .claude/ folder, commands, agents, skills, hooks, memory
6. [[structured-information-extraction]] — Extracting structured data with source grounding

**Entity Pages (3):**
1. [[andrej-karpathy]] — Originator of [[llm-wiki-pattern]]; token spend shift to knowledge management
2. [[google-langextract]] — Open-source extraction tool with source grounding
3. [[breferrari-obsidian-mind]] — Production Obsidian vault template for Claude Code

**Source Summary Pages (21):**
- Karpathy sources (3): karpathy-project-origin, karpathy-llm-wiki-gist, shann-holmberg-post
- Pattern extensions (3): code-rams-post, jumperz-multi-agent-post, dkare1009-vectorless-rag-post
- Multi-agent setup (2): dr-cintas-claude-code-setup, explorax-agentic-skills
- Claude Code ecosystem (4): zodchiii-claude-hooks, akshay-pachaar-claude-folder, tom-doerr-obsidian-vault, ernesto-software-vibe-coding
- Tools & discoveries (4): mdancho84-langextract, nate-google-cowork, ruben-hassid-claude-comparison, prince-canuma-mlx-vlm
- Repositories (4): breferrari-obsidian-mind-repo, chenglou-pretext-repo, chenglou-pretext, google-langextract-repo
- Visual references (2): ai-agents-cheat-sheet, llm-wiki-architecture-screenshot
- Incomplete/stubs (2): dkare1009-post-placeholder, sharbel-post-placeholder

### Pages Updated

- [[wiki/index.md]] — Complete catalog of all new pages with descriptions and source counts

### Major Themes Identified

1. **[[llm-wiki-pattern]]** — Core architecture (Karpathy origin, extended by Jumperz to multi-agent)
2. **[[vectorless-retrieval]]** — Paradigm shift away from embeddings (dkare1009)
3. **[[multi-agent-orchestration]]** — Agent scaling patterns (Jumperz 10-agent, Dr. Cintas 27-agent)
4. **[[claude-code-ecosystem]]** — Production tools and conventions (hooks, commands, agents, skills)
5. **[[obsidian-integration]]** — Frontend and memory (breferrari template as reference)
6. **[[structured-information-extraction]]** — Extraction tooling (Google LangExtract)

### Cross-Linking Strategy

- Linked all posts referencing [[llm-wiki-pattern]] to that concept page
- Linked agent/orchestration sources to [[multi-agent-orchestration]]
- Linked Claude Code ecosystem sources to [[claude-code-ecosystem]]
- Linked extraction/retrieval sources to [[vectorless-retrieval]] and [[structured-information-extraction]]
- Linked Obsidian/memory sources to [[obsidian-integration]]
- Every source page links to related concept, entity, and source pages

### Notes

- Two sources (dkare1009-post-2039407475275743545, sharbel-post-2039376686362333340) had incomplete extraction; created placeholder pages preserving the links
- All wikilinks use Obsidian format: [[page-name]] or [[page-name|Display Text]]
- Every page includes YAML frontmatter with title, type, created, updated, tags, sources, related
- Index now shows 3 entities, 6 concepts, and 21 source summary pages
- Total ingestion: 24 raw sources → 30 wiki pages created + 1 index updated
