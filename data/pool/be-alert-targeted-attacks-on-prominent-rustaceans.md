---
slug: be-alert-targeted-attacks-on-prominent-rustaceans
name: crates.io
builder: ''
category: ''
summary_zh: 2026年9月，Rust 生态安全团队警告存在针对 rust-lang 成员及热门 crate 维护者的持续攻击活动：攻击者以求职、项目或合同机会为由安排视频通话，诱导目标安装伪装成音频编解码器的程序或执行剪贴板中的命令，上月已借此对
  arrayref 等 crate 实施成功的供应链攻击。这意味着依赖开源组件的 AI 应用在交付链上新增了人为攻击面，采用依赖冷却期等延迟升级策略成为降低风险的现实手段。
inspiration: ''
summary_en: 'In September 2026 the Rust ecosystem security team warned of an ongoing campaign targeting
  rust-lang members and maintainers of popular crates: attackers set up video calls framed as job, project
  or contract opportunities, then trick targets into installing a purported audio codec or executing a
  clipboard command; last month this led to a successful supply chain attack on arrayref and others. This
  adds a human attack surface to the delivery chain of AI applications that depend on open source, making
  dependency cooldowns and delayed upgrades a practical risk-reduction measure.'
inspiration_en: ''
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: false
url: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
canonical_url: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans
summary: "Be alert: targeted attacks on prominent Rustaceans   \nImportant warning from Adam Harvey and\
  \ the crates security team: \n \n We believe that there is an ongoing campaign targeting rust-lang members\
  \ and owners of popular crates that is attempting to compromise devices and accounts in order to use\
  \ them to publish malware. \n A video call is set up for something positive — maybe for a job, maybe\
  \ for a project, maybe for a contract opportunity — and then that's used as a vector to either get the\
  \ target to install something on their computer (such as a purportedly missing audio codec) or execute\
  \ another command (for example, via putting a command on the clipboard). \n \n Last month this trick\
  \ was used in a successful  supply chain attack against the array ref crate , among others. \n Any piece\
  \ of software that depends on open source (which is almost  every  piece of software) has a network\
  \ of human beings who are potential attack vectors - everyone with publishing rights to any of the packages\
  \ in the dependency network for that software. \n I guess our best defense right now is  dependency\
  \ cooldowns  - giving new package releases a few days before upgrading to them, in the hope that supply\
  \ chain attacks like this will be spotted by someone else.\n\n\n     Tags:  open-source ,  security\
  \ ,  rust ,  supply-chain ,  dependency-cooldowns"
first_seen: '2026-09-17T23:59:19Z'
last_seen: '2026-09-18T00:20:10Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
  seen_at: '2026-09-18T00:20:10Z'
  metrics: {}
  kind: news
---

# crates.io

Be alert: targeted attacks on prominent Rustaceans   
Important warning from Adam Harvey and the crates security team: 
 
 We believe that there is an ongoing campaign targeting rust-lang members and owners of popular crates that is attempting to compromise devices and accounts in order to use them to publish malware. 
 A video call is set up for something positive — maybe for a job, maybe for a project, maybe for a contract opportunity — and then that's used as a vector to either get the target to install something on their computer (such as a purportedly missing audio codec) or execute another command (for example, via putting a command on the clipboard). 
 
 Last month this trick was used in a successful  supply chain attack against the array ref crate , among others. 
 Any piece of software that depends on open source (which is almost  every  piece of software) has a network of human beings who are potential attack vectors - everyone with publishing rights to any of the packages in the dependency network for that software. 
 I guess our best defense right now is  dependency cooldowns  - giving new package releases a few days before upgrading to them, in the hope that supply chain attacks like this will be spotted by someone else.


     Tags:  open-source ,  security ,  rust ,  supply-chain ,  dependency-cooldowns

## 笔记


