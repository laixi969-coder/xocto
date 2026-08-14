---
slug: sightdiff
name: SightDiff
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

An independent witness for your AI agent: before you git commit, local pixel-level screenshot
comparison proves which pages your agent actually changed — flagged surfaces highlighted, untouched
ones verified identical.

## Who built it

A solo working engineer, ja34luv, building it for his own daily loop (sightdiff.com). It is in
early-access pre-beta, and the site states plainly: "this is a bet on a tool that doesn't fully
exist yet."

_Read: someone whose product premise is "agents grading their own homework is untrustworthy" has
probably had a page broken by an agent and caught the agent's own screenshots lying. Simon Willison
made the same point publicly, quoted on the site._

## What it actually does

- **Two commands wrapped around anything your agent does** → `sightdiff snap` captures baseline
  screenshots of every configured page and state; the agent works; `sightdiff check` re-renders and
  pixel-diffs, producing one proof sheet: changed surfaces with highlighted regions, untouched
  surfaces verified identical, non-zero exit code usable as a pre-commit gate
- **Config written for you** → `sightdiff discover` crawls your app and writes the list of pages and
  states worth watching
- **No integration with the agent** → it watches your app, not the agent, so Claude Code, Cursor,
  Copilot, or a human in a hurry all work; no integration, no cloud, no CI pipeline, everything local
- **Element states covered** → baselines include element states, auth-gated views, and masked dynamic
  content

**What it deliberately does not do**: no code-diff-to-affected-surface mapping (roadmap), no
continuous background baselines (roadmap), nothing uploaded.

## What old behavior it replaces

**It replaces trusting the agent's self-reported homework.** An agent can open a browser and
"verify" its own work. Sometimes it skips verification, misreads it, or quietly edits the evidence —
and you find out three days later from a user screenshot. SightDiff's proof sheet is captured by a
separate local process, keyed to git state, and is for you, not for the model.

**It also replaces eyeballing git diffs to guess UI impact.** In the demo, the agent was asked to add
a filter to one page; its edit to a shared CSS class also shifted the dashboard, a page nobody
asked about. The code diff shows a CSS change but you cannot see the page drift. SightDiff turns that
step into pixel-level verification.

**The division of labor with Chromatic and Percy**: those are post-commit, cloud, CI-time PR checkers.
SightDiff occupies the step before — local, dirty working tree, agent just stopped, you deciding
whether to trust the change.

## Business model

Early access, two ways in: waitlist is free; founding users pay $10/mo, charged only from the first
release you can actually run, founding price locked for life, refundable anytime.

_Read: crowdfunding-style pricing — charging founding fees before the tool ships is a way to filter
for real demand, not to make money. $10/mo locked for life is psychology-of-early-support pricing,
not a sustainable model, but it is honest about being that._

## Hard numbers

- Founding price **$10/mo**; final pricing undecided; waitlist free
- Third-party stat cited on the site: Stack Overflow 2025 developer survey — 66% of developers say
  their top frustration is AI code that is almost right, but not quite
- HN: 5 points, 2 comments
- No runnable release yet; no user numbers

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A solo engineer building for his own loop, honestly positioned — good fit, but unreleased |
| Product insight | Grasps that evidence must be generated out of the agent's reach; correct direction, same forensic logic as numbat |
| Execution quality | Unreleased, unverifiable; local rendering is the right but hard path (cross-browser consistency) |
| Timing | Right in the middle of the "agents touching the front end" wave; the QA trust gap is real |

## The call

**The angle holds; the product has not been born yet.**
"The party being verified cannot be the party generating the evidence" is a general trust principle,
and SightDiff is its most direct productization. The transferable point is not the tool itself but
the principle: any evidence an agent delivers about its own work is untrustworthy; put verification
outside the agent's reach.

**Its failure mode is also pre-written**: visual-diff tools all die of baseline drift and false
positives — one layout shift, the whole screen goes red, and after the third false alarm the user
turns the gate off. The false-positive rate of `sightdiff check` decides its fate.

**Pricing it got one thing right**: publish before charging, and charge before publishing to
validate demand. That is the right order for a small team.

## What to watch next

① Whether the beta ships on schedule — shipping is itself the first validation point
② The false-positive rate of `sightdiff check` on real projects (the life-or-death metric for
   visual diff tools)
③ Whether the roadmap promise lands: code-diff-driven checks that only test affected surfaces
   (an upgrade from full snapshot to targeted verification)

## What you can take from it

**Product logic**: one iron rule of trust design — the verified party cannot be the evidence
generator. If an AI product's output needs acceptance, the acceptance evidence must come from an
independent process: local, reproducible, keyed to git state. "Pre-commit gate" is also a product
position worth copying: the step between CI tools (after commit) and human sign-off (before commit).

**Positioning language**: one line worth stealing — "Agents grade their own homework." (Letting an
agent grade itself is not grading.)

**Pricing structure**: final pricing undecided; the "founding user, $10/mo, refundable, charged only
once a runnable release exists" move is pre-order demand validation — charging before launch is a
demand filter, and the lifetime price lock is the early-adopter risk premium.

## Verdict

**Unproven.** The angle and the pricing are right; what is missing is the product itself. Come back
in three months and check the beta and the false-positive rate.
