---
slug: godmode
name: godmode
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

Engineering behavior for coding agents that already know how to code: a composable catalog of
Agent Skills that makes agents design before editing, test before claiming, review independently,
and verify with fresh evidence.

## Who built it

thiientv, an individual project. Repository created around 2026-08-12, 12 commits, initial version
plus supporting tooling in two days.

_Read: packaging software-engineering practice (TDD, review, releases, incident response) as
skills isn't a new idea, but the completion here — 14 core workflow skills plus 19 engineering
capabilities, a behavior-eval harness, and a repository gate — says the author is polishing it as
a product, not posting it as a note._

## What it actually does

- **Composable skill catalog** → no one giant prompt; discoverable, composable skill packages:
  solution-design, implementation-planning, TDD, root-cause-debugging, code-review and more
- **14 core workflow skills** → from using-godmode and plan-execution to
  dispatching-parallel-agents, subagent-driven-development, using-git-worktrees
- **19 engineering capabilities** → frontend-design, api-and-interface-design, database-design,
  security-and-hardening, release-engineering, incident-response, agent-evaluation and more
- **Deterministic helpers** → not just Markdown prompts; repeated error-prone work carries
  scripts: design_system.py, extract_design_system.py, audit_ui.py
- **Multiple clients** → standard Agent Skills layout; usable with Claude Code (plugin) and Codex
  (.codex-plugin + marketplace)
- **Behavior-eval harness** → runs behavior evals over core workflow cases
- **Repository gate** → validates frontmatter, local links, manifest shape, security scans;
  pre-1.0 but with a complete engineering process

**What it deliberately does not do**: no proprietary orchestration runtime — it stays a portable
catalog; no claiming compatibility with clients it hasn't actually checked (the README is
explicit).

## What old behavior it replaces

Without it, a coding agent's default is to start writing code immediately: authentication, tests,
security and integration get pushed to the end, and it wraps up with a plausible-looking result.
Humans catch these by manual review — but as agents multiply and tasks lengthen, review quality
collapses.

godmode replaces the old practice of "typing engineering discipline into the conversation" —
re-demanding every time that the agent write tests first, design first. It turns discipline from
an ad-hoc chat agreement into a reusable skill asset. It doesn't replace the human; it replaces
"the human having to re-teach every time."

## Business model

**Not disclosed.** MIT open-source, no pricing page, no hosted service.

_Read: a skill catalog is hard to monetize directly, but like dsh_workflow it bets that
standardized Agent Skills become the public foundation of agent engineering. If that foundation
forms, early catalog authors have first-mover advantage._

## Hard numbers

- **85 stars, 84 forks, 0 open issues.** Repository created around 2026-08-12, 12 commits
- **Forks nearly equal to stars (84/85)** — an abnormal ratio that usually means
  mirroring/copying rather than organic adoption
- 14 core workflow skills + 19 engineering capabilities
- The project page (thiientv.github.io/godmode) currently 404s; GitHub Pages not enabled
- Users and tested client compatibility: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A solo systematization of engineering practice; the author is clearly a true believer — but no record of team/real-world validation |
| Product insight | "Agents can code, they can't engineer" is an accurate observation, and the literal skill naming is right |
| Execution quality | Repository gate, behavior evals, compatibility docs — a more complete engineering process than most 12-commit projects |
| Timing | Agent Skills are becoming a standard format; an early high-quality catalog has positioning value; but the format war is undecided |

## The call

**A serious attempt to package two decades of software-engineering discipline into skills agents
can consume, and the naming principle is the part worth stealing.**

"Agent claims are not evidence" and "literal responsibility names over borrowed vocabulary" — both
map directly to the two real sources of engineering incidents: agents' optimistic false claims,
and vocabulary drift across projects. The standard death mode of a skill catalog is "nice-sounding
names that never reach concrete actions," and deterministic scripts plus reference files are the
plug for that.

**The transferable rule: name agent skills and tools by responsibility, not by brand.** Literal,
task-oriented names (root-cause-debugging, not smart-debug) align an agent's routing decisions
with human expectations and avoid being held hostage by one client ecosystem's vocabulary.

**The risk is that it hasn't proven who it speaks for.** 84 forks out of 85 stars says propagation
is by copying, not endorsement. Pre-1.0, no public field record, self-run evals — "production-grade"
is currently a self-claim.

## What to watch next

① Whether the fork/star ratio returns to normal (forks well below stars) — 84/85 says copying,
not approval
② Whether public "ran godmode on a real repo" cases or eval results appear — "production-grade"
needs production evidence
③ Whether skills get distributed through Claude Code/Codex official skill marketplaces — decides
whether it captures the format dividend

## What you can take from it

**Product logic**: when adding an "engineering behavior layer" to any agent product, copy the two
design principles — "agent claims are not evidence" (require fresh evidence for done) and
"responsibility names over aliases" (literal names prevent drift). For anyone building
agent-workflow products, these two principles are free correctness.

**Positioning language**: "Your coding agent already knows how to code. Godmode teaches it how to
engineer." — a model one-liner; keep the structure (existing capability + new capability = one
line).

**Pricing structure**: none. Not disclosed.

## Verdict

**Ideas present, unvalidated.** Disciplined engineering skills are the right direction and the
repo quality exceeds what the star count suggests, but the abnormal fork ratio, the absence of
field records, and pre-1.0 status all say "production-grade" is still a self-claim. Note it; track
field evidence and official marketplace distribution.
