---
slug: dsh-genui
name: dsh-genui
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

Giving an agent's replies a face: the model writes a JSON block straight into its answer, the browser renders it as clickable cards, charts, forms, and quizzes, and clicking one sends an action back to the model to keep iterating. The text is still there; the UI is already alive.

## Who built it

Maintained by the omdsh-dev org, author taekchef (same GitHub handle), same org as dsh-better-sidebar. Repo created 2026-08-13, MIT, TypeScript, open-sourced at 0.8.0, 70 commits, going from 0.2 to 0.8 within a week — an extremely dense release cadence.

_Read: the same org shipping both a sidebar and GenUI means it is betting on "thickening DSH's interaction layer." This org plays the UI layer, not the model layer — a well-chosen position in an everything-is-a-plugin ecosystem._

## What it actually does

- **Reply as UI** → the model writes JSON inside a `dsh-ui` fence; components stream in as the reply is generated, no waiting for the full message
- **35 component types** → cards, tables, charts, forms, tabs, collapsible panels, file trees, timelines, diff, mermaid, 3D scenes
- **Interaction loop** → buttons/switches/inputs carry an action back to the model; the model updates the UI; same-name actions are debounced at 300ms
- **Local-first** → scoring, validation, expand/collapse happen in the browser without a model round trip; quiz answers are graded locally at zero token cost
- **Whitelist security** → components render from a whitelist, the model cannot inject HTML/scripts; function expressions go through a standalone parser, never eval
- **State persistence** → saved per session + content fingerprint, restored on reload, LRU capped at 200 blocks
- **Dual-channel rendering** → new DSH builds use the official fence-registry streaming pipeline; original/older DSH builds fall back to a DOM channel that mounts itself, streaming since 0.7.2
- **Zero intrusion** → in an environment without the plugin, a fence is just a code block: no errors, no session pollution

**What it deliberately does not do**: no cross-session state persistence, no MCP adapter, no standalone gallery page, no i18n — the roadmap gives a stated reason for each. The boundary is disciplined: it only solves "UI growing inside answers," not "UI living outside the conversation."

## What old behavior it replaces

Getting a visual result out of an agent used to be "text plus human hauling": the model hands you an ASCII table or markdown; if you want a chart you copy the data into Excel or a chart site, or ask the agent to write a script and run it. Seeing a result took 3-5 minutes and two or three round trips. Claude Artifacts and ChatGPT Canvas brought interactive previews into the mainstream, but they open a separate canvas and most of what they render is static.

genui replaces that hauling chain and goes one step further: the UI renders directly in the reply stream, and the components are clickable — click a button, the action returns to the model, the model changes the UI. It is not a DSH port of Artifacts; it upgrades "generation as interaction" from rendering static results to rendering a programmable surface.

## Business model

**Not disclosed.** MIT, free on npm, no pricing page, no hosted service, no sponsorship.

_Read: same as the rest of the ecosystem — build volume first. Its only genuinely valuable asset is the protocol for "how a model outputs structured UI." If DSH ever bakes in a similar fence protocol, this protocol becomes a de facto standard, which is the one path to monetization; right now there is no commercial activity at all._

## Hard numbers

- **54 stars / 3 forks / 1 open issue** (GitHub API, 2026-08-14)
- Created 2026-08-13, 70 commits, 0.8.0 first open-source release, 0.2→0.8 in a week
- 35 component types; renderer ~110KB minified / 28KB gzipped
- ~200-800 tokens per fence; tree capped at 200 nodes / 8 levels; 300ms debounce
- 253-350 tests across versions (count shifted during evolution), plus device e2e (needs DEEPSEEK_API_KEY)
- Users, downloads, team: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | An active DSH ecosystem contributor (two UI plugins from the same org); knows the problem space |
| Product insight | Got "generation as interaction" — UI whitelist plus action callback is the safe, token-cheap way for a model to generate UI today |
| Execution quality | Dual-channel rendering across new and old DSH, local-first, no eval, the largest test suite in this batch — serious engineering |
| Timing | Perfect: Artifacts just taught the market that agent output can carry UI, and DSH happens to lack exactly this; but 54 stars means the market has not voted yet |

## The call

**The only plugin of the six betting on a future interaction paradigm — and the one with the least evidence.**

Its bet is specific: agent output will evolve from "text plus code blocks" to "structured UI," and the safe way for a model to generate UI is a component whitelist plus local-first state plus an action callback. The design logic holds — letting a model emit freeform HTML is an accident waiting to happen, whitelisting is the only realistic path; and grading state locally instead of burning tokens is a direct contribution to AI product margin.

**Transferable rule: for anything a model generates, define the whitelist first, then talk about freedom.** And: for interactive components, every "state decision" runs locally; only "when new information is needed" does it go back to the model. That is the generic move for pushing the marginal cost of generative UI toward zero.

**But today it is a 54-star plugin.** No user cases, no enterprise validation, and Claude/OpenAI are already doing the same class of thing (Artifacts, Canvas), with DSH theoretically able to bake it in. As a paradigm proof it is valuable; as a product it has not stood up.

## What to watch next

① Whether stars pass a thousand in three months — a signal that DSH's official plugin recommendations are lifting it
② Whether official DSH ships its own fence rendering — baking it in kills the plugin while validating its protocol judgment
③ Whether real users publish "agent-generated UI doing work" cases — the only hard evidence that the paradigm holds

## What you can take from it

**Product logic**: any generative-AI product that wants models to output structured interfaces should copy this security design wholesale: whitelist-based component rendering + standalone parser (no eval) + local-first state + action callback to the model. The combination solves security (the model cannot inject scripts), cost (state decisions burn no tokens), and experience (components are clickable) in one move.

**Positioning language**: none. The README is engineering documentation.

**Pricing structure**: none. Not disclosed.

## Verdict

**Unproven.** The sexiest paradigm and the thinnest evidence in this batch. If "agents generating interactive UI" really is the next interaction paradigm, its protocol design is worth copying directly; but as a product it has not collected a single market vote. Remember its mechanism, not its star count.
