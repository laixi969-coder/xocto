---
slug: omnibase
name: omnibase
verdict: 值得关注
analyzed_at: 2026-08-14
---

## 一句话定位

把 agent 从"一次性聊天人格"变成有职位、有版本、有项目上下文、有可审计
运行记录的数字员工——而且整套东西自托管，数据不离开你的服务器。

## 做这个东西的人

GitHub 用户 lss100200，开源项目（Apache-2.0，Python/FastAPI + Next.js + pgvector），
目前是 Public Preview 状态。官网 omnibase.chat 有一篇写得很诚实的长文：
"我们只展示真实完成和真实正在建设的部分"，生产级多 Agent Runtime 明确保持关闭。

_判断：这是典型的 build-in-public 自托管基建项目。最值得注意的不是功能，
是它敢在官网明说"生产 Runtime 还关着、多 Agent 还在路线图上"——开源项目
里这种诚实很少见，通常大家宁可吹一个还没做完的 demo。_

## 它到底能做哪几件事

- **Personal model gateway** → 配置自己的 OpenAI-compatible Provider，
  存 API Key，保存前后可以真实测连接
- **Workspace 隔离** → 每个项目一个独立上下文：成员、Agent、知识、任务、
  运行记录都绑定到 Workspace，不再散落在聊天历史里
- **Agent 生命周期管理** → AgentDefinition（职位/职责）→ AgentVersion
  （工作手册与 Skills）→ WorkspaceBinding（任命到项目）→ AgentRun（一次
  具体工作班次），状态机 draft → trial → sealed → appointed
- **Task/Run 审计账本** → 每次真实模型调用都留持久记录，可回滚可审计
- **自托管 RAG** → 知识检索限制在 Workspace 边界内，引用回链，只读
  knowledge_search 受租户/预算/审计边界约束
- **角色语言** → 定义了 Workspace Steward、Explorer、Builder、Verifier、
  Knowledge Curator、Operator 六个角色，但当前只保证单 Agent 可靠闭环

**当前真实能力边界**：个人 Provider + 连接测试 + Workspace + Agent Builder +
"无工具的单 Agent 模型调用" + Task/Run 持久化 + 只读知识检索。
工具调用（Typed Executor）、多 Agent Runtime、生产 Runtime 都在关闭状态。

## 它在替代什么旧行为

以前想把 agent 用进真实业务，两条路都不干净：

**用 SaaS agent 平台（Dify、Coze 这类）**。知识库、模型密钥、运行记录全在
别人服务器上。对在意数据的企业，这一步就卡死了。

**自己拼**。接模型 API、建知识库、写 agent 调度、记账——每个环节都有工具，
但没有一个把"知识 + RAG + 模型供应商 + agent + 运行记录"放进同一个
可维护的工作台。结果是上下文散落在聊天历史里，agent 每次开工都不知道
"上次干到哪、为哪个项目干的、花了多少钱"。

OmniBase 替代的正是这两件事：把数据留在本地的自托管底座，加上把 agent
从聊天人格升级成"有职位、有版本、有项目归属、有审计记录"的数字员工
这套管理模型。

## 商业模式

**未披露。** Apache-2.0 开源，Public Preview，无定价页。

_判断：自托管基建的钱历来在"企业版 + 支持服务"上——多租户、SSO、
生产 Runtime 稳定后才谈得上收费。现在连生产 Runtime 都还关着，
商业模式谈不上，谈的是"先证明单 Agent 可靠闭环"。_

## 硬数字

- **166 star / 4 fork / 4 open issues**，Apache-2.0，Python + Next.js + pgvector
- Public Preview 状态；生产 Agent Runtime 保持 gated
- 路线图自述：已具备 = 单 Agent 无工具真实调用 + Task/Run 账本 + 自托管 RAG；
  在建 = Planner / Typed Executor / Capability Gateway / Desktop；
  后续 = 多 Agent Runtime、Self-Development、Hardened Production Runtime
- 团队人数、企业用户数：未披露

## 四维评估

| 维度 | 结论 |
|------|------|
| 创始人-产品匹配度 | 自托管需求真实（企业不想交数据），作者显然自己用过才写得出这种诚实路线图 |
| 产品洞察力 | 把 agent 建模成"有职位/版本/项目归属/审计记录的数字员工"是管理视角的差异化；"一 Agent 先可靠再谈多 Agent"的顺序也对 |
| 技术实现质量 | 角色语言、版本状态机、审计账本设计完整；但当前只有无工具的裸调用，离产品闭环还远 |
| 市场时机 | 自托管 AI 基建是长期存在的一块市场；但 2026 年竞争激烈（Dify 等已在做自托管 agent 平台），差异化要靠"管理模型"而非"又能跑一个 agent" |

## 判断

**定位和诚实度都值得关注，但功能仍在很早期。**
"自托管 AI 工作台 + agent 数字员工管理"这个组合是有差异化的：
别人在赛"谁家 agent 跑得多"，它在赛"谁家能把一个 agent 管清楚"——
职位、版本、任命、审计，这是一套把 agent 当正式员工而非玩具的框架，
方向对。

**但要注意三点**：
一是**当前能力离"闭环"还有距离**。官网自己写"真实无工具单 Agent
模型调用"——没有工具调用，agent 就不能真的做事，这是最小的闭环。
二是**多 Agent 和工具执行都在路线图**，意味着现在看它等于看一个
宣言，判断依据主要靠"路线图诚实 + 代码公开"。
三是**自托管市场不缺入场者**。Dify 已经开源自托管，模型网关、
RAG、工作台都有人做，OmniBase 的差异化最终要靠那套"管理模型"
能不能做深——比如真正可审计的 Agent 运行账本、版本回滚。

**给"值得关注"**：166 star 说明有一些关注度，但主要是"定位 + 诚实"
值得研究，产品本身要等工具调用和多 Agent 落地后再回访。

## 下一步看什么

① 三个月内 Typed Executor（工具调用）是否进入主线——没有工具的单 Agent 不算闭环
② 生产 Agent Runtime 何时解锁、解锁后有没有真实部署案例
③ star 增长与社区 issue 的质量——自托管基建靠社区验证，慢即是死

## 可借鉴的做法

**产品逻辑**：任何"agent 平台"类产品都值得抄它的生命周期模型——
Definition（职位）→ Version（工作手册）→ Binding（任命）→ Run（班次）。
把 agent 当员工管理（有职位描述、有版本变更、有项目归属、有每次工作的
审计记录），比"给个聊天窗口"高一个管理维度。

**话术**："先让一个 Agent 可靠工作，再按任务需要扩展角色"——
这个上线顺序的表述值得所有做 agent 产品的人引用。

**定价结构**：无。未披露。

## 结论

**值得关注。** 定位有差异化（把 agent 当数字员工管理 + 自托管）、
路线图诚实（生产 Runtime 明说关着）、代码公开可验证。但当前能力
还停在无工具的裸调用，判断它"成不成"至少要等工具执行和多 Agent 落地。
三个月后拿上面三条验证。
