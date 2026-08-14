---
slug: getopen
name: getopen
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A modern alternative to Plausible: cookieless open-source web analytics with two things nobody else ships — revenue attribution and an MCP server, so you can ask Claude what happened yesterday and get the number back.

## Who built it

The OpenLabs team (HN handle rahulbridge). GitHub org OpenLabs-so; the main repo is openanalytics (TypeScript, AGPL-3.0), plus a macOS menu-bar client, oa-menubar. The repo was created 2026-08-11 and reached 117 stars in three days.

_Read: the tool itself is not new; the two additions are what matter for the AI era. Dashboards are table stakes; revenue attribution and an MCP interface are the differentiation it is actually betting on._

## What it actually does

- **Cookieless page analytics**: realtime visits, visitor journeys, funnels, Web Vitals (LCP/INP/CLS/TTFB), custom events, UTM/campaign attribution
- **Revenue attribution**: connects six payment processors — Stripe, Polar, LemonSqueezy, Paddle, Creem, Dodo — and traces revenue back to the campaign, page and post that earned it
- **MCP server**: AI agents can query the data directly (their line: "so you can just ask Claude what happened yesterday"); an AI chat interface is built into the dashboard
- Imports three years of Plausible history; public read-only dashboards, team roles, Slack/Telegram/email alerts
- Free to self-host; ClickHouse backend, so a year of events answers before a spinner appears

**What it deliberately does not do**: no personal data collection, no cross-site cross-day profiles. The page's line: "privacy is the default, not a setting."

## What old behavior it replaces

The GA-era workflow: drop in a heavy GA4 script → get forced into a cookie consent banner → wait two days → wander a maze of a dashboard to find "which page brings the most signups." Plausible already killed half of that (no cookies, light script), but it stops at the pageview layer.

What getopen replaces is the second half: knowing "which page brings the most paid signups" used to mean manually joining order exports, or adopting heavyweight analytics like Amplitude. Revenue attribution compresses that into one dashboard dimension; the MCP step goes further and turns "looking at data" from manual labor into a conversation.

## Business model

Free to self-host (AGPL-3.0); hosted from $9/month (the author's own words on HN: "self-host it for free, or $9 hosted"). Third-party listings show Hobby $9 (100k events/mo), Starter $19 (500k), Growth $29 (1M), plus a free Startup plan (1 year, 100 projects) — the official pricing page was not directly captured; treat actuals as canonical.

_Read: $9 entry with event-based tiers is the standard Plausible/Umami playbook, no price war intended. The real moat bet is "revenue attribution + agent interface" — which neither Plausible nor Umami has._

## Hard numbers

- **HN, two submissions: 4 points (2 comments) and 6 points (6 comments)**
- **GitHub: OpenLabs-so/openanalytics, 117 stars**, repo created 2026-08-11, TypeScript, AGPL-3.0; oa-menubar at 4 stars
- Revenue attribution covers 6 payment processors (Stripe/Polar/LemonSqueezy/Paddle/Creem/Dodo)
- Paid user count and event volume: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author ships AI tools continuously (org name OpenLabs); knows developer distribution |
| Product insight | In a crowded analytics lane, picked exactly the two gaps Plausible leaves: revenue attribution and an agent-facing interface |
| Execution quality | ClickHouse backend plus MCP plus six-channel attribution; 117 stars in three days signals developer approval |
| Timing | Analytics is a red ocean, but "AI agents must be able to read your data" just became a requirement — good positioning |

## The call

**It is betting on the next era's question: data is not just for humans to look at, it is for AI agents to read.**

Analytics has churned through three rounds (GA → Plausible/Umami → PostHog), and the dashboards are all copies of each other. getopen's smart move is not a better dashboard; it is two interfaces no one else ships — revenue attribution wires analytics to money, and MCP wires analytics to agents. For an indie developer, "which page brought N orders yesterday" is the only question worth asking daily, and Plausible cannot answer it.

**The transferable rule: in a red ocean, find the two things the previous generation deliberately does not do — do not try to do it better.** Plausible deliberately skips revenue (privacy-first, simple) and skips agent interfaces (its user is a human). getopen turned both gaps into its selling points. Any "alternative to X" positioning should start by listing X's deliberate blank spots.

**The risks**: revenue attribution across six processors is data-dirty in production (event-order joins, refunds, subscription discounts) — a long war; and the HN comments name Umami's free tier as a direct competitor outside price. The moat is not yet proven.

## What to watch next

① Whether GitHub stars keep rising in three months — is the MCP interface really pulling developers
② Whether anyone publicly says "migrated from Plausible to getopen," and why
③ How accurate attribution is on real order data — can it explain refunds and subscription discounts

## What you can take from it

**Product logic**: a "deliberate blanks" list of the incumbent — enumerate what the existing tool skips because of its own positioning, then pick two blanks as your selling points. Any AI product positioned as "an X alternative" can copy this analysis frame directly.

**Positioning language**: "ask your analytics a question and get the number back, not a report" — opposing "answer" against "report" explains the AI interface value in one line. Also: "from first visit to purchase, understand every step of the customer journey."

**Pricing structure**: free self-host plus hosted event tiers ($9/$19/$29) and a one-year free Startup plan. Standard and clear, worth referencing.

## Verdict

**Worth watching.** In an analytics lane full of identical dashboards, it carved out real differentiation with revenue attribution plus an agent interface, and 117 stars in three days is the market's first signal. Keep it as the case study for "how an alternative finds differentiation"; verify against the three checks in three months.
