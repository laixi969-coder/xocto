---
slug: livediff
name: livediff
builder: stagas
category: AI + 开发
summary_zh: 开发者在把改代码的活交给编码代理后，需要盯着代理到底动了哪些文件。livediff 是一个命令行工具，在终端里持续刷新当前仓库的 Git 差异，把代理写入的改动实时显示出来，用户据此判断是否要中断或回退；它只呈现差异，不替用户做取舍，是否保留改动仍由人确认。
inspiration: 趋势是编码代理开始批量改文件，人从写代码转向审代码，审的对象从一次提交变成持续流动的改动。切入可以放在“代理改动的可观测与可回退”这一环：面向把代理接进真实仓库的团队，做改动留痕、越权写入拦截和回滚，而不是再做一个代理本身。
summary_en: After handing code changes to a coding agent, developers need to see which files it actually
  touched. livediff is a command-line tool that continuously refreshes the Git diff of the current repository
  in the terminal, showing the agent's edits as they happen so the user can decide whether to interrupt
  or revert; it only surfaces the diff and leaves the keep-or-discard call to a human.
inspiration_en: 'The trend is that coding agents now edit files in bulk, so people shift from writing
  code to reviewing a continuous stream of changes rather than a single commit. A wedge sits in observability
  and reversibility of agent edits: for teams wiring agents into real repositories, offer change trails,
  blocking of out-of-scope writes and rollback, instead of building yet another agent.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 开发者在让编码代理批量改代码时，实时查看工作区里被改动的文件与差异
jobs_en:
- Developers monitoring which files and diffs an autonomous coding agent is changing in the working tree
regions: []
regions_en: []
open_source: true
url: https://github.com/stagas/livediff
canonical_url: https://github.com/stagas/livediff
summary: A live Git diff view cli to stay on top of what agents are doing
first_seen: '2026-09-15T13:37:25Z'
last_seen: '2026-09-16T00:20:36Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/stagas/livediff
  seen_at: '2026-09-16T00:20:36Z'
  metrics:
    points: 6
    comments: 2
  kind: product
---

# livediff

A live Git diff view cli to stay on top of what agents are doing

## 笔记


