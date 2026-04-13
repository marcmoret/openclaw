# LangExtract

- URL: https://github.com/google/langextract
- Date captured: 2026-04-10
- Type: repo

## Content

**LangExtract** is a Python library created by Google that leverages large language models to extract structured information from unstructured text documents. The tool focuses on precise source grounding—every extracted element maps to its exact location in the original text, enabling visual highlighting and verification.

### Key Features

The library offers several distinctive capabilities:

1. **Source Grounding**: "Maps every extraction to its exact location in the source text" for traceability and verification purposes.

2. **Structured Outputs**: Enforces consistent output schemas using few-shot examples and controlled generation with compatible models like Gemini.

3. **Long Document Handling**: Employs optimized chunking, parallel processing, and multiple passes to overcome the "needle-in-a-haystack" challenge.

4. **Interactive Visualization**: Generates self-contained HTML files displaying thousands of extracted entities within their original context.

5. **Flexible Model Support**: Compatible with cloud-based LLMs (Gemini, OpenAI) and local models via Ollama integration.

6. **Domain Adaptability**: Requires only a few examples for any extraction task without model fine-tuning.

7. **Knowledge Utilization**: Leverages LLM world knowledge through prompt engineering and example selection.

### Getting Started

Installation is straightforward via pip: `pip install langextract`

Users must provide an API key for cloud models. The basic workflow involves:
- Defining extraction tasks with clear prompts
- Supplying high-quality examples
- Running extraction with preferred models
- Visualizing results in interactive HTML format

### Supported Models

- **Gemini**: Recommended default (gemini-2.5-flash) for optimal speed and cost
- **OpenAI**: Requires optional dependency installation
- **Ollama**: Supports local inference without API keys
- **Vertex AI**: Enterprise deployment option

### Example Applications

The library demonstrates capabilities across domains:
- Full-text literary analysis (Romeo and Juliet extraction from Project Gutenberg)
- Medical information extraction (medication identification and attributes)
- Radiology report structuring (RadExtract demo on Hugging Face)

### Extensibility

A plugin system enables community members to add custom model providers independently, allowing integration of proprietary or emerging models without modifying core code.

### Project Details

- **Repository**: google/langextract on GitHub
- **License**: Apache 2.0 (inferred from Google open-source practices)
- **Status**: Active development with 138+ commits, 82 open issues, 45 pull requests
