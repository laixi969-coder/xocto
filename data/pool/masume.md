---
slug: masume
name: masume
builder: turanmahmudov
category: AI + 开发
summary_zh: 后端工程师在排查线上数据或核对表结构时，原本要在数据库客户端和 AI 对话窗口之间来回切换、手工复制表名和字段。masume 在终端里打开数据库读取内容，并把同一份目录信息交给 agent，让工程师在同一个界面里查看结构并让
  agent 基于该目录继续操作；最终交付仍由工程师自己确认，具体支持哪些数据库和 agent 接入方式待核验。
inspiration: 趋势是数据库目录正在变成人和 agent 共用的同一份上下文，而不是各自维护一份。切入可以从已经用 agent 写 SQL 的小型后端团队做起，先解决“agent 看不到真实表结构”这一步，再考虑按团队或按数据源收费；目前只有开源仓库，付费路径尚未披露。
summary_en: When debugging production data or checking a schema, backend engineers currently switch between
  a database client and an AI chat window and copy table and column names by hand. masume opens a database
  in the terminal, reads it, and hands the same catalog to an agent, so the engineer can inspect the schema
  and let the agent work from that catalog in one place; the engineer still confirms the final action,
  and which databases and agent integrations are supported remains to be verified.
inspiration_en: The trend is that a database catalog becomes one shared context for both the human and
  the agent instead of two copies. A way in is to start with small backend teams that already use agents
  to write SQL, fix the step where the agent cannot see the real schema, and later charge per team or
  per data source; only an open-source repository exists today and no pricing path is disclosed.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 后端开发工程师
jobs_en:
- Backend software engineer
regions: []
regions_en: []
open_source: true
url: https://github.com/turanmahmudov/masume
canonical_url: https://github.com/turanmahmudov/masume
summary: A database client for the terminal. Open a database, read it, and give an agent the same catalog.
first_seen: '2026-08-30T18:22:22Z'
last_seen: '2026-09-12T00:18:44Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/turanmahmudov/masume
  seen_at: '2026-09-12T00:18:44Z'
  metrics:
    stars: 67
    forks: 2
    open_issues: 0
  kind: product
---

# masume

A database client for the terminal. Open a database, read it, and give an agent the same catalog.

## 笔记


