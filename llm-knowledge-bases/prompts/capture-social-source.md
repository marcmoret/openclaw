# Capture Social Source Prompt

Use this prompt when the input source is a social post, especially an X/Twitter post.

## Objective

Capture the social post as a first-class source and separate it from any linked artifacts.

## Instructions

1. Create a source file in `raw/x/` for the post itself.
2. Record, when available:
   - post URL
   - author
   - timestamp
   - post text
   - thread context summary
   - attached media references
   - outbound links
3. If the post links to an article, repo, paper, video, or dataset, treat that linked item as a separate source.
4. In the post source note, explicitly mark whether the post is:
   - primary evidence
   - commentary
   - lead / pointer
   - speculation
5. Add a short note on why the post matters.

## Output format

```md
# Social Source: <short title>

- URL:
- Author:
- Timestamp:
- Type: X post
- Role: commentary | lead | evidence | speculation
- Outbound links:

## Post text

## Context

## Why it matters

## Related sources
```
