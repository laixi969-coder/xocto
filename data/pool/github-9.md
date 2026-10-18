---
slug: github-9
name: Github
builder: sunxfancy
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
url: https://github.com/EVEngine/EVEngine/pull/443
canonical_url: https://github.com/EVEngine/EVEngine/pull/443
summary: "最近用 AI 开发一个 AI native 的开源游戏引擎 EVEngine ，遇到了一个挺尴尬的问题：\r\n\r\nAI 写代码的速度，已经超过了我阅读代码的速度。\r\n\r\n\
  以前开发一个功能，可能需要花几天时间，天天都盼着有人能帮我写，发个 pr 给我。\r\n\r\n现在反过来了。\r\n\r\n我同时使用 Codex 、Cursor 、DeepSeek 等工具开发，几个\
  \ Agent 并行工作，一天下来就可能产生大量代码和 PR 。\r\n\r\n代码写得越来越快，但审查代码简直累死个人。\r\n\r\n尤其是游戏引擎这种项目，涉及底层架构、并发、内存管理、渲染等模块。很多问题不是看一眼\
  \ Diff 就能发现的。\r\n\r\n于是我开始尝试另一种方式：\r\n\r\n让 AI 写代码，再让其他 AI 来 Review 。\r\n\r\n目前我在 EVEngine 项目中尝试通过 Qodo\
  \ AI Review 和 CI 的一些约束判断来辅助审查 PR 。\r\n\r\n这里有一个真实的 PR ，大家可以直接看看：\r\n\r\nhttps://github.com/EVEngine/EVEngine/pull/443\r\
  \n\r\nAI 给出了 3 个 bug ，然后我的 agent ，还一一回复并修复了这三个 bug ，并重新提交。\r\n\r\n但越是这样做，我越觉得有一个问题绕不过去：\r\n\r\n如果我不放心\
  \ AI 写的代码，凭什么放心另一个 AI 审查的结果？\r\n\r\n两个 AI 都认为代码没问题，真的就意味着没问题吗？\r\n\r\n如果最终还是需要我把几千行代码全部读一遍，那么 AI 带来的开发速度提升，会不会被\
  \ Code Review 吃掉很大一部分？\r\n\r\n我现在逐渐倾向于另一种思路：\r\n\r\n未来程序员的工作，可能不再是逐行检查每一处实现，而是更多地审查架构、需求、测试覆盖以及最终行为。\r\
  \n\r\n但这也意味着，我们必须找到一种比“AI 说没问题”更可靠的验证方式。\r\n\r\n不知道大家现在是怎么处理 AI 生成的大量代码的？\r\n\r\n你们会放心让 AI Review AI\
  \ 吗？\r\n\r\n如果 AI Review 通过、CI 通过，你会直接 Merge 吗？还是一定要自己看完所有代码？\r\n\r\n----------------------------------\r\
  \n\r\n最后，顺手给我的项目打个广告，EVEngine （ https://github.com/EVEngine/EVEngine ）是从头设计的类 love2d 风格的 2d 、3d 混合渲染的开源游戏引擎，简单容易上手的同时，又提供各种高级光源阴影光追效果、程序化地形生成、各种\
  \ RTS 、RPG 、CardGame 等高层级玩法模块，还提供了大量的 mcp 服务功能帮助 AI 调试、理解代码行为。\r\n\r\nSSUI （ https://github.com/sunxfancy/SSUI\
  \ ）是我去年设计的一款开源的替代 ComfyUI 的 AI 生图、生视频、生 3D 、生动作的 AI 模型调用工具，基本功能实现了，但 bug 还比较多，最近在努力添加 AMD 显卡的支持。这两个项目连起来就是一整套\
  \ AI 辅助游戏开发的工具。\r\n\r\n喜欢的朋友请 star 一下多多支持。"
first_seen: '2026-10-18T00:03:42Z'
last_seen: '2026-10-18T00:03:42Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: https://github.com/EVEngine/EVEngine/pull/443
  seen_at: '2026-10-18T00:03:42Z'
  metrics:
    comments: 24
  kind: product
---

# Github

最近用 AI 开发一个 AI native 的开源游戏引擎 EVEngine ，遇到了一个挺尴尬的问题：

AI 写代码的速度，已经超过了我阅读代码的速度。

以前开发一个功能，可能需要花几天时间，天天都盼着有人能帮我写，发个 pr 给我。

现在反过来了。

我同时使用 Codex 、Cursor 、DeepSeek 等工具开发，几个 Agent 并行工作，一天下来就可能产生大量代码和 PR 。

代码写得越来越快，但审查代码简直累死个人。

尤其是游戏引擎这种项目，涉及底层架构、并发、内存管理、渲染等模块。很多问题不是看一眼 Diff 就能发现的。

于是我开始尝试另一种方式：

让 AI 写代码，再让其他 AI 来 Review 。

目前我在 EVEngine 项目中尝试通过 Qodo AI Review 和 CI 的一些约束判断来辅助审查 PR 。

这里有一个真实的 PR ，大家可以直接看看：

https://github.com/EVEngine/EVEngine/pull/443

AI 给出了 3 个 bug ，然后我的 agent ，还一一回复并修复了这三个 bug ，并重新提交。

但越是这样做，我越觉得有一个问题绕不过去：

如果我不放心 AI 写的代码，凭什么放心另一个 AI 审查的结果？

两个 AI 都认为代码没问题，真的就意味着没问题吗？

如果最终还是需要我把几千行代码全部读一遍，那么 AI 带来的开发速度提升，会不会被 Code Review 吃掉很大一部分？

我现在逐渐倾向于另一种思路：

未来程序员的工作，可能不再是逐行检查每一处实现，而是更多地审查架构、需求、测试覆盖以及最终行为。

但这也意味着，我们必须找到一种比“AI 说没问题”更可靠的验证方式。

不知道大家现在是怎么处理 AI 生成的大量代码的？

你们会放心让 AI Review AI 吗？

如果 AI Review 通过、CI 通过，你会直接 Merge 吗？还是一定要自己看完所有代码？

----------------------------------

最后，顺手给我的项目打个广告，EVEngine （ https://github.com/EVEngine/EVEngine ）是从头设计的类 love2d 风格的 2d 、3d 混合渲染的开源游戏引擎，简单容易上手的同时，又提供各种高级光源阴影光追效果、程序化地形生成、各种 RTS 、RPG 、CardGame 等高层级玩法模块，还提供了大量的 mcp 服务功能帮助 AI 调试、理解代码行为。

SSUI （ https://github.com/sunxfancy/SSUI ）是我去年设计的一款开源的替代 ComfyUI 的 AI 生图、生视频、生 3D 、生动作的 AI 模型调用工具，基本功能实现了，但 bug 还比较多，最近在努力添加 AMD 显卡的支持。这两个项目连起来就是一整套 AI 辅助游戏开发的工具。

喜欢的朋友请 star 一下多多支持。

## 笔记


