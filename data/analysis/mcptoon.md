---
slug: mcptoon
name: Mcptoon
verdict: 值得关注
analyzed_at: 2026-08-14
---

## 一句话定位

先把 MCP 工具清单压缩掉 90% 再喂给模型的命令行客户端——
让 agent 挂 100 个 MCP 服务器，也不把上下文窗口撑爆。

## 做这个东西的人

GitHub 用户 activeing123，个人项目，Apache-2.0，Python 纯标准库实现，
零第三方依赖，安装包约 50KB。309 个测试，2026-07-27 建仓，v0.4.0。

_判断：作者明显是被真实账单教育过的人。所有设计都指向一个亲身体会——
"我的上下文被工具 schema 吃光了"是装多了 MCP 服务器的人才会喊的疼。
README 里引用了 Anthropic、Cursor、Latent Space 关于 schema 膨胀的论述，
说明他把问题研究透了才动手。_

## 它到底能做哪几件事

- **CLI 模式而非客户端库** → agent 只需运行 `mcptoon` 命令，schemas 存在
  磁盘上的 `~/.mcptoon/config.json`，只有请求到的紧凑输出才进上下文
- **TOON 编码** → 用自定义的 token 导向格式替代 JSON 传工具定义，
  实测 255 个工具：JSON 90,804 tokens → slim 6,174（-93%）→ compact 117（-100%）
- **三层解耦** → CLI（50KB 零依赖）+ 23 个服务器配置模板（各约 1KB）+ 实际
  MCP 服务器（调用时才通过 npx 按需启动）：100 个服务器配置 = 0 个常驻进程
- **agent 自助装工具** → agent 自己执行 `mcptoon add github ...` 就能挂上新工具，
  不需要人手工改 JSON 配置
- **安全防护** → 工具投毒检测（拦截 "ignore previous instructions" 这类注入）、
  凭据泄漏扫描（API key / AWS key / GitHub PAT 不进上下文）、危险命令
  （delete/drop/purge）默认拦截、schema 缓存（5 分钟 TTL 省 tools/list 往返）
- **跨代理兼容** → 配一次，Claude Code / Codex / OpenCode / Cursor 共用；
  `--format openai|openapi|mcp` 还能导出给别人用

## 它在替代什么旧行为

以前给 agent 配 MCP 有两件苦事，它各替代一件：

**手工编辑 JSON 配置**。给 Claude Desktop 加服务器要改 `claude_desktop_config.json`，
多配几个、配错一个引号就要调半天。现在 `mcptoon add fetch --stdio npx -y ...`
一行命令，agent 自己都能装。

**上下文被 schema 撑爆**。标准 MCP 客户端会在工作开始前把所有工具 schema
灌进上下文——装上 10 个 MCP 服务器（尤其带浏览器工具的）能吃掉 5-10 万 token，
128K 窗口里提问前就占掉一半。mcptoon 把"工具清单"从上下文里挪到磁盘上，
模型只看到压缩后的工具名和调用结果，于是"多挂服务器"从一件要精打细算的
事变成可以放开做的事。

## 商业模式

**未披露。** 免费开源（`pip install mcptoon`），没有云服务、没有付费档、没有托管版。

_判断：这类工具的商业化路径通常是两条——要么被大厂收购变成某个 client 的
内置能力，要么推出托管版（工具发现、审计、团队共用）。现在一条都没走。
纯开源工具的问题是功能再好也不直接变成钱。_

## 硬数字

- **139 star / 4 fork**，Apache-2.0，零依赖，约 50KB，Python 3.10+
- HN 70 分 / 43 条评论（2026-08-12），讨论热度真实
- 作者实测（255 工具）：JSON 90,804 tokens；TOON 44,863（-51%）；mcptoon 35,735
  （-61%）；SLIM 6,174（-93%）；Compact 117（-100%）
- 测试规模：309 个测试；自称已测 255+ MCP 工具、23+ 服务器、30K+ 真实调用
- 24 个配置模板：fetch、github、exa、brave-search、firecrawl、filesystem、
  memory、sequential-thinking、sqlite、time、puppeteer、playwright、postgres、
  slack、notion、git、gitlab、tavily、google-maps、docker、aws、cloudflare、tmux 等
- 团队人数、收入：不适用（个人项目，未披露）

## 四维评估

| 维度 | 结论 |
|------|------|
| 创始人-产品匹配度 | 痛点是被真实使用喂出来的，README 的问题研究深度说明不是蹭热点 |
| 产品洞察力 | 抓对了问题（schema 膨胀是 MCP 的已知软肋）且给的是根治方案（挪出上下文）而不是缓解方案 |
| 技术实现质量 | 零依赖、50KB、309 测试，工程干净；但性能数字全为作者自测，需第三方复现 |
| 市场时机 | 好。MCP 生态 2026 年在爆发，schema 膨胀问题随之放大，省 token 正在变成一个品类 |

## 判断

**这是"MCP 的上下文问题"目前给得最彻底的解法，值得关注。**
别人在优化 schema 定义本身（把 description 写短），它直接把整个清单挪出上下文，
用压缩格式只在调用时传递必要信息——方向不同，效果大得多。

**一个可迁移的判断：token 成本正在变成真实的经营成本，任何"省 token"
工具都会跟着变成一个品类。** 现在的省钱工具是给 agent 省，下一步一定是
给平台省（API 网关、缓存层），再下一步是给业务省。mcptoon 踩在了第一层，
但对个人工具来说，第一层的天花板是"被内置"。

**三个隐忧**：一是 benchmark 全是自测，TOON 编码的实际 token 节省需要
独立复现；二是 43 条 HN 评论里除了赞美还有多少质疑我没逐条读，热度可能
高估了共识；三是纯开源无商业模式，作者的热情能否撑过三年要打问号。

## 下一步看什么

① 三个月后 stars 能否破 500——MCP 官方和各客户端都在做懒加载/精简，
  外部工具的红利窗口有限
② 有没有主流客户端（Claude Code / Cursor / OpenCode）把它吸收为内置——
  被内置是这类工具最好的结局
③ 是否出现独立第三方复现它的 token 节省数据

## 可借鉴的做法

**产品逻辑**：当你的产品依赖一个"必然膨胀"的输入（工具清单、规则文件、
上下文）时，别只做压缩优化，考虑把整个东西挪出主通道、按需取用——
把"常驻"改成"按需"，常常比优化格式省得多。

**话术**：README 的 benchmark 表格（同一份数据用五种格式跑一遍，列出
节省百分比）是可迁移的展示方法——省了多少要能精确到 token 数。

**定价结构**：无。未披露。

## 结论

**值得关注，但商业化未定。** 问题抓得准、解法给得狠、工程做得干净，
且 70 分的 HN 讨论说明开发者群体有真实共鸣。但它是个零依赖的开源个人工具，
最大的天花板是被主流客户端吸收而不是独立做大。三个月后拿上面三条验证。
