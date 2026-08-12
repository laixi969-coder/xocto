---
slug: stoaexchange
name: Stoa Markets
verdict: Strong pick
analyzed_at: 2026-08-11
---

## What it is in one line

A public quote board for GPUs: who has stock, at what price, deliverable when — all on one table.

## Who built it

YC S26 batch. The team isn't publicly disclosed.

The positioning line is "The market behind AI hardware," and the landing page opens with live prices
for five SKUs. That choice tells you how they see themselves: **they are not selling matchmaking,
they are selling the price itself.**

## What it actually does

- **See prices** → current clearing prices for five major SKUs, straight on the homepage:
  A100 80GB $9,490 · H100 SXM5 $25,860 · H200 SXM $33,850 · B200 $43,860 · GB200 NVL $67,400
- **Connect the two sides** → counterparties are verified, not anonymous listings
- **Price discovery** → pulls five fragmented kinds of supply into one comparable view:
  OEM allocations, cloud surplus, brokers, data-center operators, secondhand sellers
- Runs separate Data and Research sections, which says the data is a product in its own right

**What it deliberately does not do**: it holds no inventory, provides no financing, offers no escrow.
It works only at the information layer. That restraint caps how big it gets, and it sets the margin structure.

## What old behavior it replaces

Buying GPUs today means working every channel one at a time: asking OEM sales for an allocation quote, asking cloud providers about surplus, getting introduced to a broker, and taking your chances on the secondhand market. Every route quotes differently, and you have no way to know whether the price you got is good.

They state the problem precisely themselves: **"GPU supply has no shared price discovery layer."**

Price depends on model, delivery window, region, quantity, condition, financing structure, and urgency —
seven variables, each of which moves the final number, and nowhere you can see them together.

**The old behavior is unmistakable, high-frequency, and expensive.** A single GB200 NVL is $67,400;
the spread that information asymmetry creates can be thousands of dollars.

## Business model

No published pricing. This shape usually monetizes one of three ways: commission on volume,
data subscription, or research. It runs both a Data and a Research section, which says
**it is at minimum preparing for the last two.**

_Read: commission is the most direct and the easiest to route around — once two parties have found
each other they can close privately. The one that actually holds is the data subscription,
because price data is consumed continuously rather than once._

## Hard numbers

- YC S26 (the current batch)
- Five live SKU quotes published on the homepage — a rare public price source
- Volume, revenue, team size: undisclosed

## Four-way read

| Dimension | Read |
|-----------|------|
| Founder-product fit | Unknown. The team isn't public, and that's the biggest gap |
| Product insight | High. "No shared price discovery layer" names the real problem — they're building a benchmark, not a broker |
| Execution quality | Middling. The difficulty here isn't technical, it's getting real supply data |
| Timing | Good. A secondary market only forms as compute moves from scarce to unevenly abundant |

## The call

Stoa is betting that **compute is turning from a fixed asset into a commodity**.

A fixed asset is bought once, held long, and has no secondary market. A commodity has standard specs,
public quotes, a term structure, and market makers. GPUs are crossing over: the models standardized
(H100 and B200 are unambiguous SKUs), holding periods shortened (a two-year-old card is behind),
and supply diversified. When those three happen together, the middleman's opening appears.

**The transferable rule: when something shifts from "you buy it to use it" to "you can resell it any time," the first party to make money isn't the buyer or the seller — it's whoever publishes the benchmark price.** Oil, shipping, and electricity all took this path: the price index came first, the derivatives and market makers came after.

The cost is plain: right now the moat is zero. Once price data is public, nobody can stop it being
copied, and once two counterparties have met they can trade around the platform. The historical
pattern in these markets is that **the winner is decided by clearing and settlement, not information** —
whoever guarantees that money and goods actually change hands is the one who can hold onto a fee.
By explicitly not touching escrow or financing, Stoa is focusing, and also leaving the most valuable
ground to someone else.

Its relationship with cloud providers is worth watching too. The large ones are both suppliers and
potential competitors, and they have no reason to want their pricing publicly compared.

## What to watch next

1. **How often the homepage quotes update** — weekly or monthly manual updates would make this a research report, not a market
2. **Whether it moves from information into settlement** — escrow, guaranteed trades, or financing would mean they've worked out how to get paid
3. **Whether cloud providers list** — whether the biggest suppliers show up decides whether this is an industry benchmark or a secondhand market

## What you can take from it

**Don't broker. Publish the benchmark first.** In any market where the information asymmetry is severe and the ticket size is large, the play is to get everyone looking at your prices — once enough people are looking, transactions happen at your place on their own.

**Positioning**: the entire landing page argues one thing — GPU supply has no shared price discovery
layer. Stating the industry's illness in a single honest sentence does more work than ten feature bullets.
The proposal structure follows from it: say the painful true thing first, and the solution stands up by itself.

**Pricing**: commissions get routed around; data subscriptions hold. That judgment applies to any
"we'll connect you to the right resource" service business — connecting is a one-off sale,
judgment is a recurring one.

## Verdict

**Strong pick.** It's a clean sample of how an opaque industry gets rebuilt, and it's early enough
that every move over the next year can be used to test the thesis.
