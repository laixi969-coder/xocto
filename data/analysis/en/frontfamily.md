---
slug: frontfamily
name: frontfamily
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A "Rosetta Stone for UI component libraries": no AI, no guessed props — a hand-verified mapping
table translates MUI into Chakra and Ant Design into Mantine, entirely in the browser.

## Who built it

Bassem Chagra (HN: ch-bas), a self-described full-stack engineer focused on developer tooling,
solo project, Apache-2.0.

_Read: choosing deterministic conversion over LLM conversion is a deliberate contrarian move. The
bet: in migration scenarios, "no hallucinated props" is worth more than "looks intelligent." That
judgment is right in tech-debt cleanup scenarios._

## What it actually does

- **Deterministic component conversion** → 219 hand-verified component mappings, 42 conversion
  paths, 7 source frameworks (React/Vue/Angular/Svelte/TypeScript), 30+ libraries catalogued
- **Behavioral-difference flags** → not just code: it flags behavioral differences automatically
  (Chakra's onClose fires on overlay click; MUI's Dialog doesn't by default)
- **Fully local** → conversion runs entirely in the browser; no code goes to any server; no
  accounts, no API keys
- **CLI migration** → `npx @frontfamily/cli eject`, 207 templates across 23 patterns and 9
  frameworks, one command into your project, zero runtime dependencies
- **Migration guides** → 9 guides with searchable prop tables and real-world pitfalls

**What it deliberately does not do**: no LLM, no fuzzy "looks about right" translation, no code
collection.

## What old behavior it replaces

Cross-framework component migration used to mean two things: manually comparing both libraries'
docs prop by prop (hundreds of API lookups for one migration), or throwing the code at an AI
translator (producing hallucinated props — harder to find the wrong edits than the right ones).
The more common reality: the tech debt is too heavy, so no migration happens and old code rots in
its framework.

frontfamily replaces "docs-surfing + trusting AI translation" with a deterministic process that a
lookup table can verify. Its core selling point is not that it converts — it's that errors get
flagged.

## Business model

Free, no accounts, no API keys, no paywall. Apache-2.0.

_Read: there is no business model today; it reads like an engineering exhibit proving the mapping
table is an asset. The plausible monetization path is selling the mappings to migration service
providers or productizing it internally — both later-stage._

## Hard numbers

- **HN: 13 points, 2 comments** (2026-08-13), Show HN
- 219 hand-verified mappings, 42 conversion paths, 7 source frameworks, 30+ libraries catalogued
- 207 CLI templates, 23 patterns, 9 frameworks
- Users, traffic: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Solo dev-tooling, pain almost certainly firsthand; the "hand-verified mappings" grunt work means hallucinated props bit them personally |
| Product insight | "Deterministic + behavioral-difference flags" is the most undervalued design in component conversion — the death mode of conversion tools is silent wrongness |
| Execution quality | 219 manually maintained mappings is honest and verifiable; the behavioral flags are beyond string-replacement level |
| Timing | Frontend is in a framework-migration wave (especially around the shadcn ecosystem), but willingness to pay lives mainly in large tech-debt enterprises |

## The call

**A textbook case of using lookup tables against hallucination, and the rule transfers directly.**

A mapping table is a deterministic asset; an LLM is a probabilistic tool. In any scenario where
conversion output must be verifiable — component migration, data migration, format conversion —
probabilistic output is unacceptable, because a silent error costs an order of magnitude more than
an explicit one. frontfamily treats "errors get flagged" as a product feature, which is the single
most copyable design in conversion tools.

**The honest limit**: 219 mappings is the tip of the iceberg for 30+ libraries, and the long tail
needs manual labor; 7 source frameworks means it can never outrun ecosystem churn.
Mapping-table maintainability is the category's ceiling.

**A 13-point HN response says either it hasn't been seen, or it was seen and nobody needs a
library converted right now.** It reads as the right technical judgment attached to an unvalidated
market.

## What to watch next

① Mapping update frequency — this is its lifeline; stopping means dying
② Whether enterprise migration cases appear — large tech-debt teams are the real buyers
③ Whether it grows from a conversion tool into a migration service (selling guides, managed
migrations) — whether it's a business at all

## What you can take from it

**Product logic**: in any "AI-generated but must be verifiable" scenario, copy the "deterministic
mapping + explicit difference flags" combo — swap probabilistic output for a lookup table, and
make errors visible instead of silent. For anyone building content/code/data AI products, that
error-visibility design applies directly.

**Positioning language**: lines like "deterministic conversion, not AI-guessed props" transfer to
any reliability-selling product.

**Pricing structure**: none. Free, no accounts, no disclosed monetization plan.

## Verdict

**A design worth remembering; a market unvalidated.** Hand-verified mappings against hallucinated
props is one of the few correct ideas in conversion tools. But 219 mappings and 13 points both say
early. Note it; track mapping velocity and enterprise cases.
