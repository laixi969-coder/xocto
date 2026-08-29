# x-octo

每天挖全球新冒出来的 AI 应用，砍掉噪音，对留下的做商业分析，出一份三分钟能读完的中文简报。

---

## 每天怎么用

**第一步，采集**（大约 30 秒）：

```bash
cd ~/x-octo && uv run xocto collect
```

它会去新品平台、开发者社区、开源生态、增长榜单、公司一手更新和独立行业研究扫一遍；
重复的自动跳过。采集面要比站上展示宽，公开前仍会按商业价值过滤。

**第二步，云端判断和出日报**：

GitHub Actions 会调用 DeepSeek，读取 `config/filter.md` 的规则把噪音砍掉，
再按 `config/template.md` 的模板做分析，最后把简报写到 `data/reports/`。

**第三步，生成网站**：

```bash
cd ~/x-octo && uv run xocto build && open site/index.html
```

把 `data/` 里的东西变成一个能直接打开的网站：首页直接给当天判断；机会库可按场景、阶段和
信号筛选；每个详情页先给 60 秒商业判断。无需先选“我是创始人还是投资人”——同一人可以同时带着多种问题来。

**想随时看现状**：

```bash
cd ~/x-octo && uv run xocto status
```

---

## 为什么分两步

抓取是体力活，交给程序。判断是编辑工作，交给 DeepSeek API 在 GitHub Actions 里完成。
仓库不依赖 Codex、Claude Code 或任何人的电脑；唯一需要的密钥是 GitHub Secret
`DEEPSEEK_API_KEY`。

整条流程都接了 GitHub Actions 定时：采集、DeepSeek 筛选和双语日报都在云端完成，
早上七点多打开站就是当天写好的。上面那三条命令一直有效，想临时补一次、
或者想自己盯着改，随时手动跑。

---

## 你可以改的三个文件

都在 `config/` 里，都是大白话写的，改完不用动代码：

| 文件 | 管什么 | 什么时候改 |
|------|--------|-----------|
| `filter.md` | 什么值得看、什么是套壳 | 觉得每天推给你的东西不对味 |
| `template.md` | 分析要输出哪些内容 | 觉得分析写得没用或太啰嗦 |
| `sources.yaml` | 去哪些网站抓、抓多少 | 想加源、或者觉得抓太多/太少 |

**`filter.md` 是整套系统的灵魂。** 它决定了你每天收到的是 5 条有用的，还是 100 条垃圾。
现在里面是初稿，等你看过几天实际输出后应该重写它。

---

## 东西都存在哪

```
data/raw/2026-08-11.jsonl   当天抓到的原始数据，只增不改
data/pool/<产品名>.md        每个产品一个档案，去重后的唯一记录
data/analysis/<产品名>.md    深度分析
data/reports/2026-08-11.md   每日简报 ← 你主要看这个
```

产品档案是纯文本，你可以直接打开看、直接编辑。
文件里 `## 笔记` 那一行以下是留给你写东西的，程序永远不会覆盖它。

---

## 现在做到哪了

**已经能跑：**
- 七类免费公开信号持续采集：
  - **新品平台 / 开发者社区 / GitHub / Hugging Face** —— 找刚冒出来的东西，没数据，靠判断
  - **AICPB（AI 产品榜）** —— 找已经跑出规模的产品，带真实访问量、月活和环比，含独立的中国榜
  - **公司一手博客 / GitHub 官方 Release** —— 捕捉能力和基础设施变化，只作日报背景
  - **独立研究 / 开发者观察 / 行业媒体** —— 补齐采用、分发、成本和市场结构信号，不直接充当产品
- 同一个产品从不同网站进来能认出是同一个，不会重复建档
- 同一天跑十次和跑一次结果一样，不会重复堆数据
- 创始人信息一并记录（判断早期项目时，人往往比产品更能说明问题）
- GitHub 发现走关键词、专题、官方组织和新项目爆发四条独立链路；同时监控一组重点官方仓库的 Release

**还在完善：**
- 纯内销、不出海的中国 AI 产品仍然抓不全（见下方"关于中文源"）
- Reddit 和 YC 这两个源没接（Reddit 封了免登录接口，YC 是动态页面抓取脆弱）
- 产品官网还没深挖（Product Hunt 只给它自己的页面链接，真官网要再跳一次）

---

## 网站

`uv run xocto build` 会生成 `site/` 目录，那就是整个网站，纯静态：

| 页面 | 内容 |
|------|------|
| `index.html` | 今日机会 → 三个值得继续看的案例 → 证据与观察 |
| `products.html` | 机会库，按**场景**、**阶段**、**评级**三个维度筛选 |
| `p/<产品>.html` | 产品详情：60 秒商业判断（谁付钱、为什么现在、怎样切入、下一步看什么）置顶，然后是分析全文 |
| `r/<日期>.html` | 每日观察 |
| `reports.html` | 全部往期观察，按月永久归档 |
| `en/…` | 同样四类页面的英文版，结构一模一样 |

