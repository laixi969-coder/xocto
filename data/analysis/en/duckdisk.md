---
slug: duckdisk
name: DuckDisk
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A macOS disk-space analyzer that swaps the pretty map for a dense table — local disks, OneDrive, Google Drive, and SSH servers scanned in one pass, with directory size, allocated space, parent percentage, item counts, and file-type totals all visible in a single tree.

## Who built it

Built by indie developer puppypi (credited that way at launch), open source under AGPL-3.0, built with Tauri + Rust + React with the pdu scanner under the hood. Launched at launch on August 9, 2026 with 108 upvotes, #12 of the day. Apple-notarized and on the Mac App Store.

_Read: a single developer, open source, on the App Store — the standard playbook for an indie Mac tool. The telling detail is running two distribution channels: the MAS build is sandbox-limited (local disks, OneDrive, SSH only), while the notarized direct build adds Google Drive and uses system SSH config. The author knew exactly where the App Store's limits are and kept an escape hatch._

## What it actually does

- **Table-first tree view** → the WizTree idea from Windows: one dense tree showing size, allocated space, parent percentage, file/folder counts, and file-type totals at once, with information persisting as you drill down
- **Local + cloud + remote in one pass** → local disks, OneDrive, Google Drive, and SSH paths under one interface
- **Cloud reads metadata only** → OneDrive via Microsoft Graph delta sync plus a local metadata cache, no file-content downloads; Google Drive via OAuth, also metadata-level
- **SSH reuses system config** → ~/.ssh/config and Keychain-stored passwords, no credentials duplicated inside the app
- **Safe cleanup** → cleanup is staged for review; cloud deletions go to Trash, permanent local/SSH deletion needs a second confirmation
- **Large-table performance** → virtualized rows, cached results, incremental refresh; multi-million-row trees stay responsive

**Why tables, not maps**: the author's PH post states the motivation plainly — "most macOS disk cleaners make a beautiful daisy map, but I still end up asking: which folder owns this space, how much is allocated, how many files are inside, and what types dominate?"

## What old behavior it replaces

Cleaning up a Mac used to mean one of two things:

**Graphical tools like DaisyDisk / OmniDiskSweeper** — every file drawn as colored arcs, great at showing "where the big stuff is" in one glance, but that is the only question they answer. Ask "how many files in this directory, what share by type, what percentage of my whole disk" and the graphics give you nothing.

**The command line** — `du`, `ncdu`, `find | xargs`: all the information, but stuck in a terminal, unfriendly to ordinary users, with no way to drill down a table and act on it.

DuckDisk occupies the gap between them: it ports the table-first experience WizTree proved on Windows to the Mac and merges local, cloud, and SSH into one tree. The insight is that graphical maps are for guessing, tables are for answering, and disk cleanup is fundamentally repeated answering.

## Business model

**Free.** AGPL-3.0 open source, no subscription, no IAP, no ads, available on both the App Store and GitHub Releases.

_Read: there is no visible plan to make money — no Pro tier, no sponsorship link, no "paid for teams" edition. Either a deliberate free-and-generous move to build reputation and stars, or simply not thought through. Indie Mac tools making a name free and riding that into the next product is a real pattern, but DuckDisk itself shows no commercialization signal yet._

## Hard numbers

- PH launch 2026-08-09: **108 upvotes, 3 comments, #12 of the day**
- AGPL-3.0, Tauri + Rust + React + pdu scanner
- Apple-notarized + Mac App Store, two distribution channels
- GitHub repo exists (README complete); star count not verified
- Downloads, users, revenue: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author was clearly bitten by "daisy maps don't answer my questions"; the pain is concrete |
| Product insight | "Tables vs. charts are two ways of thinking" is an accurate call; metadata-only cloud scans are a clever, cheap implementation choice |
| Execution quality | Virtualization, caching, incremental refresh, double confirmation — a personal project with professional-grade detail |
| Timing | Meh. Disk cleanup is an existing market with no tailwind; it has to win on product merit alone |

## The call

**This is a textbook case of "an old tool with a new way of presenting data is a new product" — and the ceiling is visible from day one.**

DuckDisk's product insight deserves to be isolated: **graphical maps and tables are two different kinds of thinking.** Maps answer "where is it big"; tables answer "what takes what, how much, and how do I drill in." The latter is naturally built for decisions, the former for demos. On "answering structured questions," it is genuinely better than every Mac graphical tool.

**The transferable rule: don't build an interface that shows the problem, build one that answers the questions.** Most analytics tools ship v1 as "draw the data," but the questions users actually ask are structured — which, how much, what percentage, compared to what. List the five concrete questions users will ask, then decide table or chart from that, instead of defaulting to a pretty shape.

**The ceiling**: disk cleanup is low-frequency, free, and educated by the OS's own tooling. No network effects, no ecosystem, no data moat — a cheaper or prettier competitor can take the users away. Its value is less the product itself and more what it demonstrates: how complete a product a solo developer can ship with one toolchain (Tauri + Rust + open source + MAS). For anyone thinking of making Mac tools themselves, that demonstration is worth more than how much disk DuckDisk frees.

## What to watch next

① Star count and App Store rating/review volume in three months — the reputation-accumulation speed of a free tool
② Whether a paid Pro tier appears (multi-cloud accounts, report export) — tells you if "free" is strategy or an afterthought
③ Whether it gets picked up by Setapp or a third-party Mac tool bundle — the common indie-monetization path

## What you can take from it

**Product logic**: for any analysis tool, write down a "questions users will ask" list first, then answer each one with the right data form. DuckDisk's whole table is an answer set to five questions (who owns the space, what's allocated, what percentage of parent, how many files, what types) — the table is not an aesthetic choice but the result of maximizing answer density.

**Positioning language**: the author's first-person pain statement — "I still end up asking: which folder owns this space?" — reads more honest than any feature list. Your own pain plus your solution is the most effective opening for an indie tool launch.

**Pricing structure**: none. Free and open source; no commercial plans disclosed.

## Verdict

**Worth watching.** Clear product insight, complete engineering, and a solid free-and-open-source reputation path — but it is an existing-market tool with no commercialization signal. Judge it half on the tool, half on the solo-developer demonstration; revisit in three months against the three checks above.
