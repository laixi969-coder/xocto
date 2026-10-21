---
slug: beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-lin
name: 'Beyond the KV cache: Training and serving i14’s Laplace 3B linear attention model on AWS Trainium2
  with native PyTorch'
builder: ''
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
url: https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch/
canonical_url: https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch
summary: Most large language models (LLMs) use transformer architectures with softmax attention. During
  inference, their key-value (KV) cache grows with the conversation or document context. This can reduce
  concurrency, increase serving cost, and force agentic applications to discard useful history. i14 designed
  Laplace 3B as a linear attention alternative. Its recurrent state stays at 29.5 MB per sequence, independent
  of context length. Working with AWS, i14 used native PyTorch support through TorchNeuron Native to bring
  this custom architecture to AWS Trainium2 . This preserved its Gated Linear Attention (GLA) design and
  Muon optimizer. On one trn2.48xlarge instance, Laplace 3B trained at about 120,000 tokens per second.
  The model served 11,544 output tokens per second across 1,280 concurrent sequences. This post explains
  the model design, the changes i14 made for Trainium2, and the training and inference results. About
  i14 i14 is an AI research and technology company that develops model architectures, components, and
  runtimes. Its work draws on AI, computational cognitive science, and research into how biological systems
  learn over time. i14 applies these ideas to models that can retain long-range context without allowing
  serving state to grow with every token. Why linear attention models? Transformer softmax attention compares
  tokens across the
first_seen: '2026-10-21T00:38:23Z'
last_seen: '2026-10-21T00:38:23Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch/
  seen_at: '2026-10-21T00:38:23Z'
  metrics: {}
  kind: news
---

# Beyond the KV cache: Training and serving i14’s Laplace 3B linear attention model on AWS Trainium2 with native PyTorch

Most large language models (LLMs) use transformer architectures with softmax attention. During inference, their key-value (KV) cache grows with the conversation or document context. This can reduce concurrency, increase serving cost, and force agentic applications to discard useful history. i14 designed Laplace 3B as a linear attention alternative. Its recurrent state stays at 29.5 MB per sequence, independent of context length. Working with AWS, i14 used native PyTorch support through TorchNeuron Native to bring this custom architecture to AWS Trainium2 . This preserved its Gated Linear Attention (GLA) design and Muon optimizer. On one trn2.48xlarge instance, Laplace 3B trained at about 120,000 tokens per second. The model served 11,544 output tokens per second across 1,280 concurrent sequences. This post explains the model design, the changes i14 made for Trainium2, and the training and inference results. About i14 i14 is an AI research and technology company that develops model architectures, components, and runtimes. Its work draws on AI, computational cognitive science, and research into how biological systems learn over time. i14 applies these ideas to models that can retain long-range context without allowing serving state to grow with every token. Why linear attention models? Transformer softmax attention compares tokens across the

## 笔记


