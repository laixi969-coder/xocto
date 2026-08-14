---
slug: relational-to-kv
name: Relational-to-KV
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

The craft of "how do I put a relational model on a KV engine like RocksDB/ToplingDB" — a skill
only storage experts have — packaged as a skill bundle for AI coding assistants (Cursor / Claude
Code / Codex): the agent generates key designs, encoding code, and engine configs by following
rules, instead of improvising.

## Who built it

rockeet (a GitHub account), MIT licensed, repository created 2026-08-10. The author is closely
tied to the ToplingDB ecosystem — ToplingDB is a derived fork of RocksDB maintained by the
Topling team, and the repo references and compiles companion sources such as topling-zip.

_Read: this is a "harden the pain you lived through into an AI skill" project. Blockchain teams
like Sui, Aptos, and NEAR hand-translate relational models into KV layouts for performance —
an architecture only affordable to companies with dedicated storage teams. The author wants to
make it reusable for ordinary teams._

## What it actually does

- **A seven-step flow** → inventory entities/relations → enumerate access patterns (point,
  prefix, range scans) → derive key spaces → assign logical namespaces → generate byte-order-safe
  encode/decode → map column families and engine options → review the contract
- **Four deliverables** → a Key Space Catalog, key schema plus C++ code, CF/engine configs
  (CF/Options for RocksDB, SidePlugin for ToplingDB), and a consistency/cleanup/migration plan
- **Multi-runtime** → built simultaneously as Cursor / Claude Code / Codex plugins or skills
- **Encoding conventions** → BytewiseComparator (memcmp order) by default; floats use the
  FoundationDB tuple-layer transform to preserve IEEE 754 totalOrder

**What it deliberately does not do**: it is not an SQL compatibility layer, not an ORM, not a
drop-in for arbitrary SQL, and it does not migrate data automatically. It only produces design
decisions and code; humans still own the business semantics and access-pattern choices.

## What old behavior it replaces

Two old roads, both expensive.

The first is using a SQL database (MySQL/TiDB and friends) and letting the relational engine
handle storage. That carries an "abstraction tax": to preserve SQL semantics, the underlying KV
access patterns are locked in, and you never get the performance dividend of designing keys
around access patterns. It is the default because it is cheap and nobody gets fired for it.

The second is hand-mapping relational models onto KV — the Sui, Aptos, NEAR, Solana route.
Best performance, but how to split the key space, define encodings, handle range deletes and
migrations, and hold consistency constraints together is all hand-designed. Only the few
companies with dedicated storage teams can afford it, each time a bespoke tens-of-thousands-of-
lines effort.

relational-to-kv replaces the "relying on expert memory and improvisation" part of the second
road: turning expert practice into rules and templates an agent can execute, so ordinary teams
can take that road with reviewable, portable designs.

## Business model

**None.** MIT, no hosting, no pricing.

_Read: a textbook "content infrastructure" project — the value is the rule set itself, not
software. If it validates, the author's real exit is likely services or enterprise support
around the ToplingDB ecosystem. No commercial movement yet._

## Hard numbers

- **2 stars, 0 forks.** Repository created 2026-08-10
- HN: 5 points, 0 comments
- A single commit (the initial commit is complete), MIT
- Includes tests: ToplingDB source compilation, memcmp encoding round-trips, ASan/UBSan builds
- Users and enterprise adoption: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Bound to the ToplingDB ecosystem; the author is a storage practitioner who can compile and validate a RocksDB-derived codebase — high fit |
| Product insight | "Encapsulate senior engineering experience as an agent skill" is a new direction, but the target market (teams building their own KV storage) is extremely narrow |
| Execution quality | Real tests and bilingual docs, not a slide deck; but the quality of generated code cannot be independently verified |
| Timing | Early and narrow. The need for KV storage design is real, but the paying scenario has not changed in a decade |

## The call

**This is a sample of "craft encapsulation in the AI era": turning a skill held by a few into a
rule set for agents.** The direction is new and worth studying for anyone building vertical
tools; but for this specific project, the market may not support a product.

**The transferable rule: judge a "skill encapsulation" project on three things — whether the
craft is scarce (yes), whether demand is high-frequency (no, selection is low-frequency), and
whether the expert will keep maintaining the rules (doubtful). Two out of three true leaves it
a content project.**

**Its biggest problem is the same disease of the category**: nothing backstops the correctness
of the agent's key design. Tests cover encoding correctness, not design correctness — a
wrongly-designed key space is useless no matter how correct the code is. The README leaves
"semantic and access-pattern choices" to humans, which keeps the hardest judgment with the very
expert the tool is meant to replace.

**HN's 5 points says the market is cold**: this is not a mass pain point. It will only ever
serve the very few teams that put data directly on KV engines.

## What to watch next

① Whether any team actually produces a production KV design with it and publishes the result
② Whether the rule set tracks RocksDB/ToplingDB versions — once the encoding conventions go
  stale, the skill becomes a liability
③ Whether Cursor/Claude officially list it in their skill marketplaces — listing would mean a
  platform vouches for its quality bar

## What you can take from it

**Product logic**: turning your team's most expensive tacit knowledge — senior engineers'
judgment — into executable rule documents plus templates is more useful than a training manual.
The test: can another person (or an agent) follow the rules to a reviewable result?

**Positioning language**: none. Engineering documentation; nothing to steal.

**Pricing structure**: none.

## Verdict

**Unproven, but remember the form.** The specific project lacks validation (2 stars, 5 points,
no users). The "skill encapsulation" pattern itself is worth watching — it may become a new
vehicle for distributing vertical-industry knowledge.
