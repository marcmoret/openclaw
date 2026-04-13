---
title: Google LangExtract
type: entity
created: 2026-04-10
updated: 2026-04-10
tags: [tools, extraction, information-retrieval, google]
sources: [google-langextract, mdancho84-post]
related: [structured-information-extraction, vectorless-retrieval]
---

## Summary

LangExtract is Google's open-source Python library for extracting structured information from unstructured text using LLMs with **source grounding** — every extracted fact maps back to its original location in the source text.

## Key Features

- **LLM-based extraction** — uses language models with user-defined prompts and few-shot examples
- **Source grounding** — maps every extraction to exact source-text spans
- **Long document handling** — chunking, parallel processing, multiple extraction passes
- **Interactive visualization** — HTML views of extractions with source highlighting
- **Model flexibility** — supports Gemini, OpenAI, Ollama, and custom provider plugins
- **Python library** — `pip install langextract`

## Core API

```python
import langextract as lx

results = lx.extract(
    text="...",
    schema={...},     # Define what to extract
    examples=[...],   # Few-shot examples
    model="gemini-1.5"
)

# Output: JSONL with source spans
# Can be visualized as interactive HTML
```

## Use Cases

- Extracting entities and facts from long documents
- Pre-processing raw material before filing into knowledge base
- Maintaining traceability from wiki claims back to sources
- Generating intermediate extraction QA artifacts
- Scaling ingest pipelines for structured data

## Relationship to [[structured-information-extraction]]

LangExtract is the concrete tool embodying the [[structured-information-extraction]] concept—providing both the extraction capability and the source grounding that enables traceable knowledge bases.

## Discovery

[[mdancho84-langextract|mdancho84]] presented LangExtract as a major breakthrough in open-source extraction technology.

## Fit for This Wiki

**Promising applications:**
- Extracting entities and relationships from long articles
- Pre-processing difficult raw material for higher-confidence entity/fact filing
- Maintaining source spans for wiki claims

**Caveats:**
- Not needed for all sources (short posts, simple notes)
- Requires prompt design and example curation
- Best as an optional enhancement

## Where It Appears

- [[google-langextract-repo]] — full repository documentation
- [[mdancho84-langextract]] — discovery announcement
- This wiki's potential future ingest enhancements

## See Also

- [[google-langextract-repo]] for repository documentation
- [[structured-information-extraction]] for the concept
- [[vectorless-retrieval]] for complementary retrieval approaches
- [[llm-wiki-pattern]] for where extraction fits in ingest workflow
