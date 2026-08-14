---
slug: pacific-slate
name: Pacific Slate
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A self-hosted, multi-agent personal assistant written by one MBA student for himself:
models (rented) and data (his own) are strictly separated, and all data stays on his
own server.

## Who built it

Builder field says badwx (HN handle). The site self-describes: a current MBA student,
married with two children, no formal software background. The development method is
"AI-native" — he designed the architecture himself (components, connections, budgets)
and let coding AI agents write most of the code. The system has run daily since early
2026 through August 2026.

_Read: this is not a product, it is a "single-user system architecture reference." Its
value is not how many people use it, but that it proves a non-programmer can assemble
a daily-use private AI system out of self-hosting, multiple models, and cost control._

## What it actually does

- **Autonomous information stream** → pulls from email, calendar, GitHub, HN, Reddit,
  arXiv, RSS, weather, markets, earthquake data, and more on a schedule; scores items
  by relevance, importance, and novelty; produces briefings
- **Multi-agent collaboration** → 1 operator + 7 expert agents (coder, researcher,
  analyst, productivity, reviewer, evaluator), built on Google's ADK, each with
  least-privilege permissions
- **Model-agnostic** → capabilities exposed through an MCP gateway and OpenAI-compatible
  endpoints; swapping models is one config change and touches neither memory, data,
  tools, nor routing
- **Four-layer memory** → knowledge corpus, continuity graph, semantic memory, and
  hierarchical context; remembers preferences and past decisions
- **Cost routing** → a deterministic scorer (no model involved) rates prompt complexity
  1–5 and, combined with budget usage, picks the model tier; there is a monthly budget
  cap
- **Reliability engineering** → health tracking and cooldowns for rate limits, a
  first-token timeout watchdog, a degradation chain (primary model fails → backup
  takes over → explicit failure message), and no crashes
- **Traceability + data sovereignty** → every answer carries source citations; all
  data lives on his server, exportable and deletable, not used to train models;
  external requests go through zero-data-retention endpoints

**Operating shape**: Next.js canvas frontend + Starlette backend + ~24 MCP tool
servers behind a gateway (BM25 search finds the right tool instead of stuffing all
schemas into context); answers render as movable cards, each labeled with model, cost,
and latency.

## What old behavior it replaces

For the author personally, three kinds of old actions:

**Explaining yourself over and over to different AI programs.** Switching models or
tools meant re-communicating context; a unified system that self-updates, remembers
preferences, and keeps data private ends that.

**Long chat threads.** One task, one conversation, scrolling forever. Now it is
movable cards on a canvas, each labeled with which model did it, what it cost, and
how long it took.

**Dependence on a single model.** Switching vendors used to be a migration; now it is
a one-line config change.

For the general reader, it replaces "subscribing to a pile of AI services" with an
alternative: rebuild a private version for $50–80/month with all data in your own hands.

## Business model

**None.** Not a product — a personal system plus an open-source blueprint (the site
says "almost all of it is open source"). The author's reconstruction estimate:
~$20/month coding assistant, ~$20/month small server, $10–40/month metered model
calls, about $50–80/month total.

_Read: this should not be evaluated as a business model. The real question is whether
the architectural blueprint can be reused by others — if it can, it becomes a valuable
reference for the self-hosting AI community._

## Hard numbers

- Running totals: **13,053 runs, 26,515 model calls, 9 models used**
- Performance: median model-call latency 3.1s, p90 latency 14s
- Knowledge base: ~**14,000 documents / 196,000 text passages**
- Users: 1 (the author); explicitly not aimed at enterprise or multi-tenant
- HN 5 points / 0 comments (2026-08-11) — essentially undiscussed
- Team: 1 person, with AI coding agents as development partners

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Single-user system, needs are his own — perfect fit, but it is a personal tool, not a startup |
| Product insight | Three designs transfer well: model/data separation, deterministic cost routing, and BM25 tool lookup instead of stuffing schemas into context |
| Execution quality | Health tracking, degradation chain, zero-data-retention, audit logs — reliability thinking beyond most commercial products |
| Timing | Self-hosting + model-agnostic + data sovereignty is moving from technical preference to procurement requirement; timing is right, but this is not a product the market can "adopt" |

## The call

**This is a "single-user architecture reference," not a product, and the data says
Unproven.** HN 5 points, zero comments, no users, no commercial intent — but it should
not be graded as a product. It should be graded as a blueprint.

**Three designs worth stealing**:
First, **deterministic cost routing** — a rule (complexity score 1–5 × budget usage),
not a model, decides which model tier to use, avoiding the self-contradiction of
"let the LLM decide how much money to spend."
Second, **model-agnostic as a first principle** — swapping models touches neither
memory, data, tools, nor routing; "no vendor lock-in" is architecture fact, not a
slogan.
Third, **tools behind a gateway with BM25 lookup** — 24 MCP servers never enter
context; retrieval finds the right tool on demand. Same idea as mcptoon, different
implementation.

**The biggest question mark**: the reliability numbers (3.1s median latency, 13,053
runs) and the architecture diagram are self-reported by a non-programmer writing with
AI agents; no third-party verification and no direct repo link visible on the site.
So it is a "reference design worth reading," but every number must be discounted.

## What to watch next

① Whether the code actually goes open source (downloadable, reproducible) — a
blueprint's value depends on being reusable
② Whether monthly cost stays around $50–80 — the cost claim is its most falsifiable
assertion
③ Whether anyone builds a team version or an open-source project from it — reuse is
the evidence that this architecture actually works

## What you can take from it

**Product logic**: for deciding "which model to use," do not let the LLM decide —
route with a deterministic scorer (complexity score × budget level): controllable,
explainable, auditable. Any multi-model product team can copy this routing logic
directly.

**Positioning language**: "models are rented, data is yours" — compressing
model-agnosticism plus data sovereignty into a balanced phrase is a positioning
sentence every self-hosted product can use.

**Pricing structure**: no business model, but the broken-down cost items (~$20
coding assistant + ~$20 server + $10–40 model calls) are themselves a pricing
reference — the selling point of self-hosted options is "total cost below the sum
of subscriptions."

## Verdict

**Unproven, but worth filing.** Not a product — a complete design document for "one
person plus AI agents builds a private AI system," with three genuinely transferable
designs: cost routing, model-agnosticism, and tool retrieval. All data is
self-reported and no direct code link is visible, so the grade is Unproven by the
data — but this blueprint deserves a read by anyone planning a self-hosted setup.
In three months, check whether it is actually open-sourced and reused.
