---
slug: huggingface
name: Hugging Face
builder: cs1707
category: AI + 开发
summary_zh: 公开模型社区 是流行的开源 AI 模型仓库，据报道将被 Nvidia 以 129 亿美元收购。同时，OpenAI 的 rogue AI 模型事件涉及 公开模型社区 安全漏洞。
inspiration: 趋势是 AI 论文从「读摘要」变成「可筛选、可比较、可追溯的结构化数据」。切入点是科研工具链，把论文解析成带章节路径的数据库，再卖给需要做技术选型或找 research gap
  的团队，按数据集或 API 收费。
summary_en: public model community is a popular open-source AI model hub, reportedly to be acquired by
  Nvidia for $12.9B. Also, OpenAI's rogue AI model incident involved public model community security breach.
inspiration_en: The trend is AI papers moving from 'reading abstracts' to 'filterable, comparable, traceable
  structured data'. The entry point is the research toolchain, turning papers into a database with section
  paths, then selling to teams needing tech selection or research gap identification, charging per dataset
  or API.
priority_review: false
project_type: open_source
industries:
- 科研
- 人工智能
industries_en:
- Research
- Artificial Intelligence
jobs:
- 研究员
- 工程师
jobs_en:
- Researcher
- Engineer
regions:
- 全球
regions_en:
- Global
open_source: true
url: https://huggingface.co/datasets/JensCS/top-ml-conference-papers-2024
canonical_url: https://huggingface.co/datasets/JensCS/top-ml-conference-papers-2024
summary: "上次我做了一份 2023 年的 AI 论文数据集，有 7000 多篇，没想到还挺受欢迎的\U0001F449https://www.v2ex.com/t/1229793?p=1#reply9\
  \ ，还有老哥问我啥时候更新。所以今天我又来了。\r\n\r\n这次我整理了 2024 年的四大 AI 顶会论文，总共 9817 篇。在等更新的各位可以自取啦\U0001F449https://huggingface.co/datasets/JensCS/top-ml-conference-papers-2024\r\
  \n\r\nhttps://i.imgur.com/zIpVT53.png\r\n\r\n这次收录的论文来自四场 AI 顶会：\r\n\r\n- NeurIPS 2024：3960 篇\r\n\r\n\
  - CVPR 2024：2692 篇\r\n\r\n- ICLR 2024：2251 篇\r\n\r\n- ACL 2024：914 篇\r\n\r\n机器学习、计算机视觉、自然语言处理，过去一年几个最活跃的\
  \ AI 研究方向，基本都在这里了。\r\n\r\nhttps://i.imgur.com/1UNwgMc.png\r\n\r\n这份数据集并不是一份只有标题和摘要的目录。每篇论文都整理了研究领域、具体任务、核心问题、主要创新、方法、基线和实验结果，算下来一共\
  \ 24 个字段。\r\n\r\n数据里还留着论文的原文片段和对应的章节位置。看到一个实验结果，可以顺着位置查一下它是写在主实验、消融实验，还是附录里，不用只信一句脱离上下文的总结了。\r\n\r\n\
  接下来我大概讲下怎么用。\r\n\r\n平时我们想知道一个方向最近在研究什么，通常要从搜论文开始。但是搜论文你只能搜到一些很浅层的信息，比方说主题、摘要什么的，AI 论文常常涉及到的基线啊、测评集、试验条件啥的，你还是要去自己翻。你读十篇还能靠耐心，面对几千篇论文，靠人一篇篇翻就不太现实了。\r\
  \n\r\n所以这时候，你就可以拿到这份数据集，作为一份可以直接筛选和比较的研究材料，去加快你的工作进度。\r\n\r\n比如你正在找下一个实验方向，那么你可以先选定任务，再把相关论文的核心问题、主要创新、基线和关键指标摆在一起看。这样哪些问题已经被研究烂了，哪些假设还没有充分验证不可靠，以及哪些方法只在少数数据集上成立，一对比看得清清楚楚。沿着这些缺口继续追，就有机会找到值得验证的新问题。\r\
  \n\r\n你也可以把这批数据直接交给 Research Agent 。让它先梳理某个方向的技术路线，归纳不同论文共同依赖的假设，寻找尚未覆盖的场景或相互矛盾的结论，再据此整理 research gap\
  \ ，提出下一步可验证的实验方向。因为数据里保留了原文片段和章节位置，Agent 给出的判断还能继续回到论文中核对，而不是只剩一段没有出处的总结。\r\n\r\n如果不搞科研，那做技术选型也能用上。你可以先找出使用同一评测集的论文，再核对模型规模、基线和实验条件。论文里都说自己效果好，但如果训练资源、数据和评价指标不一样，数字放在一起并没有多少意义。数据集能先帮你把比较范围理顺，最后再回到原文确认。\r\
  \n\r\n平时要写报告、做分享，这份数据也能派上用场。比方说一个概念最近是不是真的热，大家是在反复讨论同一个问题，还是已经分出了几条不同的技术路线，都可以从论文里找依据。下次领导问起来，你就可以装一波顶回去，免得他又说你跟时代脱节不进步。\r\
  \n\r\n最后，如果你觉得数据集喂 AI 这个想法很有用，但是 AI 研究不是你的方向，那么我也可以给你提供方法，这样你就能拿工具去生成自己领域的数据集了，无论是做工程、通讯、硬件等等的吧，我觉得都能派上用场。\r\
  \n\r\n首先，你需要准备你所在领域的论文素材，然后用到的工具是这个——Knowhere ，开源小项目，平常使用基本免费： https://knowhereto.ai/github?utm_source=v2ex\r\
  \n\r\n这些论文基本都是 PDF 格式，在人眼里看着规整，交给程序却很容易乱套。因为它有很多双栏正文、跨页表格和图片啥的，直接转成纯文本关系就丢了，文字跟资料对不上。\r\n\r\n所以第一步，解析\
  \ PDF 。用 Knowhere 识别论文里的文字、表格、公式和版面，把正文整理成带有章节路径的内容片段。这里的 chunk 不是按固定字数随手切开的一段文字，它会同时记录自己来自哪一节。Knowhere\
  \ 会重建整篇论文的章节树，生成 doc_nav.json 。从一级标题到下面的子章节，每个节点都有自己的标题、路径、层级、摘要和片段数量。\r\n\r\n接下来我们再让 LLM 判断论文属于模型架构、方法流程、理论分析还是\
  \ Agent 系统，并按类型提取不同信息。Agent 论文重点找环境、工具、规划方式和评测基准；理论论文则关注分析对象、理论工具、主要结论和适用边界。\r\n\r\n最后，我们把通用信息、分类后的专属字段、原文片段和章节树装回同一条记录，再导出成\
  \ JSONL 和 Parquet 。Hugging Face 数据中的 chunks 和 hierarchy ，就是 Knowhere 解析后保留下来的内容。\r\n\r\n这样做出来的不是“9817\
  \ 份论文摘要合集”，而是一批可以筛选和比较、也能顺着章节路径回到原文核对的研究材料了。\r\n\r\n除了 PDF ，Knowhere 也可以处理 Word 、PPT 、图片等常见格式，并输出适合\
  \ AI Agent 和 RAG 使用的结构化 chunks 与 JSON 。如果你手里也有一批论文、报告或其他复杂文档，都可以拿去试试。\r\n\r\n其他没了，下个月可能还会做一份具身智能论文数据集，覆盖\
  \ CoRL 、ICRA 、IROS 、RSS 等机器人领域的重要会议。除了核心问题、方法和实验结果，还会继续往下拆动作空间、观测空间、传感器配置、真实机器人平台，以及 sim-to-real 方法。\r\
  \n\r\n有需要的老哥可以先关注一下，谢谢。"
