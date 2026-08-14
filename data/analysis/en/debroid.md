---
slug: debroid
name: debroid
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A headless Android debugger for AI coding agents: the agent runs commands in the terminal and,
through the JDWP (Java Debug Wire Protocol), sets breakpoints, traps exceptions, steps through
code, inspects and mutates variables, and watches fields on a live Android app — no GUI, all
strict machine-parseable JSON.

## Who built it

Shreyas Patil (GitHub `PatilShreyas`), an experienced Android/Kotlin developer well known in
the Kotlin community for a long line of Android infrastructure open-source projects.
Apache-2.0, Kotlin/JVM via the Java Debug Interface, with GitHub Actions CI.

_Read: only someone who really understands JVM debug protocols could write this — it exposes
the same JDWP channel humans use in Android Studio as a machine-readable CLI, instead of
building screenshot recognition or instrumentation. That is the right way to use your old
domain knowledge: reuse the most mature protocol in the field rather than inventing a wheel._

## What it actually does

- **Breakpoints** → line breakpoints on any class, auto-deferred if the class isn't loaded yet
- **Exception traps** → globally catch caught or uncaught exceptions (uncaught-only by default)
- **Watchpoints** → live monitoring of field access and modification
- **Deep inspection** → recursively inspect deep object memory, locals, and call frames, with
  built-in cycle guards
- **Live mutation** → `set-var` changes memory on a paused thread; `eval` evaluates Java
  expressions directly in the target VM
- **Stepping** → Step Over / Into / Out / Resume
- **Coroutine-aware** → extracts shallow locals from Kotlin Continuation frames (coroutine
  debugging is a real pain point, handled with unusual care)
- **Open-box for six agent harnesses** → one-command skill installs for Claude Code, Codex,
  Grok Build, OpenCode, Cursor, and Antigravity

**The most notable architecture choice**: the CLI is stateless and a daemon persists — the
debug connection and breakpoint state survive across agent invocations because the background
daemon holds them.

**What it deliberately does not do**: no GUI, no instrumentation hooks, no test reports. And the
security note is blunt: the daemon listens on localhost without authentication and exposes live
JVM manipulation — run it only on machines where every local user is trusted.

## What old behavior it replaces

Debugging an Android bug with an AI agent used to be blind guesswork: writing code works, but
runtime debugging doesn't — the agent can't open Android Studio, click through the UI, set a
breakpoint, inspect memory, or pause execution. So agents debugged from logcat and guessed,
each wrong guess costing a rebuild cycle.

Debroid replaces the **"human doing runtime debugging in Android Studio"** step: every GUI
action is translated into deterministic JSON commands, letting the agent itself go
"hypothesize a bug → launch the app → land on the exact failing line → read the device's live
state → evaluate the fix."

## Business model

**None.** Apache-2.0, free, no hosted service, no pricing. The author presumably has a day job.

_Read: the classic personal open-source-tool-for-reputation pattern, with no near-term
commercial intent. But it validates a category — "let agents operate real devices and real
runtimes" — which will probably be commercialized later through agent-native workflows
(harnesses, IDEs, cloud debug services) rather than through this CLI itself._

## Hard numbers

- **162 stars / 7 forks** (2026-08-12, per pool data)
- Created 2026-08-02; 90 commits to v0.1.0 in nine days — very high early development density
- Apache-2.0, Kotlin/JVM, ~22 commands
- Users, enterprise adoption, funding: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Seasoned Android/Kotlin developer who knows the JVM debug stack cold — maximal fit |
| Product insight | Saw the gap ("agents write mobile code but can't debug it") and chose to reuse JDWP instead of inventing an approach |
| Execution quality | 90 commits in 9 days, strict JSON contract with schemas, coroutine awareness, skill installs for six harnesses — not the shape of a one-week project |
| Timing | Ahead of the demand curve — agents are still mostly doing web/desktop; mobile debugging demand is just emerging, and so is the paying side |

## The call

**Top-tier execution for a project this size, but the category's commercial timing is early.**

The smartest decision is **reusing JDWP instead of inventing**. The debug protocol is two
decades of deterministic engineering in the JVM world; exposing it as JSON CLI hands every
capability a human had in an IDE to the agent. Wrapping a mature protocol beats screenshot
recognition or custom instrumentation on every axis — lighter, more reliable, cheaper.

**The "persistent daemon + stateless CLI" architecture is worth stealing too**: the classic
failure of agent tools is that each invocation is a fresh process and all state dies. A
persistent daemon keeps the debug session alive across calls — the structure every agent-tool
interface should copy.

**Two realities**: platform lock-in (Android only; iOS is another protocol stack and won't be
covered by accident), and demand timing — most teams haven't even gotten agents to write mobile
code reliably yet, let alone debug it. Great tool, waiting for its queue.

## What to watch next

① Whether stars clear 1,000 in three months — does the week-one spike become sustained adoption
② Whether anyone wires debroid into a real CI/emulator flow and says so publicly (blog, issue,
  demo) — real use, or just enthusiasm
③ Whether it expands to iOS/web debugging or ships a managed daemon — single-platform is the
  hard ceiling, and that is the breaking point

## What you can take from it

**Product logic**: to give an agent "hands," reach first for the field's most mature
deterministic protocol (debug protocol, scripting protocol, CLI) and wrap it as JSON — reusing
the protocol saves a decade of trial and error over custom instrumentation or visual approaches.

**Architecture**: "persistent daemon holds state + stateless CLI" is the standard shape for
agent tools; letting each agent call pick up the previous context is what decides whether a
tool survives long-term agent use.

**Distribution**: embedding SKILL.md in the binary and installing into six harnesses with one
command — "how an agent learns to use your tool" is a distribution problem, not a docs problem,
and this solution is directly copyable.

## Verdict

**Unproven (execution worth watching).** Right author, right approach, high completeness — but
162 stars, a single platform, no monetization, and demand ahead of its market all point to
"wait." File it as the benchmark sample for the "let agents operate real runtimes" category and
revisit against the three checks above in three months.
