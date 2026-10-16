---
slug: rdst
name: RDST
builder: gvsg
category: AI + 开发
summary_zh: 数据库工程师在版本发布或流量变化后，需要判断 Postgres/MySQL 的查询是否变慢。RDST 是一个本地运行的 agent，持续观察这些数据库的查询表现并标出回退，具体告警形式、接入方式和交付物仍待核验。
inspiration: 趋势：数据库性能回归的排查正从人工比对慢日志，转向常驻本地 agent 持续盯守。切入：可从已有 DBA 团队的中型 SaaS 或电商切入，把回归定位做成按实例或按事件计费的托管服务，而非再卖一个监控面板。
summary_en: After a release or traffic shift, database engineers must judge whether Postgres/MySQL queries
  have slowed. RDST is a locally run agent that watches these databases for query regressions; its alerting
  format, setup path and deliverables still need verification.
inspiration_en: 'Trend: catching database performance regressions is shifting from manual slow-log comparison
  to a resident local agent. Entry: target mid-size SaaS or e-commerce teams that already have DBAs, and
  sell regression triage per instance or per incident rather than another monitoring dashboard.'
priority_review: false
project_type: open_source
industries:
- 软件与信息技术服务
industries_en:
- Software and IT Services
jobs:
- 数据库工程师在版本发布或流量变化后排查 Postgres/MySQL 查询性能回退
jobs_en:
- Database engineers triaging Postgres/MySQL query performance regressions after releases or traffic shifts
regions: []
regions_en: []
open_source: true
url: https://github.com/readysettech/rdst
canonical_url: https://github.com/readysettech/rdst
summary: A local agent that watches Postgres/MySQL for query regressions
first_seen: '2026-10-16T00:25:14Z'
last_seen: '2026-10-16T00:25:14Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/readysettech/rdst
  seen_at: '2026-10-16T00:25:14Z'
  metrics:
    points: 6
    comments: 1
  kind: product
---

# RDST

A local agent that watches Postgres/MySQL for query regressions

## 笔记


