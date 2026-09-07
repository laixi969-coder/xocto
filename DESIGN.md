# DESIGN.md

x-octo 的设计系统。纯静态站，`tokens.css` + `templates/style.css`，无前端框架。

> 改了实现就回来改这份文档，不要反过来。2026-08-11 这份文档曾经落后于实现整整
> 一次改版（还记着已经废弃的暖橙配色），直接后果是 `--ink-faint` 的对比度回归
> 没人发现——文档里写着"通过 WCAG AA"，实测只有 3.72:1。
> **凡是文档里写成承诺的数字，都要能被一条命令复算。**

## 定位：情报终端 × Linear-desk 编辑部

不是产品目录，不是数据看板。是一个有主见的编辑在跟你说话——冷中性底、更密的顶栏与筛选 chrome、
描边图标始终可见，暖陶红只作 Linear 式信号（链接 / 选中下划线 / 焦点）。

**场景句**：一个做商业判断的人，早上第一件事，在 27 寸屏幕上花三分钟扫一遍
昨夜全球冒出来的东西，找一两个值得深看的。明亮的房间，注意力有限，随时会关掉。

→ 这个场景要求**浅色为底**（明亮环境、长文阅读），暗色作为可切换项而非默认。

## Hallmark 系统

- **Genre**：editorial。
- **主页**：Marquee Hero。标题先给当天判断，证据块在右侧承接；首屏之后转为决策流。
- **机会库**：Workbench。筛选器是工作台，结果用两列信息行承载，不另设稀疏的右侧标签栏。
- **报告 / 详情 / 方法页**：Long Document。正文保持 45–75 字符阅读宽度，但标题、目录、证据与判断块使用完整网格。
- **导航**：Dense sticky chrome（~48px）；图标+短标签，8px 间距；选中态用更强墨色 + signal 下划线。
- **页脚**：Ft5 Statement；站点定位是结束语，数据与方法链接退到下一行。
- **结构原则**：卡片可用细边框（line-soft）而非只靠纸面岛屿；横线留给表格、输入、当前导航。
- **图标**：`templates/icons.html` 统一 24×24 viewBox、stroke-width 2；CSS 强制 `.ico` 为 20×20 / opacity 1。

## 品牌标识

`templates/logo/` 下四个文件，构建时拷到 `site/logo/`：

| 文件 | 内容 | 用在 |
|------|------|------|
| `logo-on-light.png` | 完整锁标，navy `#25345c` | 浅色底，宽屏 |
| `logo-on-dark.png` | 完整锁标，白色 | 暗色底，宽屏 |
| `mark-on-light.png` | 只有章鱼图形，navy | 浅色底，≤640px |
| `mark-on-dark.png` | 只有章鱼图形，白色 | 暗色底，≤640px |

三条规矩：

1. **换版靠 `--logo` / `--logo-mark` 两个 token**，不用两个 `<img>`，也不用
   `<picture>`——`<picture>` 的 media 查询认系统偏好，认不了站内的手动切换。
2. **窄屏只出图形**。完整锁标宽高比 4.2:1，在 375px 上会把导航挤到换行。
3. **`.brand` 里的文字不删只藏**（`clip-path: inset(50%)`）。标识是背景图，
   读屏和高对比度模式下链接仍然要有名字。

资源规格：@3× 导出，PNG-8 128 色量化。四个文件合计 11KB，
合成到实际底色后色差 <1.1/255（即肉眼不可辨）。别用 PNG-32，那是 41KB。

navy `#25345c` 是品牌色，和站内的 deep-forest 不同色系。这是刻意的：
标识是标识，界面是界面，不需要统一。

## 色彩

策略：**Restrained Linear-desk**——冷中性纸面、更高对比墨色、一个暖陶红 signal（Linear 式强调）。
强调色占比 ≤3%，只用于链接、选中态、焦点与短锚点；状态色只承担「已验证 / 观察」语义。
所有颜色以根目录 `tokens.css` 的 OKLCH token 为准，页面样式不得写一次性颜色值。

