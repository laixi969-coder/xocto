---
slug: github-12
name: Github
builder: jonny6015
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
url: https://github.com/astralwaveorg/lyra
canonical_url: https://github.com/astralwaveorg/lyra
summary: "项目地址： https://github.com/astralwaveorg/lyra\r\n文档： https://github.com/astralwaveorg/lyra/tree/main/docs\r\
  \n镜像：ghcr.io/astralwaveorg/lyra:1.0.0\r\n\r\nLyra 是一个自托管的音乐库维护工具。它不下载音乐，也不接管播放，只维护你已有的本地文件。\r\n\r\n\
  **它主要做四件事**\r\n\r\n- **歌词**：从 QQ 音乐、网易云音乐、LRCLIB 抓取，写入内嵌歌词和同名 `.lrc`；已有有效歌词默认跳过；支持逐行对比、批量采纳和撤销。\r\n\
  - **标签**：按 MusicBrainz 补齐缺失字段，逐字段显示本地值、来源值和冲突；冲突不会自动覆盖；缺 MBID 或候选有歧义时可以用 AcoustID 指纹兜底。\r\n- **整理**：按\
  \ `艺人 / 专辑 / 音轨号 - 曲名` 生成路径；目录可多选，也可以多选排除；所有移动先预览，目标存在不覆盖，移动后为空的目录可以清理，支持批量撤销。\r\n- **重复音频**：按“音频完全一致\
  \ / 同一录音 / 标题、艺人、时长相近”分类；只检测，不自动删除；删除进入回收站，可以撤销。\r\n\r\n**为什么做这个**\r\n\r\n我的曲库在 NAS 上攒了很多年，标签和歌词状态很乱。试过一些工具，最大的顾虑是一键写入之后不知道改了什么，冲突被直接覆盖，出错也退不回去。\r\
  \n\r\n所以 Lyra 的原则是：\r\n\r\n- 写入前备份，只改目标字段，失败自动回滚；\r\n- 所有移动先给出新旧路径，确认后才执行；\r\n- 删除是移入回收站，不是直接抹掉；\r\n\
  - 重复音频只列出来，删不删由人决定。\r\n- 当然尽可能自动处理，引入 AI 决策能力（我个人使用 MiniMax ）\r\n\r\n**界面**（测试曲库）\r\n\r\n![概览]( https://raw.githubusercontent.com/astralwaveorg/lyra/main/docs/assets/screenshots/overview.png)\r\
  \n\r\n![重复音频分类]( https://raw.githubusercontent.com/astralwaveorg/lyra/main/docs/assets/screenshots/dedupe.png)\r\
  \n\r\n`http://127.0.0.1:8080`。用户名 `admin`，首次启动的随机密码在 `data/initial-password.txt`，登录后先改密码。\r\n\r\n**目前的限制**\r\
  \n\r\n- 版本是 v1.0.0 ，主要在我自己的曲库上验证，边界情况还需要更多样本。\r\n- 支持 FLAC 、MP3 、OGG Vorbis 、Opus ； OGG / Opus 的封面写入还没做。\r\
  \n- QQ 音乐和网易云的可用性受地区、网络影响； MusicBrainz 公共 API 每秒最多一次请求，大库建议自建镜像。\r\n- 单管理员，没有多用户权限（似乎也不需要）。\r\n- 不会自动整理目录，也不会自动删除重复音频（手动处理，自动风险太高）。\r\
  \n\r\n**想听听大家的反馈**\r\n\r\n- 部署有没有卡住或者什么问题\r\n- 歌词或标签匹配有没有明显误判；\r\n- 重复音频的分类是否合理，有没有把不该删的放进待删除；\r\n-\
  \ 移动端布局、文档和错误提示是否清楚。\r\n\r\n回帖或提 Issue 都行。附上版本、部署方式和错误日志即可，记得去掉密码、Token 和私人路径。\r\n\r\n项目刚发布，欢迎试用。\r\n\
  \r\n觉得有用的话点个 Star 就好。"
first_seen: '2026-10-20T01:06:24Z'
last_seen: '2026-10-20T01:06:24Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/astralwaveorg/lyra
  seen_at: '2026-10-20T01:06:24Z'
  metrics:
    comments: 1
  kind: product
---

# Github

项目地址： https://github.com/astralwaveorg/lyra
文档： https://github.com/astralwaveorg/lyra/tree/main/docs
镜像：ghcr.io/astralwaveorg/lyra:1.0.0

Lyra 是一个自托管的音乐库维护工具。它不下载音乐，也不接管播放，只维护你已有的本地文件。

**它主要做四件事**

- **歌词**：从 QQ 音乐、网易云音乐、LRCLIB 抓取，写入内嵌歌词和同名 `.lrc`；已有有效歌词默认跳过；支持逐行对比、批量采纳和撤销。
- **标签**：按 MusicBrainz 补齐缺失字段，逐字段显示本地值、来源值和冲突；冲突不会自动覆盖；缺 MBID 或候选有歧义时可以用 AcoustID 指纹兜底。
- **整理**：按 `艺人 / 专辑 / 音轨号 - 曲名` 生成路径；目录可多选，也可以多选排除；所有移动先预览，目标存在不覆盖，移动后为空的目录可以清理，支持批量撤销。
- **重复音频**：按“音频完全一致 / 同一录音 / 标题、艺人、时长相近”分类；只检测，不自动删除；删除进入回收站，可以撤销。

**为什么做这个**

我的曲库在 NAS 上攒了很多年，标签和歌词状态很乱。试过一些工具，最大的顾虑是一键写入之后不知道改了什么，冲突被直接覆盖，出错也退不回去。

所以 Lyra 的原则是：

- 写入前备份，只改目标字段，失败自动回滚；
- 所有移动先给出新旧路径，确认后才执行；
- 删除是移入回收站，不是直接抹掉；
- 重复音频只列出来，删不删由人决定。
- 当然尽可能自动处理，引入 AI 决策能力（我个人使用 MiniMax ）

**界面**（测试曲库）

![概览]( https://raw.githubusercontent.com/astralwaveorg/lyra/main/docs/assets/screenshots/overview.png)

![重复音频分类]( https://raw.githubusercontent.com/astralwaveorg/lyra/main/docs/assets/screenshots/dedupe.png)

`http://127.0.0.1:8080`。用户名 `admin`，首次启动的随机密码在 `data/initial-password.txt`，登录后先改密码。

**目前的限制**

- 版本是 v1.0.0 ，主要在我自己的曲库上验证，边界情况还需要更多样本。
- 支持 FLAC 、MP3 、OGG Vorbis 、Opus ； OGG / Opus 的封面写入还没做。
- QQ 音乐和网易云的可用性受地区、网络影响； MusicBrainz 公共 API 每秒最多一次请求，大库建议自建镜像。
- 单管理员，没有多用户权限（似乎也不需要）。
- 不会自动整理目录，也不会自动删除重复音频（手动处理，自动风险太高）。

**想听听大家的反馈**

- 部署有没有卡住或者什么问题
- 歌词或标签匹配有没有明显误判；
- 重复音频的分类是否合理，有没有把不该删的放进待删除；
- 移动端布局、文档和错误提示是否清楚。

回帖或提 Issue 都行。附上版本、部署方式和错误日志即可，记得去掉密码、Token 和私人路径。

项目刚发布，欢迎试用。

觉得有用的话点个 Star 就好。

## 笔记


