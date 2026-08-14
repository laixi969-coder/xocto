---
slug: juror
name: juror
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An open-source PR review tool that runs inside your own GitHub Actions: several frontier models each review the same PR independently, only findings they agree on get merged and reported, and every review prints a cost receipt. Positioning: "cheaper and better Greptile alternative."

## Who built it

The Juror-AI organization (primary contributor Jay Derinbogaz, GitHub cderinbogaz), MIT license, a TypeScript GitHub Action. Commit history shows heavy Claude co-authorship — typical AI-assisted, high-intensity development. Team size is not disclosed.

_Read: choosing the "runs in your own Actions + bring your own API key + prints a receipt" positioning means the author has been burned by the bills and data-sovereignty problems of hosted review services like Greptile._

## What it actually does

- **Parallel multi-model review** → supports claude-code, codex, opencode, grok-build, kimi-code, codewhale (DeepSeek's native runtime), and more; each model reviews independently through its native agent harness
- **Consensus dedup** → when several models describe the same defect it merges into one finding; default high-recall mode shows everything, and a consensus mode filters by agreement
- **Cost receipt** → every review prints a reported-vs-estimated bill, distinguishing cached tokens from long-context price cliffs
- **Zero infrastructure** → no app install, no account, no semantic index; the harnesses ship their own repo search
- **Security isolation** → only the publish step holds GITHUB_TOKEN; Codex reviews run on a kernel-enforced split filesystem so model processes never touch credentials
- **Tamper resistance** → the review ignores AGENTS.md files introduced by the PR itself, so submitters cannot rewrite the review rules

## What old behavior it replaces

Two behaviors at once.

First, **hosted AI code-review SaaS such as Greptile or CodeRabbit**: install the app, pay per repo or per seat, hand your code to a third-party index, wait in the cloud queue. Replaced by a free workflow on your own GitHub Actions whose only cost is your own LLM API usage.

Second, **the mechanical part of human code review**: common bug classes and missed edge cases that used to need a senior engineer's eyeballs now get scanned by several models first, and a human only looks at the consensus findings and adjudicates disagreements.

_Read: for open-source projects and small teams, "run in my CI with my keys" is dramatically cheaper than subscribing to SaaS. This is the standard wedge for open-source alternatives — not better features, but a completely different cost structure._

## Business model

**Not disclosed; currently revenue-free open source.** Distributed via npx juror-ai, you bring any key (OpenAI, Fireworks, Anthropic, xAI, etc.).

_Read: open-source alternatives usually keep the money in a hosted tier — removing the pain of configuring Actions and keys is a service people pay for. No hosting is visible yet, but it is the most likely monetization path._

## Hard numbers

- 82 stars / 9 forks, MIT, repo created 2026-08-06 — about a week old
- 53 commits, current line v1.4.x, latest commit 2026-08-14, active development
- HN: 6 points, 1 comment
- Internal benchmark (author-reported): on one bundled PR seed, Juror Fast found 4/6 (66.7%) P0–P2 defects at 100% precision; Greptile found 1/6 (16.7%) at 50%. The author explicitly notes this is a single PR with manual adjudication — not a statistically sufficient benchmark
- Team size, real user count: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author was clearly burned by hosted review costs and data issues; real pain, but the organization's background is unknown |
| Product insight | "Multi-model consensus + cost receipt" is a clever differentiator: buy precision with redundancy, buy trust with transparency |
| Execution quality | The obsession with token accounting (long-context price cliffs, cached tokens) is written by someone who actually paid the bills |
| Timing | Code review is one of the first dev workflows agents take over, and Greptile already proved demand |

## The call

**"Cheaper" is the real product insight.** It does not compete with Greptile on feature breadth; it competes on cost structure — your keys, your CI, your code never leaves the repo. For this category's users, that is close to decisive.

**The transferable pattern: hedge single-model false positives with multi-model redundancy.** One model reviewing code both misses and hallucinates; several independent models that must agree produce far fewer false positives. This majority-vote logic transfers to any generation or review task where precision matters.

**Two risks.** First, the benchmark is weak: single PR, manual adjudication; 66.7% vs 16.7% reads as a story, not evidence. Second, the category ceiling: the better the models review, the less humans need to look, while the token cost of running several models is real — it only wins when the human time saved clearly exceeds the token spend.

## What to watch next

① Whether stars break 300 in a month — whether "code review as a GitHub Action" gets adopted
② Whether anyone publicly shows a real defect it caught (more credible than any self-reported benchmark)
③ Whether a hosted tier or pricing appears — an open-source alternative starting to charge is demand verified

## What you can take from it

**Positioning logic**: when your product targets a SaaS with proven demand, do not compare features — compare cost structure. Making your product "your keys + your infrastructure" rewrites the opponent's cost equation, which beats a feature table.

**Product detail**: print a cost receipt on every AI call; make "what did this cost" part of the product. Cost transparency is itself a trust mechanism, especially when "saves you money" is your pitch.

**Security design**: review rules can be gamed (a PR rewriting AGENTS.md). Ignoring "rules the reviewed object brings in itself" transfers to any product where AI adjudicates — the adjudication basis must come from outside the party being judged.

## Verdict

**Worth watching, with the benchmark discounted.** The positioning holds, the engineering is solid, and the cost story is concrete; the only "score" is a weak self-tested benchmark. Wait for public cases and the stars curve — those two numbers tell you whether it is really the person doing Greptile's job for free.

