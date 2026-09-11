---
slug: turn-wire-protocols-into-structured-statements-llms-can-unde
name: Envoy LLM payload inspection extension
builder: andriosr
category: 基础层
summary_zh: 后端与安全工程师在排查线上 API 异常请求时，打开这个 Envoy 代理扩展，它先用确定性 SQL 解析器和 gRPC 载荷检查把请求内容转成结构化语句，再交给 LLM 分析，最终给出对请求内容的判断结果，仍需人工确认结论。具体交付形态与部署流程仍待核验。
inspiration: 趋势：代理层正在成为 LLM 观察流量的新位置，而不是只在应用代码里调用模型。切入：从金融、支付这类对请求审计有硬性要求的行业进入，把网关日志转成可读请求说明，按审计或排障次数收费，而不是卖一个通用代理插件。
summary_en: Backend and security engineers diagnosing abnormal live API requests open this Envoy proxy
  extension; it first converts request contents into structured statements using a deterministic SQL parser
  and gRPC payload inspection, then hands them to an LLM for analysis, returning a judgement on the request
  content that a human still has to confirm. The exact deliverable and deployment flow remain unverified.
inspiration_en: 'Trend: the proxy layer is becoming a new place to observe traffic with LLMs, rather than
  calling models only inside application code. Entry point: start with finance and payments, where request
  auditing is mandatory, turning gateway logs into readable request descriptions and charging per audit
  or troubleshooting run instead of selling a generic proxy plugin.'
priority_review: false
project_type: open_source
industries:
- 软件与互联网服务
- 金融与支付
- 企业IT服务
industries_en:
- Software and internet services
- Financial services and payments
- Enterprise IT services
jobs:
- 后端与安全工程师在排查线上 API 异常请求时，处理代理层抓到的 SQL 与 gRPC 载荷，要判断请求是否异常并定位原因
- 平台运维人员在接入第三方服务时，处理网关日志中的请求内容，要生成可读的请求说明供审计或排障
jobs_en:
- Backend and security engineers diagnosing abnormal live API requests, working on SQL and gRPC payloads
  captured at the proxy layer, to judge whether a request is anomalous and locate the cause
- Platform operations staff onboarding third-party services, working on request contents in gateway logs,
  to produce readable request descriptions for audit or troubleshooting
regions: []
regions_en: []
open_source: true
url: https://news.ycombinator.com/item?id=49646376
canonical_url: https://news.ycombinator.com/item?id=49646376
summary: Hi HN, we built an extension to Envoy proxy that parses and sends contents of requests to an
  LLM at runtime. We do that by adding a deterministic SQL parser, gGRPC payload inspection and LLM analysis
  of the payload befor…
first_seen: '2026-09-10T16:25:23Z'
last_seen: '2026-09-11T00:10:31Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://news.ycombinator.com/item?id=49646376
  seen_at: '2026-09-11T00:10:31Z'
  metrics:
    points: 5
    comments: 0
  kind: product
---

# Envoy LLM payload inspection extension

Hi HN, we built an extension to Envoy proxy that parses and sends contents of requests to an LLM at runtime. We do that by adding a deterministic SQL parser, gGRPC payload inspection and LLM analysis of the payload befor…

## 笔记


