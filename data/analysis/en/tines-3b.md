---
slug: tines-3b
name: Tines 3B
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

The stuff employees build with AI — agents, apps, automations — gets a secure place to
run: isolated execution, credentials injected through a proxy, everything auditable,
inside an environment IT and security can actually see.

## Who built it

Tines, the Dublin-founded workflow automation company (2018), co-founded by Eoin
Hinchy (CEO; ex-DocuSign, eBay, Deloitte) and Thomas Kinsella (ex-security engineer).
The original Tines Stories product served security and IT teams for eight years. 3B,
launched 2026-08-11, is a ground-up new platform — the launch platform daily #1 (405
upvotes).

_Read: a company that has raised $272M and serves major banks publicly declaring that
its own core category has an expiry date is a stronger signal than any startup pitch.
When models can write code, visual drag-and-drop builders are over — the money moves
to the run-and-govern layer that comes after everyone can build._

## What it actually does

- **Natural-language workflow authoring**: describe what you want, the LLM writes the
  implementation, and every generated step can be revised individually
- **Isolated execution**: each step runs in an ephemeral gVisor sandbox / Docker
  container, destroyed and recreated per execution
- **Credential proxying**: secrets are injected through an egress proxy — never in
  code, never in environment variables, never in logs
- **Full auditability**: logs and monitoring on everything; admins see which workflows
  are running, failing, or exposed to the public internet
- **Autotune**: automatically flags anomalies and suggests fixes; admins approve on a
  reviewable branch before anything goes live
- **Flexible deployment**: hosted, self-hosted, or hybrid; bring your own LLM or any
  vendor
- **Free Explore Edition**: 3 live workflows, unlimited users, spaces, and connectors

## What old behavior it replaces

Two layers. **Directly**, it replaces manual management of shadow AI work: finance and
marketing used to build things in Claude Code or Codex on personal laptops or personal
Vercel accounts, with API keys pasted straight into code — invisible to IT and
security, cleaned up by hand when something broke. 3B gives that work a default
governed home — making the governed path the easy path.

**Indirectly**, it replaces Tines's own old product: the CEO states plainly that
"low-code has a sell-by date." Once models can write code, the visual builder gives way
to natural-language generation plus deterministic code execution. The eight-year-old
Stories product runs in parallel, awaiting the handover.

## Business model

Free Explore Edition (3 workflows to start) plus enterprise subscription (pricing not
public). The parent company has raised $272M total, with a $125M Series C at a $1.125B
valuation in February 2025.

_Read: 3B has no pricing page yet, which means it is still in "get enterprises to use
it first" mode. Products like this eventually price by workflow/seats/execution volume;
the free tier exists to move shadow work into visible space before anyone talks money._

## Hard numbers

- launch 2026-08-11: daily #1, 405 upvotes
- Parent company: 400+ customers (Coinbase, Databricks, CrowdStrike, SAP, Reddit,
  Notion, Mars), 364 employees
- 1.0-1.5 billion automated actions per week (source-dependent; official range)
- 124% net revenue retention, 59% weekly-to-monthly active ratio, 302% YoY growth in
  AI capability adoption (company-reported)
- $272M raised, $1.125B valuation

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Founders came from security engineering; for 8 years the question was "who gets access to what and who can see it" — the new category is the same question extended |
| Product insight | Saw the new-era contradiction: employees using AI is what the boss asked for, but the boss cannot see what the AI is being used to build |
| Execution quality | Isolated execution, credential proxying, full audit — eight years of security-automation engineering behind it |
| Timing | Dead center on the pivot from "get AI working" to "lock down what AI built" |

## The call

**One of the strongest signals in the enterprise-AI-governance category.** Not a
startup telling a story — a company with $272M raised and Coinbase/SAP/Reddit on its
roster declaring its own eight-year core dead and betting on the new layer. Three
things to take:

**First, shadow work is the real enterprise entry point for AI procurement.** The boss
does not fear employees using AI; the boss fears employee-built AI outside the
sightline. 3B's positioning ("You told everyone to use AI. Now give them a secure place
to do it.") talks to the CEO's actual dread, not to a feature list.

**Second, the right way to build a security product is to make the governed path the
easiest one.** Isolated execution, credential proxying, Autotune auto-fixes, branch
approval — following the rules is less effort than not following them, so people stay
inside. Security built as a checkpoint gets routed around; security built as the
default path gets inhabited.

**Third, a reference architecture for agent runtimes now exists**: ephemeral-sandbox
isolation, secrets that never enter code, end-to-end audit, self-hostable. Anyone
building agent infrastructure can copy this baseline directly.

**Risks**: 3B just launched with no standalone revenue or adoption numbers yet; the old
Stories product still runs in parallel, so it is not yet clear whether 3B is a second
curve or a label on the old product.

## What to watch next

① Whether Tines discloses Explore Edition workflow counts and retention
② Whether any enterprise publicly says it runs 3B in production — so far the only
cited voice is Fin, one financial firm
③ The revenue mix between Stories and 3B — if the old business keeps growing while 3B
is a separate curve, the call needs updating

## What you can take from it

**Product logic**: make security the default path, not a checkpoint — admin dashboards,
branch approvals, Autotune auto-fixes. A security product sells peace of mind, not
restrictions.

**Positioning language**: pitch the value as a narrative ("You told everyone to use AI.
Now give them a secure place to do it.") aimed at the CEO's real anxiety, instead of a
feature list.

**Pricing structure**: the free tier is "3 workflows + unlimited users" — even the top
of an enterprise security funnel is free. Move the shadow work into visible space
first, talk about money second.

## Verdict

**Worth watching.** Direction, team, and capital are all validated. What remains to be
validated is whether 3B grows standalone adoption. Check back in three months against
its disclosures and customer voices.
