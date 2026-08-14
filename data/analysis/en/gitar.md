---
slug: gitar
name: Gitar
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

AI code review where the review is not the endpoint: it finds the problem, applies the fix, runs CI to validate, and only commits when the pipeline is green. "From telling you there's a problem to having already fixed it" is the line separating it from every comment-only review tool.

## Who built it

A startup that launched in April 2026 and was acquired in May 2026 by Sonar (the company behind SonarQube), now living at sonarsource.com/products/gitar as the AI-review layer of Sonar's "multilayered verification platform." CTO is Gautam Korlam, also a principal engineer at Sonar; co-founder Zac Zuo (the name in the pool's builder field) launched it on PH as co-hunter.

_Read: acquired one month after launch — Sonar bought the capability, not the customer base. A company with two decades in code quality needed a review layer that can absorb AI-agent-produced code, and Gitar is what it picked. The acquisition is net positive for Gitar: Sonar's 7 million developers and 22,000+ customers is distribution Gitar could not have built itself in three years._

## What it actually does

- **Reviews PRs and actually fixes them** → reads the diff, CI logs, repo rules, and agent instruction files; generates fixes, pushes them to the branch, and runs CI to verify the fix did not break anything else
- **Fixes CI failures** → analyzes build/test/lint failures, finds root causes, and keeps fixing until green; also deduplicates repeated build failures and detects/retries flaky tests
- **Natural-language rules** → define policies and automations in plain English — "block any PR that adds a TODO without a linked ticket," "assign security findings to the security team" — no scripts or YAML
- **Migration automation** → six migration categories, claiming roughly 40% automation (service consolidation) up to 90% (API deprecations)
- **Agent-agnostic** → reviews whatever wrote the code, Claude Code, Cursor, Codex, Devin, or Copilot
- **Static analysis guardrail** → a static-analysis layer over syntax, dependency graphs, and type information constrains what the LLM is allowed to suggest, cutting down confident-but-wrong suggestions on unfamiliar frameworks

**Its own positioning**: "Most people think this space is saturated. It is, but in the low end. High-end code reviews is blue ocean."

## What old behavior it replaces

Code review used to be two steps, both flawed:

**Human review** — senior engineers reading PRs line by line. Reliable, but slow: waiting on reviews across time zones is the norm, and AI-generated code now outpaces what humans can review — "PR pile-ups, CI failures, and senior engineers are the last friction points between AI speed and shipped product," in Gitar's own words.

**Comment-based AI reviewers (CodeRabbit, Greptile, etc.)** — they find problems, post comments, and suggest fixes, but stop at the suggestion: someone still has to accept each fix and manually confirm the build is not broken. Gitar's critique is concrete: "The review doesn't end with a finding and another comment for devs to deal with. Gitar stays with the change through the fix and back through CI."

Gitar replaces the second half after the finding — from finding to fix to validation to commit, fully automated. It upgrades the review tool from "sentry that points at problems" to "worker that removes them." Its argument: for teams whose constraint is not finding problems but keeping up with fixing them, comment-only tools deliver nothing.

## Business model

SaaS subscription:

- **Core $20/user/month**: basic review + fixes
- **Pro $40/user/month**: the full capability — automatic fixes plus CI validation
- **Enterprise custom**: migration automation is effectively Enterprise-only
- 14-day trial, free for OSI open-source public repos, 50-user ceiling on self-serve
- GitHub and GitLab only (including self-hosted); no Bitbucket, no Azure DevOps

_Read: priced a tier above CodeRabbit (which has a free tier), betting "can fix" commands a premium. The bet has logic — from "here's a problem" to "it's fixed" is a step change in value. But the 50-user ceiling pushes big teams to sales, and migration automation — the most impressive demo — sits behind Enterprise, hiding the best story until a sales call._

## Hard numbers

- Launched April 2026, **acquired by Sonar May 2026** (amount not disclosed)
- PH launch 2026-08-11: **107 upvotes, 2 comments, #12 of the day**
- Pricing $20 / $40 per user/month, 14-day trial
- Sonar platform base: 7 million developers, 22,000+ customers
- Migration automation claims: 6 categories, ~40%–90% automation potential (not independently verified)
- Review quality: **no third-party published benchmark** (four months old)
- ARR, customer count: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Founders absorbed into Sonar's core team after acquisition — an industry-veteran endorsement |
| Product insight | "The half after the finding is what's worth money" is an accurate judgment; CI-failure attribution and flaky-test retry are real differentiation |
| Execution quality | Static analysis constrains the LLM, zero-retention data handling, never touches secrets, no force-push. Disciplined engineering |
| Timing | Excellent. AI-generated code volume is exploding, review is a recognized bottleneck, and Sonar hands over distribution |

## The call

**"From telling you there's a problem to having fixed it" is indeed the step-change from sentry to worker — and its biggest advantage has already been proven by the acquisition.**

**The transferable rule: the ceiling of comment-based tools is the entry price of fix-based ones.** CodeRabbit-class tools stop at "pointing out the problem"; Gitar extends value to "the problem is gone." The felt difference is an order of magnitude — one is "someone gave me more work," the other is "the work is gone." Any diagnostics product that wants to raise prices should first figure out how to turn its diagnosis directly into action.

**Its real moat is not AI, it is deep CI attribution.** Pure-LLM reviewers are everywhere, but "deduplicating build failures, identifying flaky tests, separating code failures from infrastructure noise" is grubby work no comment-only competitor does. This explains why Sonar picked it — Sonar has the verification layer and lacks a review layer that acts on its own; Gitar fills exactly that half.

**Risks**: first, no third-party benchmark, so review quality is self-asserted (normal at four months); second, post-acquisition "product in transition" — it is being integrated into Sonar's platform, so positioning and packaging will shift and independent signals will get harder to read; third, "finds it, fixes it" requires teams to let AI touch branches directly, a much higher trust bar than "reads comments," which means a longer sales cycle.

## What to watch next

① After Sonar integration, whether Gitar is still purchasable standalone or folded entirely into SonarQube subscription
② Whether migration automation (the 40–90% claim) moves out of Enterprise and produces public customer cases
③ Whether a third-party benchmark or published fix-success-rate data appears in the next few months — "actually fixed it" needs hard numbers to sell

## What you can take from it

**Product logic**: for any diagnostics/detection product, the automation between "detected" and "fixed" is the room to raise prices. Gitar took the full step from "comment" to "fix + validate"; even a partial move — one-click apply-fix plus auto-validation — is a tier above pure suggestions.

**Positioning language**: its opener is directly stealable — "The review doesn't end with a finding and another comment." One sentence defines its difference from the entire old category. Describe the step in the old workflow users hate most, then say you stop there.

**Pricing structure**: lock the most lethal capability (migration automation) behind Enterprise, and let self-serve run on Core/Pro. But watch the 50-user ceiling — capping at 50 shoves live people into sales, which only works if enterprise conversion is high enough.

## Verdict

**Worth watching.** Precise positioning, the Sonar acquisition is hard validation, and deep CI attribution is real differentiation — but review quality has no third-party benchmark, and the product is in an integration transition that will thin independent signals. Watch migration automation opening up and third-party data.
