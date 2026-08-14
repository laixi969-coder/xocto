---
slug: lumabri
name: Lumabri
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A peer-to-peer swarm of ordinary computers running very large MoE models —
your machine donates disk, another machine donates compute. Napster for LLMs.

## Who built it

GitHub user JustVugg (HN handle vforno), a solo developer. Apache-2.0, written in pure C.
Repository created 2026-08-04; 80 commits in ten days; 47 stars / 2 forks.

It is not a fresh start: the author first built Colibrì, a single-machine project
asking whether one ordinary computer can run a huge LLM (using the same MoE
sparse-activation trick). Lumabri moves that question from one machine to many.
The first HN post ("Show HN: Lumabri – What if LLMs worked like Napster?") drew
8 points and 10 comments. In the post the author says plainly: no datacenter,
no GPU cluster, built with whatever hardware he owns.

_Read: a classic solo extreme-engineering project, not a business. The real signal is
the two-step sequence — first prove a MoE can be run frugally on one machine, then ask
whether many ordinary machines can become one big machine. The question order is worth
more than the code._

## What it actually does

- **P2P weight distribution** → a tracker (index) + maintainer (byte-range manager) +
  `liblumibri.so` (an LD_PRELOAD shim that keeps a sparse local mirror and fails over
  when a peer drops)
- **Remote expert execution** → an `expert_node` holds the weights for a few MoE
  experts; other nodes send activations over the wire, the remote node computes and
  sends results back. **Weights never leave their home machine**
- **Latency countermeasures** → distance maps, nearest-replica-first, prefetch,
  replica failover
- **Two trust models** → an open swarm verifies with SHA-256 to prevent poisoning;
  an invite-only swarm gates access with `LUMABRI_TOKEN`; `LUMABRI_VERIFY` spot-checks
  expert calls on a second replica and demands byte-identical output
- **Transport security** → X25519 + ChaCha20, identity pinning, replay protection;
  the v2 protocol adds signed checkpoints, crash-safe mirrors, and connection gating

**The core claim is byte identity**: the README says remote execution has been verified
to produce byte-identical output to local execution on OLMoE, GLM, Inkling, Kimi K3,
and DeepSeek V4.

## What old behavior it replaces

Running a hundred-billion-parameter MoE model previously meant exactly one path:
rent or buy a GPU cluster big enough. Costed by the month, out of reach for most people.

Lumabri argues for two replacements:
- a LAN of ordinary machines standing in for "one big machine with huge VRAM/RAM"
  (or even replacing disk swap — the author measures 5.97 tok/s over LAN P2P expert
  execution versus 0.04 tok/s straight from disk, claiming ~149x);
- an internet-scale swarm of donated nodes standing in for cloud GPU services.

**What it does not replace should be stated plainly**: P2P distributed inference is
not a new problem. Projects like Petals worked at it for years without ever reaching
production. On HN, commenter "hazard" named the three fundamental issues — a single
consumer card can't even hold one expert's weights, cross-node activation transfer
slows each token to hundreds of milliseconds, and a P2P network has no reliable
anti-cheat except duplicate computation (SHA-256 hashes files, not computation
results). The README does not answer any of the three.

## Business model

**None.** Pure open-source experiment. No hosted service, no pricing page, no revenue path.

_Read: this question is premature — the project has not even reached the point of asking
it. The more interesting question is that if P2P inference ever works, the money form
would be incentives for node contributors (deposit-and-forfeit, like Bittensor), not
software licenses. Too early to discuss._

## Hard numbers

- **47 stars / 2 forks.** Created 2026-08-04, Apache-2.0, pure C
- HN post 8 points / 10 comments (a second post: 6 points / 0 comments) — low attention
- Author's own measurements: LAN P2P expert execution 5.97 tok/s vs 0.04 tok/s from disk;
  expert replication 10.5 vs 1.4 tok/s at 2ms/30ms latency; cold-mirror prefetch gains
  45-50%; chat client RSS at 1.04 GB
- Byte-identity claimed verified on: OLMoE, GLM, Inkling, Kimi K3, DeepSeek V4
- Team size, enterprise users: N/A (personal project)

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Genuine motivation (a natural extension of Colibrì), but one person with no datacenter limits what can be validated |
| Product insight | "Ship activations, not weights" is the right economy for MoE, and the Napster analogy explains it in one second; but it does not answer the three structural P2P problems |
| Execution quality | Full stack — encryption, signing, deterministic execution, DoS defenses, 80 commits in ten days. Serious engineering attitude |
| Timing | Too early, and path-dependent on an unproven assumption (strangers willing to run models for each other) |

## The call

**This is a hypothesis about AI model distribution, not a product.** Worth following,
but graded as a hypothesis.

Three points worth keeping:
- **The Napster analogy is not marketing.** The P2P scenarios that actually survived
  (file distribution, CDNs) are "verify-able content, read-heavy write-light" — MoE
  inference fits that shape. The analogy is more sound than it looks.
- **Byte identity is the most valuable technical claim.** It compresses "can I trust a
  peer?" into "if outputs differ, one side is lying," and with spot-checking it is one
  of the few executable designs in P2P inference.
- **The real reason this does not replace GPU clouds is not technical.** It is that
  peers have no SLA, no incentive, and no accountability. That answer lives in token
  economics, not cryptography.

**Why Unproven rather than Worth watching is straightforward**: low attention (8 HN
points), no business model, and none of the three structural problems addressed. But
if in three months it demonstrates usable speed across an internet-scale swarm, the
architecture notes deserve a careful read.

## What to watch next

① Whether any independent third party (not the author) reproduces the speed numbers at
real internet latency
② Whether any contributor incentive appears — P2P inference without incentives has never
run in production
③ Whether stars and community engagement pick up — if they do not, even the developer
community is signaling disbelief in the direction

## What you can take from it

**Product logic**: if you hold a compute-heavy task that is verify-able and
read-heavy/write-light, outsourcing computation to a network is worth a serious look —
cheaper than renting GPUs and cheap to verify. If your task is generative and
subjective, cross P2P outsourcing off the list; anti-cheat costs will eat the gains.

**Positioning language**: none. This is engineering documentation; nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Unproven — logged with a probation period.** A beautiful hypothesis, serious
engineering, and no product destiny. If P2P inference as a direction is falsified,
Lumabri is a high-quality technical notebook; if it is confirmed, this is the first
complete blueprint. Come back in three months against the three checks above.
