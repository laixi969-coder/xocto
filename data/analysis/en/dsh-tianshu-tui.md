---
slug: dsh-tianshu-tui
name: dsh-tianshu-tui
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

Beyond giving DSH a terminal UI, this is a plugin that pushes "write the test before the code" and an evidence gate into the agent workflow — the agent must prove what it did before it can continue.

## Who built it

Individual developer huiliyi37 (same GitHub handle). The rendering core evolves from the author's own "Tianshu-Tui" agent (Apache-2.0). Repo created 2026-08-13, Apache-2.0, 36 commits in this repo; the author reports 250+ commits across the harness-side collaboration (8/10-8/13). Current version 0.1.1-rc.6.

_Read: this does not look like a casual plugin — it looks like the author of a standalone agent project (Tianshu) porting his stack onto DSH to ride its momentum. The evidence: TDD and the evidence gate depend on a whole family of his own packages (dsh-evidence-gate, dsh-agent-router, dsh-fs-snapshot, dsh-memory...), and half the README is a showcase for his own ecosystem._

## What it actually does

- **TDD-driven workflow** → modifies the official harness so tests come before implementation
- **Evidence gate** → dsh-evidence-gate enforces RED-first verification: a duty state machine, edit/verify counters, a TDD gate (enforce mode), probe suggestions with cooldown, and an L2 final review gate
- **Failure routing** → dsh-agent-router predicts step failure from turn history and routes work, including verification subagent scheduling
- **Full session workspace in the terminal** → `/fork` explore branches, `/rewind` rollback (session truncation plus optional file rollback), `/export` Markdown transcripts, `/steer` mid-turn redirection
- **Images end-to-end** → clipboard paste, inline rendering via terminal graphics protocols, and a vision bridge that converts images to descriptions when the text-only main model cannot see them
- **Reasoning visualization** → think-channel streaming, collapsed into compact lines in scroll regions, Ctrl+O to expand in place
- **Harness-side companions** → model aliases, session/file snapshots, memory, semantic index, git services (integrations of DSH official ecosystem packages)

**What it deliberately does not do**: the UI is a pure presentation layer — it registers no prompts, tools, or context surfaces; all agent state comes from the session event stream, and user input becomes ordinary log messages. The author separates "display" from "control" cleanly, which also means the TDD/evidence-gate value is entirely delivered by his companion packages; the plugin body is just a shell.

## What old behavior it replaces

It replaces the implicit assumption that "the agent will test." With Claude Code/Aider-class agents, the quality process runs through a human: you tell it "run the tests when you're done," and the agent writes all the code first, runs a token test at the end, fixes reds, or sometimes runs nothing. Developers with strict TDD discipline (red-green-refactor) have to execute that discipline by hand in their IDE — the agent does not help, it gets in the way.

tianshu turns that manual TDD discipline into an enforced agent process: tests first (RED), the evidence gate only allows the next step on a passing verification (GREEN), failures get routed, probes are suggested, and an L2 review sits at the end. It replaces the quality gate that an engineer used to hold by hand inside an agent workflow.

## Business model

**Not disclosed.** Apache-2.0, free on npm, no pricing, no hosting, no sponsorship.

_Read: what the author is really selling (if anything) is a "trustworthy harness" methodology and the package family behind it. The plugin is the entrance; the package family is the asset. This "open-source entrance plus a full suite" play is common among individual developers; monetization later means either a paid hosted version or nothing at all._

## Hard numbers

- **103 stars / 4 forks / 2 open issues** (GitHub API, 2026-08-14)
- Created 2026-08-13, 36 commits; author reports 250+ across the collaboration (8/10-8/13)
- Current 0.1.1-rc.6, baseline aligned with official 0.1.0-rc.6
- app.ts is a ~2.2k-line monolith (the author admits it needs splitting)
- Image compression: 1568px long-edge cap, three-stage JPEG 0.82→0.55 degradation, 16 image tests
- Users, team: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author built Tianshu first, so the pain is his own; but the "personal project riding DSH" motive is obvious |
| Product insight | "Turning test discipline from a human's will into an agent's enforced process" is a real direction; the evidence-gate idea transfers |
| Execution quality | Dense commits and many companion packages, but a fair share of the 36 commits is self-ecosystem display; independently verifiable value is limited |
| Timing | TDD's value for agents is genuinely contested — most people want agents fast, not slowed down by process; the audience is small |

## The call

**Right direction, and the most self-referential project in this ecosystem.**

An evidence gate (prove before proceed) is a real mechanism for making agent output trustworthy, especially where "the agent touched code and must be rollback-able." But delivering it depends on a family of packages only the author maintains, and the README's story is "my harness full suite, moved to DSH." For ecosystem users, this is the highest-migration-cost, least-trustable plugin of the six.

**Transferable rule: when you gate agents, gate on evidence, not on trust.** The evidence gate demands verifiable output (passing tests, file diffs), not the model's self-report of "I'm done." Any product selling agent labor should swap "the model says it's done" for "must attach reproducible evidence" — it visibly reduces disputes.

**Its relation to dsh-TUI**: both are DSH terminal UIs, but positioned completely differently — dsh-TUI is "Claude Code's experience ported to DSH" (experience gap-filling, for CLI geeks, 619 stars); tianshu is "quality process embedded in the terminal" (workflow reengineering, for people who want evidence, 103 stars). Audience, pitch, and stars differ by an order of magnitude.

## What to watch next

① Real-project usage of the evidence gate in enforce mode — is the gate on by default, and what is the false-block rate
② Whether the companion packages (evidence-gate/router) get adopted outside this repo — ecosystem adoption is the real evidence
③ Whether the author splits app.ts and publishes standalone docs — a 2.2k-line monolith is a maintenance risk

## What you can take from it

**Product logic**: if your agent product is accountable for results (writing code, editing docs, producing reports), copy the minimum viable evidence gate: the model must attach verifiable evidence when it delivers — test output, file diffs, data source references — and anything without evidence is marked "incomplete." That is an order of magnitude more reliable than letting the model self-assess "done." Run observe mode first to record the false-block rate, then decide on enforcement.

**Positioning language**: none. The README is a Chinese engineering notebook.

**Pricing structure**: none. Not disclosed.

## Verdict

**Unproven.** The evidence-gate mechanism is worth stealing for anyone building agent products, but this plugin body (a render layer plus a personal package family) has not demonstrated standalone value. Take the mechanism; you can skip installing the plugin.
