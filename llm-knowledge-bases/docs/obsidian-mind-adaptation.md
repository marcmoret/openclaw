# Obsidian Mind Adaptation Note

Comparison between `breferrari/obsidian-mind` and the current `llm-knowledge-bases` project.

## What `obsidian-mind` gets very right

### 1. Treats the vault as an operational system
It does not act like the vault is just a pile of notes. It treats the vault as something with:
- a governing file
- maintenance workflows
- commands/hooks
- review discipline

### 2. Takes durable markdown memory seriously
It assumes useful knowledge should live in the vault, not vanish into chat or session state.

### 3. Strong lifecycle / maintenance mindset
It includes explicit maintenance and review flows instead of assuming the vault will stay coherent automatically.

### 4. Clear human-facing home/dashboard concept
A vault should have a clear entry point, not just a directory tree.

## Where this project differs

This project is:
- more research- and source-ingest-oriented
- more focused on `raw/ -> wiki/ -> outputs/`
- less about being a general assistant memory vault
- more about knowledge compilation from external sources

So this project should **borrow patterns**, not clone structure.

## Best patterns to borrow

### Borrow now

#### A. Add a human-facing wiki home/dashboard
The project has `wiki/index.md`, but it could benefit from a more human-facing landing page.

#### B. Make maintenance more visible
`wiki/log.md`, lint passes, and promotion rules exist, but they are still somewhat hidden. A maintenance/readme dashboard would help.

#### C. Treat governing files as first-class
This is already happening with `WIKI-SCHEMA.md`, but the project should lean into it more confidently.

### Borrow later

#### D. More explicit maintenance rituals
Potential future additions:
- periodic review page
- backlog of weak notes
- ingest queue / promotion queue

#### E. More structured home views
Potential future additions:
- recently updated notes
- foundational notes list
- current focus topics

## Strong conclusion

Do not copy `obsidian-mind` literally.
Do borrow:
- seriousness about operational files
- human-facing vault navigation
- maintenance discipline
- durable markdown-first memory

## Recommended immediate adaptations

1. Add a `wiki/home.md` dashboard
2. Link operational files more clearly from the home page
3. Make the distinction clearer between:
   - foundational sources
   - core concepts
   - operational references
   - recent reports
