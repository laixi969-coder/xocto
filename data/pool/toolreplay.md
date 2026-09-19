---
slug: toolreplay
name: ToolReplay
builder: Matthew0822
category: AI + 开发
summary_zh: 当团队把 AI agent 接进内部系统后，工程师或合规人员需要复盘某次任务到底调用了哪些工具、参数是什么、有没有越权。ToolReplay 接收 agent 的工具调用记录，做哈希链封存、确定性重放和越权范围检查，最终给出一份可复核的调用轨迹与越权提示，结论仍需人工确认。具体接入方式与交付形态仍待核验。
inspiration: 趋势：agent 开始替人执行写操作，事后追责和越权检查会像日志审计一样变成必选项。切入：从受监管行业里已经上线 agent 的团队入手，先做“出事之后能还原现场”的取证环节，而不是做通用
  agent 平台；可考虑按审计次数或按合规报告收费，价格未披露。
summary_en: Once teams wire AI agents into internal systems, engineers or compliance staff need to reconstruct
  which tools a task called, with what arguments, and whether it exceeded its scope. ToolReplay takes
  agent tool-call transcripts, seals them in a hash chain, replays them deterministically and flags scope
  overreach, returning a reviewable trace plus overreach warnings that a human still has to confirm. Integration
  and delivery format remain unverified.
inspiration_en: 'Trend: as agents start performing write actions, after-the-fact accountability and scope
  checks become as mandatory as log auditing. Entry point: start with teams in regulated industries that
  already run agents, and own the forensic step of reconstructing what happened rather than building a
  general agent platform; per-audit or per-compliance-report pricing is plausible but undisclosed.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
- 金融与保险
- 专业服务
industries_en:
- Software and IT services
- Finance and insurance
- Professional services
jobs:
- AI 平台工程师
- 合规与风控人员
- 安全审计员
jobs_en:
- AI platform engineer
- Compliance and risk officer
- Security auditor
regions: []
regions_en: []
open_source: true
url: http://quartzjer.github.io/pennybank/
canonical_url: https://quartzjer.github.io/pennybank
summary: 'Audit AI agent tool-call transcripts: hash-chain sealing, deterministic replay, and scope overreach
  checks. Dependency-free Python CLI.'
first_seen: '2026-09-14T10:11:00Z'
last_seen: '2026-09-19T00:21:19Z'
status: watching
sources:
- github
sightings:
- source: github
  url: http://quartzjer.github.io/pennybank/
  seen_at: '2026-09-19T00:21:19Z'
  metrics:
    stars: 180
    forks: 21
    open_issues: 1
  kind: product
---

# ToolReplay

Audit AI agent tool-call transcripts: hash-chain sealing, deterministic replay, and scope overreach checks. Dependency-free Python CLI.

## 笔记


