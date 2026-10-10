---
slug: drop
name: Drop
builder: zhangchen0411
category: AI + 开发
summary_zh: 开发者在运行不可信代码或 AI 生成代码时打开它，把待执行的程序交给一个无 root 权限的 Linux 沙箱（支持 gVisor）隔离运行，最终拿到隔离环境中的执行结果；具体交付形态与人工确认环节仍待核验。
inspiration: 趋势：AI 生成代码大量进入生产流程，隔离执行不可信代码正从安全团队的专项工作变成普通开发者的日常步骤。切入：可从需要跑第三方或模型生成代码的团队进入，把沙箱做成按执行次数计费的托管服务，但定价与客户案例尚未披露。
summary_en: Developers open it when running untrusted or AI-generated code, handing the program to a rootless
  Linux sandbox with gVisor support for isolated execution and getting back the result from that sandbox;
  the exact delivery form and human confirmation step still need verification.
inspiration_en: 'Trend: as AI-generated code floods into production workflows, isolating untrusted code
  is shifting from a security-team specialty to a daily step for ordinary developers. Entry: start with
  teams that must run third-party or model-generated code and offer the sandbox as a per-execution hosted
  service, though pricing and customer cases are not yet disclosed.'
priority_review: false
project_type: open_source
industries:
- 软件开发
- 云计算
industries_en:
- Software Development
- Cloud Computing
jobs:
- 开发者在运行不可信代码或 AI 生成代码时，需要隔离执行环境以完成安全测试
jobs_en:
- Developers running untrusted or AI-generated code need an isolated execution environment for safe testing
regions: []
regions_en: []
open_source: false
url: https://drop.space
canonical_url: https://drop.space
summary: They chose your competitor. Find out why
first_seen: '2026-09-10T02:20:02Z'
last_seen: '2026-10-10T01:46:29Z'
status: watching
sources:
- hackernews
- newssearch
- marketfeeds
sightings:
- source: hackernews
  url: https://drop.space
  seen_at: '2026-09-11T00:10:31Z'
  metrics:
    points: 6
    comments: 2
  kind: product
- source: hackernews
  url: https://nathannaveen.dev/posts/dropping-ebpf-cpu-cost-by-90/
  seen_at: '2026-09-16T00:20:36Z'
  metrics:
    points: 149
    comments: 29
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMixAFBVV95cUxQS01NMVg3RnZ0YUZTeGNRaEl0NXBkR0s1dWVmT3hlWDlOZm9YYmNmRmludVZXSzZaRkRaWVZDaW5WMkNSRnhubmctSGMydFdSZjZ0U3gweThUQkY0cVhUWV9OUkFXbXIxYWpwOTFfZ0VRaVJJcUhDTnBxMGRUdDlBTzFpR2NCMEdNbU1UTmZlVHgyNUJnbnJ6WnFNMDNGY2Znb2RLRERsbkQ4MVFTXzJaUko1ajNLWVJaQlJ5RlVGQnd1d3hI0gHEAUFVX3lxTFBLTU0xWDdGdnRhRlN4Y1FoSXQ1cGRHSzV1ZWZPeGVYOU5mb1hiY2ZGaW51VldLNlpGRFpZVkNpblYyQ1JGeG5uZy1IYzJ0V1JmNnRTeDB5OFRCRjRxWFRZX05SQVdtcjFhanA5MV9nRVFpUklxSENOcHEwZFR0OUFPMWlHY0IwR01tTVROZmVUeDI1QmducnpacU0wM0ZjZmdvZEtERGxuRDgxUVNfMlpSSjVqM0tZUlpCUnlGVUZCd3V3eEg?oc=5
  seen_at: '2026-09-19T00:21:52Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMivwFBVV95cUxPRy1Za1h4T19JZDhxem4tR2Fldmc5QzdCeFhMbGJKYUFqMzJvVDRRYTlqd05mU1IwRFRkNkE0RGFyZlZKLWxTaUVrVFVpcnRSZEt4VzNXTXRBbnpNbFlQWVRpd2hoaXRsUmFSSzBrbFNwT01tTVRfVDJpZ3RyUjdYakdEd0tzbjM0QW45VmRPcHBUS2RXQnByMVNNeFg3Yzc3OVJZcGI1ZktVTUFJSGdXLU1xWnd2eGxkWW5FQnlXd9IBxAFBVV95cUxQS01NMVg3RnZ0YUZTeGNRaEl0NXBkR0s1dWVmT3hlWDlOZm9YYmNmRmludVZXSzZaRkRaWVZDaW5WMkNSRnhubmctSGMydFdSZjZ0U3gweThUQkY0cVhUWV9OUkFXbXIxYWpwOTFfZ0VRaVJJcUhDTnBxMGRUdDlBTzFpR2NCMEdNbU1UTmZlVHgyNUJnbnJ6WnFNMDNGY2Znb2RLRERsbkQ4MVFTXzJaUko1ajNLWVJaQlJ5RlVGQnd1d3hI?oc=5
  seen_at: '2026-09-21T00:17:23Z'
  metrics: {}
  kind: news
- source: hackernews
  url: https://droprun.sh/
  seen_at: '2026-09-24T00:30:46Z'
  metrics:
    points: 185
    comments: 61
  kind: product
- source: hackernews
  url: https://matthewbutterick.com/chron/drop-dead.html
  seen_at: '2026-09-23T00:34:15Z'
  metrics:
    points: 44
    comments: 0
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiygFBVV95cUxNRXZZUzBLTFk4ZV9HZmZ2NmFfUFl4Y1U1amYwQl90OHo5VFQwc296S1BvNlVvM1M0dE5wY3FraTFraFpOVFFfVDRSMGgtT1dXaDBveDRhVkVJM0xFYWFNVEdNZW11blE2cnlMNHhkQm02N1hyQmFhc0dJUFpUaU84X3NJX3VLM2cydlZ0WHVZM1BtMkprcTVDX1U1VTZuX2M5Rml3d0NDZUJKcTFfM1dVN0RabjdkcUYwOTQ3a0Z3bEV5QUZKcGtqZXRR?oc=5
  seen_at: '2026-10-05T00:56:35Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMirgFBVV95cUxPbkhfQXBhLVQ1eGZCaWM5YzBQa1A3N2lzdk81ZklxX0JOQ3E0VV9KUThRUjFTRWF4Y3NCbHc2OXR6blpXRnlXQkZmZkJQc2JjdF9ZallOUUtpSkltaEI0NUdWbk9pU2c2REVqd1oxbHExcGpfWG1iNW1mSjQ1R01lYnFkRF9aOUtPWE5va0pnb01lQ1ZfNEMxb3ZFTmRNM0tkWEI0TG5VbTdHVHVzREE?oc=5
  seen_at: '2026-10-08T01:56:23Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://www.theverge.com/ai-artificial-intelligence/1008726/openai-mathematics-solutions-chaos
  seen_at: '2026-10-10T01:46:29Z'
  metrics: {}
  kind: news
---

# Drop

They chose your competitor. Find out why

## 笔记


