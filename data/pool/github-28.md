---
slug: github-28
name: Github
builder: hicohuang
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
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
url: https://github.com/hongqi7/Anti-Claude
canonical_url: https://github.com/hongqi7/Anti-Claude
summary: "最近哈吉米新模型下饺子，Claude 又被封了，Neon 差不多能平替 Opus，但是哈吉米封反代就查的很严，不得不把日常主力切到反重力桌面端，但客户端有两个地方一直用不太惯。\r\n\
  \r\n一个是执行过程太黑盒。客户端默认把推理藏在折叠块里，连续调十几个工具也一声不吭，跑完直接收进一个 `Worked for Xm` 外框（知识工作模式下跑完连工具记录都会清掉），中途很难看清它查到了哪一步。另一个是常用控件太散，模型菜单平铺一长串，界面上也看不到当前会话的上下文占了多少。\r\
  \n\r\n以前用惯了 Claude Desktop 和 Claude Code 的交互节奏，这两天自己动手做了一套免改包的改造工具 **Anti-Claude**：\r\n\r\nhttps://github.com/hongqi7/Anti-Claude\r\
  \n\r\n主要做了这几块改动：\r\n\r\n1. **边做边汇报 + 流内 `TodoWrite` 进度卡**\r\n通过全局协作规则配合前端流式解析，让 Agent 每次调工具前先用一两句话交代刚查到什么、下一步准备干嘛，同时拆掉回合末的外层二次折叠，给执行中的工具行加上实时读秒。遇到\
  \ 3 步以上的多阶段任务，消息流里会渲染一张跟随滚动的圆角 `TodoWrite` 进度卡，全部做完自动消失，不再往正文里反复刷 Markdown 清单。\r\n\r\n2. **上下文圆环与分层模型菜单**\r\
  \n把平铺的模型列表收成 5 个常用主力（支持数字键 `1-5` 切换），思考档位拆进二级菜单。模型按钮旁加了上下文占用圆环，点开能看 5 小时和每周配额余量，也能一键触发 `/compact`。底栏保留了\
  \ `tok/s · TTFT`，鼠标悬停能看缓存命中率与分项耗时。\r\n\r\n3. **Claude 风格侧边栏与「项目」工作台**\r\n把原本拆成两块的会话树合并成统一的「最近对话」混排列表，点消息撤回时直接在原气泡内展开编辑框重发。侧栏加了类似\
  \ Claude Desktop 的三级 `Projects` 工作台（带项目卡片墙、本地 `AGENTS.md` 项目指令与参考文件），技能页也补上了原生缺失的新建技能和新建子 Agent 向导。\r\
  \n\r\n4. **顺带适配了 `agy` 终端状态栏**\r\n如果本机装了 Antigravity CLI（`agy`），安装时会自动配上一条零依赖的 Claude Code 风格底部状态栏，把当前模型和上下文进度条放在一行里，顺带显示\
  \ Git 分支与运行状态。平时只用终端的话，传 `--cli-only` 就能在 macOS / Linux / Windows 下单独装这一层。\r\n\r\n很多人关心改客户端会不会破签名或者一升级就失效。Anti-Claude\
  \ 全程走本地零依赖 CDP 注入加用户目录配置，完全不碰 `/Applications/Antigravity.app` 包体，系统签名原封不动。后台配了 LaunchAgent 自动重挂，已经兼容\
  \ `v2.33+` 移除默认调试端口的改动，客户端升级后会自动重新接上。\r\n\r\n界面默认保留英文原版，需要中文汉化或微调苹方字高（`94.5% / 95% / 100%`），进 `Settings\
  \ → UI Enhancements` 里随时单独开关，不用重启。不想用了跑一行 `uninstall` 就能干净还原。\r\n\r\n安装需要 macOS 和 Node.js >= 22：\r\n\
  \r\n```bash\r\ngit clone https://github.com/hongqi7/Anti-Claude.git ~/Developer/Anti-Claude\r\nnode\
  \ ~/Developer/Anti-Claude/install.mjs install\r\n```\r\n\r\n懒得敲命令的话，直接把 `帮我安装 https://github.com/hongqi7/Anti-Claude`\
  \ 发给 Antigravity 或 Claude Code 让它自己装也行，装完当前窗口直接热生效。\r\n\r\n仓库 README 里放了实机截图，同在用 Antigravity 的老哥欢迎试试，有\
  \ bug 或建议直接提 Issue。\r\n````<!-- todo:done -->"
