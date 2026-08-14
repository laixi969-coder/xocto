---
slug: needle2
name: Needle2
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A 14MB, 45M-parameter agentic LLM that does tool calling inside 28MB of RAM on phones,
wearables, smart-home devices, and robots — moving "understand a sentence, call a
device function" from the cloud onto the device.

## Who built it

Cactus Compute (cactuscompute.com, "Cactus"), an on-device AI company with three
product lines: Needle (tiny agentic model), Engine (edge inference runtime), and
Hybrid (post-trained edge-cloud cooperation). Needle 2 is the open-sourced model.

It carries a heavyweight endorsement: Pebble founder Eric Migicovsky testifies that
Pebble uses Needle in its Index 01 app for local voice-command processing.

_Read: Pebble adoption is the strongest signal available in the small-model space —
hardware constraints on power, memory, and response time are harsher than any
benchmark. But note the model is open source; the company monetizes through Engine
and Hybrid. The model is the customer-acquisition entry point._

## What it actually does

- **Device use / function calling** → device capabilities are modeled as functions
  with typed parameters; the model maps a natural-language sentence to the right
  function and arguments ("turn on the light" → `setLight(on=true)`). 45M parameters
  suffice
- **Structured extraction** → treated as a tool call: given a schema and a document,
  return typed fields; a grammar compiler derives syntax rules from the schema, making
  invalid JSON structurally impossible
- **Edge-cloud fallback** → every response carries a learned confidence score: above
  threshold, execute locally; below, ask again or escalate to cloud; irrelevant
  requests return an empty call instead of guessing
- **Native 2-bit training** → CQ2-bit quantization runs from pre-training through
  post-training, so the deployed 2-bit model is the trained model — sidestepping the
  classic "small model collapses under post-hoc quantization" problem
- **Deterministic memory** → a 256-token sliding window caps the KV cache, so session
  RAM is a fixed 28MB regardless of conversation length; tool declarations are
  permanent "sinks" that structurally cannot be evicted

**Technical base**: a Simple Attention Network (Hadamard MLP + engram hash memory +
multi-channel residual stream, 27 layers × 512 wide); single decode reads at most a
14MB blob; grammar-aware decoding skips up to 98% of vocabulary projection;
~7–85x less compute per token than comparable models. Pre-trained on 115B tokens,
post-trained on 38B tokens of compact reasoning traces.

## What old behavior it replaces

Device-side voice assistants and intent recognition previously had two expensive paths:

**Calling a cloud LLM API.** Latency, privacy, and offline failure — and running a
hundred-billion-parameter model for a task like "turn on a light" is absurd resource
allocation. It was done anyway because there was no alternative.

**Running an LLM on the device.** General small models (LFM2.5 230M, FunctionGemma
270M, Apple FM ~3B) either blew the memory budget, the power budget, or the speed
budget. Needle matches or beats them with 45M parameters and 14MB, turning "agentic
model on a tiny device" from impossible into possible.

**The core action it replaces**: a cloud call that costs money, needs a network, and
waits hundreds of milliseconds becomes a local function call that is free, offline,
and tens of milliseconds.

## Business model

**Model open and free** ("the default path remains private, fast, and free"). The
company monetizes Engine (inference runtime) and Hybrid (edge-cloud). Specific
pricing not disclosed.

_Read: the classic "open-source model acquires, platform charges" play — the model
proves capability, the platform earns on deployment and cooperation. The risk: an
open model has no moat; anyone can fine-tune a similar 14MB model, and the
acquisition window is finite._

## Hard numbers

- **HN 509 points / 171 comments** (Show HN, 2026-08-12) — high same-day attention
- **45M params / 14MB single binary / 28MB peak session RAM** (dependency-free C++)
- Speed: 500 tok/s on a Raspberry Pi 5; 400–1,500 tok/s on VR devices (Quest 3S,
  Vision Pro); 300–700 tok/s on sub-$200 phones
- Benchmarks (measured end-to-end with the shipped binary): Mobile Actions 63.7%
  (vs LFM2.5 230M at 69.1%); Seal-Tools out-of-domain 28.7% (vs 17.0%, a clear win);
  Irrelevance 60.8% (well ahead — refusing irrelevant requests); BFCL v4 42.6%
  (behind Apple FM at 61.7%, gap concentrated in Java/JavaScript domains absent from
  training); format correctness 93.4%
- Adopted by Pebble's Index 01 app
- Per-token compute: 35M matmul-active params / 70 MFLOPs (vs LFM2.5 at 460,
  Apple FM at ~6,000)
- Target hardware: from Cortex-M microcontrollers (ESP32-S3, STM32H7) to x86 to
  WebAssembly

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | An on-device AI company shipping an on-device model; capability and channel match |
| Product insight | Understood that "turning on a light needs no world knowledge," solving small-model problems with architecture rather than parameter count |
| Execution quality | Native 2-bit training + grammar-aware decoding + deterministic memory — a complete technical narrative, not a demo |
| Timing | Good. Wearables, smart home, and cheap phones are scaling; "small models for tool calling" is one of the hottest on-device tracks of 2026 |

## The call

**This is the most complete technical narrative on the "small model for tool calling"
track, and worth watching.** FunctionGemma, LFM2.5, and Apple FM compete in the same
field; Needle cuts size to 1/5–1/70 of the rivals with native 2-bit training and a
custom architecture, matching them on Mobile Actions and DroidCall and beating them
out-of-domain on Seal-Tools — if those numbers hold, it is the best current answer to
"agent capability on resource-constrained devices."

**Three honest reservations**:
First, **all benchmarks are self-measured** — end-to-end with its own binary, its own
tool retrieval, its own prompts; the out-of-domain wins especially need independent
reproduction.
Second, **it loses overall on BFCL v4** — the complex tool ecosystem (Java/JS) is not
covered, which discounts how "agentic" it really is.
Third, **an open model has no moat** — 45M params is fine-tuneable; Pebble is both the
endorsement and the only public case, and whether a second and third device maker
adopts is the decisive question.

**Worth watching**: 509 HN points, real hardware adoption, and a complete technical
narrative mean the data is not fabricated; but everything at the model level still
needs independent verification.

## What to watch next

① Whether a second device maker beyond Pebble publicly adopts it — hardware adoption
is the hardest evidence for a model like this
② Whether any third party reproduces the benchmark numbers under standard protocols
③ Whether the model is downloadable on HuggingFace and community fine-tunes reproduce
it — openness decides whether an ecosystem forms

## What you can take from it

**Product logic**: when the task boundary is clear (mapping to a finite function set),
do not default to "bigger is better" — first ask "how much world knowledge does this
task need?" Cutting "device control" out of "general conversation" and building a
dedicated model is a model of task partitioning.

**Positioning language**: the benchmark table presentation is worth copying — every
row measured with the final shipped binary, the rivals' f16 conditions stated
explicitly, and the categories where it loses listed honestly. Honesty in comparison
is credibility.

**Pricing structure**: free open model + paid platform (runtime / edge-cloud) is the
standard on-device play; useful as a reference, no proprietary details.

## Verdict

**Worth watching.** Complete technical narrative, real hardware adoption, and real
discussion heat — "a 14MB agent" is itself a spreadable number. But self-measured
benchmarks, a single public case, and an open model's missing moat keep this at Worth
watching rather than Strong pick. Come back in three months against the three checks
above.
