---
slug: dsh-web-ui
name: dsh-web-ui
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A plugin-plus-skin collection store for the DSH Web UI — task board, git graph, right-side panel, SSH, remote mobile UI, pet, live token stats, plus 8 skins, all installed with one command, and a skin center where you can try before you apply.

## Who built it

Individual developer zhu1090093659 (same GitHub handle). Repo created 2026-08-12 (the day before the official launch), 237 commits, plugins published under the `@linxin666` npm scope. Skin showcase at gallery.dsh-market.com. The license is a red flag: the README claims BSD-3-Clause, but the GitHub API license field is null (no standard LICENSE file detected) — upstream media also called it out as "no license file, legally unusable."

_Read: the highest-starred plugin in the ecosystem (1184), and the most "personally operated" — license uncertain, skins are gimmicks, npm scope doesn't match the GitHub handle. The biggest traffic and the worst compliance sitting on the same project makes it the clearest "community dividend vs engineering discipline" split in this batch._

## What it actually does

- **Task board** → five-column status (planned/todo/in progress/done/failed), cron scheduled execution, agent-session execution with review jump
- **Git graph** → branch lanes and commit-history visualization
- **Right-side panel** → file tree, multi-format preview (markdown/HTML/PDF/Office), SCM changes panel (stage/unstage/discard), drag files into the input box — head-on overlap with dsh-better-sidebar
- **SSH** → web terminal, SFTP transfer, port forwarding, cluster execution
- **Remote mobile UI** → QR pairing, SSE live messages (auto-degrades to polling when tunnels don't pass SSE)
- **Pet** → a whale-girl companion with state-based animations, feeding, growth system
- **Live token stats** → TPS, LLM latency, context usage, cache hit rate
- **8 skins** → Windows XP (Luna), Minecraft, QQ2008, Tonghuashun, Trading Terminal (hooks into market data feeds), Blue Fantasy, Whale Song, Dragon Heir — all with "try before you apply"

**What it deliberately does not do**: no agent core capabilities at all — only the Web UI's periphery and appearance. The task board is its most genuinely functional part (cron scheduling is a real need); most of the rest is gimmicks and cosmetics.

## What old behavior it replaces

The official DSH Web UI shipped thin (testers said "missing file management, preview, and such"). Users needing task management went to external tools (Trello/Linear-style boards); checking git history meant opening a terminal to run `git log --graph` or installing a GUI; watching token spend meant digging through the API dashboard afterward.

dsh-web-ui replaces that fragmentation of "one agent product plus three or four external tools." It stuffs the task board, git graph, token stats, SSH, and phone remote control into the Web UI, installed with one command. Its killer feature is the aggregate package `dsh-web-ui-all` — users don't decide which to install; install everything and be done. The old behavior it replaces is manually assembling peripheral tools around an agent workflow.

## Business model

**Not disclosed.** Plugins are free (README claims BSD-3-Clause, but the GitHub API shows no license file; legal status is in doubt). No pricing, no hosting, no sponsorship.

_Read: a pure influence project. Skin-class features have near-zero willingness to pay in the developer community; its value is the position of "first stop in the DSH Web UI ecosystem" — a position that currently has neither commercial monetization nor a compliance foundation. Of the six, it has the least commercial upside and the strongest ecosystem placement._

## Hard numbers

- **1184 stars / 48 forks / 23 open issues** (GitHub API, 2026-08-14)
- Created 2026-08-12, 237 commits, aggregate package at 0.1.10/0.1.11
- 9 function plugins + 8 skins, npm scope `@linxin666`
- Skin showcase at gallery.dsh-market.com, with try/revert/apply
- License: README claims BSD-3-Clause, but GitHub API license field is null — legal status uncertain
- Users, downloads, team: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | An active DSH beta user with real needs, but heavy "personal gimmick" fingerprints on the operation |
| Product insight | Task-board cron, SSH, and the aggregate package are three real need points; the "try before you apply" skin center is a smart UX |
| Execution quality | 237 commits show activity; but the unclear license and mismatched npm scope/handle make it the weakest on engineering/compliance discipline |
| Timing | Opened the repo the day before the official launch and absorbed the full first wave of traffic; but skin/gimmick value decays as the official UI matures |

## The call

**The most successful at ecosystem placement of the six, and the least stable in product value.**

Its success is not features, it's position: at official launch the Web UI was empty, and this project bundled every peripheral need into one install, becoming the de facto "first stop for DSH Web UI." The task board's cron scheduling and SSH are real functions; the rest (pet, skins) is the ecosystem's "living texture" — but those gimmicks are exactly what contributed most to community spread.

**Transferable rule: for platform products, the community's first stop is rarely the deepest feature set; it is the one that is "installed all at once and fun."** The aggregate package lowers decision cost (no picking which to install), and gimmicks provide the fuel for spread. If you run platform ecosystem operations, "leaving one official gap for the community's first stop" works better than building it yourself.

**Its overlap with dsh-better-sidebar**: the right-side panel (file tree, preview, SCM) collides head-on. better-sidebar is more engineering-driven (lazy loading, extension interface, 520 stars); dsh-web-ui is more aggregate (1184 stars). The overlap shows that DSH's "right sidebar" is the most crowded lane in the ecosystem — and that the official gap is the one with the most traffic value.

**Its biggest risk is compliance**: a null license field means enterprise users won't touch it, which is fatal for a plugin that wants long-term value. Skin-class content will also depreciate fast as the official UI iterates.

## What to watch next

① Whether a standard LICENSE file appears — a null license is a hard blocker at the enterprise gate
② Whether aggregate-package install counts (npm downloads) can be found — stars looking good doesn't mean anyone installed it
③ Whether the functional plugins (task board/SSH) keep iterating — gimmicks go stale, functions stay

## What you can take from it

**Product logic**: building the "first stop" plugin for an ecosystem product, copy two mechanisms: the aggregate package (install everything at once; decide for the user) and "try before you apply" (skin/template features must preview instantly and roll back completely — push the choice cost to zero).

**Positioning language**: borrowable. The skin naming uses one-word-era triggers — "Windows XP (Luna) / QQ2008 / Tonghuashun" — a nostalgia hook for older developers and a novelty hook for younger ones; both groups click in.

**Pricing structure**: none. Not disclosed, and the license status is in doubt — the anti-pattern: an open-source project that never adds a LICENSE effectively shuts the door on enterprise users.

## Verdict

**Worth watching.** Strongest ecosystem placement, smallest commercial imagination. It proves "aggregate package + gimmick content" is a working recipe for a cold-start ecosystem first stop, and demonstrates the counter-example of a plugin that can't go far without a license. Watch it to learn "position," not "product."
