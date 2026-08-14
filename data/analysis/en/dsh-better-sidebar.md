---
slug: dsh-better-sidebar
name: DSH-better-sidebar
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Not making DSH's chat box bigger — packing the whole dev environment into its sidebar: file tree, editor, terminal, Git, background tasks, embedded browser, all in one plugin, so you stop switching windows while the agent works.

## Who built it

Core author Menghuan1918 of the omdsh-dev org (same GitHub handle). Repo created 2026-08-07, a week before DSH's public launch on 8/13 — a community author working during the private beta. MIT, TypeScript, npm package `dsh-better-sidebar`, now v0.10.3, 112 commits.

_Read: betting on a specific UI-gap plugin a week before the official release means either beta access or a calculated guess that the official team would leave this hole open. The guess landed — at launch the official right sidebar was empty (testers wrote "the right sidebar isn't built yet, no Codex-style embedded browser, file management, or preview"), and this plugin filled it._

## What it actually does

- **Files & editing** → lazy directory tree (root = session cwd), CodeMirror 6 editing with Ctrl/Cmd+S atomic save, inline preview for images/Markdown/HTML/PDF/Word/Excel/PPT
- **Real terminal** → xterm.js + node-pty, 3 UI per session, can inject 8 `terminal_*` tools for the agent to use
- **Git panel** → real diff, VS Code-style diff tabs, right-click stage/discard/commit/revert
- **Background tasks** → main-session agent topology, live tool-call polling, force kill
- **Bottom panel + split panes** → a second workbench, drag tabs to split/merge, mobile layout below 768px
- **Third-party extension point** → exposes a `ctx.betterSidebar` service; other plugins can register new tabs and file viewers (7 built-in tabs, 9 viewers)
- **Lazy loading** → ~325KB core at startup; Univer (~20MB) only pulled when a .xlsx is opened, xterm when a terminal is opened

**What it deliberately does not do**: no git push/pull/fetch (local operations only), and the embedded browser refuses localhost and other machine-local addresses by default (temporarily unlockable). The restraint on scope is explicit — this is a workbench, not another IDE shell.

## What old behavior it replaces

At launch DSH was Web UI-first with an empty right sidebar. The real DSH workflow became: agent conversation in a browser tab → flip to an external IDE/editor to review file changes → open a terminal to run git by hand → paste results back. One task, three windows, state held in the human's head.

better-sidebar replaces that human glue. Files, editing, terminal, git, and task state all live in the sidebar, so while the agent works you watch results, review diffs, and roll back in one surface. It does not replace a tool; it replaces the behavior of bouncing between the agent and the dev environment.

## Business model

**Not disclosed.** MIT, free on npm, no pricing page, no hosted service, no sponsorship channel.

_Read: this category follows ecosystem rules — free to build influence, money lives elsewhere (own model service, hosted harness, or absorption by the official team). The DSH plugin ecosystem is days old; the standard bet for early authors is attaching your name to the periphery of the hottest repo. Monetization is a later chapter._

## Hard numbers

- **520 stars / 21 forks / 12 open issues** (GitHub API, 2026-08-14)
- Created 2026-08-07, 112 commits, v0.10.3, effectively daily releases
- ~325KB core at startup; Office/PPT preview deps lazy-loaded (~20MB)
- 7 built-in tabs, 9 file viewers, 8 `terminal_*` tools injected
- Team size, user count, downloads: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author is himself a heavy DSH user (started during beta); the pain is genuine |
| Product insight | Spotted the "agent interaction should become a full dev environment" gap the official team left open, and kept a third-party extension hook |
| Execution quality | host/client dual-half structure, lazy loading, sandboxed iframes, per-session state persistence — product-grade engineering, not a demo |
| Timing | Perfect landing: mature on launch day, absorbing first-wave traffic; but it feeds on the official ecosystem's growth and dies with it |

## The call

**A gap-filler that separates "what an IDE owns" from "what a plugin should do" more cleanly than anyone else here.**

Its biggest move is not features but boundaries: files, editing, terminal, git belong to the workbench and it builds them itself; new tabs and viewers are open to third-party registration. That split is what separates it from later sidebar plugins — it does not fight the official team for territory, it lays the foundation the ecosystem builds on.

**Transferable rule: for dev-facing AI products, ship v1 with fewer features but real extension points.** The official team left the right sidebar empty and the community filled it within a week — for a platform, "leaving a visible gap" is the cheapest ecosystem-launch mechanism there is.

**The ceiling is equally clear**: it is a DSH plugin; it lives only while DSH lives. If an official release fills the sidebar (the team has history — it removed its own TUI and made Web UI the primary path), the core value gets absorbed. 520 stars prove first-mover advantage, not moat.

## What to watch next

① Whether the official Web UI ships its own sidebar within 2-3 months — if it does, differentiation shrinks to the extension interface
② Whether third-party tabs/viewers grow — evidence the "foundation" positioning actually holds
③ Whether release cadence keeps pace with official rc iterations — a plugin one step behind a moving rc target stops installing

## What you can take from it

**Product logic**: if you build a companion environment for a chat-first AI product, do not build a full IDE. Ship a sidebar workbench with lazy loading — keep the core light (325KB-class) and pull heavy deps (Office preview, terminal emulation) only when the user actually opens that file type. That lets you claim "full workbench" without crushing first paint. And ship third-party panel registration as a v1 capability so the ecosystem grows features for you.

**Positioning language**: none. The Chinese README is a feature list; nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** The most product-grade sidebar plugin in this ecosystem — solid engineering, precise timing — but it bets on DSH's long-term health and owns no moat of its own. Watch it less than the pattern behind it: platform leaves a gap, plugin fills it, traffic goes to the plugin. That ecosystem dynamic will repeat across the agent era.