**版块顺序按决策距离排：先确定“我为什么来”，再看机会，最后追溯证据。**
首页让不同读者各走一条阅读路径；详情页先回答谁付钱、替代什么旧行为和能怎样小步验证，
再展开完整分析。用户不必先学习一堆工具名，才知道它与自己有什么关系。

**网站上不出现任何数据源名称。** 用户不关心东西从哪抓的，那是实现细节。
只显示两个对用户有意义的维度：阶段（刚冒头 / 已验证）和方向（赛道）。

**两类产品的卡片长得不一样**，因为判断方式本来就不同：

- **刚冒头** —— 你不知道它是什么，所以显示描述
- **已验证** —— 你本来就知道（豆包、DeepSeek 这类），所以显示流量和环比

**中英文两个语种并存。** 中文在根目录，英文在 `en/`，地址一一对应
（`/p/xxx.html` ↔ `/en/p/xxx.html`），顶栏右上角切换。
中文站的地址一个没变。

英文内容是单独写的，不是机器翻的：产品的英文一句话和灵感存在同一个产品档案里
（`summary_en` / `inspiration_en`），深度分析和每日观察放在 `data/analysis/en/`
和 `data/reports/en/`。**没写英文的地方，英文页面就整块不显示，不会退回中文。**
差多少用 `uv run xocto status` 看，漏出来的中文用 `python3 scripts/check_design.py` 抓。

**没有服务器、没有数据库、没有月费。** 双击 `index.html` 就能看，
也可以整个 `site/` 目录丢到任何托管上。支持明暗两套配色，手机上也能看。

### 部署到 Vercel

仓库里已经配好了 `vercel.json` 和 `.vercelignore`，直接连上就行。

**在 Vercel 上要这么设：**

| 项目 | 填什么 |
|------|--------|
| Framework Preset | **Other**（不要选 Python，也不要让它自动检测） |
| Build Command | 留空（`vercel.json` 里已经写死了） |
| Output Directory | `site` |
| Install Command | 留空 |

**如果它报「未找到 Python 入口点」**，是因为它看到 `pyproject.toml` 就以为这是个后端项目。
`.vercelignore` 已经把 `pyproject.toml` 排除掉了，重新部署一次就好；
还不行的话去项目设置里把 Framework Preset 手动改成 Other。

### SEO / GEO 上线后只需做一次的事

代码会自动生成每页的 canonical、双语 hreflang、Open Graph、Schema.org JSON-LD、
`robots.txt`、`sitemap.xml` 和给 AI 引擎读取的 `llms.txt`。部署后仍需由站点所有者
完成两件平台侧操作：

