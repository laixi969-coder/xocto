---
slug: media
name: Media
builder: chaxiu
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
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
url: https://media.munk.sh/blog/day-01/machines.jpg
canonical_url: https://media.munk.sh/blog/day-01/machines.jpg
summary: "今天 **Gemini-4-Argon** 正式发布了，实测它的长程规划和调度决策能力强得让人后背发凉。\r\n既然模型大脑已经到了这个水位，再拿它当「聊天框里的个人助理」就太浪费了。\r\
  \n\r\n我决定做一个为期 **7 天** 的公开实验：\r\n**给 Gemini 4 配齐一台 Mac 电脑、一个独立浏览器、一台专属手机，再配一群 DeepSeek 驱动的 AI 员工，让它替我运营一家软件公司。目标只有一个：7\
  \ 天内从零做出一款知名付费软件的替代品，并直接免费开源。**\r\n\r\n![电脑与手机设备实拍图]( https://media.munk.sh/blog/day-01/machines.jpg)\r\
  \n\r\n---\r\n\r\n## 一、1,000 美金预算：Gemini 当高管，DeepSeek 当员工\r\n\r\n跑多 Agent 最怕两件事：全用旗舰模型，两天烧穿预算；全用便宜模型，规划一团乱麻。\r\
  \n这次实验里，我用自己写的本地运行时（**Munk AI**），把 **$1,000 美金 Token** 拆成了高低两档：\r\n\r\n- **800 美金给 Gemini 4 （公司高管 /\
  \ 总架构师 / 主力研发）**\r\n  负责守住公司全局记忆、拆解产品需求、攻坚核心代码、制定验收标准，并在关键路口向我的手机发请示。\r\n- **200 美金给 DeepSeek （高频专项员工：实机自测\
  \ + 新媒体运营）**\r\n  - **跑实机自测**：桌面与手机 UI 验收要连续跑几十轮「看界面 → 点按钮 → 验状态」，非常吃上下文。底层把控件和 OCR 坐标算好后，交给 DeepSeek\
  \ 跑既快又省钱，测出 Bug 立刻打回给 Gemini 修；\r\n  - **跑全网运营**：负责生成小红书配图、用脚本与 FFmpeg 剪辑宣传视频、再控制浏览器去各平台发帖和评论区互动。\r\n\
  \r\n![Agent 设置页面截图]( https://media.munk.sh/blog/day-01/agents.png)\r\n\r\n---\r\n\r\n## 二、真手真脚：不止会写代码\r\
  \n\r\n光会写代码那叫 IDE 插件，不叫软件公司。我交给了这家 AI 公司三样物理工具：\r\n\r\n1. **直接操控 Mac 电脑（ Computer Use ）**：就算原生桌面软件没有\
  \ API ，它也能直接看懂屏幕界面、识别按钮并自己点按操作。\r\n2. **独立浏览器 + 专属实体手机**：浏览器用来查竞品、看文档、去各平台发帖回评论；桌边配给它的实体手机不仅能测 App ，后续连收手机验证码都能自己搞定。\r\
  \n3. **自测硬闸**：代码写完必须过编译和实机点按自测，不过不准合入主线。\r\n\r\n---\r\n\r\n## 三、7 天实验的死规矩\r\n\r\n1. **我不写一行代码，不手动发一条帖子**。\r\
  \n2. **我只负责「手机审批」+「填密码/付款辅助」**：关键节点我在手机上点「同意 / 驳回」；遇到首次平台登录或付款时，它呼叫我搭把手（密码绝不进 AI 上下文），登完它继续自己跑。\r\n\
  3. **第 7 天交卷**：不管最终完成度是 80% 还是 100%，**做出来的替代软件直接免费开源**，同时把背后这家 AI 公司的配置与 Munk AI 开放出来给大家体验。\r\n\r\n\
  ![飞书手机审批：Munk AI 机器人叫我完成 GitHub 登录]( https://media.munk.sh/blog/day-01/feishu.jpg)\r\n\r\n---\r\n\r\n\
  ## 四、Day 1 / 7：做什么产品，让 Gemini 4 自己调研、决定\r\n\r\n今天（ 10 月 14 日）是 **Day 1 / 7**。\r\n具体平替哪一款付费软件，我都没有直接定，而是交给了\
  \ Gemini 4 自己调研、决定。\r\n\r\n我今天给 Gemini 4 下达的第 1 个总目标是：**派员工用浏览器去全网调研目前收费贵、呼声高、但还没有公认开源替代品的软件，开一场内部圆桌评估，今晚之前把前\
  \ 3 个备选立项方案发到我手机上等我拍板。**\r\n\r\n大家平时有什么「明明功能简单、却非要收高价买断或订阅」的怨念软件？**欢迎在评论区提名！** 我会让 AI 员工去抓评论区的高赞提名一起纳入评估，明天\
  \ **Day 2** 正式揭晓最终选定的目标软件并开工写代码！"
