---
slug: getopen
name: getopen
verdict: 值得关注
analyzed_at: 2026-08-14
---

## 一句话定位

Plausible 的现代替代品：无 Cookie 的开源网站统计，多两块别人没有的东西——收入归因（revenue attribution）和给 AI 代理用的 MCP 服务器，让你直接问 Claude"昨天发生了什么"。

## 做这个东西的人

OpenLabs 团队（HN 账号 rahulbridge）。GitHub 组织 OpenLabs-so，主仓库 openanalytics（TypeScript，AGPL-3.0），另有一个 macOS 菜单栏客户端 oa-menubar。仓库 2026-08-11 创建，三天 117 star。

_判断：这是"工具本身不新、但新增的两块对 AI 时代很关键"的产品。统计面板人人会做，收入归因和 MCP 接口是它真正想抢占的差异化位置。_

## 它到底能做哪几件事

- **无 Cookie 的页面统计**：实时访问、访客旅程、漏斗、Web Vitals（LCP/INP/CLS/TTFB）、自定义事件、UTM/活动归因
- **收入归因**：接 Stripe/Polar/LemonSqueezy/Paddle/Creem/Dodo 六个收款渠道，把收入一路追到带来它的 campaign、页面和帖子
- **MCP 服务器**：AI 代理可以直接查询数据（官方说法："so you can just ask Claude what happened yesterday"），面板里也内置 AI 聊天查数
- 导入 Plausible 三年历史；公共只读看板、团队角色、Slack/Telegram/邮件告警
- 自托管免费；ClickHouse 后端，一年的事件量查询不出转圈

**它明确不做**：不收集个人信息、不做跨站跨天画像，页面原话"隐私是默认值，不是设置项"。

## 它在替代什么旧行为

GA 时代的工作流：加一段沉重的 GA4 脚本 → 被迫弹 cookie 同意横幅 → 等两天数据 → 在迷宫般的面板里找"哪个页面带来最多注册"。Plausible 已经替掉了一半（无 cookie、轻脚本），但它停在"页面浏览量"这个层面。

getopen 替掉的是后半段：想知道"哪个页面带来最多付费"，以前要么手动对订单表，要么上 Amplitude 这类重型分析。收入归因把它压成面板里的一个维度；MCP 更进一步，把"看数据"从人肉操作变成对话。

## 商业模式

自托管免费（AGPL-3.0），托管版 $9/月起（HN 作者原话："self-host it for free, or $9 hosted"）。第三方发布页显示 Hobby $9（10 万事件/月）、Starter $19（50 万）、Growth $29（100 万），另有 Startup 免费计划（1 年、100 个项目）——官网定价页未直接抓到，以实际为准。

_判断：$9 起步、按事件量分档，是 Plausible/Umami 的标准打法，没有价格战的意思。真正的护城河赌注在"收入归因 + AI 代理接口"上——这是 Plausible 没有、Umami 也没有的。_

## 硬数字

- **HN 两次发布：4 分（2 评论）和 6 分（6 评论）**
- **GitHub: OpenLabs-so/openanalytics，117 star**，2026-08-11 建仓，TypeScript，AGPL-3.0；oa-menubar 4 star
- 收入归因支持的收款渠道：6 个（Stripe/Polar/LemonSqueezy/Paddle/Creem/Dodo）
- 付费用户数、事件量：未披露

## 四维评估

| 维度 | 结论 |
|------|------|
| 创始人-产品匹配度 | 作者是连续做 AI 工具的人（仓库组织名 OpenLabs），懂开发者分发 |
| 产品洞察力 | 在拥挤的统计赛道里选了 Plausible 缺的两块：收入归因和给 agent 的接口 |
| 技术实现质量 | ClickHouse 后端 + MCP + 六渠道归因，三天 117 star，说明开发者认可 |
| 市场时机 | 统计工具红海，但"AI 代理要能读你的数据"刚成为刚需，正好卡位 |

## 判断

**它赌的是下一个时代的问题：数据不只是给人看的，还要能给 AI 代理读。**

统计工具已经卷了三轮（GA→Plausible/Umami→PostHog），面板功能都是抄来抄去。getopen 聪明的点在于：它不做更好的面板，而是做了两个别人没有的接口——收入归因把统计和钱接起来，MCP 把统计和 agent 接起来。对独立开发者来说，"昨天哪个页面带来几单"是唯一真正天天想问的问题，Plausible 答不了。

**可迁移的规律：红海品类里找"上一代产品刻意不做的两块"，而不是做得更好。** Plausible 刻意不做收入（要隐私、要简单），不做 agent 接口（用户是 human）。getopen 把这两块空白直接做成卖点。任何"xxx 的替代品"定位，都该先列出被替代者的"刻意空白"。

**风险**：六个收款渠道的收入归因在数据侧很脏（事件与订单对不上、退款、订阅折价），是持久战；HN 评论里有人点名 Umami 的免费层，是价格之外的直接对手。它的护城河还没证明。

## 下一步看什么

① GitHub star 三个月后还在不在涨——MCP 接口对开发者的吸引力是真是假
② 有没有人公开说"从 Plausible 迁到 getopen"，以及迁移原因
③ 收入归因在真实订单数据下的准确性——退款、订阅场景能不能说清楚

## 可借鉴的做法

**产品逻辑**："被替代者的刻意空白"清单——列出现有工具因为定位而刻意不做的事，挑两块做成自己的卖点。做"xxx 替代品"的 AI 产品可以直接照抄这个分析框架。

**话术**："ask your analytics a question and get the number back, not a report"——把"报告"和"答案"对立起来，一句话讲清 AI 接口的价值。还有"从第一次访问到购买，理解客户旅程的每一步"。

**定价结构**：自托管免费 + 托管按事件量分档（$9/$19/$29），并有 1 年免费 Startup 计划。标准且清晰，可参考。

## 结论

**值得关注。** 面板同质化的统计赛道里，它靠"收入归因 + AI 代理接口"切出了一块真实的差异化，三天 117 star 是市场给的第一个信号。把它作为"替代品怎么找差异化"的案例记下来，三个月后拿上面三条验证。
