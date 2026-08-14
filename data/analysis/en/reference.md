---
slug: reference
name: Reference
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Local semantic search for coding agents: it indexes your files and codebase on
your own machine, exposes an MCP server so agents like Claude Code can query it
directly, and returns results cited down to the exact function — fully offline.

## Who built it

Independent developer Rahul Thennarasu, described at launch as a SWE intern
at NASA JPL, incoming at fab2. His founder post is blunt: every new Claude Code
session burned through tokens and context, so he built this.

_Read: classic dogfood product — the author got bitten by the problem in his own
workflow, so he has first-hand feel for where agent code search actually breaks.
Independent developers build dev tools with more honest motivation than a company
initiative, but they also have thinner maintenance resources and distribution._

## What it actually does

- **Local semantic index** → a lightweight embedding model runs on-device; nothing leaves your machine
- **Live auto-reindexing** → the index updates as you save, so results track the code you are actively writing
- **Code-aware chunking** → tree-sitter chunks on functions and syntactic units, so results cite the exact code region, not the whole file
- **Built-in MCP server** → exposes /search, /explain, /find_similar and /check_doc_drift so agents query it directly instead of burning tokens on grep loops
- **Cited answers** → every result points back to a file and function, replacing generic AI advice with grounded, verifiable references
- **Doc-drift checks** → /check_doc_drift flags places where docs have fallen out of sync with the code

**Form**: a Mac desktop app (built with Tauri), open source on GitHub, free during launch.

## What old behavior it replaces

Two things used to happen when an agent needed to find code. First, grep loops:
the agent searches repeatedly, reads whole files, guesses locations — answering a
simple "how did I implement rate limiting" could cost thousands of tokens across
many tool calls. Second, human memory: developers scrolled old chats and old
projects trying to recall "how did I do this last time."

Both are expensive — tokens, time, and unreliable answers. Reference replaces the
"agent greps and guesses" inefficiency with a local, cited, function-level lookup
acting as an external memory layer.

## Business model

**Not disclosed.** Open source, free during launch, no pricing page, no hosted service.

_Read: the obvious monetization path for a "local search + MCP server" tool is
cloud features later — cross-machine index sync, team sharing, heavier local
embedding models. But in an open-source, free-by-default ecosystem, developer
tools rarely clear the willingness-to-pay bar, and whether it ever reaches a paid
tier is doubtful._

## Hard numbers

- launch (2026-08-05), 75 votes in the first week
- Open source on GitHub; star count not independently verified. Team size, user
  count, revenue: not disclosed
- Feature surface: local embedding model + tree-sitter chunking + MCP server with four endpoints
- Platform: macOS desktop app (Tauri)

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author is a heavy agent user; the pain is real, and it is an independent project open-sourced because he uses it himself |
| Product insight | Nailed the real problem of agents burning tokens to find code; making MCP the distribution channel is the smart move |
| Execution quality | Tauri desktop app + tree-sitter + local embeddings — built like a real product, not a demo |
| Timing | Right now. Agents like Claude Code are scaling, and token cost plus retrieval quality are simultaneously becoming bottlenecks |

## The call

**A clean sample of the "external memory layer" category.**

An agent's context window is a finite resource and codebases keep growing.
Reference's move is to split "retrieval" out of the agent's reasoning loop into a
local, cited, one-shot query. That split is correct — the agent never has to load
a whole file into context to locate a function, and the savings are real tokens.

**The transferable rule: for tools that serve agents, the distribution channel is
a protocol, not a UI.** Reference does not ask anyone to open its interface; it
hangs itself into Claude Code's MCP config and gets invoked mid-reasoning. If you
build agent-adjacent tools, plugging into the MCP ecosystem reaches the real
workflow far better than any standalone entry point.

**Two risks.** First, competition: the MCP ecosystem already has open-source code
retrieval tools (Serena is a notable one); tree-sitter chunking plus local
embeddings is not a moat, and the differentiator comes down to experience and
citation precision. Second, monetization: a free open-source tool that never
reaches a paid tier just sits in "author self-use plus community freeloading."

## What to watch next

① Whether GitHub stars pass a thousand in three months — real open-source
traction is more reliable than launch-day votes
② Whether it gets listed in official MCP recommendations by Claude Code / Cursor
— that sets the distribution ceiling
③ Whether paid features appear (team index, cloud sync, heavier local embeddings)
— that decides whether it can support itself

## What you can take from it

**Product logic**: if you build tools for AI agents, make cited answers the
default — every result points back to file, function, and line so the agent's
output can be verified rather than trusted on vibes. That is both a technical
feature and a trust mechanism: no one, human or agent, adopts a tool whose answers
cannot be traced to evidence.

**Positioning language**: the founder's line — "every new session burned tokens
and context, so I built this" — is the standard "personal pain → product"
narrative, and what makes it copyable is the concreteness: numbers, scenes, and
actions instead of "improve efficiency."

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** The direction is right, the pain is real, and the engineering
is credible, but traction and business model are unproven. It is a clean sample of
the "local memory for agents" category — worth watching to see whether it survives
in the MCP ecosystem and reaches a paid tier.
