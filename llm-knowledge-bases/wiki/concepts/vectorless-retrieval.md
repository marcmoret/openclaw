---
title: vectorless retrieval
type: concept
status: active
created: 2026-04-04
updated: 2026-04-04
tags:
  - retrieval
  - search
  - architecture
related:
  - wiki/source-notes/dkare1009-post-2039665922185589044.md
  - wiki/source-notes/karpathy-llm-wiki-gist.md
---

# Vectorless retrieval

## Summary

A retrieval philosophy that avoids assuming embeddings and vector databases are mandatory. Instead, it leans on keyword search, structured indexes, SQL-like retrieval, knowledge graphs, and direct context injection when the corpus is still moderate in size.

## Key points

- vector databases are optional, not mandatory
- a strong `index.md` and well-maintained source notes can go surprisingly far
- BM25 / keyword search may be enough at moderate scale
- structured navigation lowers infrastructure cost and complexity
- vector infrastructure can remain an optional later enhancement

## Why it matters

This concept is aligned with the current project architecture, which uses markdown, source notes, indexes, and curated wiki structure rather than jumping immediately to embedding-heavy systems.

## Related

- [dkare1009 post 2039665922185589044](../source-notes/dkare1009-post-2039665922185589044.md)
- [karpathy/llm-wiki gist](../source-notes/karpathy-llm-wiki-gist.md)

## Sources

- [dkare1009 post 2039665922185589044](../source-notes/dkare1009-post-2039665922185589044.md)
- [karpathy/llm-wiki gist](../source-notes/karpathy-llm-wiki-gist.md)

## Open questions

- When should the project add a dedicated search engine?
- Which retrieval operations deserve their own helper tool first?
