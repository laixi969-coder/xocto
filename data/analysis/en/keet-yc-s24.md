---
slug: keet-yc-s24
name: Keet (YC S24)
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An iOS learning app that generates a structured video course from any topic: it auto-builds a curriculum roadmap, gives each lesson a 3–4 minute explainer video (generated with Manim and Remotion) plus game-style quizzes, turning "learning on your own" into "someone else scheduled your course."

## Who built it

Zack Ashen and Tommy Tsai, YC S24, who met in a college linear-algebra class and spent four years taking classes together; both have Cornell CS backgrounds. Their original YC project was actually a web-agent API (letting AI agents access user accounts through APIs to replace brittle browser automation); they pivoted to this consumer course app. Currently in iOS TestFlight private beta.

_Read: a textbook "tools to consumer" case — the earlier agent-infrastructure work built engineering capability, and the course app bets on the same ability to turn open-ended internet activity into a predictable workflow._

## What it actually does

- **Generate a course on any topic** → enter a topic plus difficulty and depth preferences, get a roadmap of modules, lessons, and lectures
- **Explainer videos** → two pipelines: Manim for mathematical visualization, Remotion for Vox-style process animation and primary-source material
- **Reinforcement games** → multiple choice, ordering, connections, and swipe quizzes
- **Biglan-category style tuning** → it classifies the topic into hard-pure / hard-applied / soft-pure / soft-applied quadrants and adjusts how it picks examples (hard-pure seeks worked proofs and real cases; soft-pure seeks primary narratives and contrasting perspectives)
- **Intent questionnaire** → before generating it asks about difficulty, depth, and intent; a global prerequisite graph is planned so a CS major's course differs from a beginner's

## What old behavior it replaces

Two things.

First, **the "assemble your own curriculum" habit of self-learning**: like founder Zack learning coffee by piecing together YouTube videos, ChatGPT conversations, and books — the real barrier was never missing material, but nobody ordering it. Keet replaces "being your own curriculum designer."

Second, **course supply for long-tail topics**: a niche subject often has no Udemy course, or only unvetted self-shot videos. Keet makes "someone schedules your lessons" available instantly for any topic, replacing the sequencing and instructional-design function of traditional course producers.

_Read: it does not replace ChatGPT-style Q&A — GPT answers single questions but hands the responsibility of "learning a subject" back to the user. Keet sells order and structure; that is the essential difference from general assistants._

## Business model

Freemium, credit-based: TestFlight beta users get 3 free course generations (per the launch post), and further courses require credits whose price is unpublished.

_Read: charging per generation rather than per subscription directly tracks the cost structure (generating a video course is far more expensive than text Q&A) and directly tests the core consumer hypothesis — will people pay, before knowing the quality, for a custom course._

## Hard numbers

- HN launch post: 42 points, 44 comments
- YC S24 batch; two-person team, New York
- Original YC project was the agent API, since pivoted to the consumer app; YC standard deal is on the order of $500K ($125K for 7% + $375K)
- TestFlight private beta; 3 free course generations
- User count, retention, courses generated, credit pricing: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | They met over taking classes, and Zack has a concrete self-learning pain — the motivation is real |
| Product insight | "Sell the syllabus, not the Q&A" is right, and Biglan-category style tuning is an unusual level of care |
| Execution quality | The Manim + Remotion dual video pipeline is real engineering, not a wrapper |
| Timing | AI-generated courses is a crowded lane (YouLearn, Coursebox, NerdSip), and consumer retention is the life-or-death metric |

## The call

**The hardest part of "generated courses" is never generation; it is "worth finishing."** Keet is genuinely careful on the generation side — roadmaps, dual video pipelines, Biglan classification, intent questionnaires — which means it treats teaching quality as a product problem, not a content problem. But consumer learning lives and dies on retention, and retention depends on whether generated courses are accurate and get more accurate with use. It has zero public numbers on either.

**The transferable pattern: make "order" and "structure" the core selling point.** General AI assistants answer pointwise, but learning, projects, and any long process require sequence. Whoever takes on the responsibility of sequencing goes from "tool" to "service."

**Risks**: credit pricing is unpublished, so the unit economics are unknown; competitors are doing the same thing; and AI-generated courses have a credibility problem — polished video can mask inaccurate content, and learning products get abandoned the moment users catch an error.

## What to watch next

① Credit pricing and generation cost — "how much per generated course" determines whether the business model works
② Retention data: users' willingness to generate a second and third course (not public yet, but it is the number they most need to publish)
③ Whether they raise a post-YC round and whether the beta exits TestFlight

## What you can take from it

**Product logic**: for any "long process" product (learning, research, project management), make "sequencing for the user" an explicit selling point instead of single-point Q&A. Keet's course roadmap is the exemplar of "sequence as product."

**Content engineering**: divide video work by content type — Manim for precise math visualization, Remotion for narrative process animation. Anyone building tutorial or teaching products can copy this "tools split by content type" approach.

**Positioning language**: none. The website and launch post are feature descriptions; there is no commercial phrasing to steal.

## Verdict

**Worth watching, with the core metric still undisclosed.** Serious team, solid generation-side engineering, and the right call on direction (syllabus over Q&A) — but it is sitting on the consumer product's life-or-death question: retention. Credit pricing and retention data are the two numbers it must produce next.

