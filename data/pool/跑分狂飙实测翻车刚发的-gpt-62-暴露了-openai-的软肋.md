---
slug: 跑分狂飙实测翻车刚发的-gpt-62-暴露了-openai-的软肋
name: 跑分狂飙，实测翻车，刚发的 GPT-6.2 暴露了 OpenAI 的软肋
builder: ''
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
url: http://www.geekpark.net/news/374175
canonical_url: https://geekpark.net/news/374175
summary: 作者｜Techno 之王 编辑｜靖宇 「 基本不可用，不推荐 」。 OpenAI 新模型上线仅仅 8 分钟，硅谷知名创业者 Matt Shumer，就在社交平台上扔下一句毫不留情的评价。
  紧接着，拥有大批开发者拥趸的 Theo Browne，发了一篇长文《我为什么讨厌 GPT-6.2 Astra》。向来对前沿模型保持温和耐心的沃顿商学院教授 Ethan Mollick，测完后也给出了罕见的严厉定调，「非常不稳定且古怪」，直言这是「自
  GPT-4.5 以来 OpenAI 前沿发布首次未见明显进步」。 这原本该是 OpenAI 是一场漂亮的反击战。 北京时间 11 月 18 日凌晨，OpenAI 正式推出新一代旗舰 GPT-6.2 Astra
  与日常主力 GPT-6.2 Sol。官方把 Astra 的 API 单价直接砍掉 20%，还交出了一张从智能体到科研全面刷新纪录的成绩单。 当纸面跑分的狂飙撞上一线开发者的集体吐槽，这种极致的割裂感，恰恰揭开了
  OpenAI 当下最真实的窘境。 01 文字游戏和算力暗箭 单看官方海报和第三方综合榜单的头部数据，GPT-6.2 两款模型确实很能打。 两款模型均配备 105 万上下文窗口，输入上限 92.2 万
  tokens，输出上限 12.8 万 tokens，目前仅支持文本与图像输入、纯文本输出，不支持音视频和微调。定价上，接替 9 月初 GPT-6 Astra 的新版旗舰定在每百万输入 8 美元、输出
  40 美元， 缓存输入更是大砍六成至 0.40 美元 ；接替 9 月 DevDay 版本的 GPT-6.2 Sol 维持输入 2 美元、输出 10 美元不变。 在 Artificial Analysis
  的 v5.0.1 综合指数榜上，GPT-6.2 Astra 以 62 分跃居总榜第二，仅次于 65 分的 Claude Fable 5.2，反超了 60 分的 Gemini 4 Carbon 和 59
  分的 Claude Opus 5.5。 更诱人的是单任务成本， Astra 平均开销仅 4 美元，只有 Fable 5.2 高达 26.54 美元成本的 15% 。拿下 57 分的 Sol 单任务仅花
  1.01 美元，在帕累托前沿散点图上稳稳落入左上角的高性价比象限。 Artificial Analysis Intelligence Index v5.0.1 总分榜与单任务成本帕累托前沿对比｜图片来源：Artificial
  Analysis 但只要顺着官方博客往下翻，仔细去读那些字号极小的脚注，味道就开始变了 。 在 Agents' Last Exam 测试中，OpenAI 高调宣布 Astra 跑出最高 78.3%（XHigh
  档，Max 档为 77.6%）的成绩，领先 Fable 5.2 的 72.8% 一大截。脚注里却悄悄写着，这份对比排除了 Fable 5.2 使用后备模型的 9 个任务。更微妙的是， 官方配图里 Google
  的 Gemini 4 Carbon 在高推理模式下拿到了 77.4%，单任务成本 4.60 美元 ，与 Astra 的 4.47 美元几乎打平，但官方正文对这位对手只字未提。 除了跑分口径的精妙筛选，API
  定价表里还埋着两颗暗雷。 只要单次输入超过 27.2 万 tokens，整笔请求的输入和缓存单价就会翻倍，输出单价乘以 1.5 倍，Astra 直接涨到 16 美元和 60 美元。同时，仅限美区数据驻留、最高提速
  4.5 倍的 Ultrafast 模式目前按 3 倍促销， 但从 2027 年 3 月 1 日起将翻倍至 6 倍，届时
