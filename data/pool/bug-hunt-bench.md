---
slug: bug-hunt-bench
name: bug-hunt-bench
builder: phuryn
category: AI + 开发
summary_zh: 开发团队在挑选编码模型时，面对各家自报的基准成绩，打开 Bug Hunt Bench 让它把两个生产仓库里的 105 个真实缺陷交给各模型在自身 CLI 中定位并修复，盲评后给出排行榜和逐条记录，最终得到一份可核对的横向对比；评测集是否持续更新、是否覆盖私有代码库仍待核验。
inspiration: 趋势：编码模型的宣传分数与真实仓库里的缺陷修复能力之间出现落差，第三方盲评正在成为选型环节的独立供给。切入：可从需要为团队采购编码模型的技术负责人入手，用真实仓库缺陷而非合成题目做评测，卖点是对结果负责的对比报告，而不是再训练一个模型。
summary_en: When choosing a coding model, a development team faces vendors' self-reported benchmark scores;
  Bug Hunt Bench takes 105 real bugs from two production repositories, has each model locate and fix them
  in its own CLI, grades blind, and returns a leaderboard with per-case receipts, giving a checkable side-by-side
  comparison; whether the set keeps updating and covers private codebases still requires verification.
inspiration_en: 'Trend: a gap has opened between coding models'' advertised scores and their ability to
  fix bugs in real repositories, making third-party blind evaluation a separate supply for model selection.
  Entry point: start with technical leads buying coding models for a team, evaluating with real repository
  bugs rather than synthetic tasks, and selling a comparison report that stands behind its results instead
  of training another model.'
priority_review: false
project_type: open_source
industries:
- 软件与信息技术服务
industries_en:
- Software and IT services
jobs:
- 软件开发者
- 技术选型与采购人员
jobs_en:
- Software developers
- Technical evaluation and procurement staff
regions: []
regions_en: []
open_source: true
url: https://bughunt.productcompass.pm
canonical_url: https://bughunt.productcompass.pm
summary: 'Bug Hunt Bench: 105 real bugs in two production repos, frontier coding models (GPT-6, Claude,
  Grok, Gemini, DeepSeek...) find and fix them in their own CLI, graded blind. Live leaderboard + every
  receipt.'
first_seen: '2026-08-25T11:43:42Z'
last_seen: '2026-09-12T00:18:44Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://bughunt.productcompass.pm
  seen_at: '2026-09-12T00:18:44Z'
  metrics:
    stars: 47
    forks: 2
    open_issues: 0
  kind: product
---

# bug-hunt-bench

Bug Hunt Bench: 105 real bugs in two production repos, frontier coding models (GPT-6, Claude, Grok, Gemini, DeepSeek...) find and fix them in their own CLI, graded blind. Live leaderboard + every receipt.

## 笔记


