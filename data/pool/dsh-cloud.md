---
slug: dsh-cloud
name: dsh-cloud
builder: eskim2001
category: 基础层
summary_zh: 团队要在内部跑 DeepSeek Harness 时，过去得自己搭容器、分配机器并管理每个成员的工作区。dsh-cloud 提供多租户部署方式，把每个实例放进隔离容器、保留持久工作区并设置资源配额，用户最终拿到一套可自托管或托管的运行环境；候选资料未说明与官方托管方案的差异，也未给出定价或付费用户。
inspiration: 趋势：编码代理的运行环境开始被单独产品化，从“每人一台机器”变成“多租户配额管理”。切入：面向需要把编码代理放进内网、又要求隔离与配额的中型研发团队，按实例或资源用量收费；难点在于官方若自带托管，这类第三方平台的空间会被压缩。
summary_en: 'When a team wants to run DeepSeek Harness internally, the old path is building containers,
  allocating machines and managing each member''s workspace by hand. dsh-cloud offers a multi-tenant deployment:
  each instance runs in an isolated container with persistent workspaces and resource quotas, giving users
  a self-hosted or cloud-hosted runtime. The material does not compare it with official hosting, nor give
  pricing or paying users.'
inspiration_en: 'Trend: runtime environments for coding agents are becoming their own product, shifting
  from one machine per person to multi-tenant quota management. Entry: target mid-size engineering teams
  that must keep coding agents inside their network while requiring isolation and quotas, charging per
  instance or per resource usage; the risk is that official hosting shrinks the room for third-party platforms.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 团队内部 AI 编码环境运维
- 多租户沙箱环境搭建
jobs_en:
- Internal AI coding environment operations
- Multi-tenant sandbox setup
regions: []
regions_en: []
open_source: true
url: https://eskim2001.github.io/dsh-cloud/
canonical_url: https://eskim2001.github.io/dsh-cloud
summary: 'dshcloud：部署并托管 DeepSeek Harness (dsh) 实例的多租户平台，支持自托管或云端部署。Deploy and host DeepSeek Harness (dsh)
  instances — self-hosted on your own server or cloud-hosted: a multi-tenant platform with isolated Docker
  containers, persistent workspaces and resource quotas.'
first_seen: '2026-09-09T07:47:57Z'
last_seen: '2026-09-12T00:18:44Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://eskim2001.github.io/dsh-cloud/
  seen_at: '2026-09-12T00:18:44Z'
  metrics:
    stars: 63
    forks: 1
    open_issues: 0
  kind: product
---

# dsh-cloud

dshcloud：部署并托管 DeepSeek Harness (dsh) 实例的多租户平台，支持自托管或云端部署。Deploy and host DeepSeek Harness (dsh) instances — self-hosted on your own server or cloud-hosted: a multi-tenant platform with isolated Docker containers, persistent workspaces and resource quotas.

## 笔记


