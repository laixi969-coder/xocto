---
slug: shennongmi
name: ShenNongMi
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A traditional Chinese medicine (TCM) knowledge navigator: a 19,000+ node Neo4j
knowledge graph as the base, wired to a LangGraph workflow with self-correcting
NL2Cypher, so TCM questions are answered from the graph rather than hallucinated
by the model — plus a pipeline that auto-generates wellness content and publishes
it to Xiaohongshu (RED).

## Who built it

GitHub author Happy-Chen-CH; the README states it was developed in collaboration
with Claude, for educational and research purposes only, with data sourced from
public TCM encyclopedia sites. Author identity and background: not disclosed.

_Read: a typical one-person-plus-AI technical project. Its value is running a full
"knowledge graph + agent workflow" stack end-to-end and open-sourcing it — not
productizing it. The author appears to be validating whether that architecture can
land in the TCM domain._

## What it actually does

- **TCM knowledge Q&A** → answers questions about herbs, formulas, symptoms,
  effects, and classical texts from the Neo4j graph (19K+ nodes, 6 entity types,
  6 relation types)
- **Self-correcting NL2Cypher** → extract entities → match graph nodes via FAISS
  (BGE-Large-Zh-v1.5) → generate Cypher → validate it, regenerate on error →
  query → compose the answer. The answer stays inside "what's in the graph,"
  which keeps the model's hallucination contained
- **Intent recognition** → a fastText + fine-tuned RoBERTa-LoRA dual-model setup
  distinguishes "ask about TCM" from "publish content," claiming 99.75% accuracy
- **RED content generation and publishing** → generates wellness content with
  Volcano Engine Jimeng AI images and publishes to Xiaohongshu via Playwright
- **Interactive graph browsing** → visually explores a network of 6 entity types
  and 6 relation types

**Stack**: DeepSeek v4 (extraction/QA/Cypher), Neo4j, LangGraph (14-node
workflow), FAISS, Streamlit frontend + FastAPI backend (SSE streaming).

## What old behavior it replaces

Three ways to look up TCM knowledge before this: search engines — broad but
noisy, with uneven reliability; asking an LLM directly — TCM is exactly the
domain where models confidently fabricate, and wrong herb properties, meridian
attributions, or compatibilities can mislead people; or books/doctors — accurate
but slow.

This project replaces the "use a general LLM for vertical knowledge"
unreliability: the knowledge graph anchors every answer, the model only arranges
the graph query result into language, and when it cannot answer, it says so rather
than inventing. It also turns "posting wellness content to Xiaohongshu" from
hand-writing, sourcing images, logging in, and publishing manually into an
automated pipeline.

## Business model

**None.** MIT open source, purely educational/research, no product, no service,
no pricing.

_Read: the commercial value of such a project is not in the free demo itself but
in the pattern — "vertical knowledge graph + self-correcting query." If it works
for TCM, the same approach could be replicated in law, finance, or machinery,
which all have strongly structured knowledge. The author has not productized it._

## Hard numbers

- GitHub: 103 stars / 7 forks / 0 open issues, 5 commits total (latest 2026-08-07)
- Graph: 19,000+ nodes, 6 entity types, 6 relation types
- Workflow: 14 nodes (LangGraph)
- Claimed intent-recognition accuracy: 99.75% (fastText + RoBERTa-LoRA dual model)
- Authors, users, activity: single-author project, no user data

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A tech-driven personal project; the motivation is validating an architecture, not serving users |
| Product insight | "Constrain LLM hallucination with a graph" is the right direction; self-correcting NL2Cypher is the genuinely valuable mechanism |
| Execution quality | Full chain works end-to-end: crawl → extract → build graph → workflow → service. But five commits means almost no iteration |
| Timing | The "vertical knowledge graph as moat" thesis is timely, but the project has no commercial follow-through |

## The call

**Watch the mechanism, not the product.**

"Constrain LLM output with a knowledge graph" is one of 2026's most overrated and
most underrated vertical-AI theses. Overrated because building the graph is
expensive; underrated because once built, it is a moat models cannot flatten.
ShenNongMi's value is open-sourcing the whole mechanism as a template — the
self-correcting NL2Cypher (re-query instead of force-answering) is a targeted fix
for the "vertical Q&A is unreliable" disease.

**Three buckets of cold water.** First, the 99.75% accuracy is for intent
recognition (whether to publish), not medical-answer accuracy — the two are easily
conflated. And the graph covers only 19K nodes while the real body of TCM
knowledge is far larger, so the "can answer" range is narrow. Second, automated
Xiaohongshu publishing is a compliance gray zone — even the project's own
disclaimer requires following platform terms, and automation may violate them;
this feature is risky as a product. Third, five commits, a single author, and no
users put it closer to a technical experiment than to "usable" or "used."

## What to watch next

① Whether stars pass 500 in three months and commit cadence stays alive — the
difference between a one-off and a maintained project
② Whether the graph scales (node count, classical-text coverage) — vertical depth
sets the ceiling
③ Whether third parties (health-communication or knowledge-payment teams) build
products on it — how often an open-source template gets reused is the real
influence metric for this kind of project

## What you can take from it

**Product logic**: for vertical Q&A, do not expect the LLM to answer directly.
Make a structured knowledge base (graph/database) the single source of truth, let
the LLM only phrase the query results, and make "state it when you cannot find it"
the default. This "knowledge-base-constrained generation" architecture transfers
to any domain with strongly structured knowledge.

**Positioning language**: none. Technical documentation; nothing to steal.

**Pricing structure**: none. Not commercialized.

## Verdict

**Unproven.** The "vertical graph constrains the LLM" mechanism is worth learning
from, but the project is still a single-person technical experiment: shallow data,
almost no iteration, no users, no commercial intent. Watch how it gets reused as a
template rather than what it becomes itself.
