---
slug: argos
name: Argos
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An AI agent that lives in your browser and acts as you — clicking, typing, and finishing real
tasks with your own logged-in accounts, not just answering you. It takes commands from a
sidebar or from Telegram/WhatsApp, and the Pro tier adds a desktop CLI with shell access.

## Who built it

Argos (formerly Lyto AI) was founded in 2024 in Eindhoven, Netherlands by a three-person team:
Arystan Tanekov (co-founder & CEO, a 17-year-old student at Eindhoven University of
Technology) and Gleb Babichev (co-founder & CTO). Rebranded from Lyto AI to Argos in a 2.0
release in 2026-03, and the desktop CLI shipped 2026-07. The Chrome extension is still listed
under the old "Lyto AI" name: 128 users, 11 ratings, with Google warning that the developer has
not completed verification. The public developer email is a personal Gmail.

_Read: a three-person team, a teenage founder, no Google verification, 128 users, and rebrand
residue everywhere — this is a serious early product from a young team, not a resourced
project. Its heat comes from a single the launch platform day (118 upvotes, #10 daily), not from
user volume._

## What it actually does

- **Operates the browser for real** → clicks, scrolls, fills forms, organizes tabs, and runs
  real tasks using the accounts already logged into the browser
- **Native Google integrations** → drafts emails in Gmail, writes docs, and turns raw data into
  Sheets with charts
- **Multiple command channels** → ask in the sidebar, or send instructions over Telegram /
  WhatsApp (Pro), and get the finished result back after background execution
- **Desktop CLI (Pro)** → shell access plus a real browser profile, extending beyond the
  current tab to local files and desktop apps
- **Safety design** → claims data stays on-device; destructive actions (sending/submitting)
  pause and ask first
- **Anti-"fake success"** → the author answered the browser-agent failure mode in the comments:
  re-locate elements right before acting, verify the real consequence (a field's value changed,
  a network request fired) instead of trusting that an event fired, and wait for the DOM to
  settle

**The promise to discount**: "data stays on your device" has boundaries. The privacy policy
states that conversation history and usage metadata are stored while an account is active;
relevant prompts and page context may be sent to Gemini, Claude, and Perplexity; and explicitly
started Browser Sessions may send a chosen domain's cookies to a server for headless
authentication. Passwords and payment data are stated as never read or stored.

## What old behavior it replaces

Browser agents replace the oldest workflow of all — moving data by hand: copying information
from a page into a spreadsheet, typing an AI's answer from a chat log into a form, manually
compiling competitor prices across five tabs into a brief.

The old options were two paths. RPA tools (UiPath and the like) were powerful but heavy —
setup, servers, and mostly API- or VM-based, useless for "operate with my own logged-in
account." Then automation platforms like Zapier only covered services with APIs; long-tail
web apps were unreachable.

Argos fills the gap both paths left: operating at the browser layer, with the user's own
identity, against any website — no API permission negotiation per service. Its pitch, "acts
as you with your accounts," is precisely the route that bypasses every API authorization
conversation.

## Business model

Free (25 messages/day: page actions, integrations, memory, web search) + Pro ($15/month billed
annually, or $25/month monthly, 3-day trial; 400 requests/week, 70/day; Telegram/WhatsApp,
scheduled and background tasks, monitoring, deep research, desktop CLI) + Team ($120/month, 5+
users).

_Read: a clean consumer subscription funnel with a free tier — standard structure. But on 128
users, revenue hasn't started; this is a complete product with an unproven market._

## Hard numbers

- **PH: 118 upvotes / 9 comments, #10 daily** (launched 2026-08-09)
- **Chrome Web Store: 128 users / 11 ratings** (as Lyto AI 2.2.5, checked mid-Aug 2026)
- Pricing: Free 25 msgs/day; Pro $15/mo (annual); Team $120/mo (5+ users)
- 3-person team, founded 2024, rebranded 2026-03, desktop CLI shipped 2026-07
- Revenue and paying users: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Teenage founder driven by "AI gives answers but no execution" — scenario fits, experience unproven |
| Product insight | Correct call: the browser is the shared front door to every SaaS; automating at the UI layer bypasses API authorization |
| Execution quality | Anti-fake-success engineering (re-locating elements, verifying consequences) shows a product bitten by real use, not a demo |
| Timing | Right but crowded. BrowserUse, computer-use agents, and every browser-agent startup sit on the same spot; differentiation is thin |

## The call

**A browser agent that acts with your identity — right direction, real engineering, but a tiny
base and a steep trust cost.**

It bets that browser-layer automation bypasses API authorization. That call largely holds:
intranet tools, long-tail SaaS, and logged-in flows are exactly where API automation can't
reach and UI-layer operation can.

**One product-logic highlight worth recording**: the author answered the classic browser-agent
failure mode head-on in the comments (an action reports success but never lands), with a
concrete counter-strategy — re-locate before acting, verify consequences, wait for DOM
stability. That detail marks a product bitten by real usage, not a demo.

**But there are two hard problems.** First, the trust cost is high: it asks you to hand
logged-in accounts to a three-person team's unverified extension, and the privacy policy shows
"data stays local" has limits (session history is stored, page context may be sent to
third-party models). Products like this demand extreme trust from early users, and the brand
equity to earn it isn't there. Second, differentiation is thin: open-source BrowserUse and the
majors' computer-use capabilities sit at the same position, and 128 users don't fund a
competition.

**The transferable rule: UI-layer automation (act with your identity in your interface) is the
shortest route around API authorization — but it shifts all the risk onto trust.**
For this category, trust design (permission boundaries, data claims, verification
transparency) is not a differentiator; it is the admission requirement.

## What to watch next

① Whether Chrome Web Store users cross 1,000 in three months — 128 is too low a base; no growth
is a failed validation
② Whether Google completes verification of the app — the unverified state is the biggest trust
blocker, and resolving it is a real signal
③ Whether Telegram/WhatsApp remote control and the desktop CLI see paying usage — the actual
line between Pro and Free, and evidence of whether anyone pays for "remote execution"

## What you can take from it

**Product logic**: for products that need users to hand over account access, solve trust before
features. Three moves to copy: always pause and ask before destructive actions (send/submit);
verify the real consequence after an action instead of trusting the event; and state
permission boundaries explicitly (what leaves, what's never touched) instead of vague
"data stays local" promises.

**Positioning language**: "Most AI just tells you what to do. Argos does it." — one contrast
sentence separates "answer-giving" from "execution," and does the whole positioning in one
line.

**Pricing structure**: Free funnel (25 msgs/day is enough to taste) + Pro feature tiering
(remote control, scheduling, desktop CLI behind the paywall) + Team floor — a copyable
consumer-agent structure. The notable move is pricing usage and capability tiers separately.

## Verdict

**Worth watching, but in early validation.** Right direction, real engineering detail, a real
team — but 128 users, unverified Google status, and a three-person team together say trust
hasn't been earned yet. In three months, watch whether users cross 1,000 and whether
verification lands; neither clears, and the features stop mattering.
