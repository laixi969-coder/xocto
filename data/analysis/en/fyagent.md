---
slug: fyagent
name: fyagent
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Collects the models, accounts, skills, and prompts scattered across every AI tool into
one local desktop app, so switching tools no longer means starting over — it is the
carry-on luggage for your "AI identity."

## Who built it

The fy-agent organization, with core contributor `python-rust`. The project started as
VibeKey — a hardware idea for putting AI configuration onto a physical keyboard — before
the team abandoned hardware for a cross-platform desktop app derived from the open-source
project CC Switch. Built with Tauri (Rust backend, React frontend), covering Windows,
macOS, and Linux.

_Read: from "a physical keyboard" to "a cross-platform desktop app," the team hit the
wall of hardware distribution early and pivoted decisively. The CC Switch lineage means
this grew out of existing users, not a demand invented from zero._

## What it actually does

- **Manages models** → one place for providers and model selection, preset or custom
  compatible endpoints, one-click switching
- **Manages connections** → centralized MCP service management, synced to supported AI tools
- **Manages skills and prompts** → Skills and Prompts maintained once, no more duplicate
  installs in every tool
- **Manages routing** → a local proxy for request forwarding, failover, and model
  availability checks
- **Keeps the ledger** → aggregates token usage and estimated cost
- **Carries continuity** → resumes from a previous session and workspace, config backup
  and sync
- **Supported clients**: Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build,
  OpenCode, OpenClaw, Hermes

## What old behavior it replaces

Switching AI tools used to mean reconfiguring everything. Model providers, API keys, MCP
servers, skills, prompts — each tool kept its own copy, scattered across places, painful
to change, and after a switch the AI knew nothing about you. Users either maintained the
same setup in several tools at once or stayed locked into one tool forever.

fyagent decouples "my AI configuration" from "any particular tool" with a single local
dataset (SQLite, stored in `~/.fyagent`) — configure once, then distribute to each tool.
Imports go through the `fyagent://` protocol and show the diff before anything is written.

## Business model

**Source-available, not OSI open source.** Its own components and modifications sit under
the PolyForm Noncommercial License 1.0.0 — free for non-commercial use; commercial use
requires a separate written license. The CC Switch-derived parts stay MIT.

_Read: the classic "community on the free side, enterprises pay on the licensed side"
two-track. So far only the free side exists, and the licensed side does not even have a
pricing page, which means monetization is still an idea._

## Hard numbers

- **204 stars / 8 forks / 73 open issues.** 2,457 total commits, last commit on
  2026-08-13
- Covers Windows / macOS / Linux on x64 and arm64
- macOS builds are ad-hoc signed and not Apple-notarized — the project itself tells you
  to verify checksums before installing
- User counts and paid adoption: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Migrated from CC Switch with an existing user base, but the team identity is fuzzy |
| Product insight | Nailed a real pain — "starting over after a tool switch" — and decoupling the config layer is the right answer |
| Execution quality | Tauri + Rust + SQLite with atomic writes, and imports show a diff before committing. Engineering discipline shows |
| Timing | Agent clients are multiplying; the "running two or three clients at once" scenario is growing. Decent timing |

## The call

**It is betting that "AI identity" becomes the next thing you carry with you.**
Models, skills, prompts, working style — these are tool-agnostic, and binding any of them
to a single client is waste. The direction holds, and the CC Switch lineage means a base
of existing users is already there.

**But "digital persona" is narrative, not feature.** What ships today is configuration
management: models, MCP, skills. That solves scattered configs, not "the AI knows me."
The complete form of a portable persona is behavioral memory — after a switch, the AI
still knows how you work and think. That is a different order of difficulty; the current
ledger and session continuity are only the first steps.

**73 open issues is a signal and a warning.** For a 204-star repo, that issue density is
high, which means demand is high and so is maintenance pressure. Feature requests would
be good news; a bug-heavy backlog means engineering debt is accumulating.

**The license model cuts both ways.** PolyForm Noncommercial keeps commercial
copycats out, but "commercial license by separate arrangement" with no price anchor
scares off potential payers. This category's ceiling depends on becoming the default
config layer for agent workflows — and default config layers tend to be free and open.

## What to watch next

① The ratio of feature requests to bugs in those 73 open issues — demand density decides
whether this is a tool or a project
② When a commercial license page appears and what it costs — a free-only side means no
one is paying yet
③ Whether the supported-client list grows in three months — failing to keep up with new
agent tools demotes it back to CC Switch's role

## What you can take from it

**Product logic**: multi-client coexistence is the real state of the world; decoupling
"user configuration" from "tool binding" is a general architecture for any multi-endpoint
product. An import flow that shows a diff before writing beats direct overwrite on both
safety and trust.

**Positioning language**: none. The README is engineering documentation; nothing to steal.

**Pricing structure**: the two-track of PolyForm Noncommercial plus a negotiated
commercial license — free community edition, enterprise priced in conversation — fits
tool products that want users first and money later. But note there is no price page yet:
this structure solves "how to use it legally," not "how to charge for it."

## Verdict

**Worth watching.** The pain is real and the engineering is solid, but this reads more
like a continuation of CC Switch than a new species, and there is a gap between the
"digital persona" narrative and what actually ships. Write it down and track the
client-coverage and commercial-license lines.
