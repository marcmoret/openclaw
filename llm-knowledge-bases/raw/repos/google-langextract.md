# Repo Source: google/langextract

- URL: https://github.com/google/langextract
- Host: GitHub
- Owner: google
- Repo: langextract
- Type: repository
- Captured from:
  - https://x.com/mdancho84/status/2039726865775051135?s=46

## Summary

Official Google open-source repository for LangExtract, a Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization.

Notable capabilities from the README:
- extract structured information from unstructured text using user-defined prompts and few-shot examples
- map every extraction back to exact source-text locations for traceability
- optimize for long documents using chunking, parallel processing, and multiple extraction passes
- generate interactive HTML visualizations for reviewing extractions in context
- support multiple model backends, including Gemini, OpenAI, and local models via Ollama
- support custom provider plugins for additional model providers

Implementation shape:
- Python library (`pip install langextract`)
- centered on an `lx.extract(...)` API
- relies heavily on prompt design and high-quality examples
- outputs can be saved as JSONL and visualized as HTML

## Why it matters

This is highly relevant to the `raw/ -> wiki/` workflow because information extraction from messy source material is a core part of ingesting articles, papers, notes, and other raw documents into a maintained knowledge base. It looks especially useful when you want more than summarization—e.g. extracting entities, relationships, attributes, and source-grounded spans before compiling wiki notes.

## Fit assessment for this project

Promising use cases:
- extracting structured entities/facts from long articles or reports
- preprocessing difficult raw material before the LLM writes wiki pages
- preserving traceability from wiki claims back to source spans
- generating intermediate JSON/HTML artifacts for QA or linting

Caveats:
- it is a library/toolchain component, not a complete wiki compiler
- it requires prompt/example design work to get high-quality extractions
- for many small/simple sources, direct LLM summarization may still be cheaper and simpler
- likely best as an optional ingest enhancement, not the default path for every source

## Recommendation

Treat LangExtract as a strong optional ingest tool for difficult or high-volume source material, especially long documents where grounded extraction matters. It is probably not the first thing to use for every tweet, note, or short article, but it could become valuable for scaling the pipeline.

## Next action

If useful later, prototype a small ingest experiment comparing:
- direct LLM wiki compilation
- LangExtract-assisted extraction followed by wiki compilation
