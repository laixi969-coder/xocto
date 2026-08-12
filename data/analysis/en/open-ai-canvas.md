---
slug: open-ai-canvas
name: open-ai-canvas
verdict: Strong pick
analyzed_at: 2026-08-11
sources: [github]
---

# open-ai-canvas

## What it is in one line

One canvas holds a whole production: pull character assets out of a novel, then arrange storyboards, images, video, and audio into a film.

> Its own line is "take a story from words to the screen" — better writing than most commercial
> products manage, but still a literary flourish rather than a description of what it does.

## Who built it

The GitHub organization `ddcat-ai`. Very little else.

**One thing has to be recorded**: the project homepage points at `ddcat.pronhubcn.com`.
The shape of that domain — a misspelling of a well-known adult site plus a cn suffix — is
seriously suspicious. It may be a developer's throwaway server. It may be something else.

_Unresolved, and it needs checking. Until it is, don't cite this project anywhere formal,
and don't upload material to that domain._

## What it actually does

- **Feed in chapter text** → it works out the characters and the structure of the plot
- **Freeze a character into an asset** → look, voice, and temperament bound into one reusable object
  that every later generation step references, which is how you stop "the same character looks
  different in all ten images"
- **Arrange it on an infinite canvas** → storyboards, images, video, and audio organized in one space
  instead of hauled between a dozen tools and folders
- **Wire in multimodal generation** → call external generators for images, video, and voice from inside the canvas
- **Agent workflows** → chain those steps into an automated run

**What it deliberately does not do**: it trains and serves no models of its own.
It is a container; every generative capability comes from an external API. That is its
biggest lever and its biggest fragility at the same time.

## What old behavior it replaces

The real AI filmmaking workflow today is: write the outline in a chat model, generate stills in one image tool, generate clips in a video tool, stitch it in an editor, and move material between all of them through docs and chat apps.

**The pain isn't in any single tool. It's in the hauling between them**: a character's face doesn't
match across tools, the shot order lives in someone's head, and the assets are scattered across a
dozen places. This is what open-ai-canvas is replacing, and the old behavior is unmistakable.

## Business model

**AGPL-3.0.** That is not a casual pick. AGPL requires anyone who offers a network service based on
the code to open-source their version too. It is the classic setup move for dual licensing:
stop the big platforms taking it for free, push commercial users toward buying a license.

_Read: choosing AGPL says the author has thought about revenue, and a commercial license or
hosted edition is probably coming. There is no pricing yet — this is still the accumulate-stars phase._

## Hard numbers

- Open-source traction: 535
- Version v1.0.43 — the version number says it iterates often, not a toy thrown over the wall
- Users, revenue: undisclosed

## Four-way read

| Dimension | Read |
|-----------|------|
| Founder-product fit | Unknown. The author's background can't be traced, and that's the biggest gap |
| Product insight | High. "Character assets are reusable" is exactly where multi-tool workflows break |
| Execution quality | Above average. v1.0.43 with multimodal integration is real work, but there's no third-party usage to point to |
| Timing | Right, slightly early. There are plenty of AI video tools; nobody has won the container that connects them |

## The call

This is a bet on **the container, not the generator**.

It builds no model. It builds the canvas that organizes what the models produce. The logic underneath:
model quality keeps rising and converging, so what's left to compete on is **who owns the structure of
the work** — the relationships between characters, shots, and assets — not whether any single frame is pretty.

**The transferable rule: when upstream capability commoditizes fast, value migrates to the structure that organizes that capability.** This is the same move a model gateway makes one layer down. It's just happening at the creative layer instead.

The cost is that this kind of product is brutally hard to run: it has to stay wired into a pile of
fast-moving generation APIs, and any one of them changing an interface breaks a link. It also has no
moat — a canvas is easy to copy, so the only real barrier is the data structure behind asset
organization, and it isn't obvious yet how deep that goes.

It and shuohao-skills are two bets on the same judgment: one on the **upstream** (novel into material),
one on the **container** (material into a film).

## What to watch next

1. **What `ddcat.pronhubcn.com` actually is** — nothing else matters until that's answered
2. **Whether a commercial license or hosted edition appears** — AGPL is the setup; watch for the payoff
3. **Whether the character asset schema stabilizes** — refactoring it every release would mean the author hasn't settled it either

## What you can take from it

Go read the character asset schema. **How it defines a character's look, voice, and temperament, and keeps those consistent across separate generation steps, is the hardest problem in any multi-step creative pipeline — and someone has published an answer.**

**Positioning**: "take a story from words to the screen." The structure is worth stealing —
it doesn't say what the product does, it says what happens to the user's material.

**Pricing**: AGPL plus a commercial license is a ready-made template for anyone who wants open source
to do their marketing without handing the product to a competitor.

## Verdict

**Strong pick, but check that domain first.** As a public reference for how to organize a
multi-step creative workflow, reading its code beats reading ten write-ups.
