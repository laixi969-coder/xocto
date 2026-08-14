---
slug: the-new-firecrawl-mcp
name: The new Firecrawl MCP
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Firecrawl's official new MCP server: the whole web stack — search, scrape, parse,
crawl, interact, and autonomous research — exposed as tools any MCP client can call,
and already the default web route for Claude Code, Codex, and Cursor.

## Who built it

Firecrawl, officially (formerly Mendable, YC S22), co-founded by Nicolas Silberstein
Camara, Caleb Peffer, and Eric Ciarla (the pool lists Eric Ciarla as builder).
Mendable started as AI chat for documentation, then pivoted to "web to AI data"
infrastructure.

_Read: this is the closest thing the agent-era data layer has to a default. A small
documentation-chat company pivoted into a "web data API" and hit 350K registered
developers in two years by capturing one need every agent team cannot avoid: getting
clean, live web content into a model._

## What it actually does

- **firecrawl_search**: live search returning full page content (not just links), with
  time filters
- **firecrawl_scrape**: any URL to clean Markdown or structured JSON, including
  JS-heavy pages
- **firecrawl_parse**: PDFs and DOCX into text
- **firecrawl_crawl / map**: async whole-site crawling / site structure discovery
- **firecrawl_interact**: click, fill forms, log in, navigate — then scrape
- **firecrawl_agent**: an autonomous research agent that plans its own browsing,
  gathers from multiple sources, and returns structured results
- **Three access modes**: keyless (IP-rate-limited trial), OAuth (interactive
  clients), and API key (unattended)

## What old behavior it replaces

Making an AI read the web used to mean writing your own scraper (BeautifulSoup/Scrapy
do not run JS; Puppeteer/Playwright means maintaining a browser-automation stack) or
stuffing whole HTML pages into the model and wasting tokens. Worse, each MCP client
needed its own glue code. Firecrawl MCP turns the full find → extract → clean → use
loop into standard tools behind one configuration. It replaces "every agent team
maintains its own scraping infrastructure" — which is exactly why client vendors are
happy to route web tasks to it by default: building your own beats losing to the
default only if the default is bad, and this one is good.

## Business model

SaaS priced by credits: Free $0 (1,000 credits/mo), Hobby $16, Standard $83, Growth
$333, Scale $599, Enterprise custom. The open-source core (AGPL-3.0) is self-hostable,
but the anti-bot engine, Fire Engine, is closed — open source for traction, closed
engine for margin.

## Hard numbers

- GitHub firecrawl/firecrawl at roughly 100-110K stars (48K in August 2025, doubled
  within a year)
- Funding: $14.5M Series A (2025-08-19, led by Nexus Venture Partners, with YC, Zapier,
  and Shopify CEO Tobias Lütke participating); ~$16.2M total
- 350K+ registered developers; ~80K enterprise customers (Shopify, Apple, Canva,
  Zapier, Replit — company-reported)
- SDK downloads ~4.74M/month; company-reported scrape success rate of 96%
- Team of ~15

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The original Mendable team went from "AI reads docs" to "AI reads the web" — the same pain, extended |
| Product insight | Nailed the core contradiction — the web is built for humans, not models — and productized the dirty work as a standard API |
| Execution quality | Multi-engine racing, Rust hot paths, custom queue. Infrastructure-grade architecture, not a toy |
| Timing | Past "should we use it?" and into "who is the default?" — and free self-hosted rivals are closing in |

## The call

**The clearest current example of "agent-era infrastructure replaying early cloud."**
Three signals matter for you:

**First, whoever becomes the default takes everything.** Claude Code, Codex, and Cursor
route web tasks to the Firecrawl MCP by default, so for most developers it is "the
option you do not choose." Infrastructure products compete for the default slot, not
for feature counts — this is the inspiration note in the pool, made concrete.

**Second, the defense structure is worth copying.** AGPL open source blocks cloud
vendors from packaging it; the anti-bot Fire Engine stays closed (self-hosted builds
without it are visibly weaker at anti-bot); and the crawl cache flywheel (every scrape
enriches shared caches, lowering marginal cost) makes the cost curve hard to chase.
Open source for traction, closed key capability for margin, data flywheel for moat.

**Third, read the company's own benchmarks with a discount.** Official success rate:
96%. Third-party testing (Proxyway): 33.69%, and clearly weaker than Zyte (93%) in
enterprise-grade anti-bot scenarios. Self-reported benchmarks in infrastructure tend
toward optimism — run your own measurements before choosing.

**Risk surface**: Crawl4AI (~60K stars, fully free and self-hosted) is eating
cost-sensitive users, and AGPL gives some enterprise legal teams pause. The "default
slot" is far from locked.

## What to watch next

① Whether the keyless MCP endpoint discloses monthly call volume — a measure of how
deep v2 is actually used
② A second third-party anti-bot benchmark — the gap between the official 96% and
Proxyway's 33.69% needs a second measurement
③ How fast the free self-hosted rival (Crawl4AI) closes the gap — that decides whether
the default slot holds

## What you can take from it

**Product logic**: take a dirty job everyone does badly (web to LLM data), productize
it as one API plus one MCP server, and stop every agent team from reinventing it —
infrastructure products aim at the default slot, not at feature counts.

**Defense structure**: AGPL open-source core + closed key engine + shared cache
flywheel draws a clean line between open-source traction and commercial protection.

**Pricing structure**: credit-tiered, from 1,000 free credits up six steps to custom
enterprise — the standard usage-based ladder that grows free users into paying ones.

## Verdict

**Worth watching.** It is already validated infrastructure, not a bet — but the fight
for the default slot is far from over, with real anti-bot capability and free rivals
as the two open variables. For the reader, it is a live textbook on who captures the
infrastructure rent of the agent era.
