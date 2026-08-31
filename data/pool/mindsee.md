---
slug: mindsee
name: Mindsee
builder: cdx
category: AI + 创作
summary_zh: 用户注册后获得生图次数，在 Mindsee 输入提示词生成图片；交付的是 AI 生成的图像，具体生成流程和输出规格仍待核验。
inspiration: 趋势是 AI 生图工具从通用走向垂直。可从电商产品图、营销素材等具体场景切入，按生成次数或订阅收费，但需先验证生成质量和用户留存。
summary_en: After registration, users receive generation credits and input prompts into Mindsee to generate
  images; the deliverable is an AI-generated image, though the specific generation process and output
  specifications remain to be verified.
inspiration_en: The trend is AI image generation moving from general to vertical. One could enter through
  specific scenarios like e-commerce product images or marketing assets, charging per generation or via
  subscription, but generation quality and user retention must first be validated.
priority_review: false
project_type: new_application
industries:
- 设计
- 营销
industries_en:
- Design
- Marketing
jobs:
- 平面设计师
- 内容创作者
jobs_en:
- Graphic Designer
- Content Creator
regions:
- 中国
regions_en:
- China
open_source: false
url: https://mindsee.app
canonical_url: https://mindsee.app
summary: "# 起因\r\n我在周六也就是 8 月 29 号下午 2 点左右发布了我的生图网站 https://mindsee.app\r\n然后在下午 4-5 点左右，有大量请求并发调用我的注册接口，并发非常高，万幸没有造成任何损失\r\
  \n\r\n![SCR-20260831-mcll.png]( https://ime-store-cdn.gtimg.com/pc/uploadImage/2026/08/31/1788165865c7139772_former.png)\r\
  \n![ca3ddee0f128e63e0be116b0d7e7cea6.png]( https://ime-store-cdn.gtimg.com/pc/uploadImage/2026/08/31/178816602091fc60c9_former.png)\r\
  \n\r\n# 时间线\r\n - 下午 2 点：\r\n   上线网站\r\n - 下午 3 点：\r\n   开始陆陆续续开始报警，查看是支付回调接口被请求，`接口签名校验未通过`，最开始以为是有用户支付了，一查毛都没有，此时没继续关注，继续忙其他的\r\
  \n - 下午 4 点：\r\n   发现注册接口频繁报 400 错误，检查后发现是被 156.248.15.37 这个 ip 一直在请求，给他 ban 后，给接口增加限流后，暂时停止攻击\r\n -\
  \ 下午 5 点：\r\n   发现注册接口还是频繁报 400 错误，不过限流后没有那么严重了，检查后发现是有多个 ip 并发在请求接口，将这几个 ip 都 ban 掉后，至今不在出现攻击\r\n#\
  \ 复盘\r\n这波攻击的人应该是同一人，并且是新手，可能还是使用 ai 来做的\r\n4 点的一波攻击，请求的 user-agent 是空的，猜测是用的 shell 脚本干的\r\n5 点的 user-agent\
  \ 是 go 语言的 http 客户端请求的。\r\n\r\n事情其实不算严重，甚至没有影响到我的其他服务，不过挺有意思的\r\n只不过没有想明白这是在干嘛，因为都是一直使用的同一个邮箱来注册，并且注册还需要验证码，验证码接口做了限流的，有了解在做什么的望告知一下\r\
  \n\r\n一直都相信互联网上一定有无缘无故的恶，所以我部署的服务一开始就使用了 cloudflare tunnels + worker 穿透出来的，没想到 cloudfalre 的免费层没有给非 GET\
  \ 请求做安全拦截，还要自己加，百密一疏啊，现在也在持续增加更多的保护措施\r\n\r\n# 结尾\r\n欢迎大家使用生图网站 [https://mindsee.app]( https://mindsee.app)，目前注册就送\
  \ 3 次生图机会，还可以使用兑换码兑换更多使用次数  \r\n在上个帖询问方向后，目前打算往垂直领域的工具深入，主要目标应该是 B 端用户，和部分 C 端用户"
first_seen: '2026-08-31T09:00:24Z'
last_seen: '2026-08-31T17:38:24Z'
status: watching
sources:
- v2ex
sightings:
- source: v2ex
  url: https://mindsee.app
  seen_at: '2026-08-31T17:38:24Z'
  metrics:
    comments: 4
  kind: product
---

# Mindsee

# 起因
我在周六也就是 8 月 29 号下午 2 点左右发布了我的生图网站 https://mindsee.app
然后在下午 4-5 点左右，有大量请求并发调用我的注册接口，并发非常高，万幸没有造成任何损失

![SCR-20260831-mcll.png]( https://ime-store-cdn.gtimg.com/pc/uploadImage/2026/08/31/1788165865c7139772_former.png)
![ca3ddee0f128e63e0be116b0d7e7cea6.png]( https://ime-store-cdn.gtimg.com/pc/uploadImage/2026/08/31/178816602091fc60c9_former.png)

# 时间线
 - 下午 2 点：
   上线网站
 - 下午 3 点：
   开始陆陆续续开始报警，查看是支付回调接口被请求，`接口签名校验未通过`，最开始以为是有用户支付了，一查毛都没有，此时没继续关注，继续忙其他的
 - 下午 4 点：
   发现注册接口频繁报 400 错误，检查后发现是被 156.248.15.37 这个 ip 一直在请求，给他 ban 后，给接口增加限流后，暂时停止攻击
 - 下午 5 点：
   发现注册接口还是频繁报 400 错误，不过限流后没有那么严重了，检查后发现是有多个 ip 并发在请求接口，将这几个 ip 都 ban 掉后，至今不在出现攻击
# 复盘
这波攻击的人应该是同一人，并且是新手，可能还是使用 ai 来做的
4 点的一波攻击，请求的 user-agent 是空的，猜测是用的 shell 脚本干的
5 点的 user-agent 是 go 语言的 http 客户端请求的。

事情其实不算严重，甚至没有影响到我的其他服务，不过挺有意思的
只不过没有想明白这是在干嘛，因为都是一直使用的同一个邮箱来注册，并且注册还需要验证码，验证码接口做了限流的，有了解在做什么的望告知一下

一直都相信互联网上一定有无缘无故的恶，所以我部署的服务一开始就使用了 cloudflare tunnels + worker 穿透出来的，没想到 cloudfalre 的免费层没有给非 GET 请求做安全拦截，还要自己加，百密一疏啊，现在也在持续增加更多的保护措施

# 结尾
欢迎大家使用生图网站 [https://mindsee.app]( https://mindsee.app)，目前注册就送 3 次生图机会，还可以使用兑换码兑换更多使用次数  
在上个帖询问方向后，目前打算往垂直领域的工具深入，主要目标应该是 B 端用户，和部分 C 端用户

## 笔记


