---
slug: godmode
name: godmode
verdict: 有待观察
analyzed_at: 2026-08-14
---

## 一句话定位

给你已经会写代码的编码 agent 补上"工程行为"：一份可组合的 Agent Skills 目录，
让 agent 先设计再动手、先测试再声称完成、独立审查、用新证据验证。

## 做这个东西的人

thiientv，个人项目。仓库 2026-08-12 左右建，12 个 commit，两天内完成初版和配套工具链。

_判断：把软件工程实践（TDD、审查、发布、事故响应）封装成技能的思路本身不新，但这个仓库的
完成度——14 个核心 workflow 技能加 19 个工程能力技能、带行为评测 harness 和仓库门禁——
说明作者是把它当产品在打磨，不是当帖子发。_

## 它到底能做哪几件事

- **组合式技能目录** → 不用一个巨型 prompt，而是可发现、可组合的技能包：
  solution-design、implementation-planning、TDD、root-cause-debugging、code-review 等
- **14 个核心 workflow 技能** → 从 using-godmode、plan-execution 到 dispatching-parallel-agents、
  subagent-driven-development、using-git-worktrees
- **19 个工程能力技能** → frontend-design、api-and-interface-design、database-design、
  security-and-hardening、release-engineering、incident-response、agent-evaluation 等
- **确定性辅助工具** → 不只是 Markdown 提示，重复易错的工作带脚本：
  design_system.py、extract_design_system.py、audit_ui.py
- **兼容多种客户端** → 标准 Agent Skills 布局，Claude Code（plugin）和 Codex
  （.codex-plugin + marketplace）都可用
- **行为评测 harness** → 自带 behavior eval 跑核心工作流案例
- **仓库门禁** → 校验 frontmatter、本地链接、manifest 形状、安全扫描等，pre-1.0 但工程流程完整

**它明确不做**：不做私有的编排运行时，坚持可移植目录；不声称没测过的客户端兼容
（README 明确写"绝不声称兼容未实际检查过的客户端"）。

## 它在替代什么旧行为

不用这套东西时，编码 agent 的默认行为是"马上写代码"：认证、测试、安全和集成都被推到后面，
最后用一个看起来合理的输出收尾。工程师靠人肉审查去抓这些问题，但 agent 一多、任务一长，
审查质量就崩了。

godmode 替代的是"把工程纪律写进对话里"的旧做法——每次在提示词里重新要求 agent 先写测试、
先做设计。它把纪律从对话里的临时约定，变成可复用的技能资产。它不是替代人，
是替代"人每次都要重新教一遍"。

## 商业模式

**未披露。** MIT 开源，无定价页，无托管服务。

_判断：技能目录本身很难直接变现，但它和 dsh_workflow 一样，赌的是"标准化 Agent Skills 会
成为 agent 工程化的公共底座"。如果这个底座成型，早期目录作者有先发优势。_

## 硬数字

- **85 star / 84 fork / 0 open issue**，仓库 2026-08-12 左右建，12 个 commit
- **fork 数接近 star 数（84/85）**——这个比例异常，通常意味着大量镜像/复制，而不是有机采用
- 14 个核心 workflow 技能 + 19 个工程能力技能
- 项目主页（thiientv.github.io/godmode）目前 404，未启用 GitHub Pages
- 使用人数、客户端兼容实测：未披露

## 四维评估

| 维度 | 结论 |
|------|------|
| 创始人-产品匹配度 | 个人把工程实践系统化，作者显然是工程方法重度信徒；但缺乏团队实战验证记录 |
| 产品洞察力 | "Agent 会写代码，不会做工程"是准确的观察，技能的原子化命名（literal names）也是对的 |
| 技术实现质量 | 仓库门禁 + 行为评测 + 兼容性文档，工程流程比多数 12-commit 项目完整得多 |
| 市场时机 | Agent Skills 正在成为标准格式，抢先建立高质量目录有卡位价值；但格式竞争未定 |

## 判断

**这是"把二十年软件工程纪律封装成 agent 能消费的技能"的一次认真尝试，最值得注意的是它的
命名原则。**

"Agent 声称不是证据"和"用字面责任名而不是借用词"——这两条设计原则直接对应真实工程事故的
两大来源：agent 的乐观误报，和跨项目术语漂移。技能目录最大的死法是"名字好听但不进到具体
动作"，它用确定性脚本和引用文件堵住了这条。

**可迁移的规律：给 agent 的技能/工具命名，用"责任名"而不是"品牌名"。** 字面、任务导向的
名字（root-cause-debugging 而不是 smart-debug）让 agent 的路由决策和人的预期对齐，
也避免被某个客户端生态的词表绑架。

**风险是它替谁说话还没证明。** 85 star 里有 84 个 fork，这个 fork/star 比说明传播主要靠复制
而不是认可。pre-1.0、没有公开的实战记录、行为评测是自测——它的"生产级"还没被生产验证。

## 下一步看什么

① fork/star 比能不能回归正常（fork 远小于 star）——现在的 84/85 说明复制多于认可
② 有没有公开的"用 godmode 跑真实仓库"的案例或评测结果——"生产级"需要生产证据
③ 技能会不会跟着 Claude Code/Codex 的官方技能市场做分发——决定它能不能吃到格式红利

## 可借鉴的做法

**产品逻辑**：给任何 agent 产品配"工程行为层"时，照抄两个设计原则——"Agent 声称不是证据"
（要求新证据才算完成）和"责任名优于别名"（字面命名防漂移）。对做 agent 工作流产品的人，
这两个原则是免费的正确性。

**话术**："Your coding agent already knows how to code. Godmode teaches it how to engineer."——
一句式定位的范本，值得收藏结构（已有能力 + 新增能力 = 一句话）。

**定价结构**：无。未披露。

## 结论

**有想法，未验证。** 工程纪律技能化是正确方向，仓库工程质量也超出星数观感，但 fork/star
比例异常、无实战记录、pre-1.0 都说明"生产级"还只是自称。记下来，跟踪实战证据和官方技能
市场分发。
