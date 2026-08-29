---
slug: flyxl
name: DataZen
builder: flyxl
category: AI + 开发
summary_zh: DataZen 是一个开源的数据库客户端，面向日常查库和跨库查询场景。开发者输入多步 SQL 查询，用 YAML 串联工作流，上一步结果自动传给下一步，支持跨数据库执行；同时提供运营看板，保存常用
  SQL 和图表定时刷新。AI 辅助生成 SQL 和错误诊断，但核心是工作流和看板。
inspiration: 趋势是数据库工具从单机客户端走向可编程工作流和自动化看板。切入点是合规限制催生的自建工具需求，可面向中小团队提供跨库查询和报表自动化，按席位或功能收费。
summary_en: DataZen is an open-source database client for daily queries and cross-database workflows.
  Developers chain multi-step SQL queries via YAML, passing results automatically between steps, and use
  dashboards to save frequent queries and charts with scheduled refresh. AI assists SQL generation and
  error diagnosis, but the core is workflow and dashboard.
inspiration_en: The trend is database tools evolving from standalone clients to programmable workflows
  and automated dashboards. The entry point is compliance-driven self-built tooling, targeting small teams
  with cross-database query and reporting automation, charging per seat or feature.
priority_review: false
project_type: open_source
industries:
- 软件开发
- 信息技术服务
industries_en:
- Software Development
- IT Services
jobs:
- 数据库管理员
- 后端开发者
jobs_en:
- Database Administrators
- Backend Developers
regions:
- 中国
regions_en:
- China
open_source: true
url: https://flyxl.github.io/datazen/assets/screenshots/01-main-window.png
canonical_url: https://flyxl.github.io/datazen/assets/screenshots/01-main-window.png
summary: "![DataZen 主界面]( https://flyxl.github.io/datazen/assets/screenshots/01-main-window.png)\r\n\r\
  \n写代码十几年了。之前也给孩子们做过几个 Android 小应用，背单词、练口算那种，他们用得还行。\r\n\r\n但那些说到底还是「给别人用」。**DataZen 是我第一次想只为自己做一个软件。**\r\
  \n\r\n起因很现实：公司合规不让装 Navicat 了。DBeaver 能用，但日常用起来总觉得差点意思。正好赶上 vibe coding 这股风，心想不如自己试一把，看能不能做出一个**真正工业级、能天天拿来干活**的数据库客户端。\r\
  \n\r\n不是玩票，也不是 demo 。就是给自己用。\r\n\r\n---\r\n\r\n## 两个具体痛点\r\n\r\n### 1. 查线上问题，经常要串好几张表，还跨库\r\n\r\n处理投诉、排查线上问题，流程大概是这样：\r\
  \n\r\n- 先查表 A ，拿到某个 ID 或状态\r\n- 用这个值去查表 B\r\n- 再查 C 、D……\r\n- 更麻烦的是，这些表往往不在同一个库，没法直接 JOIN\r\n- 只能等上一条\
  \ SQL 跑完，把结果里的字段复制出来，填到下一条 SQL 的 WHERE 里\r\n\r\n一条链路下来，复制粘贴十几次是常态。烦，还容易填错。\r\n\r\n所以做了 **Workflow**：用\
  \ YAML 把多步查询串起来，上一步的结果可以直接传给下一步，不同步骤还可以连不同的库。查一次，整条链路跑完。\r\n\r\n![Workflow 编辑器]( https://flyxl.github.io/datazen/assets/screenshots/04-workflow.png)\r\
  \n\r\n![跨数据库 Workflow]( https://flyxl.github.io/datazen/assets/screenshots/12-workflow-crossdb.png)\r\
  \n\r\n### 2. 老板要数据，要报表\r\n\r\n做开发的都懂。临时要个数字、要张图，经常就是「帮查一下上周 xxx 」「对比一下这个月和上个月」。每次打开客户端、写 SQL 、导出、贴到\
  \ PPT 或飞书里，重复劳动很多。\r\n\r\n所以做了 **运营看板（ Dashboard ）**：把常用 SQL 和图表保存下来，定时刷新，多个指标放在一页。老板要看的时候，打开就行，不用每次重新查。\r\
  \n\r\n![运营看板]( https://flyxl.github.io/datazen/assets/screenshots/21-dashboard.png)\r\n\r\n这两个功能，都是我自己日常真的会用到的东西。不是看竞品有什么就抄什么。\r\
  \n\r\n---\r\n\r\n## 做下来的一些体会\r\n\r\n一路做下来，也踩了不少坑。\r\n\r\n很多功能远看很简单，真正做深才发现不容易。SQL 编辑器、Schema 浏览、大结果集性能、不同数据库方言差异……每个点都能耗掉不少时间。AI\
  \ 相关的能力也做了（自然语言生成 SQL 、错误诊断、EXPLAIN 分析），但对我来说，**Workflow 和 Dashboard 才是最先想解决的**。\r\n\r\n以前总觉得自己还算懂产品，至少比纯写后端的同事更关心体验。做着做着才发现，离「优秀的产品经理」还差得远。中间有好几次，差点去做一些「技术上很酷、但日常用不上」的东西。后来慢慢学会问一句：**这个功能，是不是在解决我自己的真实问题？**\r\
  \n\r\n产品还是要回到用户的痛点上。对我自己来说，就是上面那两件事。\r\n\r\n---\r\n\r\n## DataZen 是什么\r\n\r\n**DataZen** 是一个开源的数据库客户端，Tauri\
  \ + Rust + React ，macOS / Windows / Linux 都能用。\r\n\r\n除了 Workflow 和 Dashboard ，还有这些：\r\n\r\n### 日常查库\r\
  \n\r\n- SQL 编辑器、Schema 树、结果集查看\r\n- 支持 PostgreSQL 、MySQL 、SQLite 、Redis 等，更多数据库通过 Driver 扩展\r\n- SSH\
  \ 隧道，连接信息本地加密存储\r\n\r\n![查询结果与图表]( https://flyxl.github.io/datazen/assets/screenshots/02-query-chart.png)\r\
  \n\r\n### AI 辅助（有，但不是全部）\r\n\r\n- 自然语言生成 SQL ，会带当前库的 Schema\r\n- SQL 报错诊断、EXPLAIN 分析\r\n- 支持 OpenAI\
  \ 、Anthropic 、DeepSeek 和自定义接口\r\n\r\n![AI 自然语言生成 SQL]( https://flyxl.github.io/datazen/assets/screenshots/03-ai-nl2sql.png)\r\
  \n\r\n![AI SQL 错误诊断]( https://flyxl.github.io/datazen/assets/screenshots/05-ai-diagnosis.png)\r\n\r\n\
  ![AI EXPLAIN 分析]( https://flyxl.github.io/datazen/assets/screenshots/06-ai-explain.png)\r\n\r\n### 查询结果转图表\r\
  \n\r\n- 查完直接看图，折线、柱状、饼图等，可导出 PNG/SVG\r\n\r\n![多种图表类型]( https://flyxl.github.io/datazen/assets/screenshots/10-chart-types.png)\r\
  \n\r\n### MCP\r\n\r\n- 可以作为 MCP Server ，把数据库能力暴露给 Cursor 等外部工具\r\n- 也可以接外部 MCP Server 到 AI Chat\r\n\
  - 支持无头 stdio 模式\r\n\r\n### Driver 插件\r\n\r\n- 数据库能力通过 Driver API 扩展，社区可以贡献新数据库支持\r\n\r\n还有 ER 图、Schema\
  \ Diff 、数据同步、导出等，文档里都有。\r\n\r\n![ER 图]( https://flyxl.github.io/datazen/assets/screenshots/16-er.png)\r\
  \n\r\n![Schema Diff]( https://flyxl.github.io/datazen/assets/screenshots/27-schema-diff-en.png)\r\n\r\
  \n### 本地优先，开源免费\r\n\r\n- 不用注册账号\r\n- 连接和凭据留在本机\r\n- GPLv3 开源\r\n\r\n---\r\n\r\n## 还不完美\r\n\r\n说实话，DataZen\
  \ 离「极致好用」还有距离。\r\n\r\n很多功能能用，但还不够顺手。交互细节、边界情况、各数据库的打磨，都需要时间，也需要更多人的使用反馈。\r\n\r\n我一个人做，速度有限。所以开源了——不是因为它已经很好，而是希望有人一起把它做好。\r\
  \n\r\n如果你也天天和数据库打交道，欢迎：\r\n\r\n- GitHub 点个 Star： https://github.com/flyxl/datazen\r\n- 提 Issue 说 bug\
  \ 或体验问题\r\n- 讨论功能方向\r\n- 贡献代码、Driver 、文档\r\n\r\n---\r\n\r\n## 最后\r\n\r\n做一个「只为自己」的软件，听起来挺理想，过程其实挺磨人的。会怀疑值不值得做，会在细节上卡住，也会在产品方向上走弯路。\r\
  \n\r\n但如果有一个你自己每天都会遇到的问题，值得花时间做一个能用的版本出来。先能用，再慢慢改。\r\n\r\n**链接**\r\n\r\n- 项目地址： https://github.com/flyxl/datazen\r\
  \n- 下载： https://github.com/flyxl/datazen/releases\r\n- 中文文档： https://flyxl.github.io/datazen/zh/manual.html\r\
  \n\r\n也想听听大家：**你平时用数据库客户端，最烦的一件事是什么？** 这个对我比任何功能清单都有用。"
