---
slug: kimi
name: Kimi
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Moonshot's Kimi overseas site: the same K-series models, an English-language entry point for international users, selling "frontier capability, open weights, and a price that is a fraction of the closed labs'."

## Who built it

Moonshot AI's international version of Kimi (kimi.ai). The English-facing consumer contract sits with Moonshot AI PTE, Singapore; the developer platform is platform.kimi.ai, billed in USD. The other traffic board entry, "Kimi｜月之暗面" (kimi.com, domestic, RMB), is the same company's other site.

_Read: this is a capability clone plus compliance rework of the domestic product, not an independent product. Its meaning is not feature difference but a test: can a Chinese open-weight model take money from closed-lab subscriptions abroad._

## What it actually does

- **Model switching** → K2 family from 0905 through K2.5, K2.6, and K2.7 Code: chat, deep thinking, vision, agent work
- **Cheap high-volume API** → K2 launched at $0.15 / $2.50 per million tokens (input/output); K2.6 dropped to $0.55 / $2.65; K2.7 Code at $0.95 / $4.00. Anthropic-compatible API format, so it can drop into a Claude workflow
- **Coding workflows** → Kimi Code CLI positioned against Claude Code / GitHub Copilot, subscriptions from $19/month; adopted by Cursor, Windsurf, Cline
- **Consumer plans** → international tiers: Adagio (free) / Moderato ($19/mo, unlocks vision and deep research) / Allegretto ($39/mo, adds Agent Swarm)
- **Open ecosystem** → K2 / K2.5 weights open under a Modified MIT license; self-hostable from Hugging Face

## What old behavior it replaces

Two kinds of people, two replaced behaviors.

**For consumers**: the habit of paying $20/month for ChatGPT or Claude. A free or $19 tier that is close on capability, aimed at budget-sensitive international users who treat AI as a tool.

**For developers**: paying full price on closed APIs. At launch, K2's input price was 1/100th of Claude Opus 4 ($0.15 vs $15 per million tokens) and 1/30th on output. For high-volume coding and agent workloads that is an order-of-magnitude cost difference — one developer measured ten similar tasks at $10-20 with Claude Sonnet 4 versus roughly $7 with K2.

_Read: this is a price-gap plus open-weights combo, not a feature gap. DeepSeek proved the play; Kimi is running it again in the coding/agent segment._

## Business model

Same shape as domestic: free C-end plus subscriptions ($19/$39), metered API, open models for ecosystem. Differences: USD billing and an offshore entity. Company-reported ARR crossed $300M in June 2026, with overseas API revenue a significant slice (up ~4x since November 2025).

## Hard numbers

- traffic board figure: **22.69M MAU, -12.40% MoM**, and it sits on the global slowdown board — it grew before, now it is retracing
- As of May 2026, K2.6 was the second most-used LLM on OpenRouter
- K2 became the fastest-downloaded model on Hugging Face in a single day at launch; K2.5's cumulative revenue exceeded Moonshot's full-year 2025 revenue
- Launch API pricing $0.15 / $2.50 per million tokens, roughly 1/100th of Claude Opus 4 on input
- Team size and absolute paid-user count internationally: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Same origin as the domestic product; founder's long-sequence research background, strong fit |
| Product insight | Built the international narrative on a price gap: cheap + open + Anthropic-compatible format to cut migration cost |
| Execution quality | Models adopted by mainstream coding tools and #2 on OpenRouter by usage — the ecosystem has validated the engineering |
| Timing | Right window: overseas frustration with closed API pricing; but DeepSeek and Qwen open models are hunting the same developers |

## The call

**A verified overseas play that is decelerating.** -12.4% MoM on the slowdown board means the explosive stretch (paid users +170% MoM, API revenue x4) peaked in late 2025 to early 2026; this is now a retrace on a much larger base.

The reason to keep watching is not growth. It is that two things were achieved at once: proving an open-weight model can rank in the top two by usage in the overseas developer ecosystem, and proving that "capability on par with closed, price one or two orders lower" — effective domestically with DeepSeek — also works internationally.

_Read: two risks. One, an open-model price war has no moat — DeepSeek and Qwen are courting the same developers, diluting Kimi's price edge. Two, the consumer tier ($19/$39) goes head-to-head with ChatGPT Plus user habits overseas, a much harder fight than the developer side._

## What to watch next

① Whether 22.69M MAU's negative MoM narrows — and whether it stays on the slowdown board next month
② Whether the #2 OpenRouter position holds, and whether API revenue keeps pace with each model generation (international K3)
③ Any disclosed absolute number for international consumer subscribers (Moderato / Allegretto)

## What you can take from it

**Product logic**: going global is not about translating the UI; it is about the price gap plus a compatible format. The key move of Kimi's international site was not an English app but an Anthropic-compatible API — a developer changes one base_url and migrates, with migration cost near zero. Any product trying to take existing users from an incumbent should make "switching costs nothing" the first design principle.

**Positioning language**: none. It is a product page; the sentences are not transferable.

**Pricing structure**: put a comparison directly on the pricing page — "input price is 1/100th of that closed model" — rather than a bare price list. Price competition needs a reference point; a low price without one is not a price.

## Verdict

**Worth watching.** The data is real and so is the deceleration. It validated the playbook of internationalizing an open-weight model; the open question is whether the position survives once DeepSeek and Qwen dilute the price gap.
