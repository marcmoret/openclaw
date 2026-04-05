# Promotion Rules

Rules for deciding when an output should remain in `outputs/` versus being promoted back into the wiki.

## Principle

Not every output deserves promotion.
Promote durable knowledge, not every transient answer.

## Promote into the wiki when the output is...

### 1. Reusable
If the answer is likely to matter again, it should not live only in `outputs/`.

Examples:
- architectural decisions
- stable comparisons
- recurring explanations
- durable synthesis across multiple sources

### 2. Clarifying
If the output sharpens the project's understanding of a concept, tool, workflow, or tradeoff, promote it.

Examples:
- why vectorless retrieval is preferred right now
- how ingest/query/lint should work
- when LangExtract should be used

### 3. Source-backed
If the output is grounded in multiple strong sources and not just a speculative chat answer, it is a better candidate for promotion.

### 4. Likely to influence future work
If future ingests, questions, or project design decisions should take it into account, promote it.

## Do NOT promote when the output is...

- purely temporary
- conversational only
- low-confidence speculation
- superseded quickly
- too narrow to matter again
- just a rough working note with no durable value

## Promotion destinations

### Promote to a concept page when...
- the output defines a recurring idea
- it captures a stable pattern or architecture
- it explains a reusable workflow or principle

### Promote to an entity page when...
- the output deepens understanding of a person, tool, repo, framework, or organization
- the entity is appearing across multiple sources

### Promote to an index page when...
- the output improves navigation or organization
- it helps the system find or group relevant material later

### Leave in `outputs/` when...
- the result is useful but still situational
- it may later be distilled into the wiki, but is not there yet

## Recommended workflow

1. write the answer/report to `outputs/`
2. ask: is this durable, reusable, and likely to matter again?
3. if yes, distill the durable parts into the wiki
4. log the promotion in `wiki/log.md`

## Strong default

When in doubt, prefer:
- **distilling** the durable insight into the wiki
- not copying the entire output wholesale

The wiki should store the stable insight.
The full report can remain in `outputs/` as the longer artifact.
