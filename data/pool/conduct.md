---
slug: conduct
name: Conduct
builder: sudhendra1
category: 基础层
summary_zh: 面向在应用里调用大模型与 MCP 工具的开发团队：当模型要执行外部工具调用时，Conduct 在调用发出前接收这些请求并做规则校验与拦截，最终给出放行或阻断的结果，仍需开发者自行配置规则并确认边界。具体流程与交付形态仍待核验。
inspiration: 趋势是工具调用从演示走向生产后，拦截与审计成为独立环节。切入可从金融、医疗等受监管行业的合规与平台工程团队入手，把规则库和审计记录做成随调用量计费的托管服务，而非只发一个开源库。
summary_en: 'For engineering teams that let models call external tools: Conduct sits in front of LLM and
  MCP tool calls, checking each request against rules and returning an allow-or-block result, while developers
  still configure the rules and confirm boundaries. The exact workflow and delivery form remain unverified.'
inspiration_en: The trend is that once tool calling moves from demo to production, interception and audit
  become a separate layer. A wedge is compliance and platform teams in regulated sectors such as finance
  and healthcare, selling a hosted rule library and audit trail priced by call volume rather than shipping
  only an open-source library.
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
last_seen: '2026-09-11T00:10:53Z'
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
---

# Conduct

open-source guardrails for LLM and MCP tool calls

## 笔记


