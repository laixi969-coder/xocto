---
slug: train-qwen3-on-aws-trainium-with-torchtitan
name: Train Qwen3 on AWS Trainium with torchtitan
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
url: https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan/
canonical_url: https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan
summary: Using torchtitan on AWS Trainium means using it the way you always have. TorchNeuron registers
  Trainium as a native PyTorch device, which lets torchtitan use it through standard PyTorch interfaces.
  You can use these configurations to pre-train from random initialization or fine-tune published weights.
  You can also customize the model implementation and kernels for your workload. In this post, you train
  Qwen3 three ways on a single trn2.48xlarge . The first method uses Transformers v5 as a modeling backend
  in torchtitan. It runs Hub models through AutoModelForCausalLM and reads and writes published safetensors
  directly. The second method switches to torchtitan’s native Qwen3 by changing config.model_spec . The
  third adds Neuron Kernel Interface (NKI) mixture-of-experts (MoE) kernels from the torchtitan-neuron
  recipes and then uses torchtitan’s override registry to attach your own kernel. All three configurations
  use the same torchrun launch pattern and config structure. Prerequisites To follow this walkthrough,
  use a single trn2.48xlarge with either the AWS Deep Learning AMI for Neuron or a Neuron PyTorch training
  container. Both environments provide the Neuron driver, runtime, and compiler required to train on Trainium.
  Before you install torchtitan-neuron , check whether your environment already includes it. The following
  command prints the installed version
first_seen: '2026-10-22T00:42:46Z'
last_seen: '2026-10-22T00:42:46Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan/
  seen_at: '2026-10-22T00:42:46Z'
  metrics: {}
  kind: news
---

# Train Qwen3 on AWS Trainium with torchtitan

Using torchtitan on AWS Trainium means using it the way you always have. TorchNeuron registers Trainium as a native PyTorch device, which lets torchtitan use it through standard PyTorch interfaces. You can use these configurations to pre-train from random initialization or fine-tune published weights. You can also customize the model implementation and kernels for your workload. In this post, you train Qwen3 three ways on a single trn2.48xlarge . The first method uses Transformers v5 as a modeling backend in torchtitan. It runs Hub models through AutoModelForCausalLM and reads and writes published safetensors directly. The second method switches to torchtitan’s native Qwen3 by changing config.model_spec . The third adds Neuron Kernel Interface (NKI) mixture-of-experts (MoE) kernels from the torchtitan-neuron recipes and then uses torchtitan’s override registry to attach your own kernel. All three configurations use the same torchrun launch pattern and config structure. Prerequisites To follow this walkthrough, use a single trn2.48xlarge with either the AWS Deep Learning AMI for Neuron or a Neuron PyTorch training container. Both environments provide the Neuron driver, runtime, and compiler required to train on Trainium. Before you install torchtitan-neuron , check whether your environment already includes it. The following command prints the installed version

## 笔记


