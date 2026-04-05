# Source Triage

A working index of captured sources, their roles, linked primary artifacts, and next actions.

## Triage statuses

- `captured` — source recorded but not yet enriched
- `resolved` — linked artifacts or media behavior identified
- `summarized` — primary artifact/source note summarized
- `needs-media-review` — important details likely trapped in attached images/media
- `needs-primary-artifact` — social source captured but underlying repo/article/tool not yet identified

## Canonical references

### Karpathy — project origin
- Source: [karpathy-project-origin](../source-notes/karpathy-project-origin.md)
- Raw: [raw/x/2026-04-03-karpathy-2039805659525644595.md](../../raw/x/2026-04-03-karpathy-2039805659525644595.md)
- Status: `summarized`
- Notes:
  - canonical framing for the whole project
  - see [Project Origin](../../docs/project-origin.md)
- Next action:
  - use as a reference whenever project scope or workflow gets fuzzy

## Social sources

### Tom Dörr — Obsidian vault for Claude Code memory
- Source: [tom-doerr-post-2039906409387610408](../source-notes/tom-doerr-post-2039906409387610408.md)
- Raw: [raw/x/2026-04-03-tom-doerr-2039906409387610408.md](../../raw/x/2026-04-03-tom-doerr-2039906409387610408.md)
- Status: `resolved`
- Notes:
  - One link resolves to GitHub repo `breferrari/obsidian-mind`
  - One link resolves to attached media
- Linked primary artifact:
  - [breferrari-obsidian-mind](../source-notes/breferrari-obsidian-mind.md)
- Next action:
  - Optional deeper file-by-file inspection of repo conventions

### Matt Dancho — LangExtract
- Source: [mdancho84-post-2039726865775051135](../source-notes/mdancho84-post-2039726865775051135.md)
- Raw: [raw/x/2026-04-03-mdancho84-2039726865775051135.md](../../raw/x/2026-04-03-mdancho84-2039726865775051135.md)
- Status: `resolved`
- Notes:
  - Visible link resolves to attached media
  - Actual primary artifact identified separately as `google/langextract`
- Linked primary artifact:
  - [google-langextract](../source-notes/google-langextract.md)
- Next action:
  - Optional ingest experiment later

### Alvaro Cintas — Claude Code setup post
- Source: [dr-cintas-post-2038660653410320556](../source-notes/dr-cintas-post-2038660653410320556.md)
- Raw: [raw/x/2026-04-03-dr-cintas-2038660653410320556.md](../../raw/x/2026-04-03-dr-cintas-2038660653410320556.md)
- Status: `needs-media-review`
- Notes:
  - Visible link resolves to attached media
  - Underlying repo/project still not identified
- Next action:
  - Review attached media and identify underlying repo/project

### dkare1009 post
- Source: [dkare1009-post-2039407475275743545](../source-notes/dkare1009-post-2039407475275743545.md)
- Raw: [raw/x/2026-04-03-dkare1009-2039407475275743545.md](../../raw/x/2026-04-03-dkare1009-2039407475275743545.md)
- Status: `captured`
- Notes:
  - Browser extraction stalled for this specific page
- Next action:
  - Retry later or enrich with pasted text / screenshot

### Cheng Lou — Pretext
- Source: [chenglou-post-2037715519277760531](../source-notes/chenglou-post-2037715519277760531.md)
- Raw: [raw/x/2026-04-03-chenglou-2037715519277760531.md](../../raw/x/2026-04-03-chenglou-2037715519277760531.md)
- Status: `resolved`
- Notes:
  - Link resolves to GitHub repo `chenglou/pretext`
- Linked primary artifact:
  - [chenglou-pretext](../source-notes/chenglou-pretext.md)
- Next action:
  - Summarize the repo and assess fit for output/demo workflows

### Akshay Pachaar — Anatomy of the .claude/ folder
- Source: [akshay-pachaar-post-2035341800739877091](../source-notes/akshay-pachaar-post-2035341800739877091.md)
- Raw: [raw/x/2026-04-03-akshay-pachaar-2035341800739877091.md](../../raw/x/2026-04-03-akshay-pachaar-2035341800739877091.md)
- Status: `captured`
- Notes:
  - title extracted cleanly
  - likely media-heavy post
