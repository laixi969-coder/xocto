---
slug: codeburn
name: CodeBurn
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A free, local, open-source ledger for AI coding spend: no keys uploaded, it reads the session
logs your tools already write to disk — Claude Code, Cursor, Codex, Copilot, and ~37-40 more —
and breaks token and dollar spend down by task, model, project, and PR, then goes one step
further and tells you whether the money actually shipped code.

## Who built it

Resham (ProductHunt `@iamtoruk`), an open-source project under the GitHub org AgentSeal.
His stated motivation: burning ~$1,400 in a week on Claude Code, with no idea where it went,
so he built it and open-sourced it. The launch thread also shows Aditya V. Singh
(`@adityavsingh`, self-described ex-strategy/venture, now in an operating role) answering as a
co-builder.

_Read: writing the accounting tool only after burning real money is the most credible origin
story in this category. And the bookkeeper's obsession — "mark it unattributed rather than
smear it somewhere plausible" — is the habit of someone who has actually done financial
judgment, not a growth hacker._

## What it actually does

- **Spend broken down by dimension** → time / project / model / task / tool, down to each model
  call; pricing from the LiteLLM table with input/output/cache split, and it says "estimate"
  out loud for opaque models
- **Attribution down to the PR** → correlates session cost with git commits into four buckets:
  Productive (merged) / Reverted / Abandoned / Ambiguous — answering "did the budget ship a PR"
- **Finds waste and fixes it** → Optimize surfaces cache bloat, retry tax, and expensive models
  doing cheap work, applies the fix, tracks the actual savings, with undo
- **Model comparison on your own usage** → one-shot rate, retry rate, cost per edit, cache hit
  rate, on your real workloads
- **Budget guard** → installed globally or per project; warns at a soft cap (default $5),
  pauses at a hard cap (default $15)
- **One source, five surfaces** → CLI, desktop (Mac/Win/Linux), macOS menu bar, self-hosted
  web, GNOME panel extension, all reading the same local data
- **Agents check their own spending** → an MCP server so Claude Code and friends can answer
  "how much did I burn this week" in the conversation
- **Team sync (preview)** → pushes usage to a remote endpoint; only token counts, cost, model,
  project — no code, no prompts; OIDC login

**What it deliberately does not do**: no shell-client wrapper, no cloud billing platform, no
invoice-grade reconciliation. No account and no telemetry by default; data never leaves the
machine.

## What old behavior it replaces

Figuring out your AI coding spend used to mean two things: provider pages, each with its own
number (Claude.ai's total, Cursor's total) that never add up, or handing API keys to a cloud
aggregator and swallowing the privacy/compliance cost.

CodeBurn takes the third route — **read the session files that already exist on disk**. Every
AI coding tool writes detailed session logs locally; nobody was reading them. It replaces the
"open every vendor dashboard and stitch the bills together" ritual, and pre-answers the next
question too: did any of it become a merge.

## Business model

**Free and open source (MIT); no paid product today.** Sponsor links on GitHub; team sync
marked preview. The founder says plainly on launch: "it's already free, nothing to unlock."

_Read: classic "build the tool, earn trust, monetize later." The valuable bet is the
"cost per useful unit of work" framing — whoever makes that metric the standard owns the
category's pricing power. No evidence yet that they've decided where to charge._

## Hard numbers

- **9.3k stars / 738 forks** (2026-08), MIT, TypeScript-first
- First commit 2026-04-14; current v0.9.20 (2026-08-11) — 0.1 to 0.9 in four months is fast
- Tool coverage: 40 per the README body (37 per the description), including Claude Code,
  Cursor, Codex, Copilot, Devin, Gemini CLI, and others
- Paid users, ARR, funding: none (no paid product)
- A Chinese aggregator claims "150,000+ developers use it"; no first-party source found, treat
  as unverified

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Born from a $1,400-a-week bill and first-hand pain; the conservative attribution habit comes from real financial judgment |
| Product insight | Sees two facts at once — the bill is a black box and session logs sit unread; "attribute to the PR" and "did the spend ship" are angles nobody else took |
| Execution quality | v0.9.20, five surfaces from one local source, 40 tool parsers, an MCP server; high engineering completeness |
| Timing | Right as runaway agent spend becomes a common pain; landing on the same need as Decant confirms the category exists |

## The call

**One of the most serious independents in the AI-observability lane, and its direction — from
"how much" to "what did it produce" — is the industry's correct next step.**

The dashboard is not the asset; the **attribution philosophy** is: numbers that can't be traced
stay "unattributed" rather than being smeared onto something plausible. Users praised this
explicitly in the launch thread — for a finance tool, trust is the product. Their own data
proves the rule: one unbounded directory correlation once attached 129 of 131 sessions to a
single PR, and that lesson was written into the product's constraints.

**Two things decide whether this moves from "worth watching" to "strong pick."** First,
monetization. Free plus sponsors won't sustain chasing format changes across 40 tools; team
sync and the budget guard are obvious enterprise hooks but nothing is priced yet. Second, the
"Optimize applies the fix itself" line — sliding from measurement tool toward an auto-optimizing
agent is either the moat or a fight with the very tools it monitors, and the choice isn't made.

**Competition**: Decant and others sit in the same lane, and vendor-native usage pages keep
improving. CodeBurn's stack of local-first, key-free, honest attribution is hard to copy quickly.

## What to watch next

① Whether a paid tier or clear pricing appears (team sync / enterprise) — where does the first
  revenue beyond sponsors come from
② Whether "cost per merged PR" and similar output-side metrics get adopted by peers — adoption
  means they defined the standard
③ Whether stars clear 15k in three months and coverage keeps pace with new agents — coverage
  is the life-or-death line for this category

## What you can take from it

**Product logic**: when your users already produce the data nobody is reading, build the
"reader of existing data" instead of the "requires instrumentation first" tool — it costs a
tenth of the distribution effort. One `npx codeburn` reads the entire history; that is the
first cause of its growth.

**Positioning language**: "The bill shows a total, and that's it." An exact one-line indictment
of the status quo opens better than a feature list.

**Pricing structure**: none, not disclosed — but the "free + sponsors + enterprise features in
preview" staging is worth copying: let the tool grow into the de facto standard, then layer
the enterprise tier.

## Verdict

**Worth watching.** Real pain, solid engineering, fast growth (9.3k stars in four months), and
an attribution philosophy that is unique in the category. What's missing is a business model and
a decision on the auto-optimize direction; those two determine how big it gets. Note the three
checks above and revisit in three months.
