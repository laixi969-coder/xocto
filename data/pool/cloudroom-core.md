---
slug: cloudroom-core
name: cloudroom-core
builder: davidondrej
category: AI + 开发
summary_zh: 团队想让 Claude Code、Codex 这类编码代理在云端而不是某台笔记本上跑时，cloudroom-core 提供一个可自托管的 Rust 运行时来承载这些代理会话。它接收的是代理运行环境与任务，产出是云端可运行的会话环境；具体如何隔离、如何计费、是否支持多人协作，公开材料未说明，部署与交付细节仍待核验。
inspiration: 趋势是编码代理从个人玩具变成团队资产，随之出现的是“代理跑在哪、谁负责它的运行环境”这类基础设施问题。切入可以选受合规约束的行业，例如金融或医疗的研发团队，卖自托管加审计日志，而不是再做一个托管代理平台。
summary_en: When a team wants coding agents such as Claude Code or Codex to run in the cloud rather than
  on one laptop, cloudroom-core offers a self-hostable Rust runtime that hosts those agent sessions. It
  takes the agent runtime and task as input and produces a runnable cloud session environment; how isolation
  works, how it is priced, and whether multi-user collaboration is supported are not stated in the public
  material, so deployment and delivery details remain unverified.
inspiration_en: The trend is that coding agents are turning from a personal toy into a team asset, which
  raises infrastructure questions about where the agent runs and who owns its runtime. A wedge is compliance-constrained
  engineering teams in finance or healthcare, selling self-hosting plus audit logs rather than building
  yet another hosted agent platform.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 平台工程师
- 开发团队负责人
jobs_en:
- Platform engineers
- Engineering team leads
regions: []
regions_en: []
open_source: true
url: https://www.cloudroom.dev
canonical_url: https://cloudroom.dev
summary: Open-source, self-hostable Rust runtime that runs Claude Code, Codex, and Pi in the cloud.
first_seen: '2026-09-17T18:56:56Z'
last_seen: '2026-10-07T01:32:31Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://www.cloudroom.dev
  seen_at: '2026-10-07T01:32:31Z'
  metrics:
    stars: 259
    forks: 40
    open_issues: 0
  kind: product
---

# cloudroom-core

Open-source, self-hostable Rust runtime that runs Claude Code, Codex, and Pi in the cloud.

## 笔记


