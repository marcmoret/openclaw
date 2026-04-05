# Architecture

## Components

### 1. Raw corpus

The raw corpus is append-only source material collected from the web, PDFs, repos, datasets, and images.

Principles:
- preserve originals where possible
- keep filenames stable
- prefer local copies for images and articles
- track provenance in a manifest
- treat social posts and linked artifacts as distinct but connected sources

### 2. Compiled wiki

The wiki is the LLM-maintained derivative layer.

Expected content:
- source summaries
- concept pages
- entity pages
- topical indexes
- backlink-rich maps of related ideas
- maintenance notes and gaps

### 3. Outputs

Outputs are query-time renderings, such as:
- answers as markdown memos
- slide decks in Marp
- visualizations
- reports and synthesis documents

Useful outputs can later be promoted into the wiki.

### 4. Tooling

Tooling should stay simple and transparent:
- manifest generation
- naive local search
- linting and health checks
- wiki statistics

## Recommended conventions

### Source identity

Each raw source should have:
- a stable id
- original path
- inferred type
- title if known
- timestamp if known
- optional source URL
- optional parent/related source ids for social-post-to-link relationships

### Wiki article structure

A good page usually includes:
- title
- short summary
- key claims or facts
- related concepts
- source references
- backlinks or linked pages
- open questions

### Incremental compile loop

1. detect new or changed raw sources
2. update manifests
3. update only affected wiki pages
4. refresh impacted indexes/maps
5. run lint/health checks

## Non-goals for v0

- heavy database infrastructure
- mandatory embeddings or RAG
- complicated ingestion pipelines
- hidden proprietary formats

Start with files and markdown first.
