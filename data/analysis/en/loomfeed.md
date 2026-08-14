---
slug: loomfeed
name: loomfeed
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An open-source Reddit alternative built for AI agents and humans together: content
carries provenance, epistemic status labels, and reputation scores, and the
trustworthiness of AI-generated content is designed into the product.

## Who built it

A solo project by Surya Koritala, MIT licensed. Go 1.25 backend, Next.js 15 frontend,
PostgreSQL 16 (pgvector, pg_trgm), optional Redis. One-command self-hosting via Docker
Compose. First released 2026-08-09, with active commits since.

_Read: one person and a sharply articulated thesis. "Quality is enforced, not assumed" —
when that is the product stance, the author is not building a community, he is running
an experiment about communities._

## What it actually does

- **Provenance tracking** → content's source and evolution are traceable end to end,
  maintained as a citation graph
- **Epistemic status labels** → a five-tier shared language for informational
  certainty: Hypothesis / Supported / Contested / Refuted / Consensus
- **Reputation and trust scores** → move dynamically with community voting; "trust is
  earned, not bought"
- **Human Seal of Approval** → only humans can validate AI-generated content
- **Agent Arena** → AI agents debate side by side in structured head-to-heads, and the
  community votes on the most convincing argument
- **Eight post types** → text, link, question, task, synthesis, debate, code review, alert
- **Three interfaces** → REST (90+ endpoints), MCP, and A2A, so agents can plug in
  directly

## What old behavior it replaces

Traditional forums (the Reddit pattern) fail on two counts in the AI era: AI content
and human content mix indistinguishably, and quality depends on human voting and
moderation — expensive and gameable.

Previously, judging whether a piece of information was trustworthy meant relying on
personal experience and hand-to-hand combat in the comments. loomfeed replaces that
with a systemic mechanism — provenance, status labels, reputation scores, human
backing. Trust shifts from "the reader evaluates it" to "the platform labels it." It
does not replace a specific tool; it replaces a class of workflow: "UGC forums with no
trust layer."

## Business model

**MIT open source, no hosted service, no pricing.** External services (LLM providers,
OAuth, analytics, email) are all optional and off by default; costs of using them are
borne by whoever deploys.

_Read: this is still a project, not a product. But note the structure — the trust
mechanism is packaged as self-hostable open source, and if the mechanism proves out, a
hosted edition is the obvious place to charge._

## Hard numbers

- **212 stars / 2 forks / 0 open issues** (sampled 2026-08-13)
- MIT, Go + Next.js + PostgreSQL, first release 2026-08-09
- REST API with 90+ endpoints, plus MCP and A2A
- Users and deployment instances: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Solo project, thesis-first, high engineering completeness — but community-running ability is untested |
| Product insight | Pinpointed the trust gap in AI-era communities; "epistemic status labels" is a transferable mechanism |
| Execution quality | Three interfaces, eight post types, Docker self-hosting. A complete system, not a demo |
| Timing | Rising AI content share is a certain trend, but "humans and agents in one community" is far from mainstream |

## The call

**It turns "content credibility" from a human duty into a product mechanism.** That is
the most valuable cut in this whole thread. Old forums outsource trust to the reader:
you tell AI posts from human posts yourself, you chase sources yourself. loomfeed makes
provenance, certainty status, reputation, and human backing a layer of the platform, so
readers stop re-judging from scratch every time. The "epistemic status label" pattern
is a layer any content product can copy directly.

**But 2 forks / 0 issues means only the author is pushing this today.** A mechanism
without a second deployment and outside feedback is still a design document. Self-hosted
projects die most often in exactly this gap: "the author runs it happily, nobody else
can."

**"Human Seal of Approval" is the most interesting bet on the board.** It assumes that
once AI content dominates, "verified by a human" becomes scarce in itself. If that
assumption holds, certification-style mechanisms will appear in almost every content
product; if human verification gets mass-forged or diluted, the mechanism depreciates
with it.

**It does not replace Reddit; it replaces the hidden cost of Reddit's trust model.**
Community products fail on cold start, not features. loomfeed's cold start is harder
than a normal forum's because it first asks users to learn the language of epistemic
status labels.

## What to watch next

① Whether forks and issues move — 2 forks / 0 issues means a solo project today
② Whether a second instance gets deployed — a self-hosted project only the author runs
is not a product
③ Whether the epistemic labels demonstrably improve discussion quality — the mechanism
only holds if people actually use it

## What you can take from it

**Product logic**: the AI-content share only rises, and "content credibility" will move
from a human duty to a product mechanism. Adding deterministic status labels
(hypothesis / supported / contested / refuted / consensus) plus a human-backing slot is
a layer any UGC product can copy.

**Positioning language**: none. The README is engineering documentation; nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** The ideas and mechanisms are worth more than its current scale, but
2 forks / 0 issues means it is still one person's system. The mechanism is copyable,
the product is unproven — file away "epistemic status labels," do not commit to the
product yet.
