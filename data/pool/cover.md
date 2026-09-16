---
slug: cover
name: cover
builder: DavidCarliez
category: 基础层
summary_zh: 开发者在把真实客户数据交给外部大模型接口前打开它：代理层把姓名、账号等敏感字段替换成格式一致的假值再转发给模型，模型返回后在本机把假值还原成原文，开发者拿到的是可用的模型输出，同时原始数据没有离开本地。具体还原范围与人工确认环节仍待核验。
inspiration: 趋势是模型调用正在被合规和隐私审查卡住，尤其是金融、医疗这类不能把原始数据外发的场景。切入可以从受监管行业的 AI 接入环节做：不做通用脱敏工具，而是绑定某一类数据（如券商客户记录、病历字段）做可逆替换加本地还原，按接入的模型调用量或按合规审计报告收费。
summary_en: 'Before sending real customer data to an external model API, a developer routes it through
  this proxy: sensitive fields such as names and account numbers are swapped for format-consistent fakes,
  the model answers on the fakes, and the originals are restored locally so the usable output comes back
  without the raw data leaving the machine. The exact restore scope and any human confirmation step still
  need verification.'
inspiration_en: 'The trend is that model calls are increasingly gated by compliance and privacy review,
  especially where raw data cannot leave the building. The entry point is the AI onboarding step inside
  regulated industries: instead of a generic redaction tool, bind to one data class (brokerage client
  records, medical fields) with reversible substitution plus local restore, and charge by model call volume
  or by compliance audit report.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
