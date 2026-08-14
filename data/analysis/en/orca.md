---
slug: orca
name: Orca
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

It compresses "which store the subscription was bought in, and whether it works on every platform"
into one unified ledger: subscription state synced in real time across iOS, Android, macOS, Linux,
Windows, and Web — with zero revenue share.

## Who built it

A product from pcvetkovski, founder of Maxint (orca.maxint.com). His own app ships across six
platforms and was stuck on multi-platform subscriptions: RevenueCat and Adapty only supported mobile
and web, desktop required hand-rolling, and GitHub issues sat unanswered for months. So he built the
orchestration layer internally, ran it for 12+ months and tested it with thousands of users, added
an MCP server early this year, and is now launching publicly.

_Read: the classic internal-tool-grows-into-a-product path — bitten by the problem first, solved it,
now selling the solution. The founder's authority on this pain point is the most grounded of this
batch._

## What it actually does

- **Six-platform sync** → connects Apple StoreKit, Google Play, Stripe, and GoCardless; a user pays
  or cancels on any platform and entitlement state updates everywhere in real time
- **Unified ledger** → each store's events normalize into one record: user, entitlement, platform,
  active flag, expiry time
- **Config as code** → Stripe price IDs, GoCardless plan IDs, Apple product IDs, and Google
  subscription IDs live in a single config file, no double-bookkeeping across portals
- **SDK coverage** → Flutter/Dart, TypeScript, Swift, Kotlin, more on the way
- **MCP server** → lets AI agents operate the stores directly: create products, map subscriptions,
  manage entitlements, pull insights
- **Edge validation** → entitlement states evaluated at the payment edge; the comparison page claims
  <50ms validation (RevenueCat claims 150–400ms)
- **0% revenue share** → flat monthly tiers, no percentage of revenue

## What old behavior it replaces

**Setting up products and entitlements by hand in every store.** The old flow: set it up once in
Google Play, once in the App Store, once in Stripe; change one and forget another, and users' access
diverges across platforms.

**Maintaining your own server-side receipt validation and background schedulers.** Invoice
validation, renewals, grace periods, and edge cases meant writing your own multi-threaded scheduler.
Orca absorbs all of that and leaves you a single ledger API.

**Desktop platforms left to fend for themselves.** Most concretely: RevenueCat and Adapty do not do
macOS/Linux/Windows, so desktop apps either build their own subscription state machine or sell on
one platform only. Orca replaces that "build it yourself or give up" dilemma.

## Business model

**Explicit.** SaaS tiers: free at 500 active entitlements (~$3.5k MRR scale); Pro $299/mo at 10k;
enterprise custom, starting at $999/mo. Add-ons priced separately: storage $49/mo per 50GB, MCP
Server API $199/mo (requires Pro), Growth Intel $149/mo. The core pitch: 0% revenue share —
versus RevenueCat's up to 1% of gross MRR.

_Read: the most standard move against an incumbent there is — the incumbent takes a percentage of
your revenue, you charge a flat fee. The unit of account shifts from "your revenue" to "a fixed
bill," which is real savings for a growing product. The problem: this model has no moat of its own.
RevenueCat announcing desktop support is one release away._

## Hard numbers

- Pricing: free at 500 active entitlements / Pro $299/mo at 10k / enterprise from $999/mo; MCP
  add-on $199/mo
- Page claims 12+ months internal use and thousands of tested users (self-reported, unverified)
- Claims of <50ms edge validation, 0% revenue share, six-platform SDKs, and an MCP server (all
  self-reported on the product page)
- HN: 5 points, 0 comments
- Revenue and public user counts: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Someone who was blocked by RevenueCat's blind spot building a desktop subscription tool — lived pain, strong fit |
| Product insight | Took the desktop-subscription gap the incumbent explicitly ignores and made 0% take-rate the price weapon; clean positioning |
| Execution quality | Six-platform SDKs, MCP server, edge validation — wide engineering surface; newly launched, no third-party validation of stability |
| Timing | Desktop and cross-platform apps are being revived by the agent era, so subscription infrastructure demand is real; zero HN comments says cold start is weak |

## The call

**Worth watching, because it got two things right, and both transfer.**

**First, 0% take-rate is the standard weapon against a revenue-share incumbent.** Any payment or
distribution infrastructure facing an incumbent that takes a percentage of revenue can copy this
directly: flat fee + 0% take-rate + a free tier. Change the unit of account and you change the
marketing story.

**Second, an MCP server is a new interface for B2B tools.** Letting AI agents operate your system —
create products, map configurations, pull insights — is not a gimmick; it turns the product into an
agent-programmable surface. For AI product builders, that is a new distribution surface worth copying.

**The risks are equally standard**: the incumbent needs only one release to close the gap; the
5-point, 0-comment cold start says market education is early; and the sustainability of "0% take-rate"
depends on actually making the cost structure work flat.

## What to watch next

① Whether public user counts and revenue get disclosed — can 12 months internal and thousands of
   users convert into public numbers
② Whether the MCP server gets used by third-party agent workflows (not just marketed as a feature)
③ Whether RevenueCat or Adapty announces desktop support — incumbent retaliation is the biggest risk
   for a company like this

## What you can take from it

**Product logic**: platforms the incumbent ignores (desktop) are where new categories start; making
your product operable by agents (MCP-ization) is a new interface for B2B tools. When building AI
products, "let agents call my product directly" belongs in the feature plan, not in the nice-to-have
column.

**Positioning language**: one line worth stealing — "Other cross-platform billing wrapper services
charge up to 1% of your gross MRR. We think that is extortionate." Reframing the category by calling
the industry's convention unreasonable is stronger than saying "we are cheaper."

**Pricing structure**: tier by "active entitlements" rather than seats or devices — the free tier
caps at 500, Pro at 10k, the unit maps directly to user scale; capability add-ons (MCP, growth
analytics, storage) priced separately instead of bundled into the main plan. Both the unit design and
the a-la-carte add-on menu are copyable.

## Verdict

**Worth watching.** Real need, real pricing, real internal usage history; public validation is thin
and the cold start is weak. Come back in three months against the three checks above.
