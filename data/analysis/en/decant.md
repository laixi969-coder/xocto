---
slug: decant
name: Decant
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A local-first tool that turns the Claude Code and Codex session logs on your machine into a
searchable, analyzable knowledge base: where tokens and cost go, how full the context windows
run, which files and tools agents touch, full-text search across complete transcripts — plus
distilling reusable workflow scripts from your command history. Zero outbound network calls at
runtime; transcripts never leave the machine.

## Who built it

Maintained by Dosu (dosu.dev), self-described as "Knowledge Infrastructure for Agents." The
repo `dosu-ai/decant` is Apache-2.0, Bun + TypeScript; the most recent active contributor is
Taylor Dolezal (GitHub `teedole`). The pool lists `devstein` as builder, likely the repo's
creator; his relationship to Dosu could not be verified.

_Read: Dosu builds agent infrastructure and runs agents daily, so this is dogfooding its own
logs — Decant is both a community tool and an acquisition funnel for its main product. That
"company core business + free open-source satellite" combo has steadier maintenance momentum
than a purely personal project._

## What it actually does

- **One unified archive** → normalizes Claude Code (`~/.claude/projects`) and Codex (`~/.codex`)
  logs into a single SQLite database
- **Full-text search** → across messages, tool calls, and complete transcripts
- **Multi-dimensional analytics** → token, estimated cost, context, activity, tool, MCP, and
  file usage analysis
- **Browsable, two surfaces** → sessions, projects, files, and ingest diagnostics; CLI and a
  local web UI (127.0.0.1:3000) share one data source
- **Exports** → Markdown / JSON / reports / trajectories
- **Distill** → extracts deterministic scripts, replays, and agent instructions (AGENTS.md
  sections) from command history, redacting secrets on the way out — the feature that separates
  it from a pure ledger
- **Local API** → an OpenAPI 3.1 contract, so agents can query their own history

**What it deliberately does not do**: no cloud, no network calls, no telemetry; because real
transcripts can contain source code, prompts, credentials, and local paths, the project
explicitly requires synthetic session data in issues and tests.

## What old behavior it replaces

Reconstructing "what that agent session actually did and cost" used to mean digging through
scattered JSONL logs under `~/.claude/projects` or trusting a vendor dashboard's single total.
Relationships between sessions, tool-call patterns, and "which files did agents keep re-reading
this week" could not be answered by eyeballing raw logs.

Decant replaces three chores: **reading raw logs** (→ one SQLite archive + full-text search),
**unclear cost attribution** (→ token/cost/context broken down by dimension), and, most
distinctively — **turning past agent work into reusable assets** (distill freezes a successful
run into scripts/skills). That last one stops being accounting and starts being compounding.

## Business model

Decant itself is free and open source (Apache-2.0). Dosu's revenue sits in its main product
(agent knowledge infrastructure); the Decant blog post lands on "see what knowledge your agents
lack, then use Dosu to fill it."

_Read: the classic tool-as-funnel structure — the analyzer is free for installs and goodwill,
and the money lives in the managed "make agents faster and cheaper" service. Judging Decant as a
standalone business is meaningless; judging it as a funnel for Dosu is the real question._

## Hard numbers

- Repo created ~2026-06; 297 commits; current v0.4.0 (2026-08-12)
- Apache-2.0, Bun + TypeScript; macOS / Linux on x64 and arm64; no native Windows
- HN launch: 10 points / 0 comments (pool data); star count not verified first-hand in this pass
- Team: Dosu (company); paying users, ARR: not disclosed
- Note: one AI-generated article describes Decant as an "LLM-request-intercepting proxy with
  847 stars in 24 hours" — that contradicts the actual repo (a local session analyzer) and is
  treated as hallucinated content, not credible

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Dosu is itself a heavy agent user; the insight "agents keep relearning knowledge the company already has" comes straight from self-use |
| Product insight | Hits the same need as CodeBurn from a different angle — not just a ledger, but search and distillation, upgrading "analysis" into "reuse" |
| Execution quality | Local API with an OpenAPI contract, SLSA release verification, synthetic-data discipline — solid engineering norms |
| Timing | Appeared within days of CodeBurn; runaway AI cost is now a confirmed common pain and the category is forming |

## The call

**Landing on the same need as CodeBurn is itself the evidence that the category exists.**

Two products surfaced within the same week: CodeBurn (personal open source, cost dashboard
across 40 tools with budget guards) and Decant (company open source, Claude Code/Codex session
archive plus search and distill). The same pain picked independently by two parties is the
strongest possible signal that runaway AI cost is a general problem.

**Decant's most notable feature is distill.** A ledger tells you where the money went; distill
turns successful operation history directly into scripts, skills, and AGENTS.md sections —
moving from "read the books" to "turn past work into future leverage." That is the line that
separates it from CodeBurn, and the real landing point of the "knowledge infrastructure" thesis.

**Two limits**: coverage is only Claude Code and Codex, far narrower than CodeBurn's 40 tools;
and as a funnel piece, its roadmap will follow Dosu's main-product strategy, not the
standalone needs of Decant users.

## What to watch next

① Whether stars clear 1,000 within three months and the HN attention converts to sustained
  adoption — current public heat is low (10 points / 0 comments)
② Whether any user publicly reports that distilled scripts are actually being reused — it is
  the only feature that differentiates it from a ledger
③ Whether tool coverage expands beyond Claude Code and Codex — coverage is the life-or-death
  line for this category

## What you can take from it

**Product logic**: in "analyze your history" tools, the top tier does not just tell you what you
spent — it distills history into directly reusable assets (scripts, skills, instructions).
That step from visibility to reusability is worth copying in any agent-workflow tool.

**Positioning language**: "Turns the logs your agents write into real numbers." Making "logs
become numbers" the one-line claim folds local-first and privacy in without saying them.

**Distribution**: free open source plus a local API (OpenAPI contract) so "your agents can query
your own history" — making the tool itself an agent-callable node is the right posture for
open-source tools joining the agent ecosystem.

## Verdict

**Unproven.** The company backing is steadier than a solo project, distill is genuinely
distinctive, but public heat is low, tool coverage is narrow, and feature evolution is held
hostage by Dosu's main product. The category judgment — cost runaways are a common pain — was
already proven by Decant and CodeBurn appearing in the same week; wait on the product itself.
