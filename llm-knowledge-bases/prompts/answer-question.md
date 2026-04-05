# Answer Question Prompt

Use this prompt with an LLM agent working inside this repository.

## Objective

Answer a question against the local wiki and raw corpus, then render the result into `outputs/` as a durable artifact instead of only replying in chat.

## Required first step

Read:
1. `WIKI-SCHEMA.md`
2. `wiki/index.md`
3. `wiki/log.md`

## Instructions

1. Restate the question as a filename-safe slug.
2. Search the relevant wiki pages first.
3. Pull supporting evidence from `raw/` only when the wiki is insufficient.
4. Write the answer to one of:
   - `outputs/answers/`
   - `outputs/reports/`
   - `outputs/slides/`
   - `outputs/visuals/`
5. Include:
   - question
   - short answer
   - evidence / reasoning
   - linked related pages
   - follow-up questions
6. If the output reveals durable knowledge, promote or suggest promoting the useful parts back into `wiki/`.
7. Add a concise log entry to `wiki/log.md` for meaningful durable outputs.

## Frontmatter convention

For durable output pages, prefer YAML frontmatter like:

```yaml
---
title: Output title
type: answer | report | slides | visual
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
question: original question
related:
  - wiki/relative/path.md
---
```
