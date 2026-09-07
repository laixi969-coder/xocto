# xOcto 案例管线规格

状态：待实施

本文件定义「真实生意案例」采集与富化管线。它是 OPPORTUNITY_RADAR_SPEC.md 的补充：
机会流回答「今天有什么新冒头」，案例管线回答「已经跑通的人是怎么做的」。
后续数据模型、采集、判断、页面和测试均以此为准。

## 1. 产品定义

案例管线是一条给现有板块供血的采集管线，不是一个新页面。

它做三件事：

1. 从公开来源发现「已跑出真实收入」的生意案例；
2. 用 DeepSeek 把案例富化成结构化档案：钱从哪来、启动成本、第一批用户从哪来、
   替代了什么旧行为、证据等级几何；
3. 喂给三个已有出口：机会库的筛选维度、已验证生意卡片的详情层、
   打法库的证据，以及每周 3–5 条进入日报。

不做 Starter Story 式的「几千条可浏览数据库页面」。PRODUCT.md 反参照明确
不做成列表堆砌；数量不是价值，判断才是。案例必须过与产品相同的编辑层
（config/filter.md），过不了的宁可不进。

## 2. 数据源与可达性（2026-09-06 实测）

本节是实测结论，不是假设。所有测试使用 xocto 声明的 UA
（`x-octo/0.1 (+https://github.com/laixi969-coder/xocto)`），无登录、无特殊手段。

### 2.1 starterstory.com —— 主源，可抓

- robots.txt 允许除 `/admin` 外的全部路径，并公布 sitemap。
- sitemap（`https://d1coqmn8qm80r4.cloudfront.net/sitemap.xml.gz`，
  272KB）全量枚举 URL：**3273 个 `/stories/*` 采访案例、566 个 `/businesses/*`
  案例页、946 个 `/ideas/*`、168 个 `/tools/*`**。不存在「不知道有什么」的问题。
- `/stories/<slug>` 为服务端渲染（单页约 500KB 静态 HTML），采访正文直接在
  HTML 里，无需 headless 浏览器。**实施时只采 `/stories/*`**：
  `/businesses/*` 的正文（230KB 页面里只有约 3.8KB 可见文本）在前端 JSON
  块里渲染，解析脆弱，留待确有需要再做。
- `/ideas` 列表页是前端 JS 渲染，静态 HTML 无条目数据——不抓它，走 sitemap
  逐页抓即可。
- `/businesses/*` 页面自带声明：内容为 Starter Story 自动研究汇编
  （"the founder didn't write it. Automated research can misrepresent..."）。
  这正是证据分级要标记的对象。

版权红线：`/stories/*` 正文是受版权保护的采访内容。只提取事实（收入数字、
渠道名、时间线）与不超过一句的短引，每条档案必须回链原页；禁止全文转载。
`/businesses/*` 上的事实（数字、日期、渠道）不受版权保护，但表达同样不抄。

### 2.2 trustmrr.com —— 收入最硬的源，结构化程度最高

- 首页即服务端渲染。**数据不在 `ld+json` 标签里**，而在 Next.js 的
  `application/json` script 块中（92 个 script 块里有一块约 26KB 可直接
  `json.loads`，其余是 RSC flight 文本）。实体可能平铺也可能嵌在 `item`
  字段下，采集器对全部可解析块做全树遍历，收集带 `/startup/<slug>` 链接
  与 `additionalProperty` 的实体。
- 字段即 schema.org PropertyValue：`Verified GMV, last 30 days`、
  `Verified total revenue`、`Current MRR`、`Revenue growth, last 30 days`
  等，值为美元数字。实测首页可提取 29 条（Gumroad、Stan、Chatbase、
  Comp AI 等），其中 Chatbase 近 30 天验证收入 $865,869。
- 定位：给案例档案提供「收入可验证」这一档证据，并交叉校验其他源的数字。

### 2.3 已在生产、零新增成本的源

- Hacker News（Algolia 公共接口）：show_hn / Launch HN 本身就是创始人自述，
  现有采集已在跑。
- newssearch 的 `evidence_kind: customer_case` 查询：已在抓"case study /
  customer outcomes"信号，是本管线的天然上游。

### 2.4 暂不接入

- Indie Hackers：首页可访问（200），但数据由前端加载，未验证出稳定免登录
  通道。列为 P2，等有明确需要再按官方合作或 OAuth 路径评估。
- Acquire.com 等交易平台：需登录，且挂牌数据激励失真，不采。

### 2.5 抓取纪律

- 沿用 sources.yaml 的 UA 与超时配置；
- 对 starterstory.com 限速：单次运行串行、请求间隔不低于 2 秒、
  每日新增页面上限 200 页（sitemap 全量首次导入允许一次性分日完成）；
- 所有原始响应只进 `data/raw/`，只增不改，与现有约定一致；
- 任一源连续失败触发 health 报警，但不阻塞其他源——与 officialfeeds /
  marketfeeds 的故障隔离原则相同。

## 3. 收录边界

满足任一条件才进入案例流：

1. 产品或公司与 AI 应用、AI 改造直接相关，且有可核验的收入或用户信号；
2. 非 AI 案例，但从中提炼的打法（获客、定价、分发）可直接迁移到机会库中的
   在库产品，且在档案中写明「迁移动作」。

不进入：

- 无可核验收入或用户数字的纯点子（`/ideas/*` 的空想条目默认不采）；
- 无法回链一手来源的转述；
- 与在库产品同质、无新增事实的重复案例。

