---
slug: github-10
name: zcode-mobile-android
builder: houjinxin
category: AI + 开发
summary_zh: 同时开多台开发机跑编码代理的程序员，原来要在多个窗口或远程桌面之间来回切换，才能看进度、批权限、补指令。这个非官方 Android 客户端扫码绑定多台桌面后，由手机本地起一个群控台网页，PC
  浏览器打开即可把各机器的 ZCode 会话排成单屏、双列或四宫格；用户拿到的是一个多机会话总览页，凭据只存本机，具体稳定性与官方兼容性仍待核验。
inspiration: 趋势是编码代理从单机单会话走向多机并行，管理这些会话本身成了新负担。切入可放在“代理运行看板”这一层：先服务同时维护多台机器的小型开发团队，按机器数或席位向团队收费，而不是再做一个编码代理。
summary_en: Programmers running coding agents on several machines previously had to switch between windows
  or remote desktops to check progress, approve permissions and add instructions. This unofficial Android
  client binds multiple desktops by QR code, serves a control console from the phone, and lets a PC browser
  arrange each machine's ZCode sessions in single, dual or quad layouts; the user gets a multi-machine
  session overview, with credentials kept on the device, while stability and official compatibility remain
  unverified.
inspiration_en: 'The trend is coding agents moving from one machine and one session to many parallel sessions,
  which makes managing them a new burden. The opening is a session dashboard layer: serve small teams
  running several machines first and charge per machine or seat, rather than building another coding agent.'
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- software development
jobs:
- 同时维护多台开发机的程序员在办公室、家中和云主机上并行运行编码代理时，需要在一个界面里查看各会话进度、批准权限并补充指令
jobs_en:
- Programmers running coding agents across several office, home and cloud machines need one view to check
  each session's progress, approve permissions and add instructions
regions: []
regions_en: []
open_source: true
url: https://github.com/woshihoujinxin/zcode-mobile-android
canonical_url: https://github.com/woshihoujinxin/zcode-mobile-android
summary: "四台机器，一个页面，零次切窗。\r\n\r\n我有四台机器在跑 ZCode：公司台式、家里笔记本、云主机、Mac mini。\r\n\r\n以前最烦的不是看不到进度，而是看不过来。每台机器一个窗口，切来切去，上下文全断。想看眼\
  \ e2e、批个权限、补一句 prompt，得先把窗口找出来。\r\n\r\n所以我写了个 Android 客户端。做完才发现，手机扫码只是入口，真正解决问题的是多机聚合：\r\n\r\n手机扫码，一次绑定多台桌面；\r\
  \n手机本地起一个群控台 Web 服务；\r\n同一 Wi-Fi 下，PC 浏览器打开这个地址；\r\n每台机器一个独立会话，单屏 / 双列 / 四宫格随便切；\r\nPC 直连官方云，不经过手机转发。页面不关，就能一直连着多台机器。\r\
  \n现在的日常：早上到公司，四台机器同屏。\r\n\r\n左上：办公室 MacBook 在重构登录模块\r\n右上：家里台式机在跑全量 e2e\r\n左下：云主机在部署 staging\r\n右下：Mac\
  \ mini 在等我看 PR #42\r\n不用 Cmd+Tab，也不用给每台机器开一个远程桌面。它不是远程桌面，只是把官方会话页聚合成一个多机控制台。\r\n\r\n技术实现也很直接：WebView\
  \ 承载官方手机页，扫码或通过深链接绑定，凭据只存本机，https + 官方域名白名单 + sid/hash 校验；群控台本质上就是把凭据下发给浏览器，让 PC 自己连官方云。\r\n\r\n手机端本身也能单独扫码接管，通勤、出门、躺床上都能看进度、批权限、补\
  \ prompt。\r\n\r\n适合同时开多台开发机、多环境跑 Agent 的人；只有一台机器的话，手机端扫码接管也够用。\r\n\r\n非官方客户端，Android 8.0+，APK 5.7 MB，直接装。debug\
  \ 签名，内测/自用没问题，别拿去上架。 代码在 GitHub / Gitee，欢迎 Issue / PR。\r\n\r\nGitHub： https://github.com/woshihoujinxin/zcode-mobile-android\
  \ \r\nGitee： https://gitee.com/houjinxin/zcode-mobile-android\r\n\r\n最近 GLM 降智严重，大家可以在本地配置好别的模型，推荐 DS"
first_seen: '2026-10-20T01:06:24Z'
last_seen: '2026-10-20T01:06:24Z'
status: watching
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/woshihoujinxin/zcode-mobile-android
  seen_at: '2026-10-20T01:06:24Z'
  metrics:
    comments: 2
  kind: product
---

# zcode-mobile-android

四台机器，一个页面，零次切窗。

我有四台机器在跑 ZCode：公司台式、家里笔记本、云主机、Mac mini。

以前最烦的不是看不到进度，而是看不过来。每台机器一个窗口，切来切去，上下文全断。想看眼 e2e、批个权限、补一句 prompt，得先把窗口找出来。

所以我写了个 Android 客户端。做完才发现，手机扫码只是入口，真正解决问题的是多机聚合：

手机扫码，一次绑定多台桌面；
手机本地起一个群控台 Web 服务；
同一 Wi-Fi 下，PC 浏览器打开这个地址；
每台机器一个独立会话，单屏 / 双列 / 四宫格随便切；
PC 直连官方云，不经过手机转发。页面不关，就能一直连着多台机器。
现在的日常：早上到公司，四台机器同屏。

左上：办公室 MacBook 在重构登录模块
右上：家里台式机在跑全量 e2e
左下：云主机在部署 staging
右下：Mac mini 在等我看 PR #42
不用 Cmd+Tab，也不用给每台机器开一个远程桌面。它不是远程桌面，只是把官方会话页聚合成一个多机控制台。

技术实现也很直接：WebView 承载官方手机页，扫码或通过深链接绑定，凭据只存本机，https + 官方域名白名单 + sid/hash 校验；群控台本质上就是把凭据下发给浏览器，让 PC 自己连官方云。

手机端本身也能单独扫码接管，通勤、出门、躺床上都能看进度、批权限、补 prompt。

适合同时开多台开发机、多环境跑 Agent 的人；只有一台机器的话，手机端扫码接管也够用。

非官方客户端，Android 8.0+，APK 5.7 MB，直接装。debug 签名，内测/自用没问题，别拿去上架。 代码在 GitHub / Gitee，欢迎 Issue / PR。

GitHub： https://github.com/woshihoujinxin/zcode-mobile-android 
Gitee： https://gitee.com/houjinxin/zcode-mobile-android

最近 GLM 降智严重，大家可以在本地配置好别的模型，推荐 DS

## 笔记


