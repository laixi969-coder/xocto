---
slug: markupbase
name: markupbase
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Not more logging for your agent, but a standalone artifact for the work that deserves review —
human-readable, versioned, evidence-bound, so a person can still understand, challenge, and stop
what an agent did after the fact.

## Who built it

A whitepaper, "Making Autonomous Work Reviewable," published August 2026 by the company MarkupBase
(markupbase.com). The same company runs a product for reviewing Markdown and HTML with people and
agents: publishing artifacts, inline comments, immutable versions, and review assignments to agents
over MCP (mcp.markupbase.com).

_Read: a company selling review software writes the methodology for why review deserves to exist as
its own layer, then points the product at the conclusion. A whitepaper is a zero-cost move. What
matters is whether anyone outside the product adopts the framework._

## What it actually does

**The whitepaper**:
- **Defines the "review artifact"** → a work statement answering nine questions: what was requested,
  what is the scope, what changed, why this approach, what supports the conclusion, what could go
  wrong, can it be rolled back, what human judgment is needed, what work is being approved
- **Rejects three older review surfaces** → chat transcripts (record what was said, not what
  happened), activity logs (answer narrow questions, never why), approval prompts (show a command
  without business impact, and decay into conditioned reflexes)
- **Four review modes** → proposal before action, record after action, exception-based, and periodic;
  they coexist
- **Four action tiers** → 0 observe / 1 reversible / 2 significant / 3 critical, from "periodic
  sampling" to "two-person control, full evidence, retained decision record"
- **Eight requirements for trusted review** → approval bound to exact actions, immutable versions,
  claims tied to evidence, clear identity and permissions, least privilege, visible uncertainty,
  protected sensitive material, source and rendered view preserved

**The product**: publish a Markdown/HTML artifact → people and agents comment inline on the same
immutable version → review requests and status → version history. Isolated preview and separated
identities on the security side.

**What it deliberately does not do**: no final decision by the tool, no execution layer — a
deliberate narrowing to "designed for review, not execution."

## What old behavior it replaces

Reviewing agent work used to mean three things: scrolling a chat log (records what was said, not
what happened), checking activity logs (answers which call fired and whether it errored, never why),
and clicking approval prompts (shows a command with no business impact, until clicking becomes a
reflex).

All three live inside the agent's running account of itself. The whitepaper's move is to pull the
object of review out of that running account and give it its own artifact — versioned, anchored to
specific sentences and rows — so review reads the artifact, not the conversation.

For that substitution to hold, the artifact must be cheaper than the log and hold up better when
looked at later.

## Business model

**Not disclosed.** No pricing in the whitepaper; no pricing or user numbers on the product page.

_Read: the classic "thought leadership first" move. Whether this framework becomes money depends on
whether "review artifact" gets absorbed by bigger agent platforms as a standard. Being copied is
traffic; being copied and still unable to charge is the risk._

## Hard numbers

- Public lessons cited in the whitepaper: Knight Capital's $460M loss in 45 minutes in 2012;
  Moffatt v Air Canada (2024) liability for chatbot misinformation; Mata v Avianca (2023) lawyer
  submitting AI-fabricated citations; Replit (2025) agent deleting database data
- 4 anonymized composite cases + 4 public precedents; 9-question artifact template; 4 action tiers
- HN: 5 points, 1 comment
- Product user count, pricing: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A review-product company writing review methodology — fit, but zero public evidence of users |
| Product insight | Making "review" a standalone artifact instead of a log search; the nine-question template is a rare executable checklist |
| Execution quality | A real product exists (MCP service, immutable versions, inline comments), but reliability cannot be independently verified |
| Timing | Agent audit and compliance demand is just becoming visible — half a step early, but the direction is right |

## The call

**"Review artifact" is a transferable framework, but it is a whitepaper, not a product.**
Give high-risk agent output its own standalone artifact, bind approval to an exact version, and match
review intensity to an action tier — all three apply to any product that lets agents do real work.
Its most valuable line: the useful question is not whether a human remains in every loop, it is
whether humans can still see, challenge, and govern the work that matters.

**Its weakness is even earlier than numbat's**: numbat at least has endpoint code; this is a
framework. Anyone can publish a whitepaper; adoption is the only moat. Five HN points says the
market has not received it yet.

**Order of judgment**: platform-level adoption first, then whether the product itself sells.
Neither happening means this is just another good document.

## What to watch next

① Whether "review artifact" gets adopted as standard practice by any mainstream agent platform or company
② Whether the markupbase product publishes users and pricing
③ Whether the nine-question template spawns third-party templates or tools (a copy-count signal)

## What you can take from it

**Product logic**: pull "review" out of the conversation record and make it a versioned,
annotatable, evidence-bound artifact; tier actions (0 observe / 1 reversible / 2 significant /
3 critical) with matching review intensity; bind approval to an exact action and version. When
building AI products, the review layer can itself be a standalone product.

**Positioning language**: one line worth stealing — "The useful question is not whether a human
remains in every loop. It is whether humans can still see, challenge, and govern the work that
matters."

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** The framework has incremental value; the product is unverified. Come back in
three months against the three checks above.
