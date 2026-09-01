---
slug: claude-ad
name: Claude-AD
builder: ADScanPro
category: AI + 开发
summary_zh: 红队工程师在内部 Active Directory 渗透测试中，将 Claude Code 作为执行引擎，通过技能、代理和斜杠命令驱动 netexec、impacket 等工具，自动执行
  Kerberoasting、ADCS 攻击等手法，并附带 OPSEC 和遥测提示。交付的是可复用的攻击流程和操作指引，但具体输出形式仍待核验。
inspiration: 趋势是 AI 从辅助写代码进入安全攻防的具体操作层，把专家手法编码成可执行流程。切入可从特定攻击链（如 ADCS 证书攻击）的自动化检测与防御验证开始，按每次渗透测试或安全评估收费，而非卖通用工具。
summary_en: Red team engineers use Claude Code as an execution engine during internal Active Directory
  penetration tests, driving tools like netexec and impacket through skills, agents, and slash commands
  to automate techniques such as Kerberoasting and ADCS attacks, with OPSEC and telemetry notes. The deliverable
  is a reusable attack workflow and operational guidance, though the exact output format remains to be
  verified.
inspiration_en: The trend is AI moving from code assistance into specific security operations, encoding
  expert techniques into executable workflows. Entry could focus on automating detection and defense validation
  for specific attack chains like ADCS certificate attacks, charging per penetration test or security
  assessment rather than selling a generic tool.
priority_review: false
project_type: open_source
industries:
- 网络安全
industries_en:
- Cybersecurity
jobs:
- 红队工程师
- 渗透测试员
jobs_en:
- Red team engineer
- Penetration tester
regions: []
regions_en: []
open_source: true
url: https://adscanpro.com
canonical_url: https://adscanpro.com
summary: 'Active Directory pentest methodology for Claude Code: skills, agents and slash commands for
  internal AD red-team work (Kerberoasting, ADCS ESC1-17, DCSync, ACL abuse, NTLM relay, delegation),
  with per-technique OPSEC/telemetry notes. Drives netexec, impacket, certipy, bloodyAD, BloodHound CE.'
first_seen: '2026-08-24T18:13:22Z'
last_seen: '2026-09-01T01:18:14Z'
status: queued
sources:
- github
sightings:
- source: github
  url: https://adscanpro.com
  seen_at: '2026-09-01T01:18:14Z'
  metrics:
    stars: 139
    forks: 23
    open_issues: 0
  kind: product
---

# Claude-AD

Active Directory pentest methodology for Claude Code: skills, agents and slash commands for internal AD red-team work (Kerberoasting, ADCS ESC1-17, DCSync, ACL abuse, NTLM relay, delegation), with per-technique OPSEC/telemetry notes. Drives netexec, impacket, certipy, bloodyAD, BloodHound CE.

## 笔记


