# Safe to Commit

Recommended files/folders to keep in the repo if the repo root is `C:\Users\marco\.openclaw\workspace`.

## Assistant / workspace behavior
- `AGENTS.md`
- `SOUL.md`
- `USER.md` *(only if you are comfortable versioning it)*
- `TASKS.md`
- `TOOLS.md` *(only if it does not contain sensitive infra details)*

## Knowledge-base project
- `llm-knowledge-bases/README.md`
- `llm-knowledge-bases/WIKI-SCHEMA.md`
- `llm-knowledge-bases/docs/`
- `llm-knowledge-bases/prompts/`
- `llm-knowledge-bases/tools/`
- `llm-knowledge-bases/wiki/`
- `llm-knowledge-bases/outputs/` *(except large generated media if you prefer to ignore it)*
- `llm-knowledge-bases/raw/` *(selectively; see note below)*

## Raw-source note
`raw/` can be committed, but be selective.

Safer things to commit:
- markdown source shells
- repo source notes
- article clips you are comfortable storing publicly/private in the repo
- screenshot metadata markdown notes

Be cautious with:
- copyrighted PDFs
- large binary datasets
- personal/private source material
- bulky image dumps

## Best default
If unsure, commit:
- markdown
- schema/docs/prompts
- wiki notes
- reports

And be selective about large raw binaries.
