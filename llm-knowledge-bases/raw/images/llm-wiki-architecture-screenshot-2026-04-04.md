# Image Source: LLM Wiki architecture screenshot

- Type: image / screenshot
- Date captured: 2026-04-04
- Origin: user-provided screenshot in chat

## Visible title

LLM Wiki — Karpathy's Knowledge Compilation Pattern

## Summary

A concise architecture diagram of the LLM wiki pattern showing the three-layer structure, the three core operations, and the split between human and LLM-agent responsibilities.

## Visible architecture

### Layers
- **Raw Sources** — immutable, read-only
- **The Wiki** — LLM-owned markdown
- **Schema** — `CLAUDE.md` / `AGENTS.md`

### Relationships
- Raw Sources -> The Wiki (`reads`)
- Schema -> The Wiki (`guides`)

### Operations
- **Ingest** — source -> wiki updates
  - read src
  - write summary
  - update idx
  - cross-link

- **Query** — question -> synthesized answer
  - search idx
  - synthesize
  - file back to wiki

- **Lint** — health-check / consistency
  - find issues
  - fix & patch
  - suggest sources

### Actors
- **Human** — curate, question, think
- **LLM Agent** — summarize, cross-ref, maintain

## Why it matters

This is one of the clearest compact architecture references for the project so far. It directly reinforces the exact structure we have now been building into the repository: raw sources, wiki, schema, ingest/query/lint workflows, and the division of labor between human and LLM.
