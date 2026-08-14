---
slug: insidedb
name: Insidedb
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A webpage that turns database internals into playable animations — insert a key and watch the B-tree split; pull the plug and watch the write-ahead log bring data back. It replaces reading with playing, covering B-trees, query planning, the WAL, and MVCC.

## Who built it

GitHub user david-g-3654 (David G.), a personal project hosted on GitHub Pages, repository created 2026-08-11, the same day it hit HN. Team background and motivation are not disclosed.

_Read: this is the classic "if you cannot explain it, build it" artifact. The author was most likely pushed to make animations by the frustration of explaining databases with static images._

## What it actually does

- **B-tree** → insert keys in real time and watch nodes split and middle keys rise; you see the tree height and the reads needed to find any key
- **Query planner** → run the same WHERE clause two ways (sequential scan vs index) and watch the cost estimate choose
- **Write-ahead log** → step through write, commit, power-out, recover as a story
- **MVCC** → the versioning mechanism that lets readers and writers stop blocking each other

Each topic is a hands-on animation, not a static diagram.

## What old behavior it replaces

Learning database internals used to mean three things: textbooks with static diagrams, long blog posts with ASCII art, and recorded lectures you can only watch. This page swaps "read the figure and imagine the motion" for "do it yourself" — you insert the key, you pull the plug, you switch the plan. For actually getting it, an interactive explainer is much faster than text. But it covers only four topics with no course structure: it replaces "look up one concept," not "learn a subject."

## Business model

None. Free educational page, no ads, no paywall, no course derivative.

_Read: single-page explainers like this exist for reputation or a portfolio, not for money. Their commercial value is proving the author can explain complex systems — a skill the hiring market prices._

## Hard numbers

- HN: 5 points, 0 comments
- GitHub: 0 stars / 0 forks, created 2026-08-11
- Four topics: B-tree, query planner, WAL, MVCC
- Author's full name, team, and any monetization plan: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Cannot be assessed; author information is nearly zero |
| Product insight | The form judgment — interactive animation over static diagrams — is right, and the explainer format is proven |
| Execution quality | Smooth interactions, dense information, readable; not a rough demo |
| Timing | Database learning is evergreen, but more people will build this form, and topic count is the moat |

## The call

**The form judgment is correct, but the sample is tiny.** Interactive explainers are almost always more effective than text for "how a complex system works" — that part is settled. The problem is four topics, no growth data, and no sign of becoming a product or a course.

_Read: the thing actually worth tracking here is not this page but the content format it represents — system internals made playable. That format is moving from "teaching aid" toward "product shape" on its own._

## What to watch next

① Whether the topic count grows past four — staying at four means a one-off; continued updates mean a product
② Whether GitHub stars break 100 in three months
③ Whether the author extends it into a course, a paid product, or at least a public roadmap

## What you can take from it

**Content logic**: for any process-type knowledge (protocols, algorithms, system mechanics), first ask "can the reader do one step with their own hands?" Turning "watch" into "do" drops comprehension cost by an order of magnitude, and the artifact is self-promoting — a screen recording travels better than a text excerpt.

**Engineering tradeoff**: a single page, no dependencies, free GitHub Pages hosting, one topic done to an extreme instead of many topics listed. For individual content products, this is the cheapest way to start.

**Positioning language**: none. This is a personal work; nothing to steal.

## Verdict

**Unproven.** Right form, well executed, but no product intent and no data. Keep it as a reference sample for the "interactive explainer" content format, and check in three months to see whether it became something else.

