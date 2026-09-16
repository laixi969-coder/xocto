---
slug: tare
name: tare
builder: sachinneravath
category: AI + 开发
summary_zh: 使用 Claude 等按量计费模型的开发者，在配额被意外快速耗尽时打开 tare，让它读取自己的调用记录，拆出是哪些请求、哪类上下文吃掉了额度，最终得到一份用量去向的分解结果，据此调整提示或调用方式；具体统计口径与交付形式仍待核验。
inspiration: 趋势是模型按量计费后，额度本身成了需要被管理的生产资源，围绕“钱花在哪一步”的观测会先于优化工具出现。切入可以从独立开发者和小型 AI 应用团队入手，先做单账户的用量归因，再考虑按团队席位或按被监控的调用量收费；价格未披露，不做假设。
summary_en: Developers using metered models such as Claude open tare when their quota drains unexpectedly
  fast; it reads their call records and breaks down which requests and which kinds of context consumed
  the budget, returning a usage attribution the developer can act on by changing prompts or call patterns.
  The exact accounting method and output format still need verification.
inspiration_en: 'The trend: once models are metered, quota becomes a production resource that must be
  managed, so observability into where spend goes tends to appear before optimization tooling. The entry
  point is individual developers and small AI app teams, starting with single-account usage attribution
  and later charging per seat or per monitored call volume; no pricing is disclosed, so none is assumed.'
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software development
jobs:
- AI 应用开发者
jobs_en:
- AI application developer
regions: []
regions_en: []
open_source: true
url: https://github.com/kelviq/tare
canonical_url: https://github.com/kelviq/tare
summary: My Claude quota ran out in 10 minutes, so I made a tool to find out why
first_seen: '2026-08-27T16:37:44Z'
last_seen: '2026-09-16T00:21:06Z'
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
- source: marketfeeds
  url: https://www.theverge.com/ai-artificial-intelligence/995917/data-center-nyt-midterm-poll-september
  seen_at: '2026-09-16T00:21:06Z'
  metrics: {}
  kind: news
---

# tare

My Claude quota ran out in 10 minutes, so I made a tool to find out why

## 笔记


