---
slug: github-15
name: Github
builder: hydraegret
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
url: https://github.com/offzen/dsh-gitea-search
canonical_url: https://github.com/offzen/dsh-gitea-search
summary: "终于搓完发布了 #dsh #dsh-gitea-search `欢迎试用、提建议`\r\n\r\n**项目地址**： https://github.com/offzen/dsh-gitea-search\r\
  \n\r\n**开发的动机**：token 不够烧的，还经常因为重复的任务延长等待，无数的 429 限流...原理上很多任务可以在本地加速。\r\n\r\nDSH 的插件机制很适合自己改造，只有一个搜索框显然是太弱了；手动去输脚本使用上不现实。\r\
  \n\r\n**跨会话检索和长期记忆**：用 SQLite 全文索引加快关键词查找，再用向量副库做语义相近内容的检索，方便找回以前的方案、命令和报错等片段。（你通常记得的就只有片段信息，如果让 AI\
  \ 检索会很慢）\r\n  大量代码和信息本来就在本地，不必整包丢给云端模型去耗时间和 token 。本地先找出来，再只把命中的上下文交给模型，交互会更快，也更省上下文。模型看到的是筛过的历史方案、命令和报错，而不是整份会话，回答也会更准。\r\
  \n\r\n原理部分：\r\n[见链接]( https://tof.cloudns.ch/default/95.html)\r\n## 增强 dsh 的搜索-引入 SQLite FTS 索引+向量记忆副库\r\
  \n在 DSH （ DeepSeek Harness ） 及大模型 Agent 架构中，保存会话、上下文并解决“文件保存难以搜索”的问题，通常有两类存储需求：\r\n\r\n会话状态与事件回放（ Session\
  \ State & Event Replay ）：要求保证上下文完整性、严格时序、确定性重放与分支（ Fork ）。\r\n上下文检索与长期记忆（ Context Retrieval & Memory/RAG\
  \ ）：要求能够跨会话精准定位历史方案、命令、错误记录或语义相似内容。\r\n\r\n### 术语解释：rg 逐次扫描 SQLite FTS 索引 向量记忆副库 Qdrant \r\n[见链接]( https://tof.cloudns.ch/tech/98.html)\
  \ 以后再放到 github 文档里 \r\n\r\n在大模型 Agent （代理）架构中引入了 **SQLite FTS (全文索引)** 与 **向量记忆副库**，并将检索功能与本地的 Gitea\
  \ （私有代码托管平台）以及本地历史会话进行了深度绑定。\r\n\r\n### \U0001F6E0️ 它解决了什么核心问题？\r\n\r\n在重度依赖大模型进行开发的场景下，随着会话和代码的积累，AI\
  \ 往往会面临“失忆”或响应缓慢的问题。该项目针对性地解决了以下三大痛点：\r\n\r\n1. **Token 浪费与交互高延迟**\r\n以前大模型处理代码时，往往粗暴地将整个文件或多个文件直接丢给云端。该插件通过本地化检索预检，先在本地筛出相关的历史方案、命令或代码段，**只将精确命中的上下文片段交给大模型**。这大幅减少了\
  \ Token 消耗，并极大提升了响应速度。\r\n2. **海量会话中的“搜索盲区”**\r\nDeepSeek Harness 的原生内置搜索依赖 `rg` (ripgrep) 进行逐次扫描，当会话数据攒积过多时，速度会显著变慢。引入\
  \ SQLite FTS 完美解决了大量文本历史的毫秒级全文检索问题，使得 Agent 能够跨会话迅速捞出曾经遇到的报错或历史方案。\r\n3. **分离“会话状态”与“长期记忆”**\r\n它在架构上将两类不同的存储需求剥离开来：“会话状态”负责保持代码操作的严格时序，支持确定性的分支\
  \ (Fork)；而“记忆副库”则负责像人类的长期记忆一样，通过语义和向量进行跨维度的关联与 RAG （检索增强生成）。\r\n\r\n### ⚖️ 架构解题思路对比：dsh-gitea-search\
  \ vs Codex vs Google AI\r\n\r\n面对海量代码资产和 AI 辅助编写，这三者的解题思路截然不同：\r\n\r\n| 评估维度 | `dsh-gitea-search` (本地增强)\
  \ | Codex (典型的本地 CLI/基础 IDE) | Google AI (Gemini / Code Assist) |\r\n| --- | --- | --- | --- |\r\n|\
  \ **核心机制** | **“四两拨千斤”**：本地极速切片检索，过滤出最相关的碎块再进行推理 | **实时上下文流**：主要依赖当前打开的文档或编辑器传递的可见上下文 | **“力大砖飞”**：超大上下文窗口（如\
  \ 200 万 Token ），直接在云端全量解析工程 |\r\n| **跨会话持久记忆** | 极强。通过常驻系统的 SQLite+向量库构建持续跨时间的个人知识库 | 弱。属于每会话进程（非常驻），重启或关闭进程后通常就丢失了上文\
  \ | 强，但依赖云端的对话历史、项目缓存以及全托管的云端 RAG 方案 |\r\n| **隐私与控制权** | **极致本地化**。建库、向量化均在本地服务器，无关代码坚决不出境 | 中等。高度依赖云端\
  \ API 进行处理，受限于具体的服务隐私条款 | 中/高（企业级合规）。代码资产必须上传到 Google Cloud 闭环中进行计算 |\r\n| **极客魔改潜力** | 极高。作为声明式插件，无需深入编译源码即可低成本改造出专属本地引擎\
  \ | 低。一般为闭源产品或黑盒调用，普通用户很难干涉其底层检索和拼接逻辑 | 低。开箱即用但缺乏底层架构的透明度，与大厂生态深度绑定 |\r\n\r\n实际执行效果：![Screenshot 2026-10-24\
  \ at 14-15-48 dsh-gitorca-search 的搜索技巧和对比默认的 DSH session_search - General - whY The AI.png][1]\r\n\r\
  \n  [1]: https://tof.cloudns.ch/usr/uploads/2026/10/2383904717.png"