first_seen: '2026-08-28T15:55:19Z'
last_seen: '2026-08-29T15:06:00Z'
status: queued
sources:
- v2ex
sightings:
- source: v2ex
  url: https://flyxl.github.io/datazen/assets/screenshots/01-main-window.png
  seen_at: '2026-08-29T15:06:00Z'
  metrics:
    comments: 40
  kind: product
---

# DataZen

![DataZen 主界面]( https://flyxl.github.io/datazen/assets/screenshots/01-main-window.png)

写代码十几年了。之前也给孩子们做过几个 Android 小应用，背单词、练口算那种，他们用得还行。

但那些说到底还是「给别人用」。**DataZen 是我第一次想只为自己做一个软件。**

起因很现实：公司合规不让装 Navicat 了。DBeaver 能用，但日常用起来总觉得差点意思。正好赶上 vibe coding 这股风，心想不如自己试一把，看能不能做出一个**真正工业级、能天天拿来干活**的数据库客户端。

不是玩票，也不是 demo 。就是给自己用。

---

## 两个具体痛点

### 1. 查线上问题，经常要串好几张表，还跨库

处理投诉、排查线上问题，流程大概是这样：

- 先查表 A ，拿到某个 ID 或状态
- 用这个值去查表 B
- 再查 C 、D……
- 更麻烦的是，这些表往往不在同一个库，没法直接 JOIN
- 只能等上一条 SQL 跑完，把结果里的字段复制出来，填到下一条 SQL 的 WHERE 里

一条链路下来，复制粘贴十几次是常态。烦，还容易填错。

所以做了 **Workflow**：用 YAML 把多步查询串起来，上一步的结果可以直接传给下一步，不同步骤还可以连不同的库。查一次，整条链路跑完。

![Workflow 编辑器]( https://flyxl.github.io/datazen/assets/screenshots/04-workflow.png)

![跨数据库 Workflow]( https://flyxl.github.io/datazen/assets/screenshots/12-workflow-crossdb.png)

### 2. 老板要数据，要报表

做开发的都懂。临时要个数字、要张图，经常就是「帮查一下上周 xxx 」「对比一下这个月和上个月」。每次打开客户端、写 SQL 、导出、贴到 PPT 或飞书里，重复劳动很多。

所以做了 **运营看板（ Dashboard ）**：把常用 SQL 和图表保存下来，定时刷新，多个指标放在一页。老板要看的时候，打开就行，不用每次重新查。

![运营看板]( https://flyxl.github.io/datazen/assets/screenshots/21-dashboard.png)

这两个功能，都是我自己日常真的会用到的东西。不是看竞品有什么就抄什么。

---

## 做下来的一些体会

一路做下来，也踩了不少坑。

很多功能远看很简单，真正做深才发现不容易。SQL 编辑器、Schema 浏览、大结果集性能、不同数据库方言差异……每个点都能耗掉不少时间。AI 相关的能力也做了（自然语言生成 SQL 、错误诊断、EXPLAIN 分析），但对我来说，**Workflow 和 Dashboard 才是最先想解决的**。

以前总觉得自己还算懂产品，至少比纯写后端的同事更关心体验。做着做着才发现，离「优秀的产品经理」还差得远。中间有好几次，差点去做一些「技术上很酷、但日常用不上」的东西。后来慢慢学会问一句：**这个功能，是不是在解决我自己的真实问题？**

产品还是要回到用户的痛点上。对我自己来说，就是上面那两件事。

---

## DataZen 是什么

**DataZen** 是一个开源的数据库客户端，Tauri + Rust + React ，macOS / Windows / Linux 都能用。

除了 Workflow 和 Dashboard ，还有这些：

### 日常查库

- SQL 编辑器、Schema 树、结果集查看
- 支持 PostgreSQL 、MySQL 、SQLite 、Redis 等，更多数据库通过 Driver 扩展
- SSH 隧道，连接信息本地加密存储

![查询结果与图表]( https://flyxl.github.io/datazen/assets/screenshots/02-query-chart.png)

### AI 辅助（有，但不是全部）

- 自然语言生成 SQL ，会带当前库的 Schema
- SQL 报错诊断、EXPLAIN 分析
- 支持 OpenAI 、Anthropic 、DeepSeek 和自定义接口

![AI 自然语言生成 SQL]( https://flyxl.github.io/datazen/assets/screenshots/03-ai-nl2sql.png)

![AI SQL 错误诊断]( https://flyxl.github.io/datazen/assets/screenshots/05-ai-diagnosis.png)

![AI EXPLAIN 分析]( https://flyxl.github.io/datazen/assets/screenshots/06-ai-explain.png)

### 查询结果转图表

- 查完直接看图，折线、柱状、饼图等，可导出 PNG/SVG

![多种图表类型]( https://flyxl.github.io/datazen/assets/screenshots/10-chart-types.png)

### MCP

- 可以作为 MCP Server ，把数据库能力暴露给 Cursor 等外部工具
- 也可以接外部 MCP Server 到 AI Chat
- 支持无头 stdio 模式

### Driver 插件

- 数据库能力通过 Driver API 扩展，社区可以贡献新数据库支持

还有 ER 图、Schema Diff 、数据同步、导出等，文档里都有。

![ER 图]( https://flyxl.github.io/datazen/assets/screenshots/16-er.png)

![Schema Diff]( https://flyxl.github.io/datazen/assets/screenshots/27-schema-diff-en.png)

### 本地优先，开源免费

- 不用注册账号
- 连接和凭据留在本机
- GPLv3 开源

---

## 还不完美

说实话，DataZen 离「极致好用」还有距离。

很多功能能用，但还不够顺手。交互细节、边界情况、各数据库的打磨，都需要时间，也需要更多人的使用反馈。

我一个人做，速度有限。所以开源了——不是因为它已经很好，而是希望有人一起把它做好。

如果你也天天和数据库打交道，欢迎：

- GitHub 点个 Star： https://github.com/flyxl/datazen
- 提 Issue 说 bug 或体验问题
- 讨论功能方向
- 贡献代码、Driver 、文档

---

## 最后

做一个「只为自己」的软件，听起来挺理想，过程其实挺磨人的。会怀疑值不值得做，会在细节上卡住，也会在产品方向上走弯路。

但如果有一个你自己每天都会遇到的问题，值得花时间做一个能用的版本出来。先能用，再慢慢改。

**链接**

- 项目地址： https://github.com/flyxl/datazen
- 下载： https://github.com/flyxl/datazen/releases
- 中文文档： https://flyxl.github.io/datazen/zh/manual.html

也想听听大家：**你平时用数据库客户端，最烦的一件事是什么？** 这个对我比任何功能清单都有用。

## 笔记


