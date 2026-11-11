---
slug: github-22
name: Github
builder: soleilune
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
url: https://github.com/AnalyseDeCircuit/oxideterm
canonical_url: https://github.com/AnalyseDeCircuit/oxideterm
summary: "大家好，我是 OxideTerm 的作者。https://github.com/AnalyseDeCircuit/oxideterm\r\n\r\n7 月底我在这里[发过一帖]( https://www.v2ex.com/t/1229777)，介绍了将\
  \ OxideTerm 从 WebView 迁移到 Rust + GPUI 的过程。我也希望借鉴 WindTerm 等知名 SSH 客户端和终端的一些好用设计，继续打磨这个免费开源、功能丰富（ SSH\
  \ ，Mosh ，Serial ，Telnet ，RDP ，VNC ，BLE 等）的原生 SSH 客户端。\r\n\r\n\r\n原生版持续迭代了近四个月，兼容性和日常交互一直在完善，目前已经比较稳定了。从当时的\
  \ 2.0.11 到前几天发布的 2.3.1 ，我们还花了不少精力打磨终端的基本功：吞吐、绘制和历史存储，希望持续追赶 WindTerm 、Ghostty 、Alacritty 等成熟终端的表现。\r\
  \n\r\n![OxideTerm 工作区]( https://analysedecircuit.github.io/oxideterm-media/screenshots/2.3.1/workspace-docker-framed.png)\r\
  \n\r\n既然说要让终端飞起来，那就拿实际输出比划比划。\r\n\r\n## 刷日志的时候，让终端速度跟上\r\n\r\n跑构建、看大量诊断信息时，数据已经到了本机，如果终端却还在慢慢处理，眼前的内容就会落后；想滚动回看、切换会话，界面线程又忙着解析输出。我们想减少的，就是终端自己带来的这部分等待。\r\
  \n\r\n下面是 8 月早期发布构建与现在 2.3.1 的吞吐测试记录对比。每类负载输出 **16 MiB**，预热一次，测量三次取中位数，具体[测试方法]( https://github.com/AnalyseDeCircuit/oxideterm/blob/v2.3.1/benchmark/README.md)在仓库里。\r\
  \n\r\n![OxideTerm 终端吞吐对比]( https://analysedecircuit.github.io/oxideterm-media/benchmarks/2.3.1/throughput.png)\r\
  \n\r\n\r\n\r\n**其实这背后没有什么黑魔法**，就是反复测试、找瓶颈：把 SSH 终端解析放到后台线程，批量处理文本和网格写入，减少重复扫描与内存复制，绘制时复用没有变化的文字排版。大量输出的时候，少做一点重复工作，就能给界面操作多留一些余地。\r\
  \n\r\n## 日志想多留一点？内存就要省着用！\r\n\r\n上次去掉 WebView ，这次则深入到了历史存储。像 [xterm.js 的缓冲区]( https://github.com/xtermjs/xterm.js/blob/master/src/common/buffer/BufferLine.ts)，内容和属性逐字符格保存，整行同色也仍然逐格保留属性。我们则把历史文本和样式分开紧凑保存，让相邻的同样式文字共享记录。\r\
  \n\r\n在 10 月这轮分阶段存储改造中，保留 20,000 行历史、400 列，另含 40 行屏幕，伪随机 ASCII 满行时，终端与解析器的保留堆从 196.47 MB 降到 15.50 MB\
  \ ，**减少 92.1%。**\r\n\r\n![OxideTerm 终端历史存储内存对比]( https://analysedecircuit.github.io/oxideterm-media/benchmarks/2.3.1/history-memory.png)\r\
  \n\r\n这是我们自己的终端内核改造前后的结果，[完整记录]( https://github.com/AnalyseDeCircuit/oxideterm/blob/v2.3.1/docs/development/performance-and-benchmarking.md)里有具体条件。\r\
  \n\r\n**落到日常使用，就是多留些日志、多挂几个会话时，少挤占浏览器、IDE 和容器的内存。赶上这轮内存涨价，终端能省一些，肯定是个好事情。**\r\n\r\n## 新增功能与改进\r\n\r\n\
  我们在这三四个月内也更新了很多别的功能，这里仅仅挑出来一些和大家分享：\r\n\r\n- **WindTerm 用户熟悉的本地语义着色**：远端输出没带颜色，也能初步识别一些内容，轻松辨别数字、unix\
  \ 权限等。\r\n- **类 WindTerm 的 Free Type Mode**：用鼠标定位和选择当前命令，支持复制、剪切和拖动文字，改长命令不用一直按方向键。\r\n- **SFTP 侧边栏与拖拽上传**：侧边栏可以跟随活动\
  \ SSH 主机，也可以固定。把本地文件拖进 SSH 终端，就能上传到它的当前目录。\r\n- **向外部 AI 开放的 MCP 接口**：让 Codex 等常用 AI 客户端，经授权使用连接、终端、文件和主机工具，少一点复制粘贴，权限随时可撤销。\r\
  \n- **壁纸功能大拓展**：图片、GIF 、视频和粒子效果都支持，模糊、透明度和阅读遮罩可以调整，还能开启输入时暂停动效，简约和华丽随你选择。\r\n- **最多 16 窗格混合工作区**：终端、SFTP\
  \ 、IDE 、设置乃至插件页面都能混排，本机和不同服务器自由组合，拖拽布局不用重连。\r\n- **原生插件系统**：通过应用内市场，按需安装语言高亮、RDP ／ VNC ／ Mosh 等扩展，插件可以独立更新。\r\
  \n- X11 转发、BLE 连接模式、Kerberos 认证方式、审计系统、个人运维知识库（支持 Markdown 编辑和预览）……\r\n\r\n比如下面这样，把 SSH 、本地终端、笔记和 SFTP\
  \ 放进同一个标签页：\r\n\r\n![OxideTerm 四窗格混合工作区]( https://analysedecircuit.github.io/oxideterm-media/screenshots/2.3.1/mixed-workspace-framed.png)\r\
  \n\r\n## 写在最后\r\n\r\n**玉不琢不成器，感谢这几个月以来热心帮助的朋友们。**OxideTerm 目前依然是 GPL-3.0 的开源自由软件，免费，没有账号和订阅门槛，也不收集遥测数据。欢迎试试现在的\
  \ 2.3.1 ，之前用过早期版本的朋友也欢迎回来看看。觉得顺手可以点个 Star ，有问题或建议，欢迎提 Issue 、PR ，希望它能越来越实用。最近也开了个交流群，欢迎来聊使用体验和改进建议。\r\
  \n\r\n**感谢大家！**"
