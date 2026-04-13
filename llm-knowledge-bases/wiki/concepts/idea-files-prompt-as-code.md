---
title: Idea Files / Prompt-as-Code
type: concept
created: 2026-04-11
updated: 2026-04-11
tags: [philosophy, prompts, knowledge-management, meta, architecture]
sources: [code-rams-post, karpathy-llm-wiki-gist, karpathy-project-origin]
related: [llm-wiki-pattern, schema-driven-governance, claude-code-ecosystem]
---

## Definition

Idea files (or prompt-as-code) is the concept that schema documents, operational prompts, and wiki structures are themselves a codebase for ideas — and maintaining them is the primary engineering work in LLM-powered knowledge systems.

## Core Argument

In traditional software, code is the artifact and documentation is secondary. In LLM-maintained systems, the relationship flips: the prompts, schemas, and structural documents *are* the primary artifacts because they determine what the LLM produces. The wiki content is the output; the schema and prompts are the source code.

This reframing has practical implications:
- Schema files deserve version control, review, and iteration — the same rigor applied to source code
- Prompt engineering for a knowledge base is architectural work, not just "writing instructions"
- The investment in `CLAUDE.md`, page conventions, and workflow definitions compounds over time as the wiki grows

## Origin

[[code-rams-post]] introduced the "idea files" framing: treating operational documents (schema files, project instructions, agent definitions) as first-class artifacts rather than throwaway configuration. This builds on [[andrej-karpathy]]'s original insight from [[karpathy-project-origin]] that the real shift is in where tokens get spent — moving from code generation to knowledge management.

## Where It Appears

- **[[code-rams-post]]** — Explicit articulation of idea files concept; schema/operational documents as first-class artifacts
- **[[karpathy-project-origin]]** — Token spend shifting from code to knowledge management
- **[[karpathy-llm-wiki-gist]]** — The gist itself is an idea file: a prompt-as-code artifact that defines an entire system architecture
- **This wiki's `CLAUDE.md`** — A production example of prompt-as-code governing a knowledge base

## Implications

1. **Wiki maintenance is engineering**: Adding cross-links, improving page structure, and refining the schema are not busywork — they improve the "codebase" that produces knowledge
2. **Schema iteration compounds**: Each improvement to `CLAUDE.md` makes every future session more consistent
3. **Prompts are architecture**: The decision to separate raw/, wiki/, and schema layers is an architectural choice encoded in prompts, not in traditional code

## See Also

- [[schema-driven-governance]] for the practical application of this philosophy
- [[llm-wiki-pattern]] for the architecture this concept grounds
- [[claude-code-ecosystem]] for how .claude/ folder embodies prompt-as-code in development workflows
