---
slug: dsh-workflow
name: dsh_workflow
verdict: 有待观察
analyzed_at: 2026-08-14
---

## 一句话定位

把 Claude Code 的 UltraCode 模式带到 DSH（DeepSeek Harness），把 DSH 的一次性多 Agent
调度升级成一套可命名、可保存、可治理、可续跑、可审计的工作流层——让"这次怎么拆任务"
变成"以后按名字就能再跑一遍"。

## 做这个东西的人

icetomoyo，个人开发者，同时维护 DSH 快照仓库。项目致谢 DeepSeek Harness 的能力面、
KodaX 的 workflow 设计参考和 dsh-external 社区。

_判断：DSH 缺的正是"流程产品层"——模型路由、子 Agent、审批、Session 日志这些基础设施
都有，但没有一个地方把策略沉淀下来。开源生态的规律是"谁疼谁先修"，个人开发者先补这一层，
符合常理。_

## 它到底能做哪几件事

- **版本化 workflow 胶囊** → 每个 workflow 是带 manifest、source、intent、inputs、requires、
  provenance 的 v1 capsule，统一 `async function run(wf, args)` 执行模型
- **六个标准模式** → classify-and-act、fan-out-and-synthesize、adversarial-verification、
  generate-and-filter、tournament、loop-until-done；两个内置 workflow（parallel-investigation、
  scoped-review）
- **三级发现机制** → 内置 → 项目 `.dsh/workflows` → 个人 `$DSH_HOME/workflows`，同名覆盖规则
  带符号链接、路径逃逸、版本不兼容等安全检查
- **生命周期与落盘** → 每次 run 有稳定 id 和状态机（running → paused/completed/failed/denied/
  stopped），默认落盘 run.json、events.jsonl、不可变快照、results/、artifacts/
- **续跑与重跑** → 按 run id 或 saved name 重跑、resume-run 续跑、effect cache 跳过已完成部分
- **安全约束** → 生成型脚本只在 capability-only 的 QuickJS WASM VM 里跑，JSON capability RPC，
  确定性 guard，审批分级
- **三条路径共享同一引擎** → 斜杠命令（/workflow）、模型工具（workflow_list / run_workflow /
  workflow_manage）、后台 jobs

**它明确不做**：不引入新的编排运行时，不绑定模型，不做云端服务。它是 DSH 的一个插件，
不是替代品。

## 它在替代什么旧行为

以前用 DSH 跑多 Agent 是"一次性调度"：团队每次都要在提示词里重新描述怎么拆任务、
怎么并发、怎么验证、怎么汇总。并行结果散落在会话里，中断了就从零再来；换一个人跑同一件事，
等于把上一次的提示词重写一遍。

DSH 前台原本有个 workflow 工具，但它只是"一次把若干工作并行跑完"的通道，不是资产。
dsh_workflow 把这层升级成工程资产：策略可命名、可发现、可复用、可审计、可续跑，
越权脚本还被限制在能力白名单沙箱里。

## 商业模式

**未披露。** MIT 开源插件，无定价页，无托管服务。

_判断：这类东西的钱不在插件本身，而在它证明的价值——如果 DSH 生态里足够多的人需要
"可治理的多 Agent 工作流"，这一层迟早被官方或商业化产品收编。开源放出来的是先验证，
不是先变现。_

## 硬数字

- **49 star / 0 fork / 0 open issue**，仓库 2026-08-12 附近建
- 5 个 commit（截至 2026-08-13），但结构完整：179 个 Vitest 测试、覆盖率阈值 80%、
  带安全模型和架构文档
- TypeScript，Node >=22.19，pnpm workspace，QuickJS WASM 沙箱，MIT
- 作者背景、实际使用者：未披露

## 四维评估

| 维度 | 结论 |
|------|------|
| 创始人-产品匹配度 | icetomoyo 是 DSH 生态参与者，痛点真实，但个人项目维护持续性未知 |
| 产品洞察力 | 抓住了"一次性调度 → 可治理资产"这一跳；六个标准模式和续跑机制不是凑功能 |
| 技术实现质量 | 179 个测试、带安全检查的发现机制、capability-only 沙箱，工程态度比 5 个 commit 成熟 |
| 市场时机 | 取决于 DSH 生态本身的扩散速度，目前 DSH 远没到主流 |

## 判断

**这是一次把"多 Agent 调度"物化成"工作流资产"的示范，技术选型很克制。**

最值得注意的是 capability-only VM——生成型脚本默认不可信，只能在受限沙箱里跑。
多 Agent 工作流一旦可保存、可复用，就意味着会被反复执行，恶意或越权脚本的风险被放大；
先默认不信，是对的起点。

**规律：任何"把一次性操作变成可复用资产"的升级，都要先回答"复用时的越权风险谁兜底"。**
dsh_workflow 用沙箱加审批分级兜底，这一步做对了。

**问题是它押注在一个很小的生态上。** DSH 本身用户基数有限，0 fork 说明连拿来复制学习的人
都没有。除非 DSH 生态起量，否则这个插件是"对的答案，还没到对的场合"。

## 下一步看什么

① fork 数能不能起来——0 fork 意味着连复制学习的人都没有
② 有没有出现第二条消费路径（比如 Claude Code 用户把它当模式参考）——说明价值出了 DSH 圈子
③ 两个月后的 commit 频率——个人项目最常死于发布后熄火

## 可借鉴的做法

**产品逻辑**：多 Agent 工作流的治理层，可以参考它的三级抽象——一次性调度（prompt）→
可命名工作流（胶囊）→ 可续跑可审计（run 落盘 + snapshot）。"能续跑"是工作流和脚本的分水岭，
多数人做到第二级就停了。

**话术**：无。README 是工程文档。

**定价结构**：无。未披露。

## 结论

**记下来，不急。** 设计有示范价值，但押注的生态太小，49 star / 0 fork 说明现在还只是
作者自己的工程表达。三个月后拿上面三条回头验证。
