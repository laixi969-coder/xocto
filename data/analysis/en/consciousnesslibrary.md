---
slug: consciousnesslibrary
name: consciousnesslibrary
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A free, open library that pulls the world's psychedelic and consciousness research into one
place: every 20 minutes it ingests new papers from a dozen-plus academic APIs, dedupes them,
organizes them by topic, writes plain-language summaries, and can synthesize evidence across
the whole corpus — while correctly keeping "LSD the psychedelic" apart from Lumpy Skin Disease.

## Who built it

Posted on HN (Show HN, 30 points / 12 comments). The author writes that he had just
finished a master's in Psychedelics and Consciousness Studies, built the library he wanted
while studying, shelved it for a year, then picked it back up after his practicum advisor
pushed him to go hard on it. The project is registered as a 501(c)(3), legal entity Mindscape
Collective, self-funded so far. The pool lists the builder as `elliotec`.

_Read: a library that "reads the whole field" can only be built by someone who actually read
the field for a degree and uses it daily — the barrier is not technical, it is knowing what to
collect and what "complete" means. This author has both._

## What it actually does

- **Aggregates and dedupes** → pulls from a dozen-plus academic APIs (PubMed, OpenAlex, Europe
  PMC, bioRxiv, more) every 20 minutes, automatically deduplicated
- **Relevance judging** → a two-stage pipeline of cheap keyword prefilter plus an LLM rubric
  that accepts or rejects papers, resolving the hard cases: LSD the psychedelic vs Lumpy Skin
  Disease, ketamine for depression vs anesthesia for cats
- **Plain-language summaries** → every paper gets a "Study at a glance": design, sample size,
  key findings, in plain language
- **Topic organization** → 35,787 papers across 37 topics grouped under psychedelics, practices
  (meditation), experience, humanities, neuroscience
- **Evidence synthesis** → topic pages carry evidence overviews, and you can ask across the
  whole corpus; the AI synthesizes consensus, conflicts, and unknowns
- **Clinical trial tracking** → refreshed daily from ClinicalTrials.gov: recruitment status,
  phase, enrollment, sponsor
- **A map of the whole corpus** → one dot per paper, so the shape of the field is visible at a glance

**What it deliberately does not do**: no commercial search platform, no ads, no login required
to read; free-text synthesis needs a free account.

## What old behavior it replaces

Researching psychedelics used to mean searching PubMed, bioRxiv, and ClinicalTrials.gov
separately, manually deduping, and manually reading dozens of abstracts to find consensus and
disagreement. A literature review per topic ran on a weekly timescale.

This library replaces three manual chores: **cross-database search** (one query covers
everything), **reading abstracts to find consensus** (synthesis names what agrees and what is
still contested), and **tracking clinical trials** (daily refresh instead of weekly manual
checking).

## Business model

**Non-commercial.** A 501(c)(3) nonprofit: free, ad-free, readable without an account, funded
by donations (Stripe, PayPal, Buy Me a Coffee) plus the author's own money.

_Read: this is not a business, it is infrastructure. But "build the complete corpus of a narrow
field as a free public good at near-zero cost" is itself a signal for anyone making vertical AI
products — the asset pays off elsewhere (influence, data partnerships, foundation support),
not in subscription fees._

## Hard numbers

- **35,787 papers / 82,200+ authors / 37 topics**, growing daily
- Infrastructure: Rails 8.1, a single Postgres (full-text, vectors, and job queue all in one),
  a $24/month DigitalOcean droplet (just upgraded from the $12 tier), deployed with Kamal
- **Total LLM spend to date: ~$28** (DeepSeek-V4-Flash), trending down after a one-time backfill push
- Ingestion cadence: polls a dozen-plus academic APIs every 20 minutes
- Team: essentially one person (the site lists a few collaborator avatars); revenue, funding:
  none (donation-based)

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Field master's degree, built to satisfy his own research need — the textbook "user is the author" case |
| Product insight | Sees that a complete narrow corpus is the moat; handles the relevance ambiguity (LSD vs Lumpy Skin Disease) early — the life-or-death issue for this kind of library |
| Execution quality | One Postgres carrying full-text, vectors, and queue on a $24/month box; engineering restraint at textbook level |
| Timing | Psychedelic research renaissance plus open scholarly data — exactly the window for public infrastructure |

## The call

**A template for "turn a very narrow field into a complete corpus at near-zero cost." Low
commercial value, high mechanism value.**

The most stealable part is the **relevance pipeline**: cheap keyword prefilter first, LLM
rubric accept/reject second. It sounds plain, but the author says relevance was by far the
hardest part — generic search fails here because Lumpy Skin Disease also contains "LSD," and
vector retrieval cannot tell the semantic camps apart. The two-stage pipeline brought the whole
corpus's LLM cost down to $28, and it transfers to any vertical corpus.

**The one thing it did right** was registering as a nonprofit instead of a company. Trust
barriers are high for narrow-field public libraries, and "we don't sell data, we don't sell
ads" is part of the content.

**The limits** are obvious too: solo operation, donation funding, no public retention metrics.
The biggest risk in this project is not the product, it is the maintainer's energy — once the
author lands a job, update cadence will drop.

## What to watch next

① Whether paper count keeps growing daily and the 20-minute cadence actually holds — is
  maintenance alive
② Whether registered users and synthesis-query usage ever go public — real use, or self-indulgence
③ Whether institutional partners appear (universities / foundations / journals) — the hinge
  between a personal project and public infrastructure

## What you can take from it

**Product logic**: any vertical can copy the trio of "complete corpus + plain summaries +
evidence synthesis." The key move is defining "complete" first — subscribe to a dozen APIs and
poll every 20 minutes; completeness beats retrieval quality as the initial claim.

**Positioning language**: "The world's psychedelic and consciousness research, in one open
library." Define the product by the promise of totality, not by "our database is large."

**Pricing structure**: none. But "nonprofit + donations + self-funding" is a viable structure
for narrow-field tools that need public credibility.

## Verdict

**Worth watching — as a mechanism sample, not an investment.** Complete corpus, near-zero cost
($24/month infra plus $28 of LLM spend), and a two-stage relevance pipeline that transfers
directly. It proves one person, one $24 server, and a few dozen dollars of LLM calls can build a
field's public infrastructure. Don't expect a business; do copy the mechanism.
