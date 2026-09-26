---
slug: sloppy
name: sloppy
builder: Heyosseus
category: AI + 开发
summary_zh: Laravel 后端工程师在合并 AI 编码代理提交的代码前打开它：工具读取 git diff 中的 PHP 代码，按 24 条 Laravel 相关规则做确定性静态检查，并给出
  Rector 与 Pint 的修复结果、Pest 断言和 CI 注解；最终交付是一份可复核的检查与修复清单，是否合并仍由工程师确认。具体规则覆盖范围与修复成功率仍待核验。
inspiration: 趋势是 AI 写代码之后，审查与清理这些代码本身正在变成独立环节，而不是继续塞进编辑器插件。切入可以从特定框架或特定代码库规范入手，把“代理产出后的验收”做成可计价的 CI 环节，按仓库或按检查次数收费，而不是再做一个通用代码助手。
summary_en: 'A Laravel backend engineer opens it before merging code submitted by an AI coding agent:
  it reads PHP code in the git diff, runs deterministic static checks against 24 Laravel-related rules,
  and returns Rector and Pint fixes, Pest expectations and CI annotations; the deliverable is a reviewable
  check-and-fix list, with the merge decision still made by the engineer. Rule coverage and fix success
  rates remain unverified.'
inspiration_en: The trend is that once AI writes code, reviewing and cleaning that code becomes its own
  step rather than another editor plugin. A wedge is to start from one framework or one codebase convention
  and sell post-agent acceptance as a billable CI step, priced per repository or per check, instead of
  building another general coding assistant.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- Laravel 后端工程师在合并 AI 代理提交的代码前，对 diff 做规则化静态检查并自动修复
jobs_en:
- Laravel backend engineers running rule-based static checks and automated fixes on diffs before merging
  AI-agent-generated code
regions: []
regions_en: []
open_source: true
url: https://github.com/Heyosseus/sloppy
canonical_url: https://github.com/Heyosseus/sloppy
summary: Laravel-aware static analysis for the debt AI coding agents leave behind. 24 rules, git-diff
  review, a Rector and Pint fix pass, Pest expectations, CI annotations, agent rulesets and an MCP server.
  Deterministic, local, no LLM.
first_seen: '2026-09-10T07:41:59Z'
last_seen: '2026-09-26T00:37:55Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/Heyosseus/sloppy
  seen_at: '2026-09-26T00:37:55Z'
  metrics:
    stars: 81
    forks: 0
    open_issues: 0
  kind: product
---

# sloppy

Laravel-aware static analysis for the debt AI coding agents leave behind. 24 rules, git-diff review, a Rector and Pint fix pass, Pest expectations, CI annotations, agent rulesets and an MCP server. Deterministic, local, no LLM.

## 笔记


