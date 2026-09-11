---
slug: huggingface-transformers-release-5170
name: Hugging Face Transformers
builder: huggingface
category: ''
summary_zh: 2026年9月9日，公开模型社区 Transformers 发布 v5.17.0，新增对 Hy4-Preview 的支持：一个 780B 参数、每 token 仅激活 49B 的混合专家模型，带
  100 万 token 上下文窗口，并用 MLA 将键值压缩进低秩潜表示。这意味着超大规模稀疏模型经主流开源库即可被应用开发者调用（推断：低激活比加键值压缩可能降低长上下文推理成本）；发布说明未含定价与性能实测，成本收益尚待核验，不宜据此推断长上下文应用已成主流。
inspiration: ''
summary_en: 'On September 9, 2026, public model community Transformers shipped v5.17.0, adding support
  for Hy4-Preview: a 780B-parameter mixture-of-experts model activating only 49B parameters per token,
  with a 1M-token context window and MLA that compresses keys and values into a low-rank latent. Very
  large sparse models are now callable through a mainstream open-source library (inference: the low activation
  ratio plus KV compression may lower long-context inference cost); the release notes contain no pricing
  or benchmark data, so the cost claim stays unverified and one release does not prove long-context apps
  have gone mainstream.'
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
url: https://github.com/huggingface/transformers/releases/tag/v5.17.0
canonical_url: https://github.com/huggingface/transformers/releases/tag/v5.17.0
summary: "# Release v5.17.0\r\n\r\n\r\n## New Model additions\r\n\r\n### HYV4\r\n\r\n<img width=\"1503\"\
  \ height=\"827\" alt=\"image\" src=\"https://github.com/user-attachments/assets/e6ed85ee-eb1d-40eb-a0d4-c649f6337ca9\"\
  \ />\r\n\r\n\r\nHy4-Preview is a 780B-parameter mixture-of-experts language model that activates 49B\
  \ parameters per\r\ntoken. Each MoE layer holds 256 routed experts plus one always-active shared expert\
  \ and routes every\r\ntoken to 8 of them. The context window is 1M tokens.\r\n\r\nThe architecture combines\
  \ four features:\r\n\r\n- **Multi-head Latent Attention (MLA)** compresses keys and values into a low-rank\
  \ latent\r\n  (`kv_lora_rank`) that `kv_b_proj` expands back to one key/value per query head.\r\n- **DeepSeek\
  \ Sparse Attention (DSA)** selects `index_topk` keys per query with a lightweight indexer.\r\n  Following\
  \ [IndexShare](https://huggingface.co/papers/2603.12201), only the layers marked `\"full\"`\r\n  in\
  \ `indexer_types` run an indexer; `\"shared\"` layers reuse the previous full layer's selection.\r\n\
  - **Gated MLA with learnable attention sinks**, where each head owns a sink logit that participates\r\
  \n  in the softmax and contributes no value, as in [GPT-OSS](./gpt_oss).\r\n- **Independent Hyper-Connections\
  \ (iHC)** replace the plain residual path with `hc_mult` parallel\r\n  residual streams that are collapsed\
  \ before, and redistributed after, every sublayer.\r\n\r\nThe implementation does not execute the multi-token\
  \ prediction (MTP) layers. Released checkpoints\r\nkeep those weights so that other runtimes can use\
  \ them for speculative decoding; they are ignored\r\nat load time.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hy_v4)\r\
  \n* Add h4 (#48473) by @ArthurZucker in [#48473](https://github.com/huggingface/transformers/pull/48473)\r\
  \n\r\n### VibeVoice\r\n\r\n<img width=\"2140\" height=\"1188\" alt=\"image\" src=\"https://github.com/user-attachments/assets/29ccea01-a855-4d4f-a6af-61bc4fc883a4\"\
  \ />\r\n\r\n[VibeVoice](https://huggingface.co/papers/2508.19205) is a novel framework for synthesizing\
  \ high-fidelity, long-form speech with multiple speakers by employing a next-token diffusion approach\
  \ within a Large Language Model (LLM) structure. It's designed to capture the authentic conversational\
  \ \"vibe\" and is particularly suited for generating audio content like podcasts and multi-participant\
  \ audiobooks.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/vibevoice)\r\
  \n* Implement VibeVoice  (#40546) by @pengzhiliang in [#40546](https://github.com/huggingface/transformers/pull/40546)\r\
  \n\r\n### NeoMME\r\n\r\nNeoMME is a family of efficient 260M and 800M parameter multimodal-native multilingual\
  \ foundation encoders from H Company. It processes multilingual text tokens and raw image patches in\
  \ a single bidirectional Transformer encoder, without a separately pretrained vision tower or causal\
  \ language model.\r\n\r\nNeoMME-Retriever is a model fine-tuned from the NeoMME backbone for visual\
  \ document retrieval with joint late-interaction and dense objectives. It takes text queries and documents\
  \ (text or page screenshots) and produces multi-vector embeddings for MeanMaxSim scoring (late-interaction)\
  \ and mean-pooled embeddings for cosine similarity (dense).\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/neomme)\r\
  \n* Add NeoMME and NeoMME-Retriever (#47992) by @tonywu71 in [#47992](https://github.com/huggingface/transformers/pull/47992)\r\
  \n\r\n### Fun-ASR-Nano\r\n\r\nFun-ASR-Nano is an 800M-parameter end-to-end speech recognition model\
  \ developed by Alibaba DAMO Academy's FunAudioLLM team. It achieves state-of-the-art performance on\
  \ Chinese, English, and Japanese ASR benchmarks while being significantly smaller than comparable models.\r\
  \n\r\nKey features are\r\n- **Chinese, English, and Japanese**, including 7 Chinese dialects and 26\
  \ regional accents\r\n- **Hotword customization** for domain-specific vocabulary\r\n- **Native punctuation**\
  \ output (no separate punctuation model needed)\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/fun_asr_nano)\r\
  \n* Add Fun-ASR-Nano model (#46180) by @LauraGPT in [#46180](https://github.com/huggingface/transformers/pull/46180)\r\
  \n\r\n### KimiLinear\r\n\r\nKimi Linear is a hybrid linear attention architecture from Moonshot AI,\
  \ introduced in\r\n[Kimi Linear: An Expressive, Efficient Attention Architecture](https://huggingface.co/papers/2510.26692).\r\
  \n\r\nAt its core is **Kimi Delta Attention (KDA)**, a refinement of [Gated DeltaNet](https://huggingface.co/papers/2412.06464)\r\
  \nthat gives each key channel its own forget gate, so the recurrent state decays per channel instead\
  \ of per head. KDA is\r\nused in most layers; every fourth layer keeps a full-attention block that reuses\
  \ DeepSeek-V3's Multi-head Latent\r\nAttention (MLA), and the feed-forward blocks are DeepSeek-V3-style\
  \ MoE with a shared expert.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/kimi_linear)\r\
  \n* Kimi linear (#48250) by @remi-or in [#48250](https://github.com/huggingface/transformers/pull/48250)\r\
  \n\r\n### Canary\r\n\r\nCanary-1B-v2, a fast, robust multilingual model for Automatic Speech Recognition\
  \ (ASR) and Speech-to-Text Translation (AST):\r\n\r\nCanary reuses the [Fast Conformer](https://huggingface.co/papers/2305.05084)\
  \ encoder from [Parakeet](./parakeet.md) (loaded through [`ParakeetEncoder`] / [`ParakeetEncoderConfig`])\
  \ and pairs it with a Transformer decoder that uses fixed sinusoidal positional embeddings, cross-attention\
  \ to the encoder outputs and tied input/output embeddings. The task is selected through a decoder prompt\
  \ prefix built by [`CanaryProcessor`] of the form `<|startofcontext|> <|startoftranscript|> <|emo:undefined|>\
  \ <source_lang> <target_lang> <pnc|nopnc> <|noitn|> <|notimestamp|> <|nodiarize|>`, where `source_lang\
  \ == target_lang` selects transcription and otherwise selects translation.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/canary)\r\
  \n* model: Add NVIDIA Canary-1B-v2 to Transformers (#46825) by @harshaljanjani in [#46825](https://github.com/huggingface/transformers/pull/46825)\r\
  \n\r\n\r\n\r\n## Breaking changes\r\n\r\nVision rotary embeddings (2D/3D) have been standardized into\
  \ a unified RoPE frequency computation module, so users with custom vision models relying on attention-layer-level\
  \ or model-specific RoPE grid interleaving logic must migrate to the new centralized `modeling_rope_utils.py`\
  \ implementation.\r\n* :rotating_light: Vision (2d/3d) rotary embeddings  (#48105) by @zucchini-nlp\r\
  \n\r\n\r\n\r\n## Generation\r\n\r\nGeneration improvements include a performance optimization that avoids\
  \ unnecessary accelerator synchronization on every decode step (reducing per-step overhead), and a fix\
  \ to prevent unconditional downloading of remote hub files during generation. Several correctness fixes\
  \ were also applied, including enforcing auto-compile cache checks for encoder-decoder models, standardizing\
  \ `past_key_values` naming in AfMoE, and resolving flaky export and integration test failures.\r\n\r\
  \n\r\n* [`Generate`] Avoid unconditionally downloading remote hub file (#48620) by @vasqu in [#48620]\r\
  \n* [generate] stop synchronizing the accelerator on every decode step (#47975) by @SunMarc in [#47975]\r\
  \n* [AfMoE] Standardize past_key_values argument naming across forward and generate (#48430) by @shenhuaqingshi\
  \ in [#48430]\r\n* Fix MTP generation test regex gate for escaped layer ignore keys (#48003) (#48262)\
  \ by @Noxtimo in [#48262]\r\n* fix(generation): Enforce the auto-compile cache check for encoder-decoder\
  \ models (#48364) by @harshaljanjani in [#48364]\r\n* [serge] Fix 4 integration tests for model `generation`\
  \ failing with `output_mismatch` (list output differs (4)) (#48133) by @sergereview[bot] in [#48133]\r\
  \n* [VibeVoice] Skip generate export tests (flaky) (#48396) by @ydshieh in [#48396]\r\n\r\n\r\n## Cache\r\
  \n\r\nFixed several cache-related bugs, including a quantized cache issue in VibeVoice, incorrect rejection\
  \ of non-static cache implementations in VoxtralRealtime, missing auto-compile cache checks for encoder-decoder\
  \ models, and a silent failure when paged attention is called without a cache. Documentation was also\
  \ updated to clarify `ContinuousBatchingConfig` usage and sliding window model limitations.\r\n\r\n\r\
  \n* vibevoice: fix bug for quant cache (#48487) by @kaixuanliu in [#48487]\r\n* Fix VoxtralRealtime\
  \ rejecting non-static cache implementations (#48082) by @jiqing-feng in [#48082]\r\n* Raise when a\
  \ paged attention forward is called with no cache (#48297) by @qgallouedec in [#48297]\r\n* [docs] Pass\
  \ ContinuousBatchingConfig and sliding window models  (#48381) by @stevhliu in [#48381]\r\n* Retry get_daily_ci_runs\
  \ on stale GitHub API cache (#48374) by @ydshieh in [#48374]\r\n\r\n\r\n## Kernels\r\n\r\nKernel support\
  \ was improved with fixes for nested FLA kernel imports when only `fla-core` is installed, a warning\
  \ when hub-kernel functions silently fall back to slower pure-PyTorch reference implementations, and\
  \ the ability to register standalone functions (e.g., RoPE) in `KernelConfig` with optional non-inheritance\
  \ of default mappings. Additional fixes include corrected repository paths for ESMFold2 kernels and\
  \ updated documentation for `KernelConfig` customization.\r\n\r\n\r\n* Support nested FLA kernel imports\
  \ for fla-core (#48221) by @DimensionSTP in [#48221]\r\n* Warn once when a hub-kernel function falls\
  \ back to its reference PyTorch path (#48185) by @qgallouedec in [#48185]\r\n* [docs] Kernel updates\
  \ (#48465) by @stevhliu in [#48465]\r\n* [`Kernels`] Enable functions into kernels registry and allow\
  \ non inheritance (#48443) by @vasqu in [#48443]\r\n* Fix kernel commit and repo paths for ESMFold2\
  \ (#48186) by @Rocketknight1 in [#48186]\r\n\r\n\r\n## Quantization\r\n\r\nFixed several quantization\
  \ bugs, including a quant cache issue in VibeVoice, incorrect FP8 embedding handling for Qwen models,\
  \ missing FP8 tensor parallelism layer overrides, and unnecessary MXFP4 weight dequantization on XPU\
  \ devices.\r\n\r\n\r\n* fix qwen4exp-fp8 ple embedding (#48368) by @JJJYmmm in [#48368]\r\n* Keep MXFP4\
  \ weights quantized on XPU when use_kernels is set (#47923) by @jiqing-feng in [#47923]\r\n* Fix missing\
  \ FP8 TP layer overrides (#48343) by @changwangss in [#48343]\r\n\r\n\r\n## Bugfixes and improvements\r\
  \n\r\n* MRoPE continued (#48594) by @zucchini-nlp in [#48594]\r\n* [fix] Update stale expected strings\
  \ in HunYuanVL integration tests (#48646) by @ydshieh in [#48646]\r\n* [Quantizaiton]support 5/6/7 bits\
  \ in AutoRound (#48481) by @wenhuach21 in [#48481]\r\n* [fix] Update stale golden values and fix expected_logits\
  \ shape in FlavaForPreTraining integration tests (#48639) by @ydshieh in [#48639]\r\n* Fix YOLOS device\
  \ mismatch with device_map=\"auto\" (#46886) by @swankystark in [#46886]\r\n* Honor `shift_labels` in\
  \ decoder-only LLM/VLM losses (#48493) by @qgallouedec in [#48493]\r\n* [KimiLinear] Fix test_cpu_offload:\
  \ set num_local_experts=4 in model tester (#48624) by @ydshieh in [#48624]\r\n* [docs] Per-layer config\
  \ (#48601) by @stevhliu in [#48601]\r\n* Fix `generate_flags` parsing in `transformers chat` (#48597)\
  \ by @SunMarc in [#48597]\r\n* [fix] Fix how we read package versions - triggered by torch 2.14+ (#48615)\
  \ by @ydshieh in [#48615]\r\n* [Docker] Upgrade CPU torch to <=2.14.0, torchcodec to <=0.16.0 (#48614)\
  \ by @ydshieh in [#48614]\r\n* Fix AttributeError in gradient_checkpointing_enable(offload=True) (#48590)\
  \ by @tarekziade in [#48590]\r\n* Another day fixing CI (#48591) by @zucchini-nlp in [#48591]\r\n* esmfold2:\
  \ keep `distogram_head` in fp32 as well (#48488) by @kaixuanliu in [#48488]\r\n* Add `supports_context_parallel`\
  \ to `PreTrainedModel` (#48442) by @qgallouedec in [#48442]\r\n* [docs] mlinter reference (#48460) by\
  \ @stevhliu in [#48460]\r\n* [docs] Add a LiteRT page under community integrations (#48540) by @john-rocky\
  \ in [#48540]\r\n* [GLM 5.3 Flash] Fix NaN gradients in chunked KDA (#48455) by @imvladikon in [#48455]\r\
  \n* [docs] Fix [[autodoc]] directives in ALBERT model documentation (#48593) by @samyuktahegde in [#48593]\r\
  \n* [Fix] Fix A10 expectations for a test (#48454) by @remi-or in [#48454]\r\n* Add PR comment CI for\
  \ AMD (MI300) (#48065) by @ydshieh in [#48065]\r\n* docs: fix docstring parameter names that do not\
  \ match signatures (#48575) by @simpleqt in [#48575]\r\n* docs: remove phantom parameters from docstrings\
  \ (#48576) by @simpleqt in [#48576]\r\n* extend some case to xpu as well (#48502) by @sywangyi in [#48502]\r\
  \n* [serge] Fix 2 integration tests for model `glm4_moe` failing with `OOM` (other (2)) (#48551) by\
  \ @sergereview[bot] in [#48551]\r\n* [serge] Fix 2 integration tests for model `nemotron` failing with\
  \ `import_or_config` (other (2)) (#48582) by @sergereview[bot] in [#48582]\r\n* Compress the agent conventions\
  \ file and document two modular pitfalls (#48586) by @tarekziade in [#48586]\r\n* Guard against a None\
  \ video processor class when the backend is unavailable (#48557) by @caiotheodoro in [#48557]\r\n* [serge]\
  \ Fix 2 integration tests regressed by commit 83d46aa2a2c4 (PR #47625) (#48580) by @sergereview[bot]\
  \ in [#48580]\r\n* [nit] use requires_backends (#47576) by @eustlb in [#47576]\r\n* [serge] Fix 2 integration\
  \ tests for model `kosmos2` failing with `import_or_config` (other (2)) (#48552) by @sergereview[bot]\
  \ in [#48552]\r\n* Fix failing tests for cohere_compass (#48005) by @kaixuanliu in [#48005]\r\n* [Fix]\
  \ Use dedicated helpers for DeepGEMM and SonicMoE tests (#48523) by @remi-or in [#48523]\r\n* CI: Point\
  \ test fixtures at hf-internal-testing copies we already host (#48521) by @tarekziade in [#48521]\r\n\
  * fix failed test cases for glm5_next (#48497) by @kaixuanliu in [#48497]\r\n* Pass kwargs to the Mamba2\
  \ mixer in Nemotron-H, Falcon-H1 and Mamba2 (#48490) by @kfastino in [#48490]\r\n* Retire test_multi_gpu_data_parallel_forward\
  \ (#48508) by @tarekziade in [#48508]\r\n* Processing tests [part 2] (#47922) by @zucchini-nlp in [#47922]\r\
  \n* QA: Add noisy comment checker (#48484) by @tarekziade in [#48484]\r\n* Allow nested rope params\
  \ for tiny models (#48435) by @zucchini-nlp in [#48435]\r\n* Fix sliding-window mask `layer_idx` in\
  \ Gemma3/Gemma4 `create_masks_for_vision_model` (#48482) by @jiqing-feng in [#48482]\r\n* add xpu expectations\
  \ for hunyuan_vl model tests (#48504) by @kaixuanliu in [#48504]\r\n* [`Qwen 3.5 Moe`] Fix decorators\
  \ (#48436) by @vasqu in [#48436]\r\n* Infinite loop in dependency search (#48393) by @zucchini-nlp in\
  \ [#48393]\r\n* [serge] Fix 2 integration tests for model `fsmt` failing with `output_mismatch` (tensor\
  \ values differ (2)) (#48496) by @sergereview[bot] in [#48496]\r\n* Fix some tests by removing the deprecation\
  \ cycle (#48503) by @Cyrilvallez in [#48503]\r\n* Remove deprecation (#48500) by @Cyrilvallez in [#48500]\r\
  \n* Fix Pix2StructTextAttention init using hidden_size instead of d_kv (#47558) by @<NOT FOUND> in [#47558]\r\
  \n* Fix pre patch release utility (#48499) by @Cyrilvallez in [#48499]\r\n* Update dev version (#48498)\
  \ by @Cyrilvallez in [#48498]\r\n* Fix Inkling inputs_embeds and add more tests (#47827) by @Cyrilvallez\
  \ in [#47827]\r\n* Simplify and fix qwen4 tests (#48340) by @Cyrilvallez in [#48340]\r\n* [docs] Partial\
  \ checkpointing and group_by_length (#48463) by @stevhliu in [#48463]\r\n* doc: fix syntax error and\
  \ typos in VibeVoice documentation (#48489) by @VimalN2005 in [#48489]\r\n* [`Qwen4 Exp`] Use partial\
  \ to avoid skipping mask more easily (#48456) by @vasqu in [#48456]\r\n* Add support for NeuCodec (#47143)\
  \ by @harryjulian in [#47143]\r\n* [serge] Fix 1 integration tests regressed by commit bd9509355c8a\
  \ (PR #47493) (#48426) by @sergereview[bot] in [#48426]\r\n* Fix rotary embedding regression (#48477)\
  \ by @Cyrilvallez in [#48477]\r\n* Remove deprecated mask functions (#48476) by @Cyrilvallez in [#48476]\r\
  \n* [MTP] Save memory by only capturing the last layer's hidden_states (#48475) by @Cyrilvallez in [#48475]\r\
  \n* Allow capturing only necessary hidden_states with capture_outputs (#48081) by @sywangyi in [#48081]\r\
  \n* Support per-layer MTP configuration (#48264) by @eladsegal in [#48264]\r\n* [docs] Fix code snippets\
  \ (#47772) by @stevhliu in [#47772]\r\n* [Fix] Sparse TikToken tokenizers silently fail (#48446) by\
  \ @remi-or in [#48446]\r\n* No inherit decorator for NeoMME (#48457) by @zucchini-nlp in [#48457]\r\n\
  * Batch Rebalance Data Sampler (#47340) by @delock in [#47340]\r\n* [serge] Fix 2 integration tests\
  \ for model `cwm` failing with `import_or_config` (other (2)) (#48414) by @sergereview[bot] in [#48414]\r\
  \n* fix: Add DEIMv2 attribution (#48448) by @harshaljanjani in [#48448]\r\n* [fix] inkling: mps + cuda\
  \ mel spec extraction (#47432) by @eustlb in [#47432]\r\n* fix: decode() batch path respects self.clean_up_tokenization_spaces\
  \ (#47793) by @lorenzozanee in [#47793]\r\n* Grounding dino fp16 dtype [backlog] (#48438) by @molbap\
  \ in [#48438]\r\n* Init the process group with a load-scaled timeout for sharded loading (#48228) by\
  \ @qgallouedec in [#48228]\r\n* Raise a clear error when a token is both forced and suppressed (#47511)\
  \ by @qgallouedec in [#47511]\r\n* Clarify device placement in pipelines (#47367) by @LysandreJik in\
  \ [#47367]\r\n* Add offload to gradient checkpointing (#48444) by @qgallouedec in [#48444]\r\n* [MiniCPMV4_6]\
  \ Update test_small_model_vision_generation_batch expected output (value drift) (#48406) by @ydshieh\
  \ in [#48406]\r\n* [serge] Fix 2 integration tests for model `hyperclovax` failing with `other` (other\
  \ (2)) (#48440) by @sergereview[bot] in [#48440]\r\n* fix(models): Drop the position-indexed token type\
  \ lookup in RoPE encoders (#48407) by @harshaljanjani in [#48407]\r\n* Document image_hidden_states/pixel_values\
  \ mutual exclusivity for SmolVLM/Idefics2/Idefics3 (#47714) by @verma8076 in [#47714]\r\n* Re-order\
  \ a bit for easier navigation (#48434) by @zucchini-nlp in [#48434]\r\n* Deprecated stuff gone (#48367)\
  \ by @zucchini-nlp in [#48367]\r\n* [serge] Fix 6 integration tests for model `seamless_m4t_v2` failing\
  \ with `other` (other (6)) (#48425) by @sergereview[bot] in [#48425]\r\n* [Docs]: Update GLM 5.3 (#48401)\
  \ by @Dovis01 in [#48401]\r\n* Avoid print to stdout that fails the job `check_failed_tests` job (#48391)\
  \ by @ydshieh in [#48391]\r\n* Fix incorrect tuple return annotations on forward methods returning a\
  \ Tensor (#48359) by @Gronoxx in [#48359]\r\n* Fix interval merge invariant in _find_disjoint (#47860)\
  \ by @sharmax-vikas in [#47860]\r\n* skip mtp slow tests for now (#48328) (#48329) by @tarekziade in\
  \ [#48329]\r\n* Update Tailscale action version in workflow (#48394) by @glegendre01 in [#48394]\r\n\
  * fix some failure in xpu (#48252) by @sywangyi in [#48252]\r\n* [Improvement] Make gated delta rule\
  \ more explicit  (#47625) by @remi-or in [#47625]\r\n* [CB] Fix wrong device scoping (#48370) by @remi-or\
  \ in [#48370]\r\n* Bump transformers-mlinter to 0.1.5 and clear the new findings (#48259) by @tarekziade\
  \ in [#48259]\r\n* fix: flash-attn fallback failing on torch2.13 (#48388) by @NanoCode012 in [#48388]\r\
  \n* [LongcatFlash] Fix test_longcat_generation_cpu: use device_map=\"cpu\" to avoid MoE disk offload\
  \ issue (#48377) by @ydshieh in [#48377]\r\n* [Qwen3VLMoe] Update `test_small_model_integration_test_batch`\
  \ expected output (value drift) (#48376) by @ydshieh in [#48376]\r\n* [ONNX] Skip affected models on\
  \ torch 2.13 (two dynamo regressions) (#48191) by @ydshieh in [#48191]\r\n* Fix `safe_open` mmap memory\
  \ exhaustion on Windows by using `pread` backend (#48341) by @eryk-roch in [#48341]\r\n* Fix Zamba2\
  \ construction for num_mem_blocks > 1 checkpoints (#48325) by @john-rocky in [#48325]\r\n* [Docs] Change\
  \ 5.3 Flash pos in toc (#48366) by @Dovis01 in [#48366]\r\n* [conftest] Use get_cpu_ram_total_gib for\
  \ psutil patch (cgroup-aware) (#48290) by @ydshieh in [#48290]\r\n* Fix flaky test_training_gradient_checkpointing\
  \ for BigBirdPegasus (fp noise filter) (#48332) by @ydshieh in [#48332]\r\n* Quiet continuous batching\
  \ at default verbosity (#48314) by @qgallouedec in [#48314]\r\n* Wait for the first request in the async\
  \ continuous batching bootstrap (#48304) by @qgallouedec in [#48304]\r\n* Ignore a stale best checkpoint\
  \ recorded in a resumed trainer state (#48319) by @VaggelisGian in [#48319]\r\n* [docs] Fix links and\
  \ remove TokenizerFast (#47748) by @stevhliu in [#47748]\r\n* Fix incorrect token classification prefix\
  \ for ESMC (#48348) by @Rocketknight1 in [#48348]\r\n* Create the continuous batching CPU group with\
  \ local synchronization (#48302) by @qgallouedec in [#48302]\r\n* Resolve continuous batching config\
  \ against the text config for composite models (#48299) by @qgallouedec in [#48299]\r\n* [`CI`] Unblock\
  \ fast CI for now (failing tests) (#48344) by @vasqu in [#48344]\r\n* [qwen4_exp] disable torch/onnx\
  \ export tests due to data-dependent control flow (#48345) by @ydshieh in [#48345]\r\n* [debug] Trace\
  \ previous CI run selection in get_previous_daily_ci.py (#48338) by @ydshieh in [#48338]\r\n* Normalize\
  \ HunYuanVL's legacy field aliases via attribute_map (#48261) by @hmellor in [#48261]\r\n\r\n## Significant\
  \ community contributions\r\n\r\nThe following contributors have made significant changes to the library\
  \ over the last release:\r\n\r\n* @ydshieh\r\n    * [fix] Update stale expected strings in HunYuanVL\
  \ integration tests (#48646)\r\n    * [fix] Update stale golden values and fix expected_logits shape\
  \ in FlavaForPreTraining integration tests (#48639)\r\n    * [tests] Fix integration test golden values\
  \ broken by fast image processor default (PR #41388) (#48637)\r\n    * [KimiLinear] Fix test_cpu_offload:\
  \ set num_local_experts=4 in model tester (#48624)\r\n    * Fix GPU memory teardown in CLI serve tests\
  \ (#48618)\r\n    * [fix] Fix how we read package versions - triggered by torch 2.14+ (#48615)\r\n \
  \   * [Docker] Upgrade CPU torch to <=2.14.0, torchcodec to <=0.16.0 (#48614)\r\n    * Add PR comment\
  \ CI for AMD (MI300) (#48065)\r\n    * [MiniCPMV4_6] Update test_small_model_vision_generation_batch\
  \ expected output (value drift) (#48406)\r\n    * Avoid print to stdout that fails the job `check_failed_tests`\
  \ job (#48391)\r\n    * [VibeVoice] Skip generate export tests (flaky) (#48396)\r\n    * [LongcatFlash]\
  \ Fix test_longcat_generation_cpu: use device_map=\"cpu\" to avoid MoE disk offload issue (#48377)\r\
  \n    * [Qwen3VLMoe] Update `test_small_model_integration_test_batch` expected output (value drift)\
  \ (#48376)\r\n    * [ONNX] Skip affected models on torch 2.13 (two dynamo regressions) (#48191)\r\n\
  \    * Retry get_daily_ci_runs on stale GitHub API cache (#48374)\r\n    * [conftest] Use get_cpu_ram_total_gib\
  \ for psutil patch (cgroup-aware) (#48290)\r\n    * Fix flaky test_training_gradient_checkpointing for\
  \ BigBirdPegasus (fp noise filter) (#48332)\r\n    * [qwen4_exp] disable torch/onnx export tests due\
  \ to data-dependent control flow (#48345)\r\n    * [debug] Trace previous CI run selection in get_previous_daily_ci.py\
  \ (#48338)\r\n* @LauraGPT\r\n    * Add Fun-ASR-Nano model (#46180)\r\n* @tarekziade\r\n    * Fix AttributeError\
  \ in gradient_checkpointing_enable(offload=True) (#48590)\r\n    * Compress the agent conventions file\
  \ and document two modular pitfalls (#48586)\r\n    * CI: Point test fixtures at hf-internal-testing\
  \ copies we already host (#48521)\r\n    * Retire test_multi_gpu_data_parallel_forward (#48508)\r\n\
  \    * QA: Add noisy comment checker (#48484)\r\n    * skip mtp slow tests for now (#48328) (#48329)\r\
  \n    * Bump transformers-mlinter to 0.1.5 and clear the new findings (#48259)\r\n* @remi-or\r\n   \
  \ * [Fix] Fix A10 expectations for a test (#48454)\r\n    * Kimi linear (#48250)\r\n    * [Fix] Use\
  \ dedicated helpers for DeepGEMM and SonicMoE tests (#48523)\r\n    * [Fix] Sparse TikToken tokenizers\
  \ silently fail (#48446)\r\n    * [Improvement] Make gated delta rule more explicit  (#47625)\r\n  \
  \  * [CB] Fix wrong device scoping (#48370)\r\n    * [CB] Fail faster (#48334)\r\n* @ArthurZucker\r\n\
  \    * Add h4 (#48473)\r\n* @harryjulian\r\n    * Add support for NeuCodec (#47143)\r\n* @delock\r\n\
  \    * Batch Rebalance Data Sampler (#47340)\r\n* @harshaljanjani\r\n    * fix: Add DEIMv2 attribution\
  \ (#48448)\r\n    * model: Add NVIDIA Canary-1B-v2 to Transformers (#46825)\r\n    * fix(generation):\
  \ Enforce the auto-compile cache check for encoder-decoder models (#48364)\r\n    * fix(models): Drop\
  \ the position-indexed token type lookup in RoPE encoders (#48407)\r\n* @tonywu71\r\n    * Add NeoMME\
  \ and NeoMME-Retriever (#47992)\r\n* @Dovis01\r\n    * [Docs]: Update GLM 5.3 (#48401)\r\n    * [Docs]\
  \ Change 5.3 Flash pos in toc (#48366)\r\n    * [Glm 5.3 Flash] GLM 5.3 Flash Support (#48342)\r\n*\
  \ @pengzhiliang\r\n    * Implement VibeVoice  (#40546)"