| 角色 | 浅色 | 暗色 | 用途 |
|------|------|------|------|
| paper | `oklch(96.9% 0.0055 250)` | `oklch(18.5% 0.02 255)` | 页面画布，冷灰白 / 深墨蓝 |
| surface | `oklch(99.1% 0.0025 250)` | `oklch(22.8% 0.026 255)` | 判断块、筛选器、目录 |
| ink | `oklch(22% 0.034 255)` | `oklch(95.5% 0.01 95)` | 正文 |
| ink-soft | `oklch(39% 0.028 252)` | `oklch(80% 0.01 120)` | 次级文字 |
| ink-faint | `oklch(47.5% 0.02 248)` | `oklch(68% 0.014 235)` | 标签、元信息 |
| line | `oklch(84% 0.009 250)` | `oklch(38% 0.022 255)` | 数据边界、控件、卡片描边 |
| signal | `oklch(53.46% 0.1258 35.8)` | `oklch(76.29% 0.1082 40)` | 链接、选中、焦点、短锚点 |
| signal-soft | `oklch(93.2% 0.024 42)` | `oklch(30% 0.04 25)` | 语义判断垫底 |
| good | `oklch(48.54% 0.0816 179.1)` | `oklch(74.87% 0.0777 174.3)` | 「值得关注」评级 |
| watch | `oklch(51.06% 0.1081 64.6)` | `oklch(80.93% 0.1137 79.1)` | 「有待观察」评级 |

### 对比度硬底线

**所有承担文字的 token，在 paper 和 surface 上都必须 ≥4.5:1**（WCAG AA 1.4.3）。
`ink-faint` 和 `watch` 是最容易破线的两个，因为它们本来就该"弱"。
换配色之后必须复算，命令见本文件末尾。

对比度以 `uv run python scripts/check_design.py` 实测为准（换色后必须复算）。
`ink-faint` 与 `watch` 最容易贴 AA 底线，动之前先跑检查脚本。

`scripts/check_design.py` 同时解析 hex 和 OKLCH；换色后仍由同一条命令复算。

## 排版

- **展示标题**：`"Fraunces", "Noto Sans SC"`，roman only —— 拉丁走 Fraunces，中文走思源黑体 Bold。
  混排时同一行里两套字体各管自己的字符集。
- **正文 / UI**：`"Inter"` + PingFang SC 兜中文。Inter 只负责拉丁。
- **数字**：沿用 Inter，通过 `font-variant-numeric: tabular-nums` 对齐表格数字。
  不额外引入第三套等宽字族，避免标签与数字把全站带成开发者工具气质。
- 字体全部自托管（`src/xocto/fonts.py` 构建时拷贝/子集化），不依赖 CDN。
  构建会复制 Inter 与 Fraunces，并对子集化后的中文标题字体做本地加载。

层级靠**字号 + 字重 + 字体族**三者拉开，不靠单一维度：

| 层级 | 字号 | 字体 | 字重 |
|------|------|------|------|
| 报头主标题 | clamp(27px, 3.7vw, 44px) | serif | 700 |
| 页面主标题 | clamp(36px, 4.6vw, 56px) | serif | 700 |
| 版块标题 | clamp(23px, 2.6vw, 31px) | serif | 700 |
| 卡片/条目标题 | 17-21px | sans | 600 |
| **长文正文** | **16px / 行高 1.78** | sans | 400 |
| 界面正文 | 16px / 行高 1.7 | sans | 400 |
| 元信息/标签 | 12.5-14.5px | sans | 400-600 |

正文最小 16px。长文通过 `74ch` 的阅读宽度与 1.78 行高控制密度，不再靠缩小字号
换取单行字数；UI 元信息可降到 12–14px，但不承担正文信息。

## 间距与布局

- 版心最大宽 `--maxw: 1480px`。1200 在 27 寸屏上两侧各留 400px 死白，
  反而把内容挤成一条窄带。
- 报告正文阅读宽 `74ch`；展示标题用 `min(…em, 100%)` 吃满网格，不再用过紧的 `ch` 上限（首页 lede / 报告 masthead / 页脚声明同理）。侧栏 210px，栏距使用 54–112px fluid gap。
- 换行策略：桌面正文与卡片用 `overflow-wrap: break-word`；窄屏中英混排标题仍允许 `anywhere`，避免长英文词撑破视口。
  阅读段落不盲目拉满，但目录、证据、判断和元信息必须使用右侧空间。