- Next action:
  - revisit media if the `.claude/` breakdown becomes important

### Nate.Google — Claude Cowork good read
- Source: [nate-google-post-2034663068685205625](../source-notes/nate-google-post-2034663068685205625.md)
- Raw: [raw/x/2026-04-03-nate-google-2034663068685205625.md](../../raw/x/2026-04-03-nate-google-2034663068685205625.md)
- Status: `captured`
- Notes:
  - title/body text extracted cleanly
  - linked resource not yet identified
- Next action:
  - revisit if we decide Claude Cowork resources are a priority

### Ruben Hassid — choosing the right Claude mode
- Source: [ruben-hassid-post-2034577982811992142](../source-notes/ruben-hassid-post-2034577982811992142.md)
- Raw: [raw/x/2026-04-03-ruben-hassid-2034577982811992142.md](../../raw/x/2026-04-03-ruben-hassid-2034577982811992142.md)
- Status: `captured`
- Notes:
  - body extracted mostly cleanly
  - linked infographic/resource not yet resolved
- Next action:
  - resolve the target if we want a stronger note on Code vs Cowork vs Projects

### Ernesto Lopez — important prompt in vibe coding
- Source: [ernesto-software-post-2034294904994627901](../source-notes/ernesto-software-post-2034294904994627901.md)
- Raw: [raw/x/2026-04-03-ernesto-software-2034294904994627901.md](../../raw/x/2026-04-03-ernesto-software-2034294904994627901.md)
- Status: `captured`
- Notes:
  - title extracted cleanly
  - visible link resolves to attached media
- Next action:
  - inspect media if the prompt content becomes important

### Prince Canuma — mlx-vlm v0.4.3
- Source: [prince-canuma-post-2039815307821199709](../source-notes/prince-canuma-post-2039815307821199709.md)
- Raw: [raw/x/2026-04-03-prince-canuma-2039815307821199709.md](../../raw/x/2026-04-03-prince-canuma-2039815307821199709.md)
- Status: `captured`
- Notes:
  - body extracted cleanly
  - visible link resolves to attached media
- Next action:
  - revisit if multimodal/vision tooling becomes a near-term priority

### Shann Holmberg — Karpathy workflow summary
- Source: [shann-holmberg-post-2040136166641693080](../source-notes/shann-holmberg-post-2040136166641693080.md)
- Raw: [raw/x/2026-04-03-shann-holmberg-2040136166641693080.md](../../raw/x/2026-04-03-shann-holmberg-2040136166641693080.md)
- Status: `captured`
- Notes:
  - body extracted cleanly
  - commentary on Karpathy's workflow
  - visible link resolves to attached media
- Next action:
  - use as a secondary explanatory source; inspect media if useful

### zodchiii — 8 Claude Code Hooks
- Source: [zodchiii-post-2040000216456143002](../source-notes/zodchiii-post-2040000216456143002.md)
- Raw: [raw/x/2026-04-03-zodchiii-2040000216456143002.md](../../raw/x/2026-04-03-zodchiii-2040000216456143002.md)
- Status: `captured`
- Notes:
  - title extracted cleanly
  - likely media-heavy post with hook details
- Next action:
  - revisit media if the hook breakdown becomes important

### Dhairya — vectorless RAG
- Source: [dkare1009-post-2039665922185589044](../source-notes/dkare1009-post-2039665922185589044.md)
- Raw: [raw/x/2026-04-03-dkare1009-2039665922185589044.md](../../raw/x/2026-04-03-dkare1009-2039665922185589044.md)
- Status: `captured`
- Notes:
  - body extracted cleanly
  - highly relevant to non-vector knowledge workflows
  - visible link resolves to attached media
- Next action:
  - use as supporting evidence for the project's low-infra retrieval direction

### JUMPERZ — multi-agent Karpathy pattern
- Source: [jumperz-post-2040166448492900356](../source-notes/jumperz-post-2040166448492900356.md)
- Raw: [raw/x/2026-04-03-jumperz-2040166448492900356.md](../../raw/x/2026-04-03-jumperz-2040166448492900356.md)
- Status: `summarized`
- Notes:
  - body extracted cleanly
  - highly relevant multi-agent adaptation of Karpathy pattern
  - attached media reviewed; general agent architecture concepts recovered
