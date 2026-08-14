---
slug: merge
name: Merge
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Candidates review a real PR the way they would at work, while an AI agent plays the
engineer who replies to their comments in real time — hiring tests engineering
judgment instead of algorithm puzzles.

## Who built it

Five founders (including Harshith Latchupatula) who claim 250+ interviews collectively,
from startups to FAANG+ to quant shops. Launched at launch 2026-08-07 (119
upvotes, #10 on the daily board). Website mergeoa.com — currently demo-booking only.

The founders' own pitch contains a key observation: at their own companies PR counts
have nearly tripled, most of them have not hand-edited a line of code in a year, teams
increasingly rely on code and architecture reviews — and the hiring process has not
changed at all. Even the AI-assisted interviews they ran still scored code output.

_Read: this is a product built by people annoyed at the status quo. Five interview
veterans pushed to act by the double absurdity of Leetcode interviews and "testing
handwritten code in the AI era." The pain is described concretely — "haven't written
a line in a year but review code daily" — which is the real shape of work after AI
assistance has penetrated._

## What it actually does

- **Simulates real code review** → candidates get a small codebase plus a PR, and
  comment on correctness bugs, refactors, and vulnerabilities the way they would on
  the job
- **AI agent responds in real time** → each comment is answered with a code change or
  a reply, simulating a real engineer; candidates iterate up to 5 revisions or until
  time runs out
- **Multi-dimensional scoring** → bug/vulnerability coverage, communication quality
  (is the feedback efficient and constructive?), and efficiency (how many revisions
  and tokens the review took, and what it cost)
- **Calibrated by level and domain** → difficulty from intern to principal;
  specializations across frontend, backend, security, infrastructure, platform,
  distributed systems, data pipelines; language stacks can be restricted
- **Token efficiency as the differentiator** → claims to be the first platform that
  shows exactly how efficient a candidate is with token use, LLM cost, and PR
  revisions

## What old behavior it replaces

Hiring engineers used to test two things, both broken by AI:

**Leetcode algorithms** — testing pure no-AI coding ability, when the real job is
reviewing code, especially reviewing what another engineer's AI generated with little
context of your own. The founders say it plainly: as agents develop, writing code will
not be the hardest ability an engineer has.

**Take-home assignments** — candidates go home with the same AI tools the company uses,
and no one can tell whether the submission is theirs. A PH commenter asked "how do you
stop a candidate from just running the whole thing through their own AI review tool?"
The founders' answer is practical: their codebases are small, but the in-PR bugs that
require codebase context defeat candidates who hand the whole repo to their agent —
someone who reviews without that context shows up in missing coverage or wasted
revisions.

**What it replaces operationally**: a 1–2 hour interview graded by one interviewer's
subjective impression becomes a 30-minute asynchronous assessment where every revision
is objectively recorded. The object of evaluation shifts from "writing code" to
"judging code."

## Business model

**Pricing not disclosed; the website only offers "book a demo."**

_Read: assessment is a mature paid category (CoderPad, HackerRank, Codility all charge
per seat or per assessment), and Merge will likely follow. But demo-only, no
self-serve pricing means the product is early and the revenue loop is not yet closed._

## Hard numbers

- launch 2026-08-07: 119 upvotes, 5 comments, #10 on the daily board
- 5 founders, 250+ interviews of collective experience
- Candidates complete a 30-minute assessment; up to 5 AI revision rounds
- Users, revenue, funding: not disclosed (demo booking only)

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Five interview veterans with scenario-specific pain; genuine motivation |
| Product insight | Aimed correctly (judgment over output), and the token-efficiency dimension hits the new competency AI work demands |
| Execution quality | The review-loop + multi-dimensional scoring + scorecard design is complete; but the quality of the AI agent's "conversation with the candidate" is unverified independently |
| Timing | Good. "Leetcode is broken" is already consensus among hiring teams; everyone is looking for a replacement |

## The call

**The direction is right — the kind of right answer that was always going to be built.**
The absurdity of AI-era hiring: candidates write with AI while interviews test writing
without it. Merge switches the assessed object to "reviewing AI-written code" — which
is exactly what happens on the job. That one switch makes the assessment valid by
construction.

**Both reservations deserve honesty**:
First, the **AI-versus-AI arms race**. Candidates carry the same AI tools; the PH
commenter's "eventually it's AI grading AI on both sides" is a question every AI hiring
product faces. Merge's defense is codebase context, but that is a catch-up-able design,
not a moat.
Second, **incumbents will follow**. CoderPad and HackerRank already own the customer
base and question bank; "review this PR" as a new question type is a scheduling problem
for them. Merge's head start is probably a quarter to half a year.

**Worth watching**: insight, timing, and founders are all right, but the revenue loop
is open, the moat is not built, and 119 upvotes validates the direction, not the product.

## What to watch next

① Whether any named paying customer or case study appears — enterprise-side
credibility is everything for a hiring product
② Whether self-serve pricing opens within three months — moving from "book a demo"
to "buy online" is the revenue-loop signal
③ Whether CoderPad/HackerRank ship a "PR review" question type — incumbent timing
tells you how long the window lasts

## What you can take from it

**Product logic**: for assessment products, the most important thing is not "what you
measure" but "is what you measure what actually happens on the job." Any training,
hiring, or certification product should run this replacement test once — swap the
question for a slice of the real workflow and assessment validity jumps immediately.

**Positioning language**: "test judgment, not output" and "the hardest skill in the AI
era is reviewing someone else's AI's code" — compressing an industry pain into a
counter-intuitive sentence is the most effective way to open a conversation with hiring
teams.

**Pricing structure**: not disclosed; nothing to borrow.

## Verdict

**Worth watching.** A correct answer forced into existence by the real shape of work:
hire for reviewing code rather than writing it, and make token efficiency a measurable
assessment dimension along the way. But it is still in demo-booking phase, the moat is
shallow, and incumbents can follow at any time. Come back in three months against the
three checks above.
