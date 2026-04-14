# OpenClaw Browser Recovery Plan

Goal: rebuild OpenClaw browser control for the managed `openclaw` profile from a clean baseline, then restore tweet capture through Marco's logged-in X session.

## Principles

- Stop stacking ad-hoc `node_modules` patches unless a clean baseline still fails.
- Prefer a clean, minimal, reproducible browser setup over clever local surgery.
- Prove each layer before moving to the next one.
- Treat Google/open-tab success as the prerequisite for X/tweet capture.
- Keep the task-reminder and restart workflow intact throughout.

## Step-by-step plan

### Phase 1: Preserve current state
1. Save current findings and decisions.
2. Preserve the current `openclaw.json` and restart helper behavior.
3. Record which runtime files were locally patched so they can be restored or compared.

### Phase 2: Return OpenClaw runtime to a clean baseline
1. Reinstall or refresh the installed OpenClaw package cleanly.
2. Remove local JS bundle surgery from the active runtime.
3. Confirm the running gateway is using the clean installed dist tree.

### Phase 3: Rebuild the browser config minimally
1. Keep only the minimum browser config needed:
   - `browser.enabled = true`
   - `browser.defaultProfile = "openclaw"`
   - managed `openclaw` profile with explicit CDP port
   - `user` existing-session attach profile if still desired
2. Reapply only clearly justified browser SSRF settings if needed.
3. Restart using the approved helper workflow.

### Phase 4: Prove the managed browser path from zero
1. Start the `openclaw` profile.
2. Verify `http://127.0.0.1:18800/json/version` responds.
3. Verify `http://127.0.0.1:18800/json/list` responds.
4. Verify browser status and `/profiles` agree with direct CDP checks.

### Phase 5: Prove one simple browser action
1. Open `https://www.google.com` through OpenClaw browser control.
2. Verify the tab appears in `/tabs` or CDP tab listing.
3. Verify snapshot works.
4. Only if these succeed, mark core browser control as restored.

### Phase 6: Restore the real X workflow
1. Open the target tweet through the managed `openclaw` profile.
2. Verify tab visibility and snapshot/page content.
3. Capture the tweet honestly with provenance.
4. Resume knowledge-base ingest once browser control is trustworthy.

## If the clean baseline still fails
Only then patch, in this order:
1. browser SSRF policy/config issues
2. browser status/reporting mismatches
3. launch/readiness contract bugs
4. tab/snapshot action bugs

Each patch should be small, justified, and re-tested immediately.

## Success criteria
- `/start` succeeds only when CDP is genuinely reachable.
- `/tabs` returns real tabs.
- `/snapshot` works.
- Google open works.
- X tweet open works through Marco's logged-in session.
