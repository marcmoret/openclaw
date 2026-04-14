---
name: x-to-obsidian-clipper
description: Capture X/Twitter posts into Obsidian through the already-configured Obsidian Web Clipper in the managed OpenClaw browser profile. Use when Marco sends an X/Twitter post URL to analyze, save, or clip into Obsidian. This skill is specifically for the workflow: open the post in the managed `openclaw` browser, focus the exact tab, then trigger the clipper via OS-level `Alt+Shift+O` because pure OpenClaw browser `press` was not sufficient for the extension shortcut.
---

# X to Obsidian Clipper

Use the managed `openclaw` browser profile and the OS-level clipper shortcut.

## Workflow

1. Open the X post in the managed `openclaw` profile.
2. Wait briefly for the page to load.
3. Focus the exact returned tab id.
4. Trigger the clipper with the OS-level helper:
   - `C:\Users\marco\.openclaw\workspace\toolbox\send-alt-shift-o.ps1`
5. Report success honestly.

## Preferred helper

Prefer this wrapper for the full sequence:

- `C:\Users\marco\.openclaw\workspace\toolbox\x-to-obsidian-clip.ps1 -Url <x-post-url>`

It:
- opens the post in the managed browser
- focuses the exact returned tab
- triggers the OS-level clipper shortcut

## Important notes

- Do **not** rely on pure `openclaw browser press "Alt+Shift+O"` for this workflow. It did not trigger the extension reliably.
- Do **not** rely on direct `chrome-extension://...` navigation through `tabs/open`; OpenClaw blocks that protocol.
- Some `openclaw browser ...` CLI calls may hang or end with SIGKILL in the wrapper even when the underlying action succeeded. Treat direct browser state and user confirmation as higher-trust signals.
- The best confirmation is user-visible clipper success or downstream evidence in Obsidian.

## Friction that is not a blocker

- X may render with partial logged-out chrome while still exposing the post content.
- Wrapper-level CLI hangs do not necessarily mean browser failure.
- Focus matters. If needed, re-focus the exact tab before running the OS-level helper.

## If the clipper does not fire

1. Confirm the target X tab is frontmost/focused.
2. Retry the OS-level helper once.
3. If it still fails, say so plainly and do not bluff that the note was clipped.
