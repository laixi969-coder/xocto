# xOcto architecture context

## Discovery Interpretation Module

xOcto treats every collected item as a **Discovery Signal** first. A product page,
repository, ranking entry, media report, filing, announcement, or discussion is the
carrier of evidence; it is not the editorial object by itself.

The interpretation seam turns each signal into one of three public objects:

- **Entity** — a stable company, product, or AI-transformed business that can receive
  evidence, events, and an opportunity judgment.
- **Market Context** — a model release, price change, regulation, platform policy, or
  industry shift. It keeps a stable name and bilingual summary and is published in
  the daily market flow; it is not a rejection bucket.
- **Rejected Signal** — material that does not support a useful public observation.

## Identity and event rules

Entity identity is independent from the carrier URL. Media-host domains never imply
that two reports describe the same entity. Exact evidence URLs, stable product URLs,
and unique entity-name mentions may connect a new signal to an existing entity.

A **Discovery Event** records what changed and when xOcto learned it. Reports,
financial disclosures, launches, adoption, revenue, customer, funding, pricing, and
policy changes receive bilingual event summaries after editorial validation.

## Daily Revision Module

The daily report is a revision, not a one-shot artifact. A later collection on the
same Beijing date reopens editing whenever new candidates exist, retains supported
material from the earlier edition, and incorporates formal market context. With no
new candidates the run is idempotent.

The hosted workflow collects and revises in the morning and evening, retries a failed
editorial pass once, and checks that raw data plus both language editions exist for
the target date before considering the daily chain complete.

## Demand Assessment Module

The public demand assessment has one deep projection seam, the **Demand Read**.
It combines the stable product record, the latest non-downgraded review, normalized
usage metrics, and semantic evidence into four user-centred answers: the job, the
pain or problem, the current alternative, and the reason people adopt or attend to
the product. Every verdict receives this read; a negative or uncertain verdict may
not erase the problem the product attempts to solve.

Demand and business evidence are separate interfaces. **Demand Maturity** describes
whether the user job, pain intensity, and existing behaviour are supported.
**Business Evidence Maturity** describes adoption, pricing, actual payment,
retention, and renewal. Product copy is not pain evidence, traffic is not payment,
and missing commercial evidence is unknown rather than failure.

Full reviews are deeper revisions and always outrank later baseline reviews. A
baseline review is created for every public Entity, refreshed only when the Entity
or its evidence changes, and never generated daily merely to advance a date.
