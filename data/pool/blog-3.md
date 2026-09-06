---
slug: blog-3
name: llmdoc
builder: pDJJq
category: AI + 开发
summary_zh: 软件工程师在指挥 AI 编码助手处理复杂代码库时打开此工具。它接收代码库的架构设计与领域决策文档，通过结构化元数据和 CLI 程序化匹配当前任务所需的关键上下文并随代码做版本控制，让编码智能体直接获取准确的技术约束与既有实现，减少上下文污染与重复造轮子。
inspiration: AI 辅助编程的瓶颈正从模型推理能力转向代码库上下文供给的信噪比。创业切入点不是通用提示词工程，而是为特定技术栈或大型企业遗留系统提供与 Git 工作流绑定的代码决策管理与自动化上下文裁剪方案。
summary_en: Software engineers use this tool when guiding AI coding agents in complex repositories. It
  manages architecture designs and domain docs with structured metadata, programmatically feeding the
  right context into agents via CLI while syncing with Git commits to prevent hallucinations and redundant
  code.
inspiration_en: The bottleneck in AI coding is shifting from model reasoning to repository context quality.
  The entry point is providing automated codebase context curation tightly bound to Git workflows for
  specific stacks or legacy enterprise systems.
priority_review: false
project_type: open_source
industries:
- 软件开发
- 信息技术
industries_en:
- Software Development
- Information Technology
jobs:
- 软件工程师
- 架构师
jobs_en:
- Software Engineer
- Software Architect
regions:
- 全球
regions_en:
- Global
open_source: true
url: https://blog.pdjjq.org/post/llmdoc-solving-the-last-100-meters-of-ai-coding-z2tuegp#:~:text=%E5%BC%80%E5%A7%8B%E8%A7%A3%E5%86%B3%E9%97%AE%E9%A2%98.-,Context%20Floor,-%23
canonical_url: https://blog.pdjjq.org/post/llmdoc-solving-the-last-100-meters-of-ai-coding-z2tuegp
summary: "# 标题的说明\r\n\r\n标题有一点夸大, 其实应该是 2.9 亿 ARR, 四舍五入其实差不多, 当然了其实是两家公司的两家产品加起来的 ARR \U0001F62D\r\n\r\
  \n在前司主要负责公司的 AI/Agent 建设, 同时也比较深入的参与了业务的开发, 一些开发上的尤其是 人&人, 人&AI 的协作的痛点感知还是非常清晰的.\r\n\r\n我相信我列出的问题肯定不止一个人遇到过:\r\
  \n\r\n1. AI 写的代码没有沿用默认的技术框架/方案\r\n2. 需要在 Coding 前不断地输入/纠正\r\n3. 已经有的解决方案/函数/包库没有直接用, 又造了一堆轮子\r\n4. 明明纠正过很多次,\
  \ 同样的错误在下一次又犯病\r\n5. 使用的 memory 没有版本化管理, 代码回滚/合并了, memory 没有更新\r\n6. 给了目标之后, 用了巨多时间巨多 context, 读取了 N\
  \ 多文件, 问了 N 个问题, 然后在过了甜点 context 阈值的情况下开始工作, 写的乱七八糟\r\n\r\n# context floor\r\n\r\n我曾经给很多人表达过一个观点: Agent\
  \ 完成工作的好坏, 取决于 context 的丰富程度\r\n\r\n这里有几个需要说明的地方:\r\n\r\n1. 工作的好坏: 这里是靠人判断的, 架构是否合理, 抽象是否清晰, 是不是没有重复造轮子...\r\
  \n2. Context 的丰富程度: 这里指的是和\"完成目标\"相关的 Context, 尽可能的多而且不重复, 在 context 无限大, 甜点 window 无限长的情况下, 最好的方案是把代码库+架构+db+UI+PRD\
  \ 全都塞进去\r\n\r\n换句话说: 如果有办法能够稳定的为 Agent 提供良好的快速到达满足工作条件的 Context 路径, 就能提升 Agent 的工作效果和工作效率\r\n\r\n> context\
  \ floor 只是我臆造的一个名词, 大家不用搜索, 我在一篇[早期的 blog]( https://blog.pdjjq.org/post/llmdoc-solving-the-last-100-meters-of-ai-coding-z2tuegp#:~:text=%E5%BC%80%E5%A7%8B%E8%A7%A3%E5%86%B3%E9%97%AE%E9%A2%98.-,Context%20Floor,-%23)\
  \ 里简单的说了一下, 大家不用关心\r\n\r\n# llmdoc\r\n\r\n好了, 为了引出正文已经瞎扯了很多了\r\n\r\n> Github: https://github.com/TokenRollAI/llmdoc\r\
  \n>\r\n> llmdoc 首页: https://llmdoc.tokenroll.ai/\r\n\r\n### 还是文档\r\n\r\n如果有一种内容, 一种 AI 产生的内容, 是比代码更高的抽象层次,\
  \ 而且有足够好的阅读性和可理解性, 能够指导写代码, 它会是什么?\r\n\r\n我的答案是**文档**\r\n\r\n如果你已经想到让 AI 自动维护一个文档文件夹, 代码更新之后自动维护, 那么你已经理解了\
  \ llmdoc 了\r\n\r\n这就是最开始的 llmdoc \U0001F601\r\n\r\n### 不仅仅是文档\r\n\r\n可是只靠文档就够了吗?\r\n\r\n尤其是代码库的文档, 我们会发现:\
  \ 适合人阅读的文档, 不一定适合 AI, but why?\r\n\r\n最常用的文档组织形式是: [diataxis]( https://diataxis.fr/)\r\n\r\n也就是类似: overview\
  \ + guide + tutorials + reference ... 这样的组织形式, 经常看技术文档的朋友看到这几个名词应该不会默认\r\n\r\n但是在实践中, 这可能不是最好的组织形式\r\
  \n\r\n1. Agent 能够极为快速的\"Read\"(其实准确来说是 Load), 如果表达一个 Topic 的不同文档, 过于分散, 反而是在降低效率\r\n2. Agent 不需要太过于细粒度的内容,\
  \ 粒度再细也不会超过文档来源(代码), 这种情况下不如直接读代码\r\n\r\n### 一个更好的组织形式\r\n\r\n在之前的 v2 版本的 llmdoc 中, 使用的文档结构是优化版本的[diataxis](\
  \ https://diataxis.fr/), 额外加了一个反思层 + index.md 用来帮助 Agent 判断哪些要读, 哪些不要读\r\n\r\n这是有用的, 但是有用的不是文档的组织形式,\
  \ 而是文档内容, 实际 Agent 在读文档时还是经常会判断不准确文档和文档之间的关联...\r\n\r\n##### not only md\r\n\r\nmd 的格式没有问题, 但是 纯靠 md\
  \ 无法结构化的表达文档和文档的关系, 文档和代码的关系, topic/domain 和文档的关系...\r\n\r\n一个简单的解决方案是: 增加 yaml frontier\r\n\r\n在 yaml\
  \ 中做这些结构化的表达\r\n\r\n同时为了一些扩展性, 这里用了 mdx 格式 (可能不是个好主意\U0001F62D)\r\n\r\n##### 程序化的判断\r\n\r\nAgent 可以判断很多事情,\
  \ 代价是每判断一次, 就要烧 token\r\n\r\n程序化判断的好处有这么几个:\r\n\r\n1. 不可变的结论, 不会因为 Agent 主观判断而发生变化, 尤其是在代码和文档不一致时非常有用\r\
  \n2. 免费\r\n\r\n##### topic by topic\r\n\r\n按照一个\"topic\"组织文档, 这里的 topic 可以是一个业务 domain, 可以是 cicd, 可以是\
  \ release...\r\n\r\n总之, 对于 codebase 来说, 最好不要是按照层级来划分的\r\n\r\n过多的层级, 过于强调渐进式暴露, 反而会对 Agent 的性能有影响\r\n\
  \r\n按照 Topic 划分的另一个好处是, 一般来说一个任务需要的 Topic 不会太多, Agent 可以快速的知道 Topic 的大概, 知道要读写哪些文件, 这会非常快速的构成 context\
  \ floor(我没有更好的表达方式了, 请原谅)\r\n\r\n# llmdoc V3\r\n\r\n> 一个示例的 llmdoc: https://github.com/TokenRollAI/llmdoc/tree/main/llmdoc\r\
  \n>\r\n> 是的, llmdoc 本身是自举的\U0001F601\r\n\r\n在前几天推出的 V3 版本中, 结合长期的实践, 我们做了[这样]( https://github.com/TokenRollAI/llmdoc/issues/32)的设计:\r\
  \n\r\n1. 不改变 llmdoc 的核心定位: 一个跟随代码做版本控制的外置 context provider\r\n2. doc 中保留最关键的信息: 决策/架构/设计\r\n3. 用稳定的\
  \ cli 替代掉 hook sh\r\n4. 更好的支持 diff code 和 doc 的 gap\r\n5. 文档增加 meta info 用来承担 description 和 related\
  \ code file\r\n6. 更适合 AI 的文档组织形式: 按照 topic 和 domain 划分, 适合快速阅读\r\n\r\n好了, 这就是目前的完全体了, 他目前支持 Claude Code\
  \ / Codex / 其他适配 Agent Plugin 标准的产品\r\n\r\n一个可以完全适配 任何工作流, 任何 Skill 的外挂的 Context Provider\r\n\r\n没有上手成本,\
  \ 有完成的 cli/plugin/skill/hooks 支持\r\n\r\n我的个人项目也在长期使用, 效果不错, 强烈推荐\r\n\r\n---\r\n\r\n[点点 Star]( https://github.com/TokenRollAI/llmdoc)\
  \ 更有帮助哦, 如果大家有问题也欢迎 Issue / PR / 评论区提问"
