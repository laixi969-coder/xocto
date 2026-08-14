---
slug: passmint
name: passmint
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A Node library that issues Apple and Google Wallet passes from any edge runtime — the same pass
data produces a signed `.pkpass` for iOS and a save-link JWT for Android, without any Node
built-ins.

## Who built it

alexpate (Alex Pate), an independent developer long embedded in the JS/TypeScript/edge-computing
world, with prior work near the Pusher and StackBlitz ecosystems. The repo lives under the
getpassmint organization, and there is also passmint.com plus an npm package `@passmint/node`
("official Node SDK for the Passmint API") — the latter hinting at a hosted API service behind it.

_Read: when a solo developer ships a library first, the usual plan is to charge for a hosted
service later. The library is the funnel and the trust-builder._

## What it actually does

- **One schema, two wallets** → after `Pass.eventTicket({...}).build()`, `sign(apple)` yields
  `.pkpass` bytes and `toGoogleSaveLink(google)` yields a Google Wallet save-link JWT
- **Edge-native** → zero `node:*` imports, Web Crypto only; runs on Cloudflare Workers, Vercel
  Edge, Deno, Bun, Supabase Edge, Netlify Edge, and Node 20+
- **Engineering guardrails** → ~21 KB gzipped, strict TypeScript, Valibot discriminated unions,
  typed error hierarchy; CI includes a bundle-guard that fails the build on any `node:*` import
- **Common pass styles** → event tickets plus the usual Apple/Google pass families (exact
  coverage not fully verified)

## What old behavior it replaces

Supporting both Apple and Google Wallet used to mean maintaining two generation paths: hand-built
`.pkpass` with manifest and signature (usually node-forge / node:crypto) on the Apple side, and a
separately constructed JWT on the Google side. Worse, those Node built-ins do not exist in edge
runtimes, so teams ended up running a dedicated "pass issuance" microservice on traditional Node.
passmint replaces both "two logic paths" and "a special service that only runs in classic
environments."

## Business model

**Library is MIT open source; a hosted service is hinted at but undisclosed.** passmint.com is set
as the repo homepage and an "official SDK for the Passmint API" exists on npm, but pricing and
launch status are not public.

_Read: pass issuance is a low-frequency operation, hard to scale on per-call fees. A real business
would have to come from batch issuance or pass-update pushes; otherwise this stays a personal
technical showcase._

## Hard numbers

- **4 stars, 1 fork.** Created 2026-04-15, officially pre-1.0 alpha
- 119 commits, 7 branches, 8 tags, last commit 2026-07-27; npm `passmint` 0.1.0 published ~3 weeks ago
- 5 points on HN, 0 comments
- No users, no revenue data

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Author lives in the JS/edge ecosystem, so the pain is real; it is a personal project, energy and patience ride on one person |
| Product insight | Spotting "edge runtimes also need to issue passes" is right, and the one-schema-two-wallets abstraction is correct |
| Execution quality | Proper engineering — Web Crypto only, bundle guard, publint/attw, changesets releases. Not a demo |
| Timing | Wallet passes as a channel are warming up, but the issuing library itself is a low-moat small market; the hosted API is the real battlefield |

## The call

**Good engineering, tiny market, and today it is still just a business card.** Four stars means no
one has really trusted it yet, and a pre-1.0 API scares off early adopters. The technical choices
(zero Node built-ins, edge-first) are exactly right for its audience, but issuing wallet passes is
not a high-frequency need, and a library alone is unlikely to grow paying intent.

**Watch whether the hosted API lands and how it is priced.** The library is the hook; the service
is the business. If passmint.com never ships a paid offering, this stays a demonstration of the
author's craft.

## What to watch next

① Whether stars cross 100 in three months and whether any third-party repo actually depends on it
② Whether the passmint.com hosted API launches and how it is priced — the real demand test
③ Whether it leaves pre-1.0 and the API stabilizes

## What you can take from it

**Product logic**: for anything that must run in constrained environments, turn "zero external
dependencies" into a CI-enforced gate instead of a promise. passmint's bundle-guard fails the
build on any violating import, converting compatibility from "hope" into "requirement." Copy that
idea for your own multi-runtime library.

**Positioning language**: none. Engineering documentation; nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Unproven.** Solid engineering fundamentals, but no users, no revenue, and no hosted service on
the ground. For now it is a business card for the author. The three checks above are your
three-month re-evaluation.
