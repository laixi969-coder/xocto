---
slug: brier
name: brier
builder: Noisyxl
category: 基础层
summary_zh: 做预测或研究的人让 LLM 给出判断时，答案往往事后才被回忆，无法核对当时说了什么。brier 在答案出现前把预测写入哈希链账本封存，事后按 proper scoring rules
  打分，用户拿到一份可追溯、可评分的预测记录；具体使用流程与交付形态仍待核验。
inspiration: 趋势是模型输出开始需要“留痕与结算”，而不只是生成。切入可放在需要事后追责的预测场景，例如投研观点、咨询结论或内部决策记录，把封存与打分做成可核验的交付物；目前只有开源仓库，尚无付费路径证据。
summary_en: People who ask an LLM for a forecast usually cannot verify afterwards what was actually said
  at the time. brier seals each prediction into a hash-chained ledger before the answer exists and grades
  it later with proper scoring rules, giving the user a traceable, scorable prediction record; the concrete
  workflow and delivery format still need verification.
inspiration_en: The trend is that model output increasingly needs a receipt and a settlement, not just
  generation. An entry point is forecast settings where accountability matters, such as investment research
  calls, consulting conclusions or internal decision logs, selling a verifiable sealed-and-scored record;
  today only an open-source repository exists, with no evidence of a paid path.
priority_review: false
project_type: open_source
industries:
- 金融与投资
- 科研与咨询
industries_en:
- Finance and investment
- Research and consulting
jobs:
- 预测记录与事后评分
- 模型输出可信度审计
jobs_en:
- Prediction logging and retrospective scoring
- Model output credibility auditing
regions: []
regions_en: []
open_source: true
url: https://github.com/Noisyxl/brier
canonical_url: https://github.com/Noisyxl/brier
summary: Anyone can predict the future. Almost nobody keeps the receipt. A hash-chained prediction ledger
  for LLMs — sealed before the answer exists, graded with proper scoring rules.
first_seen: '2026-09-06T13:42:25Z'
last_seen: '2026-09-23T00:34:19Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/Noisyxl/brier
  seen_at: '2026-09-23T00:34:19Z'
  metrics:
    stars: 117
    forks: 8
    open_issues: 1
  kind: product
---

# brier

Anyone can predict the future. Almost nobody keeps the receipt. A hash-chained prediction ledger for LLMs — sealed before the answer exists, graded with proper scoring rules.

## 笔记


