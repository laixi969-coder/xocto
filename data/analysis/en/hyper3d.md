---
slug: hyper3d
name: Hyper3D
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Generate a production-ready 3D model in seconds from text or a single image: the
output is an asset with clean topology, UVs and PBR materials — not a rough mesh
needing cleanup — aimed at gaming, film, e-commerce and embodied-AI training.

## Who built it

Deemos Tech, Shanghai, China, a team in its mid-20s led by CTO Qixuan
Zhang. Hyper3D Rodin passed a million users shortly after its June 2024 launch; the
underlying generation technique, the CLAY paper, was nominated for the SIGGRAPH best
paper award; the company is an NVIDIA Inception member and worked with NVIDIA to make
the platform Sim-Ready on Omniverse / OpenUSD.

_Read: one of the best cases of academic results productized in the Chinese 3D
generation scene — the SIGGRAPH best-paper nomination is international technical
credibility, and they turned it into a product at roughly one new feature every nine
days for sixteen months. Tripo, Meshy and Luma are all doing the same thing; the
difference is the "production-ready" standard — peers output models, it outputs
assets that go straight into an engine._

## What it actually does

- **Image to 3D / Text to 3D** → images, sketches, multi-views or text prompts
  generate 3D assets with geometry, UVs and PBR materials built in
- **3D editing** → partial edits (change only a selected region), iterative
  splitting (break into editable parts), import .obj/.fbx/.glb for modification
- **Fine control** → 3D ControlNet with bounding-box, voxel and point-cloud
  guidance; Smart Low-Poly optimizes high-detail assets into lightweight meshes
- **Speed** → Gen-2.5 tiers: Extreme-Low ~4s, Low ~9s, Medium ~20s, High ~40s,
  Extreme-High ~80s; 10M+ polygons supported
- **Ecosystem tools** → AI avatar generation, AI textures, OmniCraft HDRI
  environments
- **Delivery formats** → GLB, FBX, OBJ, STL, USDZ; plugins for Blender, Unity,
  Unreal, Godot, Cinema 4D, Maya, Omniverse, 3ds Max
- **API and enterprise** → REST inference API; SSO/SAML, team management, shared
  asset workspaces

**What it deliberately does not do**: it is not a local modeling tool — generation
runs in the cloud, and it sells generation capability and assets, not a replacement
for everything an artist does in Blender. Even partial editing and splitting happen
in the cloud, not in a local workflow.

## What old behavior it replaces

**It replaces the most expensive step: hand-modeling in professional software.**
An engine-ready 3D asset — clean topology, UV unwrap, PBR textures — used to be days
of work by a 3D artist in Blender/Maya, requiring professional knowledge of topology
and UVs. AI generation compresses the pipeline to minutes and erases the "can you use
the software" barrier.

**It replaces the manual translation from 2D concept art to a usable model.**
The classic pipeline in games and film: a concept image → an artist builds to it →
topology cleanup → UV unwrap → texturing → check whether it deforms. All manual.
Rodin makes the model understand "what parts this object consists of," so a single
concept image produces an asset with structural understanding and the manual cleanup
steps disappear.

**For embodied-AI teams, it replaces the work of building simulation assets for
robot training.** Training a robot arm used to require hand-modeling and manually
assigning physical properties to every asset. The Sim-Ready feature exports assets
with physical attributes via OpenUSD straight into Isaac Sim — the company reports a
one-third trial-to-paid conversion since launch.

## Business model

**Freemium plus metered API plus enterprise.**
- Free tier: register and generate; a community gallery showcases work
- API: usage-metered, aimed at game and e-commerce batch production
- Enterprise: SSO, team management, shared assets, for studios and companies
- The site does not publish prices; payment lives inside the workspace

_Read: the model mirrors Meshy/Tripo — free trials build word-of-mouth, API and
enterprise make money, and the UGC game partnership (users generating pets and
objects inside a game with tens of millions of concurrent users) is a hidden revenue
channel: every user generation is an API call. This embedded, "eaten by someone
else's product" revenue model has a higher ceiling than standalone subscriptions._

## Hard numbers

- traffic board: 3.12M monthly visits, +134.62% MoM (2026-08), on the global growth and
  overseas leaderboards
- Passed one million users shortly after the June 2024 launch (NVIDIA blog)
- Roughly one new feature every nine days over sixteen months (media)
- Rodin Gen 1.5 (2025-04): 4B+ parameters; Rodin v2 (2025-10): 10B parameters,
  BANG architecture; Gen-2.5 is the current flagship
- Sim-Ready: one-third trial conversion since launch, tens of thousands of assets
  exported (NVIDIA blog)
- CLAY nominated for SIGGRAPH best paper; recognition at SIGGRAPH 2024 and 2025
- Funding, team size, ARR: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | An academic team productizing fast; SIGGRAPH backing plus a feature every nine days — strong fit |
| Product insight | "Production-ready" is the differentiator — peers output models, it outputs usable assets |
| Execution quality | 10B parameters, quad topology, PBR, ControlNet guidance — domestic first tier |
| Timing | 3D content demand (games, e-commerce, embodied AI) is exploding; generative 3D is at the threshold of scaled adoption |

## The call

**Worth watching — the +134% MoM needs decomposing, but the technical standing is
real.**

3.12M monthly visits at +134.62% MoM is likely a stack: the "4-second generation"
attention from Gen-2.5, traffic from the 10M-concurrent-user UGC game partnership,
and leaderboard placement inflating the count. The previous base was low (~1.33M),
so the absolute number is still in the millions. The real proof is whether next
month's MoM continues, not the single-month figure.

**Its technical narrative is credible**: a SIGGRAPH best-paper nomination, an
official NVIDIA blog endorsement and a million users stack into a story that is not
marketing-driven. The real gap in 3D generation is not "can it generate" but
"can what it generates be used" — is the topology right, are the UVs clean, can it
enter an animation or simulation pipeline. Making "production-ready" the product
standard is exactly where it sits apart from Meshy and Tripo.

**The open questions**: first, all commercial numbers (ARR, paying users, the
game-partnership revenue split) are undisclosed; second, the UGC game is one
customer — is the embedded channel replicable or a single-client dependency; third,
whether the free tier drifts into the classic "free to generate, paid to export"
pattern, which would erode creator goodwill.

## What to watch next

① Whether next month's MoM holds past +134% — real traction or a Gen-2.5 launch
spike
② A second public UGC/platform partnership — proving the embedded channel is
replicable
③ Any disclosure of API paying users or enterprise customers (game studios,
e-commerce) — the real commercial grade

## What you can take from it

**Product logic**: in generation tools, treat "production-ready" as a product
standard, not a slogan — users do not care how pretty the preview is; they care
whether the output drops into their pipeline. Post-generation editability (partial
editing, splitting, editable topology) is the dividing line between a demo and a
productivity tool.

**Business model (embedded)**: embed your capability inside someone else's product
(UGC games, e-commerce platforms) so every user generation is an API call. That
"eaten by another product" revenue model has a higher ceiling than standalone
subscriptions — provided your capability is cheap and fast enough that another
product is willing to put your generate button inside its own UI.

**Positioning language**: none. The site is standard product-page copy.

## Verdict

**Worth watching, commercial verification pending.** The technical standing is real
(SIGGRAPH, NVIDIA, a million users) and the "production-ready" differentiation
holds; the +134% MoM looks like a launch spike rather than a steady state. Write it
down, verify next month's MoM, and wait for commercial disclosure.