- 区块间距 48–88px，连续区块交替使用 paper / paper-3，而不是连续横线。
- **刻意不对称**：顶部条 1.9fr / 1fr，首页判断条目 1fr / 2.4fr。
- **少用卡片，但不用横线模拟所有层级**：表格保留 hairline；判断、筛选、目录、分页使用
  单层 surface island。禁止嵌套卡片。
  `products.html` 的机会库条目使用两列信息行：左列名称与标签，右列说明、规模和商业摘要；
  目录只保留扫读所需的说明、规模、标签与状态，完整进入窗口放在详情页，
  避免产品增长后把重复正文无限写进一个 HTML 文档。

### 触控目标

**所有可点元素 ≥44px**（WCAG 2.5.5）。做法是**把内边距从容器挪到目标本身**：
顶栏自己只留 6px，导航链接和按钮各自 `min-height: 44px`。
这样点击区够大，顶栏总高反而比原来还矮 1px。

导航项之间 `gap` 收到 4px（窄屏 0），让相邻目标直接相接——
中间留空隙就等于留了一条"点了没反应"的死区。

## 动效

- 缓动统一 `cubic-bezier(0.16, 1, 0.3, 1)`，200ms。不用 bounce/elastic。
- **只动 `transform` 和 `opacity`**。位移用 `translateX` 不用 `padding`——
  padding 每一帧都要重排整条列表。
- 载入用 `animation-delay` 级联，每项差 60-70ms。
- hover 反馈：内容标题只变 signal 色，不叠加位移或投影。每个元素只用一种主要反馈。
- 不写 `transition: all`，列清楚实际会变的属性。
- 全局尊重 `prefers-reduced-motion`。

## 无障碍

- 所有交互状态都要有**程序化等价物**，不能只有视觉。
  筛选按钮的 `aria-pressed` 必须在**首屏 HTML 里就是对的**，
  不能等第一次点击才补；「清掉筛选」这类批量重置也必须同步 aria。
  只清 class 不清 aria，读屏用户拿到的是**相反**的状态，比没有更糟。
- 主题切换按钮同理：`aria-pressed` 初始就要说对当前是明还是暗。
- 每组筛选器 `role="group"` + `aria-label`，把可见的「方向/阶段/评级」关联上。
- 焦点环 `2px solid var(--signal)` + 3px offset（非文字只需 3:1，实测 5.41:1）。
- 跳转链接、`.totop` 的 `aria-label`。
- `<html lang>` 跟着语种走（中文站 `zh-CN`，英文站 `en`）。
  语言切换链接自己带 `lang` + `hreflang`，指向的是另一语种 ——
  不标的话读屏会用当前语言的发音去念「中文」两个字。

## 组件清单

### 全站

| 类名 | 用途 |
|------|------|
| `.brand` | 标识链接，背景图换版，文字视觉隐藏 |
| `.lede-bar` | 顶部条，左右不对称，直接给结论不喊标语 |
| `.pick` | 首页判断条目，左边名字右边内容 |
| `.rows` / `.row-insp` | 密集列表；灵感用 signal-soft surface 标记 |
| `.tbl` / `.scroll-x` | 数据表，数字等宽；窄屏在容器内横滑 |
| `.obs-item` | 每日观察卡片入口 |
| `.cat` | 赛道入口 |
| `.card` / `.card-proven` | 产品卡，已验证型重数据、早期型重描述 |
| `.verdict` | 三档评级标签。类名用稳定键 `.v-strong` / `.v-notable` / `.v-unproven`，不用评级文字——中英文各写各的词，认文字会让英文站的徽章整片掉色 |
| `.top-tools` / `.lang-btn` | 顶栏右侧两个开关：语言与明暗。都是"改变整站呈现"，不是导航 |
| `.brand-block` / `.brand-tag` | 标识 + 一句话说明（中文「全球 AI 应用雷达」/ 英文 "Global AI product radar"）。词标只说了名字没说做什么，进任何一页都该一眼看懂这站干嘛的。竖线分隔，≤640px 撤掉——顶栏挤到换行比少一句说明糟得多 |
| `.field-take` | 可迁移点；用 16px 内缩和文字层级表达，不在卡片里再套一张卡片 |
| `.prose` | 整篇 Markdown（产品详情），16px/1.78，最大 74ch |

### 报告页（`templates/report.html`）

报告是全站唯一的长文页。扁平 Markdown 在 `src/xocto/report.py` 里切成有层级的
版块结构再渲染——整篇丢给渲染器会得到一条没有主次的直线。

