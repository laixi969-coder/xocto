---
slug: git-knife
name: Git-knife
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A desktop app that edits git commit metadata like a spreadsheet — commit messages, author name/email, author date, committer date, all editable, with bulk find-and-replace. A scalpel GUI for operating on git history.

## Who built it

A personal project by HN user YonathanTesfaye (GitHub: TheRealYT), repo `TheRealYT/git-knife`, a Tauri desktop app (Rust backend, TypeScript frontend), created August 10, 2026, posted to HN as a Show HN the next day. v0.2.0, self-described MVP.

_Read: indie developer + a problem he hit himself; this kind of tool is usually "pain first, product second." The README's thoroughness shows the author has thought through the niche's boundaries — what it does and deliberately does not do, both written out._

## What it actually does

- **Edit commit metadata** → message, author name/email, committer name/email, author date, committer date — every field editable
- **Bulk find-and-replace** → literal or regex replacement across messages, author/committer names and emails ("move every commit from one email to another"), with preview and live match counts
- **Never changes file contents** → it does not reimplement git; it shells out to the system git CLI and rebuilds commits with `git commit-tree`, reusing each commit's original tree, so file contents are provably never changed
- **Branch browsing without checkout** → view/edit any local branch by its ref, no checkout, your working tree stays untouched
- **Safety net** → automatic backup ref before every rewrite plus one-click restore; warns when a rewrite touches pushed history; signed-commit aware — badges them, warns a rewrite strips signatures, and can re-sign with your key
- **Auditable transparency** → each rewrite leaves a disclosed note on a separate notes ref saying "this repo was edited by git-knife," invisible in a normal `git log` but fully discoverable, toggleable off

**What it deliberately does not do**: no reorder/squash/drop yet (planned, unimplemented), merge commits are locked, and it never pushes — pushing is always your explicit step, and it only touches local branches.

## What old behavior it replaces

Editing git history used to mean choosing between two broken options:

**GUIs like GitKraken, Sublime Merge, Fork, lazygit** — good at rewording and reordering, but they treat commit **dates** as effectively immutable, do not expose committer dates, and cannot bulk-edit author identity. Want to change a date in a GUI? Nothing works.

**CLIs like `git filter-repo`, git rebase environment tricks, `git commit-tree`** — can rewrite every field, but all terminal: no interface, fiddly syntax, error-prone, and one command rewrites the whole repo in ways ordinary people are afraid to touch.

git-knife sits in the intersection: **a GUI that can edit all the fields.** It wraps the "can do it" CLI power in a "looks nice" GUI shell, and makes the high-risk act of rewriting history reversible with backup refs, warnings, and notes markers.

## Business model

**None.** Indie open-source project, no pricing, no sponsorship, no hosted service. The README also **declares no open-source license** (the GitHub API's license field is null).

_Read: the missing license is more notable than the missing business model. For a tool, "can I use it in my project" depends on the license, and the author has not picked one — either an oversight or undecided. It will not stop stars, but it will stop enterprise adoption; anyone wanting to run it in production hesitates at that empty field._

## Hard numbers

- **294 stars, 9 forks.** Created 2026-08-10, just over four days old
- HN Show HN: **143 points / 88 comments per the pool, 165 / 101 per Algolia**
- v0.2.0, MVP; TypeScript + Tauri (Rust); three-platform installers via GitHub Actions
- Real use cases named in the comments: reconstructing history (rebuilding the original Tim Berners-Lee browser repo with commit dates aligned), preserving history while splitting repos, fixing wrong attribution on merged open-source PRs, repairing git config an AI agent mangled
- Downloads, users: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author was clearly bitten by "can't change the date"; the README comparison table is the product thinking itself |
| Product insight | Precisely identified the vacuum — "what can rewrite has no GUI, what has a GUI cannot rewrite" — and solved signing plus backup along the way |
| Execution quality | commit-tree rebuild + backup refs + notes markers; the safety design is thought through, not a demo |
| Timing | Right now. AI agents are generating commits at scale, and mangled git configs and wrong attribution are multiplying |

## The call

**A textbook sample of "polish the dirty job nobody wants," and it happens to catch the new pain of the AI era.**

**The transferable rule: find the corner where everyone assumes "it can't be done" — it is usually just "nobody did it well."** Most developers default to "can't change git dates" or "not worth it," yet the comments prove real demand has always been there: simonw listed three scenarios (history reconstruction, repo splits, attribution fixes), and someone had been hunting for this exact tool for nearly a decade ("store laws in a git repo, each commit is a bill; we need to insert history without resetting the dates of later commits"). The fields abandoned by mainstream tools are where new tools grow.

**The new pain it catches**: after AI agents write code, git configs get mangled, attribution goes wrong, and commit dates no longer match the real workflow — a recently emerged class of problems. git-knife's "bulk-fix author emails" lands right on it.

**The name does real work.** Git-knife — a scalpel — and the comments picked up the metaphor themselves: "we generally don't want to cut people open, but when surgery is needed, a sharp knife is useful." A name that makes users instantly understand a tool is dangerous but valuable and must be used carefully beats any feature description.

**Risks**: first, no license, which blocks enterprise adoption; second, it handles high-risk "pushed history" operations where one misuse breaks a team's collaboration, a trust bar that is very high; third, it currently stops at "edit metadata," and commenters already want it extended into a full rebase UI (drag-to-reorder, file-to-commit reassignment) — if the author does not take these on, a stronger competitor will.

## What to watch next

① Whether stars cross 1,000 in three months — a measure of how big the "abandoned corner" demand really is
② Whether a license appears — the switch from personal tool to production tool
③ Whether a full rebase UI ships (drag reorder / squash / reassignment) — whether it stays narrow or grows toward mainstream

## What you can take from it

**Product logic**: any operation "everyone assumes is impossible" is worth validating — often nobody just did it well. List the fields/capabilities mainstream tools deliberately abandon; that is the whitespace. git-knife's comparison matrix (tools × capabilities) is a research method worth copying: put your position precisely on the cell where no one else can check the box.

**Positioning language**: naming beats copy. One word — "Knife" — makes users understand the danger and the value in three seconds and generates its own discussion. For small, dangerous tools, a name that honestly admits the danger beats any feature description.

**Pricing structure**: none. No license, no pricing; personal-project status.

## Verdict

**Worth watching.** Precise positioning, solid safety design, and it happens to catch the AI-era commit chaos — but no license, no business model, and still parked at "edit metadata." Watch star growth and feature expansion to see whether the scalpel grows into a full tool.
