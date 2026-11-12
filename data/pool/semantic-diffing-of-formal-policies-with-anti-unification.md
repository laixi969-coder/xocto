---
slug: semantic-diffing-of-formal-policies-with-anti-unification
name: Semantic diffing of formal policies with anti-unification
builder: ''
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: false
url: https://aws.amazon.com/blogs/machine-learning/semantic-diffing-of-formal-policies-with-anti-unification/
canonical_url: https://aws.amazon.com/blogs/machine-learning/semantic-diffing-of-formal-policies-with-anti-unification
summary: When reviewing code, you start with a diff. You wouldn’t compare two 3,000-line files by eye
  and hope to spot every change. Formal policies can be even harder to compare because a textual diff
  often highlights syntactic changes that don’t affect meaning. Reorder two conjuncts, swap the arguments
  of an equality, or use an equivalent predicate, and much of the file might appear changed. A real change
  in behavior, such as an Or where the requirement says and , can get lost in that noise. A semantic diff
  shows what two policies have in common and where they disagree. The open source engine used in this
  post computes this diff using anti-unification , which finds a most specific common pattern for two
  expressions. Plotkin’s 1970 paper gives the classical formulation. The engine works over an e-graph,
  which keeps track of expressions known to be equal. We supply the algebraic laws and domain rules that
  justify those equalities, such as equating an external destination with one that isn’t internal. The
  result shows the shared parts once and keeps both versions of each differing part for review. If no
  differences remain, the policies are equivalent under those laws and rules. When the
first_seen: '2026-11-12T03:00:02Z'
last_seen: '2026-11-12T03:00:02Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/semantic-diffing-of-formal-policies-with-anti-unification/
  seen_at: '2026-11-12T03:00:02Z'
  metrics: {}
  kind: news
---

# Semantic diffing of formal policies with anti-unification

When reviewing code, you start with a diff. You wouldn’t compare two 3,000-line files by eye and hope to spot every change. Formal policies can be even harder to compare because a textual diff often highlights syntactic changes that don’t affect meaning. Reorder two conjuncts, swap the arguments of an equality, or use an equivalent predicate, and much of the file might appear changed. A real change in behavior, such as an Or where the requirement says and , can get lost in that noise. A semantic diff shows what two policies have in common and where they disagree. The open source engine used in this post computes this diff using anti-unification , which finds a most specific common pattern for two expressions. Plotkin’s 1970 paper gives the classical formulation. The engine works over an e-graph, which keeps track of expressions known to be equal. We supply the algebraic laws and domain rules that justify those equalities, such as equating an external destination with one that isn’t internal. The result shows the shared parts once and keeps both versions of each differing part for review. If no differences remain, the policies are equivalent under those laws and rules. When the

## 笔记


