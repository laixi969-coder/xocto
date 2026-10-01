---
slug: photo-scrubber-local-face-blur-metadata-removal
name: Photo Scrubber
builder: ''
category: AI + 创作
summary_zh: 摄影记者或活动组织者在拍摄抗议、集会等含陌生人面孔的照片后，需要在发布前处理这些图片。Photo Scrubber 在浏览器本地接收照片，用人脸检测模型找出人脸并自动模糊，同时清除元数据，用户拿到可直接分享的脱敏图片；模糊范围与漏检仍需人工确认。具体流程与交付仍待核验。
inspiration: 趋势：隐私脱敏正从云端服务下沉到浏览器本地推理，处理敏感影像的人不必再把原始素材交给第三方。切入：可从新闻机构、非营利组织的图片发布环节进入，按机构或按批量脱敏收费；但该工具目前是个人实验项目，尚无定价与客户证据，先观察其是否被编辑部实际采用。
summary_en: A photojournalist or event organizer who has shot protests or gatherings containing strangers'
  faces needs to prepare those images before publishing. Photo Scrubber takes photos locally in the browser,
  runs a face detection model to find and automatically blur faces, and strips metadata, returning shareable
  redacted images; blur coverage and missed detections still need human review. The exact workflow and
  delivery remain to be verified.
inspiration_en: 'Trend: privacy redaction is moving from cloud services to local in-browser inference,
  so people handling sensitive imagery no longer hand originals to a third party. Entry: start from the
  image publishing step of newsrooms and nonprofits, charging per organization or per batch; but this
  is currently a personal experiment with no pricing or customer evidence, so watch whether newsrooms
  actually adopt it.'
priority_review: false
project_type: new_application
industries:
- 新闻与媒体
- 摄影服务
- 公民社会组织
industries_en:
- News and media
- Photography services
- Civic and nonprofit organizations
jobs:
- 摄影记者
- 图片编辑
- 活动组织者
jobs_en:
- Photojournalist
- Picture editor
- Event organizer
regions:
- 全球
regions_en:
- Global
open_source: false
url: https://simonwillison.net/2026/Sep/29/photo-scrubber/
canonical_url: https://simonwillison.net/2026/Sep/29/photo-scrubber
summary: "Tool:   Photo Scrubber — local face blur & metadata removal  \n         I took a photograph\
  \ of some protesters, then thought about how I don't like sharing photographs of strangers with identifiable\
  \ faces. I  had GPT-6 Astra build  this experimental tool that would identify faces and automatically\
  \ blur them out. \n It uses Google's  MediaPipe  C++ library, compiled to WebAssembly via  @mediapipe/tasks-vision\
  \ , plus the  BlazeFace  face detection model. \n    \n    \n         Tags:  photography ,  tools"
first_seen: '2026-09-29T16:45:27Z'
last_seen: '2026-10-01T01:19:01Z'
status: watching
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/29/photo-scrubber/
  seen_at: '2026-10-01T01:19:01Z'
  metrics: {}
  kind: news
---

# Photo Scrubber

Tool:   Photo Scrubber — local face blur & metadata removal  
         I took a photograph of some protesters, then thought about how I don't like sharing photographs of strangers with identifiable faces. I  had GPT-6 Astra build  this experimental tool that would identify faces and automatically blur them out. 
 It uses Google's  MediaPipe  C++ library, compiled to WebAssembly via  @mediapipe/tasks-vision , plus the  BlazeFace  face detection model. 
    
    
         Tags:  photography ,  tools

## 笔记


