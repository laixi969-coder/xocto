---
slug: quoting-felix-rieseberg
name: Claude Cowork
builder: ''
category: ''
summary_zh: 这是 Anthropic 对 Claude Cowork 运行架构的一次调整，不是新产品发布。旧版本在云端做模型推理、把虚拟机下发到用户电脑执行工具调用，用户抱怨占磁盘、耗电、影响性能，且合上笔记本工作就中断；新版本把推理和虚拟机都移到云端，每个会话独立沙箱，需要读取用户设备文件时由桌面应用完成该次访问调用。
inspiration: ''
summary_en: This is an architecture change to Anthropic's Claude Cowork rather than a new product. The
  old version ran model inference in the cloud but shipped a VM to the user's computer to execute tool
  calls, which users disliked for disk, battery and performance cost, and because closing the laptop stopped
  the work; the new version runs both inference and the VM in the cloud, gives each session its own sandbox,
  and lets the desktop app handle device file access when needed.
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
url: https://simonwillison.net/2026/Oct/5/felix-rieseberg/
canonical_url: https://simonwillison.net/2026/Oct/5/felix-rieseberg
summary: "The \"old\" version of Cowork runs model inference in the cloud, executing tool calls in an\
  \ Anthropic-provided VM we shipped to your computer. We added the VM for capability, safety, and security\
  \ reasons - mapping in just the data you explicitly added to your session. People loved what they were\
  \ able to do with Claude but didn't love the disk, battery, and performance cost of running the VM locally.\
  \ Also, people didn't love that closing your laptop means the work stops. \n The \"new\" version of\
  \ Cowork runs model inference and the VM in the cloud. Each session gets its own sandbox, not sharing\
  \ state with other sessions. When the VM needs something on the users' device (like a file), the desktop\
  \ app is responsible for that file access tool call. [...] \n We think this solves a lot of problems\
  \ we've heard about  (like using Cowork from a phone, keeping work running, or getting all the same\
  \ power without losing battery to the VM)  \n —  Felix Rieseberg , Anthropic, see also  this help page\
  \  \n\n     Tags:  claude-cowork ,  anthropic ,  claude ,  generative-ai ,  ai ,  general-agents , \
  \ llms"
first_seen: '2026-10-05T23:56:47Z'
last_seen: '2026-10-06T02:19:01Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/5/felix-rieseberg/
  seen_at: '2026-10-06T02:19:01Z'
  metrics: {}
  kind: news
---

# Claude Cowork

The "old" version of Cowork runs model inference in the cloud, executing tool calls in an Anthropic-provided VM we shipped to your computer. We added the VM for capability, safety, and security reasons - mapping in just the data you explicitly added to your session. People loved what they were able to do with Claude but didn't love the disk, battery, and performance cost of running the VM locally. Also, people didn't love that closing your laptop means the work stops. 
 The "new" version of Cowork runs model inference and the VM in the cloud. Each session gets its own sandbox, not sharing state with other sessions. When the VM needs something on the users' device (like a file), the desktop app is responsible for that file access tool call. [...] 
 We think this solves a lot of problems we've heard about  (like using Cowork from a phone, keeping work running, or getting all the same power without losing battery to the VM)  
 —  Felix Rieseberg , Anthropic, see also  this help page  

     Tags:  claude-cowork ,  anthropic ,  claude ,  generative-ai ,  ai ,  general-agents ,  llms

## 笔记


