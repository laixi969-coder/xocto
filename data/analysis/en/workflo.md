---
slug: workflo
name: Workflo
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A Mac tool that stages your windows before you need them — arranging the right apps for a
call or a focus block ahead of time, and restoring your layout in under a second when
displays change. It asks for Accessibility permission only, so it structurally cannot see
your screen. "Never sees your screen" is a product boundary, not a slogan.

## Who built it

A solo project by Chirag Chopra, launched 2026-08-09 (97 upvotes, #14
that day). A native Swift menu-bar app, about 4MB, requiring macOS 14+.

_Read: the classic indie builds what annoys him daily — window wrangling is a cost
everyone who shuttles between a laptop and external monitors pays every single day.
Solo, one-time purchase, no subscription: the author wants cost coverage, not growth._

## What it actually does

- **Scenes & Desks** → a Scene is a named window layout (writing, review, monitoring);
  a Desk is a display configuration (single screen, dual screen). When it detects you
  switched Desks, it swaps layouts
- **Calendar/clock triggers** → in the minutes before a calendar event with a video link,
  or at a set focus-block time, it opens what you need and hides what you do not
- **Cancelable countdowns** → every automated move is preceded by a countdown you can
  veto. This is the design decision that keeps proactive window-arranging from being
  infuriating
- **Stash** → Option+Shift+S hides every window on screen; press again and everything
  returns exactly as it was — built for the moment before you share your screen and
  remember the private Slack DM behind your browser
- **Scene Studio** → a drag-and-resize canvas for designing layouts, including dual
  monitor setups; nothing moves on your real screen until you apply
- **Launch placement + per-app rules** → newly opened apps land at their remembered
  position; individual apps can be excluded entirely

**What it deliberately does not do**: no Screen Recording permission (most window tools
need it for previews), no account, no cloud, nothing uploaded — configuration is plain
local JSON you can open, back up, or delete.

## What old behavior it replaces

Setting up windows before a meeting used to be fully manual: open Zoom, Notes, and the
right browser tabs, drag them into position, then lose it all when you unplug the
monitor and start over. Heavy users — remote workers, frequent screen-sharers — burn
minutes a day and pay a context-switch tax each time.

The existing tools split into two camps: **Rectangle** (free, manual shortcut-based
window snapping) and **Moom** (paid, keyboard-shortcut preset layouts). Their shared
model is "you reach, it responds" — you invoke the tool. Workflo replaces that model: it
goes from "invoked" to "already done." A window manager is something you go to; Workflo
is already there before you are.

## Business model

$19.99 one-time purchase, 7-day free trial, no subscription, no account. For comparison:
Moom is also one-time-priced and Rectangle is free, so $19.99 sits in the normal band.

_Read: one-time pricing fits this kind of single-pain-point Mac utility — the math "saves
me three minutes a day, worth $20" closes the sale. But one-time purchases bring no
recurring cash, so the author must keep shipping new features or build a product line to
grow._

## Hard numbers

- PH: 97 upvotes, 7 comments, #14 that day
- MakerStack review: 7.5/10 — "a narrow utility done properly": proactive staging with a
  cancelable countdown, no Screen Recording permission, no account, one-time price
- Native Swift, ~4MB, macOS 14+
- User count and sales: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A solo dev building a tool he uses daily; the pain comes from lived experience, and it shows |
| Product insight | Caught the active-vs-passive difference: everyone else is a window manager, this is a window pre-stager |
| Execution quality | Doing everything on Accessibility alone with sub-second layout restore is restrained, solid engineering |
| Timing | Remote work and multi-monitor setups are the norm; window wrangling is evergreen pain, already educated by Rectangle and Moom |

## The call

**What is worth copying is not the features — it is putting "what we don't do" into the
positioning.**

Half of Workflo's differentiation is the product (proactive staging, cancelable
countdown); the other half is trust. It upgraded "we don't look at your screen" from a
disclaimer to an architectural promise — requesting only Accessibility means there is no
screen-reading code path at the system level. In an era where screen-recording
permissions are everywhere and everyone is "watching," that stance is itself the selling
point. As the pool's inspiration puts it: **privacy is moving from a compliance item to a
marketing one.** It does not merely claim not to collect; it structurally cannot — and
those two statements persuade very differently.

**But the moat is close to zero.** Window management is a mature category, Moom already
covers shortcut-triggered layouts, Rectangle is free, and the proactive staging idea can
be copied within months (Moom could absorb it directly). At $19.99 one-time, there is
also no revenue runway for sustained iteration.

**The transferable rule**: for privacy-sensitive tools, "what we don't look at" sells
better than "what we protect" — because the former is verifiable fact and the latter is
an unprovable promise. But state the cost: that sentence forfeits the features reading
the screen would enable (like auto-detecting what you are working on). That is trading
functional ceiling for a trust floor, and you have to decide whether your category makes
that trade worthwhile.

## What to watch next

① Whether a big player or Moom ships proactive staging within three months — that sets
the length of the differentiation window
② Whether sales or review counts on the App Store/site grow — one-time tools have no
subscription data, so word of mouth is the only signal
③ Whether the author ships a second tool — the growth path for one-time-priced indie
tools is usually serialization

## What you can take from it

**Product logic**: treat "proactive vs reactive" as the first-order product difference —
peers wait for you to call them; can you finish before the user asks? The countdown
(giving the user a veto before any automatic action) is the key to making proactive
automation tolerable, and it is worth copying into any automation product.

**Positioning language**: "never sees your screen" — writing a negative sentence as the
positioning. Not "we protect your privacy," but "we cannot see you." The former is a
claim; the latter is verifiable at the architecture level. For privacy products, reach
for "structurally impossible" statements, not "we promise not to."

**Pricing structure**: single-pain-point tools work at one-time prices, and $19.99 is a
sweet spot — below the mental threshold, above the psychological cost of "free." But
one-time pricing only fits scenarios that are solved once and need no ongoing service.

## Verdict

**Worth watching.** Small and well-made, with a trust design that is the genuine
highlight — "architecturally cannot read your screen" is a more powerful position than
any privacy pledge. But the category is mature, the moat is shallow, and the one-time
price caps the upside. In three months, check whether the big players follow, and
whether the author can roll it into a product line.
