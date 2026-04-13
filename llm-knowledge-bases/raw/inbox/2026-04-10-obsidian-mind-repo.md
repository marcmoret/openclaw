# Obsidian Mind

- URL: https://github.com/breferrari/obsidian-mind
- Date captured: 2026-04-10
- Type: repo

## Content

**Obsidian Mind** is a GitHub template repository that creates a persistent memory system for AI coding agents. It enables Claude Code, Codex CLI, and Gemini CLI to maintain context across sessions through an organized Obsidian vault.

### Core Problem & Solution

The fundamental issue: AI agents forget between sessions, forcing users to re-explain context repeatedly. Obsidian Mind solves this by providing agents with a structured knowledge base that grows with each interaction, creating compound learning over time.

### Key Features

**Session Lifecycle Management**
- Morning standup loads North Star goals, active projects, and recent changes
- Classification hooks automatically route content (decisions, incidents, wins, meetings) to appropriate locations
- End-of-day wrap-up verifies links, updates indexes, and identifies uncaptured wins

**Memory Architecture**
- Vault-first storage in `brain/` folder (git-tracked, browsable, linked)
- Five lifecycle hooks handle context injection and validation automatically
- Tiered loading keeps token costs low (~2K tokens at session start)
- Optional QMD semantic search for meaning-based queries

**Performance Tracking**
- Competency notes serve as link targets for work evidence
- Backlinks automatically accumulate review-season proof
- Brag Doc aggregates wins with source links
- Deep PR scanning for peer evidence generation

### Command Set

18 slash commands handle daily workflows:
- `/om-standup` - Morning context loading
- `/om-dump` - Freeform brain capture
- `/om-wrap-up` - Session review
- `/om-weekly` - Cross-session synthesis
- `/om-review-brief` - Review preparation
- `/om-incident-capture` - Deep incident documentation
- Plus 12 specialized commands for meetings, audits, and migrations

### Technical Stack

**Requirements:**
- Obsidian 1.12+ (for CLI support)
- Python 3.8+
- Git
- AI agent: Claude Code, Codex CLI, or Gemini CLI
- QMD (optional, for semantic search)

**Included Infrastructure:**
- 9 subagents for specialized tasks
- Obsidian skills (markdown, CLI, databases, canvas)
- Custom QMD skill for proactive semantic search
- Database views for dashboards and filtering
- 6 templates with YAML frontmatter

### Vault Structure

```
work/          - Projects, incidents, 1:1 notes
org/           - People, teams, organizational context
perf/          - Brag doc, competencies, evidence, reviews
brain/         - North Star, decisions, patterns, gotchas
reference/     - Architecture, codebase knowledge
.claude/       - Commands, agents, hooks, skills
```

### Multi-Agent Support

- **Claude Code** - Full support with integrated hooks and subagents
- **Codex CLI** - Reads AGENTS.md natively; hooks configured in `.codex/hooks.json`
- **Gemini CLI** - Reads GEMINI.md natively; hooks configured in `.gemini/settings.json`
- **Other agents** - Can follow vault conventions documented in AGENTS.md

### Getting Started

1. Clone as GitHub template or use as repository
2. Open folder as Obsidian vault
3. Enable Obsidian CLI in Settings (requires 1.12+)
4. Fill in `brain/North Star.md` with personal goals
5. Run `claude`, `codex`, or `gemini` in vault directory
6. Use `/om-standup` for first morning kickoff

### Customization Points

Users adapt the system by modifying:
- North Star goals (grounds every session)
- Organizational notes (manager, team, collaborators)
- Competency framework (perf/competencies/)
- Commands (for GitHub org, Slack workspace)
- Operating manual (`CLAUDE.md` - evolved over time)

### License

MIT License

---

**Repository:** github.com/breferrari/obsidian-mind
**Stars:** 1.7k | **Forks:** 240
