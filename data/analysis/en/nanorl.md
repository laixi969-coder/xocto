---
slug: nanorl
name: NanoRL
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

One RL training loop that runs CartPole on a laptop and disaggregated async RLVR on a GPU
cluster — about 1,800 lines across 7 files, readable in an afternoon. It is meant to be read,
not imported.

## Who built it

alex000kim (a GitHub account), MIT licensed, repository created 2026-08-11, explicitly styled
after Karpathy's nanoGPT ("meant to be forked, not imported").

_Read: a nanoGPT-style education-first project. The author clearly knows production RL training
(veRL, TRL, DeepSpeed territory) but chose the opposite: strip everything down to the core so
the training loop becomes readable. Someone who writes code like this has usually been burned by
production-stack complexity first._

## What it actually does

- **Four algorithms** → REINFORCE, PPO (GAE + critic), GRPO, and RLOO all live in ~90 lines of
  algos.py. The core update is one line — `loss = -(advantage * logprob).mean()` — and the
  algorithms differ only in how advantage is computed
- **Sync to async** → `--role trainer` and `--role rollout` run on separate boxes talking over
  stdlib HTTP; one knob (max_staleness) simultaneously sets the rejection bound, the queue
  depth, and the number of weight snapshots kept
- **Distrusts other people's logprobs** → the trainer recomputes old_logp under the exact
  weights that sampled each batch, and drops any batch whose weights it no longer has. This is
  the single most valuable engineering judgment in the project
- **vLLM generation + adapter sync** → vLLM on the workers, separate batch sizes for generation
  and scoring (tying them cost 6x in one measured run), and weight sync that moves only LoRA
  adapters (~170 MB versus 16 GB)
- **End-to-end reproducible** → a SkyPilot config that just runs: Qwen3-8B + LoRA, 8x H100
  trainer and 8x L40S generation, 102k sequences in 90 minutes

## What old behavior it replaces

Training LLMs with RL today defaults to TRL or veRL plus Ray plus DeepSpeed: thousands of
dependencies, more docs than code, and a training loop buried under three layers of abstraction.
To understand "how does GRPO actually update" you have to read a framework's source first.

That splits into two dead ends. Teams shipping to production swallow a black-box framework and
tune it like superstition when things break. Individual researchers trying to learn face an
industrial codebase with an absurd onboarding cost.

nanoRL replaces the entire burden of the second path: 1,800 lines you can finish reading, run,
and modify. It changes RL training from "you must trust the framework" to "you can verify every
line." Its value is not training a SOTA model; it is making the craft of RL training learnable
and inspectable — the same move nanoGPT made for GPT.

## Business model

**None.** MIT, no hosting, no service.

_Read: an educational infrastructure project whose value sits in ecosystem position, not
commerce. But note one signal: the end-to-end run exposes a real training-engineering bug (vLLM
logprobs inconsistent with HF silently destroy training) and fixes it. That "knowledge bought
with pain" is the content asset it gives the industry._

## Hard numbers

- **5 stars, 0 forks.** Repository created 2026-08-11
- HN: 10 points, 0 comments
- Code size: ~1,800 lines across 7 files (algos.py ~90, core.py ~110, utils.py ~170,
  serve.py ~250, tasks.py ~310, model.py ~330, train.py ~560)
- End-to-end result (Qwen3-8B + LoRA, Countdown): held-out accuracy 0.391 → 0.609 (+22 pp),
  200 steps / 90 minutes / 102k sequences; 0 of 1,603 batches dropped
- The key contrast: without recomputing old_logp, the ratio drifts from 1.006 to 1.165 and
  accuracy falls from 0.500 to 0.188; with recomputation, the same model climbs
- 44 CPU-only tests

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Identity unconfirmed, but the production experience visible in the code (the vLLM logprob trap) says someone who has actually done this |
| Product insight | Nails "training code is unreadable" as a real problem and makes readability the product positioning |
| Execution quality | High. 44 tests, an end-to-end run that converges, numbers that reconcile, and an explicit "deliberately not doing" list |
| Timing | Always right for education; for production, the scale ceiling (single box, single model, no MoE) is a deliberate choice |

## The call

**This is the "teach the market with a minimal rewrite" play, executed cleanly.** It never
claims to replace veRL — it claims "you can read the whole codebase, fork it, change it."
That positioning is exactly nanoGPT's: not a tool, a textbook.

**The transferable rule: when a domain is dominated by a big black framework, a readable minimal
implementation is the strongest trust-builder.** Big frameworks prove capability; small
implementations prove understanding. And it proves understanding in a very specific way: it
publishes a real pitfall (logprob mismatch dropping accuracy from 0.500 to 0.188) with the fix.
That is a lesson-built-credibility play, more persuasive than any benchmark.

**But it is not a product.** 5 stars, 10 points, no users, no commercial outlet. Its readers
are "the people who write the next production RL framework" — if they fork it, learn from it,
and apply it inside veRL configs, its value closes the loop.

**The way educational projects die is also visible**: once stars plateau, if the author stops
maintaining (new algorithms, new model compatibility), it becomes an outdated handout.

## What to watch next

① Whether anyone forks it for a real production task or publicly reproduces the end-to-end numbers
② Whether the author adds algorithms (a DPO/Online-DPO line) or fixes issues within three months —
  an educational project lives or dies on maintenance
③ Whether a production framework absorbs it as teaching material or source code (being cited is
  the real success)

## What you can take from it

**Product logic**: when your domain contains a hard-to-enter skill, building authority with one
readable minimal implementation beats a hundred tutorials. Tutorials are one-way; readable code
is an asset people can fork.

**Positioning language**: "meant to be forked, not imported" — naming the target user's
behavior in the positioning beats any feature description. Also "if you need these, you have
outgrown this repo, and that's the point" — stating the boundary as a feature.

**Pricing structure**: none.

## Verdict

**Unproven.** As a textbook it has real value, and its content asset (the logprob trap) is
industrial-grade experience; as a product it has no commercial form. Write it down and check in
three months whether it gets forked and cited.
