---
slug: first-pass
name: first-pass
builder: joetawil7
category: AI + 开发
summary_zh: 使用 Claude Code 写代码的工程师，在提交改动前打开这套规则集：它让模型先回答十个关于改动影响范围的问题，再由一个未参与编写的审查角色复核，并要求给出完成证据后才算结束。用户拿到的是被约束过的改动流程和审查记录，最终是否合并仍由人确认；具体交付形态与执行细节仍待核验。
inspiration: 趋势是编码代理的产出速度已经超过人工审查速度，瓶颈从写代码挪到“谁来复核”。切入不在再造一个编码助手，而是给已经用上代理的团队做审查与放行环节的规则层：从受监管行业或外包交付团队切入，把“改动影响范围”和“完成证据”做成可留档的交付物，按团队或按项目收费。
summary_en: 'Engineers using Claude Code open this rule set before committing a change: it makes the model
  answer ten questions about the blast radius of the edit, then has a reviewer that did not write the
  code check it, and requires proof before the work is called done. The user gets a constrained change
  process and a review trail, while the final merge decision stays human; the exact delivery format and
  enforcement details still need verification.'
inspiration_en: 'The trend is that coding agents now produce changes faster than humans can review them,
  so the bottleneck moves from writing code to who signs off. The opening is not another coding assistant
  but a rules layer for the review and release step inside teams already using agents: start with regulated
  industries or outsourced delivery teams, turn blast-radius and proof-of-done into auditable artifacts,
  and charge per team or per project.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 软件工程师
jobs_en:
- Software engineers
regions: []
regions_en: []
open_source: true
url: https://github.com/joetawil7/first-pass
canonical_url: https://github.com/joetawil7/first-pass
summary: 'Rules and checks that make Claude Code look around a change, not just at the lines it writes:
  ten questions before code, a reviewer that didn''t write it, proof before done, bugs fixed as a class.'
first_seen: '2026-09-25T15:45:56Z'
last_seen: '2026-10-06T02:18:35Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/joetawil7/first-pass
  seen_at: '2026-10-06T02:18:35Z'
  metrics:
    stars: 109
    forks: 1
    open_issues: 0
  kind: product
---

# first-pass

Rules and checks that make Claude Code look around a change, not just at the lines it writes: ten questions before code, a reviewer that didn't write it, proof before done, bugs fixed as a class.

## 笔记