| 类名 | 用途 |
|------|------|
| `.masthead` | 报头。日期降成刊号，标题位置给当天那句结论 |
| `.masthead-rule` | 76px signal 短锚点，只保留一个页面级规则 |
| `.toc` | 本期目录卡，编号 + 副标 + 条数，进门先给地图 |
| `.sec-bar` | 版块头，编号置于标题上方，条数落在右下；靠字号与间距分层，不铺整条线 |
| `.sec-quiet` | 边界/免责版块，整块降权 |
| `.pick-card` | 上榜产品卡，排名/名字/徽章/指标各自成件 |
| `.pick-lead` | 一句话定位，放大一档 |
| `.report-rail` | 滚动定位条 + 往期入口，≤1120px 撤掉 |
| `.prose-body` | 切好版块后的一小段，和 `.prose` 共用排版规则 |


### 行内 Markdown（`md_inline`）

分析短字段（可借鉴点、灵感、需求判断、首页机会文案）里常有作者写的 `**强调**`。
`src/xocto/site.py` 注册 Jinja 过滤器 `md_inline`：先 HTML escape，再把 `**x**` 转成 `<strong>x</strong>`。
长文正文仍走 mistune（`body_html`）。模板里凡面向读者的短文案用 `| md_inline`，禁止把原始 `**` 漏到页面上。

### 产品详情 / 报告 desk

- `templates/product.html` → `.product-desk`：密报头、分区编号、描边判断块、证据折叠。
- `templates/takeaways.html` → `.takeaways-desk`：每个案例三栏——这是什么、功能、可参考；不盖生意判断徽章。
- `templates/report.html` / `reports.html` → `.report-desk` / `.reports-desk`：与首页/打法库同一套 command + bordered sections。
- `methodology.html` / `privacy.html` → `.reading-desk` 轻量共用 chrome。

## 明确不要

- 侧边色条（`border-left` 粗色条当装饰）。灵感和判断用 `signal-soft` surface 表达语义。
- 渐变（当前 0 处）、玻璃拟态、重投影、三栏等宽卡片行；surface 只允许 1px whisper shadow
- 图标（当前 0 个）。尤其不要"每个标题上方一个圆角大图标"
- emoji、感叹号、em dash
- 大标题喊口号（"每天挖掘全球 AI 应用" 这种）
- 重复文案：标题里已经写了数量就别再右对齐标一次

## 缓存与收录（`vercel.json` / `write_seo`）

线上 `https://xocto.vercel.app`，只有带 `.html` 的路径能访问（`/products` 是 404），
所以 canonical 必须带扩展名。首页例外：`/` 和 `/index.html` 收敛到 `/`。

**缓存按各资源的实测变更频率分档，不要一律 immutable。**

| 资源 | max-age | 为什么 |
|------|---------|--------|
| HTML（含 `/`） | 0 + s-maxage 300 | 每天变 |
| `style.css` | 1 小时 | 改样式的频率 |
| `inter-*` / `fraunces-*` | 30 天 | 史上变过 1 次 |
| `noto-sans-sc-*-subset` | **1 天** | 见下 |
| `logo/*` | 7 天 | 变过 1 次 |

中文子集那 87KB 是全站最大的文件，却**只能缓存 1 天**，两个理由：

1. 它按标题字符集生成，报告标题出现新字就重新生成 —— 实测已变过 2 次。
2. 更要命的是失效方式：子集过期后新字会逐字回落到 PingFang SC，
   于是**一行标题里混着两种字重**，比多花一个 RTT 难看得多。

**内容哈希文件名：测过，不做。** 所有资源都带强 etag，不哈希的真实代价是
每次访问几个 304 条件请求（几百字节），不是重下 208KB。用哈希省掉这几个 RTT，
代价是构建时后处理 163 个文件加一个新故障源 —— 不值。
要重新评估的话，先 `curl -I` 看线上响应头，别凭感觉。

**收录**：`robots.txt` 全放开并指向 sitemap；`sitemap.xml` 只写 loc + lastmod
（priority/changefreq 主流引擎早就不看）。每页的 description 用它自己的内容 ——
产品页用产品简介，报告页用当天那句钩子。163 个页面共用一句通用描述，
对搜索引擎等于没有描述。

## Exports

