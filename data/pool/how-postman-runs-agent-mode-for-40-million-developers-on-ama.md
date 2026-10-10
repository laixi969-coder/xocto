---
slug: how-postman-runs-agent-mode-for-40-million-developers-on-ama
name: Postman Agent Mode
builder: ''
category: AI + 开发
summary_zh: 已有 Postman 使用习惯的开发者，在调试接口、补文档或查找某个 API 用法时，可以直接用自然语言让 Agent Mode 在测试、文档、接口发现与实现之间操作，而不必逐层展开侧边栏和标签页找入口。候选材料只给出架构与集成说明，具体交付物与人工确认环节仍待核验。
inspiration: 趋势：成熟工具把 AI 接进已有界面时，难点从模型能力转到“让老产品对智能体可读”，上下文组织成了新的工程门槛。切入：可面向已有大量历史数据但界面复杂的垂直软件做智能体适配层，例如把老牌
  ERP 或医疗信息系统的操作路径改写成可被智能体调用的结构化读取，按接入的系统收费。
summary_en: Developers already using Postman can, while debugging an API, updating docs or looking up
  how an endpoint works, ask Agent Mode in natural language to act across testing, documentation, discovery
  and implementation instead of expanding sidebars and tabs to find each entry point. The candidate material
  only gives architecture and integration notes; concrete deliverables and human confirmation steps still
  need verification.
inspiration_en: 'Trend: when mature tools embed AI into existing interfaces, the hard part shifts from
  model capability to making an old product legible to an agent, with context organization as the new
  engineering barrier. Entry: build an agent adaptation layer for data-rich but complex vertical software,
  e.g. rewriting operation paths of legacy ERP or clinical systems into structured reads an agent can
  call, charged per connected system.'
priority_review: false
project_type: ai_transformation
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- API 测试与文档维护
jobs_en:
- API testing and documentation maintenance
regions:
- 全球
regions_en:
- Global
open_source: false
url: https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock/
canonical_url: https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock
summary: Building an AI agent for a demo and operating one for 40 million developers are different engineering
  problems. Postman set out to build Agent Mode , an AI-native way to work across API testing , documentation
  , discovery, and implementation. The team expected model quality and prompt design to be the hardest
  problems. The deeper challenges came from integrating an agent into a mature product with years of interface-driven
  assumptions, a wide surface area, and specialized concepts. In this post, Postman and AWS describe the
  architectural patterns that emerged while making a mature product legible to an AI agent. These patterns
  include controlling tool sprawl, exposing schema-based reads, and treating context rather than capability
  as the primary bottleneck. We also explain how Agent Mode uses Amazon Bedrock for model flexibility,
  geographically scoped cross-Region inference, model-dependent zero data retention, and multi-tier prompt
  caching. Together, these lessons can help teams move production agents beyond prototypes. Why Postman
  built Agent Mode Agent Mode is Postman’s portal for working with the product in an AI-native way across
  testing, documentation, discovery, and implementation. Postman has evolved over 11 years, and developers
  and users learned to locate information through the interface by expanding sidebars, checking tabs,
first_seen: '2026-10-10T01:46:28Z'
last_seen: '2026-10-10T01:46:28Z'
status: watching
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock/
  seen_at: '2026-10-10T01:46:28Z'
  metrics: {}
  kind: news
---

# Postman Agent Mode

Building an AI agent for a demo and operating one for 40 million developers are different engineering problems. Postman set out to build Agent Mode , an AI-native way to work across API testing , documentation , discovery, and implementation. The team expected model quality and prompt design to be the hardest problems. The deeper challenges came from integrating an agent into a mature product with years of interface-driven assumptions, a wide surface area, and specialized concepts. In this post, Postman and AWS describe the architectural patterns that emerged while making a mature product legible to an AI agent. These patterns include controlling tool sprawl, exposing schema-based reads, and treating context rather than capability as the primary bottleneck. We also explain how Agent Mode uses Amazon Bedrock for model flexibility, geographically scoped cross-Region inference, model-dependent zero data retention, and multi-tier prompt caching. Together, these lessons can help teams move production agents beyond prototypes. Why Postman built Agent Mode Agent Mode is Postman’s portal for working with the product in an AI-native way across testing, documentation, discovery, and implementation. Postman has evolved over 11 years, and developers and users learned to locate information through the interface by expanding sidebars, checking tabs,

## 笔记


