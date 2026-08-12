---
slug: douyin-tiktok-story-skill-agent
name: Douyin / TikTok Story Skill
verdict: Worth watching
analyzed_at: 2026-08-11
---

## What it is in one line

A short-video script library you search by story tags, installed inside an AI agent as a source of reference material.

## Who built it

The GitHub account `liujunxibaba`, a Chinese developer.

The engineering details give away his actual setup: the installer is PowerShell (a Windows user),
it installs under `$HOME\.codex\skills\` (Codex, not Claude Code), and nothing touches the network.
**This is someone using it to do his own work, not a demo built to be looked at.**

## What it actually does

- **Search by story element** → `search "campus teacher-student misunderstanding conflict-in-first-3-seconds" --top-k 5`,
  pulling matching script samples by tag combination
- **Runs fully offline** → install and use never hit the network; material never leaves the machine
- **Installs into Codex as a skill** → the agent calls it; nobody browses a library by hand
- **Health check** → verifies database integrity after install
- **Code and data separated** → skill code in one repo, script database in another, licensed separately

**What it deliberately does not do**: it doesn't write scripts, make video, or handle shooting.
It only does the step of finding the right reference sample.

## What old behavior it replaces

A short-video writer looking for references actually does this: open the app, scroll comparable content, manually note the good ones, build up a personal document, and then fail to find anything in it next time.

**The old behavior is unmistakable, and it's pure manual labor.** A writer's time should go into
adapting, not into "I remember something like this but I can't find it."

That search example says a lot about how well he understands the work:
**"campus / teacher-student misunderstanding / conflict in the first three seconds"** — the first
two are subject matter, the third is **structure**. Anyone who indexes on "conflict in the first
three seconds" has written short-video scripts with their own hands.

## Business model

**Code is MIT; the database is licensed separately.** The README is explicit:
this repo does not contain the real database, and the database repo declares its own license.

The split is deliberate: **give away the engine, sell the content.**
Anyone can read the code, but it doesn't run without the database, and the database terms are elsewhere.

_Read: the pricing logic holds and it's healthier than pure open source. The risk is provenance —
if the script samples were scraped from a platform, its copyright position is as fragile as
open-kimi-ppt-skill's was._

## Hard numbers

- Open-source traction: 233
- Two paired repos (skill + database)
- Database size, licensing terms, pricing: undisclosed

## Four-way read

| Dimension | Read |
|-----------|------|
| Founder-product fit | High. "Conflict in the first three seconds" is not a dimension an outsider invents |
| Product insight | High. It attacks "find the reference" rather than "write the script," dodging the most crowded step |
| Execution quality | Middling. Local search plus a health check is complete work, but not technically hard |
| Timing | Good. Short drama and creator-led storytelling are hot, and every tool is bunched at the generation end |

## What to watch next

1. **Where the database came from and how it's licensed** — this single question decides how long it lives, above every other metric
2. **Whether the database keeps growing** — a reference library that stops updating is worthless within six months
3. **Whether a payment path appears** — "separately licensed" is a declaration until someone can actually pay for it

## The call

This project and shuohao-skills are two executions of the same judgment:
**both sidestep generation and work on the step before it.**

shuohao turns a novel into shoot-ready material; this one finds the right reference sample.
Both bet on the same thing: **the bottleneck in AI short video is input, not output.**
The models can already write and shoot. What's stuck is deciding what to write and what to model it on.

**The transferable rule: when generative capability is in surplus, the scarce things are judgment and a material library — the first is hard to productize, the second isn't.** Which makes building the library the most concrete business available at this stage.

The cost comes in two layers. **Copyright first** — if the database was scraped, it can repeat
open-kimi's ending at any time, and he clearly senses it (splitting the database out with its own
license is risk isolation). **Then the moat** — search itself has no technical barrier, so the
moat equals the quality and size of the database, and that requires continuous manual curation
that can't be automated.

The Windows + PowerShell + Codex combination is worth noting too: that isn't the mainstream
developer stack, which says his target user is **someone making content on Windows**, not a programmer.
That judgment may well be right.

## What you can take from it

**Index reference material by structure, not by subject.** Anyone can tag a topic; "conflict in the first three seconds" is what a writer is actually searching for. Choosing structural dimensions over subject dimensions is what makes a reference library worth opening twice.

**Business model**: open the code, license the data separately. That's a healthier structure than
a free tool plus a paid chat group — a group has to be maintained by a person, a database
accumulates as an asset. If you want to productize a method, this is the shape worth copying.

**Risk note**: read this next to the other case from the same day (a 1,600-star repo wiped for
copyright). Provenance is a live risk for anything built on a material library.
If you build one, the sources have to be clean from day one.

## Verdict

**Worth watching.** The product judgment is right and the structure is sound, but everything
hangs on whether the database is legally clean, and public information doesn't say.
Come back in three months; whether it's still there is the answer.
