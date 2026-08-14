---
slug: languagereactor
name: languagereactor
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A browser extension that turns Netflix and YouTube into a language classroom: dual subtitles while you watch, click-to-look-up words, line-by-line replay, and one-click export of vocabulary to Anki.

## Who built it

Language Reactor (formerly Language Learning with Netflix), an independent product living mostly as a Chrome/Firefox extension, registered in Vietnam, maintained long-term by a small crew. It sits outside any big-model ecosystem — the core is subtitle handling and dictionaries, with AI only as an accessory (Lexa dictionary, Aria chat assistant).

_Read: this is a language tool that survived before the AI wave, by embedding itself in what people already do, not by model capability. The growth signal suggests that model still works today._

## What it actually does

- **Dual subtitles** → target language and native language shown together, 40+ languages, transliteration for non-Latin scripts
- **Click-to-look-up** → click any subtitle word for a dictionary pop-up with pronunciation and examples; Lexa AI explains in context
- **Playback built for study** → jump back one line (S), previous/next line (A/D), auto-pause after each line (Q)
- **Vocabulary workflow** → save words while watching into a personal collection; Pro exports to Anki with screenshots and audio clips
- **Pro machine translation** → machine-translated subtitles for content with no official subs (roughly 5 hours of MT per day)

**What it deliberately does not do**: no courses, no gamification, no standalone mobile app. The restraint is a feature — it owns the one step of "video + subtitles" and leaves the rest to Anki.

## What old behavior it replaces

**The act of setting aside a dedicated study session.**

Before, learning a language meant a course, a textbook, or a fixed daily slot (Duolingo-style coursework); or it meant watching shows with two windows open — one playing, one dictionary — pausing to look up words, noting them by hand, and forgetting them by the next episode. Language Reactor embeds learning into the viewing you would do anyway: words get clicked, saved, and exported in the moment, and review is delegated to Anki's spaced repetition.

_Read: its insight is that retention comes from scenario, not motivation — it does not ask users to do one more thing, it makes the thing they already do count as learning. The floor of this ride-along model is that it does not build courses; the ceiling is that users open it anyway._

## Business model

Freemium. The free tier covers dual subtitles, the dictionary, basic playback, and limited saving. Pro costs $5.95/month, $13.95/quarter, or $39.95/year, unlocking machine translation, speech recognition, unlimited saving, and the enhanced Lexa AI. Payment happens on the website, not via Chrome Web Store in-app purchases.

## Hard numbers

- traffic board figure: **2.59M monthly visits, +54.1% MoM**, on the global growth board
- 2M+ lifetime Chrome installs, 4.17 stars across 4,313 reviews — but the last 100 reviews sit at 2.81 stars
- Recent months brought recurring Netflix subtitle-loading failures and flaky paid features; reputation visibly slid through mid-2026
- Maintained by a solo/small team, slow release cadence, while rivals Trancy and Migaku attack its core dual-subtitle scene
- Headcount and revenue: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The founder is a serious language learner who built the tool for himself — naturally high |
| Product insight | "Embed learning in entertainment" is the right direction; but little product evolution lately, coasting on old features |
| Execution quality | Subtitle parsing and playback controls are solid; frequent Netflix failures show fragile dependence on platform internals |
| Timing | Watch-and-learn demand is durable, but the AI dual-subtitle lane is filling with new entrants; it rides on legacy users |

## The call

**Worth watching, but unproven.** The +54% MoM is a real signal, and this is not a new face — 2M installs is a legacy base; the new traffic means it is being rediscovered in a fresh language-learning wave.

Two caveats. First, **growth and reputation are diverging**: visits up 54% while the last 100 reviews sit at 2.81 stars, driven by Netflix subtitle outages and unstable paid features. It may be gaining new users while losing old ones; churn risk is accumulating. Second, **there is no moat**: dual subtitles are being chased by Trancy and Migaku, while this is a solo-maintained product with a slow cadence — one platform API change and it stumbles.

_Read: the product validates the "embedded in entertainment" need, and demonstrates the ceiling of an independent small tool — the demand is right, but the organization cannot keep up, and competitors will fill the moat with engineering._

## What to watch next

① Next month's MoM on 2.59M visits — a one-off spike or a new plateau
② Whether the Netflix subtitle failures get fixed — a recovery of the 2.81-star recent rating is a direct churn signal
③ Rival growth rates (Trancy, Migaku) — if they climb faster, users are migrating

## What you can take from it

**Product logic**: embedding a tool/learning in an action users already take (watching shows) retains better than asking them to add a new usage slot. When building a tool, ask "what are users already doing," not "what do we want them to do."

**Workflow design**: own only the core link (learning words while watching) and hand review to Anki — do not fight a stronger tool in its ecosystem. A clear boundary keeps the product light and tells users exactly where it fits.

**Positioning language**: none. There are no marketing sentences worth stealing.

## Verdict

**Worth watching, but unproven.** The demand model holds and the growth is real, but recent reliability problems and a thin organization may not retain this wave of traffic. Next month's MoM and the review recovery are the two checks.
