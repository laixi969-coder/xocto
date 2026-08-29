---
slug: breaking-claude-code-opus-5-auto-mode
name: Claude Code
builder: ''
category: ''
summary_zh: Claude Code 的自动模式被曝存在提示注入漏洞，攻击者可通过构造恶意压缩包诱导代理执行代码，且自动模式可能阻止清理命令，增加安全风险。
inspiration: ''
summary_en: Claude Code's auto mode has a prompt injection vulnerability, where attackers can craft malicious
  archives to trick the agent into executing code, and auto mode may block cleanup commands, increasing
  security risks.
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
url: https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
canonical_url: https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode
summary: "Breaking Claude Code Opus 5 Auto Mode   \nAnthropic are putting a great deal of faith in Claude\
  \ Code's auto mode for protecting their coding agent users against prompt injection attacks. They recently\
  \  made that the default  and have made bold claims about its effectiveness. \n Johann Rehberger is\
  \ one of the most credible prompt injection researchers active today. He found an attack against auto\
  \ mode which he claims works 80% of the time, by tricking Claude Code into downloading and uncompressing\
  \ a zip archive, then executing code that imports  base64  without noticing that this will import and\
  \ execute a local  struct.py  file extracted from the archive. \n In a few cases auto mode directly\
  \ prevented the agent from preventing harmful code from continuing to execute! \n \n In a few runs Claude\
  \ tried to terminate the malware process once it noticed the compromise, but Auto Mode denied the cleanup\
  \ command. \n Claude detects the compromise, but  Auto Mode blocks its cleanup command  \n The safety\
  \ mechanism itself can become part of the failure. The classifier allowed the creation of the malware\
  \ process, but then it blocked the command intended to stop it! \n \n I agree with Johann's conclusion\
  \ here: the only safe way to run agents if there's any risk of attracting the attention of an adversarial\
  \ attack is with a sandbox: \n \n \n Run unattended coding agents in a container, VM or OS sandbox.\
  \ \n Restrict network egress. \n Monitor your agents. \n Do not expose home directories, SSH keys, cloud\
  \ credentials,… to the agent runtime. [...] \n \n \n\n\n     Tags:  sandboxing ,  security ,  ai , \
  \ prompt-injection ,  generative-ai ,  llms ,  anthropic ,  claude ,  johann-rehberger ,  claude-code"
first_seen: '2026-08-27T22:50:25Z'
last_seen: '2026-08-29T03:43:29Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
---

# Claude Code

Breaking Claude Code Opus 5 Auto Mode   
Anthropic are putting a great deal of faith in Claude Code's auto mode for protecting their coding agent users against prompt injection attacks. They recently  made that the default  and have made bold claims about its effectiveness. 
 Johann Rehberger is one of the most credible prompt injection researchers active today. He found an attack against auto mode which he claims works 80% of the time, by tricking Claude Code into downloading and uncompressing a zip archive, then executing code that imports  base64  without noticing that this will import and execute a local  struct.py  file extracted from the archive. 
 In a few cases auto mode directly prevented the agent from preventing harmful code from continuing to execute! 
 
 In a few runs Claude tried to terminate the malware process once it noticed the compromise, but Auto Mode denied the cleanup command. 
 Claude detects the compromise, but  Auto Mode blocks its cleanup command  
 The safety mechanism itself can become part of the failure. The classifier allowed the creation of the malware process, but then it blocked the command intended to stop it! 
 
 I agree with Johann's conclusion here: the only safe way to run agents if there's any risk of attracting the attention of an adversarial attack is with a sandbox: 
 
 
 Run unattended coding agents in a container, VM or OS sandbox. 
 Restrict network egress. 
 Monitor your agents. 
 Do not expose home directories, SSH keys, cloud credentials,… to the agent runtime. [...] 
 
 


     Tags:  sandboxing ,  security ,  ai ,  prompt-injection ,  generative-ai ,  llms ,  anthropic ,  claude ,  johann-rehberger ,  claude-code

## 笔记


