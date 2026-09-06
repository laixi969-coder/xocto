---
slug: runta
name: Runta
builder: leemysw
category: ''
summary_zh: Runta 发布 FrontierHarness Eval 评测：固定同一模型 Kimi K3 与任务环境，只更换 Coding Agent 的 Harness，在 30 道题上得到
  50.0%–66.7% 的通过率，单题通过成本从 1.05 美元到 18.34 美元，相差逾 17 倍。结果显示模型之外的外层工程封装对智能体交付质量与成本影响显著，为选型 Agent 框架的团队提供了公开参照，也提示关注点正从模型能力本身转向模型之上的工程层。
inspiration: ''
summary_en: 'Runta released FrontierHarness Eval: holding the same model (Kimi K3) and task environment
  fixed, it varied only the coding agent harness across 30 tasks, obtaining pass rates of 50.0%–66.7%
  and cost per solved task from $1.05 to $18.34 — a gap of more than 17x. The results show that the engineering
  scaffolding around a model materially changes agent delivery quality and cost, giving teams a public
  reference for choosing agent frameworks and signaling that attention is shifting from raw model capability
  to the engineering layer above it.'
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
url: https://runta.com/blog/introducing-frontierharness-eval/
canonical_url: https://runta.com/blog/introducing-frontierharness-eval
summary: "Runta 最近发布了一个 Coding Agent Harness 评测，名字叫 FrontierHarness Eval 。\r\n\r\n他们让同一个 Kimi K3 跑 30\
  \ 道题，每轮只更换 Agent Harness 。公开结果里，通过率从 50.0% 到 66.7%，每通过一道题的成本从 1.05 美元到 18.34 美元。\r\n\r\n看完[发布文章]( https://runta.com/blog/introducing-frontierharness-eval/)、任务和逐题结果，差距比我原先预想的大。\r\
  \n\r\n![FrontierHarness 官方成本与通过率结果]( https://imgdb.io/i/QhBJc_4.png)\r\n\r\nFrontierHarness v1.0 选了\
  \ 30 道题，其中 21 道来自 Terminal-Bench ，9 道来自 DeepSWE 。Runta 测了 9 个 Harness 、12 组配置，一共跑了 360 个 cell 。\r\n\r\
  \n所有配置都使用 Kimi K3 。模型经由同一个网关连接到 Fireworks ，任务环境做成 Golden Checkpoint 。每次运行都从同一份快照恢复，vCPU 、内存、磁盘和内存状态保持一致。调试不用正式题，每个\
  \ cell 只跑一次。\r\n\r\n这些约束固定了模型、任务和运行环境，Harness 成为主要变量。\r\n\r\n## 一样的通过率，成本差了 5.6 倍\r\n\r\nRunta 的结果里，Codex\
  \ 通过 20 题，通过率是 66.7%。DSH Creator 和 Claude Code 都通过 19 题，通过率同为 63.3%。\r\n\r\nDSH Creator 每通过一道题花 3.28\
  \ 美元，Claude Code 花 18.34 美元，相差 5.6 倍。\r\n\r\nExo Harness 的通过率是 53.3%，每通过一道题花 1.05 美元。在 Runta 展开的那道难题里，它跑到\
  \ 51 步上限后停止，花了 1.46 美元。产品如果自动重试，这笔钱会反复累加。\r\n\r\n模型生成下一步，Harness 决定模型能看到什么、能调用哪些工具，还要管理上下文和测试失败后的重试。\r\
  \n\r\n## NXS 的结果有点出乎意料\r\n\r\nNXS 是 Nexus 默认使用的 Agent Runtime 。Nexus Host 负责 Room 、消息和协作状态，NXS 在独立进程里运行\
  \ Agent Loop ，调用模型和工具，管理上下文。\r\n\r\n以前测试 NXS ，我们会看文件能不能读、命令能不能跑、补丁能不能写回去、Session 能不能结束。这些测试能发现功能故障，但看不出\
  \ NXS 在完整任务里能做到什么程度。\r\n\r\nFrontierHarness 提供了 30 道带 verifier 的任务。我们沿用这批题，在本地用 NXS 跑了一轮。\r\n\r\n我们还是用\
  \ Kimi K3 ，接 Kimi 官方 Coding API 。评测由 Harbor 0.20.0 驱动，宿主机是 Apple Silicon ，任务容器为 Linux ARM64 。NXS 使用\
  \ `stock-no-memory` 配置，Session Persistence 和 AutoMemory 都关闭。并发任务组为 1 ，每次只推进一道题。\r\n\r\n题目和模型与官方评测相同，运行环境有差别。Runta\
  \ 使用 Fireworks 、统一网关和 Golden Checkpoint ，我们使用 Kimi 官方 API 与本地 Docker Desktop 。13 道题在 API 或 verifier\
  \ 故障处理后重新运行。\r\n\r\n![NXS 本地结果在官方成本图中的位置]( https://imgdb.io/i/epolRd4.png)\r\n\r\nNXS 通过了 **22** 道题，通过率为\
  \ **73.3%** 。\r\n\r\nTerminal-Bench 通过 18 / 21 ，DeepSWE 通过 4 / 9 。22 道成功任务的执行时长中位数是 3 分 35 秒，缓存命中中位数是\
  \ 95.6%。29 道留下 usage 的任务合在一起，Token 加权缓存命中率是 97.8%。\r\n\r\n![加入 NXS 本地结果后的 FrontierHarness 数据表]( https://imgdb.io/i/NjXli_U.png)\r\
  \n\r\n这里的 NXS 是本地结果，记作 `LOCAL*`。官方公开结果中，最高成绩是 Codex 的 20 / 30 。NXS 的本地结果多通过两题，但两套运行条件不同，不能据此排名。\r\n\r\
  \n官方 12 组配置都通过的 Terminal-Bench 有 12 道，NXS 这 12 道也全过。NXS 还通过了 `kv-store-grpc` 和 `largest-eigenval`，这两道题在\
  \ FrontierHarness 的公开数据里都是 0 / 12 。\r\n\r\nDeepSWE 的 4 道通过项分别是 `anko-typed-variable-bindings`、`fastapi-deprecation-response-headers`、`httpx-multipart-response-parsing`\
  \ 和 `python-statemachine-state-data-scoping`。其余 5 道失败题在官方 12 组配置中最多只有 2 组通过。\r\n\r\n## 一个代表任务\r\n\r\n\
  Runta 用 `python-statemachine-state-data-scoping` 展示不同 Harness 的执行过程。这道题需要修改状态机、回调注入、历史恢复、序列化、SCXML 解析和图表生成。官方给出的历史通过率是\
  \ 38%。\r\n\r\nNXS 也通过了这道题。\r\n\r\nNXS 用了 98 个模型回合，调用工具 146 次，缓存命中率为 98.5%，执行时间是 52 分 16 秒。本地记录成本为 7.37\
  \ 美元。\r\n\r\n| 配置             | 结果 | 成本   | 回合 | 缓存  | 时间    |\r\n| ---------------- | ---- | ------\
  \ | ---- | ----- | ------- |\r\n| NXS 本地         | 通过 | $7.37  | 98   | 98.5% | 52m 16s |\r\n| Pi 官方\
  \          | 通过 | $2.50  | 90   | 98.2% | 39m     |\r\n| Codex 官方       | 通过 | $5.97  | 187  | 99.1%\
  \ | 37m     |\r\n| Claude Code 官方 | 通过 | $64.36 | 381  | 15.7% | 60m     |\r\n\r\n官方结果里，Pi 用了 90 轮，Codex\
  \ 用了 187 轮，Claude Code 用了 381 轮。两边使用的模型服务不同，时间和价格不能直接比较。这道题跨了多个模块，NXS 跑到 98 轮后做完了。\r\n\r\n## 工具与回合效率\r\
  \n\r\n| 口径           | 通过任务 | 失败任务 | 全部任务 |\r\n| -------------- | -------- | -------- | -------- |\r\
  \n| 回合数中位数   | 10       | 58       | 12       |\r\n| 工具调用中位数 | 10.5     | 56.5     | 17       |\r\n\
  | 工具调用总数   | 575      | 498      | 1073     |\r\n\r\n8 个失败任务占全部工具调用的 46.4%。通过题通常在十个回合左右结束，失败题会继续工作到五十多个回合。这个差距与成本、耗时的长尾相互对应。\r\
  \n\r\n| 工具                               | 调用数 | 占比  |\r\n| ---------------------------------- | ------\
  \ | ----- |\r\n| Bash                               | 553    | 51.5% |\r\n| Edit                   \
  \            | 209    | 19.5% |\r\n| Read                               | 142    | 13.2% |\r\n| TaskCreate\
  \ 、TaskUpdate 、TaskOutput | 128    | 11.9% |\r\n| Write                              | 40     | 3.7%\
  \  |\r\n| EnterPlanMode                      | 1      | 0.1%  |\r\n\r\n任务状态工具占 11.9% 的调用量。这些调用是否能改善长任务完成率，当前数据没有对照组。后续可以只在\
  \ DeepSWE 长任务上做一次开关实验，不需要再跑整套 benchmark 。\r\n\r\n## 八道失败的题目，花掉一半成本\r\n\r\n计入结果的 30 个 cell 至少花了 39.34\
  \ 美元。22 个成功 cell 合计 18.35 美元，7 个留下完整费用的失败 cell 合计 21.00 美元。`gcode-to-text` 超时后没有留下 usage ，实际费用会高一些。\r\
  \n\r\n用 39.34 美元除以 22 道通过题，每通过一道题至少花 1.79 美元。这个价格来自 Kimi 官方 API 。Runta 会重算首轮缓存成本，本轮没有重算。1.79 美元只代表这次本地运行。\r\
  \n\r\n8 道失败题用了 53.4% 的已记录成本。成功任务的时长中位数是 3 分 35 秒，失败任务达到 19 分 52 秒。失败任务还占了 46.4% 的工具调用。\r\n\r\nToken\
  \ 加权缓存命中率是 97.8%，问题出在长时间失败的任务。测试反复失败时，NXS 需要减少重复尝试，把时间留给剩余用例和交付检查。\r\n\r\n几道 DeepSWE 任务只差少数用例。`arktype`\
  \ 的新增用例通过 23 / 25 ，`katex` 通过 92 / 94 ，`scc` 通过 28 / 31 。Agent 改完了大部分代码，但没有解决最后几个边界问题。\r\n\r\n| 任务 \
  \                                    | verifier 结果                  | 直接原因                         \
  \                 |\r\n| ---------------------------------------- | ------------------------------ |\
  \ ------------------------------------------------- |\r\n| `arktype-json-schema-refs-dependencies` \
  \ | P2P 1679 / 1679 ，F2P 23 / 25   | 两个递归 `$defs` 引用场景访问到未定义节点         |\r\n| `expr-try-catch-errors`\
  \                  | 基线全过，新增顶层用例 68 / 74 | 错误变量字符串与 `errtype` 分类不符合要求         |\r\n| `katex-multicolumn-array-spans`\
  \          | P2P 599 / 599 ，F2P 92 / 94     | 跨列后仍保留内部竖线分隔符                        |\r\n| `scc-bounded-memory-spilling`\
  \            | P2P 286 / 286 ，F2P 28 / 31     | 有界内存下的 csv-stream 输出与普通模式不一致      |\r\n| `meriyah-explicit-resource-declarations`\
  \ | P2P 51469 / 51469 ，F2P 0 / 49  | `using` 与 `await using` 语法没有真正进入解析路径 |\r\n| `dna-insert`      \
  \                       | 0 / 1                          | 两条引物 Tm 相差 8.19°C ，要求不超过 5°C           |\r\
  \n| `extract-elf`                            | 1 / 2                          | 输出覆盖 0%，要求覆盖至少 75% 的参考地址\
  \          |\r\n| `gcode-to-text`                          | 0 / 2                          | 900 秒到期，44\
  \ 次工具调用后仍未生成 `out.txt`     |\r\n\r\n`dna-insert` 和 `extract-elf` 都在 2 分 34 秒结束，产物没有满足 verifier 的数值条件。交付前跑一次本地检查就能发现问题。`gcode-to-text`\
  \ 走到 900 秒上限还没生成 `out.txt`，需要时间预算和收尾策略。\r\n\r\n\r\n## 一些判断\r\n\r\nNXS 在 Terminal-Bench 子集表现很强，DeepSWE\
  \ 长任务仍决定整体上限。缓存没有成为主要问题。失败任务的回合数、工具调用、时间和成本同时拉长，说明运行时需要更早识别停滞，并在剩余预算不足时转入定向验证与交付。\r\n\r\n短任务的下一个改进点是\
  \ verifier 条件感知。`dna-insert` 与 `extract-elf` 都可以在交付前用本地检查发现确定性错误。长任务需要保留测试失败的结构化摘要，随后只修剩余边界，不再重复全量探索。\r\
  \n\r\n## 相关资料\r\n\r\n- [Runta 发布文章]( https://runta.com/blog/introducing-frontierharness-eval/)\r\n-\
  \ [FrontierHarness 在线结果]( https://frontierharness.org/)\r\n- [FrontierHarness 公开数据]( https://github.com/frontier-harness-eval/eval)\r\
  \n- [Nexus 开源仓库]( https://github.com/nexus-research-lab/nexus)"
