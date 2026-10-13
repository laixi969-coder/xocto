---
slug: self-compacting-language-model-agents
name: Self-Compacting Language Model Agents
builder: ''
category: ''
summary_zh: 2026 年 10 月 12 日，一项研究提出 SELFCOMPACT 推理时脚手架，让模型自行决定何时以及如何压缩累积的思维链与工具调用轨迹，替代按固定 token 阈值触发的压缩方式。既有固定间隔压缩不关注轨迹结构，可能在推导或检索中途丢弃部分结果。该变化针对长轨迹代理的上下文窗口溢出与陈旧内容锚定问题，意味着代理类
  AI 应用在长任务中的上下文管理与交付稳定性可能出现改进，但材料仅描述方法本身，未给出采用或成本数据。
inspiration: ''
summary_en: On 12 October 2026, a study proposed SELFCOMPACT, an inference-time scaffold that lets the
  model itself decide when and how to compact accumulated chains of thought and tool-call traces, replacing
  compaction triggered at a fixed token threshold. Existing fixed-interval compaction ignores trajectory
  structure and risks discarding partial results mid-derivation or mid-search. The change targets context-window
  overflow and stale-content anchoring in long agent traces, implying possible improvements in context
  management and delivery reliability for long-horizon agentic AI applications, though the material describes
  only the method and provides no adoption or cost data.
inspiration_en: ''
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: false
url: https://machinelearning.apple.com/research/self-compacting-language-agents
canonical_url: https://machinelearning.apple.com/research/self-compacting-language-agents
summary: 'Long agent traces composed of chains of thought and tool calls accumulate stale content that
  anchor subsequent generations, and eventually outgrow the context window. Existing scaffolds mitigate
  it with fixed-interval compaction triggered at a token threshold. Such triggers pay no heed to trajectory
  structure, risking discard of partial results mid-derivation or mid-search. We propose SELFCOMPACT,
  a scaffold that allows the model itself to decide when and how to compact. Specifically, it pairs two
  inference-time elements: (i) a compaction tool the model invokes to summarize the accumulated…'
first_seen: '2026-10-13T03:04:22Z'
last_seen: '2026-10-13T03:04:22Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://machinelearning.apple.com/research/self-compacting-language-agents
  seen_at: '2026-10-13T03:04:22Z'
  metrics: {}
  kind: news
---

# Self-Compacting Language Model Agents

Long agent traces composed of chains of thought and tool calls accumulate stale content that anchor subsequent generations, and eventually outgrow the context window. Existing scaffolds mitigate it with fixed-interval compaction triggered at a token threshold. Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. We propose SELFCOMPACT, a scaffold that allows the model itself to decide when and how to compact. Specifically, it pairs two inference-time elements: (i) a compaction tool the model invokes to summarize the accumulated…

## 笔记


