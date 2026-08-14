---
slug: alphabet-soup
name: Alphabet Soup
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A web-based multiplayer word game: seven random letters, and you compete with
people online to spell the longest word. Unlike NYT Spelling Bee, it does not
count how many words you find — only your single best (longest) one scores.

## Who built it

johnchinjew (John Chin-Jew), an independent developer, personal project. His Show
HN post describes it plainly: a simple multiplayer word game where friends play
private matches, or you join a public Arena against whoever is online, matched
with a bot when nobody is around.

_Read: a textbook personal side project — the author is his own first user, and
the motivation is "play word games with friends," not "I found a market." These
projects usually do not live long, but the spread mechanism (call a friend) is
worth studying separately._

## What it actually does

- **Longest word wins** → seven random letters, spell the longest valid word;
  scoring is by length, and only your best submission counts
- **Private matches plus Arena** → play with friends in a private match, or join
  a public Arena against online players; a bot fills in when nobody is around
- **Not turn-based** → works with 2 or more players, suited to bigger groups
- **Panagrams not required** → explicitly allows words that do not use every
  letter (the author's official reply: panagrams are too hard to demand)

**What it deliberately is not**: no AI, no ad-monetization, no complex systems.

## What old behavior it replaces

"Wanting to play a word game" and "wanting to play something with friends" used
to map to two old habits:

**Playing NYT Spelling Bee alone** — single-player, one puzzle a day, score by
how many words you find. A quiet solo ritual with no social layer, no opponent,
and nobody to compare against afterward.

**Wanting to play with people but failing to assemble them** — play with friends
meant meeting offline (scheduling people and time) or opening a game that is
turn-based (waiting, taking turns), and the interest died before the group
assembled.

Alphabet Soup replaces "getting a round going with friends" as an action: open
the page and you are in; not turn-based means jump in anytime; the longest-word
rule gives every round a clear winner; bots cover empty arenas. It turns a solo
word puzzle into an "invite a friend" entry point — which is exactly the core
action behind how light multiplayer games spread.

## Business model

**None — Buy Me a Coffee tips.** No subscription, no ads, no in-app purchases.

_Read: the normal shape of a hobby project; the author clearly is not trying to
make a business of it. Its value is not revenue but validating the "multiplayer +
short round + clear winner" spread formula._

## Hard numbers

- HN: 35 points / 35 comments (this batch's observation)
- The comment section shows real play evidence: someone was pleased to beat a
  player named "hitler1488" (and asked for name filtering), someone reported a
  bug ("word already used" false positive, promised fixed the same day), people
  requested a "gg" button and chat, and one proposed a Countdown variant
- It suffered a Railway outage at launch, with the author live-reporting the fix
  on HN ("seeing full recovery now, Aug 9 10 PM PST")
- Users, DAU, retention: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author plays it himself and answers every bug and feature request |
| Product insight | "Longest word vs most words" turns a word game from a marathon into a sprint, a natural fit for short multiplayer rounds |
| Execution quality | A Railway outage and one false-positive bug, both fixed the same day; MVP-level and acceptable |
| Timing | No special window, a pure casual-game lane; first users came from the HN launch |

## The call

**It validates the "multiplayer + short round + clear winner" spread formula, and
little else.** The HN comment section is the best evidence: most of the 35
comments are real post-play feedback — someone was happy to have beaten a player,
someone reported a bug, someone asked for features. That means the game actually
gets played and produces emotion, which most small-game launches never achieve.

**The "longest word" rule change is smart.** Word games traditionally score by
volume (Spelling Bee); changing it to longest makes a round short, the outcome
unambiguous, and the game spectator-friendly — anyone can see who won at a glance.
That is exactly the trait an "invite a friend" product needs.

**But do not overrate it.** Solo development, no business model, and casual games
are naturally short-lived; this will most likely fade as a side project. It
deserves attention not because Alphabet Soup will succeed, but because it is a
clean sample of what light multiplayer games actually spread on — the act of
inviting a friend, not how good the game is.

## What to watch next

① Is the site still alive in a month, and can it still match real players — the
cruelest retention metric for a casual game
② Do the requested features (Countdown variant, chat / gg button) ship — whether
the author is still iterating
③ Whether a "same rules, different shell" clone appears — being copied is a
signal the formula works

## What you can take from it

**Product logic**: for a light multiplayer game, the rules must make rounds short,
outcomes unambiguous and spectating friendly — Alphabet Soup replaces "most words"
with "longest word," turning the game from solo practice into watchable duels.
The core design goal for multiplayer products is not depth; it is "always able to
pull someone in."

**Positioning language**: none. It spreads on the gameplay itself; there is no
copy to steal.

**Pricing structure**: none. Not disclosed; fully free.

## Verdict

**Worth watching.** Not because it will succeed, but because it is a clean sample
of "multiplayer games spread by inviting a friend" — 35 HN comments full of real
play traces is itself a scarce signal. Its success or failure does not matter;
what matters is remembering the formula: light multiplayer games spread on the
act of inviting a friend, not on how good the game is.
