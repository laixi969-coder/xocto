---
slug: approving
name: approving
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An open-source, self-hostable platform that turns coding agents into visible, reviewable,
recoverable delivery workflows: agents run in real Docker sandboxes, swap backends per need
(Cursor / Claude Code / CodeBuddy / Trae), pause for human approval at critical nodes,
exchange structured artifacts, and finally open the PR/MR themselves.

## Who built it

Solo-led by cocofhu. MIT license, repo created 2026-07-24, 77 stars / 3 forks. Backend in Go
(FSM engine, API, SQLite, artifact MCP, scheduling, audit), frontend in Vue 3 + Vue Flow (the
orchestration canvas), sandboxing via Docker plus a custom sandbox-gateway. ~723 commits,
currently at 0.2.1-beta. The commit history includes AgentBot and Cursor commits — the author
is literally building this with agents.

_Read: a tool whose job is "make agent delivery trustworthy" is being built by agents itself.
That self-certification chain is informal but oddly consistent. 77 stars says people who looked
nodded; it has not been validated yet._

## What it actually does

- **Visual FSM orchestration** → draw agent/human-gate/rollback nodes on a canvas; edges
  define success, failure, and rollback paths
- **Human-in-the-loop gates** → pause at critical nodes so a human can approve, reject, or
  request changes from structured artifacts
- **Real Docker sandboxes** → isolated execution via sandbox-gateway; each agent picks its own
  backend, so one workflow can mix different agents
- **Artifact contracts + MCP** → every run gets its own artifact MCP and token; agents exchange
  structured outputs via write_artifact / set_* / node_complete, isolated per run
- **Git delivery** → GitHub/GitLab/SSH credentials injected into the sandbox; auto-opens
  PRs/MRs
- **Self-hostable** → one-repo Docker Compose bring-up, images published on GHCR, no local
  build needed
- **Typical workflow** → Clarify → Research → Proposal → human approval → Plan → Implement →
  Test → Review → human confirmation → PR/MR

## What old behavior it replaces

Handing delivery to a coding agent used to default to post-hoc review: the agent finishes, opens
a PR, and a human eyeballs it — while what the agent changed and why was often a black box, so
the reviewer had to re-read the whole diff to judge it.

Approving replaces that chain in two shapes. First, it moves review earlier: approval happens
before the code exists — the human approves the Proposal and the plan, not the aftermath.
Second, it makes rollback an explicit path in the graph instead of a human detective job.

It also replaces a more basic behavior: agent tools were siloed (Claude Code's way, Codex's
way), with no platform layer to orchestrate different agents into one gated flow. Approving
wants to be that orchestration layer.

_Read: "approve before code is written" is the right design. Reviewing a finished PR is the
most expensive form of review — the work is done, overturning means redoing. Approving a plan
is a far cheaper checkpoint._

## Business model

**Not disclosed.** MIT open source, self-hostable, no cloud service, no pricing page. The
homepage shows team-shaped features (parallel-sprints, a PM that chats) but nothing is priced.

_Read: the same classic script as its peers — open source for distribution, a future cloud for
revenue. But cloud, enterprise tier, and pricing are all absent, so the model has not started._

## Hard numbers

- **77 stars / 3 forks.** Repo created 2026-07-24, ~723 commits, at 0.2.1-beta
- Four agent backends supported: Cursor, Claude Code, CodeBuddy, Trae
- Go backend + Vue 3 frontend + custom sandbox-gateway; Docker Compose self-host with
  multi-GB sandbox images on first pull
- Users and revenue: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Background unknown, but building a "manage agents" platform with agents is unusually self-consistent tool-scenario fit |
| Product insight | Two real problems: approval should move to the plan stage, and rollback should be an explicit path, not post-hoc forensics |
| Execution quality | Complete architecture (Go backend + canvas frontend + sandbox gateway + artifact MCP + audit), 0.2.1-beta shows fast iteration |
| Timing | Right. Coding agents already run; "how do I trust what they deliver" is exactly the next gate for enterprise adoption |

## The call

**This is the trust layer for agent delivery, positioned at the right moment, but not yet
validated.**

Once single coding agents work, the enterprise question becomes "how do I trust what it
changed." Approving answers part of it: make agent workflows visible, approvable, and
recoverable — and move the human checkpoint from "review after it's done" to "review the plan
before it starts."

**The transferable rule: where you place the approval point in a process decides its cost.**
Reviewing a plan is an order of magnitude cheaper than reviewing a result — a result is
already committed, overturning means starting over; a plan is text, changing it takes minutes.
Deciding "at which step does a human say yes" is the highest-leverage design decision in any
automation.

**Its weakness is the orchestration layer itself.** Four backends, each with its own
acpBackend; the platform manages sandboxes and credentials. Adopting it requires willingness
to self-host, pull multi-GB images, and maintain your own sandbox infrastructure. That makes
it a tool for technical teams, not a sales-driven product.

**Where it sits vs peers**: AgentGate and Lelu build the permission/policy layer (approving
agent actions); Approving builds the delivery-flow layer (turning agents into gated
pipelines). The former is closer to a security tool, the latter to CI/CD for agents. Both
directions are valid; Approving walks the dev-delivery lane.

## What to watch next

① Whether stars pass 300 in three months and any company publicly says it runs this — the line
between "watched" and "trusted"
② Whether a hosted tier or team pricing appears — the first step from free self-host to a
business model
③ Whether the backend list keeps growing as new agent tools ship — an orchestration layer
that lags new agents is dead

## What you can take from it

**Product logic**: when designing human-machine workflows, decide where the human approval
point sits before deciding features. Copy this ordering: approve the plan (cheap) → execute →
review the result (expensive). Back plan approval with structured artifacts so the approver
has something concrete to read, and back result review with explicit rollback paths.

**Positioning language**: "Agents run in real Docker sandboxes, exchange structured artifacts,
and pause for human Approve at critical nodes." — one sentence covering sandbox, artifacts, and
approval; more reassuring to a technical buyer than an abstract capability list.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching, but early.** Right position, right design (approval moved forward), fast
iteration — this is the closest thing in this batch to a shippable form of the "agent
governance" thesis. But 77 stars and zero business model mean it hasn't crossed from tool to
product. Revisit in three months against the checks above.
