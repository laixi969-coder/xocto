---
slug: cover
name: cover
builder: DavidCarliez
category: 基础层
summary_zh: cover 是一个开源的可逆隐私代理，面向调用外部 AI 代理的开发者。开发者在把真实数据交给 cover 后，cover 会向外部 AI 代理发送逼真的假数据，并在本地恢复原始结果。它解决的是开发者担心敏感数据泄露给第三方
  AI 服务的问题，但具体工作流程和交付形式仍需进一步核验。
inspiration: 趋势：随着 AI 代理深入企业工作流，数据隐私成为采用瓶颈，可逆脱敏可能成为基础层标配。切入：可从数据合规要求高的行业（如医疗、金融）入手，提供按数据量或按代理调用计费的服务，但需先验证开发者实际付费意愿。
summary_en: cover is an open-source reversible privacy proxy for developers invoking external AI agents.
  Developers give real data to cover, which sends realistic fake data to external AI agents and restores
  originals locally. It addresses developers' concerns about sensitive data leakage to third-party AI
  services, but the specific workflow and delivery form still need verification.
inspiration_en: 'Trend: As AI agents penetrate enterprise workflows, data privacy becomes an adoption
  bottleneck, and reversible anonymization may become a standard infrastructure layer. Entry: Start with
  highly regulated industries like healthcare and finance, offering usage-based pricing per data volume
  or agent call, but first validate developers'' willingness to pay.'
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- 开发者
- 安全工程师
jobs_en:
- Developers
- Security Engineers
regions: []
regions_en: []
open_source: true
url: https://github.com/DavidCarliez/cover
canonical_url: https://github.com/DavidCarliez/cover
summary: 'Reversible privacy proxy for AI agents: send realistic fakes, restore originals locally.'
first_seen: '2026-08-21T18:56:30Z'
last_seen: '2026-09-10T05:13:56Z'
status: pending_filter
sources:
- github
- officialfeeds
- marketfeeds
- newssearch
- hackernews
sightings:
- source: github
  url: https://github.com/DavidCarliez/cover
  seen_at: '2026-08-24T22:44:36Z'
  metrics:
    stars: 41
    forks: 4
    open_issues: 0
  kind: product
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/batch-write-and-discover-records-in-amazon-sagemaker-feature-store/
  seen_at: '2026-08-29T03:43:28Z'
  metrics: {}
  kind: news
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/preparing-data-for-supervised-fine-tuning-part-1-formatting-and-quality/
  seen_at: '2026-08-29T03:43:28Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://arstechnica.com/tech-policy/2026/08/meta-tweaks-ai-glasses-to-block-some-creepy-recordings-but-privacy-risks-remain/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMi-gFBVV95cUxNQ3BiVU54T3ZUbDdUMWstU01lN090eFJ5QjVDVnluTHRIR2RBUUNNZ01oSS02ZG9VZ3dLUTlPRWpqS21KM1dmS184cWN5RThZbkdySWVhQW43ZFI3VFpLcVZFTkZnRWY1dGFoYUxZcnJmZ0x1ck9HZGJ1Tl9seW05dm1WQW1nUVc1OXh6aVlXOEludllqMklGMUk3bk1uaE1RUnhmaTdnMHpMYzZqV05tX2ZQRm9IUndTZWYyUGpYWWE5bFRyTWMybnQtNjdobjJLOUNHTVRxTjJhZl9KVmRxUWZOVGVSNzc2NHNqcmhDSmtrOU81TUJNY3pR?oc=5
  seen_at: '2026-08-29T03:43:33Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiZkFVX3lxTE5jQjJRWEh1aVBzZDJYUnBoM0JSMUdKZFhHMExkTm9GUXN3a1MtalRXZDFhNWd6Z1BQaVVEdG5fT3VFc1JKcVdCazR1Vkx4NXFPLTI4WU5VVjdNaEMzdXp2ZzJrcklEdw?oc=5
  seen_at: '2026-08-30T14:53:44Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://simonwillison.net/2026/Aug/31/andrew-digby/
  seen_at: '2026-09-01T01:18:41Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMi6gFBVV95cUxQS3R5akFJTXA1d19HVGdqRHFhY0NkMTFKN2VwQWlCVHJveUNnXzRibkRqU1JtUnNEZUpmdEJhN1JEVjM2dlNjT204akJEVkFzT2dOSlIyYnJKSnFuSmthbjNKVEVPaXJjQWdudmFfcENrS2hmMmFnNEJXWFBtZzk0R3hXV202cm9kR1BfaHA3VmxXQXF4ZWZ1OTAtaFlMNnNDbkNRVFZab2xuRi1yQ0lqalFDNFBPWi15aDNaZXNwWTl3TkU5QXVmQURKZHZ1WVVwUElSZ2F5eUYwQTRpUDFDd3RBak8tdkRlbVE?oc=5
  seen_at: '2026-09-01T14:56:33Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiogFBVV95cUxQTmNoRVN3LTNFaXcwQnUyM2lWbjl4TVcwUlZ3Z1VRWEJSV1c5emRGQ0NldFhxWnlDVlpCVkFsX2M2VTZVQlhEdmxET3FqblE4a3pKQm5rNGxzNkotWllZRndncTB0N1JMNmxaR0xJck1IRG1WcjVtazk0TF8tVnVqZERPaFBUa1BZNTRXVmdnUk1HMkJOcV9wRXdJRGl4cG4wY1E?oc=5
  seen_at: '2026-09-02T14:32:07Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMipwFBVV95cUxPbVBUVW43bjFLREJrc1doMzJFdjdvZkZJc1lrek52aFc0cS1wMEEwd2tIZ0IwTEJvTkgyZ3N2VE5NMUxBZVpRU0xDakpUTDRuRGVsV3RTWU0tSmRVWG5Pck9zdkwwMlBEQ0kyV1dYc2NvWFBDODhVbThqSjBONFFxamxySlhZbS1oU0o1c3g4NVRjTXhfNzF0MTFJdlplWi1rdXZLcV82cw?oc=5
  seen_at: '2026-09-08T14:34:55Z'
  metrics: {}
  kind: news
- source: hackernews
  url: https://mhacevedo.com/posts/the-discovery-problem
  seen_at: '2026-09-10T05:13:24Z'
  metrics:
    points: 68
    comments: 34
  kind: news
- source: marketfeeds
  url: https://www.qbitai.com/2026/09/486436.html
  seen_at: '2026-09-10T05:13:56Z'
  metrics: {}
  kind: news
---

# cover

Reversible privacy proxy for AI agents: send realistic fakes, restore originals locally.

## 笔记


