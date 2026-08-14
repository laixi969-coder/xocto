---
slug: phi
name: phi
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A terminal coding agent that treats edit reliability and context cost as first-class citizens —
edits anchored by content hash instead of whole-file rewrites, sub-tasks run in isolation, and tool
schemas never enter the model's context.

## Who built it

A Go project under the pulseaiclub org, self-described as a "sibling to Pi." Pi is Mario Zechner's
open-source coding agent, whose well-known fork is oh-my-pi (omp); phi's hashline mechanism is
explicitly credited to oh-my-pi. Repository created 2026-08-03, MIT license.

_Read: a clean genetic chain — pi to oh-my-pi to phi — all treating the same disease: coding agents
with fragile edit formats and expensive context. Who exactly pulseaiclub is, and the authors'
backgrounds, are not disclosed. What is visible is going from zero to v0.9.0 in eleven days._

## What it actually does

- **Hashline edits** → the model targets a "line number + content hash" anchor instead of reprinting
  whole files; if the anchor is stale (the file moved under it), the edit is rejected. No brittle
  full-text matching, fewer over-edits and silent corruptions
- **Permission gate** → four modes: interactive (confirmation dialogs), readonly (no writes),
  autopilot (auto-allow), headless-strict (auto-deny, effectively readonly); per-tool allow/deny
  rules with command-prefix matching
- **Isolated sub-agents** → sub-tasks run in separate jobs, full transcripts live on disk, only
  summaries return to the parent context — no context blowup
- **MCP with zero schema pollution** → any number of MCP servers, but tool schemas never enter the
  prompt; the model sees only three meta-tools (mcp_list / mcp_inspect / mcp_call) and discovers on demand
- **Any model** → OpenAI/Anthropic-compatible interfaces, no vendor lock-in; no Node/Electron/Python
  runtime dependencies

**What it deliberately does not do**: no SaaS, no hosting, no IDE plugin — terminal-only, with a
local config file (~/.phi/config.yaml).

## What old behavior it replaces

It replaces not a human workflow but three bad habits of its own category of tool:

- **Whole-file rewrite / full-text string-match editing** → models located edit points by
  reprinting the old text; a whitespace or newline change broke the match, triggering retry loops
  and token burn. Hashline anchors edits to a content hash and fails safe when the anchor goes stale
- **Dumping all MCP tool schemas into context** → most hosts pour every tools/list schema into the
  prompt before you even ask; one browser tool stack can burn 50k+ tokens. phi exposes three
  meta-tools, discovers on demand, and lazily spawns sub-processes
- **Sub-task output polluting the parent context** → the old way was every turn going into the
  parent context; phi isolates sub-agents under ~/.phi/jobs and returns only summaries

All three substitutions share one move: take the places where models err and move them into
deterministic engineering mechanisms.

## Business model

**Not disclosed.** MIT open source, no cloud service, no pricing page, no hosted tier.

_Read: terminal coding agents are the classic "open source for distribution, enterprise edition for
revenue" category, but phi has no enterprise shadow yet. Its only moat right now is mechanical
innovation, and mechanisms are the easiest thing to copy._

## Hard numbers

- **75 stars, 4 forks, 2 open issues** (fetched 2026-08-14). Created 2026-08-03, 196 commits,
  already at v0.9.0
- Release binary ~12 MB; single idle session ~21 MB RSS; first-frame render ~40 ms; cold build ~5.5 s
- ~22k lines of Go / 107 files / 32 packages; only 6 direct module dependencies
- Hashline cites oh-my-pi's public benchmark: 61% token reduction, Grok-4 Fast edit success
  6.7% → 68.3% (that is oh-my-pi's data; phi has published no benchmark of its own)
- Team size and user count: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Anonymous org, main committer yumosx; zero-to-v0.9 in eleven days shows drive, background unknown |
| Product insight | Hashline, the permission gate, and MCP meta-tools hit real pain; the context hygiene call shows engineering judgment |
| Execution quality | Single Go binary, 6 direct deps, cross-platform CI matrix, 196 commits — solid, not a demo |
| Timing | Red ocean for terminal coding agents; 75 stars is a hard climb. The differentiation is real but mechanically easy to copy |

## The call

**Worth watching, because its three mechanisms can be lifted and used separately.**
For anyone building agent products, these are three cheap, high-yield design decisions: anchor edits
to content hashes instead of letting the model reprint whole blocks; discover tools on demand
instead of flooding the context; isolate sub-tasks and return only summaries.

**What to actually watch is the copy speed.** A 75-star project cannot win on scale. It can only win
by being right about the problems — and the moment mainstream tools like Claude Code absorb these
mechanisms, the value migrates to the ecosystem and the project is left with maintenance cost.

**One honest note**: the 61% token reduction and 10x edit-success numbers come from oh-my-pi, not
from phi. Do not credit a sibling project's results to this one.

## What to watch next

① Whether stars cross 1,000 in three months and whether outside projects adopt its mechanisms
② Whether anyone independently replicates hashline or the MCP meta-tool pattern (a mechanism-validation signal)
③ Whether headless mode keeps defaulting to deny execution (a safety-posture signal)

## What you can take from it

**Product logic**: three transferable designs — edit operations anchored to content hashes with
fail-safe rejection; tool schemas kept out of context and discovered on demand; sub-tasks isolated
with summaries only. All three apply directly to agent products, especially when users run cheap
models or long tasks.

**Positioning language**: none. This is engineering documentation.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** The mechanisms have incremental value and the engineering is solid, but it is
extremely early with no user evidence. Come back in three months against the three checks above.
