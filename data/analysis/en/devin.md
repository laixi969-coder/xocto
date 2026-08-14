---
slug: devin
name: Devin
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An autonomous coding agent billed as "the world's first AI software engineer":
it works in a cloud sandbox with its own terminal, browser and editor, takes jobs from
Slack or GitHub, writes code, runs tests, debugs, and opens PRs — priced per unit of
work the agent actually does, not per human seat per month.

## Who built it

Cognition AI, founded 2023. The three founders — Scott Wu, Steven Hao and Walden Yan —
are a Chinese-American team of International Olympiad in Informatics gold medalists,
later joined by Gennady Korotkevich (8x IOI gold). Devin launched March 2024, and in
July 2025 Cognition acquired Windsurf, the agentic IDE.

_Read: this is a company that put the whole bet on autonomy — everyone else builds
copilots that assist people; it builds an agent that does the work. An IOI-gold
founder team is top-shelf for this bet, and they treat planning, tool use and
self-correction as the core moat, not code completion._

_Note: the pool summary says "Devin Financial Services: Modernizing financial
services with autonomous AI engineers." That is a misattribution from the data source.
The real Devin is Cognition AI's AI software engineer, not a financial-services
product._

## What it actually does

- **Autonomous task execution** → plans, writes code, runs tests, debugs failures
  and deploys in a cloud sandbox, taking jobs from Slack / GitHub / Linear
- **End-to-end PRs** → submits merge requests when the work is done; a human reviews
- **Devin 2.0 (2025-04)** → price cut from $500/mo to $20/mo, VS Code-like IDE
  experience, parallel development, interactive planning
- **ACU metering** → 1 ACU ≈ 15 minutes of agent work, charged by task complexity
  and execution time
- **Windsurf integration (post-acquisition)** → Windsurf IDE handles
  human-in-the-loop coding, Devin handles independent execution, covering the full
  spectrum of coding tools
- **In-house models** → SWE-1.5/1.6 coding models, claimed 13x faster than Claude
  Sonnet

**What it deliberately does not do**: it is not a local tool. Devin is a service, not
software — you hand it work in the cloud, it executes, you review PRs. That is a
fundamentally different use pattern from Cursor's local, real-time editing.

## What old behavior it replaces

**It replaces hiring junior engineers or outsourcing for high-volume, rule-governed
work.** Tech-debt remediation, dependency upgrades, batch file changes, validation
runs used to be scheduled human work or outsourced. Devin turns it into "pay the
agent per usage": 1 ACU ≈ $2.25, roughly $8-9/hour, against a junior engineer's
~$150/hour. It swaps software engineering's cost sheet for a cloud-metering sheet —
Goldman Sachs announced piloting Devin alongside its 12,000 engineers with a target
of 20% efficiency, the equivalent of 2,400 engineers for free.

**It replaces the daily grind of triaging issues and PRs by hand.** Dev teams used to
spend hours daily on GitHub/Slack — classifying issues, fixing lint, resolving merge
conflicts. Devin's design is "hand the ticket to it"; humans only review.

## Business model

**Subscription plus usage metering (SaaS + consumption), structurally closer to AWS
than to Cursor.**
- Core: $20/mo with base ACU quota (post April 2025 price cut)
- Team / Enterprise: custom, higher ACU, team management
- ACU: 1 ACU ≈ 15 minutes of agent work, ~$2-2.25, on top of the monthly fee
- Active engineering teams realistically spend $5K-50K+/month

_Read: this is its smartest move — a $20 entry price for acquisition, with the real
money in ACU burn. Pricing is tied directly to value delivered: simple tasks are
cheap, complex tasks are expensive. It is not selling "a software subscription"; it
is selling "paid per job completed," letting buyers model ROI as "how much human
labor replaced." Procurement moves from "software budget" to "cost replacement."_

## Hard numbers

- traffic board: 2.97M monthly visits, +80.1% MoM (2026-08)
- ARR: $1M (Sept 2024) → $73M (June 2025), 73x in nine months
- Windsurf acquisition (July 2025, ~$82M ARR, 350+ enterprise customers); combined
  ARR ~$155M
- September 2025 Series C at $10.2B valuation; reported in talks near $25B
  (April 2026)
- Total funding >$696M, net burn <$20M (self-reported)
- Customers: Goldman Sachs, Citi, Dell, Cisco, Ramp, Palantir, Nubank, Mercado
  Libre, NASA-JPL
- Early adopters report project cost cuts of up to 50% and >2x efficiency

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | IOI-gold founders building agent orchestration — a rare "algorithm background + right product" combo |
| Product insight | "Autonomous execution" positioning plus ACU metering turns headcount-replacement into a sales language |
| Execution quality | Planning, tool use, self-correction is a fuller agent stack than completion tools; real-world success rate is contested |
| Timing | Enterprises are just starting to accept "agents doing work," and Devin is the first to prove payment |

## The call

**Worth watching — the pricing and commercialization sample of the "autonomy" path
in AI coding.**

The +80.1% MoM needs decomposition: the tail of the April 2025 Devin 2.0 price cut,
traffic pulled in by the Windsurf integration, and attention from Goldman-level
customer news. It is the stack of "price cut + acquisition + marquee customers"
rather than pure organic growth — discount it accordingly — but the direction is
real: autonomous agents are moving from demo to paid business.

**The most valuable thing is its pricing model, not its model.** ACU metering turns
"how much work the agent did for you" into a billable number, making the CFO rather
than the CTO the buyer — Goldman runs the math "20% efficiency = 2,400 free
engineers." That "usage-metering plus headcount-replacement narrative" is why it hit
$73M ARR in nine months, and it is the template every later agent product copies.

**The controversy must be admitted**: independent analysis shows SWE-bench training
contamination, with real-world success (~15%) far below the benchmark (80%); early
demos were frame-by-frame dissected over truncated task descriptions. Since 2025
Cognition has shifted to more honest disclosure (67% PR merge rate, admitted
limits) — that is how it is rebuilding trust. Split its data in two: revenue numbers
(cross-validated by multiple sources) are credible; capability numbers
(self-reported benchmarks) need discounting.

## What to watch next

① Whether the +80% MoM holds — how much organic growth is left after the price-cut
and acquisition tailwinds
② Whether combined ARR grows past $155M — whether the Windsurf + Devin synergy works
③ Whether third-party re-tests publish real-world success rates — that is the
foundation of its valuation story

## What you can take from it

**Pricing structure**: if your product "does the work," copy ACU metering — charge
per job completed, not per month. Then the buyer can directly compute "how much human
labor was replaced," and the decision-maker shifts from user to finance. A low entry
price plus high usage price is the shortest path between acquisition and revenue.

**Product logic**: automate the "rule-governed, high-volume, low-creativity" work
first — tech debt, dependency upgrades, batch edits. That is the only range where an
agent delivers reliably. Devin also proves: never oversell beyond your demo — a
one-time trust collapse costs a full version of honesty to rebuild.

**Positioning language**: none. Official copy is engineering-oriented; nothing to
steal.

## Verdict

**Worth watching.** The first commercial proof of the autonomous coding agent:
a real revenue curve, a transferable pricing model, and credible marquee customers.
But capability numbers need discounting, and +80% MoM is a stacked-event result. It
is the pricing template for every "sell work, not software" product.
