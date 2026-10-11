---
slug: solvecraft
name: solvecraft
builder: bherbruck
category: AI + 开发
summary_zh: 工程师或设计师在需要改动零件尺寸、装配关系时，打开这个纯 Rust 写的参数化 3D CAD，用参数驱动重建模型；它同时提供桌面端、浏览器端和通过 MCP 供 AI 代理调用的接口，最终交付可继续加工的模型文件。具体建模能力边界与
  AI 代理实际能完成到哪一步仍待核验。
inspiration: 趋势：参数化 CAD 这类被商业软件长期把持的重型工具，开始出现开源重写并把接口开放给 AI 代理。切入：不要正面做通用 CAD，可从某个具体制造环节切入——例如只服务注塑件改模、钣金展开或非标零件报价，让
  AI 代理直接读图纸参数生成可报价模型，按件或按项目收费。
summary_en: When engineers or designers need to change a part dimension or assembly constraint, they open
  this pure-Rust parametric 3D CAD and rebuild the model by driving parameters; it ships as desktop, browser,
  and an MCP interface for AI agents, delivering a model file that can be machined further. The actual
  modeling limits and how far an AI agent can complete a task remain unverified.
inspiration_en: 'Trend: parametric CAD, long locked inside commercial suites, is being rewritten in the
  open and exposed to AI agents. Entry: avoid head-on general CAD; start from one manufacturing step,
  such as injection-mold changes, sheet-metal unfolding, or custom-part quoting, letting an agent read
  drawing parameters and produce a quotable model, charged per part or per project.'
priority_review: false
project_type: open_source
industries:
- 机械制造
- 工业设计
- 建筑与工程
industries_en:
- Mechanical Manufacturing
- Industrial Design
- Architecture & Engineering
jobs:
- 机械工程师在需要修改零件尺寸或装配关系时，打开参数化 CAD 模型，调整参数并重新生成可制造的 3D 模型
- 工业设计师在向客户或工厂交付前，用参数化建模核对尺寸与结构，输出可继续加工的模型文件
jobs_en:
- A mechanical engineer opens a parametric CAD model to change a part dimension or assembly constraint,
  then regenerates a manufacturable 3D model
- An industrial designer checks dimensions and structure with parametric modeling before delivering to
  a client or factory, and exports a model file for further machining
regions: []
regions_en: []
open_source: true
url: https://bherbruck.github.io/solvecraft/
canonical_url: https://bherbruck.github.io/solvecraft
summary: An open-source, clean-room reimplementation of Autodesk Fusion 360 in pure Rust. Parametric 3D
  CAD for desktop, browser, and AI agents via MCP.
first_seen: '2026-10-11T01:01:22Z'
last_seen: '2026-10-11T01:01:22Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://bherbruck.github.io/solvecraft/
  seen_at: '2026-10-11T01:01:22Z'
  metrics:
    stars: 131
    forks: 10
    open_issues: 20
  kind: product
---

# solvecraft

An open-source, clean-room reimplementation of Autodesk Fusion 360 in pure Rust. Parametric 3D CAD for desktop, browser, and AI agents via MCP.

## 笔记


