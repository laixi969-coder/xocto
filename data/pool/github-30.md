---
slug: github-30
name: Github
builder: wasabihu
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
url: https://github.com/xerj-org/xerj
canonical_url: https://github.com/xerj-org/xerj
summary: "最近拿 19.4k★ 的单文件 Rust AI 搜索引擎 [XERJ](https://github.com/xerj-org/xerj) 测了一轮真实中文/双语 RAG 场景（33,575\
  \ 个分块：29 部中国现行法规 + SEC/港股财报与招股书 + 临床试验三线表）。\r\n\r\n默认 BM25 词法检索在中文场景掉得很惨，端到端 60 题基准里证据块 `R@3` 只有 `0.2222`（Oracle\
  \ 达成率 `5.3%`）。主要踩出三个真实硬伤：\r\n1. 阿拉伯数字 vs 中文数字法条错排（搜「第 147 条」漏召「第一百四十七条」）\r\n2. 简繁术语断链 + 港交所 PDF 常见 CMap\
  \ 错字（比如腾讯季报里「月」被抽成「尸」，以及表格折行断小数点 `39.\\n9 亿美元`）\r\n3. 不可回答陷阱题疯狂过召回（单字匹配每次吐出 15–3,319 条弱相关分块）\r\n\r\n\
  没动底层引擎一行代码，用纯 Python 标准库（`dependencies = []`）写了个客户端查询适配层 `query_cn` + 文本/表格修复器，同一批 33,575 分块 60 题重跑：\r\
  \n- 证据块 `R@3`：`0.2222` -> **`0.9111`**（`nDCG@3`: `0.2029` -> **`0.8561`**）\r\n- 端到端 Oracle 达成率：`5.3%`\
  \ -> **`97.4%`**（4,000 次 Bootstrap `ΔNet = +35`）\r\n- 不可回答陷阱严格 0 误召拒答：`0/4` -> **`4/4`**\r\n- 腾讯 `0700.HK`\
  \ PDF 季报日期「月→尸」修复 341 处、残留 0 处（且严格限定日期上下文，不误伤「尸检」）\r\n\r\n目前两份 PR 已经合进 `xerj-org/xerj` 主库：\r\n- 实测报告\
  \ `#3371`（官方已单开 `#3377` 跟进内核 CJK 支持）：https://github.com/xerj-org/xerj/pull/3371\r\n- 两座纯文本合规语料仓收录 `#3372`（3,204\
  \ 条中国法规 CC0 + 55 篇 271 张临床表 NLM/CC-BY）：https://github.com/xerj-org/xerj/pull/3372\r\n\r\n整套工具包、合规门禁和评测脚本已以\
  \ Apache-2.0 开源（核心零依赖，可选 PDF 几何重建用 `[pdf]` 惰性隔离 `PyMuPDF` 的 AGPL-3.0）：\r\n- 主仓库：https://github.com/wasabihu/vericorpus\r\
  \n- 法规纯文本仓：https://github.com/wasabihu/corpus-cn-statutes\r\n- 临床试验表仓：https://github.com/wasabihu/corpus-clinical-trials\r\
  \n\r\n做本地 RAG 或金融/法律文档检索的 V 友欢迎拍砖，也想听听大家在中文长 PDF 表格和混合检索上还有哪些难啃的坑。"
first_seen: '2026-11-23T02:45:54Z'
last_seen: '2026-11-23T02:45:54Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/xerj-org/xerj
  seen_at: '2026-11-23T02:45:54Z'
  metrics:
    comments: 0
  kind: product
---

# Github

最近拿 19.4k★ 的单文件 Rust AI 搜索引擎 [XERJ](https://github.com/xerj-org/xerj) 测了一轮真实中文/双语 RAG 场景（33,575 个分块：29 部中国现行法规 + SEC/港股财报与招股书 + 临床试验三线表）。

默认 BM25 词法检索在中文场景掉得很惨，端到端 60 题基准里证据块 `R@3` 只有 `0.2222`（Oracle 达成率 `5.3%`）。主要踩出三个真实硬伤：
1. 阿拉伯数字 vs 中文数字法条错排（搜「第 147 条」漏召「第一百四十七条」）
2. 简繁术语断链 + 港交所 PDF 常见 CMap 错字（比如腾讯季报里「月」被抽成「尸」，以及表格折行断小数点 `39.\n9 亿美元`）
3. 不可回答陷阱题疯狂过召回（单字匹配每次吐出 15–3,319 条弱相关分块）

没动底层引擎一行代码，用纯 Python 标准库（`dependencies = []`）写了个客户端查询适配层 `query_cn` + 文本/表格修复器，同一批 33,575 分块 60 题重跑：
- 证据块 `R@3`：`0.2222` -> **`0.9111`**（`nDCG@3`: `0.2029` -> **`0.8561`**）
- 端到端 Oracle 达成率：`5.3%` -> **`97.4%`**（4,000 次 Bootstrap `ΔNet = +35`）
- 不可回答陷阱严格 0 误召拒答：`0/4` -> **`4/4`**
- 腾讯 `0700.HK` PDF 季报日期「月→尸」修复 341 处、残留 0 处（且严格限定日期上下文，不误伤「尸检」）

目前两份 PR 已经合进 `xerj-org/xerj` 主库：
- 实测报告 `#3371`（官方已单开 `#3377` 跟进内核 CJK 支持）：https://github.com/xerj-org/xerj/pull/3371
- 两座纯文本合规语料仓收录 `#3372`（3,204 条中国法规 CC0 + 55 篇 271 张临床表 NLM/CC-BY）：https://github.com/xerj-org/xerj/pull/3372

整套工具包、合规门禁和评测脚本已以 Apache-2.0 开源（核心零依赖，可选 PDF 几何重建用 `[pdf]` 惰性隔离 `PyMuPDF` 的 AGPL-3.0）：
- 主仓库：https://github.com/wasabihu/vericorpus
- 法规纯文本仓：https://github.com/wasabihu/corpus-cn-statutes
- 临床试验表仓：https://github.com/wasabihu/corpus-clinical-trials

做本地 RAG 或金融/法律文档检索的 V 友欢迎拍砖，也想听听大家在中文长 PDF 表格和混合检索上还有哪些难啃的坑。

## 笔记