根目录 `tokens.css` 是完整 source of truth；下面三种是同一系统的便携映射。

### tokens.css

```css
@import "tokens.css";
/* 页面只消费 --color-* / --font-* / --space-* / --text-* / --ease-* token。 */
```

### Tailwind v4 `@theme`

```css
@theme {
  --color-paper: oklch(96.9% 0.0055 250);
  --color-paper-2: oklch(99.1% 0.0025 250);
  --color-paper-3: oklch(94.2% 0.007 250);
  --color-ink: oklch(22% 0.034 255);
  --color-ink-2: oklch(39% 0.028 252);
  --color-muted: oklch(47.5% 0.02 248);
  --color-rule: oklch(84% 0.009 250);
  --color-accent: oklch(53.46% 0.1258 35.8);
  --font-display: "Fraunces", "Noto Sans SC", ui-serif, serif;
  --font-body: "Inter", ui-sans-serif, sans-serif;
  --font-outlier: var(--font-body);
  --spacing-sm: 1rem;
  --spacing-md: 1.5rem;
  --spacing-lg: 2rem;
  --spacing-xl: 3rem;
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --radius-card: 10px;
}
```

### DTCG `tokens.json`

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "color": {
    "paper": { "$value": "oklch(96.9% 0.0055 250)", "$type": "color" },
    "surface": { "$value": "oklch(99.1% 0.0025 250)", "$type": "color" },
    "ink": { "$value": "oklch(22% 0.034 255)", "$type": "color" },
    "muted": { "$value": "oklch(47.5% 0.02 248)", "$type": "color" },
    "accent": { "$value": "oklch(53.46% 0.1258 35.8)", "$type": "color" }
  },
  "font": {
    "display": { "$value": "Fraunces, Noto Sans SC, serif", "$type": "fontFamily" },
    "body": { "$value": "Inter, sans-serif", "$type": "fontFamily" }
  },
  "space": {
    "md": { "$value": "1.5rem", "$type": "dimension" },
    "xl": { "$value": "3rem", "$type": "dimension" }
  }
}
```

### shadcn/ui CSS variables

```css
:root {
  --background: 96.13% 0.0111 89.7;
  --foreground: 26.05% 0.0375 253.9;
  --card: 98.77% 0.0054 95.1;
  --card-foreground: 26.05% 0.0375 253.9;
  --primary: 53.46% 0.1258 35.8;
  --primary-foreground: 98.77% 0.0054 95.1;
  --muted: 82% 0.014 89.7;
  --muted-foreground: 53.74% 0.0241 241.7;
  --border: 82% 0.014 89.7;
  --input: 82% 0.014 89.7;
  --ring: 53.46% 0.1258 35.8;
  --radius: 10px;
}
```

## 改完必须跑

```bash
uv run xocto build && python3 scripts/check_design.py
```

`scripts/check_design.py` 复算五件事：token 对比度、来源泄漏、**中文漏进英文站**、
站内死链、sitemap 自洽。它是上面那些数字的唯一真相——文档和它对不上，改文档。

「中文漏进英文站」这条的存在理由和另外几条一样：新采到的产品没写 `inspiration_en`、
新写的分析忘了出英文版、新出现的细分榜没登记译名，页面只会安静地少一块或混一段中文，
没有人会报错。产品名里的中文是合法的（豆包、纳米AI 是专有名词，翻译它等于伪造它），
所以检查会先把产品档案里的中文名扣掉，剩下的才算漏译。
这条检查验证过能抓到真故障：英文灵感里混中文、细分榜漏登记译名，两种情况下退出码都是 1。

## 两个语种

中文在 `site/`，英文在 `site/en/`。**模板只有一套，渲染两次** ——
复制一份英文模板一定会跑偏：改了中文版的间距，英文版就落后一个版本，而且没人会发现。
所有随语种变化的东西（界面文案、赛道名、评级词、指标口径、日期格式、阅读速度）
都在 `src/xocto/i18n.py` 里。

英文缺内容就整块不显示，**绝不回退成中文** —— 英文页面里混一段中文比缺一块更糟。

窄屏顶栏现在有三个控件（导航 + 语言 + 明暗），英文词又比中文长。
320 / 375 / 414 / 768px 上两个语种的主要页面都不得横向溢出。点击文字保持单行；
长英文词与展示标题允许在词内安全换行。
