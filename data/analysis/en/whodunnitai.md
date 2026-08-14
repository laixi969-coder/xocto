---
slug: whodunnitai
name: whodunnitai
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A murder-mystery game you play with your voice: five AI suspects with full backstories,
you interrogate them freely into a microphone, present evidence, and accuse — and the AI
answers in real speech. Talking is the gameplay.

## Who built it

A solo project by indie developer MrRowTheBoat, launched as a Show HN around 2026-08-10
(whodunnitai.com). The game currently ships a single case, "Death at Blackwood Manor": a
poisoned patriarch, five guests, one locked-in truth.

_Read: a classic "technologist built a game he would play himself." On HN the discussion
centered less on "is it fun" and more on "how was this assembled with the latest real-time
voice models." The creator replies directly in the thread about API costs and
hallucinations — high-responsiveness, engineering-first author._

## What it actually does

- **Speech-to-speech interrogation** → OpenAI's gpt-realtime-2 line over WebRTC; you talk
  to suspects like a phone call, not speech-to-text followed by a text reply
- **Free-form questions, no dialogue trees** → ask anything, every playthrough's
  conversation path differs, built-in replayability
- **A separate judge model** → a gpt-5-mini that takes no part in conversation
  independently rules on whether your presented evidence is valid — generation and
  adjudication decoupled, so one model is never both suspect and referee
- **Suspects lie and get flustered** → characters respond per preset principles (may lie,
  must not admit), and the real-time voice carries the tension — interrogation pressure
  is the most-praised part
- **Accusation mechanic** → the suspect agent records your stated evidence through a tool
  call and hands a structured list to the judge model for a ruling

**What it deliberately does not do**: no preset dialogue trees, no text-first pipeline.
Every link — capture, transcribe, respond, adjudicate — exists to sell the feeling of a
real interrogation.

## What old behavior it replaces

Playing detective games in the Ace Attorney mold meant picking options from a fixed
dialogue tree: you could only ask what the writer pre-wrote, and replays converged.

whodunnitai replaces the real thing — pressing a liar who gets nervous and invents
stories — which previously only live murder-mystery parties delivered: gather friends,
spend half a day, need a host. It compresses that into 15-30 minutes in a browser. Peers
like Vaudeville (Steam) support voice, but as voice-typed text commands; this is true
speech-to-speech.

## Business model

Free + donations + BYOK. The free tier caps at 30 minutes (briefly cut to 15 after the
launch-night cost spike). Players can bring their own OpenAI API key for unlimited time;
the key lives in browser localStorage, and the server issues a temporary credential per
session without persisting the key. The creator openly asks for donations to cover
per-minute API costs.

_Read: this is not a business model, it is an emergency brake on cost. Real-time voice
APIs bill by the minute; with a typical 21-minute solve time, every player is a hard
cost. BYOK is clever cost-shifting — but it turns "buy the game" into "bring your own
fuel," and most non-technical players do not have an API key. That door shuts out the
bulk of the potential audience._

## Hard numbers

- HN 203-208 points, 86 comments — among the most-discussed voice products in this batch
- Site snapshot: 205 investigations underway, 8 solved, typical solve time 21 minutes
- Launch night exhausted the API balance and players hit connection failures; after the
  fix, roughly $100 burned in a few hours
- The script is produced by a 40-plus-stage generation pipeline — roughly book-length
- Stack: Next.js + MongoDB + Clerk, with gpt-realtime for live voice

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The creator knows the real-time voice APIs from the inside; craft is the core asset, but one person caps content output |
| Product insight | Nailed that voice fits games better than tools — talking is already part of interrogation play |
| Execution quality | The decoupled generate-and-judge architecture is the real highlight, a clear step above a single-model bodge |
| Timing | Real-time voice models just matured and costs just entered a playable range — a genuinely good window |

## The call

**The product's value is not "a good game" — it is proof that voice interaction works in
games.**

It validates two things. First, **entertainment tolerates model flaws far better than
tools do.** In a tool, one mistranscribed word is an incident; in a game, a model
inventing a false family relationship reads as "the suspect is lying" and becomes
immersion. That is the most underrated design dividend in voice AI: games convert the
model's defects into gameplay. Second, **the generate-and-judge split** — gpt-5-mini as
referee, the suspect model as contestant — is an architecture that ports wholesale to any
"AI both generates and rules on output" scenario.

**The ceiling is equally legible**: cost is a hard constraint. Under per-minute
speech-to-speech billing, every free player is a liability and every solver burns money.
Today it reads more like a technical demonstration — HN's core audience for it is fellow
developers, not players, which says the first wave of attention is about the architecture,
not the fun.

**The transferable rule**: for real-time voice products, design the cost structure before
you design the experience. The 30-minute cap, BYOK, and per-session credentials are the
honest answer to an unmanaged cost curve. Do not complain about its UX friction — first
ask what your product burns per minute.

## What to watch next

① Whether a second case ships — one case caps replayability, and content output is the
life-or-death constraint for a solo author
② Whether the solved-to-investigated ratio climbs — 8/205 is near-zero conversion and
means most people never reach the ending
③ The share of BYOK players — if the free-to-paid path is almost entirely bring-your-own-
key, pure subscription cannot cover the costs

## What you can take from it

**Product logic**: split "generation" and "adjudication" into two models with distinct
jobs. When your product needs an AI to improvise freely yet still produce a correct
result, let one model generate and another rule — far more reliable than one model being
both player and referee. The gpt-5-mini judge is a direct demonstration.

**Positioning language**: none. Its taglines are feature statements; nothing to steal.

**Pricing structure**: BYOK is worth copying for API-usage-billed products — let heavy
users bring their own fuel while the platform charges for the service layer. The
precondition is a technically capable audience; it does not fit consumer scenarios.

## Verdict

**Worth watching — as a technology bellwether, not as a game to buy.**
How naturally voice works in play, and the two-model adjudication architecture, are both
directly transferable to any voice or generative product. But until the cost model is
solved, this one is not a business. In three months, check for a second case and a rising
solve rate.
