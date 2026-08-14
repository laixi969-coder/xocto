---
slug: ai-courtroom
name: ai_courtroom
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A replayable multi-agent "liability tribunal" experiment: multiple agents cast as
judge, lawyers, witnesses and jurors talk to each other over agent-to-agent (A2A)
messages, and the question is how "who may talk to whom" changes a collective
verdict. Every run produces an interactive, replayable HTML report.

## Who built it

nMaroulis (GitHub handle), the author of ProtoLink — a Python multi-agent
framework built around the A2A protocol, MIT-licensed, positioned as an
alternative to chain-centric frameworks like LangChain: each agent is a
self-contained runtime entity with identity, capabilities, lifecycle and
task-level communication.

ai_courtroom is an example under `examples/` in the ProtoLink repo, not a
standalone product.

_Read: what the author is really doing is building observable, experimentable
tooling for multi-agent communication; the courtroom is just the narrative shell.
The actual product being sold is ProtoLink's orchestration and the idea that
communication topology can be controlled._

## What it actually does

- **A fictional liability courtroom** → 7 court roles (judge, plaintiff counsel,
  defense executive, engineer, regulator, insurance lead, investigator) plus 5
  jurors; prompts describe personalities only, with no preset verdicts
- **Four communication topologies** → solo (single direct judgment) /
  independent (5 jurors, no contact) / star (all messages relayed through the
  chair) / mesh (everyone talks to everyone)
- **A replayable event ledger** → guilt-register values and votes before and after
  every A2A message, replayable side by side
- **Influence tracing** → jurors expose only structured actions (ask a question,
  cite an exhibit); private confidence stays hidden; the report distinguishes
  observed change from causal attribution
- **Deterministic baseline plus real models** → a seed-driven offline LLM, or
  OpenAI/Anthropic and others for reproduction
- **Full evidence output** → JSON, summaries, transcripts, interactive HTML, trace
  telemetry, with hash checks and paired-ablation design

**What it deliberately is not**: a general intelligence leaderboard, and it makes
no causal claims — only reported observations.

## What old behavior it replaces

Figuring out "do multiple agents get better answers by talking to each other"
used to rely on two things:

**Judging the final output** — treat the multi-agent system as a black box; trust
good results, tweak prompts on bad ones, and nobody knows what happened inside.

**Reading raw logs** — eyeball transcripts and log streams to match "which
message caused which change": slow, lossy, and logs only allow after-the-fact
review, not tracing the causal chain between messages.

ai_courtroom replaces "debugging multi-agent collaboration by intuition and log
reading" with a machine-viewable, frame-by-frame record where every message
carries structured state change. It is effectively putting a flight recorder on
agent conversations.

## Business model

**None.** This is a research example inside an open-source (MIT) framework: no
pricing, no product, no corporate entity.

_Read: the commercial imagination lives elsewhere — traceability of multi-agent
systems is becoming a compliance requirement, and finance and healthcare will
eventually demand "every decision step can be replayed." ProtoLink is betting on
being the framework that can replay, before the compliance demand arrives._

## Hard numbers

- HN: 19 points / 1 comment (this batch's observation)
- ProtoLink: 257 commits, MIT, pure Python, sole core dependency Pydantic
- The demo runs four conditions on a deterministic reference LLM, with hash
  checks and paired-ablation design
- Users and adopters: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author is both framework author and experiment designer; the example serves the framework |
| Product insight | Turns "who talks to whom" — an overlooked variable — into an experiment, closer to the truth than the default "more messages is better" |
| Execution quality | Replay, hash checks, paired ablation, structured action protocols; methodologically stricter than most HN projects |
| Timing | Early. The traceability need is real, but multi-agent systems are not in production at scale yet, so buyers are scarce |

## The call

**This is the most carefully built demo in the "observability of multi-agent
systems" space.** Its smartest move is not the courtroom wrapper but treating
communication topology as a controlled variable, with a blunt, useful result:
what decides collective-decision quality is not message volume but who may talk to
whom. Anyone building multi-agent orchestration can use that.

**But it is a research example, not a product.** No standalone entry point, no
users, no business model, and 19 HN points says the breakout is not happening yet.
Its value only materializes once ProtoLink gets adopted by real projects.

**The transferable rule: making the process replayable builds more trust than
making the output better.** In any system with multiple cooperating parties —
agents or otherwise — solve "can we replay what happened frame by frame" before
optimizing results. The repeated warning that "observed change is not causation"
is the same methodology.

## What to watch next

① Whether ProtoLink clears 1,000 stars in three months — whether the example can
pull the framework along
② Whether the "controllable topology" result gets cited by independent papers or
production case studies
③ Whether any finance/healthcare company publicly adopts ProtoLink for traceable
agent systems

## What you can take from it

**Product logic**: in a multi-agent system, make "who may communicate with whom"
an explicitly configurable topology instead of letting every agent message freely.
Controlling the communication structure moves results more than adding agents —
that is the transferable conclusion straight from the experiment.

**Positioning language**: none. This is technical documentation and an experiment
report; there is nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Unproven.** The experimental insight is solid and the methodology is rigorous,
but this is a framework example rather than a product, with no users and no
business model. What is worth keeping is the methodology — replayable, comparable,
observations separated from causation. Come back in three months and check whether
ProtoLink actually gained traction.
