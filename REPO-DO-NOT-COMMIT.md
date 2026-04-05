# Do Not Commit

Things you should usually keep out of the repo.

## Personal memory / private continuity
- `memory/`
- `MEMORY.md`

## Secrets / auth / tokens
- any API keys
- auth tokens
- `.env`-style secrets
- exported session cookies
- private browser/session material

## Transient runtime noise
- `media/`
- temporary screenshots unless intentionally curated
- logs
- caches
- generated temp files

## Sensitive local notes
Be careful with:
- `TOOLS.md` if it contains hostnames, SSH aliases, camera names, or other infrastructure details
- `USER.md` if you do not want personal preferences/notes versioned

## Heavy or legally messy source material
Avoid committing unless you explicitly mean to:
- copyrighted PDFs
- large binary datasets
- random downloaded image dumps
- anything scraped or collected that you are unsure about sharing/storing in git

## Rule of thumb
If the file is:
- secret
- personal
- noisy
- auto-generated
- huge
- or legally questionable

keep it out of the repo.
