---
slug: ai-pulse
name: ai-pulse
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A virtual LED strip floating in the unused space beside the macOS Dock: is your AI
agent working, waiting on you, finished, or broken — one glance. Pure software,
does not touch the Dock, reads nothing.

## Who built it

leog (GitHub: leog), an independent developer. Inspired by the SidePulse hardware
gadget, reimplemented as software. The commit history shows pair-programming with
Claude (Anthropic) — many co-authors are AI — with 27 commits so far.

_Read: a classic "open-sourced personal tool" — the author's pain (not knowing
where a background agent is in its work) was concrete enough to justify a full
app, but the positioning stays personal-utility; there is no commercial intent._

## What it actually does

- **Five states, one strip** → working (cyan comet streaks), needs you (orange
  breathing), failed (red double-blink), finished (all eight LEDs settle green),
  idle (slow aurora), plus an off state
- **No per-model distinction** → deliberately a single aggregate signal: you see
  "is something happening," not which agent
- **Not embedded in the Dock** → macOS exposes no public API for Dock accessories,
  so it is a Dock-adjacent, borderless, nonactivating NSPanel positioned from
  public screen geometry (NSScreen.frame vs visibleFrame)
- **Zero permissions** → no private APIs, no Accessibility or Screen Recording
  permissions, no injection
- **Local loopback service** → listens on 127.0.0.1:7455; a bearer token is
  generated at launch and stored in the Keychain, the aipulse CLI reports status
  without tokens ever appearing in shell history
- **Integrations** → an official Claude Code hook adapter, plus a pi extension
  (aipulse-pi.ts); other agents are meant to be added later

**What it deliberately does not do**: read prompts, terminal content, editor
content, or windows; no interception, no recording.

## What old behavior it replaces

With a desktop agent (especially a CLI agent like Claude Code), knowing "where is
it now" used to mean one of two things:

**Keeping the terminal open** — staring at a scrolling log; look away for a moment
and you lose track of which step it is on, and whether you should wait.

**Flipping over to poke it** — constantly switching windows to check output, or
just waiting blind; when the agent is waiting on your approval you may not know,
burning minutes.

Further back, people bought hardware like the SidePulse LED strip for the same
problem — extra money, a physical spot, and locked to a specific ecosystem.

AI Pulse replaces "repeatedly checking agent status": it lifts "busy / waiting on
you / broken" out of the logs and turns it into ambient light you catch with
peripheral vision. It solves an anxiety problem rather than a functional one, and
the README says exactly that.

## Business model

**None.** MIT open source, free, no paid plan, no ads.

_Read: there is no commercial imagination here, and the value lives elsewhere —
it validates that the psychological cost of an invisible agent is real and can be
addressed by a 30-line UI. That need will most likely be absorbed by agent
products themselves._

## Hard numbers

- HN: 18 points / 12 comments (this batch's observation)
- 27 commits, MIT, Swift/SwiftUI, Universal binary (arm64 + x86_64)
- All six milestones delivered; the README calls the MVP complete
- Releases not yet notarized; install requires right-click → Open (plus a
  Privacy & Security allowance on macOS 15+)
- Users and downloads: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author is a daily CLI-agent user; the pain is real |
| Product insight | Targets anxiety, not function; the aggregate signal (no per-model split) is a deliberately restrained, good design |
| Execution quality | NSPanel placement, Keychain token, zero permissions, local loopback API; clean engineering, not a toy |
| Timing | Reasonable but a short window. Desktop agents do not ship a status light yet, but absorption is only a matter of time |

## The call

**A clean sample of "solve a psychological problem, not a functional one."**
Most agent tools add features; this one subtracts noise — compressing "what is the
agent doing" into a peripheral signal. The aggregate signal is the smartest
choice: the user does not want detail, they want the single answer "do you need me
right now."

**The engineering is serious.** Not docked (impossible anyway), zero permissions,
token through the Keychain, local loopback — a "fake LED strip" built to
production standard is itself a statement about quality.

**But its fate is probably absorption.** Status visibility is part of agent
product experience, and Claude and friends will eventually make status better
themselves. That makes it a good transitional tool, not a business.

**The transferable rule: adding an ambient visible signal to an invisible process
is the cheapest and most effective experience upgrade there is.** User anxiety
about background processes is real, and the UI to fix it is often just a status
light.

## What to watch next

① Whether stars clear 300 in three months — diffusion speed of a utility shows
real use
② Whether official adapters appear for agents beyond Claude Code (Codex, Cursor,
etc.) — that decides whether it survives the transition
③ Whether desktop agents ship their own status light (the absorption signal)

## What you can take from it

**Product logic**: when building tools, ask "what is the user anxious about right
now" before "what feature should I add." An ambient status light for a
background-running agent is subtractive design — sometimes a product upgrade means
letting the user know less, not more.

**Positioning language**: none. The README is engineering documentation; nothing
to steal.

**Pricing structure**: none. Not disclosed; fully free.

## Verdict

**Unproven.** Good insight, clean engineering, a genuinely usable tool — but no
business model, and likely to be absorbed by a bigger product. Its value is
demonstrating the "status visibility" experience point. Check its diffusion speed
in three months; no need to study it as a business.