first_seen: '2026-11-11T01:56:49Z'
last_seen: '2026-11-11T01:56:49Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/AnalyseDeCircuit/oxideterm
  seen_at: '2026-11-11T01:56:49Z'
  metrics:
    comments: 4
  kind: product
---

# Github

大家好，我是 OxideTerm 的作者。https://github.com/AnalyseDeCircuit/oxideterm

7 月底我在这里[发过一帖]( https://www.v2ex.com/t/1229777)，介绍了将 OxideTerm 从 WebView 迁移到 Rust + GPUI 的过程。我也希望借鉴 WindTerm 等知名 SSH 客户端和终端的一些好用设计，继续打磨这个免费开源、功能丰富（ SSH ，Mosh ，Serial ，Telnet ，RDP ，VNC ，BLE 等）的原生 SSH 客户端。


原生版持续迭代了近四个月，兼容性和日常交互一直在完善，目前已经比较稳定了。从当时的 2.0.11 到前几天发布的 2.3.1 ，我们还花了不少精力打磨终端的基本功：吞吐、绘制和历史存储，希望持续追赶 WindTerm 、Ghostty 、Alacritty 等成熟终端的表现。

![OxideTerm 工作区]( https://analysedecircuit.github.io/oxideterm-media/screenshots/2.3.1/workspace-docker-framed.png)

既然说要让终端飞起来，那就拿实际输出比划比划。

## 刷日志的时候，让终端速度跟上

跑构建、看大量诊断信息时，数据已经到了本机，如果终端却还在慢慢处理，眼前的内容就会落后；想滚动回看、切换会话，界面线程又忙着解析输出。我们想减少的，就是终端自己带来的这部分等待。

下面是 8 月早期发布构建与现在 2.3.1 的吞吐测试记录对比。每类负载输出 **16 MiB**，预热一次，测量三次取中位数，具体[测试方法]( https://github.com/AnalyseDeCircuit/oxideterm/blob/v2.3.1/benchmark/README.md)在仓库里。

![OxideTerm 终端吞吐对比]( https://analysedecircuit.github.io/oxideterm-media/benchmarks/2.3.1/throughput.png)



**其实这背后没有什么黑魔法**，就是反复测试、找瓶颈：把 SSH 终端解析放到后台线程，批量处理文本和网格写入，减少重复扫描与内存复制，绘制时复用没有变化的文字排版。大量输出的时候，少做一点重复工作，就能给界面操作多留一些余地。

## 日志想多留一点？内存就要省着用！

上次去掉 WebView ，这次则深入到了历史存储。像 [xterm.js 的缓冲区]( https://github.com/xtermjs/xterm.js/blob/master/src/common/buffer/BufferLine.ts)，内容和属性逐字符格保存，整行同色也仍然逐格保留属性。我们则把历史文本和样式分开紧凑保存，让相邻的同样式文字共享记录。

在 10 月这轮分阶段存储改造中，保留 20,000 行历史、400 列，另含 40 行屏幕，伪随机 ASCII 满行时，终端与解析器的保留堆从 196.47 MB 降到 15.50 MB ，**减少 92.1%。**

![OxideTerm 终端历史存储内存对比]( https://analysedecircuit.github.io/oxideterm-media/benchmarks/2.3.1/history-memory.png)

这是我们自己的终端内核改造前后的结果，[完整记录]( https://github.com/AnalyseDeCircuit/oxideterm/blob/v2.3.1/docs/development/performance-and-benchmarking.md)里有具体条件。

**落到日常使用，就是多留些日志、多挂几个会话时，少挤占浏览器、IDE 和容器的内存。赶上这轮内存涨价，终端能省一些，肯定是个好事情。**

## 新增功能与改进

我们在这三四个月内也更新了很多别的功能，这里仅仅挑出来一些和大家分享：

- **WindTerm 用户熟悉的本地语义着色**：远端输出没带颜色，也能初步识别一些内容，轻松辨别数字、unix 权限等。
- **类 WindTerm 的 Free Type Mode**：用鼠标定位和选择当前命令，支持复制、剪切和拖动文字，改长命令不用一直按方向键。
- **SFTP 侧边栏与拖拽上传**：侧边栏可以跟随活动 SSH 主机，也可以固定。把本地文件拖进 SSH 终端，就能上传到它的当前目录。
- **向外部 AI 开放的 MCP 接口**：让 Codex 等常用 AI 客户端，经授权使用连接、终端、文件和主机工具，少一点复制粘贴，权限随时可撤销。
- **壁纸功能大拓展**：图片、GIF 、视频和粒子效果都支持，模糊、透明度和阅读遮罩可以调整，还能开启输入时暂停动效，简约和华丽随你选择。
- **最多 16 窗格混合工作区**：终端、SFTP 、IDE 、设置乃至插件页面都能混排，本机和不同服务器自由组合，拖拽布局不用重连。
- **原生插件系统**：通过应用内市场，按需安装语言高亮、RDP ／ VNC ／ Mosh 等扩展，插件可以独立更新。
- X11 转发、BLE 连接模式、Kerberos 认证方式、审计系统、个人运维知识库（支持 Markdown 编辑和预览）……

比如下面这样，把 SSH 、本地终端、笔记和 SFTP 放进同一个标签页：

![OxideTerm 四窗格混合工作区]( https://analysedecircuit.github.io/oxideterm-media/screenshots/2.3.1/mixed-workspace-framed.png)

## 写在最后

**玉不琢不成器，感谢这几个月以来热心帮助的朋友们。**OxideTerm 目前依然是 GPL-3.0 的开源自由软件，免费，没有账号和订阅门槛，也不收集遥测数据。欢迎试试现在的 2.3.1 ，之前用过早期版本的朋友也欢迎回来看看。觉得顺手可以点个 Star ，有问题或建议，欢迎提 Issue 、PR ，希望它能越来越实用。最近也开了个交流群，欢迎来聊使用体验和改进建议。

**感谢大家！**

## 笔记


