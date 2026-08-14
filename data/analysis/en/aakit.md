---
slug: aakit
name: Aakit
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

An assumption detector for your coding agent: it digs out every silent assumption the
agent made, attaches evidence, shows which assumption broke and how wide the blast radius
was, and measures whether asking one question or not asking at all is actually cheaper.

## Who built it

An independent open-source project by GitHub user Abhixhek (identity not disclosed).
Posted on HN; this pool records 5 points and 1 comment.
_Name-collision note: GitHub also hosts "AA Kit (Agent As Everything)" and several
"AIKit" toolkits, all unrelated. This analysis covers only `abhixhek/aakit`._

_Read: publishing a tool whose three experiments produced no publishable number — along
with a full two-week protocol — suggests the author wants the method discussed more than
he wants impressive charts. That alone is worth reading._

## What it actually does

- **Extracts assumptions** → parses tasks and each implicit assumption from Claude Code
  session logs (JSONL), labeling provenance (read from something, or pure guess)
- **Judges what broke** → uses failing tests, file contradictions, and user corrections as
  evidence; finds defeated assumptions and computes the blast radius — which artifacts
  fall when one assumption falls
- **Computes a base rate** → experiment 1: how often silent assumptions are wrong in a
  load-bearing way, with confidence intervals
- **Tests asking policies** → experiment 2: four policies (never ask / always ask /
  ask only on divergence / ask on divergence with a budget) compared across equivalent
  tasks on success rate and token cost
- **Reports honestly** → every conclusion carries Wilson intervals and an explicit
  "kills the thesis" criterion

**What it explicitly does not guarantee**: none of the three experiments has produced a
publishable result in the current version — that is the author's own statement in the
README, not our judgment.

## What old behavior it replaces

Figuring out why an agent botched a job used to mean manually scrolling session logs and
retrospectively reconstructing why it did what it did and where the reasoning went wrong.
Slow, luck-dependent, and usually impossible to reconstruct after the fact.

aakit replaces that "post-hoc vibes review" with a repeatable measurement pipeline:
parse, extract, human adjudication, metrics. It is not the first agent-log analyzer,
but it is the first to make "implicit assumptions" an explicit measurement object and to
publicly admit the measurement is not yet accurate.

_Read: it replaces not a specific action but a habit — the default trust that "if the
agent finished, it finished right." Every team that dares to put agents in production
will eventually have to replace that habit._

## Business model

**None.** Open source, no license statement found, no paid or hosted service, and the
author's identity and background are undisclosed.

_Read: the usual commercialization path for a measurement tool is "open-source endpoint
plus paid team edition," but with experiments still unpublished, business model talk is
premature._

## Hard numbers

- This pool: 5 HN points, 1 comment (observed 2026-08-13); GitHub stars/forks not retrieved
- Experiment 2: 120 trials (10 tasks × 4 policies × 3 repeats, `claude-sonnet-4-5`).
  gated_multi 19/30 (63.3%) vs always 18/30 (60%) vs divergence_gated 13/30 (43.3%) vs
  never 10/30 (33.3%) — all confidence intervals overlap; the author declares experiment 2
  failed
- Strongest finding: the divergence gate asks 3.7x fewer questions but spends 25% more tokens
- Experiment 1: n=2, no base rate; experiment 3 (monitor recall): never run
- Three self-reported instrumentation bugs (header truncation inflating assumption counts,
  tool calls swallowed by the tool, session-ID exclusion ineffective)
- Self-assessed sample size: ~n=40/policy needed to separate gated_multi from never;
  the current n=30 is not enough

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Writing a PROTOCOL.md like this suggests someone genuinely bitten in production agent work — but the identity is unverifiable |
| Product insight | Making "implicit assumptions" measurable is the right question; "calibrate the extractor before trusting results" is rigorous methodology |
| Execution quality | Stdlib-only, local SQLite, privacy care (redaction and local execution) is real engineering — but three instrumentation bugs mean it is not yet trustworthy |
| Timing | More teams are putting agents in production and asking "how do we measure what agents did" — the need is growing faster than the tools |

## The call

**An honest draft of what an agent-era measurement tool should look like.** Its value is
not in the results — all three experiments came up empty — but in two things: it makes
explicit the "implicit assumptions" that are the most common failure point of agents and
the hardest for humans to spot; and it is honest about the measurement itself. It says
sample size is insufficient, reports its instrumentation bugs, and warns readers not to
peek at interim tables after a mid-run lead got reversed.

_Read: for a measurement tool, admitting you measured wrong is worth more than pretending
you measured right. That honesty is rare in AI tooling, and it is the only reason this
project deserves a note._

**The business judgment is simple though**: 5 HN points, an anonymous author, and no
experimental results. There is no reason to bet on this direction now, and no data to
suggest it works. This is "methodology worth filing, engineering still mid-road."

## What to watch next

① Whether stars cross 100 within three months — community acceptance is the first signal
  of validation
② Whether experiment 2 reaches sufficient samples (n≈40/policy) and produces a
  publishable number — whether the author's stated next step gets delivered
③ Whether anyone publicly reproduces or cites the protocol — outside adoption of the
  measurement method counts more than stars

## What you can take from it

**Product logic**: "make implicit assumptions explicit" transfers directly to reviewing
any proposal — have the agent (or a colleague) list assumptions before starting, and
review the assumption list, not just the conclusion. AI failures usually live in the
premises it took for granted, not in the code.

**Language**: terms like "load-bearing-wrong" cut through — separating "wrong but
harmless" from "wrong and everything collapses" is a distinction worth stealing.

**Engineering discipline**: calibrate before publishing numbers; state plainly when the
sample is too small; surface your own instrumentation bugs. This "no result rather than
fake result" discipline is worth more than any feature.

## Verdict

**Unproven.** The methodology has real substance and the engineering honesty is rare, but
the data is thin, the experiments are not run to completion, and the author is anonymous
— no investable basis exists. Check in three months whether it moved from "honest draft"
to "working tool."