first_seen: '2026-11-19T03:28:38Z'
last_seen: '2026-11-19T03:28:38Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: http://www.geekpark.net/news/374175
  seen_at: '2026-11-19T03:28:38Z'
  metrics: {}
  kind: news
---

# 跑分狂飙，实测翻车，刚发的 GPT-6.2 暴露了 OpenAI 的软肋

作者｜Techno 之王 编辑｜靖宇 「 基本不可用，不推荐 」。 OpenAI 新模型上线仅仅 8 分钟，硅谷知名创业者 Matt Shumer，就在社交平台上扔下一句毫不留情的评价。 紧接着，拥有大批开发者拥趸的 Theo Browne，发了一篇长文《我为什么讨厌 GPT-6.2 Astra》。向来对前沿模型保持温和耐心的沃顿商学院教授 Ethan Mollick，测完后也给出了罕见的严厉定调，「非常不稳定且古怪」，直言这是「自 GPT-4.5 以来 OpenAI 前沿发布首次未见明显进步」。 这原本该是 OpenAI 是一场漂亮的反击战。 北京时间 11 月 18 日凌晨，OpenAI 正式推出新一代旗舰 GPT-6.2 Astra 与日常主力 GPT-6.2 Sol。官方把 Astra 的 API 单价直接砍掉 20%，还交出了一张从智能体到科研全面刷新纪录的成绩单。 当纸面跑分的狂飙撞上一线开发者的集体吐槽，这种极致的割裂感，恰恰揭开了 OpenAI 当下最真实的窘境。 01 文字游戏和算力暗箭 单看官方海报和第三方综合榜单的头部数据，GPT-6.2 两款模型确实很能打。 两款模型均配备 105 万上下文窗口，输入上限 92.2 万 tokens，输出上限 12.8 万 tokens，目前仅支持文本与图像输入、纯文本输出，不支持音视频和微调。定价上，接替 9 月初 GPT-6 Astra 的新版旗舰定在每百万输入 8 美元、输出 40 美元， 缓存输入更是大砍六成至 0.40 美元 ；接替 9 月 DevDay 版本的 GPT-6.2 Sol 维持输入 2 美元、输出 10 美元不变。 在 Artificial Analysis 的 v5.0.1 综合指数榜上，GPT-6.2 Astra 以 62 分跃居总榜第二，仅次于 65 分的 Claude Fable 5.2，反超了 60 分的 Gemini 4 Carbon 和 59 分的 Claude Opus 5.5。 更诱人的是单任务成本， Astra 平均开销仅 4 美元，只有 Fable 5.2 高达 26.54 美元成本的 15% 。拿下 57 分的 Sol 单任务仅花 1.01 美元，在帕累托前沿散点图上稳稳落入左上角的高性价比象限。 Artificial Analysis Intelligence Index v5.0.1 总分榜与单任务成本帕累托前沿对比｜图片来源：Artificial Analysis 但只要顺着官方博客往下翻，仔细去读那些字号极小的脚注，味道就开始变了 。 在 Agents' Last Exam 测试中，OpenAI 高调宣布 Astra 跑出最高 78.3%（XHigh 档，Max 档为 77.6%）的成绩，领先 Fable 5.2 的 72.8% 一大截。脚注里却悄悄写着，这份对比排除了 Fable 5.2 使用后备模型的 9 个任务。更微妙的是， 官方配图里 Google 的 Gemini 4 Carbon 在高推理模式下拿到了 77.4%，单任务成本 4.60 美元 ，与 Astra 的 4.47 美元几乎打平，但官方正文对这位对手只字未提。 除了跑分口径的精妙筛选，API 定价表里还埋着两颗暗雷。 只要单次输入超过 27.2 万 tokens，整笔请求的输入和缓存单价就会翻倍，输出单价乘以 1.5 倍，Astra 直接涨到 16 美元和 60 美元。同时，仅限美区数据驻留、最高提速 4.5 倍的 Ultrafast 模式目前按 3 倍促销， 但从 2027 年 3 月 1 日起将翻倍至 6 倍，届时

## 笔记


