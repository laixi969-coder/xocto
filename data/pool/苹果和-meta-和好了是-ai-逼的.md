---
slug: 苹果和-meta-和好了是-ai-逼的
name: Muse Spark Open
builder: ''
category: ''
summary_zh: 这是 Meta 发布的开放权重模型 Muse Spark Open，以及苹果随之调整 Mac 上 AI 读取数据提示规则的一次平台与模型侧变化，不是面向具体工作流的独立应用；对应用方的直接影响是本地可跑的大模型供给增加、系统级数据访问提示更明确，具体成本与交付影响仍待核验。
inspiration: ''
summary_en: This is Meta's open-weight model Muse Spark Open plus Apple's change to how Macs prompt users
  when AI reads data — a model-and-platform shift rather than a standalone application tied to a specific
  workflow; the direct effect on builders is more locally runnable model supply and clearer system-level
  data-access prompts, while concrete cost and delivery impact remains unverified.
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
url: http://www.geekpark.net/news/372458
canonical_url: https://geekpark.net/news/372458
summary: 没有永远的敌人，只有永远的 AI 焦虑。 10 月 2 日，苹果做了一件很少见的事，因为一个第三方 App，宣布要调整系统规则。 起因是《Inc.》杂志的科技专栏作者 Jason Aten
  公开指控，Meta 的 AI 智能体 Muse 在他的 Mac 上读取了私人消息。Muse 是 Meta 力推的「能替你办事」的 Agent，会帮你退订闲置会员，甚至替你砍价。 苹果随即表态， 今后
  AI 请求读取 Mac 数据时，系统会主动提示用户 。 这几乎就是苹果和 Meta 过去五年关系的缩影，Meta 想拿数据，苹果出面拦着。 然而仅仅两周后，故事发生了反转。 当地时间 10 月 15
  日，Meta 发布开放权重模型 Muse Spark Open，扎克伯格在 X 上发帖，感谢「John Ternus 和苹果」的合作，让这个模型能在新款 Mac Studio 上流畅运行。 苹果 CEO
  Ternus 本人很快回复，称能在自己桌上如此高效地跑起这种量级的模型： 「鹅妹子嘤」。 Meta 的 AI 负责人 Alexandr Wang 接受 Axios 采访时，说了一句更搞笑但直白的话：
  「 很高兴爸爸妈妈又和好了 。」 所以，「爸爸」和「妈妈」，是怎么和好的？以及，Meta 最近连续在模型上发力，终于重回牌桌了吗？ 01 一台桌子，放下 8000 亿参数 先看这次苹果和 Meta 的合作到底做成了什么。
  Meta 宣称 Muse Spark Open 总参数 8160 亿，每次推理只激活其中 420 亿，支持 100 万 token 的上下文。Meta 称它是： 「 迄今美国最强的开放权重模型 」。
  注意这个措辞里的「美国」两个字。论参数规模，它并不是全球最大的开源模型。 月之暗面的 Kimi K2、蚂蚁的 Ling-1T，早在 2025 年就把开源模型推到了万亿参数级别 。Meta 这次是在追赶，而且对手是中国公司。
  真正新鲜的，是它跑在哪里。 苹果的 M5 Ultra Mac Studio 绝对是本地模型利器｜图片来源：Apple 按 Meta 的说法， 两台顶配 M5 Ultra Mac Studio 就能装下整个模型
  。每台 Mac Studio 的 GPU 能直接调用最多 512GB 统一内存，两台连起来约 1TB，在 Apple 的 MLX 框架下像一台小型超算一样协同工作。 这件事放在别的 AI 硬件平台上，几乎不可能放在一张书桌上。
  道理不复杂。这类「总参数大、激活参数小」的模型，最需要的是超大的内存容量，对带宽的要求反倒没那么极端。每生成一个 token，模型只需要读取 420 亿参数那一小块，M5 Ultra 每秒 1.2TB
  的内存带宽足够应付。 换到 NVIDIA 阵营，一张消费级显卡的显存不过几十 GB，想装下 8000 亿参数，得上 8 卡 H100 级别的服务器，那是机房里的设备，不是桌面上的。 也就是说， 苹果统一内存架构这几年被嘲笑「贵」的那部分，恰好成了跑超大模型的护城河
  。 Meta 展示的用例也很有针对性。基于 Muse Spark Open 的编程工具 Muse Code，全程在本地完成了两件事。一件是给开源 Mastodon 客户端 Ice Cubes 提交 iOS
  代码修改，另一件是操作 DaVinci Resolve 审看素材，把横屏视频裁成竖屏。 写代码、剪视频，两个都是 Mac 用户最典型的工作场景。 当然，门槛也很现实。 256GB 内存版的 M5 Ultra
  Mac Studio 起售价已经是 10799 美元 ，512GB 版本预计本月晚些时候才上市，两台下来价格可想而知。这不是给普通消费者准备的，而是给开发者、工作室和对数据敏感的企业准备的。 02 「爸爸」「妈妈」怎么和好了？
  要理解苹果和 Meta 这次握手有多不寻常，得把时间往回拨。 2021 年，苹果在 iOS 14.5 推出「App
