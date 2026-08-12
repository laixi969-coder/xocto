---
slug: gendangzou-skill
name: Gendangzou Skill
verdict: Strong pick
analyzed_at: 2026-08-11
---

## What it is in one line

Turns policy direction, media framing, fund flows, and sector relationships in the Chinese A-share market into something an AI agent can query directly.

## Who built it

Published by MobiusQuant — not a personal project, a product with a company behind it.
The evidence is complete: its own site (gendangzou.mobiusquant.ai), its own docs site
(docs.mobiusquant.ai), an official community, Apache-2.0, and a stated support matrix
covering five agent platforms.

_Read: a solo developer doesn't stand up a docs site and write a multi-platform compatibility
matrix. This is a team using open source for distribution, with the revenue somewhere else._

## What it actually does

- **Trace policy through to sectors** → give it a policy, get the affected sectors, companies,
  and ETFs, with a traceable chain of relationships
- **Cross four kinds of signal** → policy, authoritative media, market attention, and fund
  confirmation, four independent lines cross-checking the same conclusion
- **Query live** → not a static data drop; you can ask about right now
- **Built for agents, not people** → installs into Claude Code / Codex / OpenClaw / Hermes / WorkBuddy,
  gets called by the agent, and the output goes straight into the reasoning chain
- **Supports building on top** → API docs and an application development guide
- Two entry points by design: `README_AGENT.md` for the agent to read (how to install, verify, uninstall),
  `SKILL.md` for day-to-day calls

**What it deliberately does not do**: no buy or sell recommendations, no trade execution, no backtesting.
It works only on the traceable link from policy to instrument.

## What old behavior it replaces

An analyst picking stocks off policy runs this loop: read the policy document, work out which industry it hits, dig through research notes for the beneficiaries, check fund flows to confirm, and read the media framing to confirm expectations. Half a day to a full day per chain, and it starts from scratch every time.

**The old behavior is unmistakable and repeats constantly.** Policy lands every day and the chain
is identical every time. That is precisely the kind of work a tool eats.

## Business model

The skill is free under Apache-2.0, but **the API and the data stay in their hands**.

The structure is clear: the skill is the hook — it wins users and builds a habit.
The value and the fee sit in the data service and API quota.

_Read: this is one of the most durable open-source revenue structures of the AI era —
give away the tool, sell the data. Tools get copied; continuously updated data doesn't._

## Hard numbers

- Open-source traction: 184
- Five supported agent platforms
- Pricing, users, API volume: undisclosed

## Four-way read

| Dimension | Read |
|-----------|------|
| Founder-product fit | High. The name MobiusQuant is a quant background, and the product matches what they'd have accumulated |
| Product insight | High. They skipped "pick stocks" for "the traceable chain from policy to instrument" — the first is crowded, the second is empty |
| Execution quality | Above average. A docs site, multi-platform support, and agent-specific install instructions aren't a side project |
| Timing | Right on. Agents just became able to call external capabilities, and vertical data skills are the first beneficiaries |

## The call

The smartest thing about this product is that **it serves agents instead of people**.

The same data rendered as a web page for humans has to fight a wall of financial terminals.
The same data shipped as a skill an agent calls has almost no competition — and it becomes a
link in someone's reasoning chain, which makes it very expensive to switch away from once
it's written into a workflow.

**The transferable rule: when the consumer-facing surface of a category is too crowded to attack, dropping one layer down and becoming a capability inside someone else's product is the cheapest way around the fight.** It doesn't compete for users. It gets called by them.

The cost is that the ceiling is capped by how mature the agent ecosystem gets. How many people
currently research equities through a coding agent? Very few. The bet is that this number climbs,
and it has to stay alive until it does.

The name is worth a note too. In Chinese it's an extremely sticky phrase, but it also welds the
product to one market — it can't travel abroad. Whoever picked it presumably knew that.

## What to watch next

1. **Whether an API pricing page appears** — there's no way to pay today; a payment path proves the model
2. **Whether the supported platform count keeps growing** — more means people actually use it; frozen means the compatibility work was a one-off marketing move
3. **How fresh the data actually is** — "live query" is a claim; whether it's minute-, day-, or week-level decides its real value

## What you can take from it

**The four-line cross-check is the portable structure**: policy, media, market attention, and fund confirmation — four independent lines validating one conclusion. That's steadier than any single signal, and it isn't specific to equities. Property, for instance, has the same four: policy, sentiment, transactions, capital.

**Business model, and this is the valuable part**: give away the skill, sell the data API.
Any capability you're thinking of monetizing can use this shape — hand out the capability free
to build the habit, put the fee on continuously updated data or service. Tools get copied; data doesn't.

**Positioning strategy**: skip the consumer interface, become a capability inside other people's agents.
That is a particularly good fit for anyone strong at structuring expert judgment and weak at
running a mass-market product.

## Verdict

**Strong pick.** It hands you three things at once: a working example of an agent-native data
product, a four-line analysis structure that transfers to other industries, and an open-source
revenue model that already has a path to getting paid.
