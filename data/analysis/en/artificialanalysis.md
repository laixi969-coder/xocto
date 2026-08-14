---
slug: artificialanalysis
name: Artificial Analysis
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Instead of picking models by a generic leaderboard, you build a benchmark around your own
task, run it, and read off score, cost, and latency per model — turning model selection from
a gut call into a reproducible measurement.

## Who built it

Artificial Analysis, an independent third-party model benchmarking company, co-founded by
George Cameron. It runs the model Intelligence Index (now v4.1) and a family of leaderboards,
publishes evaluations of 150+ models, and in mid-2026 added six industry indices (finance,
legal, healthcare, ops, engineering, economics) weighted by the O*NET occupational taxonomy.

_Read: benchmarking is its home turf, and Optima is an attempt to productize that capability.
This is not a newcomer — it is an established authority adding a "build your own" exit to its
existing leaderboards._

## What it actually does

- **Builds your own benchmark** → describe the task, attach examples, import your traces, or let
  the build agent draft tasks and rubrics with you; small batches (the sample page shows 24 tasks)
- **Four evaluation types** → Q&A (known correct answers), document Q&A (questions about your
  uploaded files), agentic (complete deliverables with tools), and interaction (simulated
  conversations, coming soon)
- **Runs across models** → every result carries score, cost per task, and time per task; your
  own agent can join the same run over HTTP
- **Two grading modes** → criterion-by-criterion rubric grading, or pairwise head-to-head with a
  judge model from major evaluations

**What it deliberately does not do**: no new models, no new benchmark sets, no "here is your
answer" decision. It only standardizes the evaluation itself.

## What old behavior it replaces

Two paths, both bad.

The first is reading generic leaderboards — MMLU, Intelligence Index, the averages. They have no
discrimination for your specific job ("I review contracts"). The top model is not necessarily
best on your task, but the average score makes you think it is.

The second is building your own eval: write a script, wire up APIs, run your few dozen examples,
then eyeball the outputs. Every team rebuilds the same harness, nobody maintains it, and every
new model release means redoing it.

Optima replaces all the dirty work in the second path: organizing examples, writing rubrics,
running batches, summarizing results. It compresses "build one eval" from person-days to token
counts, and turns "choose by leaderboard" into "choose by your own task."

## Business model

Usage-based: benchmarks are billed at the raw token cost of the models used, "with nothing added
on top" (their words); rubric grading is $0.125 per criterion per model; pairwise grading is
$0.375 per match. A credit hold is taken against a cost estimate before each stage, and only
actual usage is charged.

_Read: this is "evaluation as a service" pricing — the margin comes from grading and orchestration,
not from marking up model tokens. Note that the grader has become one of the judges, which is a
position that has to earn trust over time._

## Hard numbers

- Public track record: 150+ models, Intelligence Index v4.1, six industry indices, GDPval-AA v2
  (44 occupations across 9 industries)
- HN launch: 10 points, 0 comments (around 2026-08-13)
- Team size, paying Optima users: not disclosed
- Site traffic roughly 4.2M visits/month (third-party estimate, unconfirmed)

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A benchmarking company building a benchmarking tool; the fit is natural, and the company has years of public record |
| Product insight | Nails the gap where generic leaderboards have no discrimination for a specific use case, and hands the evaluation back to the use case |
| Execution quality | Not disclosed; but rubric grading priced at $0.125/criterion/model implies a mature judge pipeline behind it |
| Timing | Right moment. Model release cadence and agent workloads are both rising; "pick a model with your own task" is just being lit up |

## The call

**This turns "evaluation" from a public good into a private instrument.** Public leaderboards
compare across the whole field; Optima compares down one axis — "who is best on your task."
The two do not conflict; Optima actually feeds the leaderboards more users who want to get their
hands dirty.

**The transferable rule: selection only holds when evaluation belongs to the use case.** Any
situation where you repeatedly pick a supplier — clouds, models, APIs, even vendors — deserves a
scoring process built on your real tasks rather than a public ranking. A public ranking averages
away the one dimension that matters most to you.

**The risk is "who judges the judge."** A benchmarking company selling a grading tool lives or
dies on reproducibility and auditability. Criterion-by-criterion rubric grading is more auditable
than pairwise preference, and that design choice is correct.

**The other question**: is an evaluation one-shot or continuous? If every model release means
re-running, Optima's value scales with usage frequency. If it is used once at selection time, it
is a low-frequency tool with a limited ceiling.

## What to watch next

① Whether Optima publishes growth numbers for paid evaluations in three months (benchmarks run,
  enterprise customers)
② Whether results can be exported as reproducible reports — grading method, judge models, version
  numbers — since that decides whether enterprises adopt it in formal selection
③ Whether agents building and running benchmarks themselves becomes a first-class flow — that is
  the point where it actually changes how people work

## What you can take from it

**Product logic**: if you build anything that "helps the user decide," give the decision back to
the user's concrete task instead of offering an average. Averages drive traffic; private
evaluations earn the money.

**Positioning language**: the pricing phrasing is worth stealing — "raw token cost with nothing
added on top" plus "$0.125 per criterion" breaks cost down to a perceivable grain and reads far
more credible than "usage-based pricing."

**Pricing structure**: price grading and compute separately, and make money on the organization
layer, not on compute markups.

## Verdict

**Worth watching.** The company is credible, the direction holds, and the pain is real. But
Optima just shipped, HN response was lukewarm, and neither paid usage nor reproducibility has
been proven. Write it down and come back against the three checks above.
