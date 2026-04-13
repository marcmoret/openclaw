# Cross-Agent Workflow

How multiple agents should collaborate on this project through shared files instead of fragile chat handoffs.

## Shared truth

The shared truth is the repository itself:
- `raw/`
- `wiki/`
- `outputs/`
- `CLAUDE.md`
- `wiki/index.md`
- `wiki/log.md`
- `docs/claude-handoff.md`

Do not rely on agent-to-agent chat history as the primary state.

## Working rules

### 1. Read before acting
Before substantial work, read:
1. `CLAUDE.md`
2. `wiki/overview.md`
3. `wiki/index.md`
4. `wiki/log.md`
5. `docs/claude-handoff.md`

### 2. Use durable files for coordination
If a decision matters later, put it in a file.
Examples:
- source notes
- concept pages
- entity pages
- `wiki/log.md`
- handoff notes

### 3. Log meaningful work
Append meaningful actions to `wiki/log.md`.
Examples:
- ingest pass
- query artifact worth keeping
- lint pass
- new concept/entity page
- structural change

### 4. Respect the layer split
- `raw/` = immutable source layer
- `wiki/` = maintained knowledge layer
- `outputs/` = task artifacts / reports / slides / visuals

### 5. Promote carefully
Use `docs/promotion-rules.md`.
Promote stable insights, not every temporary answer.

## Recommended handoff pattern

When handing off work, update:
- `docs/claude-handoff.md` for short operational context
- `wiki/log.md` for chronological record
- relevant notes/pages for actual durable content

## Good division of labor

One agent can:
- capture sources
- resolve links
- create source notes

Another can:
- synthesize concepts
- create entity pages
- lint and consolidate

Both should work through the same file conventions.

## Avoid

- duplicated notes for the same source unless clearly justified
- rewriting large portions of the wiki without updating index/log
- silent architecture changes with no log entry
