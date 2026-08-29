---
slug: obsidian-img
name: SiteData
builder: fantexi178
category: AI + 商业
summary_zh: SiteData 是浏览器插件，用户在 Google 搜索关键词时，它展示该词最近 4 周有多少网站投放 Google Ads，点击可查看具体投放站点、广告主、流量和 DR。AI
  接收关键词查询，返回广告竞争信号，帮助判断关键词是否经过真金白银验证。
inspiration: 趋势是广告情报从搜索量转向真实投放行为，用投放网站数验证商业意图。切入点是面向 SEO、AFF 和 media buying 人群，把广告竞争信号做成默认展示，按查询或订阅收费。
summary_en: SiteData is a browser extension that shows how many sites have run Google Ads for a keyword
  in the last 4 weeks, with clickable details on advertisers, traffic, and DR. AI processes keyword queries
  to return ad competition signals, helping users gauge if a keyword is backed by real ad spend.
inspiration_en: 'Trend: ad intelligence shifts from search volume to actual ad spend, using site count
  to validate commercial intent. Entry: target SEO, affiliate, and media buying professionals, make ad
  competition signals default, and charge per query or subscription.'
priority_review: false
project_type: ai_transformation
industries:
- 数字营销
- SEO
industries_en:
- Digital Marketing
- SEO
jobs:
- SEO 专家
- 联盟营销人员
- 媒体购买人员
jobs_en:
- SEO specialists
- Affiliate marketers
- Media buyers
regions:
- 全球
regions_en:
- Global
open_source: false
url: https://obsidian-img.prodbox.cc/images/2026/08/27/a6940db7-99f2-473f-afa0-ac105dd5da53.png
canonical_url: https://obsidian-img.prodbox.cc/images/2026/08/27/a6940db7-99f2-473f-afa0-ac105dd5da53.png
summary: "![公众号封面图]( https://obsidian-img.prodbox.cc/images/2026/08/27/a6940db7-99f2-473f-afa0-ac105dd5da53.png)\r\
  \n\r\n> 发布摘要：SiteData 原来一次 Google Ads 标题模糊查询最快也要约 6 秒，我最后把搜索层换成 Manticore ，把查询压到约 0.6 秒，也让免费的 Ads 投放站点数从手动触发变成可以自然展示。\r\
  \n\r\n大家好，我是饭特稀。\r\n\r\n最近给 SiteData 做了一次性能优化。\r\n\r\n这次优化不是为了让页面看起来更快一点，而是为了解决一个非常具体的问题：\r\n\r\n**千万级以上\
  \ Google Ads 标题和关键词数据，怎么做到可以实时模糊查询？**\r\n\r\n其实之前这个功能已经有了。\r\n\r\n比如你在 Google 搜索一个关键词，SiteData 插件会在搜索结果页里显示这个关键词最近\
  \ 4 周大概有多少家网站在投放相关广告。\r\n\r\n![Google 搜索页里的 SiteData Ads 网站数]( https://obsidian-img.prodbox.cc/images/2026/08/27/ba37e15e-8cbf-4983-b2e6-da7eb00d2090.png)\r\
  \n\r\n在插件里的热门关键词模块，也会显示每个关键词对应的 Ads 数量。\r\n\r\n这里的数字不是搜索量，也不是 CPC 。\r\n\r\n它更接近一个广告竞争信号：\r\n\r\n**最近\
  \ 4 周，有多少个网站围绕这个关键词投过 Google Ads 。**\r\n\r\n![SiteData 插件热门关键词里的 Ads 数量]( https://obsidian-img.prodbox.cc/images/2026/08/27/56a22033-db66-4a88-8327-fe882eef1496.png)\r\
  \n\r\n还有一点需要说明：\r\n\r\n**这个最近 4 周指定关键词投放站点的功能，目前是免费给用户看的。**\r\n\r\n它也不是一个只能看一眼的静态数字。\r\n\r\n用户可以直接点击这个数字，进入\
  \ SiteData 的 Google Ads Analysis 详情页，看最近 4 周有哪些网站在围绕这个关键词投放广告。\r\n\r\n详情页里会列出相关站点、广告主、流量、DR ，以及进一步查看域名分析的入口。\r\
  \n\r\n比如下面这个关键词，最近 4 周匹配到了 59 个相关投放站点：\r\n\r\n![点击 Ads 数字后查看关键词相关投放站点详情]( https://obsidian-img.prodbox.cc/images/2026/08/27/8ef23582-aa15-44f6-a22d-ca25122f7455.png)\r\
  \n\r\n这个信号对做 SEO 、AFF 、media buying 、网站增长的人很有用。\r\n\r\n因为搜索量只能说明有人搜。\r\n\r\n但有人持续投广告，说明另一个问题：\r\n\r\n\
  **这个关键词背后，可能已经有人愿意花真钱验证。**\r\n\r\n当然，这不代表一定赚钱。\r\n\r\n但它比单纯看搜索量更接近商业行为。\r\n\r\n## 一开始为什么没有默认展示\r\n\r\
  \n这个功能之前没有默认打开。\r\n\r\n原因也很简单：太慢。\r\n\r\nSiteData 后面有大量 Google Ads 数据，其中广告 title 、description 、keyword\
  \ 这类字段非常适合做模糊查询。\r\n\r\n但问题是，数据量到千万级以后，传统 MySQL 直接查广告 title ，哪怕做了基础优化，一次查询最快也要 6 秒左右。\r\n\r\n6 秒是什么概念？\r\
  \n\r\n如果只是后台手动查一次，可以忍。\r\n\r\n如果是用户打开 Google 搜索页，每个关键词都要等这个结果，那就不行。\r\n\r\n所以之前我只能做成手动触发：\r\n\r\n用户真的想看这个广告信号时，再点一下按钮。\r\
  \n\r\n这不是我理想中的体验。\r\n\r\n很多 SiteData 用户其实对这个数据有需求。\r\n\r\n他们不是想多点一个按钮，而是希望在判断关键词、分析竞品、看广告机会时，这个信号默认就在旁边。\r\
  \n\r\n问题就变成了：\r\n\r\n**能不能把一个原本只适合手动触发的慢查询，变成一个可以常态化展示的实时查询？**\r\n\r\n## 继续压 MySQL ，不是最划算的路\r\n\r\n\
  一开始最自然的想法，肯定还是继续优化 MySQL 。\r\n\r\n加索引、拆表、缓存、预计算，这些都可以做。\r\n\r\n但这次的问题有点特殊。\r\n\r\n我要查的不是一个精确字段，也不是简单的\
  \ `domain = xxx.com`。\r\n\r\n更常见的是：\r\n\r\n- title 里是否包含某个关键词\r\n- 用户输入的关键词和广告标题是否接近\r\n- 再叠加国家、语言、时间范围等过滤\r\
  \n- 最后还要统计最近 4 周有多少网站投过广告\r\n\r\n这类查询，本质上已经不是 MySQL 最舒服的场景了。\r\n\r\nMySQL 仍然适合做业务主数据库。\r\n\r\n用户、订单、会员、广告主关系、任务状态，这些数据应该继续放在\
  \ MySQL 。\r\n\r\n但广告 title 的全文搜索和模糊匹配，最好交给专门的搜索引擎。\r\n\r\n所以我开始重新调研搜索方案。\r\n\r\n常见选择当然是 Elasticsearch\
  \ / OpenSearch 。\r\n\r\n它们很成熟，生态也很强。\r\n\r\n但对我这个阶段来说，ES 的问题也很明显：重。\r\n\r\nJVM 、heap 、shard 、refresh\
  \ 、集群运维，这一整套东西当然有价值，但如果只是为了把几千万条广告标题搜快一点，上来就用 ES ，多少有点提前交架构税。\r\n\r\n后来我选了一个相对小众的开源搜索数据库：Manticore Search\r\
  \n\r\n![../../Pasted image 20260827180754.png]( https://obsidian-img.prodbox.cc/images/2026/08/27/e728ead5-75a8-4ba0-8ca1-1c91dd912d61.png?mFUguZ5mZc)\r\
  \n\r\n## 为什么最后选 Manticore\r\n\r\n我选 Manticore ，不是因为它名气最大。\r\n\r\n恰恰相反，它没有 Elasticsearch 那么出圈。\r\n\r\n\
  但它很适合 SiteData 当前这个场景。\r\n\r\nSiteData 这里需要的是：\r\n\r\n- 千万级以上广告标题全文搜索\r\n- 模糊匹配\r\n- 按国家、语言、时间过滤\r\n\
  - 按网站或广告主做统计聚合\r\n- 服务器成本不能太夸张\r\n- 开发接入最好不要太复杂\r\n\r\nManticore 的几个特点刚好对上了。\r\n\r\n第一，它是 C++ 写的，资源占用比较克制。\r\
  \n\r\n第二，它支持 SQL 和 MySQL 协议。\r\n\r\n这点对开发体验很重要。\r\n\r\n你可以用类似这样的方式理解查询：\r\n\r\n```sql\r\nSELECT *\r\n\
  FROM google_ads\r\nWHERE MATCH('ai image generator')\r\nAND country = 'US'\r\nORDER BY last_seen DESC\r\
  \nLIMIT 100;\r\n```\r\n\r\n这比一上来写一大段 ES DSL 更直接。\r\n\r\n第三，它适合做搜索层，而不是替代业务数据库。\r\n\r\n我现在更倾向的架构是：\r\n\
  \r\n```text\r\nMySQL\r\n  负责用户、订单、会员、业务状态\r\n\r\nManticore\r\n  负责 Google Ads title 、description 、keyword\
  \ 的全文搜索、模糊查询、过滤和聚合\r\n```\r\n\r\n![MySQL 到 Manticore 搜索层架构示意]( https://obsidian-img.prodbox.cc/images/2026/08/27/5f3d0bad-3806-478f-a985-72ec604cc286.png)\r\
  \n\r\n也就是说，MySQL 仍然是业务事实来源。\r\n\r\nManticore 专心做一件事：把搜索变快。\r\n\r\n## 上线后的结果\r\n\r\n这次上线以后，最直观的变化是：\r\
  \n\r\n原来 MySQL 查一次最快约 6 秒。\r\n\r\n现在一条广告标题模糊查询，大概 0.6 秒就能返回。\r\n\r\n从用户体验上看，这个差别非常大。\r\n\r\n6 秒的时候，我不敢默认展示。\r\
  \n\r\n0.6 秒的时候，这个功能就有机会从“手动点一下”变成“页面自然呈现”。\r\n\r\n为了验证它不是偶然快，我还做了分阶段压测。\r\n\r\n下面是压测结果：\r\n\r\n![Manticore\
  \ 查询接口分阶段压测结果]( https://obsidian-img.prodbox.cc/images/2026/08/27/4d35f3ee-3ae5-491f-a36c-6f3528bc18b3.jpg)\r\
  \n\r\n在这组测试里，从 1 RPS 到 50 RPS ，错误数都是 0 。\r\n\r\n表里的平均耗时基本在 170ms 到 180ms 左右，P95 大多在 200ms 附近。\r\n\r\n\
  当然，压测数据不能简单等同于真实线上所有场景。\r\n\r\n真实用户请求还会受到网络、接口包装、缓存命中、数据分布、并发形态等因素影响。\r\n\r\n但这至少说明一件事：\r\n\r\n**这个方向是对的。**\r\
  \n\r\n它不再是一个只能偶尔查一下的慢功能，而是有机会进入常规产品体验的功能。\r\n\r\n## 更让我惊喜的是资源占用\r\n\r\n速度变快，其实我有心理预期。\r\n\r\n真正让我惊喜的是资源占用。\r\
  \n\r\n这是机器上的内存情况：\r\n\r\n![服务器 free -m 内存占用截图]( https://obsidian-img.prodbox.cc/images/2026/08/27/f2393568-02ab-4bcd-98f3-03d5fee54bcf.png)\r\
  \n\r\n总内存 8GB 左右，实际 used 只有 662MB ，可用内存还有 7GB 多。\r\n\r\n再看 htop：\r\n\r\n![服务器 htop CPU 和负载截图]( https://obsidian-img.prodbox.cc/images/2026/08/27/f6052469-d957-4606-8ff4-98f0a9981e4b.png)\r\
  \n\r\nCPU 基本没有明显压力，load average 也很低。\r\n\r\n磁盘情况也比我预期轻很多：\r\n\r\n![服务器 df -h 磁盘占用截图]( https://obsidian-img.prodbox.cc/images/2026/08/27/344f6066-791f-4988-bd18-057f7d6c3651.png)\r\
  \n\r\n144G 的盘，只用了 6.3G 。\r\n\r\n这点对独立开发者和小团队很重要。\r\n\r\n很多时候，我们不是做不出功能。\r\n\r\n真正的问题是：\r\n\r\n功能一旦上线，服务器成本会不会跟着起飞？\r\
  \n\r\n如果一个功能必须上更大的机器、更多节点、更复杂的集群运维，那它不只是技术问题，还是商业问题。\r\n\r\n这次 Manticore 给我的感觉是：\r\n\r\n**在当前这个数据量和访问规模下，它把搜索性能和服务器成本控制在了一个很舒服的区间。**\r\
  \n\r\n## 这不是说 Manticore 一定比 ES 好\r\n\r\n我不想把这篇写成“某某数据库吊打某某数据库”。\r\n\r\n这种结论通常没什么意义。\r\n\r\nElasticsearch\
  \ 仍然是非常成熟的搜索基础设施。\r\n\r\n如果你的场景是超大规模集群、自动分片、强 HA 、复杂日志分析、成熟 ELK 生态，ES / OpenSearch 依然很有优势。\r\n\r\n但\
  \ SiteData 这次的问题不是搭一个企业级搜索平台。\r\n\r\n它的问题更具体：\r\n\r\n千万级到亿级广告情报数据里，如何低成本、低运维压力地做全文搜索和模糊匹配？\r\n\r\n在这个阶段，Manticore\
  \ 更像一个务实选择。\r\n\r\n不追求第一天就把架构搭得很重。\r\n\r\n先让最痛的查询快起来。\r\n\r\n等真的遇到单机瓶颈、手工分片瓶颈、更多节点的 HA 需求时，再重新评估 ES\
  \ / OpenSearch 。\r\n\r\n## 对 SiteData 来说，这个优化意味着什么\r\n\r\n这次优化以后，SiteData 的关键词广告信号可以做得更自然。\r\n\r\n以前用户看到一个关键词，想知道有没有人在投广告，需要额外触发。\r\
  \n\r\n现在更理想的体验是：\r\n\r\n你在 Google 搜索一个词。\r\n\r\nSiteData 顺手告诉你：\r\n\r\n- 这个词最近 4 周,甚至 1 年以上有多少网站在投广告\r\
  \n- 这些广告主是否持续出现\r\n- 相关网站是否还有其他关键词在投\r\n- 这个关键词是短期测试，还是已经有持续预算\r\n\r\n这对判断机会很关键。\r\n\r\n因为做网站增长、做 SEO\
  \ 、做 AFF ，最怕的不是没有数据。\r\n\r\n最怕的是数据看起来很多，但离真实商业行为很远。\r\n\r\n搜索量是兴趣。\r\n\r\nCPC 是竞价结果。\r\n\r\n广告投放网站数，是另一层真实行为。\r\
  \n\r\n它不能替你做决定，但能帮你少一点盲猜。\r\n\r\n## 这次给我的几个提醒\r\n\r\n第一，慢功能不一定是产品没价值。\r\n\r\n有些功能不是没人要，而是性能没到可以自然使用的程度。\r\
  \n\r\n当一次查询要 6 秒时，用户会觉得它像一个附加工具。\r\n\r\n当一次查询压到 0.6 秒时，它才有机会变成产品体验的一部分。\r\n\r\n第二，不要什么都塞进主数据库。\r\n\r\
  \nMySQL 很重要，但它不需要负责所有事情。\r\n\r\n业务数据归业务数据库。\r\n\r\n全文搜索、模糊匹配、过滤聚合，可以交给搜索层。\r\n\r\n第三，小团队选型要看成本。\r\n\r\
  \n不是越成熟、越庞大的系统就越适合。\r\n\r\n如果一个小众工具刚好解决当前最痛的问题，并且资源占用低、接入成本低，那它可能就是更好的选择。\r\n\r\nSiteData 这次从 MySQL\
  \ 慢查询迁到 Manticore ，我最大的感受是：\r\n\r\n**技术优化最后还是要回到产品体验：原来不敢默认展示的数据，现在终于有机会变成用户每天都能用到的信号。**\r\n\r\n## 相关阅读\r\
  \n\r\n- [SiteData 新功能：在 Google 搜索页里直接查看关键词搜索量、趋势和广告竞争度]( https://mp.weixin.qq.com/s/Z5_dIYwMbDEJarJLpRLTlQ)\r\
  \n- [做 AFF 最怕选错方向：如何用 SiteData 找到被预算验证过的机会]( https://mp.weixin.qq.com/s/nxWxPd7c6dV0oL9IvfjS2g)\r\n\
  - [一个 API ，查遍对手的流量、外链和广告打法]( https://mp.weixin.qq.com/s/DqG6Otdqmz76BXzC0kgytg)\r\n\r\n![]( https://obsidian-img.prodbox.cc/images/2026/08/21/83aecc69-75de-49f4-8ac2-bc1a6f1e69c2.png)"