first_seen: '2026-09-04T07:10:15Z'
last_seen: '2026-09-05T13:28:57Z'
status: watching
sources:
- v2ex
- newssearch
sightings:
- source: v2ex
  url: https://blog.pdjjq.org/post/llmdoc-solving-the-last-100-meters-of-ai-coding-z2tuegp#:~:text=%E5%BC%80%E5%A7%8B%E8%A7%A3%E5%86%B3%E9%97%AE%E9%A2%98.-,Context%20Floor,-%23
  seen_at: '2026-09-04T14:23:24Z'
  metrics:
    comments: 0
  kind: product
- source: newssearch
  url: https://news.google.com/rss/articles/CBMia0FVX3lxTE1mcGdOVXFkUndzSXpZN0o0d0ZOSTBiQ2xDUldvbWdQVUVBYkVPVnBEclJUU3p1S2puOEVtcFlSVUphUUgxZHhPOHBqejg4NWxPRWlSS2dVaEhHaGtnRW1YWE1idWVJRHdsbFdZ?oc=5
  seen_at: '2026-09-05T13:28:57Z'
  metrics: {}
  kind: news
---

# llmdoc

# 标题的说明

标题有一点夸大, 其实应该是 2.9 亿 ARR, 四舍五入其实差不多, 当然了其实是两家公司的两家产品加起来的 ARR 😭

