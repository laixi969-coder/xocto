---
slug: deepgemm-ascend
name: DeepGEMM-Ascend
builder: deepseek-ai
category: 基础层
summary_zh: 在昇腾 NPU 上跑模型训练或推理的工程师，原本要自己写或调矩阵乘法算子来榨出算力；该库接收矩阵乘法计算需求，在昇腾硬件上执行高效算子，最终交付可被训练或推理框架调用的算子实现，具体支持矩阵形状、精度与性能数据仍待核验。
inspiration: 趋势是模型厂商把自家训练用到的算子层也搬到国产加速卡上，说明昇腾生态的软件缺口正被外部团队填补。切入可考虑面向使用昇腾的行业客户做算子级性能优化与精度对齐服务，按可核对的加速比交付。
summary_en: Engineers running model training or inference on Ascend NPUs previously had to write or tune
  matrix multiplication kernels to extract usable compute; this library takes matrix multiplication needs
  and executes efficient kernels on Ascend hardware, delivering kernel implementations callable by training
  or inference frameworks, though supported shapes, precision and performance figures still need verification.
inspiration_en: The trend is that model vendors are porting their own training kernels to domestic accelerators,
  showing that Ascend ecosystem software gaps are being filled by outside teams. An opening is kernel-level
  performance optimization and precision alignment services for Ascend users, delivered against verifiable
  speedup ratios.
priority_review: true
project_type: open_source
industries:
- 云计算与数据中心
- 半导体
- 人工智能基础设施
industries_en:
- Cloud computing and data centers
- Semiconductors
- AI infrastructure
jobs:
- AI 基础设施工程师
- 算子开发工程师
- 国产算力适配工程师
jobs_en:
- AI infrastructure engineer
- Kernel developer
- Domestic accelerator adaptation engineer
regions:
- 中国
regions_en:
- China
open_source: true
url: https://github.com/deepseek-ai/DeepGEMM-Ascend
canonical_url: https://github.com/deepseek-ai/DeepGEMM-Ascend
summary: 'DeepGEMM-Ascend: clean and efficient matrix multiplication kernel library for Huawei Ascend
  NPUs'
first_seen: '2026-09-29T15:49:55Z'
last_seen: '2026-10-02T01:41:55Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/deepseek-ai/DeepGEMM-Ascend
  seen_at: '2026-10-02T01:41:55Z'
  metrics:
    stars: 451
    forks: 33
    open_issues: 9
  kind: product
---

# DeepGEMM-Ascend

DeepGEMM-Ascend: clean and efficient matrix multiplication kernel library for Huawei Ascend NPUs

## 笔记


