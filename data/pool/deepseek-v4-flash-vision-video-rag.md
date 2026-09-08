---
slug: deepseek-v4-flash-vision-video-rag
name: deepseek-v4-flash-vision-video-rag
builder: liangdabiao
category: AI + 创作
summary_zh: 这是一个基于 DeepSeek 视觉模型的视频理解与问答 agent skill。用户上传视频后，它按时间轴抽帧建立索引，对问题做本地粗筛、视觉精排、深读回答，输出带时间戳的答案、可播放片段和关键帧，并生成自包含
  HTML 预览页。
inspiration: 趋势是视频内容从人工观看转向 AI 索引与问答，视频检索将更精准。切入可从视频审核、内容归档等需要精确时间定位的场景做起，提供可核对的片段引用。
summary_en: This is a video understanding and Q&A agent skill based on DeepSeek's vision model. After
  a user uploads a video, it extracts frames along the timeline to build an index, performs local coarse
  filtering, visual re-ranking, and deep reading to answer questions, outputting timestamped answers,
  playable clips, and key frames, and generates a self-contained HTML preview page.
inspiration_en: 'The trend is video content shifting from manual viewing to AI indexing and Q&A, enabling
  more precise video retrieval. Entry point: start with scenarios requiring precise time localization,
  such as video review and content archiving, providing verifiable clip references.'
priority_review: false
project_type: open_source
industries:
- 视频分析
industries_en:
- Video analysis
jobs:
- 视频内容分析师
jobs_en:
- Video content analysts
regions: []
regions_en: []
open_source: true
url: https://skillhub.cn/skills/user_8bb4b4f5/deepseek-v4-flash-vision-video-rag
canonical_url: https://skillhub.cn/skills/user_8bb4b4f5/deepseek-v4-flash-vision-video-rag
summary: DeepSeek V4-Flash Vision Video RAG 让 AI 真正"看懂" 一段视频，然后你对它提问：它告诉你答案、答案发生在 第几分几秒，并切出那一段的可播放片段和关键帧给你核对。  基于
  DeepSeek 视觉大模型 deepseek-v4-flash-vision-exp 的视频理解与问答 （video RAG）agent skill。先按时间轴抽帧阅读、建立索引（一次性），再对问题做
  本地粗筛 → 视觉精排 → 深读回答；回答带 [MM:SS] 时间戳引用，自动生成 自包含 HTML 预览页（内嵌可播放片段 + 关键帧 + 答案），双击浏览器即看。
first_seen: '2026-08-24T09:46:05Z'
last_seen: '2026-09-08T14:34:27Z'
status: queued
sources:
- github
sightings:
- source: github
  url: https://skillhub.cn/skills/user_8bb4b4f5/deepseek-v4-flash-vision-video-rag
  seen_at: '2026-09-05T13:28:25Z'
  metrics:
    stars: 62
    forks: 5
    open_issues: 0
  kind: product
- source: github
  url: https://skillhub.cn/skills/user_8bb4b4f5/ecom-video-seedance-prompt
  seen_at: '2026-09-08T14:34:27Z'
  metrics:
    stars: 55
    forks: 6
    open_issues: 0
  kind: product
---

# deepseek-v4-flash-vision-video-rag

DeepSeek V4-Flash Vision Video RAG 让 AI 真正"看懂" 一段视频，然后你对它提问：它告诉你答案、答案发生在 第几分几秒，并切出那一段的可播放片段和关键帧给你核对。  基于 DeepSeek 视觉大模型 deepseek-v4-flash-vision-exp 的视频理解与问答 （video RAG）agent skill。先按时间轴抽帧阅读、建立索引（一次性），再对问题做 本地粗筛 → 视觉精排 → 深读回答；回答带 [MM:SS] 时间戳引用，自动生成 自包含 HTML 预览页（内嵌可播放片段 + 关键帧 + 答案），双击浏览器即看。

## 笔记


