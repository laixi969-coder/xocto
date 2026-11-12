---
slug: detecting-and-recovering-from-silent-data-corruption-on-amaz
name: Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod
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
url: https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod/
canonical_url: https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod
summary: 'Silent data corruption (SDC) happens when hardware, such as a GPU, returns a wrong but plausible
  number and raises no error. In distributed training, the wrong number can flow into the gradients and
  weights of every replica. Loss can still look normal for hours, and by the time a team notices an unexplained
  divergence or a weaker model, the compute is spent. It happens at scale: during a 54-day period of Llama
  3 405B pre-training on up to 16K H100 GPUs, Meta attributed 6 of 419 unexpected job interruptions to
  silent data corruption, and those were only the cases that interrupted the job and were traced to SDC.
  Amazon SageMaker HyperPod already replaces nodes that report a fault: the health-monitoring agent watches
  for GPU errors, deep health checks stress-test nodes, and automatic node recovery swaps out bad hardware.
  SDC slips past all of these features, because the hardware never reports anything. Detection has to
  come from the training job itself. In this post, we add three checks to a PyTorch DistributedDataParallel
  (DDP) training loop to detect SDC. When a check fires, we map the suspect rank to its node, contain
  the corruption, and have SageMaker HyperPod replace the node. Each'
first_seen: '2026-11-12T03:00:02Z'
last_seen: '2026-11-12T03:00:02Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod/
  seen_at: '2026-11-12T03:00:02Z'
  metrics: {}
  kind: news
---

# Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod

Silent data corruption (SDC) happens when hardware, such as a GPU, returns a wrong but plausible number and raises no error. In distributed training, the wrong number can flow into the gradients and weights of every replica. Loss can still look normal for hours, and by the time a team notices an unexplained divergence or a weaker model, the compute is spent. It happens at scale: during a 54-day period of Llama 3 405B pre-training on up to 16K H100 GPUs, Meta attributed 6 of 419 unexpected job interruptions to silent data corruption, and those were only the cases that interrupted the job and were traced to SDC. Amazon SageMaker HyperPod already replaces nodes that report a fault: the health-monitoring agent watches for GPU errors, deep health checks stress-test nodes, and automatic node recovery swaps out bad hardware. SDC slips past all of these features, because the hardware never reports anything. Detection has to come from the training job itself. In this post, we add three checks to a PyTorch DistributedDataParallel (DDP) training loop to detect SDC. When a check fires, we map the suspect rank to its node, contain the corruption, and have SageMaker HyperPod replace the node. Each

## 笔记


