---
slug: qm
name: qm
verdict: Strong pick
analyzed_at: 2026-08-13
---

## What it is in one line

Not another company-wide ChatGPT, but an agent scoped per person: every employee gets an
isolated workspace, and in shared channels everyone still drives the same one.

## Who built it

Y Combinator's own engineering team (`yc-software/qm`, MIT). The product runs at
qm.ycombinator.com. They used it internally first and open-sourced it after.

_Read: YC coordinates thousands of portfolio companies, hundreds of partners, and a pile of
internal process every day. "Get the whole company onto one agent" is a more real pain for
them than for most startups. Used-in-house-first is more credible than any pitch deck._

## What it actually does

- **A scope per person** → memory, files, keychain view, permissions, crons, and sandbox are
  separate for each employee and never bleed into each other
- **One identity across Slack and web** → what you configure in Slack is what you get on the web
- **Collaboration in channels** → beyond private workspaces, channels, group messages, and
  projects each carry their own memory and permissions
- **Swap the harness, keep the platform** → Pi, OpenCode, Codex, and Claude Code all drive the
  same core, so a deployment is not tied to one vendor
- **Work while nobody watches** → crons and watches run in the background
- **Admins keep control** → org-level config, a security posture, and which harnesses and
  models are allowed

**What it deliberately does not do**: it is not a general assistant for individuals. The whole
design assumes a company with many people in it. Alone, you carry the complexity for nothing.

## What old behavior it replaces

Until now a company that wanted AI in real work had two options, both awkward:

- **Everyone gets their own account.** Memory is not shared, material is scattered, permissions
  are uncontrollable, and nobody dares wire it into an internal system.
- **IT runs one shared bot.** Everyone shares one memory and one permission set. It cannot
  remember what *you* prefer, and no one will grant it real access, so it decays into an
  expensive search box.

qm fills in the missing middle: scope it per person instead of rationing permissions. Companies
have been taping this together themselves — several months of one engineer's time, per company.

## Business model

**Not disclosed.** MIT licensed, no pricing page, no hosted offering.

_Read: YC is not trying to make money here. The return is the standard. If thousands of
portfolio companies run the same agent substrate, YC owns the default position in that layer,
which is worth considerably more than subscription revenue. This is open source used the
classic way._

## Hard numbers

- **13,257 stars, 1,547 forks.** Repository created 2026-07-29 — fifteen days ago
- Forks are 11.7% of stars, a ratio that says people are deploying it, not bookmarking it
- TypeScript, MIT, Postgres for persistence, Fastify plus Slack Bolt plus Vite/Lit
- Team size and number of real deployments: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Built for their own use first. The pain is their own — the strongest form of fit |
| Product insight | Saw that "personal assistant" and "company system" are different animals, and solved it by scoping rather than by permissions |
| Execution quality | Already in production; every substrate (harness, session store, sandbox, memory) sits behind an interface |
| Timing | Right on. Companies just finished trying AI and are now asking how to put everyone on one thing |

## The call

**This is a textbook open-source land grab, aimed at the layer that is hardest to displace later.**

13,257 stars and 1,547 forks in fifteen days is extraordinary for enterprise-facing
infrastructure, which normally has no viral surface at all. There is one explanation: the
people adopting it were already waiting for it. The fork count carries the signal — an 11.7%
fork-to-star ratio means these are not applause, they are checkouts being configured for a
deployment.

**The transferable rule: when every company is taping the same thing together by hand, turning
the tape into an open-source product wins you the standard, not just users.** The barrier is not
technical — multi-tenant isolation, Slack integration, sandboxes are each unremarkable. The
barrier is who gets to be the default.

**The cost is just as direct.** Freedom to swap harnesses is bought with an abstraction layer,
and every additional harness adds a convention the core can no longer change. When one harness
makes a breaking change, qm either follows or loses those users. Worse, it only serves
companies with a lot of people in them; for a team under ten it is a net liability. The design
itself amputates the low end of the market.

**The bigger question**: does the agent-platform layer end up winner-take-all like Slack, or
does every company roll its own like CI? qm is betting on the former, and YC's position in the
ecosystem earns it the right to make that bet.

## What to watch next

① Whether the fork-to-star ratio holds above 10% in three months — a drop means the attention
was spectating, not deploying
② Whether any company outside the YC ecosystem says publicly that it runs this — this decides
whether it is an industry standard or an internal tool
③ Whether third parties contribute non-default harness adapters — that is the test of whether
"not tied to any vendor" is real

## What you can take from it

**Product logic**: if a multi-agent video workflow has to go from "you use it" to "the team uses
it," qm's scoping structure ports directly — one isolated workspace per person, one shared
skill library, admin-defined model allowlist. That combination is far simpler than building a
permission system and gets you the same outcome.

**Positioning language**: its opening line is "Most agents are designed like personal
assistants." Negate a premise everyone holds by default, then step into the space that opens
up. In a pitch this beats "we are better" — it says everyone has been pointed the wrong way.

**Pricing structure**: none. There is no pricing.

## Verdict

**Strong pick.** Not because the execution is exceptional, but because it demonstrates a path:
use open source to take the default position in a layer that is just now forming — a layer that
will certainly be collecting rent three years from now.
