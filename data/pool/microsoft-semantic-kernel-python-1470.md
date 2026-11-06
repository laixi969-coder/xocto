---
slug: microsoft-semantic-kernel-python-1470
name: 'microsoft/semantic-kernel: python-1.47.0'
builder: microsoft
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/microsoft/semantic-kernel/releases/tag/python-1.47.0
canonical_url: https://github.com/microsoft/semantic-kernel/releases/tag/python-1.47.0
summary: '## Python compatibility


  This release requires Python 3.11 or later. Python 3.10 support has been removed. Supported and tested
  Python versions are 3.11 through 3.14.


  Includes consolidated Python dependency updates and the bug fixes listed below.

  ## What''s Changed

  * .Net: Remove migrated .NET Milvus connector by @adamsitnik in https://github.com/microsoft/semantic-kernel/pull/14682

  * .Net: Bump Aspire.Azure.Search.Documents from 13.4.6 to 13.5.4 by @dependabot[bot] in https://github.com/microsoft/semantic-kernel/pull/14499

  * .Net: Bump Aspire.Hosting.Azure.CognitiveServices from 13.4.6 to 13.5.4 by @dependabot[bot] in https://github.com/microsoft/semantic-kernel/pull/14501

  * .Net: [BREAKING] Consolidate file access by @westey-m in https://github.com/microsoft/semantic-kernel/pull/14679

  * Python: preserve path case in OpenAPI allowed URLs by @eavanvalkenburg in https://github.com/microsoft/semantic-kernel/pull/14693

  * Python: normalize OpenAPI allowlist paths before prefix match by @mangeshraut712 in https://github.com/microsoft/semantic-kernel/pull/14668

  * Python: Batch Google AI embedding requests to the 100-input limit by @pcbeingused333 in https://github.com/microsoft/semantic-kernel/pull/14700

  * Python: fix Mistral AI chat completion crash on unknown finish reasons (model_length) by @pcbeingused333
  in https://github.com/microsoft/semantic-kernel/pull/14696

  * Python: fix(sql_server): validate collection field types before table creation by @BlueX888 in https://github.com/microsoft/semantic-kernel/pull/14697

  * Python: Fix Mistral AI seed setting being rejected by the SDK by @pcbeingused333 in https://github.com/microsoft/semantic-kernel/pull/14677

  * Python: keep empty tool results through the prompt round trip by @iamthehimansh in https://github.com/microsoft/semantic-kernel/pull/14686

  * Python: fix(sqlserver): handle None and boolean expressions in SqlServerCollection lambda parser by
  @wasim-builds in https://github.com/microsoft/semantic-kernel/pull/14687

  * Python: Respect optional MCP prompt arguments by @jaeminbird in https://github.com/microsoft/semantic-kernel/pull/14676

  * Python: count Gemini thinking tokens in the usage of Google AI completions by @pcbeingused333 in https://github.com/microsoft/semantic-kernel/pull/14671

  * Python: fix(python): preserve non-adjacent tool pairs during history truncation by @linhongyu510 in
  https://github.com/microsoft/semantic-kernel/pull/14658

  * Python: fix(python): wire ChatHistoryReducer into ChatCompletionAgent invocation (#12303) by @sparkysolutions10-pixel
  in https://github.com/microsoft/semantic-kernel/pull/14607

  * Python: Fix Handlebars messages helper ignoring its argument by @VANDRANKI in https://github.com/microsoft/semantic-kernel/pull/14537

  * Python: fix(python/redis): restore vector search broken by redisvl>=0.5 API change and KeyError on
  include_vectors=False by @PatrickRibbsaeter in https://github.com/microsoft/semantic-kernel/pull/14278

  * Python: Handle empty chat message function results by @lprnmns in https://github.com/microsoft/semantic-kernel/pull/14375

  * Python: Exclude ClassVar annotations from generated JSON schemas by @Pushpak731 in https://github.com/microsoft/semantic-kernel/pull/14528

  * Python: Propagate MCP initialization failures by @lxingy3 in https://github.com/microsoft/semantic-kernel/pull/14095

  * Python: Fix VolatileMemoryStore.get_nearest_matches on an empty collection by @VANDRANKI in https://github.com/microsoft/semantic-kernel/pull/14536

  * .Net: docs: fix 20 broken sample links in GettingStartedWithAgents README by @leom1919 in https://github.com/microsoft/semantic-kernel/pull/14699

  * .Net: docs: fix dead links after planner removal and MEVD code migration by @leom1919 in https://github.com/microsoft/semantic-kernel/pull/14715

  * Python: Drop 3.10 support and expand CI coverage through 3.14 by @eavanvalkenburg in https://github.com/microsoft/semantic-kernel/pull/14708

  * Python: Build an array schema for variadic tuple parameters by @anishmehta24 in https://github.com/microsoft/semantic-kernel/pull/14692

  * Python: docs(python): fix broken sample links in agents READMEs by @pratikgx in https://github.com/microsoft/semantic-kernel/pull/14703

  * Python: Send the NVIDIA nvext setting in extra_body by @codewithfourtix in https://github.com/microsoft/semantic-kernel/pull/14698

  * Python: Use storage_name for hybrid search fields and vector queries (#14684) by @Fire162 in https://github.com/microsoft/semantic-kernel/pull/14688

  * Python: close native generators when stream invocations end by @DiadkoShmek in https://github.com/microsoft/semantic-kernel/pull/14701

  * Python: Fix OracleCollection search with multiple filters by @VANDRANKI in https://github.com/microsoft/semantic-kernel/pull/14541

  * .Net: Bind validated HTTP addresses to connections by @rogerbarreto in https://github.com/microsoft/semantic-kernel/pull/14719

  * .Net: Harden structured data mutation boundaries by @rogerbarreto in https://github.com/microsoft/semantic-kernel/pull/14718

  * Python: Prepare 1.47.0 release and consolidate dependency updates by @eavanvalkenburg in https://github.com/microsoft/semantic-kernel/pull/14720


  ## New Contributors

  * @mangeshraut712 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14668

  * @BlueX888 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14697

  * @iamthehimansh made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14686

  * @jaeminbird made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14676

  * @linhongyu510 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14658

  * @sparkysolutions10-pixel made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14607

  * @PatrickRibbsaeter made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14278

  * @lprnmns made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14375

  * @Pushpak731 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14528

  * @lxingy3 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14095

  * @leom1919 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14699

  * @anishmehta24 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14692

  * @pratikgx made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14703

  * @codewithfourtix made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14698

  * @DiadkoShmek made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14701


  **Full Changelog**: https://github.com/microsoft/semantic-kernel/compare/python-1.46.0...python-1.47.0'
first_seen: '2026-11-06T02:26:55Z'
last_seen: '2026-11-06T02:26:55Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/microsoft/semantic-kernel/releases/tag/python-1.47.0
  seen_at: '2026-11-06T02:26:55Z'
  metrics:
    reactions: 1
  kind: news
---

# microsoft/semantic-kernel: python-1.47.0

## Python compatibility

This release requires Python 3.11 or later. Python 3.10 support has been removed. Supported and tested Python versions are 3.11 through 3.14.

Includes consolidated Python dependency updates and the bug fixes listed below.
## What's Changed
* .Net: Remove migrated .NET Milvus connector by @adamsitnik in https://github.com/microsoft/semantic-kernel/pull/14682
* .Net: Bump Aspire.Azure.Search.Documents from 13.4.6 to 13.5.4 by @dependabot[bot] in https://github.com/microsoft/semantic-kernel/pull/14499
* .Net: Bump Aspire.Hosting.Azure.CognitiveServices from 13.4.6 to 13.5.4 by @dependabot[bot] in https://github.com/microsoft/semantic-kernel/pull/14501
* .Net: [BREAKING] Consolidate file access by @westey-m in https://github.com/microsoft/semantic-kernel/pull/14679
* Python: preserve path case in OpenAPI allowed URLs by @eavanvalkenburg in https://github.com/microsoft/semantic-kernel/pull/14693
* Python: normalize OpenAPI allowlist paths before prefix match by @mangeshraut712 in https://github.com/microsoft/semantic-kernel/pull/14668
* Python: Batch Google AI embedding requests to the 100-input limit by @pcbeingused333 in https://github.com/microsoft/semantic-kernel/pull/14700
* Python: fix Mistral AI chat completion crash on unknown finish reasons (model_length) by @pcbeingused333 in https://github.com/microsoft/semantic-kernel/pull/14696
* Python: fix(sql_server): validate collection field types before table creation by @BlueX888 in https://github.com/microsoft/semantic-kernel/pull/14697
* Python: Fix Mistral AI seed setting being rejected by the SDK by @pcbeingused333 in https://github.com/microsoft/semantic-kernel/pull/14677
* Python: keep empty tool results through the prompt round trip by @iamthehimansh in https://github.com/microsoft/semantic-kernel/pull/14686
* Python: fix(sqlserver): handle None and boolean expressions in SqlServerCollection lambda parser by @wasim-builds in https://github.com/microsoft/semantic-kernel/pull/14687
* Python: Respect optional MCP prompt arguments by @jaeminbird in https://github.com/microsoft/semantic-kernel/pull/14676
* Python: count Gemini thinking tokens in the usage of Google AI completions by @pcbeingused333 in https://github.com/microsoft/semantic-kernel/pull/14671
* Python: fix(python): preserve non-adjacent tool pairs during history truncation by @linhongyu510 in https://github.com/microsoft/semantic-kernel/pull/14658
* Python: fix(python): wire ChatHistoryReducer into ChatCompletionAgent invocation (#12303) by @sparkysolutions10-pixel in https://github.com/microsoft/semantic-kernel/pull/14607
* Python: Fix Handlebars messages helper ignoring its argument by @VANDRANKI in https://github.com/microsoft/semantic-kernel/pull/14537
* Python: fix(python/redis): restore vector search broken by redisvl>=0.5 API change and KeyError on include_vectors=False by @PatrickRibbsaeter in https://github.com/microsoft/semantic-kernel/pull/14278
* Python: Handle empty chat message function results by @lprnmns in https://github.com/microsoft/semantic-kernel/pull/14375
* Python: Exclude ClassVar annotations from generated JSON schemas by @Pushpak731 in https://github.com/microsoft/semantic-kernel/pull/14528
* Python: Propagate MCP initialization failures by @lxingy3 in https://github.com/microsoft/semantic-kernel/pull/14095
* Python: Fix VolatileMemoryStore.get_nearest_matches on an empty collection by @VANDRANKI in https://github.com/microsoft/semantic-kernel/pull/14536
* .Net: docs: fix 20 broken sample links in GettingStartedWithAgents README by @leom1919 in https://github.com/microsoft/semantic-kernel/pull/14699
* .Net: docs: fix dead links after planner removal and MEVD code migration by @leom1919 in https://github.com/microsoft/semantic-kernel/pull/14715
* Python: Drop 3.10 support and expand CI coverage through 3.14 by @eavanvalkenburg in https://github.com/microsoft/semantic-kernel/pull/14708
* Python: Build an array schema for variadic tuple parameters by @anishmehta24 in https://github.com/microsoft/semantic-kernel/pull/14692
* Python: docs(python): fix broken sample links in agents READMEs by @pratikgx in https://github.com/microsoft/semantic-kernel/pull/14703
* Python: Send the NVIDIA nvext setting in extra_body by @codewithfourtix in https://github.com/microsoft/semantic-kernel/pull/14698
* Python: Use storage_name for hybrid search fields and vector queries (#14684) by @Fire162 in https://github.com/microsoft/semantic-kernel/pull/14688
* Python: close native generators when stream invocations end by @DiadkoShmek in https://github.com/microsoft/semantic-kernel/pull/14701
* Python: Fix OracleCollection search with multiple filters by @VANDRANKI in https://github.com/microsoft/semantic-kernel/pull/14541
* .Net: Bind validated HTTP addresses to connections by @rogerbarreto in https://github.com/microsoft/semantic-kernel/pull/14719
* .Net: Harden structured data mutation boundaries by @rogerbarreto in https://github.com/microsoft/semantic-kernel/pull/14718
* Python: Prepare 1.47.0 release and consolidate dependency updates by @eavanvalkenburg in https://github.com/microsoft/semantic-kernel/pull/14720

## New Contributors
* @mangeshraut712 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14668
* @BlueX888 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14697
* @iamthehimansh made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14686
* @jaeminbird made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14676
* @linhongyu510 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14658
* @sparkysolutions10-pixel made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14607
* @PatrickRibbsaeter made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14278
* @lprnmns made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14375
* @Pushpak731 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14528
* @lxingy3 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14095
* @leom1919 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14699
* @anishmehta24 made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14692
* @pratikgx made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14703
* @codewithfourtix made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14698
* @DiadkoShmek made their first contribution in https://github.com/microsoft/semantic-kernel/pull/14701

**Full Changelog**: https://github.com/microsoft/semantic-kernel/compare/python-1.46.0...python-1.47.0

## 笔记


