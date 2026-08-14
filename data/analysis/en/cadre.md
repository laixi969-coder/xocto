---
slug: cadre
name: cadre
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A local-first kanban control plane that pulls multiple coding agents' terminal sessions onto one
board: assign tasks, run them in parallel, and gate every outcome behind human approval before
code touches a branch.

## Who built it

l-crispr (a founder comment signs as Lucas Mota), one person shipping a local-first desktop app.
The site carries six interactive step-by-step guides — more care than most products in this space.

_Read: at this depth, it is almost certain the author is a heavy user of his own problem. But the
two HN questions — how parallel agents editing the same files conflict, and whether you can see
which sessions are running what — went unanswered, which says it hasn't reached a
community-response, iteration-pressure stage._

## What it actually does

- **Kanban task orchestration** → tasks carry descriptions, acceptance criteria, images and tags,
  move through custom columns, route to a chosen agent per column
- **Detects installed CLIs** → Claude Code, Codex, Grok, OpenCode, OpenAI-compatible endpoints;
  no new account needed
- **Two execution modes** → reuse a CLI login (no new billing) or BYOK (key stored in the OS
  keyring); tokens are billed by your provider, **zero token markup**
- **Parallel with isolation** → tasks run in isolated Git worktrees, up to 16 concurrent runs on
  the Team tier
- **Four human gates** → questions, plans, diffs, commands, each with its context attached,
  approve/reject on one decision surface
- **Rust backend enforces command policy** → not front-end hints, back-end policy
- **Local-first** → offline by default, no account; sync is opt-in per workspace for team work;
  repos and credentials stay local

**What it deliberately does not do**: no automatic push or merge, no token brokering, no taking
over the models you already subscribe to.

## What old behavior it replaces

The typical chaos of teams using coding agents: developers open several terminal sessions, each
running an agent, with chat history scattered everywhere. Over time three questions become
unanswerable — which session is running what, how far along it is, who approved it. Agent output
lands on a branch without anyone reviewing the diff; parallel agents editing the same repo collide
only at merge time.

cadre replaces the default of "terminal session as workflow" with a visible queue and approval
gates. The two HN comments are precisely the core pains: one asks whether parallel agents editing
the same files get conflict detection; the other asks "which sessions are running what" — which
is the problem itself.

## Business model

Local desktop free; Pro/Team online workspaces paid (cross-device sync, workspace invites,
collaboration); pricing not public ("Contact us").

_Read: "free local, paid collaboration" is the standard local-first path; the hard stretch is
between free individual use and paid team buying. Zero token markup is deliberate restraint, and
it rules out profiting on the spread._

## Hard numbers

- **HN: 5 points, 2 comments** (2026-08-13), Show HN
- Supports 4 agent families + OpenAI-compatible (Claude Code, Codex, Grok, OpenCode)
- Up to 16 concurrent runs on Team, 1:1 isolated worktree
- Desktop on Windows / macOS / Linux
- Users, downloads, pricing: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A solo full-stack build to this depth is almost certainly a self-use pain product |
| Product insight | "Terminal sessions are not a workflow" is right, and the four gates match real engineering habits |
| Execution quality | Rust backend, OS keyring, three platforms, six interactive guides — completion beyond what 5 points suggests |
| Timing | Half a step early — most teams are still at "one agent works"; managing several is next-stage |

## The call

**A local-first "engineering board for coding agents," and the smartest move is admitting it
should not touch the model layer.**

No token markup, no takeover of your model subscriptions, no agent of its own — only orchestration
and approval. That restraint is the same product philosophy as numbat's monitor-only default:
don't grab authority until you've been trusted.

**The transferable rule: an orchestration tool's boundary should be drawn at decision, not
execution.** cadre's entire value sits in the gates — what to ask, how to approve plans, who
reviews diffs, who clears commands — while execution is fully outsourced to the user's existing
CLIs. That makes switching cheap, and it also makes the moat shallow: anyone can copy it.

**The risk is in the same place.** 5 points means almost no one has seen it. The orchestration
layer is the most crowded lane (Kiro Crew and a row of agent-orchestration platforms are all in
it), and a solo project without feedback usually dies first — especially when there's no hard
technical problem like worktree conflict detection to differentiate on, just UX.

## What to watch next

① Whether the two HN questions (worktree conflict detection, session visibility) become product
features and get answered in docs
② When online-workspace pricing numbers go public — "Contact us" usually means nobody has bought yet
③ Whether public cases or user logs appear — evidence of real team usage

## What you can take from it

**Product logic**: if you build a tool, copy "the boundary sits at the decision layer" — let users
keep their existing execution stack (models, CLIs, subscriptions) and take only the decision
actions (approvals, queue, visibility). Lower switching cost means an easier foot in the door.

**Positioning language**: "4 approval gates, not 400 prompts" is a rare good comparison line;
keep it.

**Pricing structure**: free local + paid collaboration, zero token markup. Pricing undisclosed;
nothing to dissect yet.

## Verdict

**Right direction, too few people.** An orchestration control plane occupies a real need, but a
5-point launch means it hasn't been seen, and the lane is extremely crowded. Note it and come back
once it solves a hard problem like worktree conflict detection or lands its first users.
