---
slug: paper-docx
name: Paper-docx
builder: i_rush_carriers
category: AI + 开发
summary_zh: 工程师在自动化生成合同、报告等 DOCX 文件时，把结构化内容交给这个库写入文档；它接收文本与格式指令并输出可打开的 Word 文件，宣称比原库更少出现文档损坏或格式错乱。具体失败率如何测得、哪些场景适用，公开材料尚未说明。
inspiration: 趋势是 agent 开始直接产出交付物，而交付物的格式稳定性成了新瓶颈。切入可以从文档密集的行业（律所、财税、招投标）入手，把“生成后必坏”的环节做成可核验的交付保证，而不是再做一个通用文档库。
summary_en: Engineers automating DOCX contracts and reports hand structured content to this library, which
  writes it into an openable Word file and claims fewer corrupted or misformatted documents than the original
  library. How the failure rate was measured and which scenarios it covers are not stated in the public
  material.
inspiration_en: The trend is agents producing deliverables directly, which makes format reliability the
  new bottleneck. An entry point is document-heavy sectors such as law, tax and tendering, turning the
  'breaks after generation' step into a verifiable delivery guarantee rather than another generic document
  library.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
- 办公文档处理
industries_en:
- Software and IT services
- Office document processing
jobs:
- 后端或自动化工程师在批量生成合同、报告等 DOCX 文件时，调用文档库写入内容并处理格式异常
jobs_en:
- Backend or automation engineers generating DOCX contracts and reports in bulk, calling a document library
  to write content and handle formatting errors
regions: []
regions_en: []
open_source: true
url: https://github.com/paper-instruments/paper-docx
canonical_url: https://github.com/paper-instruments/paper-docx
summary: agent-native Python-docx fork with 78% fewer DOCX failures
first_seen: '2026-09-25T19:05:31Z'
last_seen: '2026-09-27T00:36:16Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/paper-instruments/paper-docx
  seen_at: '2026-09-27T00:36:16Z'
  metrics:
    points: 6
    comments: 0
  kind: product
---

# Paper-docx

agent-native Python-docx fork with 78% fewer DOCX failures

## 笔记


