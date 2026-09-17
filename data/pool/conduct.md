---
slug: conduct
name: Conduct
builder: sudhendra1
category: 基础层
summary_zh: 面向在应用里调用大模型和 MCP 工具的开发团队：当模型准备执行一次工具调用时，Conduct 先接收这次调用请求，按预设规则判断是否放行、拦截或改写，再把结果交回调用方。用户拿到的是被约束过的调用结果，具体规则配置与交付形态仍待核验。
inspiration: 趋势是模型开始直接操作外部工具，出错代价从“答错一句话”变成“改错一条数据”，因此调用前的拦截层正在变成刚需。切入可以从金融、医疗这类对操作留痕有硬要求的行业做起，把规则库和审计记录做成可交付的合规材料，而不是只卖一个开源库。
summary_en: 'For teams calling LLMs and MCP tools inside their apps: when a model is about to run a tool
  call, Conduct receives the request, applies preset rules to allow, block or rewrite it, and returns
  the result to the caller. What users get is a constrained call result; the rule configuration and delivery
  format still need verification.'
inspiration_en: The trend is models acting directly on external tools, so an error shifts from a wrong
  sentence to a corrupted record, making a pre-call interception layer a real need. A wedge is to start
  with finance or healthcare, where operation trails are mandatory, and sell rule sets plus audit records
  as compliance deliverables rather than just an open-source library.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/sseshachala/conductai
canonical_url: https://github.com/sseshachala/conductai
summary: open-source guardrails for LLM and MCP tool calls
first_seen: '2026-08-28T19:29:20Z'
last_seen: '2026-09-17T00:33:01Z'
status: watching
sources:
- hackernews
- marketfeeds
- newssearch
sightings:
- source: hackernews
  url: https://github.com/sseshachala/conductai
  seen_at: '2026-08-29T15:06:03Z'
  metrics:
    points: 22
    comments: 4
  kind: product
- source: marketfeeds
  url: https://tech.eu/2026/08/31/s-transistors-raises-eur26m-for-superconducting-quantum-computing-platform/
  seen_at: '2026-08-31T17:38:50Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMivwFBVV95cUxQYXJCTFBmOXJaeW5COWpEbHA3bE9ndVAzazBTOXZkUkhGMk5SVFhhb1o1bTUzUzVFSzRGWUdmZk40N3Nra1VHV0k3a2lXQ21jQk15Vmc4OFNkZENSVkxtRUdfX0o3cXVzU04wRjN1TWR2LVlTeUV6NGVKeDFDMEJ0RnVuS1E2SC0xakFUcklFYnlUaUZvd29lN1duenFGNXFFYXJrSUt0Z0RRem9GS2pVa3g3Wjc3ZFFySUd1U281Zw?oc=5
  seen_at: '2026-08-31T17:38:59Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://news.crunchbase.com/venture/august-2026-new-unicorns-ai-robotics-semiconductors-xpeng-lumilens-river-source/
  seen_at: '2026-09-11T00:10:53Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://www.technologyreview.com/2026/09/16/1144014/building-the-materials-foundation-for-ai/
  seen_at: '2026-09-17T00:33:01Z'
  metrics: {}
  kind: news
---

# Conduct

open-source guardrails for LLM and MCP tool calls

## 笔记


