---
slug: passmint
name: passmint
verdict: 有待观察
analyzed_at: 2026-08-14
---

## 一句话定位

从任意边缘运行时签发苹果和谷歌钱包卡券的 Node 库——同一份卡券数据，
同时生成 iOS 的 .pkpass 和 Android 的保存链接，而且不用 Node 内置模块。

## 做这个东西的人

alexpate（Alex Pate），一位长期混在 JS / TypeScript / 边缘计算生态的独立开发者，
此前作品分布在 Pusher、StackBlitz 生态附近。仓库挂在 getpassmint 组织下，
另有官网 passmint.com 和 npm 上的 `@passmint/node`（自称"Passmint API 官方 Node SDK"）——
后者的存在暗示背后还藏着一个托管 API 服务。

_判断：一个人先做库，几乎总是为了后面收托管服务的钱，库是获客和建立信任的入口。_

## 它到底能做哪几件事

- **一份 schema，两端签发** → `Pass.eventTicket({...}).build()` 之后，
  `sign(apple)` 直接产出 `.pkpass` 字节，`toGoogleSaveLink(google)` 产出 Google 钱包的保存链接 JWT
- **纯边缘环境可用** → 零 `node:*` 导入，只用 Web Crypto，
  Cloudflare Workers、Vercel Edge、Deno、Bun、Supabase Edge、Netlify Edge、Node 20+ 都能跑
- **工程护栏** → 约 21KB gzipped，严格 TypeScript、Valibot 判别联合、类型化错误；
  CI 里带 bundle-guard，任何 `node:*` import 都会让构建失败
- **常见卡种** → 除了活动票，还面向苹果/谷歌钱包的常用卡券样式（具体覆盖范围未逐一核实）

## 它在替代什么旧行为

以前要同时支持苹果和谷歌钱包，得维护两套生成逻辑：苹果侧要手拼 `.pkpass`
的 manifest 和签名（常用 node-forge / node:crypto），谷歌侧要单独构造 JWT。
更麻烦的是这些 Node 内置模块在边缘运行时里根本不存在，
于是很多团队被迫在传统 Node 服务上专门开一个"卡券签发"小服务。
passmint 要替代的是"两套逻辑 + 一个只能跑在传统环境的专用服务"这两件事。

## 商业模式

**库开源（MIT），托管服务迹象存在但细节未披露。** passmint.com 在仓库里被设为 homepage，
npm 上有"Passmint API"的官方 SDK 包名，但 API 的定价和上线状态没有公开信息。

_判断：卡券签发是低频操作，很难按调用量收出规模，真要做成生意大概率要靠
"批量发卡 + 卡券更新推送"这类增值，否则就是一个个人技术名片项目。_

## 硬数字

- **4 star / 1 fork**，仓库 2026-04-15 建，官方标注 pre-1.0 alpha
- 119 commits、7 分支、8 tag，最近提交 2026-07-27；npm 上 passmint 0.1.0 约三周前发布
- HN 5 分、0 评论
- 用户数、付费数据：无

## 四维评估

| 维度 | 结论 |
|------|------|
| 创始人-产品匹配度 | 作者长年在 JS/边缘计算生态，痛点真实；是个人项目，动力和耐心都在个人身上 |
| 产品洞察力 | 抓住"边缘运行时也要发卡券"的空白，一份 schema 两端的抽象是对的 |
| 技术实现质量 | 工程规范到位——Web Crypto only、bundle guard、publint/attw、changesets 发布流程，不是 demo |
| 市场时机 | 钱包卡券作为触达渠道在回暖，但签发库本身是低壁垒的小市场，托管 API 才是真正的战场 |

## 判断

**工程质量好，市场很小，现在还只是名片。** 4 颗星意味着还没有人真正信任它，
pre-1.0 的 API 也会劝退一批早期采用者。这个库的技术选择（零 Node 内置、边缘优先）
对它的目标用户是准确的，但"签发钱包卡券"不是高频需求，单靠库很难长出付费意愿。

**真正该盯的是托管 API 会不会落地、怎么定价。** 库是钩子，服务才是生意。
如果 passmint.com 的托管服务一直不上线，这个项目大概率停留在"作者的技术能力展示"。

## 下一步看什么

① 三个月后 stars 能否过百、有没有非作者维护的仓库真正依赖它
② passmint.com 托管 API 是否上线、定价如何——托管服务是验证需求的试金石
③ 是否脱离 pre-1.0、API 是否稳定下来

## 可借鉴的做法

**产品逻辑**：要做"必须跑在受限环境里"的工具，先把"零外部依赖"变成 CI 里的强制门禁，
而不是口头承诺。passmint 用 bundle-guard 让任何违规 import 直接构建失败，
把兼容性从"希望保持"变成"必须保持"。你的多环境库可以照抄这个思路。

**话术**：无。工程文档，没有可偷的句式。

**定价结构**：无。未披露。

## 结论

**有待观察。** 工程底子不错，但没有用户、没有收入、托管服务没有落地，
现在只是作者能力的一张名片。记下上面三条，三个月后回头验证。