证据分级（每个案例必标其一，页面上如实展示）：

- `stripe_verified`：TrustMRR 等渠道的支付验证数字；
- `interviewed`：创始人书面采访自报（Starter Story `/stories/*`）；
- `ai_estimated`：平台自动研究汇编（Starter Story `/businesses/*`）；
- `cited_public`：仅公开报道交叉。

「拿不准就说拿不准」适用于数字本身：采访自报数字必须在档案中标注
「创始人自报，未经审计」。

## 4. 数据结构

新增 `data/casestudies/<slug>.md`，格式与产品池一致（YAML frontmatter + 正文）。
`## 笔记` 以下留给人工，程序不覆盖。

```yaml
slug: expandi
name: Expandi
url: https://www.starterstory.com/stories/expandi   # 一手来源，必填
source: starterstory_stories                        # starterstory_stories /
                                                    # starterstory_businesses /
                                                    # trustmrr / hackernews / newssearch
evidence_level: interviewed
monthly_revenue_usd: 60000
revenue_note: 创始人自报，未经审计
startup_cost_usd: null
first_customers: LinkedIn 自动化内容 + 社群
channels: [LinkedIn, 社交媒体, 联盟计划]
replaces: 销售"手写"LinkedIn 加好友与 follow-up
ai_relevance: high
related_pool_slugs: []          # 与产品池合并时填对方 slug
playbooks: [自动化冷启动, 联盟计划]
summary_zh: …
summary_en: …
first_seen: '2026-09-06T00:00:00Z'
last_seen: '2026-09-06T00:00:00Z'
```

去重与合并：案例公司若已存在于产品池（同域名或同产品名），并入既有档案，
在既有档案上加 `case_*` 字段，不另立条目——一个产品一份档案的原则不变。

## 5. 采集与富化流程

1. **发现**：新 collector（`src/xocto/sources/casestudies.py`）。首次运行读
   sitemap 建立全量清单，之后每日增量比对 sitemap 与本地清单；TrustMRR 每日
   拉首页与新增 `/startup/<slug>`。输出进 `data/raw/<date>.jsonl`，
   `kind: casestudy`。
2. **过滤**：编辑层（config/filter.md 追加「案例」一节）判断是否满足第 3 节
   收录边界，尤其 AI 相关性与打法迁移价值。
3. **富化**：DeepSeek 按 config/template.md 追加的「案例」模板抽取第 4 节
   字段；抽取不到的字段写 null，禁止编造。生成 `data/casestudies/<slug>.md`。
4. **判定**：进入 req_review 的真需求判定流程——SPEC 2.2 的规则不变，
   公开结论只能是真需求、伪需求或需求不成立。
5. **展示**：site.py 渲染。机会库筛选维度增加「有案例」；已验证生意卡片
   挂接案例详情；打法库从 `playbooks` 字段聚合；每周挑 3–5 条进日报
   （ rotation 逻辑复用已验证生意的按日轮换）。

## 6. 反参照

- 不做「2996 条任你浏览」的数据库页——案例入口只有机会库与日报；
- 不写「直接抄作业」「月入 X 万」式营销话术——PRODUCT.md 调性约束不变；
- 不因源站有 3000 条就降低编辑标准，每天进不了 1 条就空着。

## 7. 实施顺序

1. collector + sources.yaml 配置 + sitemap 增量（含限速与 health）；
2. frontmatter 数据模型与去重合并；
3. template.md 案例模板 + DeepSeek 富化；
4. 机会库筛选维度与已验证生意卡片挂接；
5. 日报轮换与打法库聚合；
6. i18n 词条、字体子集、测试。

## 8. 验收标准

- 断网任一外部源，管线降级不崩溃，health 页报警；
- 每条公开展示的案例都有可点击的一手来源链接与证据等级；
- 首次导入后，`/stories/*` 清单入库数不低于 3000，被编辑层淘汰的比例如实
  呈现在 status 中；
- 页面上不存在未标证据等级的收入数字；
- 案例正文中不出现来自源站的连续 20 字以上原文（中英同理）。

## 9. 实施记录（2026-09-06）

第一期按第 7 节顺序落地，与规格的差异和现状如下：

- **采集独立成 `xocto cases` 命令**，不进 sources.yaml 编排。原因：案例采集
  需要 manifest 增量状态，而 sources.yaml 的采集器签名 `fetch(cfg, http)`
  不接触存储；硬塞进去要改全部采集器的签名。配置拆成
  `config/cases.yaml`（设置）与 `config/cases.md`（富化判断模板）。
- **健康检查豁免**：案例管线写入 raw 的源名 `casestudies`、`trustmrr` 列入
  sources.yaml 的 `health.standalone_sources`，避免每天误报
  「配置和实际不一致」。
- **merge_into_pool 跳过 `kind=casestudy`**：rebuild 从历史存档整池重建时，
  案例条目也不会混进产品池。
- **首批数据已入库**：60 篇采访 + 20 条 TrustMRR 记录；4 条已富化上站
  （chatbase、comp-ai、snackable、diesel-laptops），其余由每日 Actions 以
  每次最多 15 条的速度富化。
- **呈现**：案例详情页 `c/<slug>.html`（双语），首页「谁在为它付钱」
  每天轮换三条。第 5 节的机会库筛选、产品页案例区块、打法库聚合留待
  案例攒到几十条后接（先有数据再做入口，避免空板块）。
