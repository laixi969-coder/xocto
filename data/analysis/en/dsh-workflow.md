---
slug: dsh-workflow
name: dsh_workflow
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

Brings Claude Code's UltraCode mode to DSH (DeepSeek Harness), turning DSH's one-off
multi-agent dispatch into a workflow layer that can be named, saved, governed, resumed and
audited — so "how we split the work this time" becomes "rerun it by name later."

## Who built it

icetomoyo, an individual developer who also maintains a DSH snapshot repo. The project credits
DeepSeek Harness for the capability surface, KodaX for the workflow design reference, and the
dsh-external community for practice.

_Read: what DSH was missing was precisely the workflow product layer — model routing, subagents,
approval and session logs all existed, but there was nowhere to sink strategy into something
reusable. In open-source ecosystems the person who hurts builds the fix first._

## What it actually does

- **Versioned workflow capsules** → each workflow is a v1 capsule carrying manifest, source,
  intent, inputs, requires and provenance, under a unified `async function run(wf, args)` model
- **Six standard patterns** → classify-and-act, fan-out-and-synthesize, adversarial-verification,
  generate-and-filter, tournament, loop-until-done; two built-in workflows (parallel-investigation,
  scoped-review)
- **Three-level discovery** → built-in → project `.dsh/workflows` → personal `$DSH_HOME/workflows`,
  with overwrite rules and safety checks for symlinks, path escape and version incompatibility
- **Run lifecycle and persistence** → stable run id, state machine (running → paused/completed/
  failed/denied/stopped), everything lands on disk by default: run.json, events.jsonl, immutable
  snapshot, results/, artifacts/
- **Resume and rerun** → rerun by run id or saved name, resume-run, effect cache skips finished work
- **Safety constraints** → generated scripts run only in a capability-only QuickJS WASM VM with JSON
  capability RPC, deterministic guards, and approval levels
- **Three entry paths, one engine** → slash commands (/workflow), model tools (workflow_list /
  run_workflow / workflow_manage), background jobs

**What it deliberately does not do**: no new orchestration runtime, no model lock-in, no hosted
service. It is a plugin for DSH, not a replacement.

## What old behavior it replaces

Running multi-agent work on DSH used to be one-off dispatch: every time, the team re-described in
a prompt how to split tasks, parallelize, verify and synthesize. Parallel results scattered across
sessions; an interruption meant starting from zero; a second person running the same job meant
rewriting last time's prompt.

DSH already had a front-desk workflow tool, but it was a channel that ran several jobs in parallel
once — not an asset. dsh_workflow promotes that layer into an engineering asset: strategy becomes
nameable, discoverable, reusable, auditable and resumable, with over-privileged scripts confined to
a capability-whitelist sandbox.

## Business model

**Not disclosed.** MIT open-source plugin, no pricing page, no hosted service.

_Read: the money is not in the plugin; it is in the value it demonstrates. If enough of the DSH
ecosystem wants governable multi-agent workflows, this layer will eventually be absorbed by the
official or a commercial product. Open-sourcing it validates first, monetizes later._

## Hard numbers

- **49 stars, 0 forks, 0 open issues.** Repository created around 2026-08-12
- 5 commits as of 2026-08-13, yet structurally complete: 179 Vitest tests, an 80% coverage
  threshold, documented security model and architecture
- TypeScript, Node >=22.19, pnpm workspace, QuickJS WASM sandbox, MIT
- Author's background and actual users: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | icetomoyo is a DSH ecosystem participant with a real pain point, but maintenance longevity of an individual project is unknown |
| Product insight | Nails the jump from one-off dispatch to governable asset; the six patterns and resume mechanism are not padding |
| Execution quality | 179 tests, safety-checked discovery, capability-only sandbox — engineering attitude more mature than 5 commits suggests |
| Timing | Depends on DSH ecosystem diffusion, which is far from mainstream |

## The call

**A demonstration of turning multi-agent dispatch into workflow assets, with unusually restrained
engineering choices.**

The most notable design is the capability-only VM — generated scripts are untrusted by default and
run only in a restricted sandbox. Once a workflow becomes saveable and reusable it will be executed
repeatedly, which amplifies the risk of malicious or over-privileged scripts. Defaulting to
distrust is the right starting point.

**The transferable rule: any upgrade from a one-off operation to a reusable asset must first answer
who covers the abuse risk of reuse.** The sandbox plus approval levels answer it; that step is done
right.

**The problem is that it bets on a very small ecosystem.** DSH's user base is limited, and 0 forks
means no one is even copying it to learn from. Unless DSH takes off, this plugin is the right
answer at the wrong venue.

## What to watch next

① Whether forks start to grow — 0 forks means nobody is even copying it
② Whether a second consumption path appears (e.g. Claude Code users adopting the pattern) — proof
the value escaped the DSH bubble
③ Commit frequency in two months — individual projects most often die of post-launch silence

## What you can take from it

**Product logic**: for the governance layer of a multi-agent workflow, copy its three-level
abstraction — one-off dispatch (prompt) → named workflow (capsule) → resumable/auditable
(disk-persisted run + snapshot). "Resumability" is the line that separates a workflow from a
script, and most people stop at level two.

**Positioning language**: none. The README is engineering documentation.

**Pricing structure**: none. Not disclosed.

## Verdict

**Write it down, no rush.** The design has demonstration value, but it bets on a tiny ecosystem,
and 49 stars / 0 forks says this is still one author's engineering statement. Recheck against the
three points above in three months.
