---
slug: bullet
name: Bullet
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Not a smarter model, a leaner loop around it. Bullet attacks the wall-clock time of an agent run
by cutting round trips, on the insight that model speed matters less than reducing them.

## Who built it

Adi and Alex, Yale CS grads fresh out of AppLovin and Citadel, YC S26. Bullet is the survivor of
six pivots — earlier attempts included an AI hedge fund, a browser-use agent, synthetic financial
data, and a mobile IDE, all failures.

_Read: split the background in half. The negative half: six pivots says they are good at hitting
walls. The positive half: latency optimization and cost control are exactly the fundamentals of
quant trading systems, and they map directly onto what this product does._

## What it actually does

- **Model routing** → easy steps go to fast models; escalation only when the task earns it; no
  manual model picking
- **Targeted code search** → no whole-repo embedding; search with fallbacks pulls only relevant
  files, so context stays small
- **Context hygiene** → bounded tool output, stale screenshots removed, no file re-reads
- **Parallel tool calls** → independent searches/reads/commands run concurrently; dependent edits
  and verification stay sequential; self-reported 16% fewer round trips and 27% lower cost
- **Uses what you already pay for** → works with a Claude Code/Codex subscription, any API key, or
  an on-device model
- **CLI** → `npm install -g @trybullet/cli`, macOS and Linux

**What it deliberately does not do**: no model training, not a Claude Code replacement — a tighter
loop wrapped around existing models and subscriptions.

## What old behavior it replaces

The typical waiting workflow with Claude Code or Codex: shovel the whole repo into context (or a
compressed version), execute tasks serially, queue every tool call. A 100-turn agent run spends
most turns on boring work — reading a file, checking a path, running a test — that should return
instantly but gets dragged into frontier-model latency.

Bullet replaces the default of "strongest model end to end, serial, whole-repo context." Its bet:
a real router beats a bigger model on both wall-clock and cost.

## Business model

**Not disclosed.** Private beta, free for now, no subscription. macOS and Linux.

_Read: no pricing page means still in validation. The charging point in this category will likely
be per run or per seat rather than per token — the token cost is already on the user's own
subscription and keys._

## Hard numbers

- **HN Launch HN: 93 points, 68 comments** (early August 2026)
- SWE-bench Verified: **479/500 (95.8%) in one attempt**, averaging **119s per task**, claiming
  **35–67% faster** than mini-SWE-agent + Fable/Sol; the marketing line is "30-60% faster than
  Claude Code/Codex"
- Internal measurement: 16% fewer round trips, 27% lower cost
- Team size, user count, revenue: not disclosed

**Benchmark credibility is contested**: the 95.8% comes from an eval without the router enabled
(for an apples-to-apples harness comparison), and SWE-bench Verified is described as saturated.
HN's soulofmischief said outright the result "is essentially meaningless."

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High — they were bitten daily by slow agents; AppLovin/Citadel latency experience is on-topic |
| Product insight | "Fewer round trips beats a faster model" is the most important and least-worked insight of this agent generation |
| Execution quality | Real user feedback (one says they've switched to Bullet as primary); fast iteration; MCP support still missing |
| Timing | Good — everyone waits for faster models, nobody fixes the loop; but the hardware side (Cerebras) attacks the same pain |

## The call

**Quant-trading latency thinking applied to coding agents: don't optimize the model, optimize the
pipeline.**

The most transferable rule is that routing is the cheapest speed-up available in today's agents.
The default in most harnesses is to send everything to the strongest model — safe, and nobody gets
blamed. But a 100-turn agent run is mostly boring turns, and paying frontier price and latency for
a directory listing is the industry's most expensive habit.

**The most valuable objections in the comments**: the benchmark is saturated and the router wasn't
in the eval; and routing plus search can be approximated open-source (OpenCode +
codebase-memory-mcp). Both point to the same conclusion: Bullet's moat is currently shallow — it
sells execution quality, not models and not ecosystem.

**But "selling execution quality" is a real category.** One commenter says they've switched to
Bullet as their primary tool; another reports a clearly faster feel, a useful integrated browser,
and credits Linux support. The specific complaints — git commit authorship and privacy prompts —
the founders acknowledged and are fixing.

## What to watch next

① When MCP support and skill preservation land — no ecosystem slot means one-shot tooling
② When pricing appears and how it's billed — the business model decides whether it's a real business
③ Whether benchmarks move to harder tasks (Terminal-Bench, CursorBench) — the founders say they're testing them

## What you can take from it

**Product logic**: any efficiency product should ask where its most expensive step is. Bullet's
answer is round trips, not model speed. Before building an agent product or an efficiency tool,
count the serial waits in your pipeline — that's the cheapest cost to remove.

**Positioning language**: the opening of the HN post — six pivots before solving your own real
problem — is a standard honesty narrative worth copying for its list of admitted failures; it
builds trust on candor.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** Right direction, real users, candid founders — but a shallow moat, an
unresolved benchmark dispute, and no pricing yet. Its biggest value is validating the direction
"optimize the loop, not the model," which is directly usable judgment for anyone building AI
efficiency products.
