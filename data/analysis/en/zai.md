---
slug: zai
name: Z.ai
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Zhipu AI's overseas front door for the GLM family — officially a "global experience center for GLM models," practically two things: chat.z.ai for foreign consumers to talk to the model, and api.z.ai for developers (with both OpenAI-compatible and Anthropic-compatible endpoints). The domestic counterparts are Zhipu Qingyan (consumer) and BigModel (API); Z.ai is the same models behind a separate door outside the wall.

## Who built it

Zhipu AI, the Beijing lab spun out of Tsinghua University in 2019. The z.ai domain was registered in April 2024 and positioned as the GLM global experience center (per Huxiu). The company is preparing an IPO and expanding overseas through a partnership with Alibaba Cloud, with offices in the Middle East, Singapore, the UK, and Malaysia, plus joint innovation centers in Indonesia, Vietnam, and elsewhere.

_Read: Zhipu is going overseas with an assignment — sell models abroad, build local government agent partnerships, and get GLM's global mindshare up before the IPO. Z.ai is the traffic door and API cash register for that operation._

## What it actually does

- **Chat (chat.z.ai)** → the GLM chat interface for overseas consumers
- **API (api.z.ai)** → an OpenAI-compatible endpoint and an Anthropic-compatible endpoint; the latter lets Claude Code switch to GLM by changing one base URL, making Z.ai one of the few true Anthropic API drop-in replacements outside Anthropic itself
- **GLM Coding Plan** → quota-based subscriptions for coding; after the April 2026 price adjustment: Lite $18/mo, Pro $72/mo, Max $160/mo
- **Free Flash models** → GLM-4.7-Flash and GLM-4.5-Flash are free for all registered accounts; the former has a 203K context window, the largest free window from any major API provider
- **ZCode desktop app** → launched July 2026, an "agent-first development environment" built on GLM-5.2

## What old behavior it replaces

For overseas developers, frontier coding capability used to have exactly two routes: subscribe to ChatGPT Plus or Claude ($20–$200/month), or pay OpenAI/Anthropic per-token APIs whose bills scale with usage.

Z.ai replaces that subscription spend — the Coding Plan starts at $18/month, runs on the same Claude Code configuration with a base-URL swap, and the benchmarks genuinely sit at the top (GLM-5.1 scores 58.4% on SWE-bench Pro, ahead of GPT-5.4 and Claude Opus 4.6). For Zhipu itself, Z.ai replaces the old path where overseas users had to route through the domestic site and get stuck on phone-number verification and compliance.

_Read: this is one of the rare "product-level replacement" plays in Chinese model export — not selling "a cheaper Chinese model" but selling "a drop-in replacement for Claude Code." The Anthropic-compatible endpoint is the smartest single move in the whole playbook._

## Business model

Two layers: per-token direct API (GLM-4.5 at roughly $0.6/M input and $2.2/M output) plus the quota-based Coding Plan subscriptions. Overseas subscription prices run 2–3x the domestic tiers (49/149/469 RMB); some overseas developers call the gap a "Western tax." There were two price increases in 2026 — 30–60% in February and 80–150% in April.

_Read: charging 2–3x for the same model outside the wall is "export pricing power" — no domestic-alternative narrative or domestic price anchor overseas, and the model genuinely competes, so it prices like an international leader. That premium window is rare for Chinese model vendors, and it stays open only as long as the SWE-bench ranking holds._

## Hard numbers

- **traffic board: 10.24M visits, +24.56% MoM** (June 2026); on the chatbot board and both China/global overall and growth boards
- GLM-5.1: 745B parameters, 58.4% on SWE-bench Pro (May 2026, ahead of GPT-5.4 and Claude Opus 4.6); GLM-5.2 released July 2026, ranked #1 among globally available models on Code Arena
- Coding Plan pricing (post-April 2026): $18 / $72 / $160 per month, 2–3x domestic
- ZCode desktop launched 2026-07-02; phased rollout was needed after traffic exceeded expectations, with Max users prioritized
- Company level: IPO in preparation, overseas expansion via Alibaba Cloud; team size and revenue: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High: Tsinghua-linked team, GLM family iterated continuously since 2019, models are the company's core asset |
| Product insight | High: the Anthropic-compatible endpoint plus free large-context Flash models attacks the developer's switching cost directly — more effective than pure price cuts |
| Execution quality | High: top of SWE-bench Pro and Code Arena, plus a no-Nvidia training angle as a geopolitical differentiator |
| Timing | Good: the window where coding tools shift from subscriptions to API quotas, and a Chinese model stands at the top on hard metrics for the first time |

## The call

**Z.ai is the cleanest export signal among Chinese foundation-model companies right now: the model genuinely competes, the pricing genuinely dares, and the growth is real traffic.**

At 10.24M visits with +24.56% MoM, this is healthy growth for a product of its size — not a viral spike, but a steady inflow of developers and users. There is no MoM anomaly, no dressed-up positioning; it is three things: a strong enough model, cheap enough access, and an easy enough integration.

Two things are actually worth watching. First, visits are still climbing after two consecutive price increases (February and April) — that shows demand rigidity, but it also pushes more overseas users toward the domestic tier, and Zhipu is already fighting that arbitrage. Second, if Anthropic tightens the compatibility protocol or the endpoint gets restricted, the foundation of the drop-in play wobbles.

_Read: the transferable point for the reader is direct — if your product's strength is model capability, the first move overseas is not a redesigned UI; it's a zero-migration-cost integration layer. A compatibility endpoint is worth more than a Chinese-language marketing page._

## What to watch next

① Whether visit MoM stays positive a full quarter after the price increases — does demand rigidity survive the price?
② Stability of the Anthropic-compatible endpoint — if the protocol tightens, the drop-in narrative changes
③ Whether GLM's rankings keep beating GPT/Claude — SWE-bench and Code Arena are the reason overseas developers pay 2–3x; when the ranking drops, the premium window closes

## What you can take from it

**Product logic**: for capability products going overseas, build the zero-switching-cost integration layer first, brand second. Z.ai's Anthropic-compatible endpoint lets Claude Code users switch with a base-URL edit — an order of magnitude more effective as acquisition than "cheaper Chinese model" messaging. Any company selling models/APIs can follow the sequence: compatible with the leader → free small quota to try → paid to raise limits.

**Positioning language**: the "drop-in replacement" framing in the docs is directly borrowable — it translates technical specs into switching cost.

**Pricing structure**: the quota-based Coding Plan separates "chat users" from "API users" as two willingness-to-pay curves, with per-token API as the floor and subscriptions collecting the loyal — a dual-track structure worth referencing. The 2–3x wall-outside pricing is an experiment in Chinese vendors' pricing power; don't copy it blindly, but track whether it holds.

## Verdict

**Worth watching.** It is one of the few items in this batch where "data is real + growth is healthy + hard technical metrics rank at the top" all hold at once, and the reference point any Chinese model export must be measured against. Next, watch demand elasticity after the price increases and the stability of the compatibility endpoint — those two decide whether the playbook is replicable.
