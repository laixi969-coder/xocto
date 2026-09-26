---
slug: dsh-blender-plugin
name: dsh-blender-plugin
builder: sixtysevenlf
category: AI + 创作
summary_zh: 三维美术师在 Blender 里调材质、灯光和减面时，原本要自己反复渲染、截图、比对参数。这个插件让 AI 模型通过直连 TCP 通道读取视口画面和自定义角度渲染结果，在内部循环里搜索参数、做渲染耗时分析并执行安全减面，也可把渲染放到无头机器上跑；最终交付的是改好的场景参数和渲染结果，仍需美术师确认。
inspiration: 趋势是 AI 开始直接操作专业三维软件的内部渲染循环，而不只是生成一张图。切入可以从外包渲染农场、独立动画工作室或游戏美术外包团队进：把“反复试参数、等渲染”这一段按项目或按镜头收费，而不是卖插件席位；目前只有开源仓库，没有定价和客户案例，先看有没有工作室把它接进真实管线。
summary_en: 'A 3D artist tuning materials, lighting and decimation in Blender normally has to render,
  screenshot and compare parameters by hand. This plugin lets an AI model drive Blender over a direct
  TCP channel: it reads viewport frames and custom-angle renders, searches parameters in an inner loop,
  profiles render cost and performs safe decimation, and can offload rendering to a headless machine.
  The deliverable is adjusted scene parameters and renders, still subject to artist confirmation.'
inspiration_en: 'The trend is AI reaching into the inner render loop of professional 3D software rather
  than just generating an image. A wedge could be render farms, independent animation studios or game
  art outsourcing teams: charge per project or per shot for the repeated parameter-tuning and render-waiting
  step instead of selling plugin seats. Today it is only an open-source repository with no pricing or
  customer cases, so watch whether a studio wires it into a real pipeline.'
priority_review: false
project_type: open_source
industries:
- 影视动画
- 游戏开发
- 工业设计
industries_en:
- film and animation
- game development
- industrial design
jobs:
- 三维美术师
- 技术美术
jobs_en:
- 3D artist
- technical artist
regions: []
regions_en: []
open_source: true
url: https://github.com/sixtysevenlf/dsh-blender-plugin
canonical_url: https://github.com/sixtysevenlf/dsh-blender-plugin
summary: 'DSH x Blender direct realtime plugin - let an AI model drive Blender over a direct TCP channel:
  viewport frames, custom-angle renders, inner-loop search, render profiling, safe decimation, headless
  offload.'
first_seen: '2026-09-13T16:07:04Z'
last_seen: '2026-09-26T00:37:55Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/sixtysevenlf/dsh-blender-plugin
  seen_at: '2026-09-26T00:37:55Z'
  metrics:
    stars: 68
    forks: 4
    open_issues: 4
  kind: product
---

# dsh-blender-plugin

DSH x Blender direct realtime plugin - let an AI model drive Blender over a direct TCP channel: viewport frames, custom-angle renders, inner-loop search, render profiling, safe decimation, headless offload.

## 笔记


