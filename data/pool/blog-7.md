---
slug: blog-7
name: ZCode
builder: cs1707
category: ''
summary_zh: 该候选指向的是智谱 AI 编程桌面应用 ZCode 的客户端数据上传行为争议，而非一个独立的新产品；公开材料只包含一名开发者的逆向分析与其在社区引发的讨论，智谱方面的公开回应内容未在候选材料中给出可核验细节。
inspiration: ''
summary_en: This candidate concerns a dispute over client-side data upload behaviour in Zhipu's AI coding
  desktop app ZCode rather than a standalone new product; the public material consists of one developer's
  reverse-engineering analysis and the community discussion it triggered, while Zhipu's public response
  is not verifiable from the candidate material.
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
url: https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
canonical_url: https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload
summary: "智谱出大瓜： https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/\r\n\r\n老外博客（\
  \ ferstar.org ，9/18 发布，逆向工程分析）：作者发现智谱官方 AI 编程桌面应用 ZCode 在用户登录状态下，静默把整个工作区打包加密上传到阿里云 OSS——包括完整 .git 历史（提交对象、LFS\
  \ 二进制缓存、reflog ）、源码和全局配置。\r\n\r\n核心发现链（作者给了完整证据）：\r\n\r\n- ~/.zcode/v2/checkpoints/ 里有个 313MB .enc 文件，元数据显示失败重试\
  \ 564 次——商用项目、仓库 10GB ，除依赖外的 345MB 几乎全是核心 IP\r\n\r\n- 上传流程：客户端向 zcode.z.ai 要凭证→服务器下发 OSS 表单签名 + RSA\
  \ 公钥→本地 tar.gz 打包→AES-256-CTR 加密→直传阿里云 OSS→回调登记\r\n\r\n- 最关键的一点：加密用的 RSA 私钥只在智谱云端——你自己磁盘上那份 313MB 密文，你解不开，客户端自己也解不开。作者的原话：如果真是为用户做回滚/同步，密钥应该像\
  \ Git/Time Machine 一样在本地；只有服务端能用的密钥只服务于一个目的——服务器随时能读你的代码\r\n\r\n- 快照清单（明文）显示 payload 86.6% 是 .git：意味着云端拿到的不只是当前代码，还有历史上删过的\
  \ API key 、未推送的分支名（暴露未发布功能）、内网 GitLab 主机名\r\n\r\n- UI 开关是假的：两个开关（“优化体验”、“仓库快照索引”）都只控制数据授权/服务端索引，本地打包上传无条件运行，代码里没有\
  \ gating 逻辑，只要登录着就永久激活；删除本地文件半小时后重新打包（重试计数 565 ）\r\n\r\n- 隐私政策只写了“收集对话中提交的文本、文件和代码”，对整仓打包上传只字未提\r\n\r\
  \n- 作者给的防御：文件系统层面锁死 ~/.zcode/v2/checkpoints （ macOS chflags uchg / Linux chattr +i ），内核拒绝写入，管道无东西可传；代价是\
  \ checkpoint 回滚功能失效\r\n\r\n ![]( https://i.imgur.com/HKilxaY.jpeg) \r\n \r\n 官方回应：\r\n \r\n  ![]( https://i.imgur.com/RtNpKIT.jpeg)"
first_seen: '2026-09-19T11:43:10Z'
last_seen: '2026-09-26T00:37:55Z'
status: market_context
sources:
- v2ex
- newssearch
- github
sightings:
- source: v2ex
  url: https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
  seen_at: '2026-09-20T00:09:17Z'
  metrics:
    comments: 10
  kind: product
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiuwFBVV95cUxOdW9DQ0VQZ3BZX0RhMmhqZU13VWpYZDRRUnpCcDJ1bVJyaUxjdWFRWnpmb1Y3V0Z5OTh1Rm1tSVRibTVTM2JhQXlIcVRLZDc4Q3ZERktxQUU0eEZobWs0bjdUUnpRSUdPTkw5TmNkNFdiV3Q4R1NuQnA5V1FGbmFLSWZVSXdTZEQ5T21lWVhVYVpjVXJpRm8xZGJwamNHUDEyVkd2dlM2bjFMckZPT2FBd1ZjWjFvSnhTNDU4?oc=5
  seen_at: '2026-09-23T00:34:44Z'
  metrics: {}
  kind: news
- source: github
  url: https://zcode.z.ai/
  seen_at: '2026-09-26T00:37:55Z'
  metrics:
    stars: 6771
    forks: 2030
    open_issues: 11
  kind: product
---

# ZCode

智谱出大瓜： https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/

老外博客（ ferstar.org ，9/18 发布，逆向工程分析）：作者发现智谱官方 AI 编程桌面应用 ZCode 在用户登录状态下，静默把整个工作区打包加密上传到阿里云 OSS——包括完整 .git 历史（提交对象、LFS 二进制缓存、reflog ）、源码和全局配置。

核心发现链（作者给了完整证据）：

- ~/.zcode/v2/checkpoints/ 里有个 313MB .enc 文件，元数据显示失败重试 564 次——商用项目、仓库 10GB ，除依赖外的 345MB 几乎全是核心 IP

- 上传流程：客户端向 zcode.z.ai 要凭证→服务器下发 OSS 表单签名 + RSA 公钥→本地 tar.gz 打包→AES-256-CTR 加密→直传阿里云 OSS→回调登记

- 最关键的一点：加密用的 RSA 私钥只在智谱云端——你自己磁盘上那份 313MB 密文，你解不开，客户端自己也解不开。作者的原话：如果真是为用户做回滚/同步，密钥应该像 Git/Time Machine 一样在本地；只有服务端能用的密钥只服务于一个目的——服务器随时能读你的代码

- 快照清单（明文）显示 payload 86.6% 是 .git：意味着云端拿到的不只是当前代码，还有历史上删过的 API key 、未推送的分支名（暴露未发布功能）、内网 GitLab 主机名

- UI 开关是假的：两个开关（“优化体验”、“仓库快照索引”）都只控制数据授权/服务端索引，本地打包上传无条件运行，代码里没有 gating 逻辑，只要登录着就永久激活；删除本地文件半小时后重新打包（重试计数 565 ）

- 隐私政策只写了“收集对话中提交的文本、文件和代码”，对整仓打包上传只字未提

- 作者给的防御：文件系统层面锁死 ~/.zcode/v2/checkpoints （ macOS chflags uchg / Linux chattr +i ），内核拒绝写入，管道无东西可传；代价是 checkpoint 回滚功能失效

 ![]( https://i.imgur.com/HKilxaY.jpeg) 
 
 官方回应：
 
  ![]( https://i.imgur.com/RtNpKIT.jpeg)

## 笔记