first_seen: '2026-10-17T00:31:00Z'
last_seen: '2026-10-17T00:31:00Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: http://www.geekpark.net/news/372458
  seen_at: '2026-10-17T00:31:00Z'
  metrics: {}
  kind: news
---

# Muse Spark Open

没有永远的敌人，只有永远的 AI 焦虑。 10 月 2 日，苹果做了一件很少见的事，因为一个第三方 App，宣布要调整系统规则。 起因是《Inc.》杂志的科技专栏作者 Jason Aten 公开指控，Meta 的 AI 智能体 Muse 在他的 Mac 上读取了私人消息。Muse 是 Meta 力推的「能替你办事」的 Agent，会帮你退订闲置会员，甚至替你砍价。 苹果随即表态， 今后 AI 请求读取 Mac 数据时，系统会主动提示用户 。 这几乎就是苹果和 Meta 过去五年关系的缩影，Meta 想拿数据，苹果出面拦着。 然而仅仅两周后，故事发生了反转。 当地时间 10 月 15 日，Meta 发布开放权重模型 Muse Spark Open，扎克伯格在 X 上发帖，感谢「John Ternus 和苹果」的合作，让这个模型能在新款 Mac Studio 上流畅运行。 苹果 CEO Ternus 本人很快回复，称能在自己桌上如此高效地跑起这种量级的模型： 「鹅妹子嘤」。 Meta 的 AI 负责人 Alexandr Wang 接受 Axios 采访时，说了一句更搞笑但直白的话： 「 很高兴爸爸妈妈又和好了 。」 所以，「爸爸」和「妈妈」，是怎么和好的？以及，Meta 最近连续在模型上发力，终于重回牌桌了吗？ 01 一台桌子，放下 8000 亿参数 先看这次苹果和 Meta 的合作到底做成了什么。 Meta 宣称 Muse Spark Open 总参数 8160 亿，每次推理只激活其中 420 亿，支持 100 万 token 的上下文。Meta 称它是： 「 迄今美国最强的开放权重模型 」。 注意这个措辞里的「美国」两个字。论参数规模，它并不是全球最大的开源模型。 月之暗面的 Kimi K2、蚂蚁的 Ling-1T，早在 2025 年就把开源模型推到了万亿参数级别 。Meta 这次是在追赶，而且对手是中国公司。 真正新鲜的，是它跑在哪里。 苹果的 M5 Ultra Mac Studio 绝对是本地模型利器｜图片来源：Apple 按 Meta 的说法， 两台顶配 M5 Ultra Mac Studio 就能装下整个模型 。每台 Mac Studio 的 GPU 能直接调用最多 512GB 统一内存，两台连起来约 1TB，在 Apple 的 MLX 框架下像一台小型超算一样协同工作。 这件事放在别的 AI 硬件平台上，几乎不可能放在一张书桌上。 道理不复杂。这类「总参数大、激活参数小」的模型，最需要的是超大的内存容量，对带宽的要求反倒没那么极端。每生成一个 token，模型只需要读取 420 亿参数那一小块，M5 Ultra 每秒 1.2TB 的内存带宽足够应付。 换到 NVIDIA 阵营，一张消费级显卡的显存不过几十 GB，想装下 8000 亿参数，得上 8 卡 H100 级别的服务器，那是机房里的设备，不是桌面上的。 也就是说， 苹果统一内存架构这几年被嘲笑「贵」的那部分，恰好成了跑超大模型的护城河 。 Meta 展示的用例也很有针对性。基于 Muse Spark Open 的编程工具 Muse Code，全程在本地完成了两件事。一件是给开源 Mastodon 客户端 Ice Cubes 提交 iOS 代码修改，另一件是操作 DaVinci Resolve 审看素材，把横屏视频裁成竖屏。 写代码、剪视频，两个都是 Mac 用户最典型的工作场景。 当然，门槛也很现实。 256GB 内存版的 M5 Ultra Mac Studio 起售价已经是 10799 美元 ，512GB 版本预计本月晚些时候才上市，两台下来价格可想而知。这不是给普通消费者准备的，而是给开发者、工作室和对数据敏感的企业准备的。 02 「爸爸」「妈妈」怎么和好了？ 要理解苹果和 Meta 这次握手有多不寻常，得把时间往回拨。 2021 年，苹果在 iOS 14.5 推出「App

## 笔记


