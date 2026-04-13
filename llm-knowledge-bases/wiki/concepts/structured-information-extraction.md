---
title: Structured Information Extraction
type: concept
created: 2026-04-10
updated: 2026-04-10
tags: [extraction, information-retrieval, knowledge-base, tooling, traceability]
sources: [google-langextract, mdancho84-post]
related: [vectorless-retrieval, llm-wiki-pattern, claude-code-ecosystem]
---

## Definition

Structured information extraction is the process of converting unstructured text (articles, notes, reports) into structured data (entities, relationships, attributes) with **source grounding** — every extracted fact maps back to its original location in the source text.

## Why It Matters for Knowledge Bases

When ingesting raw sources into a wiki, structured extraction enables:
1. **Precise entity recognition** — extract people, companies, products with high confidence
2. **Relationship mapping** — capture "person X works at company Y"
3. **Source traceability** — every wiki claim links back to source spans
4. **Quality assurance** — review extractions against originals before filing into wiki
5. **Scalable ingest** — process large documents with consistent structure

## Google LangExtract

[[google-langextract]] is Google's open-source library for this task.

### Key Capabilities
- Extract structured information from unstructured text using LLM + prompt + examples
- **Source grounding** — map every extraction to exact source-text spans
- **Long document handling** — chunking, parallel processing, multiple passes
- **Interactive visualization** — HTML view of extractions with source highlighting
- **Multiple model backends** — Gemini, OpenAI, Ollama, custom providers

### Implementation
```python
import langextract as lx

# Define extraction schema and examples
results = lx.extract(
    text="...",
    schema={...},
    examples=[...],
    model="gemini-1.5"
)

# Results include source spans for traceability
# Can be visualized as interactive HTML
```

## Fit for This Wiki

**Promising use cases:**
- Pre-processing difficult raw material (long articles, reports)
- Extracting entities/facts with high confidence
- Maintaining traceability from wiki claims back to sources
- Generating intermediate JSON/HTML for QA

**Caveats:**
- Requires prompt/example design work
- For short/simple sources, direct summarization may be faster
- Best as an optional enhancement, not mandatory

## Relationship to Vectorless Retrieval

Structured extraction complements [[vectorless-retrieval]]:
- Instead of computing embeddings, extract meaningful structure
- Instead of vector search, use explicit entity/relationship queries
- Instead of approximate retrieval, get exact source spans

## Where It Appears

- [[google-langextract]] — the tool itself
- mdancho84 — discovery post calling it "better than $100K enterprise tools"
- This wiki's potential ingest enhancement pipeline

## See Also

- [[google-langextract]] for technical details
- [[vectorless-retrieval]] for retrieval implications
- [[llm-wiki-pattern]] for overall ingest workflow