first_seen: '2026-10-15T00:32:03Z'
last_seen: '2026-10-17T00:30:21Z'
status: pending_filter
sources:
- v2ex
- marketfeeds
sightings:
- source: v2ex
  url: https://media.munk.sh/blog/day-01/machines.jpg
  seen_at: '2026-10-15T00:32:03Z'
  metrics:
    comments: 39
  kind: product
- source: marketfeeds
  url: https://techcrunch.com/2026/10/14/gudea-leverages-ai-to-help-organizations-prevent-social-media-crises-before-they-erupt/
  seen_at: '2026-10-15T00:32:32Z'
  metrics: {}
  kind: news
- source: v2ex
  url: https://media.munk.sh/blog/day-02/round-table.png
  seen_at: '2026-10-16T00:25:11Z'
  metrics:
    comments: 5
  kind: product
- source: v2ex
  url: https://media.munk.sh/blog/day-03/company-setting.png
  seen_at: '2026-10-17T00:30:21Z'
  metrics:
    comments: 4
  kind: product
---

# Media

今天 **Gemini-4-Argon** 正式发布了，实测它的长程规划和调度决策能力强得让人后背发凉。
既然模型大脑已经到了这个水位，再拿它当「聊天框里的个人助理」就太浪费了。

我决定做一个为期 **7 天** 的公开实验：
**给 Gemini 4 配齐一台 Mac 电脑、一个独立浏览器、一台专属手机，再配一群 DeepSeek 驱动的 AI 员工，让它替我运营一家软件公司。目标只有一个：7 天内从零做出一款知名付费软件的替代品，并直接免费开源。**

![电脑与手机设备实拍图]( https://media.munk.sh/blog/day-01/machines.jpg)

---

## 一、1,000 美金预算：Gemini 当高管，DeepSeek 当员工

跑多 Agent 最怕两件事：全用旗舰模型，两天烧穿预算；全用便宜模型，规划一团乱麻。
这次实验里，我用自己写的本地运行时（**Munk AI**），把 **$1,000 美金 Token** 拆成了高低两档：

- **800 美金给 Gemini 4 （公司高管 / 总架构师 / 主力研发）**
  负责守住公司全局记忆、拆解产品需求、攻坚核心代码、制定验收标准，并在关键路口向我的手机发请示。
- **200 美金给 DeepSeek （高频专项员工：实机自测 + 新媒体运营）**
  - **跑实机自测**：桌面与手机 UI 验收要连续跑几十轮「看界面 → 点按钮 → 验状态」，非常吃上下文。底层把控件和 OCR 坐标算好后，交给 DeepSeek 跑既快又省钱，测出 Bug 立刻打回给 Gemini 修；
  - **跑全网运营**：负责生成小红书配图、用脚本与 FFmpeg 剪辑宣传视频、再控制浏览器去各平台发帖和评论区互动。

![Agent 设置页面截图]( https://media.munk.sh/blog/day-01/agents.png)

---

## 二、真手真脚：不止会写代码

光会写代码那叫 IDE 插件，不叫软件公司。我交给了这家 AI 公司三样物理工具：

1. **直接操控 Mac 电脑（ Computer Use ）**：就算原生桌面软件没有 API ，它也能直接看懂屏幕界面、识别按钮并自己点按操作。
2. **独立浏览器 + 专属实体手机**：浏览器用来查竞品、看文档、去各平台发帖回评论；桌边配给它的实体手机不仅能测 App ，后续连收手机验证码都能自己搞定。
3. **自测硬闸**：代码写完必须过编译和实机点按自测，不过不准合入主线。

---

## 三、7 天实验的死规矩

1. **我不写一行代码，不手动发一条帖子**。
2. **我只负责「手机审批」+「填密码/付款辅助」**：关键节点我在手机上点「同意 / 驳回」；遇到首次平台登录或付款时，它呼叫我搭把手（密码绝不进 AI 上下文），登完它继续自己跑。
3. **第 7 天交卷**：不管最终完成度是 80% 还是 100%，**做出来的替代软件直接免费开源**，同时把背后这家 AI 公司的配置与 Munk AI 开放出来给大家体验。

![飞书手机审批：Munk AI 机器人叫我完成 GitHub 登录]( https://media.munk.sh/blog/day-01/feishu.jpg)

---

## 四、Day 1 / 7：做什么产品，让 Gemini 4 自己调研、决定

今天（ 10 月 14 日）是 **Day 1 / 7**。
具体平替哪一款付费软件，我都没有直接定，而是交给了 Gemini 4 自己调研、决定。

我今天给 Gemini 4 下达的第 1 个总目标是：**派员工用浏览器去全网调研目前收费贵、呼声高、但还没有公认开源替代品的软件，开一场内部圆桌评估，今晚之前把前 3 个备选立项方案发到我手机上等我拍板。**

大家平时有什么「明明功能简单、却非要收高价买断或订阅」的怨念软件？**欢迎在评论区提名！** 我会让 AI 员工去抓评论区的高赞提名一起纳入评估，明天 **Day 2** 正式揭晓最终选定的目标软件并开工写代码！

## 笔记


