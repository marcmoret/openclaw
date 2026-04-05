# Source: karpathy/llm-wiki gist

- URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Raw URL: https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw
- Type: gist / concept document
- Author: Andrej Karpathy

## Summary

A foundational concept document describing a pattern for building personal knowledge bases with LLMs. The key idea is to place a persistent, LLM-maintained markdown wiki between the human and the raw source documents, so knowledge accumulates over time instead of being rediscovered from scratch at query time.

## Core ideas

- Replace pure query-time RAG with a persistent wiki that compounds over time.
- Keep three layers:
  - raw sources
  - wiki
  - schema / instruction document
- Operate the system through three main workflows:
  - ingest
  - query
  - lint
- Use `index.md` as the content-oriented catalog.
- Use `log.md` as the chronological activity record.
- Let the LLM maintain the wiki; humans curate, explore, and ask questions.
- Use Obsidian as a frontend/IDE for browsing the wiki.
- Use git naturally because the wiki is just markdown.

## Why it matters

This is the clearest written articulation of the exact project direction being explored in this workspace. It is more foundational than most of the tweet-sized commentary sources because it lays out the architecture, workflows, and rationale in one place.

## Strong takeaways

- the wiki should be a persistent, compounding artifact
- useful query outputs should be filed back into the wiki
- indexing and chronological logging deserve first-class treatment
- the schema file is a real operational layer, not a minor detail
- vector-heavy infrastructure is optional, not mandatory, at moderate scale

## Relevance to current project

Directly foundational. The current project scaffold already matches much of this pattern, but the gist sharpens the importance of:
- a stronger schema document
- a real `index.md`
- a real `log.md`
- more explicit ingest/query/lint workflows
