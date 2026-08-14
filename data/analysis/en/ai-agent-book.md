---
slug: ai-agent-book
name: ai-agent-book
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An open textbook that turns "how AI agents are actually designed and shipped" from
folklore into engineering: 10 chapters, 92 runnable experiments, all open source,
built around one formula: Agent = LLM + context + tools.

## Who built it

Author Bojie Li (GitHub: bojieli): graduated from the USTC gifted
program, was one of Huawei's first "genius youths" (researcher at Noah's Ark
Lab), co-founded Logenic AI, and is now Chief Scientist at Pine AI.

The repo analyzed here is **chemark/ai-agent-book**, a study fork of the
upstream bojieli/ai-agent-book. chemark's increment is a Japanese translation
(10 chapters, 135 localized figures, PDF/EPUB build).

_Read: the author's path is what gives the book credibility — he did frontier
research at Huawei and then built startups. This reads like engineering judgment
from someone who has been burned, not an academic survey. The fork's Japanese
translation is also a tell: the upstream team treats multilingual distribution as
a core part of textbook reach._

## What it actually does

- **10 progressive chapters** → formula basics → context engineering → memory and
  knowledge bases → tools (MCP) → coding agents → evaluation → post-training →
  self-evolution → multimodality → multi-agent collaboration
- **92 companion experiments** → categorized as runnable / reproducible / design,
  with per-chapter code in the repo
- **Defines vocabulary** → "Harness engineering": everything outside the model
  (context management, tool design, memory systems, evaluation) is where the
  competitive advantage lives
- **Multilingual distribution** → 12 language versions by the official count
- **Apache-2.0** → full text, figures, code and PDFs, all free

**What it deliberately is not**: a video course, a framework's docs, or a wrapper
around any model vendor.

## What old behavior it replaces

Learning agents used to follow three paths, and none of them answered "how does an
agent actually work in production":

**Framework docs** — LangChain, CrewAI and AutoGen each have their own APIs, every
tutorial starts at Hello World and teaches you how to call the API, but not how to
design memory, how to handle tool-call failures, or how to standardize messages
across multiple agents.

**Blogs and videos** — scattered, fast-stale, mutually contradictory. You finish
feeling like you get it, then stall the moment you try to build.

**Learning by burning** — the most expensive route: pick the wrong framework,
design context badly, lose three months and not know which step was the mistake.

The book attacks the shared gap: **a systematic, reproducible cognitive framework.**
It gives the field a common vocabulary (Harness engineering) and a coordinate
system for arguing about how to build agents.

## Business model

**None.** Pure open source, Apache-2.0, no paid content, no enterprise edition.
The author's company does not monetize it directly.

_Read: the money is elsewhere. Li is Chief Scientist at Pine AI; the book's
distribution is his recruiting channel and ecosystem-positioning statement. When a
field moves this fast, whoever writes the textbook defines the vocabulary, and
that definitional power flows toward the company he belongs to._

## Hard numbers

- Upstream bojieli/ai-agent-book: **30,013 stars** (as of 2026-08-03), with a
  peak of 9,298 stars in one week, #1 on GitHub Trending; 16k stars in the first
  16 days
- 10 chapters, 92 experiments; the Chinese PDF is ~428 pages (v1.2)
- 12 language versions per the official count; the chemark fork contributes Japanese
- chemark/ai-agent-book: 221 stars / 21 forks (this batch's observation)
- Created 2025-09-09 (upstream)

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Exceptional. Genius-youth researcher, startup founder, current AI chief scientist — full chain inside the room |
| Product insight | Caught the "field lacks a systematic textbook" gap and gave readers memory anchors via a formula and Harness engineering |
| Execution quality | 92 runnable experiments plus multilingual build chains plus versioned PDFs; far beyond a typical open book |
| Timing | Precise. The agent boom plus framework fragmentation is exactly when a textbook is most valuable |

## The call

**This is a textbook case of "whoever writes the textbook defines the
vocabulary."** The market is not short of tutorials; it is short of a coordinate
system. One formula (Agent = LLM + context + tools) and the Harness concept give
the whole conversation an anchor. The star velocity (16k in 16 days) says the need
is real and widespread.

**The book's judgment holds up too.** Putting the competitive edge outside the
model — context, tools, memory, evaluation — rather than in the model itself is a
position largely validated by 2026's agent practice: most people fail at agents
not because the model is weak.

**But separate the book's influence from its value as a "product."** It does not
sell, has no follow-on service, and its value is one-time. Do not watch it for
revenue; watch whether the vocabulary it invented actually becomes lingua franca —
and whether the author's company can absorb the attention.

## What to watch next

① Whether the star count holds at five figures in three months — textbook repos
rise fast and cool fast
② Whether "Harness engineering" gets cited by papers, job postings, or other
textbooks — a word is only real when other people use it
③ Whether Pine AI surfaces public funding or partnership signals enabled by this
book's reach

## What you can take from it

**Product logic**: in a fragmented, fast-moving technical category, the biggest
opportunity is not another tool but "the textbook that threads the fragments
together." A coordinate system is scarcer than a component. Whoever writes the
book defines the vocabulary; whoever defines the vocabulary captures attention;
attention is where all downstream monetization starts.

**Positioning language**: anchor the whole book with a one-line formula
(Agent = LLM + context + tools). If readers remember the formula they remember
the book. Compress your content to one memorable anchor before piling up chapters.

**Distribution structure**: open textbook plus multilingual translations plus a
code-experiment pack, binding "read" to "try" and lowering the friction from
reading to building.

## Verdict

**Worth watching.** This is not a product to buy; it is an event that is defining
industry vocabulary. It validates a transferable path: during a technology boom,
the textbook is the most underrated influence lever. The star count has proven the
demand; what remains to verify is whether the vocabulary gets adopted.