- 金融合规
industries_en:
- Software & IT Services
- Financial Compliance
jobs:
- AI 应用开发者
- 数据合规工程师
jobs_en:
- AI Application Developer
- Data Compliance Engineer
regions: []
regions_en: []
open_source: true
url: https://github.com/DavidCarliez/cover
canonical_url: https://github.com/DavidCarliez/cover
summary: 'Reversible privacy proxy for AI agents: send realistic fakes, restore originals locally.'
first_seen: '2026-08-21T18:56:30Z'
last_seen: '2026-09-16T00:21:13Z'
status: watching
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
- source: newssearch
  url: https://news.google.com/rss/articles/CBMixgFBVV95cUxONTF2WnlqaF9lZHItWi11dTRFdW5LdVh6eW1sNFk5U2Z5TGVSLWxyV090QlNSeDhaUVl3MEF2Y1htbWlVbHRGcHZPclBqUzRQdDhRanJYZFliZzRaTGtwWmg1TUNiUndlbjJPVDRGR2IwZU42OXQ2czhZRFphZVlaNk8zNHk0dnVjeTNRUi10eGxOUXRNY2pfeUpWTzZmU1dmajhlYThXMG95eF9rMkJ6cmFyNnl6ZTdOMWlfRVdodjVveGREaUE?oc=5
  seen_at: '2026-09-13T00:02:40Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiaEFVX3lxTFBPbFNmb1dScU4yMmZsT2VMX2tOSDE1ZC1zd2stUjdlT1FyUWxHdmNLb0JIcGhwUldmaUhnelVYYnZiaGRYZnBoeVNaU0JSRFFqaU5MckZBUTFJR0Jyc0lZVURKMGtSN1Nv?oc=5
  seen_at: '2026-09-13T00:02:40Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMi2AFBVV95cUxONVBCdEdoanlRNzJNNm5qMzk2dVNza0tra0N2bE5XbDZIVXNWdFp6VmdhVjVicnhrWWthOXg0b2xVcUZYUzlOU1BEVEMxcG94a2Z2aXJkZVJOSG9NakxpZl9OSHNrV3Q0RGFjdDFWTGJ6Vms2OGNWcTF5SUJ3cklKeUpRbmpiTmRxREpseXVrYjJ1NXdXY0lfdkdKX0lUYUhqOFhwLXhKek1IRmExcWFRMm9MalcxcUs1QXNLdXZxSmg1MzRuejhsNTdXT1lLcklSZEQ2dU8zSEvSAd4BQVVfeXFMT1pjQkVNUnpTQzhUZE1lQ244YUNnZ2lwZXBpNlc5WVpfT1BzNTRfZjRWMVRsaHRsWlBvUDBXR3FEMWxkVkpoLS15MjJhV1NXUWVBSFBVWjZRR0tGb1J1MTROVlMxUjBnWUtUS3ZncFUzS2k0U05HWXFacG9BampVOU1uTG5qdTM4ZmV5azlidFBSdkRJWnRZZGN0NnZzQjBiZ0dXUkJmQmV0OFhSZF96dnZUNEl5VEdPVzEtN3BJbWNPcmdGekpkcnloZ2hkWDRtdEFIWThJUEtDZDZ5S2J3?oc=5
  seen_at: '2026-09-14T00:13:04Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMid0FVX3lxTE03TDFKaUNobHNmYkxKZFZPaEJaVXRGUmF5YjhUX3g2eVZxVml5cW9IY2lIeVVUMXdwY1ZKeHV5TkFSQnhvOS1rVmx4ZDVKNk41MUxxcGZuUTRjVmJ3YWR3ajU4b1d2eVJBV1cwTURDQkpUU2t5Yks0?oc=5
  seen_at: '2026-09-14T00:13:04Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMixAFBVV95cUxPdmQ2YzZJR1NvWXBsNk1HTW03UVZFUjVRdHE3c1ZSMzhpakI5QVYydl9GY2dXd3BJaFZTdkt3b3Y5elZvWWJfSkdhc1lVSHNuZnJtc19ObkR2LVZoYnZENDRhMzlpNDI2UnpYWi1rYnlwZ0xhdjNDTzZmSThkaDhCOXgycU52aENCc0dEUWRDWDBmTW10WkpwNjlfWjlDN3RMbmQ1U09HWHM4RDZVTm1YVUdINVdhM1RUQ3VQWC1fRnVzOG1f?oc=5
  seen_at: '2026-09-14T00:13:04Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMilAFBVV95cUxPTnFId3lDXzdGUE5OMjA5bmVlSFY5VnNMWUVZNVJQUG5wb05vMXk2T1JMbzlWNzdWVUZod0lIcVJjNTlnZWVJX2d4WHhtOTVxVUNnZDBaaGJxLUxUT2NGQkplS1JxcWJjNzNFc3VPSXMwNmNjc1puNlJ3SDV0R3p2WkZjeC1MODVMUy1wUkdod3U5TWpQ0gGaAUFVX3lxTE5lRWlhbWNvemt3TmJ3Q09xdWRQNlR4WjdmNDFscnE0UDgxSUFIVkR3d2JLVG8yX0NCbG8wS1dzWUlKdm8ydG1kdUdwRUhicFdVV2p2bEg5NVJndEZNcVVud2xzMVBIbENMdVkwakxOblo2UmJNTmlJcmV3QzRCdV9fVm81eU1adnhPcGxGUTJfR0gwWTJsRXNTVkE?oc=5
  seen_at: '2026-09-16T00:21:13Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMitwFBVV95cUxQU2ZKSHFFZ2RIcUhZYUFfZjFiVlA4WjN6X19RWTl1VGJqNllWc0JEclF2SmpabzZrLWhzalRTWXZmWkNpb1ZfUnB6NEN5eTNyc1I4cHVQcmcwVUE3bTNfbk9uTlZ2ZnpDX2hQemVHVGNhMDJTSGlGU0pqem9ORmJINVYzcFloVjg4S1V0UUJqY0Y5a1dpX1BESHNPZWROUXJhczlqMm1OeUhTQUpmXzVFSEpNQW5jVmc?oc=5
  seen_at: '2026-09-16T00:21:13Z'
  metrics: {}
  kind: news
---

# cover

Reversible privacy proxy for AI agents: send realistic fakes, restore originals locally.

## 笔记


