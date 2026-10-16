---
slug: agent-security
name: agent-security
builder: solongate
category: AI + 开发
summary_zh: 工程团队在让编码代理调用工具前，用它在本机设定工具调用策略、检测密钥泄露并记录代理动作，最终拿到一份可审计的本地操作记录。策略配置的具体流程与拦截效果仍待核验。
inspiration: 趋势：编码代理开始真正动文件和执行命令后，安全边界从代码审查前移到工具调用这一层。切入：面向已有代理工作流的工程团队做本地策略与审计，按团队或按受管代理数收费，而不是做通用代码扫描。
summary_en: Before letting coding agents call tools, engineering teams use this to set tool-call policies
  on-device, detect leaked secrets and log agent actions, ending up with an auditable local record. The
  exact policy setup flow and how well it blocks actions still need verification.
inspiration_en: 'Trend: once coding agents actually touch files and run commands, the security boundary
  moves from code review to the tool-call layer. Entry: sell local policy and audit to engineering teams
  already running agents, charging per team or per managed agent rather than shipping generic code scanning.'
priority_review: false
project_type: open_source
industries:
- 软件开发
- 信息安全
industries_en:
- Software Development
- Information Security
jobs:
- 工程团队在让编码代理执行工具调用前，配置策略并审计其在本机上的动作
jobs_en:
- Engineering teams configuring policies and auditing on-device actions before coding agents make tool
  calls
regions: []
regions_en: []
open_source: true
url: https://solongate.com
canonical_url: https://solongate.com
summary: Local-first, open-source security gateway for AI coding agents. Enforce tool-call policies, detect
  secrets, and audit actions on-device.
first_seen: '2026-10-14T01:14:00Z'
last_seen: '2026-10-16T00:25:17Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://solongate.com
  seen_at: '2026-10-16T00:25:17Z'
  metrics:
    stars: 100
    forks: 13
    open_issues: 0
  kind: product
---

# agent-security

Local-first, open-source security gateway for AI coding agents. Enforce tool-call policies, detect secrets, and audit actions on-device.

## 笔记


