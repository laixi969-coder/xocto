---
slug: jevgrep
name: jevgrep
builder: dzhng
category: AI + 开发
summary_zh: 工程师在维护不熟悉的代码库时，需要先找到与某个行为相关的文件，再让编码智能体动手改。jevgrep 是一个命令行工具，让使用者用“这段代码做什么”的描述去检索相关文件与源码上下文，返回带行号的源码片段，也可通过
  MCP 接入编码智能体。用户拿到的是候选文件与精确代码位置，是否采纳仍需人工判断。
inspiration: 趋势是编码智能体的瓶颈从“写代码”前移到“找对上下文”，谁掌握检索层谁就影响改动的准确率。切入可放在大型遗留代码库的迁移与接手场景，按仓库或按次检索收费，或作为企业内代码检索的私有部署；目前只有开源仓库，尚无商业路径证据。
summary_en: Engineers taking over unfamiliar codebases must first locate the files tied to a behavior
  before a coding agent can change them. jevgrep is a command-line tool that lets users search by describing
  what code does, returning relevant files and source excerpts with line numbers, and can also be reached
  by coding agents over MCP. The deliverable is candidate files and exact code locations; adoption still
  needs human judgment.
inspiration_en: The trend is that the bottleneck for coding agents has moved from writing code to finding
  the right context, so whoever owns retrieval shapes how accurate the edits are. The opening is migration
  and handover work on large legacy repositories, sold per repository or per search, or as a privately
  deployed internal code search; today there is only an open-source repository and no evidence of a commercial
  path.
priority_review: false
project_type: open_source
industries:
- 软件与信息技术服务
industries_en:
- Software and IT services
jobs:
- 软件工程师
- 编码智能体使用者
jobs_en:
- Software engineers
- Coding agent users
regions: []
regions_en: []
open_source: true
url: https://github.com/dzhng/jevgrep
canonical_url: https://github.com/dzhng/jevgrep
summary: Find code by asking what it does. A CLI for coding agents that uses Jev to discover relevant
  files and source context.
first_seen: '2026-09-26T04:06:56Z'
last_seen: '2026-10-09T02:10:18Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/dzhng/jevgrep
  seen_at: '2026-10-09T02:10:18Z'
  metrics:
    stars: 2470
    forks: 178
    open_issues: 25
  kind: product
- source: github
  url: https://github.com/nassim-arifette/jevgrep
  seen_at: '2026-10-09T02:10:18Z'
  metrics:
    stars: 102
    forks: 11
    open_issues: 1
  kind: product
---

# jevgrep

Find code by asking what it does. A CLI for coding agents that uses Jev to discover relevant files and source context.

## 笔记


