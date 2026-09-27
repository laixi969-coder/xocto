---
slug: cover
name: cover
builder: DavidCarliez
category: 基础层
summary_zh: 开发者在把真实客户数据交给外部大模型处理时，可先经它把姓名、账号等敏感字段替换成逼真假数据再发出，模型返回后在本机把原值还原，最终拿到可用的模型输出而原始数据不出本地；还原环节仍需人工确认。具体流程与交付细节仍待核验。
inspiration: 趋势是 AI 应用开始把敏感数据外发当成必须处理的合规环节，而不是事后补救。切入可从处理病历、保单、财税凭证这类不能外流材料的行业入手，把脱敏与还原做成随调用发生的默认步骤，而不是让团队自己写脚本。
summary_en: When developers send real customer data to an external model, this proxy swaps names, accounts
  and other sensitive fields for realistic fakes before the request leaves, then restores the originals
  locally on the response, so usable model output comes back while raw data stays on the machine; the
  restore step still needs human confirmation. The exact workflow and deliverables remain unverified.
inspiration_en: The trend is that AI applications now treat sensitive-data egress as a step to be handled
  by default rather than patched afterwards. A wedge is to enter industries whose materials cannot leave
  the premises, such as medical records, insurance policies or tax documents, and make masking and restoration
  happen with each call instead of leaving teams to write their own scripts.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/DavidCarliez/cover
canonical_url: https://github.com/DavidCarliez/cover
summary: 'Reversible privacy proxy for AI agents: send realistic fakes, restore originals locally.'
first_seen: '2026-08-21T18:56:30Z'
last_seen: '2026-09-27T00:36:53Z'
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
- source: marketfeeds
  url: https://sifted.eu/articles/uk-sovereign-ai-fund-in-talks-to-back-500m-raise-for-drug-discovery-startup/
  seen_at: '2026-09-19T00:21:45Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiekFVX3lxTE92Y3hKMk52MlBJSlFTZ0dET1VrZzhkZXFjYk1HdndDX2xDUU9pSkxOMldZRXRaeWc4MDFxZWxnMXo3U1pIX0d3dWg1X1owaVFfSC1WbXN6WnFOQmRVdGdQZzFmMmwwWXhYTEJCMFZ2X1pSV3cwRjNhY2h3?oc=5
  seen_at: '2026-09-22T00:50:58Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://sifted.eu/articles/browse-sifteds-company-coverage/
  seen_at: '2026-09-25T00:34:10Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiwwFBVV95cUxNZ2NIVk1PZHVCR0JZMldCb2JDNmlWdnJEbzNXVWVDcEVQRG5fZHZvQTBzNzBaSTJiTk9GNkpLZGZLWGJIQm1mMzVvdnB0ZTRkUkxXOUt0S3A5QU1QNDdjVlN4RUhzQnNLRWhfTEFWZDBmZTBpa3NfZ2xYeFdFcGtkSTNwdUw5akxFUkJqOU5YWVpmTDNfdm5nV3BVbXpXb0RsdEs2QzJrT3NNNGZ5cGNSVVdBLWhmQkxUZjkyS2xGUFcxNHc?oc=5
  seen_at: '2026-09-26T00:38:27Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMihAFBVV95cUxPUDlNUTdaejBYTTZJYXZzeVFicFc3bTRaT242b3JmY1NmS0l0ajVQOWl5MHgwLXJ0aGNlNkV3VHlSVG5yTzR0SUIxMVFqT0cxSDlCRjh4bHVTTTlscFJlTkxNMVpOellxdk0wV1dicWJwUVI4T3ByWmxDQTJ2dF9yWHowUWI?oc=5
  seen_at: '2026-09-27T00:36:53Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiwAFBVV95cUxQSW1OcmFXS3NsMWhCOFZUaHdfNHlveGJNV1BKVnVkbGV1MW9UeGZLbTg2andsSlNOSEFUNlE5Q0RYTG1qdkxhQzBGQnBpOENQV3dsR2hST09YTE1EZkJMYUNnYmF3X0cyX2V4ODZBMEhzQ1lkZy1pSHhyeE9GN0RMb2czTWNBbHE4d0g0SVppbmhNa0thQ3B1dEJ0bUIwUHJkaExmVF9jel9RTXl1UVZtTE40VUtIaE8wUFBwTmtxMjI?oc=5
  seen_at: '2026-09-27T00:36:53Z'
  metrics: {}
  kind: news
---

# cover

Reversible privacy proxy for AI agents: send realistic fakes, restore originals locally.

## 笔记