first_seen: '2026-11-21T03:13:46Z'
last_seen: '2026-11-21T03:13:46Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/hongqi7/Anti-Claude
  seen_at: '2026-11-21T03:13:46Z'
  metrics:
    comments: 12
  kind: product
---

# Github

最近哈吉米新模型下饺子，Claude 又被封了，Neon 差不多能平替 Opus，但是哈吉米封反代就查的很严，不得不把日常主力切到反重力桌面端，但客户端有两个地方一直用不太惯。

一个是执行过程太黑盒。客户端默认把推理藏在折叠块里，连续调十几个工具也一声不吭，跑完直接收进一个 `Worked for Xm` 外框（知识工作模式下跑完连工具记录都会清掉），中途很难看清它查到了哪一步。另一个是常用控件太散，模型菜单平铺一长串，界面上也看不到当前会话的上下文占了多少。

以前用惯了 Claude Desktop 和 Claude Code 的交互节奏，这两天自己动手做了一套免改包的改造工具 **Anti-Claude**：

https://github.com/hongqi7/Anti-Claude

主要做了这几块改动：

1. **边做边汇报 + 流内 `TodoWrite` 进度卡**
通过全局协作规则配合前端流式解析，让 Agent 每次调工具前先用一两句话交代刚查到什么、下一步准备干嘛，同时拆掉回合末的外层二次折叠，给执行中的工具行加上实时读秒。遇到 3 步以上的多阶段任务，消息流里会渲染一张跟随滚动的圆角 `TodoWrite` 进度卡，全部做完自动消失，不再往正文里反复刷 Markdown 清单。

2. **上下文圆环与分层模型菜单**
把平铺的模型列表收成 5 个常用主力（支持数字键 `1-5` 切换），思考档位拆进二级菜单。模型按钮旁加了上下文占用圆环，点开能看 5 小时和每周配额余量，也能一键触发 `/compact`。底栏保留了 `tok/s · TTFT`，鼠标悬停能看缓存命中率与分项耗时。

3. **Claude 风格侧边栏与「项目」工作台**
把原本拆成两块的会话树合并成统一的「最近对话」混排列表，点消息撤回时直接在原气泡内展开编辑框重发。侧栏加了类似 Claude Desktop 的三级 `Projects` 工作台（带项目卡片墙、本地 `AGENTS.md` 项目指令与参考文件），技能页也补上了原生缺失的新建技能和新建子 Agent 向导。

4. **顺带适配了 `agy` 终端状态栏**
如果本机装了 Antigravity CLI（`agy`），安装时会自动配上一条零依赖的 Claude Code 风格底部状态栏，把当前模型和上下文进度条放在一行里，顺带显示 Git 分支与运行状态。平时只用终端的话，传 `--cli-only` 就能在 macOS / Linux / Windows 下单独装这一层。

很多人关心改客户端会不会破签名或者一升级就失效。Anti-Claude 全程走本地零依赖 CDP 注入加用户目录配置，完全不碰 `/Applications/Antigravity.app` 包体，系统签名原封不动。后台配了 LaunchAgent 自动重挂，已经兼容 `v2.33+` 移除默认调试端口的改动，客户端升级后会自动重新接上。

界面默认保留英文原版，需要中文汉化或微调苹方字高（`94.5% / 95% / 100%`），进 `Settings → UI Enhancements` 里随时单独开关，不用重启。不想用了跑一行 `uninstall` 就能干净还原。

安装需要 macOS 和 Node.js >= 22：

```bash
git clone https://github.com/hongqi7/Anti-Claude.git ~/Developer/Anti-Claude
node ~/Developer/Anti-Claude/install.mjs install
```

懒得敲命令的话，直接把 `帮我安装 https://github.com/hongqi7/Anti-Claude` 发给 Antigravity 或 Claude Code 让它自己装也行，装完当前窗口直接热生效。

仓库 README 里放了实机截图，同在用 Antigravity 的老哥欢迎试试，有 bug 或建议直接提 Issue。
````<!-- todo:done -->

## 笔记


