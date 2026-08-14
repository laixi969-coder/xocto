---
slug: ai-short-drama
name: ai-short-drama
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A system that compiles short-drama tropes — "fake weakling who is secretly
strong, rebirth, system, hidden boss, comeback" — into a story engine with
arcs, character consistency, per-episode payoffs and binge hooks: an open-source
Skill for Codex and Claude Code that owns the story and serialization state
instead of stuffing an entire series into one generation prompt.

## Who built it

Hao0321, an independent developer, open source on GitHub. The repo's content and
docs suggest the author practices this exact "AI toolchain for short-drama
production" workflow and distilled the lessons into a reusable Skill.

_Read: the author is very likely a short-drama practitioner or heavy experimenter
— the granularity (eight-dimension scoring, per-shot briefs, state deltas) is not
something an outsider could invent. The honesty shows in the automation-boundaries
section: login, payment, and compliance uncertainty must pause for a human, which
means the author knows what AI must not touch._

## What it actually does

- **Scout** → researches current tropes, platforms and cases
- **Greenlight** → an eight-dimension score picks concepts worth testing
- **Bible** → characters, world rules, ability costs, reveals, and the villain ladder
- **Season / Episode** → plans micro-arcs, writing episodes with a dominant turn,
  payoff, cliffhanger and state delta
- **Studio** → routes between serialized episodes, a complete micro-drama, a
  single-shot hit, grid moments, and continuous long shots
- **Model-aware production** → records model duration / reference quota, locks
  recurring-character three-views, global style, and per-shot timelines
- **Produce** → outputs a schema-validated production pack, fixed entity IDs,
  per-shot generation briefs and an edit handoff
- **Audit** → separately diagnoses concept, episode, season, production and
  packaging problems

**Automation boundaries**: the core Skill can independently finish concept,
script, production pack and validation; media prompts and generation suggestions
require ai-media-generator; assembling a final MP4 requires a separate edit
executor; and login, extra payment, model-capability mismatch, compliance
uncertainty and official public release must stop for confirmation.

**What it deliberately does not do**: include the author's private series bibles,
character assets, or unpublished story settings; model capabilities are not
hardcoded as permanent facts and must be re-verified before production.

## What old behavior it replaces

Making AI short dramas used to mean two paths, both with fatal flaws:

**One prompt for the whole series** — hand "write a 10-episode short drama" to a
model; the opening works, then characters drift and the world logic collapses,
because a single prompt's context window cannot hold the state of a serial. This
is the root of "one good episode is easy; ten that hold together is the hard part."

**Human-managed serialization** — character sheets, ability costs, villain
ladder, per-episode hooks, all tracked in documents and spreadsheets, re-aligned
by hand for every episode. It runs on human discipline — a production-manager
grind that breaks the moment the person changes.

ai-short-drama replaces both by moving serialization state — character
consistency, style locks, per-shot timelines, inter-episode hooks — out of a
single prompt and out of human memory, into checkable, resumable state files on
disk. It attacks the real bottleneck of industrializing short drama: continuity.

## Business model

**None.** MIT open source, free, no paid tier, no services.
(The repo cites aizhuiguang.tech's public "generalizable product
mechanisms" as the reference for the Studio layer, noting it is an independent
reimplementation that copies neither copy nor code, with an evidence registry.)

_Read: this is the classic "trade methodology for attention" play. Short drama is
one of the hottest content tracks of 2026, and releasing the workflow as a
reusable Skill is a bet that whoever defines the short-drama production pipeline
owns the category's ecosystem slot. Monetization would be later — paid templates,
custom production, or taking orders._

## Hard numbers

- 48 stars / 9 forks (this batch's observation)
- MIT, Python scripts (drama_lint.py / studio_lint.py) plus schema validation and
  unit tests
- Install is a clone into `~/.codex/skills/` or `~/.claude/skills/`
- Users and actual episodes produced: not disclosed
- Status: watching; the repo is being updated continuously

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The granularity of the workflow means real production, not a theoretical framework |
| Product insight | Correctly identifies continuity as the industrialization bottleneck, with a clear sense of "don't stuff a whole series into one prompt" |
| Execution quality | Schema validation plus lint plus unit tests plus explicit automation boundaries; far beyond the average skill repo |
| Timing | Well aimed. Short drama is where the money is flowing, and AI toolchains are just starting to penetrate production |

## The call

**It bet on the right bottleneck — continuity — and did the engineering properly.**
Generating a single episode stopped being the problem long ago; keeping ten
episodes consistent is. Turning characters, style, timelines and hooks into
checkable, resumable state files is a production-grade idea, not a demo-grade one.

**Honesty is its most valuable asset.** Writing out that login, payment,
compliance uncertainty and public release must pause for a human — and that model
capabilities must not be hardcoded as facts — is rare in AI-generated-content
tooling and shows the author knows which steps AI must not touch.

**But its reach is limited.** Forty-eight stars says it is still a niche
methodology repo, and it depends on coding agents like Codex and Claude Code as
the execution environment — which filters out most short-drama practitioners, who
are not programmers. The positioning is "people who use agents make short dramas,"
not "people who make short dramas use agents."

## What to watch next

① Whether stars clear 200 in three months — word-of-mouth velocity for a
methodology repo
② Whether any actually produced short drama publicly credits this workflow —
stronger evidence than stars
③ Whether commercialization appears (paid templates, production services, a
content account matrix)

## What you can take from it

**Product logic**: when building AI content-production tools, decide first which
steps must stop for a human to confirm, then talk about automation. Writing the
automation boundary into the docs is not conservatism; it is professionalism, and
it decides whether the tool is trusted in real production.

**Positioning language**: put the tropes ("fake weakling, rebirth, system") in
the first line of the README so the target reader instantly knows "this was made
for me." Vertical tools should open with the vertical's own jargon.

**Engineering structure**: define production contracts with schema files
(production pack, studio plan) and validate with lint scripts — making AI output
machine-checkable is a precondition for AI output entering a production pipeline.

## Verdict

**Unproven.** Right instinct, serious engineering, honest boundaries — but slow
diffusion, a narrow audience, and no commercialization yet. It represents one
sample of the "open-source AI content-production methodology" route. The
continuity insight is worth remembering; its merits wait for real works and real
revenue to verify.
