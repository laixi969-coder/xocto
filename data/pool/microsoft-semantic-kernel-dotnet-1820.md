---
slug: microsoft-semantic-kernel-dotnet-1820
name: 'microsoft/semantic-kernel: dotnet-1.82.0'
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
url: https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0
canonical_url: https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0
summary: '## Changes:


  * df1cb33d0d32699c8d6a2e5b3ea7e5f8990d86d5 .Net: Bump package version to 1.82.0 (#14721)

  * d08a482fab9c6980fa50de5eee79895ba702069d Python: Prepare 1.47.0 release and consolidate dependency
  updates (#14720) [ #14708, #14596, #14597, #14598, #14599, #14600, #14627 ]

  * 28c0d60222b128efc5a41d825ea74e8836231e9c .Net: Harden structured data mutation boundaries (#14718)

  * 1a3ccd8dda169ddf195e40e39c86082a3232eea4 .Net: Bind validated HTTP addresses to connections (#14719)

  * c36f221e61d7ceb96ab245a3cca25da1dd686565 Python: Fix OracleCollection search with multiple filters
  (#14541) [ #14539 ]

  * 530f2e88161634c7aa4c8132fff0c8dfd2104343 Python: Use storage_name for hybrid search fields and vector
  queries (#14684) (#14688)

  * 78f612433829a9bd858e92521c1249d79865bb4f Python: close native generators when stream invocations end
  (#14701)

  * 703eb5f0fce714a33347fb198a5c36cde634695d Python: Send the NVIDIA nvext setting in extra_body (#14698)

  * e68f977a5c9d18acf02ef9fb8116d46315bcb06f Python: Build an array schema for variadic tuple parameters
  (#14692)

  * 1ae2a39b9eb01ec2b934360e3041c6a5b11a525e Python: docs(python): fix broken sample links in agents READMEs
  (#14703)

  <details><summary><b>See More</b></summary>


  * cbb8059ad11e78855b707da16d2dee6824bf82fd Python: Drop 3.10 support and expand CI coverage through
  3.14 (#14708)

  * 9137b35f34a0313f3408404ac50adb688a30c070 .Net: docs: fix dead links after planner removal and MEVD
  code migration (#14715) [ #12399, #11028, #12962, #13396 ]

  * d41312f9d6e9c7db916990b29f799db7d7359e29 .Net: docs: fix 20 broken sample links in GettingStartedWithAgents
  README (#14699) [ #12348 ]

  * d5b2a41d0706a1a653963fd40e3a3b5c7a90979b Python: Fix VolatileMemoryStore.get_nearest_matches on an
  empty collection (#14536) [ #14534, #14523, #14524 ]

  * 9e683cea5c9b7105c0ce7b61ca8a1c81d6eae456 Python: Propagate MCP initialization failures (#14095) [
  #13414 ]

  * 6e5a4b79011d0ec7776b215f0028b841afa13e03 Python: fix(python/redis): restore vector search broken by
  redisvl>=0.5 API change and KeyError on include_vectors=False (#14278) [ #13896 ]

  * 8aa1dc55fb666a5d709aa7a1332a1d7b05a111ec Python: Handle empty chat message function results (#14375)
  [ #14359 ]

  * 7360b98d5492fc56a093194e2df6948c7c071578 Python: Exclude ClassVar annotations from generated JSON
  schemas (#14528) [ #14527 ]

  * b4c5b8349048bf231bf113685b7f414ee3d39037 Python: Fix Handlebars messages helper ignoring its argument
  (#14537) [ #14535 ]

  * 05b6569a582f96f23339b4a2724681f4c2188692 Python: fix(python): wire ChatHistoryReducer into ChatCompletionAgent
  invocation (#12303) (#14607)

  * 7a7c92f1e58eda94aae896721ebc9052c3c0e82e Python: fix(python): preserve non-adjacent tool pairs during
  history truncation (#14658)

  * ae13ada5795f6430b814a275228015614a2bf213 Python: count Gemini thinking tokens in the usage of Google
  AI completions (#14671)

  * 6bfdcb84542b31df77e44c62b80cb774d36804cd Python: Respect optional MCP prompt arguments (#14676)

  * 7a957a0eedc6fa0f3e895f4f5cfcbc070c312501 Python: Fix Mistral AI seed setting being rejected by the
  SDK (#14677)

  * aeb473776b845017fc5442c5fcc56267ac61d496 Python: keep empty tool results through the prompt round
  trip (#14686) [ #14685, #14472, #14375, #14480 ]

  * 2a2e9afb44435b21ece972b76d6f9da8d8375ae3 Python: fix(sqlserver): handle None and boolean expressions
  in SqlServerCollection lambda parser (#14687) [ #14683 ]

  * 8cda8fe1e22ef59f1f975ffe7a1cb39f4458c522 Python: fix Mistral AI chat completion crash on unknown finish
  reasons (model_length) (#14696)

  * 457e12b5300fe339f1d786d6b4c4b22a0239c9b6 Python: fix(sql_server): validate collection field types
  before table creation (#14697) [ #14611 ]

  * 87eadc7f7bb07773688711357ebe41be7639ab16 Python: Batch Google AI embedding requests to the 100-input
  limit (#14700)

  * 356acb66538a3f0f701a15105304c5c95428e51d Python: normalize OpenAPI allowlist paths before prefix match
  (#14668) [ #14662 ]

  * fe6c4831993637d267cbba7632d67d0a0ef817e7 Python: preserve path case in OpenAPI allowed URLs (#14693)

  * 96c9e860db4d7c6da40652d9b421a31b05e98692 .Net: [BREAKING] Consolidate file access (#14679)

  * fa3962b5f3a2f2340afdb45237c8b9700a8c9296 .Net: Bump Aspire.Hosting.Azure.CognitiveServices from 13.4.6
  to 13.5.4 (#14501)

  * 58d28fdea34c19fb6612156f8534e6bf262775c6 .Net: Bump Aspire.Azure.Search.Documents from 13.4.6 to 13.5.4
  (#14499)

  * a77c8ace9e4e779455bc8c29412ed880b66a41ab .Net: Remove migrated .NET Milvus connector (#14682) [ #14579
  ]

  * 4bb64ee3abcab6d007e1ea04e8fe5c2eb7c41267 Python: Bump Python version to 1.46.0 for a release (#14672)

  * ce34fdbc007c89a2f5790ef336686458e476350f Python: Reject bytes in prompt template argument encoding
  (#14669)

  * a4db76e38d997b35dc7b3c4caadab8912b4fbe99 Python: await get_nearest_matches in VolatileMemoryStore.get_nearest_match
  (#14580) [ #14521 ]

  * 43a631264a7d07fb4b355d4d7561a6dacc3bf0d6 Python: fix(anthropic): map every Anthropic stop reason instead
  of raising KeyError (#14616)

  * 8d46973417e35e8f8741b12f188115ebb6681601 Python: fix(python): keep ChatMessageContent.to_prompt a
  str when encoding is set (#14464) [ #13738, #5550, #14304 ]

  * 07ffe3591987da9ce4155a5507d0ddeb77205cb8 Python: fix(python): preserve empty tool results in chat
  history (#14472) [ #14359 ]

  * eff85dd05efc5aded21f2e7849b4f148f65877dc Python: fix(python): preserve Annotated metadata in kernel
  functions (#14496) [ #14441 ]

  * 629f9a4363db78ed4fb3a090c2e86bbdc6f2408f Python: chroma collection_exists catches too much, ensure_collection_deleted
  too little (#14510) [ #14473, #14474 ]

  * 66cb0f9acbc1c1125448923d2ffc111a79f5b1b1 Python: Cosmos NoSQL collection_exists reports a throttled
  request as a missing container (#14515) [ #14510 ]

  * 0026fd1d8d88c357a5d36d60453a4ac4f29872c1 Python: Combine multiple InMemoryCollection filters with
  AND (#14540) [ #14538 ]

  * 50156e3dc374993104e55e2822dece1e2ba52c3a Pin GitHub Actions to full-length commit SHAs (#14568)

  * 660b1a4674aeaa74305cf06b023ecb1664fd0176 Python: fix(python): preserve Pydantic field descriptions
  in schemas (#14454)

  * 9a70006e15cce468cb15632c05677765ebc06ed1 Python: FIX: honor overwrite=False for default execution
  settings in PromptTemplateConfig (#14586) [ #14582 ]

  * b5b526d9b8bd39da41db4a5c0f1aff20d26f7ec8 Python: update to files.get_content (#13159)

  * 8c48410ed91427f0f44ca429772415eea9e8c3e7 Python: fix(python): Fix VolatileMemoryStore.get_nearest_matches
  on empty collection (#14565) [ #14534 ]

  * f95d9fa54fdd6fc3019e056f8c8b1fd0aa3aad4d Python: Fold negative filter literals before vector-store
  parsers (#14572) [ #14571 ]

  * 1916759c214abb9f3b7eda0a7050d4fde7633cd5 Python: derive AggregatorTerminationStrategy from TerminationStrategy
  (#14594) [ #14591 ]

  * 32c3469a49936b89d112aedea2002e7fdade8cb0 Python: Fix default result_parser arity on kernel function
  strategies (#14595) [ #14589 ]

  * bce5801599cf7d380b3f491f327155cc2c56bd41 Python: fix(google_ai): report more Gemini finish reasons
  as content_filter (#14632)

  * 5377800bc6f48d41c61d0b51166ccaf1cb0c1599 Python: Cover callable and mixed Postgres search filters
  (#14313) [ #14497, #14311 ]

  * 2281d4d73833c808698fcfe967a0f2f63f9e78ce Python: add typing.Literal support to KernelJsonSchemaBuilder
  (#14514) [ #14511 ]

  * 2a3236dd8aee851a8b1f67bfbc6d174c32fe8173 Python: feat: support path item parameters and non-method
  keys in OpenAPI parser (#14588) [ #14581 ]

  * c79a160a886e302756a50044f2c961a0944b601e Python: Fix in-memory upserts with key storage names (#14548)
  [ #14547 ]

  * 555c46bdaaf3f1c0852d6ba50d7ff45b6c333ee8 Python: Stop doubling apostrophes in Chroma and Weaviate
  filter values (#14560) [ #14559 ]

  * f37f308ba43d2405c63f3dc3397b2e0fb5f21b25 Python: Fix Qdrant vector search on qdrant-client 1.16+ (#14562)
  [ #14561 ]

  * 27745263a063b66db89935263bc326460da4cf0f Python: Initialize key mapping for a custom FAISS index (#14569)

  * 12361d9b3d630619241badff8697532058662262 Python: fix: write enum value in annotation XML type attribute
  (#14593) [ #14590 ]

  * 63ac01f73fff701371193d4cfd9b393d966fa877 Python: fix: TimePlugin timeZoneOffset/timeZoneName return
  actual values (#14583) (#14604)

  * fdbc2cc97ef1e4122343c3f233dc102d99606e79 Python: fix(anthropic): report token usage as CompletionUsage
  (#14618)

  * 80161f5916d9ec37a231312b6d3dedf9b4857594 Python: Fix Cosmos MongoDB vector index kind set to similarity
  code (#14620) [ #14104 ]

  * b11d98b44611b4821247a40e71da9e93cd53ffff Python: fix(ollama): preserve streamed parallel tool calls
  by assigning call index (#14623) [ #14614 ]

  * cb5909658fa4144b4ffff91e0df76db77ab3c02c Python: fix: decode entities once in ChatHistory.from_rendered_prompt
  (#14624) [ #14619 ]

  * 06368f4193666f322cc9e23f926bb57464b5accd Python: fix: honor include_in_function_choices in Anthropic,
  Bedrock, Google AI, and Vertex AI tool formatters (#14625) [ #14615 ]

  * 5cea835c98e7a067d82c9ae22c98de35e03996be Python: fix a None default being reported as a required parameter
  (#14626)

  * c072a8b878a02e5e34de8bd30ea3979e25d41595 Python: fix(python): set Mistral metadata usage to CompletionUsage
  instead of tuple (#14629) [ #14617 ]

  * c28d64d5969985fff838df8e31f4e272056901d8 Python: fix(bedrock): map guardrail_intervened and model_context_window_exceeded
  stop reasons (#14631)

  * 2ebeb951871ada51d765c213a54856cd4d4dfdc8 Python: Release the AgentChat activity signal when a message
  is rejected (#14640) [ #14638 ]

  * 5e6e46161a6b9816b6bea8d595cdd03270b29a0b Python: Preserve already-typed native function arguments
  (#14643) [ #14642 ]

  * 84d4027f740210c3cfd863c132039e372d16765d Python: Account for intercepted messages when stopping the
  runtime (#14656)

  * ecb80bdcbccdec6730f319927a587a66ffcc539b Python: keep existing summaries after the system message
  in the summa… (#14661)

  * df34878de33c1b0c790527f3c60b41240c946569 Bump werkzeug from 3.1.6 to 3.1.9 in /python/samples/demos/mcp_with_oauth
  (#14556) [ #3207, #3189, #3231, #3236, #3237, #3245, #3248, #3251, #3253, #3254, #3255, #3142, #3128,
  #3127, #3134, #3113, #3088, #3108, #3121, #3309, #3261 ]

  * c40adc43e622234437910bc24d8db7d9021c2a39 Bump pyjwt from 2.13.0 to 2.15.0 in /python/samples/demos/mcp_with_oauth
  (#14555) [ #1202, #1208, #914, #1173, #1174, #1201, #1179, #1212, #1210 ]

  * 076ec468ea8ae61fbcd61752266b31252f3f7c23 Python: Bump mcp from 1.28.1 to 1.30.0 in /python/samples/demos/mcp_with_oauth/server
  (#14628) [ #3448, #3426, #3431, #3451, modelcontextprotocol/python-sdk#3396, modelcontextprotocol/python-sdk#3426,
  modelcontextprotocol/python-sdk#3431, modelcontextprotocol/python-sdk#3448, modelcontextprotocol/python-sdk#3451,
  modelcontextprotocol/python-sdk#3352, modelcontextprotocol/python-sdk#3344, #3377, #3344, #3352, #3177,
  #3082 ]

  * 2044447b8e2f8f949454e8a2dfc18c27cd87902c Python: Bump aiohttp from 3.14.3 to 3.14.4 in /python/samples/demos/mcp_with_oauth
  (#14630)

  * 483ffb487a33a1644886992d56599feae3b69b76 Python: fix(python): Pin HttpPlugin requests to validated
  DNS addresses (#14649)

  * a08e050c7679555df94f984c957813304976c6e9 Python: Preserve configured search filters for invalid overrides
  (#14645)

  * 1b22fd7d7e145175cf558284a32eb7684783fca9 Python: Fix Cosmos hybrid search field validation (#14650)

  * 6f1ae42afbc856e4f2480b202ae4006d73540c9a fix(ci): match Python coverage reports to their workflow
  run (#14651)

  * 50add35bf430a0e41d2a6a03525a3587f03bbfd9 Python: Clarify tool invocation authorization boundaries
  (#14647)

  * e92e51957445a1a4781ce353ca9a3c0daf3f6416 Python: docs(python): clarify prompt template trust boundary
  (#14648)

  * 382fe5af0ff9ffd10d0b28423892f997af69c919 .Net: Reject dot segments in session upload paths (#14646)

  * 25501830b9483ad6b23955dee340c8590fa54152 Python: Validate PostgreSQL collection field types (#14611)

  * 7a92cd4e7c2712370b8d85b687a474b2e858cdcc Python: fix(python): reject dot-segment remote paths in SessionsPythonTool.upload_file
  (#14563) [ #14520, #13478, #14085, #14140 ]

  * 7e68276a4a85022dd4da255beae3263ab5cbf059 fix(ci): select integration test events explicitly (#14603)

  * 5b4a3269a6803f7832568e66313c31d714a1f009 .Net: Remove migrated .NET Chroma connector (#14579)

  * 1b1f64b98c3828ada434d262c0e3038da6cc3508 Python: Avoid logging function argument values (#14574)

  * 11f072362e24207da9db55779c0fd73eb15123b1 .Net: Improve OpenAPI HTTP connection handling (#14570)

  * cc8a15fa356f02dcb7bc64999392ca02f3167312 .Net: Bound element nesting depth in XML prompt parsing (#14504)


  This list of changes was [auto generated](https://msdata.visualstudio.com/Vienna/_build/results?buildId=245259946&view=logs).</details>'
first_seen: '2026-11-07T01:56:40Z'
last_seen: '2026-11-08T01:27:11Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0
  seen_at: '2026-11-08T01:27:11Z'
  metrics:
    reactions: 1
  kind: news
---

# microsoft/semantic-kernel: dotnet-1.82.0

## Changes:

* df1cb33d0d32699c8d6a2e5b3ea7e5f8990d86d5 .Net: Bump package version to 1.82.0 (#14721)
* d08a482fab9c6980fa50de5eee79895ba702069d Python: Prepare 1.47.0 release and consolidate dependency updates (#14720) [ #14708, #14596, #14597, #14598, #14599, #14600, #14627 ]
* 28c0d60222b128efc5a41d825ea74e8836231e9c .Net: Harden structured data mutation boundaries (#14718)
* 1a3ccd8dda169ddf195e40e39c86082a3232eea4 .Net: Bind validated HTTP addresses to connections (#14719)
* c36f221e61d7ceb96ab245a3cca25da1dd686565 Python: Fix OracleCollection search with multiple filters (#14541) [ #14539 ]
* 530f2e88161634c7aa4c8132fff0c8dfd2104343 Python: Use storage_name for hybrid search fields and vector queries (#14684) (#14688)
* 78f612433829a9bd858e92521c1249d79865bb4f Python: close native generators when stream invocations end (#14701)
* 703eb5f0fce714a33347fb198a5c36cde634695d Python: Send the NVIDIA nvext setting in extra_body (#14698)
* e68f977a5c9d18acf02ef9fb8116d46315bcb06f Python: Build an array schema for variadic tuple parameters (#14692)
* 1ae2a39b9eb01ec2b934360e3041c6a5b11a525e Python: docs(python): fix broken sample links in agents READMEs (#14703)
<details><summary><b>See More</b></summary>

* cbb8059ad11e78855b707da16d2dee6824bf82fd Python: Drop 3.10 support and expand CI coverage through 3.14 (#14708)
* 9137b35f34a0313f3408404ac50adb688a30c070 .Net: docs: fix dead links after planner removal and MEVD code migration (#14715) [ #12399, #11028, #12962, #13396 ]
* d41312f9d6e9c7db916990b29f799db7d7359e29 .Net: docs: fix 20 broken sample links in GettingStartedWithAgents README (#14699) [ #12348 ]
* d5b2a41d0706a1a653963fd40e3a3b5c7a90979b Python: Fix VolatileMemoryStore.get_nearest_matches on an empty collection (#14536) [ #14534, #14523, #14524 ]
* 9e683cea5c9b7105c0ce7b61ca8a1c81d6eae456 Python: Propagate MCP initialization failures (#14095) [ #13414 ]
* 6e5a4b79011d0ec7776b215f0028b841afa13e03 Python: fix(python/redis): restore vector search broken by redisvl>=0.5 API change and KeyError on include_vectors=False (#14278) [ #13896 ]
* 8aa1dc55fb666a5d709aa7a1332a1d7b05a111ec Python: Handle empty chat message function results (#14375) [ #14359 ]
* 7360b98d5492fc56a093194e2df6948c7c071578 Python: Exclude ClassVar annotations from generated JSON schemas (#14528) [ #14527 ]
* b4c5b8349048bf231bf113685b7f414ee3d39037 Python: Fix Handlebars messages helper ignoring its argument (#14537) [ #14535 ]
* 05b6569a582f96f23339b4a2724681f4c2188692 Python: fix(python): wire ChatHistoryReducer into ChatCompletionAgent invocation (#12303) (#14607)
* 7a7c92f1e58eda94aae896721ebc9052c3c0e82e Python: fix(python): preserve non-adjacent tool pairs during history truncation (#14658)
* ae13ada5795f6430b814a275228015614a2bf213 Python: count Gemini thinking tokens in the usage of Google AI completions (#14671)
* 6bfdcb84542b31df77e44c62b80cb774d36804cd Python: Respect optional MCP prompt arguments (#14676)
* 7a957a0eedc6fa0f3e895f4f5cfcbc070c312501 Python: Fix Mistral AI seed setting being rejected by the SDK (#14677)
* aeb473776b845017fc5442c5fcc56267ac61d496 Python: keep empty tool results through the prompt round trip (#14686) [ #14685, #14472, #14375, #14480 ]
* 2a2e9afb44435b21ece972b76d6f9da8d8375ae3 Python: fix(sqlserver): handle None and boolean expressions in SqlServerCollection lambda parser (#14687) [ #14683 ]
* 8cda8fe1e22ef59f1f975ffe7a1cb39f4458c522 Python: fix Mistral AI chat completion crash on unknown finish reasons (model_length) (#14696)
* 457e12b5300fe339f1d786d6b4c4b22a0239c9b6 Python: fix(sql_server): validate collection field types before table creation (#14697) [ #14611 ]
* 87eadc7f7bb07773688711357ebe41be7639ab16 Python: Batch Google AI embedding requests to the 100-input limit (#14700)
* 356acb66538a3f0f701a15105304c5c95428e51d Python: normalize OpenAPI allowlist paths before prefix match (#14668) [ #14662 ]
* fe6c4831993637d267cbba7632d67d0a0ef817e7 Python: preserve path case in OpenAPI allowed URLs (#14693)
* 96c9e860db4d7c6da40652d9b421a31b05e98692 .Net: [BREAKING] Consolidate file access (#14679)
* fa3962b5f3a2f2340afdb45237c8b9700a8c9296 .Net: Bump Aspire.Hosting.Azure.CognitiveServices from 13.4.6 to 13.5.4 (#14501)
* 58d28fdea34c19fb6612156f8534e6bf262775c6 .Net: Bump Aspire.Azure.Search.Documents from 13.4.6 to 13.5.4 (#14499)
* a77c8ace9e4e779455bc8c29412ed880b66a41ab .Net: Remove migrated .NET Milvus connector (#14682) [ #14579 ]
* 4bb64ee3abcab6d007e1ea04e8fe5c2eb7c41267 Python: Bump Python version to 1.46.0 for a release (#14672)
* ce34fdbc007c89a2f5790ef336686458e476350f Python: Reject bytes in prompt template argument encoding (#14669)
* a4db76e38d997b35dc7b3c4caadab8912b4fbe99 Python: await get_nearest_matches in VolatileMemoryStore.get_nearest_match (#14580) [ #14521 ]
* 43a631264a7d07fb4b355d4d7561a6dacc3bf0d6 Python: fix(anthropic): map every Anthropic stop reason instead of raising KeyError (#14616)
* 8d46973417e35e8f8741b12f188115ebb6681601 Python: fix(python): keep ChatMessageContent.to_prompt a str when encoding is set (#14464) [ #13738, #5550, #14304 ]
* 07ffe3591987da9ce4155a5507d0ddeb77205cb8 Python: fix(python): preserve empty tool results in chat history (#14472) [ #14359 ]
* eff85dd05efc5aded21f2e7849b4f148f65877dc Python: fix(python): preserve Annotated metadata in kernel functions (#14496) [ #14441 ]
* 629f9a4363db78ed4fb3a090c2e86bbdc6f2408f Python: chroma collection_exists catches too much, ensure_collection_deleted too little (#14510) [ #14473, #14474 ]
* 66cb0f9acbc1c1125448923d2ffc111a79f5b1b1 Python: Cosmos NoSQL collection_exists reports a throttled request as a missing container (#14515) [ #14510 ]
* 0026fd1d8d88c357a5d36d60453a4ac4f29872c1 Python: Combine multiple InMemoryCollection filters with AND (#14540) [ #14538 ]
* 50156e3dc374993104e55e2822dece1e2ba52c3a Pin GitHub Actions to full-length commit SHAs (#14568)
* 660b1a4674aeaa74305cf06b023ecb1664fd0176 Python: fix(python): preserve Pydantic field descriptions in schemas (#14454)
* 9a70006e15cce468cb15632c05677765ebc06ed1 Python: FIX: honor overwrite=False for default execution settings in PromptTemplateConfig (#14586) [ #14582 ]
* b5b526d9b8bd39da41db4a5c0f1aff20d26f7ec8 Python: update to files.get_content (#13159)
* 8c48410ed91427f0f44ca429772415eea9e8c3e7 Python: fix(python): Fix VolatileMemoryStore.get_nearest_matches on empty collection (#14565) [ #14534 ]
* f95d9fa54fdd6fc3019e056f8c8b1fd0aa3aad4d Python: Fold negative filter literals before vector-store parsers (#14572) [ #14571 ]
* 1916759c214abb9f3b7eda0a7050d4fde7633cd5 Python: derive AggregatorTerminationStrategy from TerminationStrategy (#14594) [ #14591 ]
* 32c3469a49936b89d112aedea2002e7fdade8cb0 Python: Fix default result_parser arity on kernel function strategies (#14595) [ #14589 ]
* bce5801599cf7d380b3f491f327155cc2c56bd41 Python: fix(google_ai): report more Gemini finish reasons as content_filter (#14632)
* 5377800bc6f48d41c61d0b51166ccaf1cb0c1599 Python: Cover callable and mixed Postgres search filters (#14313) [ #14497, #14311 ]
* 2281d4d73833c808698fcfe967a0f2f63f9e78ce Python: add typing.Literal support to KernelJsonSchemaBuilder (#14514) [ #14511 ]
* 2a3236dd8aee851a8b1f67bfbc6d174c32fe8173 Python: feat: support path item parameters and non-method keys in OpenAPI parser (#14588) [ #14581 ]
* c79a160a886e302756a50044f2c961a0944b601e Python: Fix in-memory upserts with key storage names (#14548) [ #14547 ]
* 555c46bdaaf3f1c0852d6ba50d7ff45b6c333ee8 Python: Stop doubling apostrophes in Chroma and Weaviate filter values (#14560) [ #14559 ]
* f37f308ba43d2405c63f3dc3397b2e0fb5f21b25 Python: Fix Qdrant vector search on qdrant-client 1.16+ (#14562) [ #14561 ]
* 27745263a063b66db89935263bc326460da4cf0f Python: Initialize key mapping for a custom FAISS index (#14569)
* 12361d9b3d630619241badff8697532058662262 Python: fix: write enum value in annotation XML type attribute (#14593) [ #14590 ]
* 63ac01f73fff701371193d4cfd9b393d966fa877 Python: fix: TimePlugin timeZoneOffset/timeZoneName return actual values (#14583) (#14604)
* fdbc2cc97ef1e4122343c3f233dc102d99606e79 Python: fix(anthropic): report token usage as CompletionUsage (#14618)
* 80161f5916d9ec37a231312b6d3dedf9b4857594 Python: Fix Cosmos MongoDB vector index kind set to similarity code (#14620) [ #14104 ]
* b11d98b44611b4821247a40e71da9e93cd53ffff Python: fix(ollama): preserve streamed parallel tool calls by assigning call index (#14623) [ #14614 ]
* cb5909658fa4144b4ffff91e0df76db77ab3c02c Python: fix: decode entities once in ChatHistory.from_rendered_prompt (#14624) [ #14619 ]
* 06368f4193666f322cc9e23f926bb57464b5accd Python: fix: honor include_in_function_choices in Anthropic, Bedrock, Google AI, and Vertex AI tool formatters (#14625) [ #14615 ]
* 5cea835c98e7a067d82c9ae22c98de35e03996be Python: fix a None default being reported as a required parameter (#14626)
* c072a8b878a02e5e34de8bd30ea3979e25d41595 Python: fix(python): set Mistral metadata usage to CompletionUsage instead of tuple (#14629) [ #14617 ]
* c28d64d5969985fff838df8e31f4e272056901d8 Python: fix(bedrock): map guardrail_intervened and model_context_window_exceeded stop reasons (#14631)
* 2ebeb951871ada51d765c213a54856cd4d4dfdc8 Python: Release the AgentChat activity signal when a message is rejected (#14640) [ #14638 ]
* 5e6e46161a6b9816b6bea8d595cdd03270b29a0b Python: Preserve already-typed native function arguments (#14643) [ #14642 ]
* 84d4027f740210c3cfd863c132039e372d16765d Python: Account for intercepted messages when stopping the runtime (#14656)
* ecb80bdcbccdec6730f319927a587a66ffcc539b Python: keep existing summaries after the system message in the summa… (#14661)
* df34878de33c1b0c790527f3c60b41240c946569 Bump werkzeug from 3.1.6 to 3.1.9 in /python/samples/demos/mcp_with_oauth (#14556) [ #3207, #3189, #3231, #3236, #3237, #3245, #3248, #3251, #3253, #3254, #3255, #3142, #3128, #3127, #3134, #3113, #3088, #3108, #3121, #3309, #3261 ]
* c40adc43e622234437910bc24d8db7d9021c2a39 Bump pyjwt from 2.13.0 to 2.15.0 in /python/samples/demos/mcp_with_oauth (#14555) [ #1202, #1208, #914, #1173, #1174, #1201, #1179, #1212, #1210 ]
* 076ec468ea8ae61fbcd61752266b31252f3f7c23 Python: Bump mcp from 1.28.1 to 1.30.0 in /python/samples/demos/mcp_with_oauth/server (#14628) [ #3448, #3426, #3431, #3451, modelcontextprotocol/python-sdk#3396, modelcontextprotocol/python-sdk#3426, modelcontextprotocol/python-sdk#3431, modelcontextprotocol/python-sdk#3448, modelcontextprotocol/python-sdk#3451, modelcontextprotocol/python-sdk#3352, modelcontextprotocol/python-sdk#3344, #3377, #3344, #3352, #3177, #3082 ]
* 2044447b8e2f8f949454e8a2dfc18c27cd87902c Python: Bump aiohttp from 3.14.3 to 3.14.4 in /python/samples/demos/mcp_with_oauth (#14630)
* 483ffb487a33a1644886992d56599feae3b69b76 Python: fix(python): Pin HttpPlugin requests to validated DNS addresses (#14649)
* a08e050c7679555df94f984c957813304976c6e9 Python: Preserve configured search filters for invalid overrides (#14645)
* 1b22fd7d7e145175cf558284a32eb7684783fca9 Python: Fix Cosmos hybrid search field validation (#14650)
* 6f1ae42afbc856e4f2480b202ae4006d73540c9a fix(ci): match Python coverage reports to their workflow run (#14651)
* 50add35bf430a0e41d2a6a03525a3587f03bbfd9 Python: Clarify tool invocation authorization boundaries (#14647)
* e92e51957445a1a4781ce353ca9a3c0daf3f6416 Python: docs(python): clarify prompt template trust boundary (#14648)
* 382fe5af0ff9ffd10d0b28423892f997af69c919 .Net: Reject dot segments in session upload paths (#14646)
* 25501830b9483ad6b23955dee340c8590fa54152 Python: Validate PostgreSQL collection field types (#14611)
* 7a92cd4e7c2712370b8d85b687a474b2e858cdcc Python: fix(python): reject dot-segment remote paths in SessionsPythonTool.upload_file (#14563) [ #14520, #13478, #14085, #14140 ]
* 7e68276a4a85022dd4da255beae3263ab5cbf059 fix(ci): select integration test events explicitly (#14603)
* 5b4a3269a6803f7832568e66313c31d714a1f009 .Net: Remove migrated .NET Chroma connector (#14579)
* 1b1f64b98c3828ada434d262c0e3038da6cc3508 Python: Avoid logging function argument values (#14574)
* 11f072362e24207da9db55779c0fd73eb15123b1 .Net: Improve OpenAPI HTTP connection handling (#14570)
* cc8a15fa356f02dcb7bc64999392ca02f3167312 .Net: Bound element nesting depth in XML prompt parsing (#14504)

This list of changes was [auto generated](https://msdata.visualstudio.com/Vienna/_build/results?buildId=245259946&view=logs).</details>

## 笔记


