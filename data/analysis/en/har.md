---
slug: har
name: HAR
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An open-source framework for running multiple coding agents on the same repository: per-agent isolated workspaces, deterministic validation gates, and verifiable proof, replacing the scattered README/CLAUDE.md/CI configuration.

## Who built it

Antoine Frau (scaled agentic coding workflows at his own company for a year, hit the walls, open-sourced the fix) and Karim Traiaia. Team name: os-factory. It ships as an npm package (CLI + MCP server) plus the Mission Control local dashboard.

_Read: the authors were forced out of real production pain — "multi-agent concurrency is untrustworthy." Every item in their problem list (no standard for run/verify, agents colliding, re-verify-by-hand, platform lock-in) is concrete._

## What it actually does

- **Single in-repo contract** → one machine-readable .har/ contract replaces the drift-prone scatter of README + CLAUDE.md + Cursor rules + CI config; Claude Code, Cursor, Codex, or any MCP agent reads the same thing
- **Isolation** → each task gets its own git worktree with its own branch, ports, and database; nothing is shared with the main checkout or another agent's slot
- **Deterministic validation gates** → the project's real checks run through a fixed pipeline; the result binds to the exact code that passed, and an unverified tree cannot land
- **Verifiable proof** → every run leaves logs, artifacts, and a validated tree hash; a reviewer inspects the evidence instead of trusting the agent's self-report
- **Mission Control** → local dashboard for all repos, worktrees, runs, validations, and artifacts in one place
- **Drift detection** → har env maintain diffs the installed harness against current templates and flags drift before it causes a silent failure
- **Plugins** → verification bundles like Playwright, or any command you already run

## What old behavior it replaces

Multi-agent concurrent coding used to look like this: every agent starts its own dev server (ports and databases collide), verification is "the agent said it tested it," and switching platforms (Claude Code to Cursor, say) means rebuilding the whole verification setup.

HAR standardizes three things: **"how this repo runs and verifies" moves from scattered docs to one contract; concurrent runs move from trampling each other to isolated slots; trust moves from agent self-report to reviewable evidence.** It doesn't replace a single tool; it replaces the human-dispatch segment of multi-agent collaboration.

## Business model

**Not disclosed.** Open source; core CLI/MCP is free. os-factory is a company entity, most likely monetizing via a hosted tier or enterprise support, but no pricing information exists today.

_Read: the agent-harness category is heating up fast — in the same week this launched, DeepSeek open-sourced its own Harness v0.1 (MIT, "everything is a plugin," Model+Harness=Agent, led by Cui Tianyi). They are not the same thing: HAR manages concurrency and validation of coding agents; DeepSeek Harness is a plugin-based agent runtime. But the names collide, and both are fighting for the "harness" mindshare._

## Hard numbers

- GitHub (os-factory/har): **65 stars / 8 forks**, created 2026-06-28
- launch page: 1 review, 5.0
- npm package: @osfactory/har, installed via npm install -g
- Team: two people (per PH interactions)
- Users, ARR: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author spent a year in the pain inside his own company's real workflows |
| Product insight | Caught the trust problem — validation bound to exact code plus reviewable evidence. That's the lifeblood of multi-agent work |
| Execution quality | README, quickstart, docs tree, and a plugin system; engineering-complete. But no large-scale validation yet |
| Timing | Excellent — "trustworthy agent concurrency" is the #1 engineering problem of 2026, and big labs just entered to validate the direction |

## The call

**It grabs the most expensive problem of the multi-agent era: trust.** With a single agent you can read its output yourself; with a fleet running in parallel you can't review each one, so you have to trust an evidence system. HAR's "deterministic validation + tree hash + evidence chain" moves software engineering's reproducible-build philosophy onto agent orchestration. The direction is right.

**Its biggest risk is not quality; it's the lane getting plowed over.** In the same week, DeepSeek Harness v0.1 went open source with a dedicated team; Claude Code's own hooks/subagents and every agent platform's orchestration layer are closing in. "Harness" is becoming a crowded word. HAR's moat is "agent-agnostic + in-repo contract" — if your verification infra lives in some vendor's cloud, switching means rebuilding; HAR keeps the contract in the repo, and that's its only argument against both platform lock-in and platform absorption.

**What it lacks** is real adoption evidence: 65 stars, one review, no public "a company runs real fleets on this" case. It has made the rational case; now it has to prove someone survives a real project with it.

## What to watch next

① Whether stars pass 500 in three months and whether a company publicly adopts it
② Whether it's still being discussed after DeepSeek Harness and peers spread — or pushed out of mindshare
③ Plugin and Mission Control activity — whether anyone writes third-party plugins for it

## What you can take from it

**Product logic**: when designing agent orchestration or automation, make the trust mechanism a first-class citizen: verification results must bind to a hash of the exact input (code, data), not to an agent's self-report. This principle transfers to any "AI acts autonomously but a human is accountable" scenario.

**Engineering practice**: fight platform lock-in with an in-repo contract — put configuration, validation, and standards in the codebase itself rather than in a vendor dashboard. It's both a technical choice and a commercial moat.

**Positioning language**: "a reviewer checks the evidence instead of trusting the self-report" — one sentence that separates the product from a glossed-over agent command.

## Verdict

**Worth watching, but unproven.** The problem selection is sharp, the direction is right, and the timing is excellent, but adoption evidence is zero and the lane is filling with big players. Its winning position — in-repo contract plus vendor neutrality — is the spot the big labs haven't occupied. Validate against the three checks above in three months.
