# Bug Hunt: 首页机会判断与页面语言边界

**Date:** 2026-08-24
**Scope:** `templates/index.html`、`src/xocto/site.py`、`src/xocto/brief.py`、`src/xocto/req_review.py`、`src/xocto/market.py`、`scripts/check_design.py` 及对应测试
**Failures:** 0

## Summary

| # | Bug | Severity | File | Fix |
|---|-----|----------|------|-----|
| 1 | 首页 `/req` 初判只输出“证据不足”，不能帮助创业者分配注意力 | MEDIUM | `templates/index.html`、`src/xocto/site.py` | 将内部闸门投影为“值得研究／继续跟踪／仅作方向线索／暂不投入”，合并具体切入方向与证据边界 |
| 2 | 中文详情页直接展示英文市场检索标题和摘要 | MEDIUM | `src/xocto/site.py` | 中英文证据分别投影；中文证据使用中文产品说明，英文证据只接受英文文本 |
| 3 | 未被判断引用的通用 AI 搜索结果进入公开证据链 | MEDIUM | `src/xocto/site.py`、`src/xocto/market.py` | 查询入口不公开，市场结果只有被判断引用才展示；未来采集先按行业/工作词过滤相关性 |
| 4 | 同一证据因重复采集在详情页出现多次 | LOW | `src/xocto/site.py` | 按 URL、标题、类型与事实去重 |
| 5 | 旧 `summary_zh` 中“中文｜英文”拼接重新污染中文证据 | MEDIUM | `src/xocto/site.py`、`scripts/check_design.py` | 增加中文自由文本净化，并将“英文段落漏进中文证据”设为发布门槛 |
| 6 | 项目特定兜底理由按字符硬截断，出现“并依”一类残句 | MEDIUM | `src/xocto/req_review.py` | 按完整句截取摘要，并让历史截断理由自动重新进入返工队列 |

## Root Cause

`be6978d7` 将原始 `Evidence.title/fact` 直接映射到详情页；`3274b054` 又把首个阻塞闸门理由直接映射为首页初判。两处都把内部研究数据误当成面向用户的最终表达，缺少“创业决策投影”和“页面语种投影”。市场扫描同时保存查询入口与全部搜索结果，页面则展示全部记录，导致不相关的 OpenAI、ChatGPT、Gemini 等通用首页成为所谓证据。

## Pass 1 — Surface

重现四张截图。确认前三张来自首页 `req_reason`，第四张来自 `_research_view` 对全部原始证据的无条件展开。修复首页决策投影、证据引用过滤、语种投影与市场结果相关性过滤。

## Pass 2 — Re-read

重建全站后，新增语言门禁发现 16 个历史页面仍有双语摘要；进一步确认旧 `summary_zh` 自身含中英文拼接，且部分原始帖子全文被当作证据摘要。改为产品证据优先使用净化后的中文说明，并对重复证据去重。

## Pass 3 — Integration

99 项测试、完整建站、站内链接与 sitemap 检查通过。新增的第八项发布门槛确认英文站无中文，中文证据链无英文段落；完整句回归覆盖兜底理由不再从连接词中间截断。

## Pass 4 — Verify

GitHub Actions `32689665984` 完成首轮真实模型返工；线上抽查随后发现 `GamePhanes` 的项目摘要被按字符截在“并依”。修复提交 `5c1ec6da` 改为完整句截取，第二次真实流水线 `32689861536` 全部通过并重写该判断。

首页五条机会均显示注意力动作、具体切入与项目特定证据边界；`biosecurity-agent` 的中文证据链只保留一条中文化、可点击的开源证据，英文页只保留英文版本。通用 AI 首页、市场查询入口、重复记录与截断残句不再出现。未发现新的 HIGH 或 MEDIUM 问题，达到本轮收敛条件。