1. 在 [Google Search Console](https://search.google.com/search-console/) 和
   [Bing Webmaster Tools](https://www.bing.com/webmasters/) 验证 `xocto.vercel.app`（或未来的自有域名）。
2. 分别提交 `https://xocto.vercel.app/sitemap.xml`；部署后可用
   `https://xocto.vercel.app/llms.txt` 查看给 AI 引擎的站点说明。

如果改用自有域名，先将 `src/xocto/site.py` 中的 `BASE_URL` 改成新域名，再重新生成并部署；
否则 canonical、sitemap 和结构化数据仍会指向旧地址。

### 每天自动更新（已接好，你什么都不用做）

两班倒，一小时错开，全部按北京时间：

| 时间 | 谁在跑 | 干什么 |
|------|--------|--------|
| **06:17** | GitHub Actions（`.github/workflows/daily.yml`） | 采集 → 清理过老存档 → 生成网站 → 提交推送 |
| **采集完成后** | 同一 GitHub Actions 工作流中的 DeepSeek | 过滤 → 写中英文简报 → 复算约束 → 提交推送 |

推送完 Vercel 自动部署，所以你七点多打开站，看到的是当天已经写好的简报。
单个源没抓到、或页面检查没过，站点仍会先上线，GitHub Actions 变红；不能因为门禁让日期停在昨天。日报必须给出一条方向判断，不许写成「今天没有值得展开的」。

采集面必须一直比站上展示的更宽：新产品平台、已跑出规模的榜单、公司一手发布、独立作者和公开讨论。它们进原始存档；只有能讲成生意的才公开。站上不列来源名单。

**为什么不放整点**：GitHub 官方说明整点负载最高，定时任务会迟到，极端时甚至会被丢弃；
所以采集改在 06:17。需要重写当天日报时，可从 Actions 的 Run workflow 面板勾选
`revise_daily_brief`；它会保留已有观察并把新候选增补进去。

**为什么是 6 点多不是 9 点**：读者要在 7 点看到成品，采集必须赶在写简报之前。
代价是 6 点多对应美西前一天下午，Product Hunt 当天的榜单还差几个小时收摊，
票数比原来 9 点那版更「生」一点。

首次启用前，在 GitHub 仓库的 **Settings → Secrets and variables → Actions** 新建
`DEEPSEEK_API_KEY`（可选 `DEEPSEEK_MODEL` 覆盖默认模型）。GitHub 搜索使用工作流内置的
短期 `GITHUB_TOKEN`，不需要另配密钥；之后想立刻跑一次，
去 GitHub 仓库的 Actions 页面点「每日采集」的 Run workflow。

**没有人会复核**。判断层写完直接上线，写歪了也会直接上站，你事后才能改。
这是拿「每天准时有」换「每天有人把关」，想换回来就把自动任务改成开 PR 而不是直接 push。

DeepSeek 判断层运行在 GitHub Actions；电脑是否开机、Codex 或 Claude Code 是否登录都
不会影响更新。若密钥缺失或模型调用失败，采集结果会先推送，日报步骤会明确失败，
不会悄悄把旧日报冒充成新日报。

判断按批次保存临时断点。某一批失败时，已经通过校验的批次不会被丢弃；下一次运行
只从第一个未完成批次继续。断点位于 `data/brief-progress/`，双语日报成功发布后自动删除。
降级运行的提交会明确标为“每日降级构建”，不会伪装成判断已经完成。

### 手动跑

```bash
cd ~/x-octo && uv run xocto collect && uv run xocto build
git add -A && git commit -m "chore: 更新每日数据" && git push
```

**注意 `site/` 目录必须提交进仓库** —— Vercel 上不跑构建，它只是把这个目录原样发出去。

### 让 Product Hunt 那部分的判断变准

现在 PH 的产品只有一句 tagline，因为它除了 RSS 之外整站 403。
配一个免费 token 就能拿到**真实官网、票数、官方分类**三样东西。

1. 去 [producthunt.com/v2/oauth/applications](https://www.producthunt.com/v2/oauth/applications) 新建一个 application（免费，五分钟）
2. 拿到 **Developer Token**
3. 本地用：在终端里 `export PRODUCTHUNT_TOKEN=你的token`（或写进 shell 配置）
4. 云端用：GitHub 仓库 → Settings → Secrets and variables → Actions → New secret，
   名字填 `PRODUCTHUNT_TOKEN`，然后在 `daily.yml` 的采集那步加上：
   ```yaml
   env:
     PRODUCTHUNT_TOKEN: ${{ secrets.PRODUCTHUNT_TOKEN }}
   ```

**token 只从环境变量读，不进配置文件也不进仓库。**
没配 token 时自动退回 RSS 模式，功能照常，只是信息少一些。

**GitHub Pages 也能用，但要求仓库公开**（当前 `laixi969-coder/xocto` 是私有的）。

## 关于中文源

实测了 10 个渠道，结论是：**中文世界没有 Product Hunt 那样的「每日新品流」**——
不是没找到，是确实不存在。中国 AI 产品的首发渠道是微信公众号、即刻、小红书这些封闭平台，
没有公开的结构化入口。

测过并放弃的：

| 渠道 | 实测结果 |
|------|---------|
| V2EX 分享创造 | 通，但每次只给 10 条，AI 占 2/10，全是插件级个人副业 |
| AIbase | 108 个产品，但详情是**国外产品的 AI 翻译稿**，不是国产源 |
| ai-bot.cn | 工具导航站，是存量目录不是新品流 |
| 36 氪 RSS | 返回 0 条，feed 已废 |
| 机器之心 RSS | 只有 2 条导航项，feed 是空的 |
| 量子位 RSS | 11 条，全是新闻报道不是产品，趋势有用、发现无用 |
| 少数派 RSS | 工具/生活方式为主，AI 含量低 |
| Founder Park | 域名解析不了 |
| 即刻 | 需要登录，抓不了 |

**唯一拿下的是 AICPB**，而且它的价值比"又一个源"大：它给的是真实流量数据和环比，
能直接回答"这东西到底有没有人用"。已接入三个榜（中国增长率榜、中国总榜、全球增长率榜）。

如果你后面发现漏了重要的国产产品，把产品名告诉 Claude，我们再针对性找源。

## 出问题怎么办

**某个源报错了** —— 不影响其他源，程序会继续跑完并在最后告诉你哪个挂了。
网站改版或封接口是常事，把报错贴给 Claude 就行。

**觉得产品名字解析得不对、想重来** ——

```bash
cd ~/x-octo && uv run xocto collect --force && uv run xocto rebuild
```

这会用最新的规则重新解析。旧的产品档案会被改名备份（`data/pool.bak-*`），不会删掉。
但档案里你手写的笔记不会自动搬过去，重建前先确认。

**想删掉备份** —— `data/pool.bak-*` 这些目录确认没问题后可以自己删。
