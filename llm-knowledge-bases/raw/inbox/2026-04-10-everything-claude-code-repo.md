# Everything Claude Code

- URL: https://github.com/affaan-m/everything-claude-code
- Date captured: 2026-04-10
- Type: repo

## Content

**Everything Claude Code** is an agent harness performance optimization system that evolved from an Anthropic hackathon winner. It provides a comprehensive toolkit for Claude Code, Cursor, OpenCode, Codex, and similar AI development environments.

### Key Statistics

- **140,000+ stars** and **21,000+ forks** on GitHub
- **170+ contributors** across the project
- Supports **12+ language ecosystems**
- **47 agents**, **181 skills**, and **79 legacy command shims**

### Core Philosophy

The project is not merely configuration files. Rather, it represents a fully realized system encompassing specialized agents for delegation, workflow skills, memory optimization through hooks, continuous learning mechanisms, security scanning capabilities, and research-first development patterns honed through months of intensive daily use in production environments.

### Primary Components

#### Agents (Specialized Subagents)
The system includes 36+ specialized agents for code review, architectural decisions, testing strategies, security analysis, and language-specific problem-solving (C++, Go, Python, TypeScript, Java, Kotlin, Rust, etc.).

#### Skills (Domain Knowledge)
**"Workflow definitions and domain knowledge"** organized by specialty:
- Backend/frontend patterns and best practices
- Framework-specific guidance (Django, Spring Boot, Laravel)
- Testing and verification methodologies
- Security reviews and deployment patterns
- Content generation and business workflows (new in recent versions)

#### Commands & Rules
Legacy slash-command shims alongside rules structured by programming language, covering common practices for TypeScript, Python, Go, Java, PHP, Perl, Kotlin, C++, and Rust.

#### Hooks System
Automation triggered at development lifecycle points (session start, file edit, pre-commit) for memory persistence, context optimization, and continuous learning.

### Installation Approaches

**Plugin Method** (via Claude Code marketplace):
```
/plugin marketplace add https://github.com/affaan-m/everything-claude-code
/plugin install ecc@ecc
```

**Direct Installation** (macOS/Linux):
```bash
git clone https://github.com/affaan-m/everything-claude-code.git
./install.sh --profile full
```

**Windows PowerShell**:
```powershell
.\install.ps1 --profile full
```

### Latest Features (v1.10.0 - April 2026)

Recent updates include surface synchronization with live repository metadata, expanded operator workflows for business operations, media tooling for technical explainers, and **ECC 2.0 alpha** — a Rust control-plane prototype offering dashboard, session management, and daemon capabilities (alpha stage, not general release).

### Documentation

Three primary guides accompany the codebase:
- **Shorthand Guide**: Setup foundations and philosophy (recommended entry point)
- **Longform Guide**: Token optimization, memory persistence, evaluation strategies, parallelization
- **Security Guide**: Attack vectors, sandboxing, vulnerability scanning, AgentShield integration

### Cross-Platform Support

Full compatibility across Windows, macOS, and Linux with automatic package manager detection (npm, pnpm, yarn, bun) and runtime controls via environment variables (`ECC_HOOK_PROFILE`, `ECC_DISABLED_HOOKS`).

### License & Community

MIT licensed with 150+ GitHub App installations and active community contribution spanning multiple language implementations and translations.
