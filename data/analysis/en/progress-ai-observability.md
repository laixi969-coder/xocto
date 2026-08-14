---
slug: progress-ai-observability
name: Progress AI Observability
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An observability platform for production AI agents from Progress, the old-line software company:
it traces every model call, tool invocation, and retrieval, attributes spend to agents, workflows,
and models, and runs LLM-as-a-judge evaluations on the same captured traces.

## Who built it

Progress (NASDAQ: PRGS), a veteran infrastructure and developer-tools company best known in the
.NET ecosystem. The product is led by PM Lyubomir Atanasov (Lyubo), launched
2026-08-07, reaching 164 upvotes and #6 of the day. SDKs cover .NET, Python, and
TypeScript/JavaScript from day one — a positioning built around the enterprise .NET channel.

_Read: a big vendor entering agent observability means the category is past the "is this fake
demand" validation phase. Progress's hand is the .NET/enterprise channel, not technical
leadership — LangSmith, Langfuse, and Helicone are already running._

## What it actually does

- **End-to-end tracing** → SDKs emit OpenTelemetry traces; a multi-step run is broken into a span
  tree of model calls, tool invocations, retrieval, and custom operations. It can answer "did the
  workflow skip a tool, pass bad retrieved context to the model, or burn money in a retry loop"
- **Cost attribution** → estimated spend aggregated by agent, workflow, model, and provider, so
  expensive paths surface
- **LLM-as-a-judge evaluations** → runs evaluation tasks on captured traces, returning verdict,
  rating, and explanation; historical and real-time, with scores tied to the execution path that
  produced the output
- **Quality scorecards** → surfaces "successful but wrong" runs — the class of failure ordinary
  logs miss
- **Three-layer architecture** → lightweight SDKs (Python/.NET/TS) → dedicated collector
  (validates keys, enriches with cost and user attribution, stores) → web dashboard

## What old behavior it replaces

Previously, checking whether an agent was misbehaving meant ordinary APM and logs: you could tell
the service was up, how slow it was, and whether it errored — but not why an agent chose a
particular tool, got stuck in an expensive loop, or produced a confident hallucination. Teams
debugged by manually scrolling chat transcripts. Progress replaces the blind spot where "APM sees
outages but not wrong answers," putting execution trace, spend, and output quality in one view.

## Business model

**SaaS subscription, metered in "units."** Free: 10,000 units, 7-day retention. Starter $29/month
(200,000 units, 30 days). Pro $299/month (1M units, 60 days). Enterprise from $3,000/month with
custom volume. Overages $8 per 100,000 units. One span consumes one unit; one evaluation consumes
two — a heavily instrumented multi-step agent can eat several units per user request.

_Read: unit-based pricing is smart — evaluations cost twice as much as traces, forcing users to
learn sampling while giving the platform natural headroom to raise prices. The downside is a
complex billing story that will trip up SMBs._

## Hard numbers

- launch 2026-08-07: 164 upvotes, 15 comments, #6 of the day
- Real published pricing: free / $29 / $299 / $3,000+ per month
- SDKs: .NET, Python, TypeScript/JS; integrations include Semantic Kernel, LangChain, LlamaIndex,
  AutoGen, Microsoft Agent Framework, OpenAI, Azure OpenAI, Anthropic
- A third-party index shows the Python distribution depends on the Traceloop SDK — a possible
  acquisition/partnership with a known observability vendor, unverified
- User scale: not disclosed. A Reddit thread shows a customer describing it as "approaching
  feature parity" while asking whether anyone has actually tried it

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Established-company product with a dedicated PM; depth of agent-era understanding unproven |
| Product insight | "Bind evaluations to the trace" is right — quality scores detached from the execution path are meaningless |
| Execution quality | OpenTelemetry standard, dedicated collector, three-language SDKs — solid enterprise foundations |
| Timing | Category validated, but competition is ahead: LangSmith/Langfuse/Helicone are courting the same customers |

## The call

**Worth watching, as a template of the "established vendor chasing" product.** Complete features,
real pricing, clear channel (.NET enterprise customers) — this playbook has worked every time in
traditional software. But it shows no native insight about the agent era; every capability here
exists in LangSmith or Langfuse. Its differentiation reduces to two things the AI startups don't
have: Progress's brand trust and deep .NET ecosystem binding.

**The real question is channel conversion.** Progress has a working enterprise sales pipeline. If
.NET/Azure-centric teams start adopting in volume, this product can take a chunk of the market by
distribution rather than innovation. That makes it a worthwhile channel-competition case to study.

## What to watch next

① Whether the "has anyone actually tried it" Reddit skepticism gets replaced by real customer
cases and public endorsements
② Whether .NET/Azure-channel customers show up — the only structural advantage over startups
③ Whether unit-based billing draws complaints about complexity/cost — the metering story decides
how far it spreads into SMBs

## What you can take from it

**Product logic**: if you build evaluation features, follow the rule that scores must be bound to
the execution path that produced the output — detached scores are decoration and users can't trust
them. Also worth copying: make cost attribution a first-class feature, because cost is the pain
users feel most and pay for sooner than "quality."

**Positioning language**: none. Standard enterprise product copy; nothing to steal.

**Pricing structure**: unit metering on spans and evaluations, with evaluation priced at 2x
tracing — it nudges users toward sampling while leaving the vendor natural price headroom. A
usable model for metered pricing.

## Verdict

**Worth watching.** No impressive innovation, but the channel play is worth observing — whether an
incumbent can cut a slice of the agent-observability market with its existing sales pipeline.
Re-check channel conversion and real customer endorsements in three months.
