---
title: Prompting Patterns
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [prompting, llm-patterns, developer-workflows]
sources: []
related: [idea-files-prompt-as-code, schema-driven-governance, boris-cherny-slash-commands]
status: stub
---

## Definition

Prompting patterns are reusable, structured strategies for composing prompts that elicit consistent, high-quality outputs from language models. They abstract common problem-solving techniques into repeatable templates.

## Core Patterns

Common techniques include:

- **Few-shot examples**: Providing examples of input-output pairs to guide the model toward desired behavior
- **Chain-of-thought**: Encouraging step-by-step reasoning by explicitly asking the model to show its work
- **System prompt layering**: Using system prompts to establish core behavior, then refining through user messages
- **Structured output**: Requesting responses in specific formats (JSON, YAML, markdown) to enable downstream processing
- **Role-based prompting**: Assigning personas or roles to shape the model's communication style and expertise

## Prompts as Code

A key insight is treating prompts as versioned code artifacts:
- Prompts should be stored in version control
- Patterns should be documented and named
- Effective prompts are iteratively refined based on usage and feedback
- Teams should share and curate libraries of high-performing prompts

This [[idea-files-prompt-as-code|approach enables systematic improvement]] and knowledge sharing across teams.

## Workflow Integration

Prompting patterns enable:
- **Consistency**: Same pattern applied across similar tasks yields predictable results
- **Reusability**: Patterns can be applied to new domains with minimal modification
- **Testing**: Patterns can be evaluated against benchmarks to measure effectiveness
- **Documentation**: Named patterns serve as communication tools within teams

## Related Concepts

- [[idea-files-prompt-as-code]] — Storing and versioning prompts systematically
- [[schema-driven-governance]] — Using system prompts to govern agent behavior
- [[boris-cherny-slash-commands]] — Slash commands as a prompting interface pattern
