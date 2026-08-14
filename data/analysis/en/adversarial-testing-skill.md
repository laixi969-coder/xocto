---
slug: adversarial-testing-skill
name: Adversarial-Testing-Skill
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

Two AIs spar over your product: one reads the source code, the other is kept blind — operating
only on a structured summary and the behavior of the API surface — and attacks. It turns any AI
coding assistant into a security red team.

## Who built it

Kieran Howard (GitHub: KieranHoward646), MIT license, a single-author project. The README is signed
"Built with anger at insecure software, respect for real red teams, and a lot of Markdown."

_Read: a single person building a security tool reads like a developer who was bitten by reality,
not a security-consultancy deck. But there is tension between "single maintainer" and the claim of
a "battle-tested framework."_

## What it actually does

- **Dual-agent blind-testing architecture** → a Developer AI reads the source and produces a
  structured summary; an Adversarial AI has zero knowledge of the source and attacks from the
  summary and interface behavior, like a real attacker. Four invocation modes: full pipeline /
  review the summary before testing / summary only / attack only
- **Four attack categories** → general software, 6 classes, 100+ payloads (boundaries, injection,
  permissions, concurrency, exceptions, business logic); LLM/AI, 8 classes, 50+ payloads (prompt
  injection, jailbreaks, system leaks, poisoning, agent attacks, multimodal); network protocols,
  30+; ML models, 20+
- **Enterprise-grade reporting** → SARIF (one-line CI integration into the GitHub Security Tab),
  JSON, Markdown, HTML, plus a CVSS-like four-dimension 0–10 severity score
- **Auto-fix** → outputs unified diff patches
- **Three-layer defense in depth** → Docker sandbox (OS-level isolation, read-only filesystem) →
  7 hard-coded approval rules (DROP/SYSTEM/PROD instantly BLOCK) → natural-language constraints as
  last resort
- **CI/CD out of the box** → GitHub Actions workflow triggered on PRs, results posted as PR
  comments, Critical findings auto-uploaded as SARIF
- **Platform adapters** → native on WorkBuddy (one command), dual sessions on Cursor, dual
  terminals on Claude Code, manual prompt copy for everything else

## What old behavior it replaces

Testing the security of an AI product used to mean two things. First, prompting the model to audit
itself — which the README correctly calls out: "Traditional testing tools can't test what they
can't parse." Second, hiring human pentest teams, billed by person-day, expensive and slow, and
whose craft is HTTP endpoints — not the new attack surface of natural language.

This compresses the human red-team workflow — recon, payloads, attack, report, fix suggestions —
into a two-agent pipeline whose marginal cost per run is near zero. It replaces person-day-billed
penetration testing and prompt-based self-audits: one is too expensive, the other too weak.

## Business model

**Not disclosed.** MIT open source, no hosted service, no pricing page, no mention of a commercial
edition anywhere in the README.

_Read: the README's intent is to make its report formats a de-facto standard — SARIF into the
Security Tab is an obvious "become the input to the toolchain" play. But there is currently zero
evidence anyone pays for it._

## Hard numbers

- **41 stars, 0 forks**, 8 commits, first spotted 2026-08-11
- 38 files: 5 theory guides, 10 executable templates, 8 attack payload libraries, 4 platform
  adapters, 18 attack categories, 7 hard-coded safety rules, 15+ real cases
- The README claims "prompt injection cost the world ~$2.3B in 2025" — that is the README's claim,
  not verified by this publication
- Team size and usage data: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A single-person security framework with a genuine red-team perspective (the blind-test design) fits; the "framework ambition versus solo maintenance" tension is obvious |
| Product insight | The standout is "the adversary must be blind" — review the summary before releasing the attack, so the tester is not led astray by the source. That is a real insight |
| Execution quality | 8 commits, 41 stars, 0 forks. The claimed CI/CD and three-layer defense need hands-on verification; this scale does not support "battle-tested" |
| Timing | AI-application security testing is a genuine vacuum, but the market does not exist yet — most teams have not even put agents into production |

## The call

**The design is right; the scale is suspicious. "The adversary must test blind against the source"
is real and I cannot fault it. But a repo with 8 commits and 0 forks calling itself battle-tested
deserves a discount.** For a security tool, "battle-tested" only counts if someone else did the
battling; saying it about yourself does not count.

It is not part of the DSH ecosystem — it depends on no particular harness and instead treats
WorkBuddy, Cursor, and Claude Code as hosts. So it is a standalone tool, not a plugin. The flip
side of standalone is that nothing in an ecosystem vouches for it, and the evidence that anyone
actually runs it is currently zero.

Its fate rests on two things: whether the author keeps maintaining it, and whether someone actually
runs it and publishes results.

## What to watch next

① Whether forks grow in three months — a security tool being forked means people actually run it;
stars can be bought, forks cannot
② Whether anyone other than the author publicly uses its report formats (SARIF into the GitHub
Security Tab)
③ Run its workflow against a real project and check whether Critical findings really auto-upload —
that verifies the "CI/CD out of the box" claim

## What you can take from it

**Product logic**: "the tester must test blind" transfers to any verification product — when the
verifier does not know the answer, the verification is credible. If you are building quality or
security acceptance for AI products, copy this known-writer/unknowing-executor split between two
agents; it is far more credible than a single agent auditing itself.

**Positioning language**: none. The README is technical; nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Unproven.** The mechanism contains something real; the scale does not. Read it as a security-
testing methodology, do not install it as a tool you can rely on. Verify against the three checks
in three months.
