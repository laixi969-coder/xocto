---
slug: track-habits
name: Track habits
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A habit tracker that refuses to stop at checkmarks — check, number, time-of-day, and
pick-from-a-list sit side by side, so you see "the numbers and the time" rather than
just "done or not."

## Who built it

Individually built by bohdanstefaniuk (Habit Pocket, habitpocket.io). The author's own
pain, as stated: most trackers only know done/not-done, but he wants to log actual
effort — walking 9k steps today when the goal is 10k is still progress; three days of
camping without running should not destroy a streak, hence a "skip" feature. iOS and
web, offline-first, not open-sourced yet, with a plan to open-source and support
self-hosting.

_Read: the classic personal tool built for the maker's own pain. Four record types and
a forgiving streak are the selling points — small and honest, but no team and no growth
engine._

## What it actually does

- **Four record types** → a yes/no check, a target number with a unit (steps, weight,
  water), a time of day (what time you woke up), and a custom pick-list (mood, energy,
  workout type)
- **Grid view** → every habit on one table, the whole week at a glance
- **Forgiving streaks** → a blank day breaks the streak; a skip day pauses it instead
  of breaking it
- **Overlay charts** → sleep over mood, steps over energy, on one chart, to find what
  moves together
- **Apple Health auto-fill** → steps and weight arrive on their own on iOS
- **Ask AI about your data** → MCP connection to Claude or ChatGPT; ask in plain words
  what changed this week
- **Offline-first** → an operations-log model that reconciles on reconnect

## What old behavior it replaces

Two old behaviors. First, checkmark habit apps (Streaks and the like): binary state
only, so a near-miss like "9k steps" gets recorded as failure, real effort is erased,
and motivation erodes. Second, keeping metrics in Excel — the author's own words: "I
wanted something friendlier than an Excel spreadsheet": records anything but has zero
experience.

It replaces "either a fake win or a full failure" binary logging, and the
"records-everything-but-painful" generic spreadsheet. The core difference is the data
model: "time of day" and "numbers" are first-class citizens instead of everything being
squashed into a boolean.

## Business model

Freemium. Free: 5 habits, yes/no and numeric types, one auto chart per habit, 60 days
of stats, multi-device sync. Pro at $3.99/month: unlimited habits, time-of-day and
select types, AI access (MCP), Apple Health, candle chart and custom chart builder.
Lifetime at $49. No Android yet (planned). Data exports as CSV/JSON at any time;
deleting the account wipes everything immediately.

_Read: restrained and honest pricing; $49 lifetime is the common indie-developer
choice. But no reminder notifications and no Android means the growth engine is weak._

## Hard numbers

- **HN Show HN: 6 points / 7 comments** (2026-08-13). Very little traction
- iOS and web; no Android yet
- Not open-sourced; the author says open source + self-hosting is planned
- Users, downloads, paid conversion: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author uses it himself; the pain is real, and the motives behind number-logging and skip design all line up |
| Product insight | "Record real effort, not a binary state" has insight, but the category is crowded |
| Execution quality | Offline operations-log and MCP integration — not rough engineering |
| Timing | Habit tracking is a red ocean; four record types alone will not differentiate a market |

## The call

**The most copyable thing is the "skip, not fail" mechanism.** Real-world effort is not
binary. Three days camping without running is not abandoning running. Giving "pause" an
expression that does not break a streak sustains long-term use better than punitive
checking-in — a general design lesson for any retention-oriented product.

**"Record numbers and time" rebels against binary check-ins, but it cuts both ways.**
Numeric logging is truer and more analyzable, but it costs more to enter. A check is a
second; a number is three. Three seconds of friction will shed most users after ninety
days. It bets on the small-but-real niche of people willing to log real data.

**The MCP interface is the smartest differentiation.** Letting a user's AI read habit
data directly over MCP upgrades the tracker from "logging tool" to "personal data
base." The headroom of that interface is much larger than the four record types — once
the data layer opens, whether the tool is a habit tracker barely matters.

**But 6 points plus a red-ocean category caps its ceiling.** No reminders, no Android,
no social layer, and the head of the habit-tracking market is already taken by
checkmark apps. A differentiated data model only carves out a small market.

## What to watch next

① Whether it actually open-sources as planned — open source + self-hosting is the only
clear growth story it has
② Whether Android ships — no Android locks out half the market
③ Whether any paying user shows up publicly — for an indie product, the standard is
survival, not growth

## What you can take from it

**Product logic**: the counterintuitive design for tracking products — "skip" is a
deliberately kept escape hatch. Real effort is not binary; giving users a "pause,
not fail" option sustains long-term use better than punitive streaks. Numeric and
time-of-day record types also carry more analytical value than a plain check.

**Positioning language**: none. The copy is a feature list.

**Pricing structure**: Free / $3.99 monthly / $49 lifetime, AI behind the paid tier,
data export always free — a replicable structure for consumer tools.

## Verdict

**Unproven.** An honest little product with a useful mechanism, but a red ocean, no
Android, no reminders, and 6 points of traction. Treat it as a reference, not a target.