在前司主要负责公司的 AI/Agent 建设, 同时也比较深入的参与了业务的开发, 一些开发上的尤其是 人&人, 人&AI 的协作的痛点感知还是非常清晰的.

我相信我列出的问题肯定不止一个人遇到过:

1. AI 写的代码没有沿用默认的技术框架/方案
2. 需要在 Coding 前不断地输入/纠正
3. 已经有的解决方案/函数/包库没有直接用, 又造了一堆轮子
4. 明明纠正过很多次, 同样的错误在下一次又犯病
5. 使用的 memory 没有版本化管理, 代码回滚/合并了, memory 没有更新
6. 给了目标之后, 用了巨多时间巨多 context, 读取了 N 多文件, 问了 N 个问题, 然后在过了甜点 context 阈值的情况下开始工作, 写的乱七八糟

# context floor

我曾经给很多人表达过一个观点: Agent 完成工作的好坏, 取决于 context 的丰富程度

这里有几个需要说明的地方:

1. 工作的好坏: 这里是靠人判断的, 架构是否合理, 抽象是否清晰, 是不是没有重复造轮子...
2. Context 的丰富程度: 这里指的是和"完成目标"相关的 Context, 尽可能的多而且不重复, 在 context 无限大, 甜点 window 无限长的情况下, 最好的方案是把代码库+架构+db+UI+PRD 全都塞进去

换句话说: 如果有办法能够稳定的为 Agent 提供良好的快速到达满足工作条件的 Context 路径, 就能提升 Agent 的工作效果和工作效率

