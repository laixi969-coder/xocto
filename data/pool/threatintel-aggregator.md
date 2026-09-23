---
slug: threatintel-aggregator
name: ThreatIntel-Aggregator
builder: Ethan-Andrews
category: AI + 开发
summary_zh: 安全运营或威胁情报人员每天要面对多个外部情报源，需要把零散 IOC 和报告整理成可用的检测规则。该自托管平台把情报源聚合起来，由 AI 对条目做初步分诊，再映射到 MITRE ATT&CK
  并生成可对接 Azure Sentinel 的检测内容；最终交付是分诊后的情报条目与检测工程产物，仍需分析师确认。具体分诊准确率与交付流程仍待核验。
inspiration: 趋势：威胁情报的“收集—分诊—落成检测规则”链条正被拆成可自托管的开源组件，模型只承担分诊这一环，价值落在与 SIEM 的对接上。切入：面向没有预算买商业 TIP 的中小安全团队或托管安全服务商，从“把免费情报源变成能直接进
  Sentinel 的检测规则”这一交付环节进入，按托管或规则包收费，而非按席位卖工具。
summary_en: Security operations and threat intelligence staff face many external feeds daily and must
  turn scattered IOCs and reports into usable detections. This self-hosted platform aggregates feeds,
  uses AI to triage items, maps them to MITRE ATT&CK and produces detection content that plugs into Azure
  Sentinel; the deliverable is triaged intelligence plus detection engineering output, still confirmed
  by an analyst. Triage accuracy and the exact delivery flow remain unverified.
inspiration_en: 'Trend: the collect-triage-turn-into-detections chain in threat intelligence is being
  split into self-hostable open-source parts, with the model doing only triage and the value sitting in
  SIEM integration. Entry: target small security teams or MSSPs that cannot buy a commercial TIP, starting
  from the step that converts free feeds into Sentinel-ready detections, and charge for managed output
  or rule packs rather than seats.'
priority_review: false
project_type: open_source
industries:
- 信息安全
- 企业 IT 服务
industries_en:
- Information security
- Enterprise IT services
jobs:
- 安全运营中心分析师
- 威胁情报分析师
jobs_en:
- Security operations center analyst
- Threat intelligence analyst
regions: []
regions_en: []
open_source: true
url: https://github.com/Ethan-Andrews/ThreatIntel-Aggregator
canonical_url: https://github.com/Ethan-Andrews/ThreatIntel-Aggregator
summary: Self-hosted threat intelligence platform — feed aggregation, AI triage, MITRE ATT&CK coverage,
  and Sentinel-integrated detection engineering. Runs standalone or fully Azure-integrated.
first_seen: '2026-09-14T06:07:22Z'
last_seen: '2026-09-23T00:34:19Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/Ethan-Andrews/ThreatIntel-Aggregator
  seen_at: '2026-09-23T00:34:19Z'
  metrics:
    stars: 51
    forks: 7
    open_issues: 0
  kind: product
---

# ThreatIntel-Aggregator

Self-hosted threat intelligence platform — feed aggregation, AI triage, MITRE ATT&CK coverage, and Sentinel-integrated detection engineering. Runs standalone or fully Azure-integrated.

## 笔记


