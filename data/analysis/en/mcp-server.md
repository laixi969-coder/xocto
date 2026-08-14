---
slug: mcp-server
name: mcp-server
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An MCP server that hands AI agents a disposable phone number: when an agent needs to
sign up somewhere, it orders a private number in the right country, waits for the SMS
code, reads it, and returns the number — no human at the keyboard.

## Who built it

SV Number (sms-verification-number.com), a company already running a phone-verification
business, repackaged its existing SMS API as an MCP server (`sv-number/mcp-server`,
MIT, TypeScript) and aimed it squarely at AI agents. The site has a landing page built
for agents plus an agent-skill (plain markdown) for Claude Code and Codex.

_Read: this is not a new product launch, it is a channel redo. Same SMS-verification
service, but the user changed from a person to an agent. Nothing new was invented —
the interface language was switched from a human-facing web page to MCP tools an agent
can read. Enterprise DNA covered the pivot explicitly, treating it as the reference case
for "rewrap a vertical API for agents."_

## What it actually does

- **Order by country** → 211 countries, 1,094 service codes (Telegram, WhatsApp,
  Google, and more). The request carries `country=<id>`, and the agent picks based on
  live availability (`getCountryAndOperators`, `getServicesAndCostWithStatistics`)
  instead of a list pinned in its prompt
- **Read the code, not the inbox** → polling `getStatus` returns `STATUS_OK:123456`
  directly — the code arrives already parsed, no regex over SMS text
- **Number held exclusively for 20 minutes** → while held, no one else can receive it;
  if no code arrives, the money refunds automatically
- **Second factor included** → when the service issues an authenticator secret, the
  agent computes the 6-digit code locally per RFC 6238 (30-second windows); the secret
  never leaves the machine
- **Nine native MCP tools** → `list_countries`, `list_services`, `order_number`,
  `wait_for_code`, `finish_activation`, `cancel_activation`, `totp_code`, etc.,
  usable from Claude Code, Codex, and Cursor; without MCP, the underlying methods
  (`getNumber`, `getStatus`, `setStatus`) are the market-standard names, so an existing
  client mostly changes its base URL

**What it deliberately does not do**: no SMS sending, no calls. The numbers receive
verification codes and nothing else.

## What old behavior it replaces

When an agent needed to complete a signup (say, an Indonesian-market account), the
bottleneck was phone verification: verification services look at the number's country,
and a US number registering an Indonesian account gets refused before the SMS is sent.

The old flow was a human at an SMS-activation platform (sms-activate and peers):
choose a country, place an order, wait for the code, paste it back into the signup —
minutes of human babysitting per account. Earlier still: buying a physical SIM and
plugging it in.

SV Number automates all three steps: one API call orders, polls, and completes the
signup, with the country decided by request parameter. It replaces the act of a person
standing by waiting for a code. **More valuable**: it makes "a fresh number per
account" the default — services remember which numbers already verified an account,
so a permanent number fails on the second signup, while this market was always priced
as one-code-per-activation anyway.

## Business model

**Pay per code, prepaid balance.** Typical price $0.43 per verification (from $0.01);
if no code arrives within 20 minutes, the balance refunds automatically. Day-rental for
accounts that must keep receiving codes. 150 requests per second. No subscription, no
seat fee.

_Read: this pricing is designed for agent customers — agents do not negotiate, do not
flinch at a few cents per call, and keep running as long as the API is stable. For the
seller this is the ideal customer: usage grows by itself, near-zero service cost. The
risk is on the compliance side: phone-verification inherently sits next to batch
signups and fraud, which is the sword hanging over every provider in this category._

## Hard numbers

- **573 stars / 3 forks** (2026-08-14), MIT, TypeScript, listed in the official MCP
  Registry
- Enterprise DNA reports: 534 stars gained on GitHub in three days; a companion
  "skills" repo shipped the same week
- 211 countries / 1,094 service codes / typical $0.43 / 20-minute exclusive hold /
  150 rps (read from the site on 2026-08-06)
- Comparison pages (vs AgentLine / AgentPhone / AgentNumber / OP): competitors cover
  only the US/Canada; SV Number covers 211 countries
- Team size, revenue, funding: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | An existing verification business turning itself around; the pain (agents need an identity) was fed to them by the market, not invented |
| Product insight | Nailed "the smallest unit of identity is a phone number"; delivering the parsed code as an MCP tool is closer to real demand than the crowd building "call/text for agents" |
| Execution quality | The MCP wrapper itself is low-tech, but the agent-skill, refund policy, comparison pages, and live-availability API make this a finished product, not a demo |
| Timing | Good. Agents signing up for accounts at scale is a growing need, and 2026 is MCP's channel-window |

## The call

**This is the textbook case of "rewrap a vertical API for agents," worth studying by
anyone running an API business.** SV Number invented no new service. It did three small
things: changed the interface language to what agents read, changed the docs to what an
agent can read by itself, and changed the pricing to something an agent never flinches
at. Together, three small things turned a human-facing niche business into
agent-facing infrastructure.

**The transferable rule: take any vertical service you already use and run it through
this template — can an agent call it without waiting for a human, without reading docs,
and pay per use automatically?** First ask "can this service run autonomously."
Only services that can should get their interface redone.

**Three risks to watch**: compliance — verification sits one line away from batch
signups and fraud, and platform bans or legal action can hit at any time; it is a
channel business — stars rose because the MCP ecosystem is rising, not because it is
irreplaceable, and a big player (Twilio and peers) getting into MCP is only a matter
of time; and agent-facing pricing invites faster price wars than consumer markets
when competitors arrive.

## What to watch next

① Whether stars pass 1,000 in three months — whether it still grows after MCP hype
cools is the real demand signal
② Whether an agent platform (Claude Code, Cursor) builds it in or partners with it —
being embedded is both absorption and category validation
③ Whether any ban/compliance incident becomes public — the life-or-death line for
this kind of business

## What you can take from it

**Product logic**: if your product or API is repetitive, autonomous, and usage-priced,
seriously consider an agent-native entry (MCP or skill) and price it as pay-per-result
with automatic refunds on failure. Agent customers do not read your site and do not
call support; they read your API docs and your failure rate.

**Positioning language**: the comparison-page move is worth copying — list each
competitor, and honestly include the rows where they win. Marketing to agents is just
laying out the facts.

**Pricing structure**: pay-per-call plus auto-refund on failure plus rate-limit-not-quota.
This combination persuades agent customers far better than a subscription.

## Verdict

**Worth watching.** A clean channel pivot that turned "giving agents an identity" into
a transparent, usage-priced business. But its moat is not technical — it is compliance
handling and speed of response to the agent ecosystem, both unproven. Come back in
three months against the three checks above.
