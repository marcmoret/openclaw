---
title: Vectorless Retrieval
type: concept
created: 2026-04-10
updated: 2026-04-10
tags: [rag, information-retrieval, knowledge-base, vectors]
sources: [dkare1009-post-2039665922185589044]
related: [llm-wiki-pattern, rag-evolution, structured-extraction]
---

## Definition

Vectorless Retrieval (or Vectorless RAG) is a paradigm shift away from embedding-based vector database retrieval toward alternative retrieval methods: keyword search, SQL queries, knowledge graphs, and direct context injection.

## Core Claim

"RAG = vectors" is outdated.

Instead of embeddings + vector similarity search:
- **BM25** / full-text keyword search
- **SQL queries** against structured data
- **Knowledge graphs** with explicit relationships
- **Direct context injection** from well-organized source files

## Key Benefits

- **No embeddings** — eliminates embedding computation and storage overhead
- **No re-indexing** — changes to knowledge don't require recomputing vectors
- **Lower infra cost** — simpler stack, fewer dependencies
- **Better interpretability** — retrieval is explicit and auditable
- **Faster iteration** — easier to debug what gets retrieved and why

## Relationship to LLM Wiki Pattern

Vectorless retrieval aligns naturally with the [[llm-wiki-pattern]] because:
1. The wiki is already organized into cross-linked pages and an index
2. Obsidian wikilinks provide explicit navigation (equivalent to a knowledge graph)
3. File-based organization is naturally conducive to keyword search
4. Direct context injection (reading full files or sections) is straightforward in markdown

No vector database required—just good information architecture.

## Practical Implementation

For this knowledge base:
- `index.md` provides a catalog (replaces semantic search)
- Obsidian wikilinks create an explicit knowledge graph
- YAML frontmatter (tags, sources) enables filtering
- Full-text search of `wiki/` works well for moderate-scale knowledge bases
- If scale increases, add SQL queries over the YAML frontmatter

## Where It Appears

- dkare1009 advocating for vectorless RAG approaches
- [[google-langextract]] as a structured extraction alternative to vector embeddings
- This wiki project's design (no vector DB, pure markdown + links)

## See Also

- [[llm-wiki-pattern]] — The parent architecture pattern
- [[google-langextract]] — Structured extraction tool
- rag-evolution (candidate concept page)