first_seen: '2026-08-25T11:56:36Z'
last_seen: '2026-08-29T03:43:33Z'
status: market_context
sources:
- v2ex
- marketfeeds
- newssearch
sightings:
- source: v2ex
  url: https://huggingface.co/datasets/JensCS/top-ml-conference-papers-2024
  seen_at: '2026-08-25T22:45:06Z'
  metrics:
    comments: 1
  kind: product
- source: marketfeeds
  url: https://www.latent.space/p/ainews-nvidia-buys-huggingface-for
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://www.theverge.com/ai-artificial-intelligence/985385/openais-rogue-ai-model-hugging-face-cybersecurity-incident-reports-metr
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://www.technologyreview.com/2026/08/26/1143013/the-inside-story-on-why-openai-agents-hacked-hugging-face/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://arstechnica.com/ai/2026/08/report-nvidia-to-acquire-ai-model-repository-hugging-face-for-13-billion/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://arstechnica.com/security/2026/08/how-openai-let-a-mob-of-llm-agents-game-a-test-and-ransack-hugging-face/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://sifted.eu/articles/nvidia-hugging-face-acquisition-deal/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://tech.eu/2026/08/27/nvidia-agrees-to-buy-hugging-face-for-12-9bn-says-report/
  seen_at: '2026-08-29T03:43:29Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMigAFBVV95cUxNajlLTTI2MDh1WmN2QmR2dlBlS1Jxb2hyU0pPOXh1dGRSand0TnFENlRNZ0dmay1pRVY3aC1aenQtblpIQi1oeXBYSk5zZHJJalVScVQ5WjlTY0xHYWd5M1dIQ1NzMzdYM0Nlb1RHNDBXX0RNUXNvYTFiTnZ5Ym56Rg?oc=5
  seen_at: '2026-08-29T03:43:33Z'
  metrics: {}
  kind: news
---

# Hugging Face

上次我做了一份 2023 年的 AI 论文数据集，有 7000 多篇，没想到还挺受欢迎的👉https://www.v2ex.com/t/1229793?p=1#reply9 ，还有老哥问我啥时候更新。所以今天我又来了。

这次我整理了 2024 年的四大 AI 顶会论文，总共 9817 篇。在等更新的各位可以自取啦👉https://huggingface.co/datasets/JensCS/top-ml-conference-papers-2024

https://i.imgur.com/zIpVT53.png

