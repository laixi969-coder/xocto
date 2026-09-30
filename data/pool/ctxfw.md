---
slug: ctxfw
name: Ctxfw
builder: mikemo88
category: AI + 开发
summary_zh: 开发者在给编码代理喂代码上下文时，用它按语法结构裁剪上下文，声称可把代理提示词 token 减少 67%；候选材料只有一句说明，裁剪规则与实测口径仍待核验。
inspiration: 趋势是代理成本从模型单价转向上下文体积，谁控制喂进去的代码量谁就控制账单。切入可考虑为按仓库结构做上下文裁剪的中间层，按节省的 token 或调用量收费，而不是再做一个代理；价格未披露。
summary_en: When feeding code context to a coding agent, a developer uses this to trim context by syntax
  structure, claiming a 67% cut in agent prompt tokens. The candidate material is a single line; the trimming
  rules and how the figure was measured still need verification.
inspiration_en: The trend is agent cost shifting from model price to context size, so whoever controls
  how much code gets fed in controls the bill. A wedge is a context-trimming layer driven by repository
  structure, charged by tokens saved or calls made rather than building another agent; no price is disclosed.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 开发者
jobs_en:
- Software developers
regions: []
regions_en: []
open_source: true
url: https://github.com/heuristicolab/ctxfw
canonical_url: https://github.com/heuristicolab/ctxfw
summary: AST context firewall that cuts agent prompt tokens by 67%
first_seen: '2026-09-29T14:23:25Z'
last_seen: '2026-09-30T01:18:13Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/heuristicolab/ctxfw
  seen_at: '2026-09-30T01:18:13Z'
  metrics:
    points: 5
    comments: 0
  kind: product
---

# Ctxfw

AST context firewall that cuts agent prompt tokens by 67%

## 笔记


