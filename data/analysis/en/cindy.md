---
slug: cindy
name: cindy
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A single workspace that folds the walled-off coding agents — Claude Code, Codex, Pi — into one
agent: switch models and harnesses mid-task without losing memory, skills, or context, and
steer the same agent from desktop, phone, or chat.

## Who built it

An open-source project under the GitHub org `makecindy`, backed by X.D. Network (Huang Yimeng,
co-founder of TapTap). Announced July 22, 2026 at the TapTap Developer Salon (TDW 2026). Source
is Apache-2.0 TypeScript, a pnpm monorepo shipping desktop and mobile clients.

_Read: a gaming platform building a general-purpose coding agent client is not trying to make a
tool — it is trying to own an entry point. TapTap's first half released 5,002 playable games,
over 4,000 made with AI; supply has jumped an order of magnitude and they are betting Cindy is
the "AI work environment" where that production happens._

## What it actually does

- **One workspace, many harnesses** → Claude Code, Codex, and Pi are connected, a native
  harness is in the works; you can switch mid-task while workspace, memory, skills, and tools
  stay continuous
- **Multi-agent orchestration** → one task splits into three roles — a planner, parallel
  workers, an independent reviewer — passing the baton across harnesses
- **Out of the box** → no-login local mode, 20+ built-in tools, four ways to plug in (managed
  service / an existing Coding Plan / your own API key / local models), all working directly
- **Remote control from anywhere** → steer the computer from your phone, @ it in Slack or
  Feishu to delegate, schedule recurring jobs that report back to chat
- **Trust controls** → isolated workspaces, line-by-line review, rollback checkpoints, no full
  project upload by default, real-time cost visibility

**What it deliberately does not do**: build its own LLM (it gates GPT/Claude/Grok/Gemini/
DeepSeek/Kimi/GLM/Qwen instead), and it will not make you pay twice for a model you already pay for.

## What old behavior it replaces

Using coding agents used to mean one isolated environment per agent: Claude Code in one
terminal, Codex in another, each with its own workspace and memory, so switching models meant
starting over. Remote oversight from a phone was basically unavailable.

Cindy replaces three costs: the **switching cost** between agents (was: teardown and rebuild;
now: same workspace, flip at will), the **setup cost** (was: configure keys and environment;
now: no-login local run), and the **"must be at the keyboard" constraint** (now: dispatch and
approve from a phone or chat thread).

## Business model

The client is free (Apache-2.0) and the stated logic is "bring the subscriptions you already
own, no double billing." Revenue comes from:

- **PLUS, from $20/month**: managed model service, a unified gateway across GPT/Claude/Grok/
  Gemini/DeepSeek/Kimi/GLM/Qwen, monthly plans save 20%, with higher SUPER/ULTRA tiers
- **TEAM (coming soon)**: SSO, centralized config, credit limits, team skill distribution
- **ENTERPRISE (contact sales)**: gateway self-hosted in your VPC, audit logs, cost attribution

_Read: the three-layer "free software + managed service + enterprise control plane" is the
route n8n and Supabase validated, with one extra trick — letting users reuse existing
subscriptions. That is not generosity, that is acquisition: they bet convenience migrates users
onto the managed bill over time._

## Hard numbers

- **1,995 stars / 253 forks / 756 open issues** (2026-08-11), launched 2026-07-22 — nearly
  2,000 stars in three weeks is unusually fast early growth
- X.D. CEO stated TapTap released 5,002 playable games in H1, +843.8% YoY, over 4,000 made
  with AI (official figures, no third-party verification)
- Team self-report: internal art staff ship PRs through Cindy and engineers publish directly
  (unverified outside the company)
- Users, ARR, funding: not disclosed
- 756 open issues against 1,995 stars is a high ratio — demand is loud, but so is the message
  that the product is not stable yet

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | X.D. is itself a heavy AI-game-production user and already runs it internally; but this is a platform strategy bet, not a founder's itch |
| Product insight | Nails the two real pains — switching cost and setup cost; the "reuse your existing subscription" acquisition design is sharper than plain free |
| Execution quality | TypeScript + React Native/Electron cross-platform, local-first, isolated workspaces; solid structure, but 756 open issues say far from stable |
| Timing | Right on the inflection where agents go from single-model to multi-model mixing; but the lane is crowded with official clients and open-source rivals |

## The call

**This is a gaming platform importing its distribution playbook into the agent layer, and the
most interesting part is the acquisition design.**

"Reuse your existing subscription, no double billing" sounds like a concession. It is the
standard play: zero migration cost in, then the managed gateway (multi-model, 20% cheaper on
monthly plans) slowly moves spend from your own keys onto their bill. That funnel is directly
stealable.

**Multi-harness continuity is genuine differentiation.** Claude Code and Codex each win on
different tasks and their official clients do not interoperate. Cindy bets continuity beats
"single-point strongest," which holds for teams that already mix agents.

**The risks sit at both ends.** Ecosystem risk: every official Claude Code / Codex release
must be re-adapted to, and the day they stop keeping up is the end. Business risk: their real
moat is the home turf — AI game production around TapTap's game business — and in generic coding agents
they face the official clients directly.

## What to watch next

① Whether stars clear 5,000 in three months — early velocity becomes a trend or dies
② Whether the open-issue backlog shrinks — 756 issues says stability is unproven; the metric is
  issue growth falling below star growth
③ Whether any third party publicly reports running it in production (not just X.D.'s internal claim)

## What you can take from it

**Product logic**: when building a tool that plugs into an ecosystem, "honor and reuse what the
user already pays for" beats "free." It drops migration cost to zero, then the managed add-on
converts users gradually. Counterintuitive acquisition design, copy it.

**Positioning language**: "Reuse the subscriptions you already own." Turning "no double billing"
into a one-line stance is more memorable than saying "free."

**Pricing structure**: the three-tier stack (free with own key / $20 managed / enterprise
self-hosted) is directly reusable, including the trick of framing API reselling as "monthly
plans save 20%."

## Verdict

**Worth watching, with real caveats.** Strong backing (X.D./TapTap), fast early growth (~2,000
stars in three weeks), and a smart acquisition design — but 756 open issues say the product is
immature and the business depends on keeping pace with official agent updates. Note the three
checks above and come back in three months.
