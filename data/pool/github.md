---
slug: github
name: MWFL
builder: everettjf
category: AI + 开发
summary_zh: MWFL 是一个基于 C++20 的轻量级原生 Windows 开发框架，在 Win32 之上提供现代封装，保留原生控件和系统能力。开发者可用它构建 Windows 10 及以上系统的桌面应用，框架提供类型化事件、RAII
  资源管理和 DPI 感知布局，减少样板代码。仓库包含 62 个可编译示例，并已用于构建十六进制编辑器、Markdown 编辑器等真实工具。
inspiration: 趋势是 AI 辅助代码生成需要更规整的底层框架。切入点是面向 Windows 桌面开发者的轻量框架，可结合 AI 代码生成工具，提供更易读的代码结构。
summary_en: MWFL is a lightweight native Windows development framework based on C++20, providing modern
  wrappers over Win32 while retaining native controls and system capabilities. Developers can build desktop
  apps for Windows 10 and above, with typed events, RAII resource management, and DPI-aware layout, reducing
  boilerplate. The repo includes 62 compilable examples and has been used to build real tools like hex
  editor and Markdown editor.
inspiration_en: 'Trend: AI-assisted code generation needs more structured underlying frameworks. Entry:
  target Windows desktop developers with a lightweight framework that integrates with AI code generation
  tools for cleaner code.'
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- Windows 桌面开发者
jobs_en:
- Windows Desktop Developers
regions:
- 全球
regions_en:
- Global
open_source: true
url: https://github.com/mwfl/mwfl
canonical_url: https://github.com/mwfl/mwfl
summary: "大家好，最近做了一个原生 Windows 开发框架，叫做 **MWFL （ Modern Windows Foundation Layer ）**，想在这里简单分享一下它的来历。\r\n\
  \r\n我刚毕业时做的就是 Windows 桌面程序开发。当时用过 Qt 、MFC ，也用过 WTL 。\r\n\r\n如果追求轻量，比如需要把程序放进 U 盘或光盘里直接运行，尽量减少依赖并控制程序体积，当时我通常会选择\
  \ WTL ；如果不太在意依赖和安装包大小，则会考虑 MFC 或 Qt 。我也接触过 DuiLib 一类相对轻量的方案，但整体开发体验始终没有特别满意。\r\n\r\n后来十多年里，我的工作重心转到了移动端，基本没有再系统地做\
  \ Windows 桌面开发。直到最近，工作中又遇到了一些 Windows 开发需求。\r\n\r\n重新回头看这个领域，我发现当年的一些问题似乎还在：\r\n\r\n直接使用 Win32 API ，代码比较繁琐，需要处理大量窗口消息和样板代码；\
  \ MFC 、Qt 这样的方案相对完整，但有时又显得偏重； WTL 足够轻量，不过大量宏以及偏传统的编程方式，放在今天来看，代码的可读性和开发体验都还有改进空间。\r\n\r\n于是我开始思考：能不能利用\
  \ C++20 的一些现代语言特性，在 Win32 之上构建一个更现代、轻量而且容易理解的基础库？\r\n\r\n这个项目只面向 Windows ，不考虑跨平台。跨平台有它的价值，但也会带来更多抽象层和复杂度。对我的需求来说，既然目标就是\
  \ Windows 10 及以上系统，那保留 Windows 的原生控件、原生行为和系统集成能力，更直接。\r\n\r\n最近我和 Codex 反复讨论和迭代，逐渐把这个想法做成了现在的 MWFL 。\r\
  \n\r\n```\r\n#include <mwfl/mwfl.h>\r\n\r\nusing mwfl::operator\"\"_dip;\r\n\r\nclass MainWindow final\
  \ : public mwfl::WindowBase {\r\npublic:\r\n    void BuildUI() override {\r\n        SetTitle(L\"Hello,\
  \ mwfl\");\r\n\r\n        mwfl::ControlHost ui{*this};\r\n        ui.Add(message_, L\"Native UI, modern\
  \ C++20.\");\r\n        ui.Add(close_, L\"Close\");\r\n\r\n        SetLayout(mwfl::Column()\r\n    \
  \        .Margin(24_dip).Gap(12_dip)\r\n            .Add(message_, mwfl::Auto())\r\n            .Add(close_,\
  \ mwfl::Fixed(36_dip)));\r\n    }\r\n\r\nprivate:\r\n    mwfl::Label message_;\r\n    mwfl::Button close_;\r\
  \n};\r\n```\r\n\r\nMWFL 没有重新绘制一套 UI 。窗口和控件仍然是真实的 HWND ，底层的消息、句柄、样式和返回值也都可以直接访问。它主要使用 C++20 提供一些更现代的封装，例如类型化事件、RAII\
  \ 资源管理、DPI 感知布局和更明确的对象所有权，同时尽量减少传统 Win32 、MFC 和 WTL 开发中常见的宏与样板代码。\r\n\r\n\r\n项目现在是第一个公开版本 v0.1.0 ，使用\
  \ MIT 协议，面向 Windows 10 及以上系统，支持 x64 和 ARM64 。仓库中有 62 个可以编译运行的示例。我也用它做了几个真实的小工具，包括十六进制编辑器、Markdown 编辑器、SQLite\
  \ 查看器、PDF 阅读器、文件夹比较工具和启动项管理器等。\r\n\r\n如果你需要：\r\n\r\n- 只开发 Windows 桌面应用；\r\n- 最低兼容 Windows 10 ；\r\n-\
  \ 希望使用 C++20 ；\r\n- 想保留原生 Win32 控件和系统能力；\r\n- 或者希望让 AI 生成的 Windows 代码更规整、更容易阅读；\r\n\r\n可以看看这个项目。\r\n\
  \r\n项目地址：\r\n\r\nhttps://github.com/mwfl/mwfl\r\n\r\n文档：\r\n\r\nhttps://mwfl.github.io/\r\n\r\n业余 AI\
  \ 项目，欢迎尽情交流。"
