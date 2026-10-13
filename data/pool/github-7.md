---
slug: github-7
name: Magpie
builder: zisen
category: 基础层
summary_zh: 开发者在自己项目里需要把不同模型或协议接到同一个入口时，打开 Magpie 这个开源 AI 网关，由它承担协议转换与翻译层，用户再按自己的需求写插件补上缺失功能，最终拿到一个可自托管的统一调用入口；插件具体形态与交付边界仍待核验。
inspiration: 趋势是开源底座加用户自写插件，把过去等作者排期的功能改成用户自己补；切入可看中小团队自建模型入口时的协议适配与插件托管，卖法未披露，不宜照搬。
summary_en: When developers need to route different models or protocols through one entry point, they
  open the open-source Magpie gateway, which handles protocol conversion and the translation layer while
  users write plugins for missing features, ending with a self-hostable unified endpoint; the exact plugin
  form and delivery boundary still need verification.
inspiration_en: The trend is an open-source base plus user-written plugins, replacing waiting on maintainers
  with users filling gaps themselves; the opening is protocol adaptation and plugin hosting for small
  teams building their own model entry point, with pricing undisclosed.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- AI 应用开发者搭建多模型调用网关
- 开发者为自己使用的网关编写自定义插件
jobs_en:
- AI application developers setting up a multi-model gateway
- Developers writing custom plugins for their own gateway
regions: []
regions_en: []
open_source: true
url: https://github.com/yetone/magpie
canonical_url: https://github.com/yetone/magpie
summary: "最近 x 上刷到一个很火的 ai 网关，叫 magpie ，短短几天就干到 10k stars ，而且我相信它未来会超过 CPA 和 sub2api 之类的 https://github.com/yetone/magpie\r\
  \n\r\n这个网关和 CPA 还有 sub2api 不同的是，它支持自定义插件，也就是说用户可以让自己的 agent 根据自己的需要，开发各种插件，一是减少了作者维护 repo 的压力，二是用户不需要等作者维护，就可以自己开发想要的功能，而\
  \ ai 网关比较难实现的部分，例如不同协议的转换，翻译层的设计，则由作者来维护。\r\n\r\n感觉这种插件式的软件会越来越受欢迎，这不是因为插件的可复用性，而是插件的易开发性，像之前比较火的 chrome\
  \ 插件，obsidian 插件，都依赖插件作者的维护，而如今软件的插件可以被用户自己来开发和维护。\r\n\r\n因此未来的软件基本上都是一个坚实的底座，由开源作者或者社区维护，然后一份插件开发文档，插件开发文档和软件是一并发布的，并且会占据比较显眼的位置，告诉用户他们可以自己实现想要的功能而不是等作者来加，外加用户自己的\
  \ agent ，用户只需要说自己的需求，agent 开发对应功能的插件\r\n\r\ndsh 也是一切皆插件的概念，但是在 harness 上面实现地并不是那么好，甚至当前 ds 官方自己都给不出一个自进化的演示，我感觉主要是\
  \ dsh 自己的底座并不扎实，甚至不能自己给自己开发插件，因为插件改坏了会崩掉导致起不来，必须依赖另一个 agent 来帮助写插件，另外就是插件的开发文档不完善，基本上都是看源码来写新插件。"
first_seen: '2026-10-13T03:03:52Z'
last_seen: '2026-10-13T03:03:52Z'
status: watching
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/yetone/magpie
  seen_at: '2026-10-13T03:03:52Z'
  metrics:
    comments: 14
  kind: product
---

# Magpie

最近 x 上刷到一个很火的 ai 网关，叫 magpie ，短短几天就干到 10k stars ，而且我相信它未来会超过 CPA 和 sub2api 之类的 https://github.com/yetone/magpie

这个网关和 CPA 还有 sub2api 不同的是，它支持自定义插件，也就是说用户可以让自己的 agent 根据自己的需要，开发各种插件，一是减少了作者维护 repo 的压力，二是用户不需要等作者维护，就可以自己开发想要的功能，而 ai 网关比较难实现的部分，例如不同协议的转换，翻译层的设计，则由作者来维护。

感觉这种插件式的软件会越来越受欢迎，这不是因为插件的可复用性，而是插件的易开发性，像之前比较火的 chrome 插件，obsidian 插件，都依赖插件作者的维护，而如今软件的插件可以被用户自己来开发和维护。

因此未来的软件基本上都是一个坚实的底座，由开源作者或者社区维护，然后一份插件开发文档，插件开发文档和软件是一并发布的，并且会占据比较显眼的位置，告诉用户他们可以自己实现想要的功能而不是等作者来加，外加用户自己的 agent ，用户只需要说自己的需求，agent 开发对应功能的插件

dsh 也是一切皆插件的概念，但是在 harness 上面实现地并不是那么好，甚至当前 ds 官方自己都给不出一个自进化的演示，我感觉主要是 dsh 自己的底座并不扎实，甚至不能自己给自己开发插件，因为插件改坏了会崩掉导致起不来，必须依赖另一个 agent 来帮助写插件，另外就是插件的开发文档不完善，基本上都是看源码来写新插件。

## 笔记


