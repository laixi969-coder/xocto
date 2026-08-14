---
slug: mcp-memory
name: MCP Memory
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A persistent memory layer for agents: everything to be remembered is written as an OKF-spec
Markdown file with metadata (human-readable, diffable, git-managed), while a SQLite FTS5 index
gives the agent near-instant lookups.

## Who built it

A solo project by fellowgeek (author handle pcbmaker20), MIT licensed, first commit 2026-08-13.

_Read: something one person built in a day pulled 58 points and 35 comments on HN and hit 124
stars on day one. That means timing: OKF was published by Google in mid-June, and this is the
first decent implementation pairing OKF with MCP memory._

## What it actually does

- **Store** → `memory_store`: writes a memory record as an OKF v0.2 document (YAML frontmatter
  with type/key/namespace/tags/sources/verified/stale_after) into a `memory/` folder in the project
- **Retrieve** → `memory_retrieve`: exact lookup by key
- **Search** → `memory_search`: SQLite FTS5 full-text search with tag/namespace filters; claims
  sub-20ms key lookups
- **Session handoff** → `memory_get_last` / `memory_update_last`: records "where work stopped"
  across sessions and resumes the checkpoint at session start
- **Zero config** → `setup.py` auto-registers into Antigravity / Claude / Cursor / Windsurf / Codex

**The dual-layer design is the point**: the source of truth is plain Markdown (readable,
reviewable, versionable); SQLite is only an acceleration index. This is the opposite of the
"embedding vectors in a binary store" school — humans stay the authority.

## What old behavior it replaces

Agent "memory" today runs on three ad-hoc schemes, each broken in its own way.

First, hand-maintained project files like CLAUDE.md / AGENTS.md. You write them and update them;
the agent never writes into them on its own. That is one-way — a sticky note, not memory.

Second, the built-in memory features of Claude / Cursor, which are locked to one tool. Change
tools or machines and the memory is gone.

Third, re-feeding whole conversation histories and "remembering" by burning tokens. Expensive,
and long-term memory does not fit in a context window.

mcp-memory replaces the intersection of all three: memory the agent writes itself, reads itself,
in an open format, portable across tools. One HN commenter made the point cleanly: an MCP server
architecture makes this usable from claude.ai and other surfaces where you have MCP but no
filesystem.

## Business model

**None.** Free and open source; no hosted service, no pricing page.

_Read: memory is the foundation of agent apps but the foundation itself is hard to charge for —
every peer (mem0 and friends) is betting on "occupy the slot now, monetize higher up later."
This repo is clearly a land-grab play too._

## Hard numbers

- **124 stars, 2 forks.** Repository created 2026-08-13 (same day)
- HN: 58 points, 35 comments (around 2026-08-13)
- Claims sub-20ms key lookups (self-reported, not reproduced)
- Dependencies: SQLite + Python + FastMCP; **no embeddings, no vector database**
- Users and production deployments: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A solo dev, built in a day; this is "the OKF MCP implementation," not a memory product |
| Product insight | Bet on two right cards — OKF normalization plus pure-local no-vector-store. But what memory should hold, and what deserves remembering, this design never answers |
| Execution quality | Well-documented, tested, clean dual-directory structure; high completion for a solo project |
| Timing | Perfect. One month after OKF shipped, memory is one of the hottest MCP lanes, and this is among the first deliverables |

## The call

**A textbook case of "when a standard just ships, be the first decent implementation."** OKF
came out in mid-June; by mid-August this project shipped an MCP implementation with spec
conformance and dual-layer storage, and used Show HN to get discussion volume far above its star
count. Speed is its moat attempt — though it is not really a moat.

**The transferable rule: bet on freshly released open standards and be the first credible
landing.** A new spec's window lasts only a few months — too early and you build against a moving
target; too late and it is a red ocean. The test is the spec's release date plus "no credible
implementation exists yet." Applied to products: for any structured agent memory, make the human
the only authority first, and worry about retrieval speed second.

**But the HN thread already asked the soft questions**: "How is this different from grepping a
memory/ directory?" "How does it beat Claude's built-in memory — got benchmarks?" The author had
no benchmark answer. When "what to record, what deserves remembering, and how to make the model
actually consult it" have no answers, 124 stars is topic heat, not product validation.

**One hidden risk**: OKF is Google's spec and only at v0.2. When the spec changes, every stored
memory needs migration.

## What to watch next

① Whether a reproducible benchmark appears, proving gains in task-completion over Claude's
  built-in memory or a grep-based approach
② Whether an ecosystem forms (others following the OKF + MCP combination) or it stays a singleton
③ Repo activity in three months: Show HN stars decay fast; what matters is follow-up commits and
  issue handling

## What you can take from it

**Product logic**: for agent-memory features, ship human-readable, reviewable plain-text storage
first and accelerate with an index — do not jump straight to a vector store. Auditability is
scarcer than retrieval quality in agent memory.

**Positioning language**: none. The README is engineering documentation; nothing to steal.

**Pricing structure**: none. Free and open source.

## Verdict

**Worth watching.** The timing and the craftsmanship are both clean, but this is a
"standard-landing bonus" project, not the answer to the memory problem. Product definition —
what gets remembered — is the real winner-maker in this lane, and it has not been touched.
Come back in three months against the three checks above.
