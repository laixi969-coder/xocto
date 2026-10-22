---
slug: multiplane
name: Multiplane
builder: LBEILC
category: AI + 创作
summary_zh: 做视频的人或给 AI 代理搭流程的开发者，在已有网页动画脚本、需要导出成片时打开它：它把每个镜头当作由 render(t) 驱动的普通网页，在本地无头渲染成视频，并做确定性校验、按剪辑点加运动模糊、叠加带累积景深的
  3D 层。用户拿到的是可重复渲染的视频文件，具体成片质量与人工校对环节仍待核验。
inspiration: 趋势：AI 代理开始直接产出可渲染的网页动画，视频交付从剪辑软件转向代码化渲染。切入：从需要批量、可复现出片的营销素材或数据可视化团队进入，卖按成片条数或渲染时长计费的服务，而不是卖编辑器。
summary_en: 'People making videos, or developers wiring up AI agents, open this when they already have
  web-page animation scripts and need a finished video: each shot is a plain web page driven by render(t),
  rendered headlessly on the local machine into video, with determinism checks, cut-aware motion blur
  and a 3D layer with accumulated depth of field. The output is a repeatably rendered video file; final
  quality and the human review step still need verification.'
inspiration_en: 'Trend: AI agents now emit renderable web animations, so video delivery shifts from editing
  suites to code-driven rendering. Entry: start with marketing or data-visualization teams that need batch,
  reproducible clips, and sell per finished video or render minute rather than an editor.'
priority_review: false
project_type: open_source
industries:
- 视频制作
- 广告与营销
industries_en:
- video production
- advertising and marketing
jobs:
- 视频制作者或代理开发者把网页动画脚本渲染成带运动模糊和景深的成片视频
jobs_en:
- Video producers or agent developers render web-page animation scripts into finished videos with motion
  blur and depth of field
regions: []
regions_en: []
open_source: true
url: https://github.com/LBEILC/Multiplane
canonical_url: https://github.com/LBEILC/Multiplane
summary: Local headless HTML-to-video renderer for AI agents. Shots are plain web pages driven by render(t);
  includes determinism checks, cut-aware motion blur, and a 3D layer with accumulated depth of field.
first_seen: '2026-10-18T00:03:49Z'
last_seen: '2026-10-22T00:42:25Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/LBEILC/Multiplane
  seen_at: '2026-10-22T00:42:25Z'
  metrics:
    stars: 103
    forks: 5
    open_issues: 1
  kind: product
---

# Multiplane

Local headless HTML-to-video renderer for AI agents. Shots are plain web pages driven by render(t); includes determinism checks, cut-aware motion blur, and a 3D layer with accumulated depth of field.

## 笔记


