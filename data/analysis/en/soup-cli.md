---
slug: soup-cli
name: Soup CLI
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An LLM fine-tuning CLI that runs from one YAML and one command, built around
"layer streaming": the frozen base model lives in system RAM and only one decoder
layer streams into the GPU at a time — so an 8B model fine-tunes on a 4 GB laptop
GPU.

## Who built it

Independent developer Alpamys Makazhan (GitHub: MakazhanAlpamys/Soup), Apache-2.0.
His PyPI positioning: "training LLMs is still painful. Even experienced teams spend
30-50% of their time fighting infrastructure instead of improving models."

_Read: a developer tool built by someone who was first fed up with environment
setup. He pushed "saving VRAM" to a verifiable, exact number and designed a
verification protocol that requires streamed and resident runs to be bit-identical.
That signals a concern for correctness, not demo polish._

## What it actually does

- **Layer-streamed fine-tuning** → frozen model layers live in CPU RAM; one layer
  at a time streams into the GPU during compute, with double-buffered preloading,
  so peak VRAM drops from "the whole model" to "a single layer"; LoRA adapters
  stay resident on the GPU
- **NF4 quantization on top** → 4-bit normalfloat compresses the model and pushes
  VRAM lower
- **Preference training** → DPO / ORPO / SimPO / KTO all supported, reusing the
  same streamed base as the reference model instead of holding a full extra copy
  of the model in memory
- **One YAML for the whole run** → soup init picks a template (chat/code/medical/
  reasoning/vision/audio and more, 16 total), soup train runs it, with auto GPU
  detection, auto batch size, auto quantization
- **One command to deployment** → soup chat to test, soup push to HuggingFace,
  soup export to GGUF/ONNX/TensorRT/AWQ/GPTQ, plugging straight into
  Ollama/llama.cpp
- **Engineering extras** → VRAM pre-check, NVMe offload when RAM runs out, a "data
  flywheel" loop with canary deploy and auto-rollback, and unlearning training for
  GDPR right-to-be-forgotten

**Nine architectures**: Llama, Qwen, Mistral, Gemma, Phi, and more.

## What old behavior it replaces

Fine-tuning an 8B model used to need roughly 16 GB of VRAM in standard precision —
impossible on an ordinary 4 GB laptop. Three paths remained: rent cloud GPUs
(hourly billing, environment setup, queueing); buy a big-VRAM card (thousands of
dollars); or squeeze in with QLoRA, which only halves the requirement and still
won't fit 4 GB.

The second layer of pain was environment configuration: SSH into a GPU box, install
drivers, set up CUDA, tune parameters — experienced teams spend 30-50% of their
time there.

Soup replaces the "rent a cluster and configure the environment" threshold,
turning fine-tuning from "a server thing" into "one command on a laptop."
Layer streaming removes "4 GB VRAM" as the blocker; the YAML config removes
"environment setup" as a daily tax.

## Business model

**None.** Apache-2.0, no paid tier, no hosted service, no company entity disclosed.

_Read: a classic "build reputation on correctness" open-source path. At this stage
the author earns credibility and stars, not money. The predictable route is hosted
training or enterprise support later, but monetization in the free, open-source
ecosystem is not an easy road._

## Hard numbers

- ~430 GitHub stars (early Aug 2026), 83k cumulative PyPI downloads, 17,479 tests passing
- Core benchmark: Llama-3.1-8B-Instruct (NF4) on an RTX 3050 Laptop 4 GB at 119.6
  tok/s with 3.32 GB peak VRAM
- 8xH100 reproduction: median 113.00 tok/s at the same 3.32 GB peak, bit-exact vs
  the resident run
- v0.73.0 (Aug 5-9, 2026) fixed a silent wrong-gradient bug on NF4 layers above
  ~165 MiB
- Layer streaming is beta and ~1.43x slower than resident training; 1M training
  tokens take about 2.3 hours
- Show HN and a launch-site front page in the same week; one-person project

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author is the target user; making correctness verification the core selling point means he builds infrastructure seriously |
| Product insight | Caught the insight that peak VRAM is set by one layer, not the whole model — which redefines what a 4 GB card is for |
| Execution quality | Bit-exact verification protocol, versioned releases, large test suite — near professional-team engineering |
| Timing | Local fine-tuning demand is being lit by the "usable by everyone" narrative; this is exactly when the barrier drops from cluster to laptop |

## The call

**This is real progress on "dropping fine-tuning from rent-a-cluster to laptop,"
not a concept.**

The core insight is that the training VRAM bottleneck is the assumption "the model
must be resident in VRAM." Layer streaming removes that assumption: the base model
stays frozen in RAM, one layer streams into the GPU at a time, and the peak drops
from whole-model to single-layer. 119.6 tok/s on a 4 GB laptop with bit-identical
results to a resident run separates it from the "VRAM magic" class of projects: it
demonstrates you can save VRAM without losing quality.

**The transferable rule: make "bit-exactness" your verification protocol.** Every
release compares streamed and resident runs and requires identical logits — more
convincing than any "works great" claim, and it lets users train on a laptop and
reproduce on a cluster. For infrastructure tools, this builds trust better than a
feature list.

**To be honest: it does not make fine-tuning faster, it makes it reachable.**
Layer streaming is ~1.43x slower than resident, 1M tokens take about 2.3 hours,
and Windows numbers are worse — that is the physical price of trading time for
VRAM. It targets people who could not run at all before, not people who run fast
enough. The Unsloth relationship is clear too: Unsloth makes qualifying GPUs
faster; Soup makes non-qualifying GPUs work.

**Risks**: ① layer streaming is still beta — long contexts and larger batches can
still exceed VRAM, and the boundaries need real users to find them; ② fine-tuning
frameworks are fiercely competitive (Unsloth, LLaMA-Factory, and others are
mature), and "saves VRAM" alone may not hold users; ③ a single-maintainer
open-source project raises iteration-pace and long-term maintenance questions.

## What to watch next

① Whether stars pass 1,500 in three months and layer streaming graduates from
beta to stable — the project's live-or-dead signal
② Whether it enters mainstream framework comparisons (head-to-head with Unsloth /
LLaMA-Factory) — being benchmarked is being recognized
③ Whether CI/script workflows adopt it as the de facto automated fine-tuning
standard — YAML-driven and scriptable means it may find its first real home in
internal enterprise pipelines

## What you can take from it

**Product logic**: for "lower the barrier" tools, make correctness a verifiable
selling point — hard metrics like bit-exactness prove "saved resources without
saving worse," which beats any "30% better" claim with technical users. The
precondition is actually achieving it; the verification protocol is itself the
moat.

**Positioning language**: the PyPI line — "even experienced teams spend 30-50% of
their time fighting infrastructure" — quantifies the pain with a concrete
percentage, far stronger than "simplify setup."

**Pricing structure**: none. Not commercialized.

## Verdict

**Worth watching.** The technology holds — layer streaming has exact numbers and
bit-exact verification behind it, turning "fine-tune an 8B on a laptop" from a
slogan into a reproducible fact. But it does not make training faster, only
reachable; business model and long-term maintenance are open questions. It is
currently the most persuasive footnote in the "local fine-tuning for everyone"
narrative.
