---
title: LangExtract
type: entity
status: active
created: 2026-04-04
updated: 2026-04-04
tags:
  - tool
  - extraction
  - ingest
related:
  - wiki/source-notes/google-langextract.md
  - wiki/concepts/vectorless-retrieval.md
---

# LangExtract

## Summary

LangExtract is an optional extraction tool relevant to the ingest layer of this project. It is not the main architecture, but a specialized helper for difficult or long-form raw sources where structured extraction and traceability matter.

## Why relevant

It provides:
- source-grounded extraction
- long-document handling
- structured outputs
- reviewable intermediate artifacts

## Current project stance

Use LangExtract selectively:
- not for every source
- most useful for complex, noisy, or long documents
- optional preprocessing before wiki compilation

## Related

- [google/langextract](../source-notes/google-langextract.md)
- [Vectorless retrieval](../concepts/vectorless-retrieval.md)
- [Recommended operating model](../concepts/recommended-operating-model.md)

## Sources

- [google/langextract](../source-notes/google-langextract.md)
