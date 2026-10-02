---
slug: gutsy
name: Gutsy
builder: mrkn1
category: 基础层
summary_zh: 开发者或产品团队在需要让本地程序自动做判断（例如分流、选择下一步动作）时，把待决策的输入交给 Gutsy，由这个 0.8B 参数模型在 CPU 上直接推理并输出决策结果，无需 GPU
  或云端调用；具体输入格式与交付形态仍待核验。
inspiration: 趋势是决策类小模型开始脱离云端、往本地 CPU 走，成本结构从按 token 付费变成一次性部署。切入可看对延迟和成本敏感、又不愿把数据外发的场景，例如客服工单分流、设备端告警判定；但该模型的实际效果与集成方式尚未公开，先观察。
summary_en: When developers or product teams need a local program to make a judgement call (for example
  routing or picking the next action), they pass the input to Gutsy, a 0.8B-parameter model that reasons
  on CPU and returns a decision without GPU or cloud calls; the exact input format and delivery form still
  need verification.
inspiration_en: The trend is decision-oriented small models moving off the cloud onto local CPUs, turning
  per-token cost into a one-off deployment. A wedge could be latency- and cost-sensitive work that cannot
  send data out, such as ticket routing or on-device alert triage; the model's real quality and integration
  path are not yet public, so watch first.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/kouhxp/gutsy
canonical_url: https://github.com/kouhxp/gutsy
summary: a 0.8B Jev-compatible decision model that runs on your CPU
first_seen: '2026-10-01T15:44:42Z'
last_seen: '2026-10-02T01:41:51Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/kouhxp/gutsy
  seen_at: '2026-10-02T01:41:51Z'
  metrics:
    points: 8
    comments: 2
  kind: product
---

# Gutsy

a 0.8B Jev-compatible decision model that runs on your CPU

## 笔记


