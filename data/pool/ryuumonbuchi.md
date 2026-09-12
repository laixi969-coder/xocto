---
slug: ryuumonbuchi
name: Ryuumonbuchi
builder: elliottophellia
category: AI + 开发
summary_zh: 逆向工程师在分析二进制样本时，原本要在 Ghidra 图形界面里手工点选反编译、复制函数代码，再切到外部对话工具粘贴提问。该项目把 Ghidra 以无界面方式暴露给模型调用，让模型直接读取反编译结果并返回分析结论，最终由工程师核对。具体支持的调用流程与交付形态仍待核验。
inspiration: 趋势是逆向工程这类高度依赖专有工具链的岗位，开始把工具本身变成模型可调用的接口，而不是把代码导出到通用聊天窗口。切入可考虑安全服务商或漏洞研究团队，把反编译、符号恢复、样本比对串成按样本或按项目交付的分析服务；公开材料未披露定价，是否收费仍属推断。
summary_en: Reverse engineers analyzing binary samples normally click through Ghidra's GUI to decompile
  and copy function code, then paste it into a separate chat tool. This project exposes Ghidra headlessly
  so a model can call it directly, read decompiled output and return analysis findings for the engineer
  to verify. The exact call flow and deliverable format still need verification.
inspiration_en: The trend is that reverse engineering, a job tied to a proprietary toolchain, is turning
  the tool itself into a model-callable interface instead of exporting code into a generic chat window.
  A possible entry is security service firms or vulnerability research teams packaging decompilation,
  symbol recovery and sample diffing into per-sample or per-project analysis services; no public pricing
  is disclosed, so charging is an inference.
priority_review: false
project_type: open_source
industries:
- 信息安全
- 软件与信息技术服务
industries_en:
- Information Security
- Software and IT Services
jobs:
- 逆向工程师
- 安全分析师
jobs_en:
- Reverse Engineer
- Security Analyst
regions: []
regions_en: []
open_source: true
url: https://github.com/elliottophellia/Ryuumonbuchi
canonical_url: https://github.com/elliottophellia/Ryuumonbuchi
summary: Maybe the headless Ghidra MCP you are looking for.
first_seen: '2026-08-23T14:26:07Z'
last_seen: '2026-09-12T00:18:44Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/elliottophellia/Ryuumonbuchi
  seen_at: '2026-09-12T00:18:44Z'
  metrics:
    stars: 68
    forks: 5
    open_issues: 0
  kind: product
---

# Ryuumonbuchi

Maybe the headless Ghidra MCP you are looking for.

## 笔记


