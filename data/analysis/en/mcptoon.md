---
slug: mcptoon
name: Mcptoon
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An MCP CLI client that compresses the tool manifest by ~90% before it ever reaches the
model — so an agent can hold 100 MCP servers without blowing out its context window.

## Who built it

GitHub user activeing123, a personal project. Apache-2.0, pure Python standard library,
zero third-party dependencies, ~50KB install. 309 tests. Repository created 2026-07-27,
now at v0.4.0.

_Read: this is someone who was educated by real bills. Every design choice points to a
firsthand pain — "my context got eaten by tool schemas" is something only people who
install too many MCP servers say. The README cites Anthropic, Cursor, and Latent Space
on schema bloat, which suggests the problem was studied thoroughly before any code._

## What it actually does

- **CLI mode, not a client library** → the agent just runs `mcptoon` commands; schemas
  live on disk in `~/.mcptoon/config.json`, and only the requested compact output ever
  enters context
- **TOON encoding** → a custom token-oriented format replaces JSON for tool
  definitions. Measured on 255 tools: JSON 90,804 tokens → slim 6,174 (−93%) →
  compact 117 (−100%)
- **Three-layer decoupling** → CLI (50KB, zero deps) + 23 server config templates
  (~1KB each) + real MCP servers (spawned on demand via npx only when called):
  100 configured servers = 0 resident processes
- **Agent self-service** → an agent can run `mcptoon add github ...` to attach a tool
  by itself, no human editing JSON config
- **Safety guards** → tool-poisoning detection (blocks injections like "ignore
  previous instructions"), credential-leak scanning (API keys / AWS keys / GitHub
  PATs never enter context), destructive commands (`delete`/`drop`/`purge`) blocked
  by default, and a 5-minute schema cache to skip `tools/list` round-trips
- **Cross-agent** → configure once, use from Claude Code / Codex / OpenCode / Cursor;
  `--format openai|openapi|mcp` exports the same tools to other stacks

## What old behavior it replaces

Two painful chores of configuring MCP for an agent, one replacement each:

**Hand-editing JSON config.** Adding a server to Claude Desktop meant editing
`claude_desktop_config.json`; a misquoted character could cost half an hour.
Now `mcptoon add fetch --stdio npx -y ...` is one command, and the agent can run it
itself.

**Context blown up by schemas.** Standard MCP clients load every tool schema into
context before work begins — 10 MCP servers (especially with browser tools) can eat
50,000–100,000 tokens, filling half a 128K window before a single question.
mcptoon moves the manifest off the context channel: the model sees compressed tool
names and call results only, so "adding more servers" flips from something to budget
for into something you just do.

## Business model

**Not disclosed.** Free and open source (`pip install mcptoon`). No hosted service,
no paid tier, no managed version.

_Read: the typical paths for a tool like this are either acquisition (becoming a
built-in capability of some client) or a hosted edition (tool discovery, audit,
team sharing). Neither is being walked yet. The problem with a pure open-source tool
is that being good does not directly become revenue._

## Hard numbers

- **139 stars / 4 forks.** Apache-2.0, zero deps, ~50KB, Python 3.10+
- HN 70 points / 43 comments (2026-08-12) — real discussion heat
- Author's measurements (255 tools): JSON 90,804 tokens; TOON 44,863 (−51%);
  mcptoon 35,735 (−61%); SLIM 6,174 (−93%); Compact 117 (−100%)
- Test scale: 309 tests; claims 255+ MCP tools, 23+ servers, 30K+ real calls exercised
- 24 config templates: fetch, github, exa, brave-search, firecrawl, filesystem,
  memory, sequential-thinking, sqlite, time, puppeteer, playwright, postgres, slack,
  notion, git, gitlab, tavily, google-maps, docker, aws, cloudflare, tmux, and more
- Team size, revenue: N/A (personal project, not disclosed)

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Pain fed by real usage; the depth of the README's problem analysis says this is not hype-chasing |
| Product insight | Identified the right problem (schema bloat is MCP's known soft spot) and gave a root fix (move it out of context) rather than a palliative |
| Execution quality | Zero deps, 50KB, 309 tests — clean engineering; but all performance numbers are self-measured and need independent reproduction |
| Timing | Good. MCP is booming in 2026, schema bloat is scaling with it, and token-saving is becoming a category of its own |

## The call

**This is the most thorough fix yet for MCP's context problem, and worth watching.**
Others optimize the schema definition itself (shorter descriptions); mcptoon moves the
whole manifest off the context channel and passes only what a call needs, in a compact
format. Different direction, much larger effect.

**A transferable judgment: token cost is turning into a real line item, and any
token-saving tool will become a category.** Today's savers target agents; the next
layer will target platforms (gateways, caches), then business logic. mcptoon is on
layer one, and for an individual tool the ceiling of layer one is "being absorbed."

**Three reservations**: the benchmarks are all self-measured and the TOON token
savings need independent reproduction; of the 43 HN comments I did not read each one,
so the heat may overstate consensus; and with no business model, whether the author's
motivation survives three years is an open question.

## What to watch next

① Whether stars pass 500 in three months — the MCP official spec and every client are
also adding lazy-loading and compaction, so the window for an external tool is limited
② Whether a mainstream client (Claude Code / Cursor / OpenCode) absorbs it as a
built-in — being absorbed is the best outcome for this kind of tool
③ Whether any independent third party reproduces the token-savings numbers

## What you can take from it

**Product logic**: when your product depends on an input that inevitably grows (tool
manifests, rule files, context), do not only compress it — consider moving the whole
thing out of the main channel and fetching on demand. Turning "resident" into
"on-demand" often saves far more than format optimization.

**Positioning language**: the README's benchmark table — run the same data through
five formats and list each saving percentage — is a transferable way to show off.
"How much you save" must be precise down to the token count.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching, but commercialization is undecided.** The problem is well-aimed,
the fix is aggressive, the engineering is clean, and the 70-point HN thread shows real
resonance among developers. But it is a zero-dependency open-source personal tool whose
ceiling is absorption by a mainstream client, not independent scale. Come back in three
months against the three checks above.