- Next action:
  - use as conceptual support, not a direct implementation blueprint

### code_rams — Karpathy follow-up / idea files
- Source: [code-rams-post-2040483611732791535](../source-notes/code-rams-post-2040483611732791535.md)
- Raw: [raw/x/2026-04-04-code-rams-2040483611732791535.md](../../raw/x/2026-04-04-code-rams-2040483611732791535.md)
- Status: `captured`
- Notes:
  - body extracted cleanly
  - strong support for idea files / schema files as first-class artifacts
- Next action:
  - use as supporting reference when evolving schema-driven workflow

### explorax_ / m0h — 20 Powerful Agentic-Skills
- Source: [explorax-m0h-post-2039269234253934811](../source-notes/explorax-m0h-post-2039269234253934811.md)
- Raw: [raw/x/2026-04-03-explorax-m0h-2039269234253934811.md](../../raw/x/2026-04-03-explorax-m0h-2039269234253934811.md)
- Status: `captured`
- Notes:
  - source identity/title recovered cleanly from tab state
  - deeper media/body still not extracted
- Next action:
  - retry extraction later if this source becomes a priority

### Sharbel example post
- Source: [sharbel-post-2039376686362333340](../source-notes/sharbel-post-2039376686362333340.md)
- Raw: [raw/x/2026-04-03-sharbel-2039376686362333340.md](../../raw/x/2026-04-03-sharbel-2039376686362333340.md)
- Status: `captured`
- Notes:
  - Created as a shell because public extraction failed
- Next action:
  - Enrich with pasted text, screenshot, or successful clip

## Image / conceptual references

### AI Agents Cheat Sheet screenshot
- Source note: [ai-agents-cheat-sheet-screenshot](../source-notes/ai-agents-cheat-sheet-screenshot.md)
- Raw: [raw/images/ai-agents-cheat-sheet-screenshot-2026-04-03.md](../../raw/images/ai-agents-cheat-sheet-screenshot-2026-04-03.md)
- Status: `summarized`
- Role:
  - conceptual architecture reference for agents, tools, orchestration, protocols, and patterns

## Primary artifacts

### breferrari/obsidian-mind
- Source note: [breferrari-obsidian-mind](../source-notes/breferrari-obsidian-mind.md)
- Raw: [raw/repos/breferrari-obsidian-mind.md](../../raw/repos/breferrari-obsidian-mind.md)
- Status: `summarized`
- Role:
  - strong inspiration for Obsidian + LLM memory workflows

### google/langextract
- Source note: [google-langextract](../source-notes/google-langextract.md)
- Raw: [raw/repos/google-langextract.md](../../raw/repos/google-langextract.md)
- Status: `summarized`
- Role:
  - optional structured-extraction component for difficult ingest cases

### chenglou/pretext
- Source note: [chenglou-pretext](../source-notes/chenglou-pretext.md)
- Raw: [raw/repos/chenglou-pretext.md](../../raw/repos/chenglou-pretext.md)
- Status: `resolved`
- Role:
  - possible output/demo/presentation layer candidate

### karpathy/llm-wiki gist
- Source note: [karpathy-llm-wiki-gist](../source-notes/karpathy-llm-wiki-gist.md)
- Raw: [raw/repos/karpathy-llm-wiki-gist.md](../../raw/repos/karpathy-llm-wiki-gist.md)
- Status: `summarized`
- Role:
  - foundational primary source for the project architecture and workflow

## Workflow notes

Observed pattern for X/Twitter sources:
1. capture the post as a social source
2. resolve visible links
3. distinguish:
   - external primary artifact
   - attached media
   - thread-only framing
4. create separate source notes for primary artifacts
5. leave social posts as discovery/framing sources

## Next capture checklist

For each new X source:
- capture post text
- record visible links
- resolve t.co targets
- identify whether each target is:
  - external artifact
  - media attachment
  - internal X link
- create or update linked primary artifact notes
