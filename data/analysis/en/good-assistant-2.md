---
slug: good-assistant-2
name: Good Assistant 2
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A personal AI assistant that turns your life goals into a daily plan: it remembers everything about you and pushes you every day, instead of waiting for you to open the app.

## Who built it

Solo developer Jensa Bačík, built over two years of evenings ("two years of evenings later, it's on the App Store in AI form"). The trigger was his own unmet wish for a personal assistant to push his personal goals. Now on iOS and Web, and he uses his own instance daily (he named his assistant Claire).

_Read: a classic "scratch your own itch" product whose feature set follows the author's own usage. Two years of solo work at least proves the need is real and persistent._

## What it actually does

- **Goal decomposition** → you pick a few long-term goals (learning a language, moving countries, financial security); it breaks them into concrete daily actions and builds a visual progress timeline
- **Daily proactive push** → every morning it messages a suggested day plan you can adjust and commit to; it checks in during the day when useful
- **One place for everything** → tasks, notes, goals, reminders, calendar, and chat live in one app, and the assistant reads all of it on its own
- **Layered long-term memory** → the core selling point. Memory is layered and maintained daily; it remembers something you mentioned once a year ago and uses it naturally, without being asked
- **Collaborative notes** → the assistant reads, writes, and edits your notes, using them to understand your context

## What old behavior it replaces

Pushing a long-term life goal used to mean: paper and checklists (nothing holds you to it, abandoned by day three), friends/coaches/advisors (expensive, not always around), or a to-do app like Todoist or Things (stores tasks but doesn't understand your goals and never reminds you why you're doing them).

Mainstream conversational AI (ChatGPT and friends) fails here because it is **stateless**: every conversation starts from a blank slate, you re-explain context every time, and it never comes to you. Good Assistant is betting that "stateful + proactive" is worth $29 a month.

## Business model

Subscription: **$29/month (€26/month in Europe), 1-week free trial**. The author is explicit that the price is high because the backend constantly runs LLM inference — memory maintenance and proactive messages both burn model cost.

_Read: $29/month is aggressive for this category; habit and self-improvement apps usually land at $5–10. The bet is not more features but retention strong enough to justify the subscription. This is a retention-is-everything business, and feature completeness is secondary._

## Hard numbers

- Distribution: iOS App Store + Web
- Pricing: $29/month, 1-week free trial
- Build: one person, roughly two years
- Users, retention, revenue: **not disclosed**

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author is his own target user and uses it daily — the most direct product validation available |
| Product insight | Nailed it: statelessness is the fatal flaw of chat AIs. Memory and proactivity are genuinely the core of a personal assistant |
| Execution quality | Code unverifiable, but the product ships and keeps running, which proves it works |
| Timing | Right in the window where consumer AI shifts from "Q&A" to "long-term companionship" — but the window means everyone else is building the same thing |

## The call

**This is a bet that "memory + proactivity" buys retention.** Every goal-tracking product dies when the user stops opening it on day three. Good Assistant's answer is not a better task view but an assistant that comes to you and remembers what you said last time. The direction is right — but a meaningful share of that $29 goes to inference cost, which locks it into subscription pricing and forces it to depend on very high retention to make back its margin.

**The real risk is the line between "proactive" and "annoying."** Too few pushes and it has no value; too many and users mute notifications. That balance has to be tuned with data, and there is no public retention data.

**Market context**: this lane already holds Replika-style emotional companions, schedule AIs, and the memory features being built into every major model vendor's app. A standalone $29/month subscription has to prove its memory beats "ChatGPT plus a user-written system prompt." No public evidence of that yet.

## What to watch next

① Whether App Store review count and rating grow steadily over three months — for a solo dev product, reviews are the most honest signal
② Whether the author publishes any retention or subscription data — if 30-day retention doesn't hold, $29/month won't either
③ Whether there are "used it for three-plus months" testimonials, not just launch-week enthusiasm

## What you can take from it

**Product logic**: for any product that helps people persist, the core lever is lowering the cost of *remembering to come back* — not more features but appearing in the user's attention proactively (messages, reminders, daily digests). Design "how the user returns daily" on day one, not day one hundred.

**Positioning language**: "It remembers everything you said, and uses it on its own" beats "an AI assistant with powerful memory" — verbs and scenarios, not adjectives.

**Pricing structure**: putting the ongoing cost of memory maintenance into the pricing explanation ("the price is high because the backend runs LLM inference all the time") builds trust better than hiding it. Transparent pricing works especially well for small independent products.

## Verdict

**Worth watching, but the evidence is thin.** The direction — a stateful, proactive personal assistant — is right, the product is real, and the pricing is bold and explicit. But there is no user data and no way to verify retention, and retention is the life-or-death metric. Write the three checks above into your calendar and revisit in three months.
