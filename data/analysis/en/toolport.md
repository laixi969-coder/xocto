---
slug: toolport
name: Toolport
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Configure every MCP server once, share them across all your AI clients through one
local gateway — tools load on demand to save tokens, secrets stay in the OS keychain.

## Who built it

Independent developer "Tyler" (GitHub tsouth89, the launch platform @tsouth2), a one-person
project. First launched 2026-06-23 under the name "Conduit"; the third
launch in August 2026 hit daily rank #5 with 149 points, version v1.12.0. No funding,
relying on GitHub Sponsors. Site: toolport.app.

_Read: this is the most direct productization of "configuration complexity silently
kills adoption." Going from zero to v1.12 in two months, with a reproducible benchmark,
signed cross-platform installers, and near-daily commits — the execution puts it at
the top of its size class._

## What it actually does

- **Local MCP gateway**: configure each server once; Claude Desktop, Cursor, VS Code,
  Windsurf, Codex, and 29+ other clients share it
- **Lazy tool discovery**: instead of dumping every tool schema into context (three
  servers ≈ 24K tokens of fixed overhead per request), it exposes four searchable
  meta-tools and pulls definitions on demand; claims 74-91% token reduction at equal
  task success, with a public reproducible benchmark
- **Secret management**: API keys live in the OS keychain and are injected at runtime,
  never in config files
- **Integrity checking**: fingerprints each tool definition with a hash; if a server
  silently changes a tool, Toolport flags it as a potential rug pull / tool poisoning
- **Governance**: per-agent scoping and toggles, human approval for destructive calls,
  audit logging, latency monitoring
- **Cross-platform**: Tauri/React desktop app with a Rust gateway binary, plus a
  headless Docker gateway

## What old behavior it replaces

Two things. **"Flat tool loading"**: every MCP server used to send its full tool list
to the model on every request, so the fixed token overhead grew with every server you
added. Meta-tool on-demand discovery replaces the once-per-request full dump.

**"Configure every client separately"**: the same MCP config plus plaintext API keys
used to be pasted into each AI client individually; changing one server meant syncing N
files and always missing one. Toolport replaces multi-client config drift — set up
once, available everywhere.

## Business model

Open-source core (MIT, local app free) plus a Toolport for Teams subscription: free up
to 5 people, then $39/month (for up to 5) plus $12/person/month, identical hosted or
self-hosted, ~$390/year annual. Paying customers: none disclosed (third-party research
found zero).

_Read: free for individuals to build reputation, team subscription selling governance
(shared config, per-member local keys) — the smallest viable business loop for a solo
builder. But a $39/month team tier competing against free MCP gateways from Microsoft,
Docker, IBM, and Kong is a thin lane._

## Hard numbers

- the launch platform August 2026 launch: daily rank #5, 149 points (third launch; first was
  2026-06-23 as Conduit)
- Version v1.12.0, near-daily commits, public reproducible token benchmark (claims
  74-91% reduction)
- 29+ MCP clients supported (35 integrations per the vendor)
- Pricing $39/month (up to 5) + $12/person/month
- Paying customers, funding, team size (appears to be 1): not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The founder's real identity is barely verifiable (just "Tyler"); the product has to prove the pain itself |
| Product insight | Turned a quantifiable waste — tool definitions eating context — into a headline feature backed by a reproducible measurement |
| Execution quality | Cross-platform installers, Rust gateway, keychain secrets, integrity fingerprints, near-daily commits. Solid |
| Timing | The core capability is being absorbed natively by clients (Claude Code already lazy-loads MCP schemas) — the window may be one or two release cycles |

## The call

**Among this batch, the strongest technical execution and the weakest business
proposition.** Three things worth keeping:

**First, turn quantifiable waste into a headline.** "Every request wastes 24K tokens
on tool definitions" is a number every developer gets instantly, and it ships with a
public reproducible benchmark. Infrastructure tools persuade through measurement, not
slogans. Anyone building efficiency tooling should copy this.

**Second, the security design is a reference implementation for MCP gateways.**
Fingerprinting tool definitions (alert when a server changes a tool, guarding against
poisoning), human approval for destructive calls, secrets only in the keychain — this
whole set of defenses is portable to any product where agents call external tools.

**Third, the structural risk is the fatal one.** Lazy loading is being absorbed
natively by the clients — Claude Code already defers MCP schemas — and once every
client supports on-demand loading, the meta-tool differentiator is zero. Meanwhile
Microsoft, Docker, IBM, and Kong all ship free MCP gateways, so a solo developer is
asking for $39/month next to platform freebies. Its real value is closer to "the
pioneer's best practices": it assembled everything an MCP gateway should have in one
place. Treat it as a reference implementation to copy, not an investment.

## What to watch next

① Whether paying Teams customers appear (zero disclosed so far) — the only revenue
path
② Whether native MCP lazy loading ships across the three big clients (Claude Code /
Codex / Cursor) — when it does, this is over
③ GitHub stars and forks three months out — a measure of adoption as a reference
implementation

## What you can take from it

**Product logic**: find the fixed cost users burn on every request (tokens, config,
time), quantify it into a measurable promise ("save 74-91%"), and publish the
measurement method — efficiency tools persuade with reproducible data.

**Security design**: tool-definition hash fingerprints, human approval for destructive
calls, secrets that only ever live in the keychain — a portable defense set for any
"agent calls external tools" product.

**Pricing structure**: free open source for reputation, team subscription for
governance (shared config, per-member local keys) — the smallest viable business loop
for a solo builder, even if the future is doubtful.

## Verdict

**Worth watching, but hard to bet on.** The technology deserves copying; the business
model invites doubt — when platforms build the free version into their clients, an
independent gateway's window may be one or two release cycles. Check back in three
months against paying customers and client-side native loading.
