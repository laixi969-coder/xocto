---
slug: dsh-tui
name: dsh-TUI
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

The gap-filler for DSH having no terminal interface — a Claude Code-style full-screen interactive terminal ported to DeepSeek Harness: pixel whale, live status line, Esc rollback, context progress bar, installed with one npm command.

## Who built it

Author ccch1mneyyy (same GitHub handle), with collaborators T-Auto, CikeSeven, and even some AI-assisted commits. Repo created 2026-08-13 (version history goes back to an 8/5 beta period), MIT (changed from another license on 8/14), npm package `dsh-cc-tui`, now 0.4.0, 117 commits. Featured by the DeepSeek Harness official WeChat account as a "selected plugin of beta users."

_Read: the only one of the six with an official endorsement. The author openly calls it a gap-filler, explicitly feeding on the official team not building a TUI; the official feature listing is the team admitting the hole exists and will not be filled right now._

## What it actually does

- **Full-screen terminal interaction** → Claude Code-style interface: / command menu, tool-call cards, markdown tables/code highlighting, @ file references, Shift+Enter multiline, full-text search
- **Pixel whale top bar** → a hand-drawn 40×25 pixel sprite with a startup animation (blink → spout → tail wag), auto-collapses on narrow terminals (<64 columns)
- **Live working status line** → 28 animated indicators, context-usage warnings (≥80% yellow, ≥95% red), end-of-turn stats
- **Double-Esc rollback** → roll the conversation back to any historical message via the official fork service, edit and resend
- **Context progress bar + TPS meter** → five-segment colored progress with live readout, streaming TPS gauge and sparkline, speed color coding (≥50 green / ≥20 yellow / <20 red)
- **Streaming thought expansion** → thinking blocks expand as generated, auto-collapse at turn end, Ctrl+O for full text
- **Four agent presets + themes** → standard/code/minimal/cordis, light/dark/dark-ansi palettes plus custom JSON themes, hot-swap via /theme
- **i18n Chinese/English** → hot-swap via /lang with OS locale auto-detection; supports the official MCP client

**What it deliberately does not do**: no DSH core changes; fork/resume/compact all go through official services, and uninstalling restores everything. Its dependence on official mechanisms is deep — that is its safety declaration and also its ceiling.

## What old behavior it replaces

At release, DSH removed TUI from its repo (the commit reads literally `cleanup: remove TUI package and legacy dsh entrypoints`) and made Web UI the primary onboarding path. So using DSH meant one road only: open a browser to localhost:3080. For CLI geeks who live in the terminal, that is a downgrade — with Claude Code and Codex they get full-screen terminals with a status line, command menu, context usage, and a speed meter at a glance.

dsh-TUI replaces the behavior of "using DSH requires opening a browser." It ports the Claude Code terminal experience wholesale, so people habituated to the terminal can use DSH without changing their habits. It does not replace an old tool; it replaces the friction of DSH forcing users into a different interface paradigm.

## Business model

**Not disclosed.** MIT, free on npm, no pricing, no hosting, no sponsorship.

_Read: a pure traffic play. The exposure from the official WeChat feature is this plugin's only "business model." It competes with dsh-tianshu-tui for the same TUI slot, but its currency is experience, not process — and experience-layer plugins are the easiest for the official team to absorb, which is its biggest structural risk._

## Hard numbers

- **619 stars / 26 forks / 29 open issues** (GitHub API, 2026-08-14; the highest issue count in this batch)
- Created 2026-08-13, 117 commits, v0.4.0, npm package `dsh-cc-tui` installs without a build
- 148 Chinese strings migrated into an i18n dictionary (12 files)
- 28 status indicators, 4 presets, 3 built-in themes
- Featured by the DeepSeek Harness official WeChat account
- Users, downloads: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author calls himself a geek building for CLI users; the audience is himself |
| Product insight | Treats Claude Code's "terminal experience" as a product, not a shell skin; detail density is high (rollback, TPS, warning colors) |
| Execution quality | Pure plugin mount, official mechanisms first, clean engineering; but 29 open issues means a big surface that never gets fully fixed |
| Timing | Perfectly hits the official-no-TUI window; but the official team removed TUI and pivoted to Web UI, suggesting they may believe a terminal interface is unnecessary — the window may close by the team's own hand |

## The call

**It sells not features but "no change of habit" — the most user-psychology-aware plugin of the six.**

A CLI geek's migration cost is not "can't learn a new tool"; it is "changing the working posture." Every dsh-TUI design choice (pixel whale, status line, Esc rollback, progress bar) does the same thing: turn DSH into "the tool I already know how to use." Double-Esc rollback is especially smart — it invents no new mechanism, it just wraps the official fork service in the universally understood semantics of "undo."

**Transferable rule: adapting to an old user's habits beats adding features for new users.** If your product is technically better but interacts differently from the mainstream tool, the fastest acquisition move is a "posture compatibility layer" — let users pretend they are still using their old tool while the foundation underneath has already been swapped.

**The risk is symmetric**: experience layers have the shallowest moats. If the official team ever adds a TUI back (it removed one before, so it has the capability), the pixel whale will not save dsh-TUI. 619 stars are the dividend of this window, not a wall.

## What to watch next

① Whether the official team re-includes a TUI — its single most lethal variable
② Whether open issues fall from the current 29 — a plugin that never finishes fixing bleeds users
③ Whether star/download growth tracks DSH's own growth — it is a gap-filler; it grows only when DSH grows

## What you can take from it

**Product logic**: if your product wants the "replacement for an existing tool" slot, build a posture compatibility layer: map every operation onto semantics users already have (undo, rollback, command menu) instead of teaching new concepts. The "double-Esc = rollback" wrapper turns a high-level operation like forking a session into a zero-learning-cost gesture.

**Positioning language**: borrowable. The README declares its audience with "dedicated to CLI geeks" and takes a humble stance with "a gap-filler" — translating "I copied Claude Code" into "I gave DSH what it was missing." That reframing works well in the Chinese developer community.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** The highest-traffic, most psychologically precise plugin of the six — and the shallowest moat. It validates the "posture compatibility layer" as an acquisition mechanism and exposes the fate of experience-layer plugins in a platform ecosystem: when the platform moves, the skin is wasted.
