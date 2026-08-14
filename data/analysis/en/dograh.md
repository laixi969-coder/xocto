---
slug: dograh
name: Dograh
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An open-source voice agent platform: build phone-calling AI agents (answer calls, book appointments, qualify leads, send payment reminders) with a drag-and-drop workflow builder, self-host it or bring your own models, positioned as the open alternative to closed Vapi and Retell.

## Who built it

Maintained by the dograh-hq organization (`dograh-hq/dograh`), created September 2025, written in Python. The PH makers include Pritesh Kumar and sandeep_vemu; the team describes itself as "YC alumni and exit founders" and emphasizes that every line has been open since day zero (BSD-2-Clause). The pool record lists Rohan Chaubey as builder.

_Read: maker identity is cross-checkable across several PH commenters, but the "YC alumni" claim has no public company page to back it — treat it as marketing until shown otherwise. The real signal is the repo itself: over 5,000 stars in about a year is not small in the open-source voice-agent world._

## What it actually does

- **Visual workflow builder** → drag-and-drop nodes to assemble a voice agent; every conversation step is a node, branchable on caller response, with API calls mid-flow
- **Both architectures** → cascade (STT → LLM → TTS) and end-to-end speech-to-speech (e.g., Gemini Live, GPT Realtime), including splitting an S2S stream across multiple agents for finer control
- **Default stack included** → built-in LLM/STT/TTS runs with zero config; BYO supported (OpenAI, Azure, Groq, Deepgram, ElevenLabs, local open models)
- **Telephony** → Twilio (and other channels) integration, inbound and outbound, with warm handoff to a human
- **MCP native** → a built-in MCP server lets Claude Code, Cursor, and other agents build a voice agent by chatting — "build me an EMI collection agent"
- **AI-to-AI testing (LoopTalk)** → create AI personas that call your agents to simulate real customer behavior
- **2x conversion trick** → pre-recorded audio mixed with TTS in the same cloned voice, using pre-recorded lines when they fit and falling back to TTS otherwise

**The core pitch**: data never leaves your infrastructure — call recordings, transcripts, prompts, and customer PII stay inside your boundary, and model inference can even run fully offline/air-gapped.

## What old behavior it replaces

To make an AI that makes phone calls, you used to pick one of two paths:

**Closed SaaS billed per minute** — Vapi, Retell, Bland: register and build agents on their API. Fast, but per-minute pricing bites at volume (Retell lands around $0.10/min including a hidden platform fee), and everything — audio, transcripts, customer PII — passes through the vendor's cloud, which disqualifies it outright for compliance-sensitive industries.

**Building from scratch** — Pipecat, LiveKit, or raw model APIs: wire your own telephony, write your own orchestration, handle disconnects and retries yourself. Free, but voice agents are a swamp of engineering details (VAD endpointing, streaming, barge-in, timeouts), and a production-grade stack takes a long time to assemble.

Dograh replaces the "renting from closed SaaS" part — self-hosting removes the per-minute platform fee — while absorbing the grunt work of orchestration, telephony, and testing that hand-rolled stacks force on you. Its positioning is blunt: on Vapi you rent agents; with Dograh you own the whole stack.

## Business model

Three layers:

- **Self-hosted**: free, BSD-2-Clause, `docker compose up` and it runs, forever
- **Managed cloud** (app.dograh.com): they run the same stack for you, metered usage
- **Private cloud**: the whole stack deployed inside your VPC, they handle operations

_Read: the classic "open source as funnel, hosted as revenue" model, same playbook as self-hosted SaaS alternatives. For compliance-sensitive industries (healthcare, finance, collections), "data never leaves the boundary" is a hard requirement, and free self-hosting is the best acquisition ad there is. The real business is managed and private cloud, but pricing is not public._

## Hard numbers

- **5,318 stars, 1,278 forks.** Created 2025-09-09, roughly 11 months old
- BSD-2-Clause, primarily Python
- PH launch: 38 upvotes (early August 2026)
- Topics show a Pipecat relationship; telephony support includes Asterisk ARI
- Industries already seeing use per the makers: legal intakes, car rentals, restaurant booking, medical-insurance outbound
- Paid customers, ARR, active deployments: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The team answers voice-agent engineering details concretely (S2S splitting, QA nodes, fallbacks) — not outsiders |
| Product insight | Seized on "data sovereignty," the structural weakness of Vapi/Retell; self-hosting plus MCP-native are the right positions |
| Execution quality | A year of maturity shows: complete docs, one-line Docker install, LoopTalk testing, pluggable stack |
| Timing | Good. Voice-agent demand is rising, and per-minute pricing hurts exactly the high-volume customers who are noticing |

## The call

**This is a rare positive case of "open source cloning a validated closed product": the target is well chosen and the engineering keeps up.**

Cloning a proven closed-source product as open source skips market education entirely — Vapi already taught the market that voice agents are useful; Dograh only needs to say "same thing, without the per-minute bill." The ever-present risk is being forever the cheaper follower on leftover demand. Which kind it is shows in two signals: star count (5,318 — developers approve) and the makers' stated industry uses (collections, healthcare — the data-sensitive sectors Vapi cannot serve).

**The transferable rule: attack the customer segment where the closed SaaS hurts most on data sovereignty.** Dograh never fights Vapi on price head-on; it goes around to the compliance and data-sensitive side, where customers literally cannot use Vapi because data cannot leave the boundary — not a price question at all. Flanking your competitor's structural blind spot beats a frontal price war.

**Two risks**: first, the "YC alumni" backing has no public verification, so team credibility has to be earned by the product; second, self-hosted products earn revenue late — stars are not paychecks, and whether even 1% of 5,000 star users pays for the managed cloud is the real commercialization test.

## What to watch next

① Whether managed-cloud conversion produces public signals (case studies, industry events) after launch
② Whether compliance-sensitive customers (healthcare/finance/collections) publicly adopt — the dividing line vs Vapi
③ Star growth over three months: whether a one-year-old open-source project still grows organically tells you if the community is real or marketed

## What you can take from it

**Product logic**: if you build an "open-source replacement for a closed product," list the three things users hate most about the incumbent (price, data sovereignty, lock-in), attack exactly one, and speak only to that one's customers. Dograh puts all firepower on "data never leaves your boundary," right down to copy about HIPAA/GDPR/SOC 2 scenarios.

**Positioning language**: frame ownership against rental — "on closed platforms you rent your agents; with Dograh you own the whole stack," and "your models, data, and GPUs stay in your country; your voice stays yours." Polarizing language works better than feature lists for open-source projects.

**Pricing structure**: three ascending layers — free self-host, metered managed cloud, VPC ops. The self-hosted version must be genuinely complete, because it is the acquisition ad.

## Verdict

**Worth watching.** Well-chosen target, mature engineering, and real community traction — the strongest "open source replaces closed" sample in this batch. But revenue is unproven and the team's credentials lack public verification. Watch managed-cloud conversion and compliance-industry adoption.