first_seen: '2026-09-09T15:42:45Z'
last_seen: '2026-09-11T00:10:34Z'
status: market_context
sources:
- github
sightings:
- source: github
  url: https://github.com/huggingface/transformers/releases/tag/v5.17.0
  seen_at: '2026-09-11T00:10:34Z'
  metrics:
    reactions: 5
  kind: news
---

# Hugging Face Transformers

# Release v5.17.0


## New Model additions

### HYV4

<img width="1503" height="827" alt="image" src="https://github.com/user-attachments/assets/e6ed85ee-eb1d-40eb-a0d4-c649f6337ca9" />


Hy4-Preview is a 780B-parameter mixture-of-experts language model that activates 49B parameters per
token. Each MoE layer holds 256 routed experts plus one always-active shared expert and routes every
token to 8 of them. The context window is 1M tokens.

The architecture combines four features:

- **Multi-head Latent Attention (MLA)** compresses keys and values into a low-rank latent
  (`kv_lora_rank`) that `kv_b_proj` expands back to one key/value per query head.
- **DeepSeek Sparse Attention (DSA)** selects `index_topk` keys per query with a lightweight indexer.
  Following [IndexShare](https://huggingface.co/papers/2603.12201), only the layers marked `"full"`
  in `indexer_types` run an indexer; `"shared"` layers reuse the previous full layer's selection.
- **Gated MLA with learnable attention sinks**, where each head owns a sink logit that participates
  in the softmax and contributes no value, as in [GPT-OSS](./gpt_oss).
- **Independent Hyper-Connections (iHC)** replace the plain residual path with `hc_mult` parallel
  residual streams that are collapsed before, and redistributed after, every sublayer.

The implementation does not execute the multi-token prediction (MTP) layers. Released checkpoints
keep those weights so that other runtimes can use them for speculative decoding; they are ignored
at load time.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hy_v4)
* Add h4 (#48473) by @ArthurZucker in [#48473](https://github.com/huggingface/transformers/pull/48473)

### VibeVoice

<img width="2140" height="1188" alt="image" src="https://github.com/user-attachments/assets/29ccea01-a855-4d4f-a6af-61bc4fc883a4" />

[VibeVoice](https://huggingface.co/papers/2508.19205) is a novel framework for synthesizing high-fidelity, long-form speech with multiple speakers by employing a next-token diffusion approach within a Large Language Model (LLM) structure. It's designed to capture the authentic conversational "vibe" and is particularly suited for generating audio content like podcasts and multi-participant audiobooks.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/vibevoice)
* Implement VibeVoice  (#40546) by @pengzhiliang in [#40546](https://github.com/huggingface/transformers/pull/40546)

### NeoMME

NeoMME is a family of efficient 260M and 800M parameter multimodal-native multilingual foundation encoders from H Company. It processes multilingual text tokens and raw image patches in a single bidirectional Transformer encoder, without a separately pretrained vision tower or causal language model.

NeoMME-Retriever is a model fine-tuned from the NeoMME backbone for visual document retrieval with joint late-interaction and dense objectives. It takes text queries and documents (text or page screenshots) and produces multi-vector embeddings for MeanMaxSim scoring (late-interaction) and mean-pooled embeddings for cosine similarity (dense).

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/neomme)
* Add NeoMME and NeoMME-Retriever (#47992) by @tonywu71 in [#47992](https://github.com/huggingface/transformers/pull/47992)

### Fun-ASR-Nano

Fun-ASR-Nano is an 800M-parameter end-to-end speech recognition model developed by Alibaba DAMO Academy's FunAudioLLM team. It achieves state-of-the-art performance on Chinese, English, and Japanese ASR benchmarks while being significantly smaller than comparable models.

Key features are
- **Chinese, English, and Japanese**, including 7 Chinese dialects and 26 regional accents
- **Hotword customization** for domain-specific vocabulary
- **Native punctuation** output (no separate punctuation model needed)

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/fun_asr_nano)
* Add Fun-ASR-Nano model (#46180) by @LauraGPT in [#46180](https://github.com/huggingface/transformers/pull/46180)

### KimiLinear

Kimi Linear is a hybrid linear attention architecture from Moonshot AI, introduced in
[Kimi Linear: An Expressive, Efficient Attention Architecture](https://huggingface.co/papers/2510.26692).

At its core is **Kimi Delta Attention (KDA)**, a refinement of [Gated DeltaNet](https://huggingface.co/papers/2412.06464)
that gives each key channel its own forget gate, so the recurrent state decays per channel instead of per head. KDA is
used in most layers; every fourth layer keeps a full-attention block that reuses DeepSeek-V3's Multi-head Latent
Attention (MLA), and the feed-forward blocks are DeepSeek-V3-style MoE with a shared expert.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/kimi_linear)
* Kimi linear (#48250) by @remi-or in [#48250](https://github.com/huggingface/transformers/pull/48250)

### Canary

Canary-1B-v2, a fast, robust multilingual model for Automatic Speech Recognition (ASR) and Speech-to-Text Translation (AST):

Canary reuses the [Fast Conformer](https://huggingface.co/papers/2305.05084) encoder from [Parakeet](./parakeet.md) (loaded through [`ParakeetEncoder`] / [`ParakeetEncoderConfig`]) and pairs it with a Transformer decoder that uses fixed sinusoidal positional embeddings, cross-attention to the encoder outputs and tied input/output embeddings. The task is selected through a decoder prompt prefix built by [`CanaryProcessor`] of the form `<|startofcontext|> <|startoftranscript|> <|emo:undefined|> <source_lang> <target_lang> <pnc|nopnc> <|noitn|> <|notimestamp|> <|nodiarize|>`, where `source_lang == target_lang` selects transcription and otherwise selects translation.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/canary)
* model: Add NVIDIA Canary-1B-v2 to Transformers (#46825) by @harshaljanjani in [#46825](https://github.com/huggingface/transformers/pull/46825)



## Breaking changes

Vision rotary embeddings (2D/3D) have been standardized into a unified RoPE frequency computation module, so users with custom vision models relying on attention-layer-level or model-specific RoPE grid interleaving logic must migrate to the new centralized `modeling_rope_utils.py` implementation.
* :rotating_light: Vision (2d/3d) rotary embeddings  (#48105) by @zucchini-nlp



## Generation

Generation improvements include a performance optimization that avoids unnecessary accelerator synchronization on every decode step (reducing per-step overhead), and a fix to prevent unconditional downloading of remote hub files during generation. Several correctness fixes were also applied, including enforcing auto-compile cache checks for encoder-decoder models, standardizing `past_key_values` naming in AfMoE, and resolving flaky export and integration test failures.


* [`Generate`] Avoid unconditionally downloading remote hub file (#48620) by @vasqu in [#48620]
* [generate] stop synchronizing the accelerator on every decode step (#47975) by @SunMarc in [#47975]
* [AfMoE] Standardize past_key_values argument naming across forward and generate (#48430) by @shenhuaqingshi in [#48430]
* Fix MTP generation test regex gate for escaped layer ignore keys (#48003) (#48262) by @Noxtimo in [#48262]
* fix(generation): Enforce the auto-compile cache check for encoder-decoder models (#48364) by @harshaljanjani in [#48364]
* [serge] Fix 4 integration tests for model `generation` failing with `output_mismatch` (list output differs (4)) (#48133) by @sergereview[bot] in [#48133]
* [VibeVoice] Skip generate export tests (flaky) (#48396) by @ydshieh in [#48396]


## Cache

Fixed several cache-related bugs, including a quantized cache issue in VibeVoice, incorrect rejection of non-static cache implementations in VoxtralRealtime, missing auto-compile cache checks for encoder-decoder models, and a silent failure when paged attention is called without a cache. Documentation was also updated to clarify `ContinuousBatchingConfig` usage and sliding window model limitations.


* vibevoice: fix bug for quant cache (#48487) by @kaixuanliu in [#48487]
* Fix VoxtralRealtime rejecting non-static cache implementations (#48082) by @jiqing-feng in [#48082]
* Raise when a paged attention forward is called with no cache (#48297) by @qgallouedec in [#48297]
* [docs] Pass ContinuousBatchingConfig and sliding window models  (#48381) by @stevhliu in [#48381]
* Retry get_daily_ci_runs on stale GitHub API cache (#48374) by @ydshieh in [#48374]


## Kernels

Kernel support was improved with fixes for nested FLA kernel imports when only `fla-core` is installed, a warning when hub-kernel functions silently fall back to slower pure-PyTorch reference implementations, and the ability to register standalone functions (e.g., RoPE) in `KernelConfig` with optional non-inheritance of default mappings. Additional fixes include corrected repository paths for ESMFold2 kernels and updated documentation for `KernelConfig` customization.


* Support nested FLA kernel imports for fla-core (#48221) by @DimensionSTP in [#48221]
* Warn once when a hub-kernel function falls back to its reference PyTorch path (#48185) by @qgallouedec in [#48185]
* [docs] Kernel updates (#48465) by @stevhliu in [#48465]
* [`Kernels`] Enable functions into kernels registry and allow non inheritance (#48443) by @vasqu in [#48443]
* Fix kernel commit and repo paths for ESMFold2 (#48186) by @Rocketknight1 in [#48186]


## Quantization

Fixed several quantization bugs, including a quant cache issue in VibeVoice, incorrect FP8 embedding handling for Qwen models, missing FP8 tensor parallelism layer overrides, and unnecessary MXFP4 weight dequantization on XPU devices.


* fix qwen4exp-fp8 ple embedding (#48368) by @JJJYmmm in [#48368]
* Keep MXFP4 weights quantized on XPU when use_kernels is set (#47923) by @jiqing-feng in [#47923]
* Fix missing FP8 TP layer overrides (#48343) by @changwangss in [#48343]


## Bugfixes and improvements

* MRoPE continued (#48594) by @zucchini-nlp in [#48594]
* [fix] Update stale expected strings in HunYuanVL integration tests (#48646) by @ydshieh in [#48646]
* [Quantizaiton]support 5/6/7 bits in AutoRound (#48481) by @wenhuach21 in [#48481]
* [fix] Update stale golden values and fix expected_logits shape in FlavaForPreTraining integration tests (#48639) by @ydshieh in [#48639]
* Fix YOLOS device mismatch with device_map="auto" (#46886) by @swankystark in [#46886]
* Honor `shift_labels` in decoder-only LLM/VLM losses (#48493) by @qgallouedec in [#48493]
* [KimiLinear] Fix test_cpu_offload: set num_local_experts=4 in model tester (#48624) by @ydshieh in [#48624]
* [docs] Per-layer config (#48601) by @stevhliu in [#48601]
* Fix `generate_flags` parsing in `transformers chat` (#48597) by @SunMarc in [#48597]
* [fix] Fix how we read package versions - triggered by torch 2.14+ (#48615) by @ydshieh in [#48615]
* [Docker] Upgrade CPU torch to <=2.14.0, torchcodec to <=0.16.0 (#48614) by @ydshieh in [#48614]
* Fix AttributeError in gradient_checkpointing_enable(offload=True) (#48590) by @tarekziade in [#48590]
* Another day fixing CI (#48591) by @zucchini-nlp in [#48591]
* esmfold2: keep `distogram_head` in fp32 as well (#48488) by @kaixuanliu in [#48488]
* Add `supports_context_parallel` to `PreTrainedModel` (#48442) by @qgallouedec in [#48442]
* [docs] mlinter reference (#48460) by @stevhliu in [#48460]
* [docs] Add a LiteRT page under community integrations (#48540) by @john-rocky in [#48540]
* [GLM 5.3 Flash] Fix NaN gradients in chunked KDA (#48455) by @imvladikon in [#48455]
* [docs] Fix [[autodoc]] directives in ALBERT model documentation (#48593) by @samyuktahegde in [#48593]
* [Fix] Fix A10 expectations for a test (#48454) by @remi-or in [#48454]
* Add PR comment CI for AMD (MI300) (#48065) by @ydshieh in [#48065]
* docs: fix docstring parameter names that do not match signatures (#48575) by @simpleqt in [#48575]
* docs: remove phantom parameters from docstrings (#48576) by @simpleqt in [#48576]
* extend some case to xpu as well (#48502) by @sywangyi in [#48502]
* [serge] Fix 2 integration tests for model `glm4_moe` failing with `OOM` (other (2)) (#48551) by @sergereview[bot] in [#48551]
* [serge] Fix 2 integration tests for model `nemotron` failing with `import_or_config` (other (2)) (#48582) by @sergereview[bot] in [#48582]
* Compress the agent conventions file and document two modular pitfalls (#48586) by @tarekziade in [#48586]
* Guard against a None video processor class when the backend is unavailable (#48557) by @caiotheodoro in [#48557]
* [serge] Fix 2 integration tests regressed by commit 83d46aa2a2c4 (PR #47625) (#48580) by @sergereview[bot] in [#48580]
* [nit] use requires_backends (#47576) by @eustlb in [#47576]
* [serge] Fix 2 integration tests for model `kosmos2` failing with `import_or_config` (other (2)) (#48552) by @sergereview[bot] in [#48552]
* Fix failing tests for cohere_compass (#48005) by @kaixuanliu in [#48005]
* [Fix] Use dedicated helpers for DeepGEMM and SonicMoE tests (#48523) by @remi-or in [#48523]
* CI: Point test fixtures at hf-internal-testing copies we already host (#48521) by @tarekziade in [#48521]
* fix failed test cases for glm5_next (#48497) by @kaixuanliu in [#48497]
* Pass kwargs to the Mamba2 mixer in Nemotron-H, Falcon-H1 and Mamba2 (#48490) by @kfastino in [#48490]
* Retire test_multi_gpu_data_parallel_forward (#48508) by @tarekziade in [#48508]
* Processing tests [part 2] (#47922) by @zucchini-nlp in [#47922]
* QA: Add noisy comment checker (#48484) by @tarekziade in [#48484]
* Allow nested rope params for tiny models (#48435) by @zucchini-nlp in [#48435]
* Fix sliding-window mask `layer_idx` in Gemma3/Gemma4 `create_masks_for_vision_model` (#48482) by @jiqing-feng in [#48482]
* add xpu expectations for hunyuan_vl model tests (#48504) by @kaixuanliu in [#48504]
* [`Qwen 3.5 Moe`] Fix decorators (#48436) by @vasqu in [#48436]
* Infinite loop in dependency search (#48393) by @zucchini-nlp in [#48393]
* [serge] Fix 2 integration tests for model `fsmt` failing with `output_mismatch` (tensor values differ (2)) (#48496) by @sergereview[bot] in [#48496]
* Fix some tests by removing the deprecation cycle (#48503) by @Cyrilvallez in [#48503]
* Remove deprecation (#48500) by @Cyrilvallez in [#48500]
* Fix Pix2StructTextAttention init using hidden_size instead of d_kv (#47558) by @<NOT FOUND> in [#47558]
* Fix pre patch release utility (#48499) by @Cyrilvallez in [#48499]
* Update dev version (#48498) by @Cyrilvallez in [#48498]
* Fix Inkling inputs_embeds and add more tests (#47827) by @Cyrilvallez in [#47827]
* Simplify and fix qwen4 tests (#48340) by @Cyrilvallez in [#48340]
* [docs] Partial checkpointing and group_by_length (#48463) by @stevhliu in [#48463]
* doc: fix syntax error and typos in VibeVoice documentation (#48489) by @VimalN2005 in [#48489]
* [`Qwen4 Exp`] Use partial to avoid skipping mask more easily (#48456) by @vasqu in [#48456]
* Add support for NeuCodec (#47143) by @harryjulian in [#47143]
* [serge] Fix 1 integration tests regressed by commit bd9509355c8a (PR #47493) (#48426) by @sergereview[bot] in [#48426]
* Fix rotary embedding regression (#48477) by @Cyrilvallez in [#48477]
* Remove deprecated mask functions (#48476) by @Cyrilvallez in [#48476]
* [MTP] Save memory by only capturing the last layer's hidden_states (#48475) by @Cyrilvallez in [#48475]
* Allow capturing only necessary hidden_states with capture_outputs (#48081) by @sywangyi in [#48081]
* Support per-layer MTP configuration (#48264) by @eladsegal in [#48264]
* [docs] Fix code snippets (#47772) by @stevhliu in [#47772]
* [Fix] Sparse TikToken tokenizers silently fail (#48446) by @remi-or in [#48446]
* No inherit decorator for NeoMME (#48457) by @zucchini-nlp in [#48457]
* Batch Rebalance Data Sampler (#47340) by @delock in [#47340]
* [serge] Fix 2 integration tests for model `cwm` failing with `import_or_config` (other (2)) (#48414) by @sergereview[bot] in [#48414]
* fix: Add DEIMv2 attribution (#48448) by @harshaljanjani in [#48448]
* [fix] inkling: mps + cuda mel spec extraction (#47432) by @eustlb in [#47432]
* fix: decode() batch path respects self.clean_up_tokenization_spaces (#47793) by @lorenzozanee in [#47793]
* Grounding dino fp16 dtype [backlog] (#48438) by @molbap in [#48438]
* Init the process group with a load-scaled timeout for sharded loading (#48228) by @qgallouedec in [#48228]
* Raise a clear error when a token is both forced and suppressed (#47511) by @qgallouedec in [#47511]
* Clarify device placement in pipelines (#47367) by @LysandreJik in [#47367]
* Add offload to gradient checkpointing (#48444) by @qgallouedec in [#48444]
* [MiniCPMV4_6] Update test_small_model_vision_generation_batch expected output (value drift) (#48406) by @ydshieh in [#48406]
* [serge] Fix 2 integration tests for model `hyperclovax` failing with `other` (other (2)) (#48440) by @sergereview[bot] in [#48440]
* fix(models): Drop the position-indexed token type lookup in RoPE encoders (#48407) by @harshaljanjani in [#48407]
* Document image_hidden_states/pixel_values mutual exclusivity for SmolVLM/Idefics2/Idefics3 (#47714) by @verma8076 in [#47714]
* Re-order a bit for easier navigation (#48434) by @zucchini-nlp in [#48434]
* Deprecated stuff gone (#48367) by @zucchini-nlp in [#48367]
* [serge] Fix 6 integration tests for model `seamless_m4t_v2` failing with `other` (other (6)) (#48425) by @sergereview[bot] in [#48425]
* [Docs]: Update GLM 5.3 (#48401) by @Dovis01 in [#48401]
* Avoid print to stdout that fails the job `check_failed_tests` job (#48391) by @ydshieh in [#48391]
* Fix incorrect tuple return annotations on forward methods returning a Tensor (#48359) by @Gronoxx in [#48359]
* Fix interval merge invariant in _find_disjoint (#47860) by @sharmax-vikas in [#47860]
* skip mtp slow tests for now (#48328) (#48329) by @tarekziade in [#48329]
* Update Tailscale action version in workflow (#48394) by @glegendre01 in [#48394]
* fix some failure in xpu (#48252) by @sywangyi in [#48252]
* [Improvement] Make gated delta rule more explicit  (#47625) by @remi-or in [#47625]
* [CB] Fix wrong device scoping (#48370) by @remi-or in [#48370]
* Bump transformers-mlinter to 0.1.5 and clear the new findings (#48259) by @tarekziade in [#48259]
* fix: flash-attn fallback failing on torch2.13 (#48388) by @NanoCode012 in [#48388]
* [LongcatFlash] Fix test_longcat_generation_cpu: use device_map="cpu" to avoid MoE disk offload issue (#48377) by @ydshieh in [#48377]
* [Qwen3VLMoe] Update `test_small_model_integration_test_batch` expected output (value drift) (#48376) by @ydshieh in [#48376]
* [ONNX] Skip affected models on torch 2.13 (two dynamo regressions) (#48191) by @ydshieh in [#48191]
* Fix `safe_open` mmap memory exhaustion on Windows by using `pread` backend (#48341) by @eryk-roch in [#48341]
* Fix Zamba2 construction for num_mem_blocks > 1 checkpoints (#48325) by @john-rocky in [#48325]
* [Docs] Change 5.3 Flash pos in toc (#48366) by @Dovis01 in [#48366]
* [conftest] Use get_cpu_ram_total_gib for psutil patch (cgroup-aware) (#48290) by @ydshieh in [#48290]
* Fix flaky test_training_gradient_checkpointing for BigBirdPegasus (fp noise filter) (#48332) by @ydshieh in [#48332]
* Quiet continuous batching at default verbosity (#48314) by @qgallouedec in [#48314]
* Wait for the first request in the async continuous batching bootstrap (#48304) by @qgallouedec in [#48304]
* Ignore a stale best checkpoint recorded in a resumed trainer state (#48319) by @VaggelisGian in [#48319]
* [docs] Fix links and remove TokenizerFast (#47748) by @stevhliu in [#47748]
* Fix incorrect token classification prefix for ESMC (#48348) by @Rocketknight1 in [#48348]
* Create the continuous batching CPU group with local synchronization (#48302) by @qgallouedec in [#48302]
* Resolve continuous batching config against the text config for composite models (#48299) by @qgallouedec in [#48299]
* [`CI`] Unblock fast CI for now (failing tests) (#48344) by @vasqu in [#48344]
* [qwen4_exp] disable torch/onnx export tests due to data-dependent control flow (#48345) by @ydshieh in [#48345]
* [debug] Trace previous CI run selection in get_previous_daily_ci.py (#48338) by @ydshieh in [#48338]
* Normalize HunYuanVL's legacy field aliases via attribute_map (#48261) by @hmellor in [#48261]

## Significant community contributions

The following contributors have made significant changes to the library over the last release:

* @ydshieh
    * [fix] Update stale expected strings in HunYuanVL integration tests (#48646)
    * [fix] Update stale golden values and fix expected_logits shape in FlavaForPreTraining integration tests (#48639)
    * [tests] Fix integration test golden values broken by fast image processor default (PR #41388) (#48637)
    * [KimiLinear] Fix test_cpu_offload: set num_local_experts=4 in model tester (#48624)
    * Fix GPU memory teardown in CLI serve tests (#48618)
    * [fix] Fix how we read package versions - triggered by torch 2.14+ (#48615)
    * [Docker] Upgrade CPU torch to <=2.14.0, torchcodec to <=0.16.0 (#48614)
    * Add PR comment CI for AMD (MI300) (#48065)
    * [MiniCPMV4_6] Update test_small_model_vision_generation_batch expected output (value drift) (#48406)
    * Avoid print to stdout that fails the job `check_failed_tests` job (#48391)
    * [VibeVoice] Skip generate export tests (flaky) (#48396)
    * [LongcatFlash] Fix test_longcat_generation_cpu: use device_map="cpu" to avoid MoE disk offload issue (#48377)
    * [Qwen3VLMoe] Update `test_small_model_integration_test_batch` expected output (value drift) (#48376)
    * [ONNX] Skip affected models on torch 2.13 (two dynamo regressions) (#48191)
    * Retry get_daily_ci_runs on stale GitHub API cache (#48374)
    * [conftest] Use get_cpu_ram_total_gib for psutil patch (cgroup-aware) (#48290)
    * Fix flaky test_training_gradient_checkpointing for BigBirdPegasus (fp noise filter) (#48332)
    * [qwen4_exp] disable torch/onnx export tests due to data-dependent control flow (#48345)
    * [debug] Trace previous CI run selection in get_previous_daily_ci.py (#48338)
* @LauraGPT
    * Add Fun-ASR-Nano model (#46180)
* @tarekziade
    * Fix AttributeError in gradient_checkpointing_enable(offload=True) (#48590)
    * Compress the agent conventions file and document two modular pitfalls (#48586)
    * CI: Point test fixtures at hf-internal-testing copies we already host (#48521)
    * Retire test_multi_gpu_data_parallel_forward (#48508)
    * QA: Add noisy comment checker (#48484)
    * skip mtp slow tests for now (#48328) (#48329)
    * Bump transformers-mlinter to 0.1.5 and clear the new findings (#48259)
* @remi-or
    * [Fix] Fix A10 expectations for a test (#48454)
    * Kimi linear (#48250)
    * [Fix] Use dedicated helpers for DeepGEMM and SonicMoE tests (#48523)
    * [Fix] Sparse TikToken tokenizers silently fail (#48446)
    * [Improvement] Make gated delta rule more explicit  (#47625)
    * [CB] Fix wrong device scoping (#48370)
    * [CB] Fail faster (#48334)
* @ArthurZucker
    * Add h4 (#48473)
* @harryjulian
    * Add support for NeuCodec (#47143)
* @delock
    * Batch Rebalance Data Sampler (#47340)
* @harshaljanjani
    * fix: Add DEIMv2 attribution (#48448)
    * model: Add NVIDIA Canary-1B-v2 to Transformers (#46825)
    * fix(generation): Enforce the auto-compile cache check for encoder-decoder models (#48364)
    * fix(models): Drop the position-indexed token type lookup in RoPE encoders (#48407)
* @tonywu71
    * Add NeoMME and NeoMME-Retriever (#47992)
* @Dovis01
    * [Docs]: Update GLM 5.3 (#48401)
    * [Docs] Change 5.3 Flash pos in toc (#48366)
    * [Glm 5.3 Flash] GLM 5.3 Flash Support (#48342)
* @pengzhiliang
    * Implement VibeVoice  (#40546)

## 笔记


