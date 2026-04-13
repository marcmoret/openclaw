---
title: Recommended Operating Model
type: concept
created: 2026-04-04
updated: 2026-04-12
tags: [operating-model, architecture, workflow]
sources: [karpathy-llm-wiki-gist, karpathy-project-origin, jumperz-multi-agent-post, dkare1009-vectorless-rag-post]
related: [persistent-knowledge-base, llm-wiki-pattern, vectorless-retrieval, schema-driven-governance, multi-agent-orchestration]
status: active
---

## Summary

The project should operate as a schema-driven, Obsidian-fronted, markdown-native knowledge compiler. The best model is a mostly single-agent workflow with immutable raw sources, a maintained wiki, lightweight retrieval, and selective optional tooling for harder ingest cases.

## Key Principles

- The wiki is the primary knowledge artifact — not chat history, not raw sources
- Raw sources remain immutable; the wiki is the compiled derivative layer
- Outputs should compound back into the wiki when durable
- Single-agent discipline should come before multi-agent scale
- [[vectorless-retrieval]] should be the default stance at current scale
- LangExtract and similar tools remain optional for difficult ingest, not mandatory everywhere
- Schema and prompt files (CLAUDE.md, prompts/) are first-class implementation assets

## Why This Matters

This concept turns the source synthesis into a durable project stance, so the architecture does not have to be re-argued from scratch every session. New agents entering the project can read this page and understand the current operating posture.

## Scaling Path

Multi-agent compilation (see [[multi-agent-orchestration]]) should be treated as a later scaling path, not the default starting architecture. The current project is better served by tightening the single-agent wiki-maintenance loop first. When multiple computers or agents contribute, the shared repository acts as the coordination layer — not agent-to-agent chat.

## Related Concepts

- [[persistent-knowledge-base]] — The architectural center: why wiki over RAG
- [[llm-wiki-pattern]] — The concrete three-layer implementation
- [[vectorless-retrieval]] — Default retrieval stance at current scale
- [[schema-driven-governance]] — Schema files as coordination mechanism
- [[multi-agent-orchestration]] — Future scaling path