first_seen: '2026-08-28T07:30:03Z'
last_seen: '2026-08-29T03:43:06Z'
status: queued
sources:
- v2ex
sightings:
- source: v2ex
  url: https://obsidian-img.prodbox.cc/images/2026/08/27/a6940db7-99f2-473f-afa0-ac105dd5da53.png
  seen_at: '2026-08-29T03:43:06Z'
  metrics:
    comments: 0
  kind: product
---

# SiteData

![公众号封面图]( https://obsidian-img.prodbox.cc/images/2026/08/27/a6940db7-99f2-473f-afa0-ac105dd5da53.png)

> 发布摘要：SiteData 原来一次 Google Ads 标题模糊查询最快也要约 6 秒，我最后把搜索层换成 Manticore ，把查询压到约 0.6 秒，也让免费的 Ads 投放站点数从手动触发变成可以自然展示。

大家好，我是饭特稀。

最近给 SiteData 做了一次性能优化。

这次优化不是为了让页面看起来更快一点，而是为了解决一个非常具体的问题：

**千万级以上 Google Ads 标题和关键词数据，怎么做到可以实时模糊查询？**

其实之前这个功能已经有了。

比如你在 Google 搜索一个关键词，SiteData 插件会在搜索结果页里显示这个关键词最近 4 周大概有多少家网站在投放相关广告。

![Google 搜索页里的 SiteData Ads 网站数]( https://obsidian-img.prodbox.cc/images/2026/08/27/ba37e15e-8cbf-4983-b2e6-da7eb00d2090.png)

在插件里的热门关键词模块，也会显示每个关键词对应的 Ads 数量。

这里的数字不是搜索量，也不是 CPC 。

它更接近一个广告竞争信号：

**最近 4 周，有多少个网站围绕这个关键词投过 Google Ads 。**

![SiteData 插件热门关键词里的 Ads 数量]( https://obsidian-img.prodbox.cc/images/2026/08/27/56a22033-db66-4a88-8327-fe882eef1496.png)

还有一点需要说明：

**这个最近 4 周指定关键词投放站点的功能，目前是免费给用户看的。**

它也不是一个只能看一眼的静态数字。

用户可以直接点击这个数字，进入 SiteData 的 Google Ads Analysis 详情页，看最近 4 周有哪些网站在围绕这个关键词投放广告。

详情页里会列出相关站点、广告主、流量、DR ，以及进一步查看域名分析的入口。

比如下面这个关键词，最近 4 周匹配到了 59 个相关投放站点：

![点击 Ads 数字后查看关键词相关投放站点详情]( https://obsidian-img.prodbox.cc/images/2026/08/27/8ef23582-aa15-44f6-a22d-ca25122f7455.png)

这个信号对做 SEO 、AFF 、media buying 、网站增长的人很有用。

因为搜索量只能说明有人搜。

但有人持续投广告，说明另一个问题：

**这个关键词背后，可能已经有人愿意花真钱验证。**

当然，这不代表一定赚钱。

但它比单纯看搜索量更接近商业行为。

## 一开始为什么没有默认展示

这个功能之前没有默认打开。

原因也很简单：太慢。

SiteData 后面有大量 Google Ads 数据，其中广告 title 、description 、keyword 这类字段非常适合做模糊查询。

但问题是，数据量到千万级以后，传统 MySQL 直接查广告 title ，哪怕做了基础优化，一次查询最快也要 6 秒左右。

6 秒是什么概念？

如果只是后台手动查一次，可以忍。

如果是用户打开 Google 搜索页，每个关键词都要等这个结果，那就不行。

所以之前我只能做成手动触发：

用户真的想看这个广告信号时，再点一下按钮。

这不是我理想中的体验。

很多 SiteData 用户其实对这个数据有需求。

他们不是想多点一个按钮，而是希望在判断关键词、分析竞品、看广告机会时，这个信号默认就在旁边。

问题就变成了：

**能不能把一个原本只适合手动触发的慢查询，变成一个可以常态化展示的实时查询？**

## 继续压 MySQL ，不是最划算的路

一开始最自然的想法，肯定还是继续优化 MySQL 。

加索引、拆表、缓存、预计算，这些都可以做。

但这次的问题有点特殊。

我要查的不是一个精确字段，也不是简单的 `domain = xxx.com`。

更常见的是：

- title 里是否包含某个关键词
- 用户输入的关键词和广告标题是否接近
- 再叠加国家、语言、时间范围等过滤
- 最后还要统计最近 4 周有多少网站投过广告

这类查询，本质上已经不是 MySQL 最舒服的场景了。

MySQL 仍然适合做业务主数据库。

用户、订单、会员、广告主关系、任务状态，这些数据应该继续放在 MySQL 。

但广告 title 的全文搜索和模糊匹配，最好交给专门的搜索引擎。

所以我开始重新调研搜索方案。

常见选择当然是 Elasticsearch / OpenSearch 。

它们很成熟，生态也很强。

但对我这个阶段来说，ES 的问题也很明显：重。

JVM 、heap 、shard 、refresh 、集群运维，这一整套东西当然有价值，但如果只是为了把几千万条广告标题搜快一点，上来就用 ES ，多少有点提前交架构税。

后来我选了一个相对小众的开源搜索数据库：Manticore Search

![../../Pasted image 20260827180754.png]( https://obsidian-img.prodbox.cc/images/2026/08/27/e728ead5-75a8-4ba0-8ca1-1c91dd912d61.png?mFUguZ5mZc)

## 为什么最后选 Manticore

我选 Manticore ，不是因为它名气最大。

恰恰相反，它没有 Elasticsearch 那么出圈。

但它很适合 SiteData 当前这个场景。

SiteData 这里需要的是：

- 千万级以上广告标题全文搜索
- 模糊匹配
- 按国家、语言、时间过滤
- 按网站或广告主做统计聚合
- 服务器成本不能太夸张
- 开发接入最好不要太复杂

Manticore 的几个特点刚好对上了。

第一，它是 C++ 写的，资源占用比较克制。

第二，它支持 SQL 和 MySQL 协议。

这点对开发体验很重要。

你可以用类似这样的方式理解查询：

```sql
SELECT *
FROM google_ads
WHERE MATCH('ai image generator')
AND country = 'US'
ORDER BY last_seen DESC
LIMIT 100;
```

这比一上来写一大段 ES DSL 更直接。

第三，它适合做搜索层，而不是替代业务数据库。

我现在更倾向的架构是：

```text
MySQL
  负责用户、订单、会员、业务状态

Manticore
  负责 Google Ads title 、description 、keyword 的全文搜索、模糊查询、过滤和聚合
```

![MySQL 到 Manticore 搜索层架构示意]( https://obsidian-img.prodbox.cc/images/2026/08/27/5f3d0bad-3806-478f-a985-72ec604cc286.png)

也就是说，MySQL 仍然是业务事实来源。

Manticore 专心做一件事：把搜索变快。

## 上线后的结果

这次上线以后，最直观的变化是：

原来 MySQL 查一次最快约 6 秒。

现在一条广告标题模糊查询，大概 0.6 秒就能返回。

从用户体验上看，这个差别非常大。

6 秒的时候，我不敢默认展示。

0.6 秒的时候，这个功能就有机会从“手动点一下”变成“页面自然呈现”。

为了验证它不是偶然快，我还做了分阶段压测。

下面是压测结果：

![Manticore 查询接口分阶段压测结果]( https://obsidian-img.prodbox.cc/images/2026/08/27/4d35f3ee-3ae5-491f-a36c-6f3528bc18b3.jpg)

在这组测试里，从 1 RPS 到 50 RPS ，错误数都是 0 。

表里的平均耗时基本在 170ms 到 180ms 左右，P95 大多在 200ms 附近。

当然，压测数据不能简单等同于真实线上所有场景。

真实用户请求还会受到网络、接口包装、缓存命中、数据分布、并发形态等因素影响。

但这至少说明一件事：

**这个方向是对的。**

它不再是一个只能偶尔查一下的慢功能，而是有机会进入常规产品体验的功能。

## 更让我惊喜的是资源占用

速度变快，其实我有心理预期。

真正让我惊喜的是资源占用。

这是机器上的内存情况：

![服务器 free -m 内存占用截图]( https://obsidian-img.prodbox.cc/images/2026/08/27/f2393568-02ab-4bcd-98f3-03d5fee54bcf.png)

总内存 8GB 左右，实际 used 只有 662MB ，可用内存还有 7GB 多。

再看 htop：

![服务器 htop CPU 和负载截图]( https://obsidian-img.prodbox.cc/images/2026/08/27/f6052469-d957-4606-8ff4-98f0a9981e4b.png)

CPU 基本没有明显压力，load average 也很低。

磁盘情况也比我预期轻很多：

![服务器 df -h 磁盘占用截图]( https://obsidian-img.prodbox.cc/images/2026/08/27/344f6066-791f-4988-bd18-057f7d6c3651.png)

144G 的盘，只用了 6.3G 。

这点对独立开发者和小团队很重要。

很多时候，我们不是做不出功能。

真正的问题是：

功能一旦上线，服务器成本会不会跟着起飞？

如果一个功能必须上更大的机器、更多节点、更复杂的集群运维，那它不只是技术问题，还是商业问题。

这次 Manticore 给我的感觉是：

**在当前这个数据量和访问规模下，它把搜索性能和服务器成本控制在了一个很舒服的区间。**

## 这不是说 Manticore 一定比 ES 好

我不想把这篇写成“某某数据库吊打某某数据库”。

这种结论通常没什么意义。

Elasticsearch 仍然是非常成熟的搜索基础设施。

如果你的场景是超大规模集群、自动分片、强 HA 、复杂日志分析、成熟 ELK 生态，ES / OpenSearch 依然很有优势。

但 SiteData 这次的问题不是搭一个企业级搜索平台。

它的问题更具体：

千万级到亿级广告情报数据里，如何低成本、低运维压力地做全文搜索和模糊匹配？

在这个阶段，Manticore 更像一个务实选择。

不追求第一天就把架构搭得很重。

先让最痛的查询快起来。

等真的遇到单机瓶颈、手工分片瓶颈、更多节点的 HA 需求时，再重新评估 ES / OpenSearch 。

## 对 SiteData 来说，这个优化意味着什么

这次优化以后，SiteData 的关键词广告信号可以做得更自然。

以前用户看到一个关键词，想知道有没有人在投广告，需要额外触发。

现在更理想的体验是：

你在 Google 搜索一个词。

SiteData 顺手告诉你：

- 这个词最近 4 周,甚至 1 年以上有多少网站在投广告
- 这些广告主是否持续出现
- 相关网站是否还有其他关键词在投
- 这个关键词是短期测试，还是已经有持续预算

这对判断机会很关键。

因为做网站增长、做 SEO 、做 AFF ，最怕的不是没有数据。

最怕的是数据看起来很多，但离真实商业行为很远。

搜索量是兴趣。

CPC 是竞价结果。

广告投放网站数，是另一层真实行为。

它不能替你做决定，但能帮你少一点盲猜。

## 这次给我的几个提醒

第一，慢功能不一定是产品没价值。

有些功能不是没人要，而是性能没到可以自然使用的程度。

当一次查询要 6 秒时，用户会觉得它像一个附加工具。

当一次查询压到 0.6 秒时，它才有机会变成产品体验的一部分。

第二，不要什么都塞进主数据库。

MySQL 很重要，但它不需要负责所有事情。

业务数据归业务数据库。

全文搜索、模糊匹配、过滤聚合，可以交给搜索层。

第三，小团队选型要看成本。

不是越成熟、越庞大的系统就越适合。

如果一个小众工具刚好解决当前最痛的问题，并且资源占用低、接入成本低，那它可能就是更好的选择。

SiteData 这次从 MySQL 慢查询迁到 Manticore ，我最大的感受是：

**技术优化最后还是要回到产品体验：原来不敢默认展示的数据，现在终于有机会变成用户每天都能用到的信号。**

## 相关阅读

- [SiteData 新功能：在 Google 搜索页里直接查看关键词搜索量、趋势和广告竞争度]( https://mp.weixin.qq.com/s/Z5_dIYwMbDEJarJLpRLTlQ)
- [做 AFF 最怕选错方向：如何用 SiteData 找到被预算验证过的机会]( https://mp.weixin.qq.com/s/nxWxPd7c6dV0oL9IvfjS2g)
- [一个 API ，查遍对手的流量、外链和广告打法]( https://mp.weixin.qq.com/s/DqG6Otdqmz76BXzC0kgytg)

![]( https://obsidian-img.prodbox.cc/images/2026/08/21/83aecc69-75de-49f4-8ac2-bc1a6f1e69c2.png)

## 笔记


