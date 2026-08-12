---
slug: shuohao-skills
name: shuohao-skills
verdict: Strong pick
analyzed_at: 2026-08-11
sources: [github]
---

# shuohao-skills

## What it is in one line

Turns a novel into a shoot-ready short-drama kit: character bibles, look prompts, voice profiles, episode outlines.

## Who built it

A Chinese developer working under the handle `eternityspring`.
The first thing in the README isn't the product — it's a WeChat ID for a **paid community**.
He knows exactly what he is selling.

_Read: this is not a technical project that happened to get open-sourced.
It's a content business with a deliberate revenue path._

## What it actually does

Two skills, both fed to an AI coding agent (runs in Claude Code and codex):

- **Drop in a novel** → out comes a character set: portraits, look prompts, voice prompts, reference sheets.
  Report language and art style are configurable
- **Drop in a novel** → out comes a five-part adaptation package: adaptation notes, cast list,
  payoff beats, episode synopses, asset checklist
- **Drop in an existing outline** → it runs a review pass, checking against 13 quality gates one by one
- Those 13 gates are **scripted checks, not model judgment**. That matters more than it sounds:
  the standard is fixed and reproducible, so a script doesn't pass today and fail tomorrow

**What it deliberately does not do**: no image generation, no editing, no shooting.
It handles the stretch before the camera turns on, then hands the work off.
That restraint is exactly why it can go deep.

## What old behavior it replaces

Pre-production on a short-drama adaptation. The old way: a writer reads the novel and hand-writes character bios, an art lead produces reference sheets, a director breaks it into episodes, a producer lists the assets. Three to five people, one to two weeks per series.

It compresses that into "drop in a novel." **The old behavior is unmistakable, which is the strongest signal a need is real.**

## Business model

**Open source as the hook, a paid community as the till.** The code is free; the money is in a WeChat group.

This is a standard playbook among independent Chinese developers, but the tradeoff is worth naming:

- Upside: zero acquisition cost, stars convert straight into members, and a group is a high-frequency touchpoint
- Cost: revenue is capped by group size, and it depends entirely on one person's reputation

_Read: the pricing logic holds, but the ceiling is low. This is one person's business, not a company._

## Hard numbers

- Open-source traction: 655
- Two skills: novel-characters, novel-outline
- The outline skill runs **13 quality gates, all scripted checks**
- Paid community size: undisclosed

## Four-way read

| Dimension | Read |
|-----------|------|
| Founder-product fit | High. He makes AI short dramas himself; the product is his own tooling, released |
| Product insight | High. He skipped "generate video" for "prepare the material" — the most labor-intensive, least-served step |
| Execution quality | Above average. Scripted gates instead of model judgment is the more reliable engineering choice |
| Timing | Right on. AI short drama is hot in China, and every tool is crowded around generation |

## The call

The valuable thing here isn't the code. It's **where he chose to stand**.

Everyone is fighting over generating footage. He walked upstream to preparing what gets generated —
turning a novel into character assets, turning a character's look, voice, and temperament into
reusable objects, turning adaptation logic into episode synopses and payoff beats. In the traditional
pipeline that stretch eats the most people, leans hardest on experience, and is the least likely
to become a product, because it isn't sexy and it demos badly.

**The transferable rule: when everyone in a category piles onto the most visible step, the value tends to settle in the dirty, tiring step just upstream of it.** Generating footage is a bloodbath. Deciding what to feed the generator is empty.

The cost is just as clear: he has tied the product to himself. The README opens with a QR code, which
means growth is capped by one person's community management rather than by the product. If he stops
updating, 655 stars turn into dead code overnight.

It and open-ai-canvas are two bets on the same judgment: one on the **upstream** (preparing material),
one on the **container** (arranging it into a film). Which one is right depends on where the real
bottleneck in short-drama production sits.

## What to watch next

1. **Whether the paid community clears a few hundred people** — clearing it proves the revenue path; not clearing it makes this a hobby
2. **Whether the skill count keeps growing** — stalling at two would suggest he hasn't run the full pipeline himself either
3. **Whether anyone has shipped an actual series with it** — that's the only evidence that can disprove "shoot-ready"

## What you can take from it

The most portable idea here is the 13 quality gates: **turning creative quality into hard constraints a script can check.** Most teams treat "is this good?" as a judgment call made late by whoever is senior. He turned it into a fixed, reproducible gate that runs before anyone looks at the work.

**Positioning**: the README opens with "drop in a novel, get this," plus one screenshot of the output.
That structure beats any feature list. One line of input, one image of output, nothing explained in between.

**Pricing**: free tool, paid understanding. The specific shell here (open source plus a chat group)
only works for a developer audience, but the skeleton transfers: give away the thing that does the work,
charge for the judgment about how to use it.

## Verdict

**Strong pick.** Not because the execution is remarkable, but because it proves that the unglamorous
upstream step has buyers — and it shows the mechanism for turning taste into a checkable rule.
