---
slug: mabbs
name: Mabbs
builder: unmayx
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
url: https://mabbs.github.io/2026/11/01/compress.html
canonical_url: https://mabbs.github.io/2026/11/01/compress.html
summary: "最近把之前关于压缩的各种折腾整理成了一篇长文，发在博客上，想搬来论坛和大家聊聊。\r\n\r\n一开始只是想给博客离线包找更强的压缩算法：7-Zip 的 LZMA2 已经很能打，但我不信邪，又试了\
  \ ZPAQ 、PAQ8PX 、NNCP 、cmix 。结果挺有意思：\r\n\r\n- **ZPAQ**：一分钟左右把 16MiB 压到约 3.5MiB ，老算法但速度和压缩比还挺平衡；\r\n-\
  \ **PAQ8PX**：压到约 3.1MiB ，本次冠军，但花了一个半小时、吃了 30GiB 内存，解压同样痛苦；\r\n- **NNCP**：FFmpeg 作者 Fabrice Bellard 的\
  \ Transformer 压缩算法，RTX 4090 上跑了一个半小时，结果 4.1MiB ，还没 LZMA2 高；\r\n- **cmix**：测试时压到一半崩溃，内存和耗时也很夸张。\r\n\r\
  \n结论大概是：**追求极限压缩比，PAQ8PX 很强；日常使用，LZMA2 的 7-Zip 依然是最稳的选择；想在小文件上再挤一点，ZPAQ 可以试试。**\r\n\r\n更有意思的是后半篇：继续折腾“自包含压缩包\
  \ / Quine 压缩包”——也就是压缩包里包含一份和自身字节完全相同的副本。之前做过 7z Quine ，这次又让 AI 研究了：\r\n\r\n- **zstd Quine**：利用可跳过帧、RAW\
  \ block 和 XXH64 校验值构造，最终做成 `.tar.zst`，Windows 资源管理器也能直接打开；文章里附了完整生成代码；\r\n- **ZIP Quine**：利用成员数据重叠绕过窗口限制，7-Zip\
  \ 和 libarchive 能正常解压，但 Python `zipfile` 会因为检查压缩数据越过后续局部头而报错，算是一点兼容性代价；文章里也附了生成器；\r\n- **RAR Quine**：原理上也能做，AI\
  \ 也生成出来了，但因为 RAR 不是开源软件，文章里只放了生成后的样例供研究。\r\n\r\n文章里还有一段让我挺感慨的：这些代码我基本看不懂，但 AI 就是能把问题解决。复杂格式、校验值构造、兼容性坑，全都硬啃下来了。于是最后也忍不住写了点关于\
  \ AI 和“记录还有没有意义”的感想。\r\n\r\n原文在这里：[**《关于压缩的各种探索》**]( https://mabbs.github.io/2026/11/01/compress.html)\
  \  \r\n\r\n感兴趣的朋友可以聊聊：\r\n1. 你用过最离谱但确实有效的压缩算法是什么？\r\n2. 极限压缩比和可用性之间，你会怎么选？\r\n3. 对这种“压缩包包含自身”的 Quine\
  \ 玩法，有没有其他格式可以继续挑战？\r\n4. AI 生成这种复杂但能跑的代码，你觉得是解放生产力，还是让人越来越看不懂基础设施？\r\n\r\n欢迎拍砖、补充算法和格式，也欢迎试试文中的 zstd/ZIP\
  \ 生成器～"
first_seen: '2026-11-01T01:10:23Z'
last_seen: '2026-11-01T01:10:23Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: https://mabbs.github.io/2026/11/01/compress.html
  seen_at: '2026-11-01T01:10:23Z'
  metrics:
    comments: 4
  kind: product
---

# Mabbs

最近把之前关于压缩的各种折腾整理成了一篇长文，发在博客上，想搬来论坛和大家聊聊。

一开始只是想给博客离线包找更强的压缩算法：7-Zip 的 LZMA2 已经很能打，但我不信邪，又试了 ZPAQ 、PAQ8PX 、NNCP 、cmix 。结果挺有意思：

- **ZPAQ**：一分钟左右把 16MiB 压到约 3.5MiB ，老算法但速度和压缩比还挺平衡；
- **PAQ8PX**：压到约 3.1MiB ，本次冠军，但花了一个半小时、吃了 30GiB 内存，解压同样痛苦；
- **NNCP**：FFmpeg 作者 Fabrice Bellard 的 Transformer 压缩算法，RTX 4090 上跑了一个半小时，结果 4.1MiB ，还没 LZMA2 高；
- **cmix**：测试时压到一半崩溃，内存和耗时也很夸张。

结论大概是：**追求极限压缩比，PAQ8PX 很强；日常使用，LZMA2 的 7-Zip 依然是最稳的选择；想在小文件上再挤一点，ZPAQ 可以试试。**

更有意思的是后半篇：继续折腾“自包含压缩包 / Quine 压缩包”——也就是压缩包里包含一份和自身字节完全相同的副本。之前做过 7z Quine ，这次又让 AI 研究了：

- **zstd Quine**：利用可跳过帧、RAW block 和 XXH64 校验值构造，最终做成 `.tar.zst`，Windows 资源管理器也能直接打开；文章里附了完整生成代码；
- **ZIP Quine**：利用成员数据重叠绕过窗口限制，7-Zip 和 libarchive 能正常解压，但 Python `zipfile` 会因为检查压缩数据越过后续局部头而报错，算是一点兼容性代价；文章里也附了生成器；
- **RAR Quine**：原理上也能做，AI 也生成出来了，但因为 RAR 不是开源软件，文章里只放了生成后的样例供研究。

文章里还有一段让我挺感慨的：这些代码我基本看不懂，但 AI 就是能把问题解决。复杂格式、校验值构造、兼容性坑，全都硬啃下来了。于是最后也忍不住写了点关于 AI 和“记录还有没有意义”的感想。

原文在这里：[**《关于压缩的各种探索》**]( https://mabbs.github.io/2026/11/01/compress.html)  

感兴趣的朋友可以聊聊：
1. 你用过最离谱但确实有效的压缩算法是什么？
2. 极限压缩比和可用性之间，你会怎么选？
3. 对这种“压缩包包含自身”的 Quine 玩法，有没有其他格式可以继续挑战？
4. AI 生成这种复杂但能跑的代码，你觉得是解放生产力，还是让人越来越看不懂基础设施？

欢迎拍砖、补充算法和格式，也欢迎试试文中的 zstd/ZIP 生成器～

## 笔记


