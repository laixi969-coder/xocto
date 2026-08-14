---
slug: promentor
name: ProMentor
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

An agent skill that turns any real open-source project into a step-by-step hands-on course: install
it into Claude Code / Codex / DeepSeek Harness and the AI stops writing code for you and starts
making you write it yourself, then grades you.

## Who built it

A personal open-source project by Lyn-77, repository created 2026-07-31, 41 commits. README,
command reference, architecture notes, and a release-packaging flow are all polished to near-product
level. No license file.

_Read: a solo author who took engineering completeness to product level — command system, web
dashboard, plugin registration. But the author's background, target users, and any evidence of real
use are all undisclosed._

## What it actually does

- **Generates a course** → /promentor init scans the project architecture and produces a curriculum
  outline; once confirmed, it generates lectures, labs, and behavioral tests chapter by chapter
- **Staged learning** → /promentor learn delivers the lecture, walks you through annotated source,
  and guides you to hand-write the core logic
- **Behavioral-test grading** → /promentor test runs behavioral tests and tells you what passed,
  what failed, and why
- **Layered hints** → /promentor hint reads your code and test results and gives layered hints for
  the exact error — direction first, then approach, never the answer
- **Submit and review** → /promentor submit runs the full test suite and locks your score;
  /promentor review diffs your implementation against the original source and explains the design
  decisions
- **Progress and dashboard** → /promentor progress for totals; a web dashboard (Next.js) shows
  completion, chapter states, and scores

The learning model is a chain: learn the concept, read the source, implement the lab, run the
tests, submit and review, master the system design.

## What old behavior it replaces

Three old paths for learning to code from a real codebase:

- **Reading the source directly** → random jumping with no dependency order; ProMentor generates a
  dependency-ordered path
- **Watching video courses** → watching someone else write; ProMentor requires you to hand-write the
  core logic
- **Blogs and docs** → fragmented knowledge points; ProMentor requires a full understanding of one
  system's design philosophy

For the agent itself, it replaces passive Q&A ("explain this repo to me") with an active, tested,
graded learning loop. The critical transfer is: grading does not come from the AI eyeballing
answers, it comes from behavioral tests.

## Business model

**Not disclosed.** Free and open source, no license declaration, no paid tier, no cloud service.

_Read: skill packs are a zero-barrier category — anyone can write one, and they are naturally hard
to charge for. The real competition is not distribution; it is whether the behavioral-test grading
design holds up on projects at real scale._

## Hard numbers

- **48 stars, 1 fork, 0 open issues** (fetched 2026-08-14). Created 2026-07-31, 41 commits
- Release zip ~3.7 MB (skill + prebuilt dashboard + plugin)
- No license file; no usage numbers, no user evidence
- Not seen on HN; stars from organic GitHub traffic

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Solo author with higher engineering completeness than most skill projects; background unknown |
| Product insight | Turning pedagogy (staged chapters, behavioral tests, layered hints, locked scores) into an agent skill is a replicable pattern |
| Execution quality | Command system + Next.js dashboard + DSH plugin + release flow, complete; missing license is a red flag |
| Timing | "Real repo as textbook, system design over algorithm drills" is a genuine need; 48 stars says it is unvalidated |

## The call

**The pattern is interesting; the category is cheap.**
"Behavioral-test grading + layered hints without giving answers" is one of the few genuinely
pedagogical designs in this batch — grading comes from executable tests, not a model's subjective
score, and hints escalate from direction to approach. Both are directly copyable by anyone building
an "AI tutor" product.

**The ceiling is scale.** Generating discriminating behavioral tests works on a small project. Can
it still produce tests with real discriminative power on a multi-ten-thousand-file repository? That
is its true scale ceiling, and the README does not answer it.

**Risk list**: solo author, no license, no user evidence. Skill packs are easy to copy and hard to
moat.

## What to watch next

① Star growth, and whether anyone publicly reports completing a full course on a real project
② How large a codebase behavioral-test grading still holds up on (the scale ceiling)
③ Whether a license appears and whether contributors show up (survival signals)

## What you can take from it

**Product logic**: three pieces for teaching AI products — generate a staged course from a real
artifact (project source); grade with behavioral tests instead of letting the AI score against a
reference answer; give layered hints (direction, then approach, never the answer). Directly usable
for "AI tutor" or "generate a course from your data" products.

**Positioning language**: one line worth stealing — "What you learn is not an algorithm drill, it
is the architecture-design ability of a real system."

**Pricing structure**: none. Free and open source.

## Verdict

**Unproven.** The teaching design has incremental value, the category has a shallow moat, and
validation is thin. Come back in three months against the three checks above.
