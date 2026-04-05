# LLM Knowledge Bases

An Obsidian-friendly workspace for building personal research knowledge bases with LLMs.

## Goal

Turn a pile of raw source material into a maintained markdown wiki that an LLM can:
- ingest incrementally
- summarize and cross-link
- answer questions against
- render outputs into markdown, slides, and images
- lint for consistency and missing data

## Project origin

This project is inspired by Andrej Karpathy's framing of **LLM Knowledge Bases**.
See [docs/project-origin.md](docs/project-origin.md).

## Core idea

- `raw/` stores source material exactly as collected
- `wiki/` stores the compiled knowledge base
- `outputs/` stores query results, reports, slides, and generated visuals
- `tools/` stores scripts for indexing, linting, and query support
- `prompts/` stores reusable instructions for LLM-driven workflows

## Proposed workflow

1. Collect sources into `raw/`
2. Run ingest/index tools to create lightweight manifests
3. Use an LLM to compile or update `wiki/`
4. Ask questions that render results into `outputs/`
5. Optionally file durable outputs back into `wiki/`
6. Run lint/health checks to improve coverage and integrity

## Directory layout

```text
llm-knowledge-bases/
  raw/
    inbox/
    x/
    articles/
    papers/
    repos/
    datasets/
    images/
  wiki/
    concepts/
    entities/
    source-notes/
    indexes/
    maps/
  outputs/
    answers/
    reports/
    slides/
    visuals/
  tools/
  prompts/
  docs/
```

## Suggested Obsidian setup

Open `llm-knowledge-bases/` as an Obsidian vault.

Recommended top-level views:
- `raw/` for source capture
- `wiki/` for the maintained knowledge graph
- `outputs/` for generated artifacts

## First steps

1. Put a few source documents in `raw/inbox/` or `raw/x/`
2. For social links, use `prompts/capture-social-source.md` and keep the post separate from any linked artifact
3. If X blocks extraction, create a source shell and enrich it later with pasted text, screenshots, or a successful clip
4. Run `tools/index_raw.py` to create a source manifest
5. Use `prompts/compile-wiki.md` with your LLM agent
6. Review generated files in `wiki/`
7. Use `prompts/answer-question.md` for Q&A into `outputs/`

## Status

This is a starter scaffold, not a finished product.
