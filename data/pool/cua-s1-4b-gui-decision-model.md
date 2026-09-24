---
slug: cua-s1-4b-gui-decision-model
name: Cua-S1-4B GUI Decision Model
builder: cua-ai
category: 基础层
summary_zh: 做 GUI 自动化的开发者，在需要让程序判断“点哪个界面元素、执行什么动作”时，把当前界面截图交给这个 4B 模型，它一次前向就输出元素与动作的配对打分，开发者据此选出下一步操作；目前只有演示页，具体输入输出格式与准确率仍待核验。
inspiration: GUI 操作决策正从“大模型整页推理”拆成可单独打分的小模型零件，趋势是决策层被模块化。切入可考虑把这类打分器接到具体旧流程上，例如保险理赔录入、电商后台批量改价，按完成的单据或订单收费，而不是卖模型调用次数；前提是先拿到可复现的准确率证据。
summary_en: Developers building GUI automation hand a screenshot to this 4B model when they need to decide
  which interface element to act on and what action to take; it returns scored (element, action) pairs
  in one forward pass so the developer can pick the next step. Only a demo page exists, so input/output
  format and accuracy remain unverified.
inspiration_en: GUI decision-making is splitting from full-page model reasoning into small, separately
  scored components, a trend toward modular decision layers. A wedge is to attach such a scorer to one
  concrete legacy workflow, for example insurance claim entry or bulk price edits in an e-commerce back
  office, and charge per completed document or order rather than per model call, once reproducible accuracy
  evidence exists.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://huggingface.co/spaces/cua-ai/cua-s1-4b-02-demo
canonical_url: https://huggingface.co/spaces/cua-ai/cua-s1-4b-02-demo
summary: One-pass GUI (element, action) decision scorer
first_seen: '2026-09-23T17:42:34Z'
last_seen: '2026-09-24T00:31:15Z'
status: watching
sources:
- huggingface
sightings:
- source: huggingface
  url: https://huggingface.co/spaces/cua-ai/cua-s1-4b-02-demo
  seen_at: '2026-09-24T00:31:15Z'
  metrics:
    likes: 2
  kind: product
---

# Cua-S1-4B GUI Decision Model

One-pass GUI (element, action) decision scorer

## 笔记


