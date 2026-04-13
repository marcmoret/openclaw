---
title: dkare1009 - Vectorless RAG Post
type: source
created: 2026-04-10
updated: 2026-04-10
tags: [sources, social, commentary, vectorless-rag, retrieval]
sources: [dkare1009-post-2039665922185589044]
related: [vectorless-retrieval, llm-wiki-pattern]
---

## Source Metadata

- **URL**: https://x.com/dkare1009/status/2039665922185589044
- **Author**: dkare1009 (@dkare1009)
- **Type**: X / Social post
- **Date**: Unknown (early April 2026)
- **Role**: Commentary / media source
- **Source file**: `/raw/x/2026-04-03-dkare1009-2039665922185589044.md`

## Key Takeaways

- "RAG = vectors" is outdated paradigm
- **Vectorless RAG** is emerging as a more practical alternative
- Alternative retrieval methods: BM25, SQL, knowledge graphs, direct context injection
- No embeddings, no re-indexing, lower infrastructure cost
- Highly relevant to this knowledge-base approach (already vectorless)

## Post Text Summary

"'RAG = vectors' is outdated.
A new shift is happening:
Vectorless RAG.

Instead of embeddings + vector DBs, it uses:
- BM25 / keyword search
- SQL queries
- Knowledge graphs
- Direct context injection

Claims:
- No embeddings
- No re-indexing
- Lower infra cost"

## Detailed Summary

This post articulates an emerging paradigm: **vectorless retrieval is becoming practical**.

The shift away from embeddings because:
1. **BM25 / keyword search** — fast, interpretable, works well for structured knowledge
2. **SQL queries** — exact matches over structured metadata
3. **Knowledge graphs** — explicit relationships (like Obsidian wikilinks)
4. **Direct context injection** — just load full documents/sections directly

Advantages:
- No embedding model overhead
- No vector index maintenance
- Lower infrastructure cost
- Easier to debug and audit

This aligns naturally with the [[llm-wiki-pattern]]:
- Wiki is already organized into cross-linked pages
- Index.md provides a catalog
- Wikilinks create an explicit knowledge graph
- File-based organization suits keyword search
- No vector DB needed

## Why It Matters

This post validates the design choice of this wiki: **we don't need vectors**.

Instead:
- Use the index (like BM25)
- Use wikilinks (like a knowledge graph)
- Use structured metadata (like SQL queries on frontmatter)
- Load full documents/sections directly

## Concepts Introduced

- [[vectorless-retrieval]] — the concept
- Relationship to [[llm-wiki-pattern]]

## Related Sources

- [[google-langextract]] — structured extraction alternative to vectors
- [[karpathy-llm-wiki-gist]] — already mentions vectors are optional

## See Also

- [[vectorless-retrieval]] for detailed concept
- [[llm-wiki-pattern]] for architecture
- dkare1009 for author context
