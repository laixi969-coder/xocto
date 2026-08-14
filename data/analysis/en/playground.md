---
slug: playground
name: playground
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Red-team testing for AI agents turned into a weekly public challenge: a live agent with real tools
guards a secret, its system prompt is fully public, whoever breaks it wins, and the winning attack
transcript is published for everyone to study.

## Who built it

Fabraix, a company building runtime security for AI agents. The playground started as an internal
tool for testing their own guardrails; because "people who think like us only find the same
vulnerabilities," they open-sourced it as a public challenge ground. The repo lives at
github.com/fabraix/playground and the HN submitter, zachdotai, is a team member.

_Read: a security company open-sourcing an attack tool is both a way to collect community attack
data and a piece of positioning — "we publicized our own playground, so we're not afraid of
scrutiny." The marketing motive and the genuine need are the same thing here._

## What it actually does

- **Weekly live challenges** → deploys an agent with real tools (web search, browsing) tasked with
  protecting a secret; the system prompt is fully visible and the community tries to break through
- **Community-driven selection** → anyone proposes a challenge — scenario, agent, objective —
  the community votes, and the top choice moves toward going live
- **Public post-mortems** → when a challenge ends, the winning conversation and guardrail logs are
  archived publicly, turning every attack into a reusable security sample
- **Server-side evaluation** → guardrail judgment runs server-side to prevent client-side
  tampering; the agent runtime is being open-sourced separately
- **Runs locally** → React frontend with versioned challenge configs; `npm install` gets a local
  dev environment

## What old behavior it replaces

Previously, testing an agent's defenses meant three routes: the internal security team (fixed
viewpoints, predictable blind spots), an outsourced red team or pen-test firm (expensive,
weeks-long, often tens to hundreds of thousands of dollars), or automated scanners (nearly useless
against semantic attacks that "look normal but step out of bounds"). Playground's replacement
mechanism: offload the testing cost to an incentivized crowd — prizes plus reputation — and keep
the attack results. This is security testing experimenting with crowd-sourcing instead of hiring.

## Business model

**The playground itself is open source and free; Fabraix's revenue comes from a commercial product.**
The company positions itself as "runtime security for AI agents"; the specific product and pricing
are not public.

_Read: the public challenge is an acquisition and trust tool, not the business itself. The real
asset is the accumulated attack-transcript library — data that no internal team could assemble on
its own budget._

## Hard numbers

- **73 stars, 11 forks.** Created 2026-02-07, MIT, TypeScript
- HN post reached ~30 points (pool records 13), 13+ comments, high-quality discussion
- First challenge: make an agent call a tool it was explicitly told never to call; someone broke it
  in about 60 seconds. Second challenge shifted to data exfiltration with harder defenses
- Reports claim weekly prize pools above $100,000, but Fabraix's own launch posts never mention
  prize details — unverified

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Dogfooded internal tool; the team lives with agent security daily — the pain is their day job |
| Product insight | "Public system prompts + public transcripts" turns attacks into an accumulating asset, worth far more than star counts |
| Execution quality | Server-side judging, versioned challenge configs, runtime open-sourced separately — built for public testing |
| Timing | Agents are entering production but security budgets don't exist yet; half a step early, right direction |

## The call

**Worth watching, because it is producing data nobody else can produce.** The public archive of
attack transcripts plus guardrail logs is the most valuable thing here — in security, the moat has
always been "having seen enough attacks." The crowd-sourcing model gives Fabraix a continuous
stream of attack samples at low cost, and every published post-mortem doubles as market education.

**Watch whether the restraint holds up.** The "guard a secret" setup is a controlled scenario, far
from real production agents with many tools, long-term memory, and user identities. It validates
whether public attack testing finds real problems; it is a long way from "tested, therefore safe."

## What to watch next

① Challenge cadence and the growth of the transcript library — does the public archive grow
steadily in three months
② Whether the prize mechanism actually pays out and keeps attracting strong attackers (the
unverified $100K weekly figure is the open question)
③ Whether anyone pays for Fabraix's commercial product, or the playground is purely a lead-gen tool

## What you can take from it

**Product logic**: if you're building a community or platform product, copy this three-part
outsourcing mechanism — the task must be concrete (guard a secret), the information transparent
(system prompts public), and the output accumulated (transcripts archived). Remove any one of the
three and the crowd-sourcing degenerates into paid trivia. Also: open-sourcing your internal tool
as an acquisition entry is itself the strongest trust statement available.

**Positioning language**: none. Engineering launch copy; nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** The mechanism has real value — public transcripts are data others can't
assemble — and the team is honest, even publishing the transcripts of attacks against their own
LLM-as-a-judge defenses. Keep tracking whether it stays a marketing engine and whether the prize
narrative materializes. Re-check the three items in three months.
