---
slug: alibabacloud
name: Alibabacloud
builder: baicaix
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
url: https://www.alibabacloud.com/help/en/model-studio/model-pricing
canonical_url: https://alibabacloud.com/help/en/model-studio/model-pricing
summary: "最近调整了自己做的 reAPI 上 Wan 3.0 的价格，按视频秒数计费：\r\n\r\n  - 标准版：官方国际站原价 6.8 折\r\n  - Video Prime 加速版：官方国际站原价\
  \ 7.8 折\r\n  - 支持 2–30 秒，480P / 720P / 1080P\r\n  - 支持文生视频、图生视频和参考素材生成，支持原生音频\r\n\r\n  以 720P 、10 秒、不带输入参考视频的请求为例，标准版是\
  \ $0.68 ，Prime 是 $1.092 。\r\n\r\n  折扣按阿里云国际站新加坡区的美元原价计算，9 月 7 日核对。官方标准版目前也有 7 折活动，我们是 6.8 折。官方价格表\r\n\
  \  ( https://www.alibabacloud.com/help/en/model-studio/model-pricing)。\r\n\r\n  标准版的文生视频请求：\r\n\r\n\
  \  curl https://reapi.ai/api/v1/videos/generations \\\r\n    -H \"Authorization: Bearer YOUR_API_KEY\"\
  \ \\\r\n    -H \"Content-Type: application/json\" \\\r\n    -d '{\r\n      \"model\": \"wan3.0-video\"\
  ,\r\n      \"prompt\": \"A lighthouse keeper climbing a spiral staircase at dawn\",\r\n      \"resolution\"\
  : \"720P\",\r\n      \"duration\": 10\r\n    }'\r\n\r\n  拿到返回的任务 ID 后，轮询 /api/v1/tasks/{task_id} 获取结果。\r\
  \n\r\n  两个模型页都有 playground 和完整参数：\r\n\r\n  - Wan 3.0 标准版 ( https://reapi.ai/models/wan-3-0)\r\n  - Wan\
  \ 3.0 Video Prime ( https://reapi.ai/models/wan-3-0-video-prime)\r\n\r\n  Prime 的参数和标准版有些差异，接入时看各自文档。"
first_seen: '2026-09-07T06:36:22Z'
last_seen: '2026-09-07T15:52:43Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: https://www.alibabacloud.com/help/en/model-studio/model-pricing
  seen_at: '2026-09-07T15:52:43Z'
  metrics:
    comments: 0
  kind: product
---

# Alibabacloud

最近调整了自己做的 reAPI 上 Wan 3.0 的价格，按视频秒数计费：

  - 标准版：官方国际站原价 6.8 折
  - Video Prime 加速版：官方国际站原价 7.8 折
  - 支持 2–30 秒，480P / 720P / 1080P
  - 支持文生视频、图生视频和参考素材生成，支持原生音频

  以 720P 、10 秒、不带输入参考视频的请求为例，标准版是 $0.68 ，Prime 是 $1.092 。

  折扣按阿里云国际站新加坡区的美元原价计算，9 月 7 日核对。官方标准版目前也有 7 折活动，我们是 6.8 折。官方价格表
  ( https://www.alibabacloud.com/help/en/model-studio/model-pricing)。

  标准版的文生视频请求：

  curl https://reapi.ai/api/v1/videos/generations \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "wan3.0-video",
      "prompt": "A lighthouse keeper climbing a spiral staircase at dawn",
      "resolution": "720P",
      "duration": 10
    }'

  拿到返回的任务 ID 后，轮询 /api/v1/tasks/{task_id} 获取结果。

  两个模型页都有 playground 和完整参数：

  - Wan 3.0 标准版 ( https://reapi.ai/models/wan-3-0)
  - Wan 3.0 Video Prime ( https://reapi.ai/models/wan-3-0-video-prime)

  Prime 的参数和标准版有些差异，接入时看各自文档。

## 笔记


