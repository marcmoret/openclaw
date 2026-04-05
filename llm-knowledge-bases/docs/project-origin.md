# Project Origin

This project is grounded in Andrej Karpathy's framing of **LLM Knowledge Bases**.

## Canonical source

- X post: https://x.com/karpathy/status/2039805659525644595?s=46
- Local screenshot:
  - ~/.openclaw/media/browser/15edf749-03d4-4740-9259-937fd7c9112d.png

## Why this matters

This post is the clearest high-level statement of the workflow this repository is trying to support:
- collect raw source material
- compile it into a markdown wiki with LLMs
- query and extend the wiki over time
- render outputs back into markdown/slides/images
- feed useful outputs back into the wiki
- treat the knowledge base as a compounding system rather than one-off chat answers

## Core ideas we are inheriting

- `raw/` as the ingest layer for source materials
- `wiki/` as the compiled knowledge layer
- `outputs/` as durable artifacts from questions, reports, slides, and visualizations
- Obsidian as the main human-facing frontend
- LLMs as maintainers of the wiki, not just answer engines
- incremental health checks, linting, enrichment, and relationship discovery over time
- the possibility that future versions may incorporate synthetic data generation or fine-tuning

## Practical interpretation for this repo

This repository is not trying to be a generic note-taking vault.
It is trying to be an **LLM-operated research knowledge workspace**.

That means:
- source capture matters
- provenance matters
- derived artifacts should be durable
- outputs should "add up"
- the wiki is an evolving product of ongoing exploration

## If the project gets fuzzy

Return to the Karpathy framing:
- raw sources in
- wiki compilation
- agentic querying
- durable outputs
- feedback of useful results into the knowledge base