first_seen: '2026-09-04T08:30:43Z'
last_seen: '2026-09-04T14:23:24Z'
status: market_context
sources:
- v2ex
sightings:
- source: v2ex
  url: https://runta.com/blog/introducing-frontierharness-eval/
  seen_at: '2026-09-04T14:23:24Z'
  metrics:
    comments: 0
  kind: product
---

# Runta

Runta 最近发布了一个 Coding Agent Harness 评测，名字叫 FrontierHarness Eval 。

他们让同一个 Kimi K3 跑 30 道题，每轮只更换 Agent Harness 。公开结果里，通过率从 50.0% 到 66.7%，每通过一道题的成本从 1.05 美元到 18.34 美元。

看完[发布文章]( https://runta.com/blog/introducing-frontierharness-eval/)、任务和逐题结果，差距比我原先预想的大。

![FrontierHarness 官方成本与通过率结果]( https://imgdb.io/i/QhBJc_4.png)

FrontierHarness v1.0 选了 30 道题，其中 21 道来自 Terminal-Bench ，9 道来自 DeepSWE 。Runta 测了 9 个 Harness 、12 组配置，一共跑了 360 个 cell 。

所有配置都使用 Kimi K3 。模型经由同一个网关连接到 Fireworks ，任务环境做成 Golden Checkpoint 。每次运行都从同一份快照恢复，vCPU 、内存、磁盘和内存状态保持一致。调试不用正式题，每个 cell 只跑一次。

这些约束固定了模型、任务和运行环境，Harness 成为主要变量。

## 一样的通过率，成本差了 5.6 倍

Runta 的结果里，Codex 通过 20 题，通过率是 66.7%。DSH Creator 和 Claude Code 都通过 19 题，通过率同为 63.3%。

DSH Creator 每通过一道题花 3.28 美元，Claude Code 花 18.34 美元，相差 5.6 倍。

Exo Harness 的通过率是 53.3%，每通过一道题花 1.05 美元。在 Runta 展开的那道难题里，它跑到 51 步上限后停止，花了 1.46 美元。产品如果自动重试，这笔钱会反复累加。

模型生成下一步，Harness 决定模型能看到什么、能调用哪些工具，还要管理上下文和测试失败后的重试。

## NXS 的结果有点出乎意料

NXS 是 Nexus 默认使用的 Agent Runtime 。Nexus Host 负责 Room 、消息和协作状态，NXS 在独立进程里运行 Agent Loop ，调用模型和工具，管理上下文。

以前测试 NXS ，我们会看文件能不能读、命令能不能跑、补丁能不能写回去、Session 能不能结束。这些测试能发现功能故障，但看不出 NXS 在完整任务里能做到什么程度。

FrontierHarness 提供了 30 道带 verifier 的任务。我们沿用这批题，在本地用 NXS 跑了一轮。

我们还是用 Kimi K3 ，接 Kimi 官方 Coding API 。评测由 Harbor 0.20.0 驱动，宿主机是 Apple Silicon ，任务容器为 Linux ARM64 。NXS 使用 `stock-no-memory` 配置，Session Persistence 和 AutoMemory 都关闭。并发任务组为 1 ，每次只推进一道题。

题目和模型与官方评测相同，运行环境有差别。Runta 使用 Fireworks 、统一网关和 Golden Checkpoint ，我们使用 Kimi 官方 API 与本地 Docker Desktop 。13 道题在 API 或 verifier 故障处理后重新运行。

![NXS 本地结果在官方成本图中的位置]( https://imgdb.io/i/epolRd4.png)

NXS 通过了 **22** 道题，通过率为 **73.3%** 。

Terminal-Bench 通过 18 / 21 ，DeepSWE 通过 4 / 9 。22 道成功任务的执行时长中位数是 3 分 35 秒，缓存命中中位数是 95.6%。29 道留下 usage 的任务合在一起，Token 加权缓存命中率是 97.8%。

![加入 NXS 本地结果后的 FrontierHarness 数据表]( https://imgdb.io/i/NjXli_U.png)

这里的 NXS 是本地结果，记作 `LOCAL*`。官方公开结果中，最高成绩是 Codex 的 20 / 30 。NXS 的本地结果多通过两题，但两套运行条件不同，不能据此排名。

官方 12 组配置都通过的 Terminal-Bench 有 12 道，NXS 这 12 道也全过。NXS 还通过了 `kv-store-grpc` 和 `largest-eigenval`，这两道题在 FrontierHarness 的公开数据里都是 0 / 12 。

DeepSWE 的 4 道通过项分别是 `anko-typed-variable-bindings`、`fastapi-deprecation-response-headers`、`httpx-multipart-response-parsing` 和 `python-statemachine-state-data-scoping`。其余 5 道失败题在官方 12 组配置中最多只有 2 组通过。

## 一个代表任务

Runta 用 `python-statemachine-state-data-scoping` 展示不同 Harness 的执行过程。这道题需要修改状态机、回调注入、历史恢复、序列化、SCXML 解析和图表生成。官方给出的历史通过率是 38%。

NXS 也通过了这道题。

NXS 用了 98 个模型回合，调用工具 146 次，缓存命中率为 98.5%，执行时间是 52 分 16 秒。本地记录成本为 7.37 美元。

| 配置             | 结果 | 成本   | 回合 | 缓存  | 时间    |
| ---------------- | ---- | ------ | ---- | ----- | ------- |
| NXS 本地         | 通过 | $7.37  | 98   | 98.5% | 52m 16s |
| Pi 官方          | 通过 | $2.50  | 90   | 98.2% | 39m     |
| Codex 官方       | 通过 | $5.97  | 187  | 99.1% | 37m     |
| Claude Code 官方 | 通过 | $64.36 | 381  | 15.7% | 60m     |

官方结果里，Pi 用了 90 轮，Codex 用了 187 轮，Claude Code 用了 381 轮。两边使用的模型服务不同，时间和价格不能直接比较。这道题跨了多个模块，NXS 跑到 98 轮后做完了。

## 工具与回合效率

| 口径           | 通过任务 | 失败任务 | 全部任务 |
| -------------- | -------- | -------- | -------- |
| 回合数中位数   | 10       | 58       | 12       |
| 工具调用中位数 | 10.5     | 56.5     | 17       |
| 工具调用总数   | 575      | 498      | 1073     |

8 个失败任务占全部工具调用的 46.4%。通过题通常在十个回合左右结束，失败题会继续工作到五十多个回合。这个差距与成本、耗时的长尾相互对应。

| 工具                               | 调用数 | 占比  |
| ---------------------------------- | ------ | ----- |
| Bash                               | 553    | 51.5% |
| Edit                               | 209    | 19.5% |
| Read                               | 142    | 13.2% |
| TaskCreate 、TaskUpdate 、TaskOutput | 128    | 11.9% |
| Write                              | 40     | 3.7%  |
| EnterPlanMode                      | 1      | 0.1%  |

任务状态工具占 11.9% 的调用量。这些调用是否能改善长任务完成率，当前数据没有对照组。后续可以只在 DeepSWE 长任务上做一次开关实验，不需要再跑整套 benchmark 。

## 八道失败的题目，花掉一半成本

计入结果的 30 个 cell 至少花了 39.34 美元。22 个成功 cell 合计 18.35 美元，7 个留下完整费用的失败 cell 合计 21.00 美元。`gcode-to-text` 超时后没有留下 usage ，实际费用会高一些。

用 39.34 美元除以 22 道通过题，每通过一道题至少花 1.79 美元。这个价格来自 Kimi 官方 API 。Runta 会重算首轮缓存成本，本轮没有重算。1.79 美元只代表这次本地运行。

8 道失败题用了 53.4% 的已记录成本。成功任务的时长中位数是 3 分 35 秒，失败任务达到 19 分 52 秒。失败任务还占了 46.4% 的工具调用。

Token 加权缓存命中率是 97.8%，问题出在长时间失败的任务。测试反复失败时，NXS 需要减少重复尝试，把时间留给剩余用例和交付检查。

几道 DeepSWE 任务只差少数用例。`arktype` 的新增用例通过 23 / 25 ，`katex` 通过 92 / 94 ，`scc` 通过 28 / 31 。Agent 改完了大部分代码，但没有解决最后几个边界问题。

| 任务                                     | verifier 结果                  | 直接原因                                          |
| ---------------------------------------- | ------------------------------ | ------------------------------------------------- |
| `arktype-json-schema-refs-dependencies`  | P2P 1679 / 1679 ，F2P 23 / 25   | 两个递归 `$defs` 引用场景访问到未定义节点         |
| `expr-try-catch-errors`                  | 基线全过，新增顶层用例 68 / 74 | 错误变量字符串与 `errtype` 分类不符合要求         |
| `katex-multicolumn-array-spans`          | P2P 599 / 599 ，F2P 92 / 94     | 跨列后仍保留内部竖线分隔符                        |
| `scc-bounded-memory-spilling`            | P2P 286 / 286 ，F2P 28 / 31     | 有界内存下的 csv-stream 输出与普通模式不一致      |
| `meriyah-explicit-resource-declarations` | P2P 51469 / 51469 ，F2P 0 / 49  | `using` 与 `await using` 语法没有真正进入解析路径 |
| `dna-insert`                             | 0 / 1                          | 两条引物 Tm 相差 8.19°C ，要求不超过 5°C           |
| `extract-elf`                            | 1 / 2                          | 输出覆盖 0%，要求覆盖至少 75% 的参考地址          |
| `gcode-to-text`                          | 0 / 2                          | 900 秒到期，44 次工具调用后仍未生成 `out.txt`     |

`dna-insert` 和 `extract-elf` 都在 2 分 34 秒结束，产物没有满足 verifier 的数值条件。交付前跑一次本地检查就能发现问题。`gcode-to-text` 走到 900 秒上限还没生成 `out.txt`，需要时间预算和收尾策略。


## 一些判断

NXS 在 Terminal-Bench 子集表现很强，DeepSWE 长任务仍决定整体上限。缓存没有成为主要问题。失败任务的回合数、工具调用、时间和成本同时拉长，说明运行时需要更早识别停滞，并在剩余预算不足时转入定向验证与交付。

短任务的下一个改进点是 verifier 条件感知。`dna-insert` 与 `extract-elf` 都可以在交付前用本地检查发现确定性错误。长任务需要保留测试失败的结构化摘要，随后只修剩余边界，不再重复全量探索。

## 相关资料

- [Runta 发布文章]( https://runta.com/blog/introducing-frontierharness-eval/)
- [FrontierHarness 在线结果]( https://frontierharness.org/)
- [FrontierHarness 公开数据]( https://github.com/frontier-harness-eval/eval)
- [Nexus 开源仓库]( https://github.com/nexus-research-lab/nexus)

## 笔记


