---
slug: graph2agent-mermaid-diagrams
name: Graph2agent; Mermaid diagrams
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

Translates Mermaid diagrams into explicit text agents can read: humans look at the picture, agents read structured prose, with no model inference in between — purely deterministic conversion.

## Who built it

Author alexandroskyr, posted as a Show HN. Backstory: while building a large high-performance service, he kept specs in Mermaid diagrams to keep context small for humans; people could follow the diagrams, but when he asked agents to implement what was in them, it mostly failed. His conclusion: "agents are good at writing Mermaid diagrams but not good at reading them."

_Read: a classic case of being bitten by the problem in a real project. The pain is specific and reproducible — not a tool built before finding a scenario._

## What it actually does

- **Deterministic conversion** → no model call; expands Mermaid's elements, connections, branches, order, topology, and even "what the diagram does not prove" into explicit text
- **Four launch surfaces** → CLI (brew / Debian packages), MCP server (one-command npx), GitHub Action (required check before a PR merges), and a maintenance bot (changes only generated Markdown context)
- **Measured effect** → on a frozen paired benchmark of 330 private contracts: exact comprehension 63.3%→81.8% (failures 121→60); +8% input tokens, −46% reasoning tokens
- **Explicit limits** → the "evidence boundary" is documented more carefully than the features: layout direction doesn't declare execution order, missing links aren't forbidden, color and styling are presentation unless labeled as contract semantics

## What old behavior it replaces

Getting an agent to implement from a diagram used to mean one of two things: paste the raw Mermaid source (the agent must reverse-engineer nodes, branches, and topology from compact syntax, and often gets it wrong), or manually translate the diagram into prose for the agent (slow, and the translation itself introduces errors).

graph2agent replaces the second — **handing the "human reads the diagram, then explains it to the agent" translation job to a deterministic compiler** — and can sit in CI so every diagram in every PR is agent-ready.

## Business model

**Not disclosed.** Apache-2.0; CLI/MCP/Action are all free; no cloud service, no subscription.

_Read: the commercialization path for a tool like this is becoming the standard — if it becomes the default format for "diagrams for agents," a hosted or team tier could follow. For now it is still proving value._

## Hard numbers

- Show HN: **6 points, 1 comment** (very low heat)
- GitHub (graph2agent/graph2agent): 1 star, Apache-2.0, created 2026-08-09
- Already at v0.4.0, with four surfaces (CLI/Action/Homebrew/MCP) in sync
- Core measurement: +18.48 percentage points exact comprehension (330 contracts), −46% reasoning tokens
- Team, revenue: solo project, not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author was bitten by this problem repeatedly in a large project |
| Product insight | Documenting the evidence boundary more carefully than the features shows he understands the mechanism of agent errors |
| Execution quality | v0.4.0, four surfaces shipped in sync, with benchmark data — far beyond the HN average in completeness |
| Timing | Mermaid-as-specification for agents is becoming a trend; a deterministic translation layer sits at a sensible position |

## The call

**An "idea right, numbers good, market unproven" project.** Its measurement methodology (frozen paired benchmark, 330 private contracts, exact comprehension) is more honest than most — it even states "this benchmark doesn't prove generalization." That is its most worth-learning aspect.

**The problem is distribution.** Six points on HN means it hasn't found its viral sentence. "Getting agents to read diagrams" sounds like a niche engineering trick, not "half the rework saved." The author proved efficacy at the engineering level but hasn't proven anyone cares at the distribution level.

**The bet**: agent input isn't just prompt text; it includes diagrams, tables, and specs. If "the diagram is the agent's specification language" holds, a deterministic translation layer like this becomes infrastructure — but the "if" hasn't happened yet.

## What to watch next

① Whether stars pass 100 in three months (currently 1; HN didn't carry it — watch for other channels)
② Whether graph2agent-mcp's npm downloads keep growing (MCP is its most likely adoption surface)
③ Whether a well-known repo makes its GitHub Action a required PR check — that's the real adoption signal

## What you can take from it

**Product logic**: when feeding context to agents, "make implicit structure explicit" beats "feed more raw text" — his data: +8% input, −46% reasoning. When building agent tools, cut the agent's reverse-engineering burden instead of stacking tokens.

**Engineering practice**: write an evidence boundary for your own tool — state what the benchmark covers, what it doesn't, and what conclusions can't be drawn. This builds trust directly and suits any developer claiming improvement data.

**Positioning language**: none. Its HN title was too technical — which is itself the lesson: a tool needs one shareable sentence.

## Verdict

**Unproven.** Solid engineering, honest measurement, and a sound direction (deterministic translation layer), but distribution and heat haven't materialized and there's only one anecdotal case. Note it and check stars and MCP downloads in three months.