first_seen: '2026-08-23T06:15:09Z'
last_seen: '2026-08-29T03:43:11Z'
status: queued
sources:
- v2ex
- github
sightings:
- source: v2ex
  url: https://github.com/mwfl/mwfl
  seen_at: '2026-08-23T14:45:38Z'
  metrics:
    comments: 3
  kind: product
- source: v2ex
  url: https://github.com/aipayim/codex-proxy
  seen_at: '2026-08-23T22:38:22Z'
  metrics:
    comments: 0
  kind: product
- source: v2ex
  url: https://github.com/seekskyworld/CreatPPT
  seen_at: '2026-08-27T03:18:32Z'
  metrics:
    comments: 1
  kind: product
- source: v2ex
  url: https://github.com/gOODiDEA2002/lighttrans
  seen_at: '2026-08-29T03:43:06Z'
  metrics:
    comments: 0
  kind: product
- source: github
  url: https://github.com/cohere-ai/cohere-python/releases/tag/7.1.0
  seen_at: '2026-08-29T03:43:11Z'
  metrics:
    reactions: 0
  kind: news
---

# MWFL

大家好，最近做了一个原生 Windows 开发框架，叫做 **MWFL （ Modern Windows Foundation Layer ）**，想在这里简单分享一下它的来历。

我刚毕业时做的就是 Windows 桌面程序开发。当时用过 Qt 、MFC ，也用过 WTL 。

如果追求轻量，比如需要把程序放进 U 盘或光盘里直接运行，尽量减少依赖并控制程序体积，当时我通常会选择 WTL ；如果不太在意依赖和安装包大小，则会考虑 MFC 或 Qt 。我也接触过 DuiLib 一类相对轻量的方案，但整体开发体验始终没有特别满意。

后来十多年里，我的工作重心转到了移动端，基本没有再系统地做 Windows 桌面开发。直到最近，工作中又遇到了一些 Windows 开发需求。

重新回头看这个领域，我发现当年的一些问题似乎还在：

直接使用 Win32 API ，代码比较繁琐，需要处理大量窗口消息和样板代码； MFC 、Qt 这样的方案相对完整，但有时又显得偏重； WTL 足够轻量，不过大量宏以及偏传统的编程方式，放在今天来看，代码的可读性和开发体验都还有改进空间。

于是我开始思考：能不能利用 C++20 的一些现代语言特性，在 Win32 之上构建一个更现代、轻量而且容易理解的基础库？

这个项目只面向 Windows ，不考虑跨平台。跨平台有它的价值，但也会带来更多抽象层和复杂度。对我的需求来说，既然目标就是 Windows 10 及以上系统，那保留 Windows 的原生控件、原生行为和系统集成能力，更直接。

最近我和 Codex 反复讨论和迭代，逐渐把这个想法做成了现在的 MWFL 。

```
#include <mwfl/mwfl.h>

using mwfl::operator""_dip;

class MainWindow final : public mwfl::WindowBase {
public:
    void BuildUI() override {
        SetTitle(L"Hello, mwfl");

        mwfl::ControlHost ui{*this};
        ui.Add(message_, L"Native UI, modern C++20.");
        ui.Add(close_, L"Close");

        SetLayout(mwfl::Column()
            .Margin(24_dip).Gap(12_dip)
            .Add(message_, mwfl::Auto())
            .Add(close_, mwfl::Fixed(36_dip)));
    }

private:
    mwfl::Label message_;
    mwfl::Button close_;
};
```

MWFL 没有重新绘制一套 UI 。窗口和控件仍然是真实的 HWND ，底层的消息、句柄、样式和返回值也都可以直接访问。它主要使用 C++20 提供一些更现代的封装，例如类型化事件、RAII 资源管理、DPI 感知布局和更明确的对象所有权，同时尽量减少传统 Win32 、MFC 和 WTL 开发中常见的宏与样板代码。


项目现在是第一个公开版本 v0.1.0 ，使用 MIT 协议，面向 Windows 10 及以上系统，支持 x64 和 ARM64 。仓库中有 62 个可以编译运行的示例。我也用它做了几个真实的小工具，包括十六进制编辑器、Markdown 编辑器、SQLite 查看器、PDF 阅读器、文件夹比较工具和启动项管理器等。

如果你需要：

- 只开发 Windows 桌面应用；
- 最低兼容 Windows 10 ；
- 希望使用 C++20 ；
- 想保留原生 Win32 控件和系统能力；
- 或者希望让 AI 生成的 Windows 代码更规整、更容易阅读；

可以看看这个项目。

项目地址：

https://github.com/mwfl/mwfl

文档：

https://mwfl.github.io/

业余 AI 项目，欢迎尽情交流。

## 笔记