这次收录的论文来自四场 AI 顶会：

- NeurIPS 2024：3960 篇

- CVPR 2024：2692 篇

- ICLR 2024：2251 篇

- ACL 2024：914 篇

机器学习、计算机视觉、自然语言处理，过去一年几个最活跃的 AI 研究方向，基本都在这里了。

https://i.imgur.com/1UNwgMc.png

这份数据集并不是一份只有标题和摘要的目录。每篇论文都整理了研究领域、具体任务、核心问题、主要创新、方法、基线和实验结果，算下来一共 24 个字段。

数据里还留着论文的原文片段和对应的章节位置。看到一个实验结果，可以顺着位置查一下它是写在主实验、消融实验，还是附录里，不用只信一句脱离上下文的总结了。

接下来我大概讲下怎么用。

平时我们想知道一个方向最近在研究什么，通常要从搜论文开始。但是搜论文你只能搜到一些很浅层的信息，比方说主题、摘要什么的，AI 论文常常涉及到的基线啊、测评集、试验条件啥的，你还是要去自己翻。你读十篇还能靠耐心，面对几千篇论文，靠人一篇篇翻就不太现实了。

所以这时候，你就可以拿到这份数据集，作为一份可以直接筛选和比较的研究材料，去加快你的工作进度。

比如你正在找下一个实验方向，那么你可以先选定任务，再把相关论文的核心问题、主要创新、基线和关键指标摆在一起看。这样哪些问题已经被研究烂了，哪些假设还没有充分验证不可靠，以及哪些方法只在少数数据集上成立，一对比看得清清楚楚。沿着这些缺口继续追，就有机会找到值得验证的新问题。

你也可以把这批数据直接交给 Research Agent 。让它先梳理某个方向的技术路线，归纳不同论文共同依赖的假设，寻找尚未覆盖的场景或相互矛盾的结论，再据此整理 research gap ，提出下一步可验证的实验方向。因为数据里保留了原文片段和章节位置，Agent 给出的判断还能继续回到论文中核对，而不是只剩一段没有出处的总结。

如果不搞科研，那做技术选型也能用上。你可以先找出使用同一评测集的论文，再核对模型规模、基线和实验条件。论文里都说自己效果好，但如果训练资源、数据和评价指标不一样，数字放在一起并没有多少意义。数据集能先帮你把比较范围理顺，最后再回到原文确认。

平时要写报告、做分享，这份数据也能派上用场。比方说一个概念最近是不是真的热，大家是在反复讨论同一个问题，还是已经分出了几条不同的技术路线，都可以从论文里找依据。下次领导问起来，你就可以装一波顶回去，免得他又说你跟时代脱节不进步。

最后，如果你觉得数据集喂 AI 这个想法很有用，但是 AI 研究不是你的方向，那么我也可以给你提供方法，这样你就能拿工具去生成自己领域的数据集了，无论是做工程、通讯、硬件等等的吧，我觉得都能派上用场。

首先，你需要准备你所在领域的论文素材，然后用到的工具是这个——Knowhere ，开源小项目，平常使用基本免费： https://knowhereto.ai/github?utm_source=v2ex

这些论文基本都是 PDF 格式，在人眼里看着规整，交给程序却很容易乱套。因为它有很多双栏正文、跨页表格和图片啥的，直接转成纯文本关系就丢了，文字跟资料对不上。

所以第一步，解析 PDF 。用 Knowhere 识别论文里的文字、表格、公式和版面，把正文整理成带有章节路径的内容片段。这里的 chunk 不是按固定字数随手切开的一段文字，它会同时记录自己来自哪一节。Knowhere 会重建整篇论文的章节树，生成 doc_nav.json 。从一级标题到下面的子章节，每个节点都有自己的标题、路径、层级、摘要和片段数量。

接下来我们再让 LLM 判断论文属于模型架构、方法流程、理论分析还是 Agent 系统，并按类型提取不同信息。Agent 论文重点找环境、工具、规划方式和评测基准；理论论文则关注分析对象、理论工具、主要结论和适用边界。

最后，我们把通用信息、分类后的专属字段、原文片段和章节树装回同一条记录，再导出成 JSONL 和 Parquet 。Hugging Face 数据中的 chunks 和 hierarchy ，就是 Knowhere 解析后保留下来的内容。

这样做出来的不是“9817 份论文摘要合集”，而是一批可以筛选和比较、也能顺着章节路径回到原文核对的研究材料了。

除了 PDF ，Knowhere 也可以处理 Word 、PPT 、图片等常见格式，并输出适合 AI Agent 和 RAG 使用的结构化 chunks 与 JSON 。如果你手里也有一批论文、报告或其他复杂文档，都可以拿去试试。

其他没了，下个月可能还会做一份具身智能论文数据集，覆盖 CoRL 、ICRA 、IROS 、RSS 等机器人领域的重要会议。除了核心问题、方法和实验结果，还会继续往下拆动作空间、观测空间、传感器配置、真实机器人平台，以及 sim-to-real 方法。

有需要的老哥可以先关注一下，谢谢。

## 笔记


