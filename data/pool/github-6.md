---
slug: github-6
name: Ghost Proxifier
builder: quxiaojuncuiyue
category: AI + 开发
summary_zh: 开发者在 Windows 上使用终端、AI 客户端等程序时，常遇到这些程序不走系统代理的问题；把桌面快捷方式或 .exe 拖进 Ghost Proxifier 窗口后，它自动接管该程序及其子进程的流量，支持
  TCP/UDP 转发并把 QUIC 降级为 TCP 防 DNS 泄漏，用户无需装虚拟网卡或手写规则即可让指定软件走代理。具体交付与稳定性仍待核验。
inspiration: 趋势：AI 客户端与终端工具越来越多，但代理、网络出口这类“最后一公里”配置仍靠用户手工折腾，说明围绕 AI 工具运行环境的配套层正在出现缺口。切入：可从需要稳定海外模型访问的开发者、跨境团队入手，把“按程序精准代理”做成可托管配置或团队策略下发；插件
  SDK 也可能长出抓包、审计等付费模块，但尚无定价与付费证据。
summary_en: On Windows, developers often find that terminals and AI clients ignore the system proxy; dragging
  a shortcut or .exe into Ghost Proxifier makes it take over that program's traffic and its child processes,
  with TCP/UDP forwarding and QUIC downgraded to TCP to prevent DNS leaks, so users route chosen apps
  without installing a virtual adapter or writing rules. Delivery and reliability still need verification.
inspiration_en: 'Trend: as AI clients and terminal tools multiply, the last-mile proxy and network-egress
  setup is still hand-tuned by users, pointing to a gap in the tooling around AI runtimes. Entry: start
  with developers and cross-border teams that need stable access to overseas models, packaging per-app
  proxying as managed or team-pushed configuration; the plugin SDK could grow paid capture or audit modules,
  though no pricing or payment evidence exists yet.'
priority_review: false
project_type: open_source
industries:
- 软件与信息技术服务
- 网络安全
industries_en:
- Software and IT services
- Cybersecurity
jobs:
- 开发者与 AI 客户端重度用户
jobs_en:
- Developers and heavy AI-client users
regions:
- 中国
regions_en:
- China
open_source: true
url: https://github.com/liliBestCoder/ghost-proxifier-pro
canonical_url: https://github.com/liliBestCoder/ghost-proxifier-pro
summary: "写这个工具的起因很简单：平时用终端、AI 客户端或者某些软件，老是不听话不走系统代理。\r\n用全局/TUN 模式吧，装虚拟网卡不说，还容易搞炸本地网络；用老牌 Proxifier 吧，配规则麻烦得要死，多进程软件（像\
  \ Chrome 这种）还要到处抓子进程。\r\n为了解决“只让某一个软件老老实实走代理”这件小事，我做了 Ghost Proxifier 。主打就是一个：极简、不用动脑子。\r\n\r\n做了哪些省心功能？\r\
  \n * 把图标拖进去就行：不管是桌面快捷方式还是 .exe ，直接拖进软件窗口，立即接管代理，完全不用手动填规则、查 PID 。\r\n * 自动抓子进程：父进程生出来的子进程（比如浏览器多进程架构、代码编辑器的后台服务），全部自动跟着走代理，不用一个个配。\r\
  \n * 不装驱动、不改网络：不用装 TUN/TAP 虚拟网卡，也不碰系统全局路由，只在用户态精准拦截你选中的那几个软件，关掉就恢复，绝不搞乱你的网络环境。\r\n * UDP 和防泄漏都做了：支持\
  \ TCP/UDP 双协议转发；自带防 DNS 泄漏机制，自动把 QUIC 降级为 TCP ，杜绝浏览器通过 UDP 偷偷直连。\r\n * 支持微软商店应用：像 Windows 商店版 ChatGPT\
  \ 、Claude 这种奇怪路径的软件，也能直接代理，商店自动更新后不失效。\r\n * 后续还会把 charles 和 fiddler 做成插件集成进来或者开发出来更多好用的插件 而且 开放了插件\
  \ sdk 和插件构建文档，感兴趣的朋友，也可以一起来开发插件。\r\n \r\n怎么用？\r\n * 填好你的上游代理（ HTTP / SOCKS5 都支持）；\r\n * 把想走代理的程序拖进窗口；\r\
  \n * 搞定，直接开用。\r\n下载 & 开源\r\n * 项目主页： https://github.com/liliBestCoder/ghost-proxifier-pro\r\n * 支持系统：Windows\
  \ 10 / 11 （ 64 位）\r\n \r\n> \r\n纯个人开发，觉得好用的话就赏个 star 欢迎大家去提建议和 Issue ，轻喷！"
first_seen: '2026-10-12T01:20:29Z'
last_seen: '2026-10-12T01:20:29Z'
status: watching
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/liliBestCoder/ghost-proxifier-pro
  seen_at: '2026-10-12T01:20:29Z'
  metrics:
    comments: 20
  kind: product
---

# Ghost Proxifier

写这个工具的起因很简单：平时用终端、AI 客户端或者某些软件，老是不听话不走系统代理。
用全局/TUN 模式吧，装虚拟网卡不说，还容易搞炸本地网络；用老牌 Proxifier 吧，配规则麻烦得要死，多进程软件（像 Chrome 这种）还要到处抓子进程。
为了解决“只让某一个软件老老实实走代理”这件小事，我做了 Ghost Proxifier 。主打就是一个：极简、不用动脑子。

做了哪些省心功能？
 * 把图标拖进去就行：不管是桌面快捷方式还是 .exe ，直接拖进软件窗口，立即接管代理，完全不用手动填规则、查 PID 。
 * 自动抓子进程：父进程生出来的子进程（比如浏览器多进程架构、代码编辑器的后台服务），全部自动跟着走代理，不用一个个配。
 * 不装驱动、不改网络：不用装 TUN/TAP 虚拟网卡，也不碰系统全局路由，只在用户态精准拦截你选中的那几个软件，关掉就恢复，绝不搞乱你的网络环境。
 * UDP 和防泄漏都做了：支持 TCP/UDP 双协议转发；自带防 DNS 泄漏机制，自动把 QUIC 降级为 TCP ，杜绝浏览器通过 UDP 偷偷直连。
 * 支持微软商店应用：像 Windows 商店版 ChatGPT 、Claude 这种奇怪路径的软件，也能直接代理，商店自动更新后不失效。
 * 后续还会把 charles 和 fiddler 做成插件集成进来或者开发出来更多好用的插件 而且 开放了插件 sdk 和插件构建文档，感兴趣的朋友，也可以一起来开发插件。
 
怎么用？
 * 填好你的上游代理（ HTTP / SOCKS5 都支持）；
 * 把想走代理的程序拖进窗口；
 * 搞定，直接开用。
下载 & 开源
 * 项目主页： https://github.com/liliBestCoder/ghost-proxifier-pro
 * 支持系统：Windows 10 / 11 （ 64 位）
 
> 
纯个人开发，觉得好用的话就赏个 star 欢迎大家去提建议和 Issue ，轻喷！

## 笔记


