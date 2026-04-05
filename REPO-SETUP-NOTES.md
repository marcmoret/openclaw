# Repo Setup Notes

Recommended repo root:
- `C:\Users\marco\.openclaw\workspace`

Why:
- includes assistant behavior files
- includes `llm-knowledge-bases/`
- excludes the noisier `.openclaw` root above it

## Recommended first commit set
Suggested to include first:
- `AGENTS.md`
- `SOUL.md`
- `TASKS.md`
- `llm-knowledge-bases/`

Optional:
- `USER.md`
- `TOOLS.md`

## Recommended next step
Before first push, quickly review:
- `.gitignore`
- `REPO-SAFE-TO-COMMIT.md`
- `REPO-DO-NOT-COMMIT.md`

Then sanity-check what `git status` wants to add.

If `git status` shows anything surprising, do not blindly commit it.
