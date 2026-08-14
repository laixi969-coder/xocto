---
slug: click
name: Click
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

An MCP connector layer you install into ChatGPT, Claude, or Codex: it feeds agents the live
context that built-in web search misses — LinkedIn lead data, competitor ad campaigns, social
sentiment, live flight fares — without you leaving the chat window for the browser.

## Who built it

Aditya (ProductHunt handle `adiasg`; his YC Launch page says he "previously helped build
Ethereum"). No public site or pricing page; launched through ProductHunt and YC Launches.

_Note: the pool entry credits Garry Tan as builder, but the product page and launch materials
identify the author as Aditya and no source ties it to Garry Tan; the record is corrected here
to match the product page._

_Read: an Ethereum alumnus building the data layer for the AI chat surface is consistent — he
believes the chat interface is the next application platform and is building the missing
infrastructure for it. That background means patience for protocol/connector work, but early
commercial validation is not his comfort zone._

## What it actually does

- **Gives agents data that lives behind logins** → LinkedIn lead research and enrichment,
  competitor ad-campaign analysis, cross-platform social sentiment, trip planning with live fares
- **One-time install** → a single MCP server into ChatGPT or Claude, roughly one minute, then
  usable directly in chat
- **Domain-by-domain roadmap** → per the author, "one trusted service at a time, research
  first," with connectors to be added category by category

**What it deliberately does not do**: no browser automation, and no touching your logged-in
browser session — the author explicitly dislikes agents operating a logged-in browser — it goes
through provider APIs instead.

## What old behavior it replaces

External research with an agent used to hit two dead ends: built-in web search is too shallow
to reach LinkedIn, professional platforms, or marketplaces — the agent either fluffs or
hallucinates; or the agent asks to drive a logged-in browser, which means either handing over
your session (a security smell) or doing the search yourself and pasting results back. The
heaviest step stayed with the human.

Click replaces the act of **leaving the chat for one piece of context**: finding a lead on
LinkedIn, comparing prices, checking a competitor's spend — previously a person stepped out of
the chat to work; now the agent reaches the data source directly from inside the conversation.

## Business model

**Not disclosed.** No pricing page, no public plans — just ProductHunt and YC launch pages.

_Read: MCP connectors are hard to charge for on their own — install is free, data sources bill
per call, so the real model is probably "connectors free, premium data subscription." The
"one trusted service at a time" route only works once a connector becomes indispensable, and
none has been proven yet._

## Hard numbers

- Users, installs, ARR, funding: not disclosed
- Channels: ProductHunt (launched this week) and YC Launches
- Team: solo (per the author)
- Price: none

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Heavy Codex/Claude user; the pain (built-in search can't reach behind login walls) is specific and credible |
| Product insight | Spotted the gap between built-in web search and the real web, and chose the right delivery form — MCP, not a new client |
| Execution quality | Light one-minute install; but the connector set is small and no verifiable implementation detail is public |
| Timing | MCP just became the standard, so this is the connector window; but the lane is crowded (Perplexity, Exa, others sell context too) |

## The call

**Right direction, early small player in the "selling context" lane — too soon to call.**

The insight is real: general models lack present-tense context, not capability, and built-in
search is both shallow and walled off. "Connectors for the agent" is a much lighter, more
startable business than building the model.

**Two questions remain unanswered.** Moat: a connector has no inherent barrier — any data
provider can ship its own MCP. And the pay point: research is a low-frequency need, and users
may not pay separately for "look things up in chat." The "trusted service" route only holds once
one connector becomes indispensable — no evidence of that yet.

## What to watch next

① Whether the connector count and categories grow in three months (research-only today) — a
  single use case won't carry a subscription
② Whether pricing and paid-user numbers ever go public — a product without a revenue model
  doesn't matter at this stage
③ Whether any third party reviews or a public customer adopts the LinkedIn connector specifically

## What you can take from it

**Product logic**: when adding "present-tense context" to an AI product, find the seam where
built-in search cannot reach and login state is required (LinkedIn, transactional data,
ticketing) — that is more clever than another general search enhancement, because the majors
will own generic search and the seam is where you can win.

**Positioning language**: "The context that built-in web search misses." Defining your existence
by what they *can't* reach beats claiming "we have more data."

**Pricing structure**: none. Not disclosed.

## Verdict

**Unproven.** Real insight, light direction, credible founder — but zero data, zero pricing, a
single feature, and an unvalidated business model. File it as a sample of the MCP-connector
lane and revisit when pricing and paid usage exist.
