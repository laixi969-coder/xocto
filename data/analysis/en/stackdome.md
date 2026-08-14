---
slug: stackdome
name: Stackdome
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An open-source, self-hostable deployment platform that describes your whole application
(services + databases + storage) in one Stackfile and ships it as a unit. The human-facing
Canvas/CLI and the agent-facing skills operate on the same application model — an open-source,
self-hostable alternative to Railway.

## Who built it

The Stackdome team (lead author akshaysasidrn). Main repo is AGPL-3.0; the ecosystem also
includes stackdome-cli (MIT), stackdome-skills (Apache-2.0), and cluster-agent (a Kubernetes
operator). The repository was created 2025-05-20 and carries roughly 1,470 commits.

_Read: over a year of sustained commits says this is serious work, not a Show HN one-day stand.
But only 20 stars in the same period says marketing and community never took off — the
"engineering first, cold-start failed" shape is common, and the hard distinction is between
"nobody knows" and "nobody needs."_

## What it actually does

- **One app = one Stackfile** → services, databases, storage, networking, and observability
  described once; all three surfaces (agent / Canvas / CLI) read and write the same model
- **Git push to live** → builds in-cluster, lands images in a built-in registry, and releases
  roll back as a whole stack, not one deployment at a time
- **Managed Postgres** → HA, automated backups, point-in-time recovery
- **Unlimited preview environments** → a full stack per branch, so coding agents can spin up
  many in parallel
- **Bring your own compute** → connect your own K8s clusters (v1.27+, EKS/GKE/AKS/k3s) or a
  bare VPS with 2 vCPU / 4 GB
- **Agent as a first-class citizen** → stackdome-skills plus agents.stackdome.com let an agent
  create, deploy, and debug from a prompt; an MCP server is in progress
- **Every change is a diff** → the UI shows what moved, from what to what, and a release counts
  only after it is proven live and healthy

## What old behavior it replaces

People who want to self-host and not hand their lifeblood to Vercel/Railway have had a set of
awkward roads.

The first is hosted PaaS — Railway/Render/Heroku. Convenient, but your infrastructure logic is
locked in someone else's house, costs climb nonlinearly with usage, and compliance and
privatization are off the table.

The second is building your own PaaS: Coolify (Docker, single box) or stitching K8s + Helm +
CI + registry + a Postgres operator yourself. Coolify cannot carry multi-service orchestration
or team scenarios; the K8s road needs a dedicated platform engineer just to get it running, and
what you assemble may still not match hosted-PaaS ergonomics.

The third is a new problem of the agent era: letting a coding agent deploy for you means the
agent operates a pile of hand-stitched infrastructure with no unified model — it cannot see
what is in the stack and has to guess.

Stackdome replaces the union of roads two and three: a self-hosted PaaS that works out of the
box, plus a programmatically operable unified application model for agents. That is what
distinguishes it from Coolify and raw K8s — every entry point writes the same model, so humans
and agents can hand work back and forth.

## Business model

Two tracks: an official cloud (alpha stage, capacity-limited, ephemeral environments) plus
free self-hosting (AGPL-3.0). Cloud pricing is not disclosed.

_Read: the Supabase/Coolify pattern — open source for trust and distribution, cloud for revenue.
But the cloud is still in alpha with "capacity-limited" written on the homepage, which means the
business model itself has not started running. The AGPL choice is also clearly defensive: keep a
hyperscaler from reselling the code as hosted competition._

## Hard numbers

- **20 stars, 0 forks** (main repo), created 2025-05-20, roughly 1,470 commits
- HN: 21 points, 6 comments (around 2026-08-13)
- Ecosystem repos: cli (MIT), skills (Apache-2.0), cluster-agent (K8s operator)
- Supports K8s v1.27+ or a single VPS with 2 vCPU / 4 GB
- Cloud users and paid revenue: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Unknown, but 1,470 commits across a full stack (Go backend, React frontend, K8s operator, agent skills) says an all-round builder |
| Product insight | Catches two real gaps: self-hosted PaaS lacks a modern K8s-layer implementation, and agent deployment needs a unified programmable application model |
| Execution quality | Complete architecture (API + operator + CLI + skills); the stackfile + diff + rollback design is more rigorous than most early PaaS |
| Timing | Good. The self-hosting wave is at full strength, and "agent deploys for you" is a brand-new need |

## The call

**A product at the intersection of two trends — the self-hosting wave and agent delivery. The
direction is almost certainly right, but the execution evidence is thin.** Self-hosted PaaS
demand was proven by Coolify; a missing modern K8s-layer implementation is real; and letting
agents deploy directly is becoming a need. Putting the three together is a smart position.

**The transferable rule: when two trends converge, build the intersection product — it gains
momentum more easily than betting a single curve.** But beware: the ceiling of an intersection
product is the minimum of its two curves. Self-hosting users and agent-first users are two
different populations; serving both at once risks being shallow on each.

**The biggest question is execution**: 14 months, 20 stars. Either the author built quietly and
skipped marketing (the README, docs, and architecture look real), or the market is simply no
longer excited by "another self-hosted PaaS." One more signal worth noting: many commits carry
Claude as an author — which fits the "build with agents" narrative, but also raises the question
of whether this is a one-person side project and how long it can be sustained.

**Its differentiation bet**: agents operate the whole path from prompt to live, with human-
reviewable diffs and rollbacks. That design is right, because the trust problem of agent
deployment ("what if the agent broke something") can only be answered with "reviewable and
rollbackable." But it still needs to prove that humans will actually use it.

## What to watch next

① Pricing and GA timing at the end of the cloud alpha — whether the leap from free alpha to
  paid actually happens cleanly
② Whether stars and community grow within three months — 1,470 commits of engineering plus
  marketing would show up fast in stars; no growth means nobody wants it
③ Whether the MCP server and agent integrations get adopted in real agent workflows (a public
  case study beats any advertisement)

## What you can take from it

**Product logic**: when building an operation surface for agents, define the "unified
application model" first — all entry points (human UI, CLI, agent) read and write the same
model, then add features. That lets agents and humans hand one workflow back and forth, and it
is the key architecture decision for agent-era products.

**Positioning language**: "Ship from your agent, the CLI, or the Canvas. On our cloud or
yours." — compressing three entry points and two deployment modes into one verifiable sentence
is stronger than a feature list.

**Pricing structure**: the cloud + self-host dual track is the standard shape; the notable
detail is AGPL — using AGPL on a self-hosted product to protect the hosted business is becoming
the default pattern.

## Verdict

**Worth watching.** The position sits at the right intersection of three trends and the
architecture stands up, but 14 months and 20 stars support no optimistic conclusion. This is the
most worth-revisiting project in this batch — because its bet (agent deployment + self-hosting)
is either zero or very large.