first_seen: '2026-10-25T00:21:00Z'
last_seen: '2026-10-25T00:21:00Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/offzen/dsh-gitea-search
  seen_at: '2026-10-25T00:21:00Z'
  metrics:
    comments: 0
  kind: product
---

# Github

终于搓完发布了 #dsh #dsh-gitea-search `欢迎试用、提建议`

**项目地址**： https://github.com/offzen/dsh-gitea-search

**开发的动机**：token 不够烧的，还经常因为重复的任务延长等待，无数的 429 限流...原理上很多任务可以在本地加速。

DSH 的插件机制很适合自己改造，只有一个搜索框显然是太弱了；手动去输脚本使用上不现实。

**跨会话检索和长期记忆**：用 SQLite 全文索引加快关键词查找，再用向量副库做语义相近内容的检索，方便找回以前的方案、命令和报错等片段。（你通常记得的就只有片段信息，如果让 AI 检索会很慢）
  大量代码和信息本来就在本地，不必整包丢给云端模型去耗时间和 token 。本地先找出来，再只把命中的上下文交给模型，交互会更快，也更省上下文。模型看到的是筛过的历史方案、命令和报错，而不是整份会话，回答也会更准。

原理部分：
[见链接]( https://tof.cloudns.ch/default/95.html)
## 增强 dsh 的搜索-引入 SQLite FTS 索引+向量记忆副库
在 DSH （ DeepSeek Harness ） 及大模型 Agent 架构中，保存会话、上下文并解决“文件保存难以搜索”的问题，通常有两类存储需求：

会话状态与事件回放（ Session State & Event Replay ）：要求保证上下文完整性、严格时序、确定性重放与分支（ Fork ）。
上下文检索与长期记忆（ Context Retrieval & Memory/RAG ）：要求能够跨会话精准定位历史方案、命令、错误记录或语义相似内容。

### 术语解释：rg 逐次扫描 SQLite FTS 索引 向量记忆副库 Qdrant 
[见链接]( https://tof.cloudns.ch/tech/98.html) 以后再放到 github 文档里 

在大模型 Agent （代理）架构中引入了 **SQLite FTS (全文索引)** 与 **向量记忆副库**，并将检索功能与本地的 Gitea （私有代码托管平台）以及本地历史会话进行了深度绑定。

### 🛠️ 它解决了什么核心问题？

在重度依赖大模型进行开发的场景下，随着会话和代码的积累，AI 往往会面临“失忆”或响应缓慢的问题。该项目针对性地解决了以下三大痛点：

1. **Token 浪费与交互高延迟**
以前大模型处理代码时，往往粗暴地将整个文件或多个文件直接丢给云端。该插件通过本地化检索预检，先在本地筛出相关的历史方案、命令或代码段，**只将精确命中的上下文片段交给大模型**。这大幅减少了 Token 消耗，并极大提升了响应速度。
2. **海量会话中的“搜索盲区”**
DeepSeek Harness 的原生内置搜索依赖 `rg` (ripgrep) 进行逐次扫描，当会话数据攒积过多时，速度会显著变慢。引入 SQLite FTS 完美解决了大量文本历史的毫秒级全文检索问题，使得 Agent 能够跨会话迅速捞出曾经遇到的报错或历史方案。
3. **分离“会话状态”与“长期记忆”**
它在架构上将两类不同的存储需求剥离开来：“会话状态”负责保持代码操作的严格时序，支持确定性的分支 (Fork)；而“记忆副库”则负责像人类的长期记忆一样，通过语义和向量进行跨维度的关联与 RAG （检索增强生成）。

### ⚖️ 架构解题思路对比：dsh-gitea-search vs Codex vs Google AI

面对海量代码资产和 AI 辅助编写，这三者的解题思路截然不同：

| 评估维度 | `dsh-gitea-search` (本地增强) | Codex (典型的本地 CLI/基础 IDE) | Google AI (Gemini / Code Assist) |
| --- | --- | --- | --- |
| **核心机制** | **“四两拨千斤”**：本地极速切片检索，过滤出最相关的碎块再进行推理 | **实时上下文流**：主要依赖当前打开的文档或编辑器传递的可见上下文 | **“力大砖飞”**：超大上下文窗口（如 200 万 Token ），直接在云端全量解析工程 |
| **跨会话持久记忆** | 极强。通过常驻系统的 SQLite+向量库构建持续跨时间的个人知识库 | 弱。属于每会话进程（非常驻），重启或关闭进程后通常就丢失了上文 | 强，但依赖云端的对话历史、项目缓存以及全托管的云端 RAG 方案 |
| **隐私与控制权** | **极致本地化**。建库、向量化均在本地服务器，无关代码坚决不出境 | 中等。高度依赖云端 API 进行处理，受限于具体的服务隐私条款 | 中/高（企业级合规）。代码资产必须上传到 Google Cloud 闭环中进行计算 |
| **极客魔改潜力** | 极高。作为声明式插件，无需深入编译源码即可低成本改造出专属本地引擎 | 低。一般为闭源产品或黑盒调用，普通用户很难干涉其底层检索和拼接逻辑 | 低。开箱即用但缺乏底层架构的透明度，与大厂生态深度绑定 |

实际执行效果：![Screenshot 2026-10-24 at 14-15-48 dsh-gitorca-search 的搜索技巧和对比默认的 DSH session_search - General - whY The AI.png][1]

  [1]: https://tof.cloudns.ch/usr/uploads/2026/10/2383904717.png

## 笔记


