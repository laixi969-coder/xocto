---
slug: applied-micro-skills
name: applied-micro-skills
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A skills pack for Claude Code and Codex built for empirical applied-microeconomics research,
covering the full pipeline from data acquisition and LLM-assisted classification to
econometrics, publication tables, and delivery — where the selling point is not "publish
faster" but "make sure the numbers you publish actually reproduce from the data."

## Who built it

Solo author kennethkhoocy. MIT license, repo created 2026-07-22, 47 stars / 0 forks. Primarily
Python scripts plus Markdown skill definitions. No company, no team, no funding.

_Read: this is the "researcher builds tooling for fellow researchers" shape. Zero forks and no
issues mean no community yet; but the quality of the skills — a whole method built around
reproducibility verification — reads like solutions written by someone who got bitten by the
problem in their own research._

## What it actually does

Eighteen self-contained skills in five groups:

- **Reproducibility and verification** → flagship `adversarial-empirical-review`: adversarially
  audits whether every number in a paper's tables can be reproduced from the underlying data,
  via deterministic checks, cross-model reviewers, and a blinded review panel; also supports
  full-reproduction-from-raw-data mode
- **LLM-assisted classification** → `annotator-input-parity-check` (confirm the model sees the
  same evidence a human annotator did), `llm-gold-bound-failure-check` (when a gate fails,
  first diagnose whether the gold-standard labels are the problem, instead of burning money on
  prompt tweaks), `llm-campaign-drift-gate` (cheap canary tests to stop model-alias drift
  corrupting multi-day labeling), `adjudication-sheets` (human adjudication tables with
  byte-level evidence parity), `asyncopenai-concurrency-httpx-pool` (fixes the ~100-concurrency
  ceiling in batch scorers)
- **Econometrics and data infrastructure** → `event-study-cars` (cumulative abnormal returns
  engine, validated against Stata's eventstudy2 to floating-point precision), `wrds` (WRDS
  query patterns: Compustat/CRSP/FactSet etc.), `stata` (drives Stata through pystata with
  in-memory pandas exchange), two pyfixest debugging skills
- **Tables, figures, citations** → `latex-empirical-tables` (estout-style regression tables),
  `stata-style-figures` (matplotlib styled to Stata aesthetics), `cite-placement` (verified
  references only, explicitly "never fabricates citations")
- **Sources, documents, delivery** → `lit-review-orchestrator` (document-driven literature
  search), `latex-to-word`, `markdown-to-pdf`, `download-gated-pdfs` (pulls real PDF binaries
  from bot-blocked sites via the Wayback Machine)

## What old behavior it replaces

In empirical economics, "can this number be reproduced" used to be answered by human eyeballs
and patience: a reviewer or RA opens the paper, lines up data and code, and manually verifies
every table cell. LLM-assisted labeling was checked by human spot-checks. "Can we trust last
week's model-run classification" was answered by rerunning and hoping.

This pack replaces the repetitive half of that human review chain — turning adversarial
reviews, labeling quality gates, and table-transformation checks into repeatable automated
steps. It also replaces a more subtle default: in AI-assisted research, the default was to
trust model output; this inserts an explicit verification gate at every step.

_Read: the most valuable thing here is the author's obsession with verification. Most people
using LLMs for research are accelerating generation; this author is designing for proving that
every step after generation did not silently break. That is a perspective only someone who has
been educated by top-journal reviewers writes._

## Business model

**Not disclosed.** MIT open source, no paid service, no SaaS, no sponsor page.

_Read: the currency of academic tooling has always been reputation and methodological
influence, not direct revenue. If these skills enter real lab workflows, the author's scholarly
reputation is the more tangible return._

## Hard numbers

- **47 stars / 0 forks / 0 open issues.** Repo created 2026-07-22, MIT
- 18 skills across reproduction, LLM classification, econometrics infrastructure, tables, and
  literature delivery
- Verifiable engineering details in the core skills (validation against Stata to floating-point
  precision, a real httpx connection-pool concurrency fix)
- Users and lab adoption: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author has clearly been bitten by "the number won't reproduce" repeatedly |
| Product insight | Nails the real pain in empirical research — verification — with unusually careful method design (canary tests, byte-level evidence parity) |
| Execution quality | Solid skill definitions with reproducible engineering detail, not prompt stacking |
| Timing | Early. AI-assisted research is just starting; most researchers are still at "make AI do the work," not "prove the AI's work is right" |

## The call

**This is a guardrail system for AI-assisted research, with a real insight but no evidence of
traction yet.**

It hits a genuine problem: the biggest controversy in LLM-assisted empirical research is not
speed but trustworthiness. The author answers with an explicit verification apparatus — not "I
guarantee the results are right," but "every step can be checked." A skill like
`llm-gold-bound-failure-check` — diagnose whether the gold standard is the problem before
tweaking prompts — is the kind of detail that only comes from having lost real money to bad
classification. That cannot be faked.

**But the evidence is thin.** 47 stars, zero forks, solo author, two weeks old, and zero
adoption signals. A skills pack only proves itself inside real research workflows — until then
it is one person's well-organized notes.

**The transferable rule: design a verification layer for AI output rather than optimizing
prompts.** When the cost of error is high — retracted papers, contested labels — what users
actually buy is "provably not broken," not "usually right." Any high-error-cost domain
(research, finance, healthcare) should be built this way.

## What to watch next

① Whether forks and real adoption cases appear in three months — someone actually using it in
their paper workflow
② Whether skills are added or updated (a moving project means the author is still using it)
③ Whether it appears in a known lab's or course's recommended list — academic tools spread by
word-of-mouth endorsement, not rankings

## What you can take from it

**Product logic**: when building AI-assisted tooling, make verification an explicit product
feature, not an implicit promise. Three moves to copy: add a reproducible checkpoint to every
output step (canary tests); when a gate fails, diagnose whether it is input quality or model
quality before deciding what to change; and demand byte-level evidence parity, leaving no room
for "approximately consistent."

**Positioning language**: "Never fabricates citations" — one negative commitment builds more
trust than a hundred claims of reliability.

**Pricing structure**: none. An open-source academic tool has no transferable pricing model.

## Verdict

**Unproven.** The pain is real and the method is meticulous, but 47 stars, zero forks, and zero
adoption evidence put this at "personal project" stage. No doubt the author is a genuinely
informed researcher; the open question is whether this moves from personal notes to a used
tool. Revisit in three months against the checks above.
