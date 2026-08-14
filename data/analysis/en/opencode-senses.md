---
slug: opencode-senses
name: OpenCode Senses
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

Eyes for a text-only-model coding agent: a small local vision model converts screenshots into
structured text injected into the prompt, so cheap models without multimodal support can look at
images, read text, and locate elements.

## Who built it

A personal open-source project by itsmeadarsh2008, MIT licensed, published on npm as
opencode-senses, v0.1.3. It serves OpenCode — the open-source terminal coding agent from the SST
team (165k+ GitHub stars) with 75+ model providers, including text-only models. Repository created
2026-07-19, 38 commits.

_Read: the author picked a precise gap — OpenCode deliberately supports cheap/text-only models, and
"give text models vision" sits exactly on that route's pain point. The author's background is not
disclosed._

## What it actually does

- **13 vision tools** → OCR (extractable by kind: all / code / error), object detection, region
  locating, segmentation, crop, zoom, color analysis, image comparison, labeling, metadata, reverse
  image search, status check
- **Automatic injection** → attach an image to the agent and the plugin analyzes it (structured scene
  read + caption + precise OCR) and injects the result as a `<SENSES>` text block into the model
  prompt — the model "sees" without calling any tool
- **Local inference** → Moondream 2 by default (~4.5GB peak VRAM, fits 6GB GPUs), optional Moondream
  3.1 (9B); weights ~3.9GB, slow first call, sub-second typical response with a hot cache
- **Injection defense** → all image content is wrapped in an explicit "untrusted data" guard;
  instructions written inside screenshots are treated as data, not instructions
- **Privacy** → images and analysis never leave the machine, no API keys, free

**What it deliberately does not do**: no multimodal-model substitute, no cloud service, no general
visual Q&A — just "extract visual facts as text evidence."

## What old behavior it replaces

- **Switching to a multimodal model to see images** → text-only models could not look at anything;
  you had to switch to a paid multimodal API. Senses lets a local small model extract OCR,
  coordinates, and colors, and the text model keeps working
- **Manually transcribing error messages** → error screenshots used to require a human typing the
  text into the conversation; `senses_ocr(kind="error")` extracts clean error text directly
- **Humans describing images** → handing an agent a design mockup or screenshot used to mean either
  the human described it or the model guessed; now it is OCR'd first, so the model gets facts, not guesses

It moves vision capability from the model side to the tool side — not an upgrade to the model, an
upgrade to the facts fed to it.

## Business model

**Not disclosed / free.** MIT open source, distributed via npm, no paid tier, no API fees; the
user's own GPU is the cost.

_Read: the classic "distribution in exchange for ecosystem" play of the plugin economy — no direct
revenue, a bet that when the OpenCode ecosystem matures, this becomes the default vision layer. The
risk of this kind of project is built in: the platform ships official vision support and the plugin
value goes to zero overnight._

## Hard numbers

- **26 stars, 0 forks, 0 open issues** (fetched 2026-08-14). v0.1.3, 38 commits, created 2026-07-19
- Moondream 2 peak VRAM ~4.5GB; weights ~3.9GB; sub-second hot-cache responses
- 13 tools; MIT; published on npm
- HN: 8 points, 2 comments
- Usage and download counts: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Solo open-source project with complete community docs; author background unknown |
| Product insight | "Eyes for text-only models" is a smart angle; treating image content as untrusted data shows rare injection-defense awareness |
| Execution quality | TypeScript plugin + Python JSON-RPC runtime, clear structure; 0 forks, 0 issues means no large-scale validation |
| Timing | The price-performance window for small-VRAM local vision models plus a rising open-source agent ecosystem — good timing |

## The call

**The mechanism is worth watching; the product is under-validated.**
"Structured perception + text injection" is the cheapest way to give text-only or low-cost models a
missing capability — no model swap, no API fees, runs locally. For anyone building agent products,
this pipeline — extract external facts into structured text, then feed the model — is cheaper and
more controllable than forcing multimodality.

**Its most valuable design is the injection defense.** Wrapping screenshot content as untrusted data
blocks prompt injection — a layer most vision agents simply skip, and exactly where screenshot-based
workflows are most attackable.

**The ceiling**: Moondream 2-class models top out on complex UI understanding, and 26 stars with 0
forks means no ecosystem position has been established. The moment OpenCode ships official vision,
this is the first thing replaced.

## What to watch next

① Whether OpenCode's official plugin list includes it and whether stars cross 100
② Whether the sub-second hot-cache response holds on real projects (e.g., screenshot-to-front-end)
③ Whether third parties build "vision agent" workflows on top of it (a dependency signal)

## What you can take from it

**Product logic**: when adding capability to text-only or low-cost models, prefer "local small model
extracts structured facts (OCR, bounding boxes, colors) and injects them as text" over forcing a
multimodal upgrade. Wrap injected content in an untrusted-data guard against prompt injection. This
applies directly to agent products.

**Positioning language**: none.

**Pricing structure**: none. Free and open source.

## Verdict

**Unproven.** The mechanism transfers; the product validation does not. Come back in three months
against the three checks above.
