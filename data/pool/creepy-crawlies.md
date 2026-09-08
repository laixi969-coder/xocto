---
slug: creepy-crawlies
name: Abusive AI crawler traffic
builder: ''
category: ''
summary_zh: 滥用型网络爬虫（主要为 AI 训练与抓取流量）已对大型网络基础设施构成结构性负担：Linux 内核官方 Git 仓库运营方披露，为爬虫渲染提交页面消耗的 CPU 资源已超过全部正常访问（包括
  git 克隆），需在 5 个地理分布节点上长期投入 14 个 CPU 核心。这一变化意味着内容与代码托管服务的运营成本显著上升，可能推动反爬措施、访问限制与付费墙政策在行业内进一步扩散。
inspiration: ''
summary_en: 'Abusive web crawlers, largely AI-driven scraping traffic, have become a structural burden
  on large-scale web infrastructure: the operators of the official Linux kernel Git repository report
  that CPU cycles spent rendering commits for scrapers now exceed all legitimate access including git
  clones, requiring 14 CPU cores across five geo-distributed nodes. The shift implies significantly higher
  operating costs for content and code hosting services and may accelerate anti-crawler measures, access
  restrictions, and paywall policies across the industry.'
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
url: https://simonwillison.net/2026/Sep/7/creepy-crawlies/
canonical_url: https://simonwillison.net/2026/Sep/7/creepy-crawlies
summary: "Creepy crawlies   \nKonstantin Ryabitsev discusses how bad the \"background radiation\" of abusive\
  \ crawlers has become from the perspective of  git.kernel.org , the official Git repository for the\
  \ Linux kernel: \n \n TL;DR: we spend more CPU cycles rendering commits for scrapers than we spend on\
  \ all other kinds of legitimate access, including git clones. At any one time, across 5 geo-distributed\
  \ nodes, there are 14 CPU cores doing nothing but rendering git commits as html. \n \n I worry about\
  \ this a lot from the perspective of Datasette, which serves a huge number of crawlable web pages.\n\
  \n       Via  Hacker News   \n\n\n     Tags:  crawling ,  git ,  linux ,  datasette ,  ai-ethics"
first_seen: '2026-09-07T23:08:58Z'
last_seen: '2026-09-08T00:25:50Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/7/creepy-crawlies/
  seen_at: '2026-09-08T00:25:50Z'
  metrics: {}
  kind: news
---

# Abusive AI crawler traffic

Creepy crawlies   
Konstantin Ryabitsev discusses how bad the "background radiation" of abusive crawlers has become from the perspective of  git.kernel.org , the official Git repository for the Linux kernel: 
 
 TL;DR: we spend more CPU cycles rendering commits for scrapers than we spend on all other kinds of legitimate access, including git clones. At any one time, across 5 geo-distributed nodes, there are 14 CPU cores doing nothing but rendering git commits as html. 
 
 I worry about this a lot from the perspective of Datasette, which serves a huge number of crawlable web pages.

       Via  Hacker News   


     Tags:  crawling ,  git ,  linux ,  datasette ,  ai-ethics

## 笔记


