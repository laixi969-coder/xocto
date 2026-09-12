---
slug: tare
name: tare
builder: sachinneravath
category: AI + 开发
summary_zh: 开发者在调用大模型 API 时额度被快速耗尽，会打开 tare 查看是哪些请求、哪段代码在消耗额度；它接收调用记录并归因到具体来源，最终给出额度消耗的分布结果，具体采集方式与交付形态仍待核验。
inspiration: 趋势是模型额度正变成团队要核算的运营成本，而不是随手可用的免费资源。切入可以从按项目或按团队做额度归因与预算告警入手，卖给自建 AI 功能的研发团队；公开材料未披露定价，是否按席位收费尚不清楚。
summary_en: When developers burn through their LLM API quota quickly, they open tare to see which requests
  or code paths consumed it; it takes call records and attributes them to specific sources, returning
  a breakdown of quota consumption, though the exact collection method and deliverable still need verification.
inspiration_en: The trend is that model quota is becoming an operating cost teams must account for rather
  than a free resource. An entry point is per-project or per-team quota attribution and budget alerts
  sold to engineering teams building AI features; no public pricing is disclosed, so per-seat charging
  is unconfirmed.
priority_review: false
project_type: open_source
industries:
- 软件开发
- 信息技术服务
industries_en:
- Software Development
- IT Services
jobs:
- AI 应用开发者
- 研发效能工程师
jobs_en:
- AI Application Developer
- Developer Productivity Engineer
regions: []
regions_en: []
open_source: true
url: https://github.com/kelviq/tare
canonical_url: https://github.com/kelviq/tare
summary: My Claude quota ran out in 10 minutes, so I made a tool to find out why
first_seen: '2026-08-27T16:37:44Z'
last_seen: '2026-09-12T00:19:09Z'
status: watching
sources:
- hackernews
- marketfeeds
- newssearch
sightings:
- source: hackernews
  url: https://github.com/kelviq/tare
  seen_at: '2026-08-29T03:43:08Z'
  metrics:
    points: 86
    comments: 62
  kind: product
- source: marketfeeds
  url: https://news.crunchbase.com/venture/legal-tech-startuo-funding-down-ai-acquisitions-2026/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://www.theverge.com/tech/986593/instagram-addresses-fake-ai-profile-slop
  seen_at: '2026-08-31T17:38:50Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://www.theverge.com/ai-artificial-intelligence/987486/john-deere-jd-ai-chatbot
  seen_at: '2026-09-02T00:14:54Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMirwFBVV95cUxPNDY3U1hVblozS0s4b1VGU3BpekVLVVphTE5abXRHb0JmbzNVZGdjS3p5VVJsT05ITjFud19mRmVaUWFkR0lqLWJES1pmU3BSVUdOaHNsYkpuWTFqOFZDYzNkaGxKeWJncnlpcFNxUHduaFE2dDlYMm9BR1FNaW5QWVpYc19nbnJRMVRraF9oSFh3NzlKVUQtREtJT29wSUdaLWczcjVIR3ZkZ0F3YV9R?oc=5
  seen_at: '2026-09-10T05:14:03Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/
  seen_at: '2026-09-12T00:19:09Z'
  metrics: {}
  kind: news
---

# tare

My Claude quota ran out in 10 minutes, so I made a tool to find out why

## 笔记