> context floor 只是我臆造的一个名词, 大家不用搜索, 我在一篇[早期的 blog]( https://blog.pdjjq.org/post/llmdoc-solving-the-last-100-meters-of-ai-coding-z2tuegp#:~:text=%E5%BC%80%E5%A7%8B%E8%A7%A3%E5%86%B3%E9%97%AE%E9%A2%98.-,Context%20Floor,-%23) 里简单的说了一下, 大家不用关心

# llmdoc

好了, 为了引出正文已经瞎扯了很多了

> Github: https://github.com/TokenRollAI/llmdoc
>
> llmdoc 首页: https://llmdoc.tokenroll.ai/

### 还是文档

如果有一种内容, 一种 AI 产生的内容, 是比代码更高的抽象层次, 而且有足够好的阅读性和可理解性, 能够指导写代码, 它会是什么?

我的答案是**文档**

如果你已经想到让 AI 自动维护一个文档文件夹, 代码更新之后自动维护, 那么你已经理解了 llmdoc 了

这就是最开始的 llmdoc 😁

### 不仅仅是文档

可是只靠文档就够了吗?

尤其是代码库的文档, 我们会发现: 适合人阅读的文档, 不一定适合 AI, but why?

最常用的文档组织形式是: [diataxis]( https://diataxis.fr/)

也就是类似: overview + guide + tutorials + reference ... 这样的组织形式, 经常看技术文档的朋友看到这几个名词应该不会默认

但是在实践中, 这可能不是最好的组织形式

1. Agent 能够极为快速的"Read"(其实准确来说是 Load), 如果表达一个 Topic 的不同文档, 过于分散, 反而是在降低效率
2. Agent 不需要太过于细粒度的内容, 粒度再细也不会超过文档来源(代码), 这种情况下不如直接读代码

### 一个更好的组织形式

在之前的 v2 版本的 llmdoc 中, 使用的文档结构是优化版本的[diataxis]( https://diataxis.fr/), 额外加了一个反思层 + index.md 用来帮助 Agent 判断哪些要读, 哪些不要读

这是有用的, 但是有用的不是文档的组织形式, 而是文档内容, 实际 Agent 在读文档时还是经常会判断不准确文档和文档之间的关联...

##### not only md

md 的格式没有问题, 但是 纯靠 md 无法结构化的表达文档和文档的关系, 文档和代码的关系, topic/domain 和文档的关系...

一个简单的解决方案是: 增加 yaml frontier

在 yaml 中做这些结构化的表达

同时为了一些扩展性, 这里用了 mdx 格式 (可能不是个好主意😭)

##### 程序化的判断

Agent 可以判断很多事情, 代价是每判断一次, 就要烧 token

程序化判断的好处有这么几个:

1. 不可变的结论, 不会因为 Agent 主观判断而发生变化, 尤其是在代码和文档不一致时非常有用
2. 免费

##### topic by topic

按照一个"topic"组织文档, 这里的 topic 可以是一个业务 domain, 可以是 cicd, 可以是 release...

总之, 对于 codebase 来说, 最好不要是按照层级来划分的

过多的层级, 过于强调渐进式暴露, 反而会对 Agent 的性能有影响

按照 Topic 划分的另一个好处是, 一般来说一个任务需要的 Topic 不会太多, Agent 可以快速的知道 Topic 的大概, 知道要读写哪些文件, 这会非常快速的构成 context floor(我没有更好的表达方式了, 请原谅)

# llmdoc V3

> 一个示例的 llmdoc: https://github.com/TokenRollAI/llmdoc/tree/main/llmdoc
>
> 是的, llmdoc 本身是自举的😁

在前几天推出的 V3 版本中, 结合长期的实践, 我们做了[这样]( https://github.com/TokenRollAI/llmdoc/issues/32)的设计:

1. 不改变 llmdoc 的核心定位: 一个跟随代码做版本控制的外置 context provider
2. doc 中保留最关键的信息: 决策/架构/设计
3. 用稳定的 cli 替代掉 hook sh
4. 更好的支持 diff code 和 doc 的 gap
5. 文档增加 meta info 用来承担 description 和 related code file
6. 更适合 AI 的文档组织形式: 按照 topic 和 domain 划分, 适合快速阅读

好了, 这就是目前的完全体了, 他目前支持 Claude Code / Codex / 其他适配 Agent Plugin 标准的产品

一个可以完全适配 任何工作流, 任何 Skill 的外挂的 Context Provider

没有上手成本, 有完成的 cli/plugin/skill/hooks 支持

我的个人项目也在长期使用, 效果不错, 强烈推荐

---

[点点 Star]( https://github.com/TokenRollAI/llmdoc) 更有帮助哦, 如果大家有问题也欢迎 Issue / PR / 评论区提问

## 笔记


