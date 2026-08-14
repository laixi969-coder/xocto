---
slug: switchy-for-mac
name: Switchy for Mac
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A menu bar click moves the same Magic Keyboard, Trackpad, and Mouse from one Mac to
another — no more manual unpairing and re-pairing, and no cable tricks.

## Who built it

Independent developer Benhur Senabathi, who built it after buying himself the three
Apple accessories, switching between work and personal Macs, and getting fed up with
manual pairing (the origin story notes colleagues who bought a brand-new trackpad for
each computer just to avoid the hassle). Self-launched 2026-08-11: 85
upvotes, daily rank #18. Site: mangobons.com/switchy. Already packaged as a Homebrew
cask.

_Read: a product bitten by its own very specific annoyance — the annoyance repeats
three times a day and costs a few minutes each time, so solving it is worth $12.99._

## What it actually does

- Bonjour auto-discovery of other Macs running Switchy on the local network
- One menu command moves the whole set of accessories — it changes which Mac *owns*
  the Bluetooth accessories, not merely forwards input
- Supports Magic Keyboard (including the Touch ID model), Magic Trackpad, and Magic
  Mouse
- Purely local: no account, no analytics, no tracking; external traffic is limited to
  update checks and Lemon Squeezy license validation
- Simple pricing: $12.99 one-time, lifetime license for up to 5 Macs, including 1.x
  minor updates

**What it deliberately does not do**: none of the KVM stuff (no screen switching, no
file transfer, no cross-platform control).

## What old behavior it replaces

Moving one set of Apple accessories between two Macs used to mean three options, each
with its own pain:

1. **Manual Bluetooth re-pairing** (free, slow): forget the device in Bluetooth
   settings, wait for it to appear on the other Mac, re-pair. Thirty seconds to a
   minute per device, three rounds for the keyboard, trackpad, and mouse.
2. **The cable trick** (free, faster): plug the accessory into the new Mac via
   Lightning/USB-C and macOS pairs it in about two seconds — but one cable moves one
   device at a time and you need the cable handy.
3. **Apple Universal Control** (free, but often unusable): it *shares* input rather
   than *switching* Bluetooth ownership, and requires both Macs awake, signed into the
   same Apple Account, and on the same network. Different Apple IDs on work and
   personal machines kills it outright, and it is useless if you want to carry the
   keyboard to another room.

Switchy replaces the repeat daily chore (a few minutes, three devices, multiple
rounds) and the money spent buying a second set of accessories per computer.

## Business model

One-time $12.99 (lifetime license, up to 5 Macs, 3-day full-featured trial), no
subscription. Sold through Lemon Squeezy. Revenue and sales: not disclosed.

_Read: for a Mac tool that hurts once a day, a $12.99 one-time price is right — a lower
psychological barrier than a subscription, higher than the user's own time cost._

## Hard numbers

- launch 2026-08-11: 85 upvotes, 4 comments, daily rank #18
- Homebrew cask listed, current version 1.1.4 (another source shows 1.1.5 build 79);
  Homebrew analytics show 7 installs in 30 days
- Competitor Magic Switch is $14.99 and does not support the Trackpad, one device at a
  time
- User count, sales, revenue: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Built from the founder's own daily pain, with a real customer portrait (the colleague buying a second trackpad) observed firsthand |
| Product insight | Cleanly separates "switch Bluetooth ownership" from Universal Control's "share input" — precise positioning |
| Execution quality | Fully local, no telemetry, Homebrew-packaged, macOS 14+. Complete engineering |
| Timing | It survives exactly as long as Apple does not ship a system-level accessory switcher; the business is a bet on platform inertia |

## The call

**A textbook "annoyance this specific" tool.** Single pain point, one-time pricing, no
subscription, no telemetry, no cloud. The boundaries are clear enough that a user
knows whether to buy after reading three sentences. Products like this live for years
on word of mouth — which is also the only distribution it has, since there is no
growth team and no content engine.

**The ceiling is written on its face**: the entire value rests on Apple not shipping a
"switch accessories" button in macOS. The day System Settings grows one, this goes to
zero. Its real survival space is people who cannot use Universal Control (different
Apple IDs, or wanting to carry the keyboard to another room) — real, but small.

**What to copy if you build AI products**: restraint. A new tool does not need to be a
platform. A $12.99 one-time tool can sustain an indie developer for a long time — if
the pain hits "once a day" frequency and the user can judge the value themselves.

## What to watch next

① Whether Homebrew installs cross 100 in three months (currently 7 per 30 days — too
small to indicate any word-of-mouth compounding beyond the PH spike)
② Whether independent reviews or third-party user testimonials appear — today it is
just the official blog and directory records
③ Platform moves: if Apple ships a built-in equivalent in a macOS update, the product
goes to zero

## What you can take from it

**Positioning language**: position your paid product next to the free option that
"does not fit" — the official blog walks through Universal Control's requirements (same
Apple ID, both awake, same network) and lets the reader classify their own scenario.
Comparative positioning beats a feature list.

**Pricing structure**: one-time purchase plus a device limit (5 Macs) plus free minor
updates — a subscription-free model for an indie tool. Subscriptions are a rejection
trigger for something used occasionally.

**Product logic**: a new tool only does a small slice of one old task, with the
boundary ("I do not do KVM") stated explicitly — that keeps the user's trust cost low.

## Verdict

**Worth watching, with a defined ceiling.** Clear positioning, fair pricing, clean
engineering; the only external risk is how long Apple's platform inertia lasts. A
one-time-purchase tool has no growth data, so it lives on word of mouth — check back in
three months against Homebrew installs and third-party reviews.
