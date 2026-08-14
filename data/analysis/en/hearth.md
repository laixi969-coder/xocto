---
slug: hearth
name: Hearth
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A shared workspace for a household — plans, notes, schedules, and people all in one
place, with an agent that reads that context and can build small apps in place and run
them there.

## Who built it

jmtulloss (Jonathan Tullis, Retool co-founder) built it for his own family. It sits on
Playground, a library they are developing for building collaborative AI coding
harnesses — primitives being synchronized files, agents, people, app code sandboxing,
and a policy layer. Hearth is the family-scale example; the same library is being used
for Bear, a product for construction projects (bear.build). Site: ourhearth.ai.

_Read: when a Retool co-founder builds a personal project, the signal is that he is
testing whether "agents build their own tools" works as a paradigm — family is just the
smallest possible test bed, and the commercial target is construction._

## What it actually does

- **Shared family workspace** → plans, notes, schedules, people, and recurring family
  rituals, synced across every device
- **Contextual agent** → reads all of that and works across it, "kind of like a shared
  Obsidian with an agent"
- **Agent-built apps** → generates small apps on top of the family's notes and runs
  them inside the same workspace; calendar and travel apps are the examples
- **Tools as permissions** → IoT devices connect through an API-token proxy, so the
  agent can call the device without holding the token
- **Multi-member collaboration** → everyone shares the same data, and integrations are
  visible to the whole household
- **Explicitly beta**, with the author recommending you keep sensitive data out until
  the source is out and stable; open-sourcing is planned

## What old behavior it replaces

Household logistics are scattered across three or four tools: plans in a group chat,
calendars on individual phones, reminders on the fridge, a shared spreadsheet. The
information is fragmented, no one can see the whole family's arrangement at a glance,
and syncing is done by hand.

Hearth collects plans, notes, and schedules into one shared space, then lets an agent
consume that context — a "second brain for the whole household," replacing "family info
scattered everywhere, manually reconciled every time." The real increment is the agent:
it does not just store, it actively produces tools inside that context.

## Business model

**Pricing not disclosed.** Beta, with open-sourcing planned. At the company level, the
same stack is going into Bear (construction), and the family product has no business
model information of any kind.

_Read: the family use case cannot plausibly be the revenue source; Hearth is more like
walking advertising for the Playground library. The real commercial logic is Bear —
selling "agents that build their own tools" to construction firms is the old
construction-digitization story with a new engine._

## Hard numbers

- **HN Show HN: 8 points / 3 comments** (2026-08-13). Very little traction
- **Not open-sourced**: no source released yet, so no star/fork data
- A Home Assistant example app already exists at github.com/bearbuild/hearth-apps
- Users and pricing: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | A Retool co-founder building the family tool he eats his own product with. Fit is high |
| Product insight | "An agent that builds its own tools inside private context" is a smart direction, but family willingness to pay is doubtful |
| Execution quality | Sandboxing, least privilege, and synchronized files are designed in — but nothing is verifiable until it is open-sourced |
| Timing | Home automation is ramping, but consumer education cost for "build your own app" is extremely high |

## The call

**The sentence worth remembering: an agent should build its own tools where it can read
the context.** Most agent products today draw a boundary at "pick from a fixed toolset";
Hearth's direction is an agent generating its own tools and UI directly on top of user
data. That is the next layer of abstraction for agent applications, and family, company,
and construction site are just three different data scenarios.

**But 8 points and 3 comments means it has not left the author's backyard.** There is
one promise and one test bed: the promise is "open source soon," the test bed is his own
household. The most honest piece of evidence is the line "don't put anything too
sensitive in there until the source is out and stable" — the author himself is not sure
the isolation design holds.

**Family is a clever choice that does not pay.** Family was chosen because context
density is high, privacy boundaries are real, and the users are non-technical — the
smallest complete test environment. But consumers will not pay for "the agent builds me
a calendar app" — they struggle with the concept itself. The commercial story is Bear,
not Hearth.

**"Tools as permissions" deserves its own note.** A proxy that lets the agent call
devices without ever touching the token is a rare clean pattern in agent permission
design.

## What to watch next

① Whether the source actually ships as promised — if it does not, this is marketing copy
② Retention of the "agent-built apps" in a real household — the author says the family
uses it, but there is no data
③ Whether Bear (the construction edition) publishes prices and customers — that is the
commercial truth

## What you can take from it

**Product logic**: "agents write their own tools, then use those tools" is the next
layer of abstraction for agent applications. If you build an agent product, treat
"generating its own UI/tools on top of user data" as a capability, not a feature —
family, company, and site are just three data scenarios. A minimal test environment
needs: high context density, real privacy boundaries, and users who do not require
technical skill.

**Positioning language**: none. The HN post is a personal intro; nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Unproven.** The concept is sharp and the provenance is credible, but with 8 points,
no source, and no pricing, every commitment points to the future. Come back against the
three checks above.
