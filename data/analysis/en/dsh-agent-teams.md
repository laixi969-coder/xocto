---
slug: dsh-agent-teams
name: dsh-agent-teams
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A "team" for DeepSeek Harness: one natural-language command spins up a multi-agent team, tasks are
split across roles, members communicate directly without relaying through the lead, and the Web GUI
shows the whole team's activity tree in real time.

## Who built it

NanmiCoder, a single maintainer, MIT license, 40 commits. The project moved from a private beta in
the dsh-external organization to a public repository; latest commit 2026-08-14.

_Read: porting the AgentTeams semantics Claude Code already validated into DSH is smart leverage —
not inventing a new concept, but moving a proven pattern into a new ecosystem. That is exactly what
a plugin author should be doing._

## What it actually does

- **One command to spin up a team** → "Use AgentTeams to research X" launches a multi-agent team to
  complete the goal
- **Core semantics ported from Claude Code's AgentTeams** → create team (lead = current session
  agent) → recruit members (continuable subagents) → split tasks and declare dependencies → members
  message each other directly (mailbox delivery plus wake-ups, no lead relay)
- **9 `agent_teams_*` tools** → create team, add/remove members, create/claim/update tasks (with
  dependency declarations), send messages, query status, delete team
- **Members are "durable continuable subagents"** → file-based team state plus JSONL mailboxes
  under `<workspace>/.agent-teams/`
- **Web GUI tree panel** → Team Lead → members → tasks visualized in real time, mirroring the
  workflow-run UI pipeline
- **Ships a `dsh-plugin-development` skill** → per the open Agent Skills spec, installed via
  `npx skills add`
- **Passed a real DeepSeek-V4-Flash end-to-end test** → team creation/member/task/report/cleanup,
  full pipeline

## What old behavior it replaces

Multi-agent collaboration in DSH used to be manual orchestration: the user opens several sessions,
shuffles context around by hand, and aggregates results — effectively assembling an ad-hoc team out
of loose processes every time, with no state, no supervision, and no teardown.

It replaces "loose orchestration" by making the team a first-class citizen — a protocol for
creating a team, persistent state for members, declared task dependencies, and teardown (delete
after reporting, archive retained). The three most expensive parts of the old workflow — context
handoff, progress tracking, result aggregation — move from human labor to protocol.

The key difference from the Claude Code original is decentralization: members communicate via
mailboxes directly with no lead relay, removing the single-hub bottleneck. That is an improvement
learned from the original's downside, not a copy.

## Business model

**Not disclosed.** MIT open source, free to install (direct GitHub source, no npm package or
credentials required).

_Read: classic ecosystem-plugin logic — add value to the platform and count on the platform
growing the ecosystem so some traffic flows back. If the DSH ecosystem materializes, this kind of
plugin may get absorbed by the official side or become an ecosystem benchmark; currently there is
no commercial signal at all._

## Hard numbers

- **168 stars / 14 forks / 1 open issue**, 40 commits
- 9 `agent_teams_*` tools; requires Node.js ^22.19 or >=24 and pnpm 11
- Passed a real DeepSeek-V4-Flash end-to-end verification
- Team size and usage data: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A solo developer porting Claude Code's mature semantics into DSH; the leverage play fits |
| Product insight | Making "team" a governable protocol (file-based state, mailbox messaging, task dependencies) rather than one-off orchestration is the right direction |
| Execution quality | 40 commits, complete docs (usage, four-layer verification guide, development guide), real e2e tests. Above the DSH-ecosystem average |
| Timing | Actively developed from day one of DSH's release; early positioning. Its value rides entirely on DSH adoption speed |

## The call

**A specimen of "good plugin": the problem is well chosen (multi-agent collaboration genuinely is
hard in DSH), the leverage is well placed (semantics Claude Code already validated), and the
engineering is solid (docs, e2e, file-based state).** But it is not a standalone product — without
DSH it does not even have a runtime. Its fate equals the fate of the DSH ecosystem.

The lesson for practitioners: this is a textbook case of porting a validated pattern into a new
ecosystem at the right moment. A plugin's value is not technical originality; it is the product of
ecosystem vacancy times pattern validation.

## What to watch next

① Whether it gets listed in the dsh-external official catalog or recommended by DeepSeek — official
recognition is the signal of an ecosystem benchmark
② Whether it stays actively maintained after DSH ships a stable release — many ecosystem plugins
die at the moment the platform graduates
③ Whether enterprise users appear publicly — multi-agent teams are the most common ask from
enterprise agent platforms

## What you can take from it

**Product logic**: when building an ecosystem plugin or tool, "leverage a validated pattern" is the
highest-efficiency route — do not invent new concepts; translate semantics the leading products
already validated into the new platform, and fix the original's flaws (here, the lead-relay
bottleneck). The selection criterion: pattern validation times ecosystem vacancy.

**Engineering practice**: put collaboration state in files (JSONL mailboxes plus file-based team
state) instead of locking it in memory or a database — inspectable, recoverable, auditable. This
"state-to-files" decision transfers to any collaboration system that needs to be observable.

**Positioning language**: none.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** It is one of the better-engineered plugins in the DSH ecosystem and the
ready-made answer to "multi-agent teams" on DSH. But remember its value is entirely contingent on
DSH — under the DSH bet it is a component worth noting; under a standalone-product bet it is not.
