# Browser Recovery State Snapshot

Captured before clean-baseline recovery.

## Goal
Rebuild OpenClaw browser control for the managed `openclaw` profile from a clean baseline, then restore reliable tweet capture through Marco's logged-in X session.

## Current symptoms
- `GET /?profile=openclaw` can report healthy state (`running:true`, `cdpReady:true`, `cdpHttp:true`).
- `GET /tabs?profile=openclaw` still returns `{"running":false,"tabs":[]}`.
- `tabs/open` and `snapshot` fail with `TypeError: fetch failed`.
- Direct probes to `http://127.0.0.1:18800/json/version` and `/json/list` can refuse connections or time out even when browser status claims health.

## What was already changed
### Config
- `C:\Users\marco\.openclaw\openclaw.json`
  - browser enabled
  - default profile set to `openclaw`
  - managed `openclaw` profile uses CDP port `18800`
  - `user` remains existing-session attach profile
  - browser SSRF policy allowances were added for loopback/private local browser access
  - broken plugins were disabled/denied earlier (`codex`, `comfy`, `qwen`, `vydra`)

### Runtime bundle files locally edited during debugging
- `C:\Users\marco\AppData\Roaming\npm\node_modules\openclaw\dist\server-context-a2_X6e09.js`
- `C:\Users\marco\AppData\Roaming\npm\node_modules\openclaw\dist\chrome-D1wjC_HZ.js`
- `C:\Users\marco\AppData\Roaming\npm\node_modules\openclaw\dist\cdp.helpers-Cx11b16A.js`

### Restart tooling
- `C:\Users\marco\.openclaw\workspace\toolbox\restart-openclaw-gateway-simple.ps1`
- `C:\Users\marco\.openclaw\workspace\toolbox\restart-openclaw-gateway-simple.bat`
- current preference is Terminal-based restart flow with task reminder preserved

## Key diagnosis before reset
- Early failures were real SSRF/policy issues.
- Later failures shifted to browser/CDP lifecycle and false-health reporting.
- `/start` can return success even when real CDP tab/list operations are not working.
- Patch-on-disk versus live-runtime behavior became hard to trust, which is why clean-baseline recovery is now preferred.

## Recovery direction
1. Return runtime to clean baseline.
2. Reapply only minimal browser config.
3. Prove CDP health directly.
4. Prove Google open/tab/snapshot.
5. Only then retry X/tweet flow.
