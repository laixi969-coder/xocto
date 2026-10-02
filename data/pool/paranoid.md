---
slug: paranoid
name: paranoid
builder: kulchankas
category: AI + 开发
summary_zh: 开发者在提交上线前，把正在运行的 Web 应用交给这个 agent 技能，它用真实请求尝试入侵自己的应用，为每个漏洞留下可复现的请求证据，再打补丁并重新验证；最终交付是一份带复现请求的漏洞清单和已修补状态，人工仍需确认修复是否可接受。具体支持的框架与交付格式仍待核验。
inspiration: 趋势：安全验证正从“人工写用例、事后扫描”变成“让 agent 真打一遍自己的服务”。切入：从独立开发者和小团队的上线前自检环节进入，按次或按项目卖“可复现的入侵报告”，而不是卖扫描席位；大客户的安全合规流程不是它的入口。
summary_en: Before shipping, a developer points this agent skill at their own running web app; it attempts
  real intrusions, proves each bug with a reproducible request, patches it, and re-verifies. The deliverable
  is a list of bugs with reproduction requests plus patch status, with human sign-off still required.
  Supported frameworks and report formats remain unverified.
inspiration_en: 'Trend: security validation is shifting from hand-written test cases and after-the-fact
  scanning toward letting an agent actually attack your own service. Entry: start with solo developers
  and small teams doing pre-release self-checks, selling a per-run or per-project reproducible intrusion
  report rather than scanner seats; enterprise compliance workflows are not the entry point.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 应用安全测试
jobs_en:
- Application security testing
regions: []
regions_en: []
open_source: true
url: https://github.com/kulchankas/paranoid
canonical_url: https://github.com/kulchankas/paranoid
summary: 'Your app is guilty until proven secure: an agent skill whose /hack-me breaks into your own running
  app, proves each bug with a real request, patches it, and re-verifies. Claude Code · Codex · Cursor.'
first_seen: '2026-09-15T13:53:39Z'
last_seen: '2026-10-02T01:41:55Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/kulchankas/paranoid
  seen_at: '2026-10-02T01:41:55Z'
  metrics:
    stars: 49
    forks: 4
    open_issues: 5
  kind: product
---

# paranoid

Your app is guilty until proven secure: an agent skill whose /hack-me breaks into your own running app, proves each bug with a real request, patches it, and re-verifies. Claude Code · Codex · Cursor.

## 笔记


