---
slug: opencodex
name: Opencodex
verdict: 有待观察
analyzed_at: 2026-08-14
---

## 一句话定位

装进 VSCode 就能用的免费开源编程 agent——不用注册、不用 API key，
选个免费模型就能让 AI 在编辑器里帮你改代码。

## 做这个东西的人

GitHub 用户 matonhp5108，个人项目，MIT 协议，TypeScript。2026-08-08 首次提交，
两周 12 次提交，41 star / 10 fork。已上架 VSCode Marketplace
（扩展 ID：EvaanChowdhry.opencodex-agent）。

_判断：又一个"插件即分发"的 VSCode agent，走的是 Cline 验证过的路径——
用户已经在编辑器里了，不用教育他换工具。README 写得很完整，像是认真
做过一轮竞品研究后动手的，不是随手 demo。_

## 它到底能做哪几件事

- **零门槛起步** → 默认 OpenCode 免费模型，无需账号、无需 API key，
  装完选个模型就能用
- **多提供商切换** → OpenRouter（`:free` 模型）、Groq、Google Gemini、
  Mistral、Ollama（本地）；密钥存 VS Code SecretStorage，不写进 settings.json
- **完整 agent 能力** → 读写搜索文件、执行命令、diff 预览、持久终端
  （跨对话存活）、子代理（委派探索/审查/实现）、MCP 工具调用、多步计划展示
- **三档审批模式** → Ask（全部确认）/ Auto edits（文件自动、命令确认）/
  Open access（全自动），破坏性命令永远要确认
- **技能市场** → 从 SkillsMP 或 GitHub 发现、预览、安装 `SKILL.md` 技能包，
  全工作区生效
- **项目记忆** → 每个 VS Code 文件夹独立聊天历史 + 恢复点（可回滚到
  agent 操作前的状态）+ `.opencodex/memory.md` 记忆文件 + token 用量统计

**安全边界**：文件工具限制在工作区内，`.env` 等凭证文件被阻止访问。

## 它在替代什么旧行为

以前在 VSCode 里要"agent 化编码"，只有两条路，都有一道门槛：

**装 Cline / Copilot**。Copilot 要登录订阅，Cline 要 API key 或订阅。
对不想付费、不想绑定单一供应商的开发者，这是劝退点。

**离开编辑器用 Codex CLI / Claude Code 终端版**。好用但工作流割裂——
代码在编辑器里，agent 在终端里，改完还要回编辑器看。

Opencodex 把门槛砍到零：不注册、不付费、模型可换（还能用本地 Ollama），
全在 VSCode 里。它替代的是"为了用 agent 编程必须先交钱或先注册"
这个旧动作。

## 商业模式

**免费开源，无云服务、无付费档。** MIT 协议，个人项目。

_判断：没有商业模式，甚至没有商业模式假设。它靠的是 VSCode Marketplace
这个免费分发渠道。这类项目的现实结局通常是两种——被更多人用起来成为
生态一环，或者作者热情耗尽停在某个版本。_

## 硬数字

- **41 star / 10 fork**，MIT，TypeScript，2026-08-08 首提交，12 commits
- VSCode Marketplace 已上架（EvaanChowdhry.opencodex-agent）
- HN 6 分 / 1 条评论（2026-08-11），讨论热度接近零
- 支持：OpenCode（免费，默认）/ OpenRouter / Groq / Gemini / Mistral / Ollama
- 要求：VSCode 1.106.0+；云提供商需联网
- 下载量、用户数：未披露（Marketplace 未读到）

## 四维评估

| 维度 | 结论 |
|------|------|
| 创始人-产品匹配度 | 个人项目，痛点（付费墙 + 绑定供应商）真实但非创始人独有，匹配度一般 |
| 产品洞察力 | 差异化是"零门槛 + 多提供商 + 本地模型"，方向对但都是可被复制的特性，没有独家洞察 |
| 技术实现质量 | README 完整、功能面广（子代理/MCP/技能市场/恢复点），工程是认真做的 |
| 市场时机 | VSCode agent 赛道已经拥挤（Cline、Continue 等），新入场者要靠差异化或先发，两者都不明显 |

## 判断

**数据薄，判断只能按数据来：有待观察。**
HN 只有 6 分，41 star，无用户数据——按简报的规矩，这属于"真实热度未证明"，
诚实给观察级。

**但方向值得记一笔**：Cline 已经证明了"VSCode 里的开源编程 agent"有真实
需求，Opencodex 的差异化是"免费 + 不注册 + 模型随意换（含本地 Ollama）"。
在付费订阅疲劳的 2026 年，这个卖点是有一批真实受众的——问题是这批受众
里有多少会沉淀在它身上。

**最大的风险不是竞争，是维护**。个人开源的 VSCode 扩展，生命周期取决于
作者的业余时间。VSCode 版本一更新、MCP 协议一演进，跟不上就废了。
这类项目五成死在"作者不再更新"。

## 下一步看什么

① Marketplace 上能否看到下载量和评分——那才是真实的用户信号
② 三个月后 star 能否破 200——个人 agent 项目过不了 200 基本就停在兴趣项目
③ 免费模型 provider（OpenCode/Groq 免费层）的稳定性——免费层经常变，
  这是它"零门槛"卖点的地基

## 可借鉴的做法

**产品逻辑**："插件是获客成本最低的分发渠道"这句话对，但有个前提——
你的差异化必须用户在 30 秒内感受到。Opencodex 用"装完不用登录就能用"
做第一个感知点，这个切入顺序是对的。

**话术**：无。README 是功能清单，没有可偷的句式。

**定价结构**：无。未披露。

## 结论

**有待观察。** 方向有真实市场背书（Cline 证明过），零门槛卖点清晰，
但当前数据完全不足以判断它能不能起来——6 分热度、无用户数据、个人维护。
三个月后拿上面三条验证，重点看 Marketplace 下载量和 star 是否过 200。
