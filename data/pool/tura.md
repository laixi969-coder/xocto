---
slug: tura
name: tura
builder: turaainet
category: 基础层
summary_zh: 面向构建 MCP 工具调用 agent 的开发者：通过减少模型与工具之间的往返轮次来压缩单次任务的调用开销，用户拿到的是更少的调用次数而不是新的 agent 框架。75% 这一降幅来自项目自述，具体在什么任务上测得、如何复现仍待核验。
inspiration: 趋势是 agent 的成本结构从模型单价转向调用轮次，谁能压缩往返谁就掌握议价空间。切入可以放在为特定行业的 agent（保险理赔、货代订舱、财税对账）做调用编排与轮次压缩，卖的是可核对的单任务成本下降；但该项目的收费方式与买方尚无公开材料。
summary_en: 'For developers building agents that call MCP tools: it cuts the number of round-trips between
  model and tools to compress per-task call overhead, delivering fewer calls rather than a new agent framework.
  The 75% reduction is the project''s own claim; on which tasks it was measured and how to reproduce it
  still need verification.'
inspiration_en: The trend is that agent cost structure is shifting from model unit price to call rounds,
  and whoever compresses round-trips holds pricing power. The entry point is call orchestration and round-trip
  compression for industry-specific agents (insurance claims, freight booking, tax reconciliation), selling
  a checkable drop in per-task cost; there is no public material yet on how this project charges or who
  buys it.
priority_review: false
project_type: open_source
industries:
- 软件开发
- 企业软件
industries_en:
- Software Development
- Enterprise Software
jobs:
- 开发者在构建调用 MCP 工具的 agent 时，需要减少模型与工具之间的往返次数以控制单次任务的调用成本
- AI 应用团队在把 agent 接入生产流程时，需要压缩多轮工具调用的开销并保持任务完成度
jobs_en:
- Developers building agents that call MCP tools need to cut round-trips between model and tools to control
  per-task call cost
- AI application teams putting agents into production need to compress the overhead of multi-turn tool
  calls while keeping task completion
regions: []
regions_en: []
open_source: true
url: https://github.com/Tura-AI/tura
canonical_url: https://github.com/Tura-AI/tura
summary: Cut LLM turns in MCP interactions by 75%+
first_seen: '2026-08-11T20:39:32Z'
last_seen: '2026-09-10T05:14:03Z'
status: watching
sources:
- hackernews
- newssearch
sightings:
- source: hackernews
  url: https://github.com/Tura-AI/tura
  seen_at: '2026-08-13T03:25:27Z'
  metrics:
    points: 11
    comments: 0
  kind: product
- source: newssearch
  url: https://news.google.com/rss/articles/CBMi6gFBVV95cUxNaDBjVGNmWjNhWVBDeHJ3VDY5aWhFd1ZYUERWcWt2MUE1U0RfT3Fvb1BrRkR2RkVFejFhYWVrNmFkRlE3RzVHbWNIVzdXV3Z0V0VkTS02eF84RFhFUGgzbUZtSG1GdlQ1THNwOXRaTnAzeGpBOFZUb0pDZmttU201aVNYMDdWaDBieEk2SUU0MmtGeHZTTlZJcmY1cm1jZFk1aGlhWXNvR2xrNU1FY3NNREVWUnZ6SHFGRHlad05PaTRkTnlBWUFMQW9uQmIydlo2SjRVcklXZFFfQXFHQWthdU5WZlRSMmdvNUE?oc=5
  seen_at: '2026-09-10T05:14:03Z'
  metrics: {}
  kind: news
---

# tura

Cut LLM turns in MCP interactions by 75%+

## 笔记


