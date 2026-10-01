---
slug: huggingface-transformers-release-5180
name: 'huggingface/transformers: Release 5.18.0'
builder: huggingface
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
url: https://github.com/huggingface/transformers/releases/tag/v5.18.0
canonical_url: https://github.com/huggingface/transformers/releases/tag/v5.18.0
summary: "## New Model additions\r\n\r\n\r\n### Nemotron 3 Diarization\r\n\r\n<img width=\"1680\" height=\"\
  900\" alt=\"image\" src=\"https://github.com/user-attachments/assets/fe735cb3-9e5b-43ad-8f60-9dec8425aec7\"\
  \ />\r\n\r\nNemotron 3 Diarization is an open-weight streaming speaker diarization model designed to\
  \ determine \"who spoke when\" in real-world audio. It supports both streaming and offline inference,\
  \ handles up to eight speakers, and orders speaker outputs by each speaker's first arrival in the input\
  \ audio.\r\n\r\nThe model uses the Arrival-Order Speaker Cache (AOSC) [1](https://huggingface.co/papers/2507.18446)\
  \ and FIFO queue introduced for Streaming Sortformer [1](https://huggingface.co/papers/2507.18446),\
  \ [2](https://huggingface.co/papers/2409.06656). A single checkpoint supports configurable latency profiles,\
  \ from an 80 ms input buffer to a 30.4 s offline-style buffer, and configurable output frame resolution\
  \ in multiples of 10 ms. With chunked inference, the maximum audio duration is not limited.\r\n\r\n\
  **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron3_diarization)\r\
  \n* Add Nemotron3Diarization (#49056) by @eustlb in [#49056](https://github.com/huggingface/transformers/pull/49056)\r\
  \n\r\n### NemotronH Omni\r\n\r\nNemotronH Omni is a multimodal reasoning model from NVIDIA that pairs\
  \ the [NemotronH](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron_h) hybrid\r\n\
  Mamba-Transformer language model with a [RADIO](https://huggingface.co/docs/transformers/main/en/model_doc/radio)\
  \ vision encoder and an optional Parakeet-based sound encoder.\r\nImage (and video) patches are projected\
  \ through a RADIO tower and a pixel-shuffle MLP into the language model's\r\nembedding space at the\
  \ `<image>` / `<video>` context-token positions; audio clips are projected in the same way at\r\n`<audio>`\
  \ positions. The result is a single autoregressive model that reasons jointly over text, images, video\
  \ and\r\nsound.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron_h_omni)\r\
  \n* Add support for Nemotron Omni (#46509) by @meatybobby in [#46509](https://github.com/huggingface/transformers/pull/46509)\r\
  \n\r\n### HyperCLOVAX Vision V2\r\n\r\nHyperCLOVAX Vision V2 is a multimodal vision-language model developed\
  \ by NAVER. It combines the [HyperClovaX](https://huggingface.co/docs/transformers/main/en/model_doc/hyperclovax)\
  \ language model backbone with a [Qwen2.5-VL](https://huggingface.co/docs/transformers/main/en/model_doc/qwen2_5_vl)\
  \ vision encoder. The model supports text, image, and video inputs and is capable of chain-of-thought\
  \ reasoning via built-in thinking tokens (`<think>...</think>`).\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hyperclovax_vision_v2)\r\
  \n* add HyperClovaX Vision (#44314) by @jp1924 in [#44314](https://github.com/huggingface/transformers/pull/44314)\r\
  \n\r\n### GTE\r\n\r\nGTE was proposed in [mGTE: Generalized Long-Context Text Representation and Reranking\
  \ Models for Multilingual Text Retrieval](https://huggingface.co/papers/2407.19669) by Xin Zhang, Yanzhao\
  \ Zhang, Dingkun Long, Wen Xie, Ziqi Dai, Jialong Tang, Huan Lin, Baosong Yang, Pengjun Xie, Fei Huang,\
  \ Meishan Zhang, Wenjie Li and Min Zhang.\r\n\r\nGTE is a BERT-style bidirectional encoder that replaces\
  \ absolute position embeddings with RoPE, uses a gated MLP, and applies layer normalization after each\
  \ residual connection. The same architecture backs Alibaba's `gte-*-v1.5`, `gte-multilingual-*` and\
  \ `gte-en-mlm-*` checkpoints as well as Snowflake's `snowflake-arctic-embed-m-v2.0`.\r\n\r\n**Links:**\
  \ [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/gte)\r\n* model: Add GTE\
  \ to Transformers (#48416) by @harshaljanjani in [#48416](https://github.com/huggingface/transformers/pull/48416)\r\
  \n\r\n\r\n## Breaking changes\r\n\r\n* \U0001F6A8 [ROCm] gpt-oss: route FA3 to aiter-flash-attn, generate\
  \ ROCm fixtures (#46837) by @Abdennacer-Badaoui\r\n* \U0001F6A8 Speed up detr image processing (#48066)\
  \ by @guarin\r\n* \U0001F6A8 Remap indexers layer_type (#48974) by @Cyrilvallez\r\n* \U0001F6A8 [vLLM]\
  \ Fix video token counting for Transformers backend video inputs (Part 1) (#48894) by @harshaljanjani\r\
  \n* \U0001F6A8 \U0001F6A8Bring some dinos to modern standards (#46266) by @molbap\r\n* :rotating_light:\
  \ [`Kernels`] Bump version (#48714) by @vasqu\r\n\r\n\r\n## Bugfixes and improvements\r\n\r\n* fix incorrect\
  \ hub tokenizer class (#48641) by @itazap\r\n* [CI] Deduplicate Nvidia/AMD CI reply comments and add\
  \ headers (#48655) by @ydshieh\r\n* Update dev (#48654) by @vasqu\r\n* [tests] Fix NougatModelIntegrationTest:\
  \ pin artifact revision and update golden values (#48638) by @ydshieh\r\n* [fix] Fix GlmOcr integration\
  \ tests: wrong token IDs and image token decode bug (#48650) by @ydshieh\r\n* [GLM 5.3 Flash] Preserve\
  \ original names when saving text checkpoints (#48676) by @Dovis01\r\n* Register activation kernel layers\
  \ on XPU (#47858) by @jiqing-feng\r\n* Mirror the registered pytree flatten when building automatic\
  \ dynamic shapes (#48578) by @IlyasMoutawwakil\r\n* Fix `AutoImageProcessor` requiring torchvision when\
  \ only Pillow is installed (#48616) by @blipbyte\r\n* Assert cached decode matches recomputing without\
  \ a cache (#48289) by @IlyasMoutawwakil\r\n* [higgs_audio_v2] Fix: use config.num_codebooks in audio\
  \ labels tensor (Simple Fix!) (#48560) by @b-re-w\r\n* [`MoE`] Fix eager EP (#48653) by @vasqu\r\n*\
  \ [MusicgenMelody] Fix conditioning silently dropped at generation step 0 (#48679) by @ydshieh\r\n*\
  \ Fix deepspeed ci (#48640) by @SunMarc\r\n* Synthetic test assets (#48589) by @tarekziade\r\n* Skip\
  \ the expert-parallel sentinel masking when expert parallelism is off (#48201) by @qgallouedec\r\n*\
  \ [Fix] yolos offload issue (#48688) by @molbap\r\n* [serge] Fix 2 integration tests for model `minimax`\
  \ failing with `output_mismatch` (tensor values differ (2)) (#48515) by @sergereview[bot]\r\n* [serge]\
  \ Fix 2 integration tests for model `mistral` failing with `other` (other (2)) (#48429) by @sergereview[bot]\r\
  \n* Fix Qwen2.5-VL temporal RoPE for fractional video intervals (#48669) by @yeyeyeping\r\n* Fix slow\
  \ integration tests on XPU (#48611) by @jiqing-feng\r\n* QA: Added a `MemoryCleanupMixin` class for\
  \ tests (#48681) by @tarekziade\r\n* [serge] Fix 1 integration test for model `flex_olmo` failing with\
  \ `other` (other (1)) (#48668) by @sergereview[bot]\r\n* Fix D-FINE / RT-DETR main loss being computed\
  \ over the denoising queries (#48528) by @stefan-it\r\n* [CI] Replace hardcoded username allowlists\
  \ with author_association check in workflow triggers (#48712) by @ydshieh\r\n* Add flash_attention_4\
  \ in attn_implementation AutoModel docstring (#48684) by @3manifold\r\n* Keep the expert-parallel sentinel\
  \ slots out of the router gradient (#48689) by @qgallouedec\r\n* [DeepseekV3] OOM cascade root-cause\
  \ investigation (generator ref leak in conversion_mapping) (#48720) by @ydshieh\r\n* Use huggingface_hub\
  \ httpx export (#48685) by @Wauplin\r\n* unifying device_mesh init to enable PP + TP inference (#48155)\
  \ by @3outeille\r\n* Enable FSDP2 + expert parallelism via a 2-D (fsdp, tp) device mesh (#48516) by\
  \ @qgallouedec\r\n* Switch daily CI to torch 2.14 — update expected outputs (#48750) by @ydshieh\r\n\
  * fix videomae load error (#48675) by @sywangyi\r\n* Fix silently random-initializing `RTDetrModel`/`SEWDForCTC`\
  \ loads (wrong `base_model_prefix`) (#48744) by @<NOT FOUND>\r\n* Fix Glm4vMoeIntegrationTest: offload_folder\
  \ + MemoryCleanupMixin (#48776) by @ydshieh\r\n* [InternVL] Normalize num_patches before np.cumsum (#48469)\
  \ by @lorenzozanee\r\n* Kernel api doc, part 2 (#46889) by @michaelbenayoun\r\n* Fix hidden state selection\
  \ on Gemma4 assistant's first prefill step (#48704) by @glistening\r\n* Fix inkling embedding norm (#48786)\
  \ by @Cyrilvallez\r\n* Fix TextToAudioPipeline crash for tokenizer-only models (#48505) by @jiqing-feng\r\
  \n* Cast pixel values to the patch embedding dtype in DeepSeek-OCR-2 (#48632) by @jiqing-feng\r\n* add\
  \ kernel mapping entry for RMSNormGated, KDA, Conv1D on XPU (#48702) by @kaixuanliu\r\n* Bump `peft`\
  \ version requirement (#48716) by @shniubobo\r\n* [serge] Fix 12 integration tests for model `edgetam`\
  \ failing with `import_or_config` (other (12)) (#48322) by @sergereview[bot]\r\n* Restore legacy tensor-parallel\
  \ initialization for compatibility (#48797) by @3outeille\r\n* Fix kosmos flaky test (#48800) by @IlyasMoutawwakil\r\
  \n* Add integration tests for MuseGlimmerAssistantModel (#48796) by @ydshieh\r\n* Fix `AutoModel.from_pretrained`\
  \ not restoring `modules_to_save` weights (#48595) by @shniubobo\r\n* [docs] mrope and axial rope (#48717)\
  \ by @stevhliu\r\n* Fix decoder only path for older bert variants (#48785) by @Cyrilvallez\r\n* [Fix]\
  \ Clean-up ternaries in the DeepSeek family (#48447) by @remi-or\r\n* [utils] Add MUSA support for Flash\
  \ Attention 2 (#48612) by @XiaomingFun233\r\n* [generate] Drop attention mask early without padding\
  \ (#48814) by @Cyrilvallez\r\n* Pin utf-8 in test_can_init_all_missing_weights source read (Windows\
  \ non-UTF-8 locale fix) (#48819) by @dltsum\r\n* Relax static-cache tolerance in test_generate_with_static_cache\
  \ (1e-5 → 5e-5) (#48815) by @ydshieh\r\n* Detect nested rope_parameters without relying on layer_types\
  \ (#48798) by @hmellor\r\n* Support for MoE in the GGUF integration (#48529) by @SunMarc\r\n* [docs]\
  \ gguf (#46357) by @stevhliu\r\n* [apply_chat_template] pass sampling_rate to call (#48794) by @eustlb\r\
  \n* [CI] Add link checker (#48160) by @stevhliu\r\n* Qwen3.8 GGUF (#48660) by @SunMarc\r\n* docs: fix\
  \ broken #combining-with-fsdp2 anchor in expert_parallelism.md (#48854) by @ydshieh\r\n* [GPTNeoXJapanese]\
  \ Fix RoPE ignoring partial_rotary_factor (#48652) by @blipbyte\r\n* QA: deactivate rule 41 (#48852)\
  \ by @tarekziade\r\n* Fix `reset` on the dynamic cache layers (#48809) by @jiqing-feng\r\n* [generate]\
  \ Make all methods and logits processors agnostic to lm_head output size (#48846) by @Cyrilvallez\r\n\
  * Fix kosmos (#48853) by @Cyrilvallez\r\n* Add test for causal only variant of some encoder-decoder\
  \ models (#48760) by @nandan2003\r\n* Fix ESMFold2 ligand iPLDDT weighting: mol_type non-polymer code\
  \ is 3, not 4 (#48831) by @faustomilletari\r\n* Fix flaky RfDetr test_save_load (#48869) by @ydshieh\r\
  \n* fix(ci): harden GitHub Actions workflows (#48160) (#48834) by @hf-security-analysis[bot]\r\n* Fix\
  \ Glm4MoeIntegrationTest: split into 3 tests, switch to GLM-4.5-Air (#48820) by @ydshieh\r\n* Fix `StaticCache`\
  \ for Mllama and enable `torch.compile` (#48141) by @jiqing-feng\r\n* Fix Minimax M2 partial_rotary_factor\
  \ by remapping legacy rotary_dim (#48486) by @dajiaohuang\r\n* Fix Pixtral image processor do_pad option\
  \ (#48872) by @jzakrzew\r\n* [CB] Add pause mechanism (#48462) by @remi-or\r\n* Fix DFlash sampled candidates\
  \ losing the batch dimension (#48281) by @VaggelisGian\r\n* Fix sliding window cache when assistant\
  \ model calls generate (#48280) by @VaggelisGian\r\n* Fix GLM rope_parameters dict shared mutation across\
  \ test instances (#48895) by @ydshieh\r\n* [`feat`] Allow untying `hidden_states[-1]` from `last_hidden_state`\
  \ via the model config (#48087) by @tomaarsen\r\n* Fix Idefics2 padding when the first example has no\
  \ image (#48753) by @Arnavsharma2\r\n* Don't fail model loading when the accelerator can't report free\
  \ memory (#48136) by @studioego\r\n* [Improvement] Rework the docstring and comments of mHC (#48888)\
  \ by @remi-or\r\n* [serge] Fix 3 integration tests for model `deepseek_vl` failing with `other` (other\
  \ (3)) (#48536) by @sergereview[bot]\r\n* Add auto_docstring task model overrides (#47815) by @guarin\r\
  \n* Make LongcatFlashConfig self-consistent without building the model (#48899) by @hmellor\r\n* [`DSA`]\
  \ Only save latents on dsa with indexer as well (#48876) by @vasqu\r\n* [Chat Parsing] Coerce oneOf\
  \ tool arguments (#48719) by @yonigozlan\r\n* Always materialize the causal mask in Doge so sdpa stays\
  \ causal (#48821) by @blipbyte\r\n* Fix docstring argument names that don't match signatures (#48474)\
  \ by @IshaanPotle\r\n* Mark test_generate_with_static_cache as flaky for olmo and bigbird_pegasus (#48856)\
  \ by @ydshieh\r\n* Clean up some MoE models' integration tests (#48833) by @ydshieh\r\n* Fix T5 tied\
  \ weights order for lm_head (#48238) by @vaibhavmashal\r\n* Size the device_map buffer from the largest\
  \ leaf module (#47211) by @dhruv7477\r\n* Fix compile cache tests (#48923) by @Cyrilvallez\r\n* Update\
  \ arXiv citation in NeoMME model doc (#48926) by @tonywu71\r\n* Standardise Aria's MoE onto the experts\
  \ interface (#48907) by @hmellor\r\n* Fix possessive typo in Whisper long-form warning (#48877) by @erikdw\r\
  \n* Modular conversion small fix (#48934) by @zucchini-nlp\r\n* fix(vibevoice-asr): use integer ceiling\
  \ division for audio token count (#48864) by @ege-arhan\r\n* Improve lazy import error messages (#48602)\
  \ by @karatarassul4-max\r\n* Fix tests due to dropping attn mask (#48903) by @SunMarc\r\n* docs: fix\
  \ docstring parameters that do not match signatures (#48904) by @simpleqt\r\n* DOC: Improve documentation\
  \ for remap_legacy_layer_types function (#48651) by @mathewOracle\r\n* Align special tokens on the text\
  \ config (#48847) by @qgallouedec\r\n* docs: fix dead doc links in i18n READMEs and the xlnet docstring\
  \ (#48905) by @simpleqt\r\n* Fix AXK2 integration test: update CUDA expected text and rename class (#48941)\
  \ by @ydshieh\r\n* Resolve the Hub revision once per load instead of passing a private _commit_hash\
  \ around (#47611) by @Wauplin\r\n* Keep image processor backends in sync on keys and dtypes (#48739)\
  \ by @yupengtang\r\n* Fix infeasible cost matrix errors in hugarian matcher losses (#47730) by @guarin\r\
  \n* Fix more stuff (#48979) by @zucchini-nlp\r\n* Skip an unnecessary image copy in the torchvision\
  \ image normalization path (#48897) by @jzakrzew\r\n* Better attn default for gguf (#48935) by @SunMarc\r\
  \n* Add pose estimation keypoint preprocessing to Sapiens2ImageProcessor (#47199) by @Sainava\r\n* Fix\
  \ image processor class-level size mutation and min_pixels handling (#48916) by @Gracy769\r\n* Contract\
  \ the mamba2 chunk scan with einsum instead of broadcast-then-sum (#48978) by @tarekziade\r\n* Fix typos\
  \ in DeepseekV4 comments (#48953) by @Janiarafath\r\n* Reduce peak memory in examples_torch CI job (OOM\
  \ fix) (#48983) by @ydshieh\r\n* Fix vibevoice TTS batched audio index (#48902) by @ebezzam\r\n* [CB]\
  \ [Major] Upgrade the cache to support different attention types (#47809) by @remi-or\r\n* Fix SwitchTransformers\
  \ Top1 router: raw logits, expert capacity accounting, and router losses (#48421) by @yurekami\r\n*\
  \ Fix Qwen3OmniMoeIntegrationTest OOM (#48987) by @ydshieh\r\n* Let `prefix_allowed_tokens_fn` override\
  \ model `-inf` and raise an exception on unsatisfiable generation constraints. (#48927) by @ksh108405\r\
  \n* [generate] Simplify candidate generators by removing required `update_candidate_strategy` (#48982)\
  \ by @Cyrilvallez\r\n* [generate] Always correctly restrict assisted decoding with max length/eos token\
  \  (#48981) by @Cyrilvallez\r\n* QA: applied ruff rule PLW1514 (#48990) by @tarekziade\r\n* Update tokenizer\
  \ gguf support  (#48656) by @SunMarc\r\n* [vLLM] Fix video token counting for Transformers backend video\
  \ inputs (Part 2) (#48900) by @harshaljanjani\r\n* Update ggml kernels path  (#48991) by @SunMarc\r\n\
  * Enable compressed-tensors FP8 kernels on MPS (torch >= 2.15) (#48985) by @Isalia20\r\n* Fix mps autocast\
  \ handling in rotary embeddings (#49006) by @Isalia20\r\n* Fix static cache per layer head shapes (#48619)\
  \ by @dacorvo\r\n* Summarization examples: download NLTK punkt_tab, not punkt (#49014) by @davanstrien\r\
  \n* [docs] Fix legacy hf CLI references (transformers) (#48988) by @Wauplin\r\n* Fix RecurrentGemma\
  \ compiled generation with StaticCache (#48961) by @sywangyi\r\n* updated GraniteMoeHybrid expectations\
  \ (CPU) (#49016) by @tarekziade\r\n* OpenVINO HF Exporter (#47003) by @IlyasMoutawwakil\r\n* fix noisy\
  \ comments (#49013) by @tarekziade\r\n* Fix assisted decoding for VLM due to dropping attn mask  (#49019)\
  \ by @SunMarc\r\n* Deprecate min-max pixels (#49021) by @zucchini-nlp\r\n* Keep special token ids the\
  \ tokenizer does not define (#48708) by @albertvillanova\r\n* Added more usage of MemoryCleanupMixin\
  \ (#49011) by @tarekziade\r\n* Shorten noisy OpenVINO SDPA comment (#49033) by @tarekziade\r\n* PEFT\
  \ x Dtensor-based TP integration (#48485) by @michaelbenayoun\r\n* fix(zamba):  add use_associative_scan\
  \ config flag to avoid torch.compile slowdown (#48331) by @msnliu\r\n* Scope GITHUB_TOKEN permissions\
  \ per job (#49046) by @hf-security-analysis[bot]\r\n* Fix mask creation not being skipped under `torch.compile`\
  \ (#48975) by @jiqing-feng\r\n* [Chat] Loading GGUF models served with the Chat CLI (#49031) by @ariG23498\r\
  \n* Pin GitHub Actions to commit SHAs (#49049) by @hf-security-analysis[bot]\r\n* Only seed numpy in\
  \ BigBird block-sparse attention during training (#49037) by @jiqing-feng\r\n* QA: Fix llama4 leak (#49042)\
  \ by @tarekziade\r\n* Fix startup failures: drop permissions reusable-workflow callers cannot grant\
  \ (#49055) by @paulinebm\r\n* Fix startup failures: drop pull-requests: read from check_failed_tests.yml\
  \ (#49057) by @paulinebm\r\n* Register the remaining mamba-ssm kernel layers on XPU (#49035) by @jiqing-feng\r\
  \n* Add workflow for building XPU CI Docker images (#49039) by @regisss\r\n* Fix assistant masks for\
  \ processors (#48793) by @Rocketknight1\r\n* Add MPS maintainer (#49052) by @Rocketknight1\r\n* [docs]\
  \ Loading behavior (#49023) by @stevhliu\r\n* [Nemotron3Diarization] nit: hub pr merged to main (#49065)\
  \ by @eustlb\r\n* fix(ci): harden GitHub Actions workflows (#49057) (#49059) by @hf-security-analysis[bot]\r\
  \n* Honor `config.output_router_logits` in the MoE VLM wrappers (#48885) by @qgallouedec\r\n* Fix XPU\
  \ Docker image build (#49073) by @regisss\r\n* Fix assisted eos token condition (#49075) by @Cyrilvallez\r\
  \n* [serge] Fix OOM in Moshi integration tests with MemoryCleanupMixin (#48839) by @sergereview[bot]\r\
  \n* Fix odd head_dim validation for RoPE configurations (#48524) by @somuai\r\n* Keep already-decoded\
  \ array arguments unchanged (#49062) by @yonigozlan\r\n* Fix NaN in Parakeet eager attention with padded\
  \ batches (#49070) by @ArthurZucker\r\n* Bump huggingface_hub upper bound to <3.0 (transformers) (#49083)\
  \ by @Wauplin\r\n* Keep `attention_mask` as `None` in OPT's causal mask creation (#49002) by @jiqing-feng\r\
  \n* Add `Trainer.end` (#48875) by @qgallouedec\r\n* Add image processing tester init (#48829) by @guarin\r\
  \n* [Executorch] Add MLX recipe (#48910) by @metascroy\r\n* [Zamba] Fix associative scan breaking ONNX\
  \ export and OOM in integration test (#49092) by @ydshieh\r\n* Fix RGB early-return skipping PNG tRNS\
  \ compositing (#49005) by @cs-fisha\r\n* Use namespaced dataset ids in docs and PyTorch examples (#49017)\
  \ by @davanstrien\r\n* Fix MaskFormerSwin attention mask dtype to follow hidden states (#49032) by @kaixuanliu\r\
  \n* [NemotronH-Omni] Fix device mismatch in test tensor creation (#49102) by @ydshieh\r\n* [serge] Fix\
  \ 2 integration tests for model `cvt` failing with `output_mismatch` (tensor values differ (2)) (#49076)\
  \ by @sergereview[bot]\r\n* [serge] Fix 2 integration tests for model `hy_v3` failing with `output_mismatch`\
  \ (tensor values differ (2)) (#49068) by @sergereview[bot]\r\n* [serge] Fix 2 integration tests for\
  \ model `pvt_v2` failing with `other` (#49067) by @sergereview[bot]\r\n* Keep the eos ids the config\
  \ declares (#49082) by @albertvillanova\r\n* Use grouped_mm on TPU devices under torch.compile (#49097)\
  \ by @salkan0\r\n* [serge] Fix 2 integration tests for model `jamba` failing with `other` (other (2))\
  \ (#49044) by @sergereview[bot]\r\n* Remap the legacy Gemma 1 hidden_act in the config post-init (#49084)\
  \ by @PCfVW\r\n* Fix exporters import on torch < 2.9 (is_contiguous_or_false) (#49124) by @ydshieh\r\
  \n* [gemma3n] fix audio test fixture: use hf_hub_download instead of load_dataset (#49128) by @ydshieh\r\
  \n* qwen3 models map to wrong tokenizer class on the hub (#49116) by @itazap\r\n* Restore the Unicode\
  \ whitespace set in the GPT-SW3 tokenizer (#48912) by @David-Wu1119\r\n* [AMD] Fix some integration\
  \ tests (#49153) by @Abdennacer-Badaoui\r\n* [Gemma] Fix test_model_7b_fp16_static_cache expected value\
  \ for cuda 8 after #49084 (#49133) by @ydshieh\r\n* Fix UMT5 decoder self-attention not being causal\
  \ (#49135) by @the-cross-art\r\n* Skip flash tests that fall back to a hub kernel when kernels is missing\
  \ (#49129) by @Abdennacer-Badaoui\r\n* Auto generate model inits (#47829) by @guarin\r\n* Fix get_json_schema\
  \ dropping items/enum for unions of list/dict/Literal types (#49136) by @JoeyTan21\r\n* Pick the default\
  \ flash implementation based on the current hardware (#49109) by @Abdennacer-Badaoui\r\n* Deprecate\
  \ the use_mamba_kernels config flag that no longer has any effect (#49155) by @albertvillanova\r\n*\
  \ [CI] ssh-runner: add optional cache_type input to switch between bucket and EFS runners (#49159) by\
  \ @ydshieh\r\n* [generation] Encode multimodal data only once (#45783) by @zucchini-nlp\r\n* No more\
  \ -hf repo names for ESMC (#49158) by @Rocketknight1\r\n* [MPS] Remove cu_seqlens_k clone workaround\
  \ for metal-flash-sdpa (#49091) by @Isalia20\r\n* [PerceptionLM] Restore test_inputs_embeds overrides\
  \ to fix flaky test (#49165) by @ydshieh\r\n* [CB] Fix failing tests discovered when using the B200\
  \ (#49171) by @remi-or\r\n* [imagegpt/vilt/trocr] fix cache fixture tests: use hf_hub_download instead\
  \ of load_dataset (#49178) by @ydshieh\r\n* Fix lost call (#49163) by @molbap\r\n* Document image_like_kwargs\
  \ (#49180) by @guarin\r\n* [CacheHardIntegrationTest] use dedicated safetensors repo to fix Xet bucket\
  \ cache corruption (#49182) by @ydshieh\r\n* Document running the example scripts on Hugging Face Jobs\
  \ (#49050) by @davanstrien\r\n* Fix backslash handling in generate flag values in transformers chat\
  \ (#48709) by @JHC56\r\n* Finish removing the MPS autocast workaround (#49157) by @rubenG1009\r\n* Fix\
  \ Trainer checkpoint resume crashing on CPU with multiple processes (#49123) by @neevmodh\r\n* Fix command\
  \ syntax for optimum-cli export (#46451) by @Ahwar\r\n* QA: fix noisy comment checker (#49184) by @tarekziade\r\
  \n* update to torch 2.14 (#49199) by @sywangyi\r\n* Video processors - general maintenance (#48251)\
  \ by @zucchini-nlp\r\n* [Parakeet] Convert NeMo's stochastic depth to layerdrop (#49191) by @Deep-unlearning\r\
  \n* [MPS] Let mps sdpa handle grouped query attention directly (#49187) by @Isalia20\r\n* Replace datasets\
  \ that no longer load with maintained uploads (#49018) by @davanstrien\r\n* Fail fast on eval OOM under\
  \ `auto_find_batch_size` (#49198) by @qgallouedec\r\n* Fix SequenceBiasLogitsProcessor edge cases: token\
  \ id 0 and prefix equal to context (#49117) by @lucaluo925\r\n* Map bare list, tuple and dict annotations\
  \ to the right JSON schema type in get_json_schema (#49145) by @825pranav\r\n* [`Kernels`] Sync mamba\
  \ version (#49205) by @vasqu\r\n* gguf user defined tokens (#49008) by @SunMarc\r\n* QA: restore masking_utils\
  \ export comment with a noqa (#49209) by @tarekziade\r\n* Fix deepstack features for mixed-input (#49177)\
  \ by @zucchini-nlp\r\n* Fix stale _added_tokens_encoder entries in cpmant and wav2vec2 (#47440) by @ishan-1010\r\
  \n* Fix additional_special_tokens data loss with extra_special_tokens (#47848) by @erichanwang\r\n*\
  \ Fix MPS GQA version gating (#49210) by @Isalia20\r\n* Add Strix Halo (gfx1151) Atlas Inference Hub-kernel\
  \ path for Qwen3.5/3.6/3.8 Gated DeltaNet (#49127) by @AzeezIsh\r\n* Fix MiniMax M3 partial 3D vision\
  \ rotary embeddings (#49164) by @cuichenx\r\n* Fix missing router_logits in Qwen3.5-MoE and other MoE\
  \ models (#49179) by @zucchini-nlp\r\n* [Nemotron3Diarization] fix streaming last stft frame dropped\
  \ (#49167) by @eustlb\r\n\r\n\r\n## Significant community contributions\r\n\r\nThe following contributors\
  \ have made significant changes to the library over the last release:\r\n\r\n* @harshaljanjani\r\n \
  \   * model: Add GTE to Transformers (#48416)\r\n    * [vLLM] Fix video token counting for Transformers\
  \ backend video inputs (Part 2) (#48900)\r\n    * \U0001F6A8 [vLLM] Fix video token counting for Transformers\
  \ backend video inputs (Part 1) (#48894)\r\n* @eustlb\r\n    * [Nemotron3Diarization] fix streaming\
  \ last stft frame dropped (#49167)\r\n    * [Nemotron3Diarization] nit: hub pr merged to main (#49065)\r\
  \n    * Add Nemotron3Diarization (#49056)\r\n    * [apply_chat_template] pass sampling_rate to call\
  \ (#48794)\r\n* @tarekziade\r\n    * QA: restore masking_utils export comment with a noqa (#49209)\r\
  \n    * QA: fix noisy comment checker (#49184)\r\n    * QA: Fix llama4 leak (#49042)\r\n    * Shorten\
  \ noisy OpenVINO SDPA comment (#49033)\r\n    * Added more usage of MemoryCleanupMixin (#49011)\r\n\
  \    * fix noisy comments (#49013)\r\n    * updated GraniteMoeHybrid expectations (CPU) (#49016)\r\n\
  \    * QA: applied ruff rule PLW1514 (#48990)\r\n    * Contract the mamba2 chunk scan with einsum instead\
  \ of broadcast-then-sum (#48978)\r\n    * QA: deactivate rule 41 (#48852)\r\n    * QA: Added a `MemoryCleanupMixin`\
  \ class for tests (#48681)\r\n    * Synthetic test assets (#48589)\r\n* @ydshieh\r\n    * [CacheHardIntegrationTest]\
  \ use dedicated safetensors repo to fix Xet bucket cache corruption (#49182)\r\n    * [imagegpt/vilt/trocr]\
  \ fix cache fixture tests: use hf_hub_download instead of load_dataset (#49178)\r\n    * [PerceptionLM]\
  \ Restore test_inputs_embeds overrides to fix flaky test (#49165)\r\n    * [CI] ssh-runner: add optional\
  \ cache_type input to switch between bucket and EFS runners (#49159)\r\n    * [Gemma] Fix test_model_7b_fp16_static_cache\
  \ expected value for cuda 8 after #49084 (#49133)\r\n    * [gemma3n] fix audio test fixture: use hf_hub_download\
  \ instead of load_dataset (#49128)\r\n    * Fix exporters import on torch < 2.9 (is_contiguous_or_false)\
  \ (#49124)\r\n    * [NemotronH-Omni] Fix device mismatch in test tensor creation (#49102)\r\n    * [Zamba]\
  \ Fix associative scan breaking ONNX export and OOM in integration test (#49092)\r\n    * Fix Qwen3OmniMoeIntegrationTest\
  \ OOM (#48987)\r\n    * Reduce peak memory in examples_torch CI job (OOM fix) (#48983)\r\n    * Fix\
  \ AXK2 integration test: update CUDA expected text and rename class (#48941)\r\n    * Clean up some\
  \ MoE models' integration tests (#48833)\r\n    * Mark test_generate_with_static_cache as flaky for\
  \ olmo and bigbird_pegasus (#48856)\r\n    * Fix GLM rope_parameters dict shared mutation across test\
  \ instances (#48895)\r\n    * Fix Glm4MoeIntegrationTest: split into 3 tests, switch to GLM-4.5-Air\
  \ (#48820)\r\n    * Fix flaky RfDetr test_save_load (#48869)\r\n    * docs: fix broken #combining-with-fsdp2\
  \ anchor in expert_parallelism.md (#48854)\r\n    * Relax static-cache tolerance in test_generate_with_static_cache\
  \ (1e-5 → 5e-5) (#48815)\r\n    * Add integration tests for MuseGlimmerAssistantModel (#48796)\r\n \
  \   * Fix Glm4vMoeIntegrationTest: offload_folder + MemoryCleanupMixin (#48776)\r\n    * Switch daily\
  \ CI to torch 2.14 — update expected outputs (#48750)\r\n    * [DeepseekV3] OOM cascade root-cause investigation\
  \ (generator ref leak in conversion_mapping) (#48720)\r\n    * [CI] Replace hardcoded username allowlists\
  \ with author_association check in workflow triggers (#48712)\r\n    * [MusicgenMelody] Fix conditioning\
  \ silently dropped at generation step 0 (#48679)\r\n    * [fix] Fix GlmOcr integration tests: wrong\
  \ token IDs and image token decode bug (#48650)\r\n    * [tests] Fix NougatModelIntegrationTest: pin\
  \ artifact revision and update golden values (#48638)\r\n    * [CI] Deduplicate Nvidia/AMD CI reply\
  \ comments and add headers (#48655)\r\n* @molbap\r\n    * Fix lost call (#49163)\r\n    * \U0001F6A8\
  \ \U0001F6A8Bring some dinos to modern standards (#46266)\r\n    * [Fix] yolos offload issue (#48688)\r\
  \n* @remi-or\r\n    * [CB] Fix failing tests discovered when using the B200 (#49171)\r\n    * [CB] [Major]\
  \ Upgrade the cache to support different attention types (#47809)\r\n    * [Improvement] Rework the\
  \ docstring and comments of mHC (#48888)\r\n    * [CB] Add pause mechanism (#48462)\r\n    * [Fix] Clean-up\
  \ ternaries in the DeepSeek family (#48447)\r\n* @jiqing-feng\r\n    * Keep `attention_mask` as `None`\
  \ in OPT's causal mask creation (#49002)\r\n    * Register the remaining mamba-ssm kernel layers on\
  \ XPU (#49035)\r\n    * Only seed numpy in BigBird block-sparse attention during training (#49037)\r\
  \n    * Fix mask creation not being skipped under `torch.compile` (#48975)\r\n    * Fix `StaticCache`\
  \ for Mllama and enable `torch.compile` (#48141)\r\n    * Fix `reset` on the dynamic cache layers (#48809)\r\
  \n    * Cast pixel values to the patch embedding dtype in DeepSeek-OCR-2 (#48632)\r\n    * Fix TextToAudioPipeline\
  \ crash for tokenizer-only models (#48505)\r\n    * Fix slow integration tests on XPU (#48611)\r\n \
  \   * Register activation kernel layers on XPU (#47858)\r\n* @Wauplin\r\n    * Bump huggingface_hub\
  \ upper bound to <3.0 (transformers) (#49083)\r\n    * [docs] Fix legacy hf CLI references (transformers)\
  \ (#48988)\r\n    * Resolve the Hub revision once per load instead of passing a private _commit_hash\
  \ around (#47611)\r\n    * Use huggingface_hub httpx export (#48685)\r\n* @meatybobby\r\n    * Add support\
  \ for Nemotron Omni (#46509)\r\n* @Sainava\r\n    * Add pose estimation keypoint preprocessing to Sapiens2ImageProcessor\
  \ (#47199)\r\n* @jp1924\r\n    * add HyperClovaX Vision (#44314)"
first_seen: '2026-09-30T16:46:27Z'
last_seen: '2026-10-01T01:18:42Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/huggingface/transformers/releases/tag/v5.18.0
  seen_at: '2026-10-01T01:18:42Z'
  metrics:
    reactions: 0
  kind: news
---

# huggingface/transformers: Release 5.18.0

## New Model additions


### Nemotron 3 Diarization

<img width="1680" height="900" alt="image" src="https://github.com/user-attachments/assets/fe735cb3-9e5b-43ad-8f60-9dec8425aec7" />

Nemotron 3 Diarization is an open-weight streaming speaker diarization model designed to determine "who spoke when" in real-world audio. It supports both streaming and offline inference, handles up to eight speakers, and orders speaker outputs by each speaker's first arrival in the input audio.

The model uses the Arrival-Order Speaker Cache (AOSC) [1](https://huggingface.co/papers/2507.18446) and FIFO queue introduced for Streaming Sortformer [1](https://huggingface.co/papers/2507.18446), [2](https://huggingface.co/papers/2409.06656). A single checkpoint supports configurable latency profiles, from an 80 ms input buffer to a 30.4 s offline-style buffer, and configurable output frame resolution in multiples of 10 ms. With chunked inference, the maximum audio duration is not limited.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron3_diarization)
* Add Nemotron3Diarization (#49056) by @eustlb in [#49056](https://github.com/huggingface/transformers/pull/49056)

### NemotronH Omni

NemotronH Omni is a multimodal reasoning model from NVIDIA that pairs the [NemotronH](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron_h) hybrid
Mamba-Transformer language model with a [RADIO](https://huggingface.co/docs/transformers/main/en/model_doc/radio) vision encoder and an optional Parakeet-based sound encoder.
Image (and video) patches are projected through a RADIO tower and a pixel-shuffle MLP into the language model's
embedding space at the `<image>` / `<video>` context-token positions; audio clips are projected in the same way at
`<audio>` positions. The result is a single autoregressive model that reasons jointly over text, images, video and
sound.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron_h_omni)
* Add support for Nemotron Omni (#46509) by @meatybobby in [#46509](https://github.com/huggingface/transformers/pull/46509)

### HyperCLOVAX Vision V2

HyperCLOVAX Vision V2 is a multimodal vision-language model developed by NAVER. It combines the [HyperClovaX](https://huggingface.co/docs/transformers/main/en/model_doc/hyperclovax) language model backbone with a [Qwen2.5-VL](https://huggingface.co/docs/transformers/main/en/model_doc/qwen2_5_vl) vision encoder. The model supports text, image, and video inputs and is capable of chain-of-thought reasoning via built-in thinking tokens (`<think>...</think>`).

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hyperclovax_vision_v2)
* add HyperClovaX Vision (#44314) by @jp1924 in [#44314](https://github.com/huggingface/transformers/pull/44314)

### GTE

GTE was proposed in [mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval](https://huggingface.co/papers/2407.19669) by Xin Zhang, Yanzhao Zhang, Dingkun Long, Wen Xie, Ziqi Dai, Jialong Tang, Huan Lin, Baosong Yang, Pengjun Xie, Fei Huang, Meishan Zhang, Wenjie Li and Min Zhang.

GTE is a BERT-style bidirectional encoder that replaces absolute position embeddings with RoPE, uses a gated MLP, and applies layer normalization after each residual connection. The same architecture backs Alibaba's `gte-*-v1.5`, `gte-multilingual-*` and `gte-en-mlm-*` checkpoints as well as Snowflake's `snowflake-arctic-embed-m-v2.0`.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/gte)
* model: Add GTE to Transformers (#48416) by @harshaljanjani in [#48416](https://github.com/huggingface/transformers/pull/48416)


## Breaking changes

* 🚨 [ROCm] gpt-oss: route FA3 to aiter-flash-attn, generate ROCm fixtures (#46837) by @Abdennacer-Badaoui
* 🚨 Speed up detr image processing (#48066) by @guarin
* 🚨 Remap indexers layer_type (#48974) by @Cyrilvallez
* 🚨 [vLLM] Fix video token counting for Transformers backend video inputs (Part 1) (#48894) by @harshaljanjani
* 🚨 🚨Bring some dinos to modern standards (#46266) by @molbap
* :rotating_light: [`Kernels`] Bump version (#48714) by @vasqu


## Bugfixes and improvements

* fix incorrect hub tokenizer class (#48641) by @itazap
* [CI] Deduplicate Nvidia/AMD CI reply comments and add headers (#48655) by @ydshieh
* Update dev (#48654) by @vasqu
* [tests] Fix NougatModelIntegrationTest: pin artifact revision and update golden values (#48638) by @ydshieh
* [fix] Fix GlmOcr integration tests: wrong token IDs and image token decode bug (#48650) by @ydshieh
* [GLM 5.3 Flash] Preserve original names when saving text checkpoints (#48676) by @Dovis01
* Register activation kernel layers on XPU (#47858) by @jiqing-feng
* Mirror the registered pytree flatten when building automatic dynamic shapes (#48578) by @IlyasMoutawwakil
* Fix `AutoImageProcessor` requiring torchvision when only Pillow is installed (#48616) by @blipbyte
* Assert cached decode matches recomputing without a cache (#48289) by @IlyasMoutawwakil
* [higgs_audio_v2] Fix: use config.num_codebooks in audio labels tensor (Simple Fix!) (#48560) by @b-re-w
* [`MoE`] Fix eager EP (#48653) by @vasqu
* [MusicgenMelody] Fix conditioning silently dropped at generation step 0 (#48679) by @ydshieh
* Fix deepspeed ci (#48640) by @SunMarc
* Synthetic test assets (#48589) by @tarekziade
* Skip the expert-parallel sentinel masking when expert parallelism is off (#48201) by @qgallouedec
* [Fix] yolos offload issue (#48688) by @molbap
* [serge] Fix 2 integration tests for model `minimax` failing with `output_mismatch` (tensor values differ (2)) (#48515) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `mistral` failing with `other` (other (2)) (#48429) by @sergereview[bot]
* Fix Qwen2.5-VL temporal RoPE for fractional video intervals (#48669) by @yeyeyeping
* Fix slow integration tests on XPU (#48611) by @jiqing-feng
* QA: Added a `MemoryCleanupMixin` class for tests (#48681) by @tarekziade
* [serge] Fix 1 integration test for model `flex_olmo` failing with `other` (other (1)) (#48668) by @sergereview[bot]
* Fix D-FINE / RT-DETR main loss being computed over the denoising queries (#48528) by @stefan-it
* [CI] Replace hardcoded username allowlists with author_association check in workflow triggers (#48712) by @ydshieh
* Add flash_attention_4 in attn_implementation AutoModel docstring (#48684) by @3manifold
* Keep the expert-parallel sentinel slots out of the router gradient (#48689) by @qgallouedec
* [DeepseekV3] OOM cascade root-cause investigation (generator ref leak in conversion_mapping) (#48720) by @ydshieh
* Use huggingface_hub httpx export (#48685) by @Wauplin
* unifying device_mesh init to enable PP + TP inference (#48155) by @3outeille
* Enable FSDP2 + expert parallelism via a 2-D (fsdp, tp) device mesh (#48516) by @qgallouedec
* Switch daily CI to torch 2.14 — update expected outputs (#48750) by @ydshieh
* fix videomae load error (#48675) by @sywangyi
* Fix silently random-initializing `RTDetrModel`/`SEWDForCTC` loads (wrong `base_model_prefix`) (#48744) by @<NOT FOUND>
* Fix Glm4vMoeIntegrationTest: offload_folder + MemoryCleanupMixin (#48776) by @ydshieh
* [InternVL] Normalize num_patches before np.cumsum (#48469) by @lorenzozanee
* Kernel api doc, part 2 (#46889) by @michaelbenayoun
* Fix hidden state selection on Gemma4 assistant's first prefill step (#48704) by @glistening
* Fix inkling embedding norm (#48786) by @Cyrilvallez
* Fix TextToAudioPipeline crash for tokenizer-only models (#48505) by @jiqing-feng
* Cast pixel values to the patch embedding dtype in DeepSeek-OCR-2 (#48632) by @jiqing-feng
* add kernel mapping entry for RMSNormGated, KDA, Conv1D on XPU (#48702) by @kaixuanliu
* Bump `peft` version requirement (#48716) by @shniubobo
* [serge] Fix 12 integration tests for model `edgetam` failing with `import_or_config` (other (12)) (#48322) by @sergereview[bot]
* Restore legacy tensor-parallel initialization for compatibility (#48797) by @3outeille
* Fix kosmos flaky test (#48800) by @IlyasMoutawwakil
* Add integration tests for MuseGlimmerAssistantModel (#48796) by @ydshieh
* Fix `AutoModel.from_pretrained` not restoring `modules_to_save` weights (#48595) by @shniubobo
* [docs] mrope and axial rope (#48717) by @stevhliu
* Fix decoder only path for older bert variants (#48785) by @Cyrilvallez
* [Fix] Clean-up ternaries in the DeepSeek family (#48447) by @remi-or
* [utils] Add MUSA support for Flash Attention 2 (#48612) by @XiaomingFun233
* [generate] Drop attention mask early without padding (#48814) by @Cyrilvallez
* Pin utf-8 in test_can_init_all_missing_weights source read (Windows non-UTF-8 locale fix) (#48819) by @dltsum
* Relax static-cache tolerance in test_generate_with_static_cache (1e-5 → 5e-5) (#48815) by @ydshieh
* Detect nested rope_parameters without relying on layer_types (#48798) by @hmellor
* Support for MoE in the GGUF integration (#48529) by @SunMarc
* [docs] gguf (#46357) by @stevhliu
* [apply_chat_template] pass sampling_rate to call (#48794) by @eustlb
* [CI] Add link checker (#48160) by @stevhliu
* Qwen3.8 GGUF (#48660) by @SunMarc
* docs: fix broken #combining-with-fsdp2 anchor in expert_parallelism.md (#48854) by @ydshieh
* [GPTNeoXJapanese] Fix RoPE ignoring partial_rotary_factor (#48652) by @blipbyte
* QA: deactivate rule 41 (#48852) by @tarekziade
* Fix `reset` on the dynamic cache layers (#48809) by @jiqing-feng
* [generate] Make all methods and logits processors agnostic to lm_head output size (#48846) by @Cyrilvallez
* Fix kosmos (#48853) by @Cyrilvallez
* Add test for causal only variant of some encoder-decoder models (#48760) by @nandan2003
* Fix ESMFold2 ligand iPLDDT weighting: mol_type non-polymer code is 3, not 4 (#48831) by @faustomilletari
* Fix flaky RfDetr test_save_load (#48869) by @ydshieh
* fix(ci): harden GitHub Actions workflows (#48160) (#48834) by @hf-security-analysis[bot]
* Fix Glm4MoeIntegrationTest: split into 3 tests, switch to GLM-4.5-Air (#48820) by @ydshieh
* Fix `StaticCache` for Mllama and enable `torch.compile` (#48141) by @jiqing-feng
* Fix Minimax M2 partial_rotary_factor by remapping legacy rotary_dim (#48486) by @dajiaohuang
* Fix Pixtral image processor do_pad option (#48872) by @jzakrzew
* [CB] Add pause mechanism (#48462) by @remi-or
* Fix DFlash sampled candidates losing the batch dimension (#48281) by @VaggelisGian
* Fix sliding window cache when assistant model calls generate (#48280) by @VaggelisGian
* Fix GLM rope_parameters dict shared mutation across test instances (#48895) by @ydshieh
* [`feat`] Allow untying `hidden_states[-1]` from `last_hidden_state` via the model config (#48087) by @tomaarsen
* Fix Idefics2 padding when the first example has no image (#48753) by @Arnavsharma2
* Don't fail model loading when the accelerator can't report free memory (#48136) by @studioego
* [Improvement] Rework the docstring and comments of mHC (#48888) by @remi-or
* [serge] Fix 3 integration tests for model `deepseek_vl` failing with `other` (other (3)) (#48536) by @sergereview[bot]
* Add auto_docstring task model overrides (#47815) by @guarin
* Make LongcatFlashConfig self-consistent without building the model (#48899) by @hmellor
* [`DSA`] Only save latents on dsa with indexer as well (#48876) by @vasqu
* [Chat Parsing] Coerce oneOf tool arguments (#48719) by @yonigozlan
* Always materialize the causal mask in Doge so sdpa stays causal (#48821) by @blipbyte
* Fix docstring argument names that don't match signatures (#48474) by @IshaanPotle
* Mark test_generate_with_static_cache as flaky for olmo and bigbird_pegasus (#48856) by @ydshieh
* Clean up some MoE models' integration tests (#48833) by @ydshieh
* Fix T5 tied weights order for lm_head (#48238) by @vaibhavmashal
* Size the device_map buffer from the largest leaf module (#47211) by @dhruv7477
* Fix compile cache tests (#48923) by @Cyrilvallez
* Update arXiv citation in NeoMME model doc (#48926) by @tonywu71
* Standardise Aria's MoE onto the experts interface (#48907) by @hmellor
* Fix possessive typo in Whisper long-form warning (#48877) by @erikdw
* Modular conversion small fix (#48934) by @zucchini-nlp
* fix(vibevoice-asr): use integer ceiling division for audio token count (#48864) by @ege-arhan
* Improve lazy import error messages (#48602) by @karatarassul4-max
* Fix tests due to dropping attn mask (#48903) by @SunMarc
* docs: fix docstring parameters that do not match signatures (#48904) by @simpleqt
* DOC: Improve documentation for remap_legacy_layer_types function (#48651) by @mathewOracle
* Align special tokens on the text config (#48847) by @qgallouedec
* docs: fix dead doc links in i18n READMEs and the xlnet docstring (#48905) by @simpleqt
* Fix AXK2 integration test: update CUDA expected text and rename class (#48941) by @ydshieh
* Resolve the Hub revision once per load instead of passing a private _commit_hash around (#47611) by @Wauplin
* Keep image processor backends in sync on keys and dtypes (#48739) by @yupengtang
* Fix infeasible cost matrix errors in hugarian matcher losses (#47730) by @guarin
* Fix more stuff (#48979) by @zucchini-nlp
* Skip an unnecessary image copy in the torchvision image normalization path (#48897) by @jzakrzew
* Better attn default for gguf (#48935) by @SunMarc
* Add pose estimation keypoint preprocessing to Sapiens2ImageProcessor (#47199) by @Sainava
* Fix image processor class-level size mutation and min_pixels handling (#48916) by @Gracy769
* Contract the mamba2 chunk scan with einsum instead of broadcast-then-sum (#48978) by @tarekziade
* Fix typos in DeepseekV4 comments (#48953) by @Janiarafath
* Reduce peak memory in examples_torch CI job (OOM fix) (#48983) by @ydshieh
* Fix vibevoice TTS batched audio index (#48902) by @ebezzam
* [CB] [Major] Upgrade the cache to support different attention types (#47809) by @remi-or
* Fix SwitchTransformers Top1 router: raw logits, expert capacity accounting, and router losses (#48421) by @yurekami
* Fix Qwen3OmniMoeIntegrationTest OOM (#48987) by @ydshieh
* Let `prefix_allowed_tokens_fn` override model `-inf` and raise an exception on unsatisfiable generation constraints. (#48927) by @ksh108405
* [generate] Simplify candidate generators by removing required `update_candidate_strategy` (#48982) by @Cyrilvallez
* [generate] Always correctly restrict assisted decoding with max length/eos token  (#48981) by @Cyrilvallez
* QA: applied ruff rule PLW1514 (#48990) by @tarekziade
* Update tokenizer gguf support  (#48656) by @SunMarc
* [vLLM] Fix video token counting for Transformers backend video inputs (Part 2) (#48900) by @harshaljanjani
* Update ggml kernels path  (#48991) by @SunMarc
* Enable compressed-tensors FP8 kernels on MPS (torch >= 2.15) (#48985) by @Isalia20
* Fix mps autocast handling in rotary embeddings (#49006) by @Isalia20
* Fix static cache per layer head shapes (#48619) by @dacorvo
* Summarization examples: download NLTK punkt_tab, not punkt (#49014) by @davanstrien
* [docs] Fix legacy hf CLI references (transformers) (#48988) by @Wauplin
* Fix RecurrentGemma compiled generation with StaticCache (#48961) by @sywangyi
* updated GraniteMoeHybrid expectations (CPU) (#49016) by @tarekziade
* OpenVINO HF Exporter (#47003) by @IlyasMoutawwakil
* fix noisy comments (#49013) by @tarekziade
* Fix assisted decoding for VLM due to dropping attn mask  (#49019) by @SunMarc
* Deprecate min-max pixels (#49021) by @zucchini-nlp
* Keep special token ids the tokenizer does not define (#48708) by @albertvillanova
* Added more usage of MemoryCleanupMixin (#49011) by @tarekziade
* Shorten noisy OpenVINO SDPA comment (#49033) by @tarekziade
* PEFT x Dtensor-based TP integration (#48485) by @michaelbenayoun
* fix(zamba):  add use_associative_scan config flag to avoid torch.compile slowdown (#48331) by @msnliu
* Scope GITHUB_TOKEN permissions per job (#49046) by @hf-security-analysis[bot]
* Fix mask creation not being skipped under `torch.compile` (#48975) by @jiqing-feng
* [Chat] Loading GGUF models served with the Chat CLI (#49031) by @ariG23498
* Pin GitHub Actions to commit SHAs (#49049) by @hf-security-analysis[bot]
* Only seed numpy in BigBird block-sparse attention during training (#49037) by @jiqing-feng
* QA: Fix llama4 leak (#49042) by @tarekziade
* Fix startup failures: drop permissions reusable-workflow callers cannot grant (#49055) by @paulinebm
* Fix startup failures: drop pull-requests: read from check_failed_tests.yml (#49057) by @paulinebm
* Register the remaining mamba-ssm kernel layers on XPU (#49035) by @jiqing-feng
* Add workflow for building XPU CI Docker images (#49039) by @regisss
* Fix assistant masks for processors (#48793) by @Rocketknight1
* Add MPS maintainer (#49052) by @Rocketknight1
* [docs] Loading behavior (#49023) by @stevhliu
* [Nemotron3Diarization] nit: hub pr merged to main (#49065) by @eustlb
* fix(ci): harden GitHub Actions workflows (#49057) (#49059) by @hf-security-analysis[bot]
* Honor `config.output_router_logits` in the MoE VLM wrappers (#48885) by @qgallouedec
* Fix XPU Docker image build (#49073) by @regisss
* Fix assisted eos token condition (#49075) by @Cyrilvallez
* [serge] Fix OOM in Moshi integration tests with MemoryCleanupMixin (#48839) by @sergereview[bot]
* Fix odd head_dim validation for RoPE configurations (#48524) by @somuai
* Keep already-decoded array arguments unchanged (#49062) by @yonigozlan
* Fix NaN in Parakeet eager attention with padded batches (#49070) by @ArthurZucker
* Bump huggingface_hub upper bound to <3.0 (transformers) (#49083) by @Wauplin
* Keep `attention_mask` as `None` in OPT's causal mask creation (#49002) by @jiqing-feng
* Add `Trainer.end` (#48875) by @qgallouedec
* Add image processing tester init (#48829) by @guarin
* [Executorch] Add MLX recipe (#48910) by @metascroy
* [Zamba] Fix associative scan breaking ONNX export and OOM in integration test (#49092) by @ydshieh
* Fix RGB early-return skipping PNG tRNS compositing (#49005) by @cs-fisha
* Use namespaced dataset ids in docs and PyTorch examples (#49017) by @davanstrien
* Fix MaskFormerSwin attention mask dtype to follow hidden states (#49032) by @kaixuanliu
* [NemotronH-Omni] Fix device mismatch in test tensor creation (#49102) by @ydshieh
* [serge] Fix 2 integration tests for model `cvt` failing with `output_mismatch` (tensor values differ (2)) (#49076) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `hy_v3` failing with `output_mismatch` (tensor values differ (2)) (#49068) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `pvt_v2` failing with `other` (#49067) by @sergereview[bot]
* Keep the eos ids the config declares (#49082) by @albertvillanova
* Use grouped_mm on TPU devices under torch.compile (#49097) by @salkan0
* [serge] Fix 2 integration tests for model `jamba` failing with `other` (other (2)) (#49044) by @sergereview[bot]
* Remap the legacy Gemma 1 hidden_act in the config post-init (#49084) by @PCfVW
* Fix exporters import on torch < 2.9 (is_contiguous_or_false) (#49124) by @ydshieh
* [gemma3n] fix audio test fixture: use hf_hub_download instead of load_dataset (#49128) by @ydshieh
* qwen3 models map to wrong tokenizer class on the hub (#49116) by @itazap
* Restore the Unicode whitespace set in the GPT-SW3 tokenizer (#48912) by @David-Wu1119
* [AMD] Fix some integration tests (#49153) by @Abdennacer-Badaoui
* [Gemma] Fix test_model_7b_fp16_static_cache expected value for cuda 8 after #49084 (#49133) by @ydshieh
* Fix UMT5 decoder self-attention not being causal (#49135) by @the-cross-art
* Skip flash tests that fall back to a hub kernel when kernels is missing (#49129) by @Abdennacer-Badaoui
* Auto generate model inits (#47829) by @guarin
* Fix get_json_schema dropping items/enum for unions of list/dict/Literal types (#49136) by @JoeyTan21
* Pick the default flash implementation based on the current hardware (#49109) by @Abdennacer-Badaoui
* Deprecate the use_mamba_kernels config flag that no longer has any effect (#49155) by @albertvillanova
* [CI] ssh-runner: add optional cache_type input to switch between bucket and EFS runners (#49159) by @ydshieh
* [generation] Encode multimodal data only once (#45783) by @zucchini-nlp
* No more -hf repo names for ESMC (#49158) by @Rocketknight1
* [MPS] Remove cu_seqlens_k clone workaround for metal-flash-sdpa (#49091) by @Isalia20
* [PerceptionLM] Restore test_inputs_embeds overrides to fix flaky test (#49165) by @ydshieh
* [CB] Fix failing tests discovered when using the B200 (#49171) by @remi-or
* [imagegpt/vilt/trocr] fix cache fixture tests: use hf_hub_download instead of load_dataset (#49178) by @ydshieh
* Fix lost call (#49163) by @molbap
* Document image_like_kwargs (#49180) by @guarin
* [CacheHardIntegrationTest] use dedicated safetensors repo to fix Xet bucket cache corruption (#49182) by @ydshieh
* Document running the example scripts on Hugging Face Jobs (#49050) by @davanstrien
* Fix backslash handling in generate flag values in transformers chat (#48709) by @JHC56
* Finish removing the MPS autocast workaround (#49157) by @rubenG1009
* Fix Trainer checkpoint resume crashing on CPU with multiple processes (#49123) by @neevmodh
* Fix command syntax for optimum-cli export (#46451) by @Ahwar
* QA: fix noisy comment checker (#49184) by @tarekziade
* update to torch 2.14 (#49199) by @sywangyi
* Video processors - general maintenance (#48251) by @zucchini-nlp
* [Parakeet] Convert NeMo's stochastic depth to layerdrop (#49191) by @Deep-unlearning
* [MPS] Let mps sdpa handle grouped query attention directly (#49187) by @Isalia20
* Replace datasets that no longer load with maintained uploads (#49018) by @davanstrien
* Fail fast on eval OOM under `auto_find_batch_size` (#49198) by @qgallouedec
* Fix SequenceBiasLogitsProcessor edge cases: token id 0 and prefix equal to context (#49117) by @lucaluo925
* Map bare list, tuple and dict annotations to the right JSON schema type in get_json_schema (#49145) by @825pranav
* [`Kernels`] Sync mamba version (#49205) by @vasqu
* gguf user defined tokens (#49008) by @SunMarc
* QA: restore masking_utils export comment with a noqa (#49209) by @tarekziade
* Fix deepstack features for mixed-input (#49177) by @zucchini-nlp
* Fix stale _added_tokens_encoder entries in cpmant and wav2vec2 (#47440) by @ishan-1010
* Fix additional_special_tokens data loss with extra_special_tokens (#47848) by @erichanwang
* Fix MPS GQA version gating (#49210) by @Isalia20
* Add Strix Halo (gfx1151) Atlas Inference Hub-kernel path for Qwen3.5/3.6/3.8 Gated DeltaNet (#49127) by @AzeezIsh
* Fix MiniMax M3 partial 3D vision rotary embeddings (#49164) by @cuichenx
* Fix missing router_logits in Qwen3.5-MoE and other MoE models (#49179) by @zucchini-nlp
* [Nemotron3Diarization] fix streaming last stft frame dropped (#49167) by @eustlb


## Significant community contributions

The following contributors have made significant changes to the library over the last release:

* @harshaljanjani
    * model: Add GTE to Transformers (#48416)
    * [vLLM] Fix video token counting for Transformers backend video inputs (Part 2) (#48900)
    * 🚨 [vLLM] Fix video token counting for Transformers backend video inputs (Part 1) (#48894)
* @eustlb
    * [Nemotron3Diarization] fix streaming last stft frame dropped (#49167)
    * [Nemotron3Diarization] nit: hub pr merged to main (#49065)
    * Add Nemotron3Diarization (#49056)
    * [apply_chat_template] pass sampling_rate to call (#48794)
* @tarekziade
    * QA: restore masking_utils export comment with a noqa (#49209)
    * QA: fix noisy comment checker (#49184)
    * QA: Fix llama4 leak (#49042)
    * Shorten noisy OpenVINO SDPA comment (#49033)
    * Added more usage of MemoryCleanupMixin (#49011)
    * fix noisy comments (#49013)
    * updated GraniteMoeHybrid expectations (CPU) (#49016)
    * QA: applied ruff rule PLW1514 (#48990)
    * Contract the mamba2 chunk scan with einsum instead of broadcast-then-sum (#48978)
    * QA: deactivate rule 41 (#48852)
    * QA: Added a `MemoryCleanupMixin` class for tests (#48681)
    * Synthetic test assets (#48589)
* @ydshieh
    * [CacheHardIntegrationTest] use dedicated safetensors repo to fix Xet bucket cache corruption (#49182)
    * [imagegpt/vilt/trocr] fix cache fixture tests: use hf_hub_download instead of load_dataset (#49178)
    * [PerceptionLM] Restore test_inputs_embeds overrides to fix flaky test (#49165)
    * [CI] ssh-runner: add optional cache_type input to switch between bucket and EFS runners (#49159)
    * [Gemma] Fix test_model_7b_fp16_static_cache expected value for cuda 8 after #49084 (#49133)
    * [gemma3n] fix audio test fixture: use hf_hub_download instead of load_dataset (#49128)
    * Fix exporters import on torch < 2.9 (is_contiguous_or_false) (#49124)
    * [NemotronH-Omni] Fix device mismatch in test tensor creation (#49102)
    * [Zamba] Fix associative scan breaking ONNX export and OOM in integration test (#49092)
    * Fix Qwen3OmniMoeIntegrationTest OOM (#48987)
    * Reduce peak memory in examples_torch CI job (OOM fix) (#48983)
    * Fix AXK2 integration test: update CUDA expected text and rename class (#48941)
    * Clean up some MoE models' integration tests (#48833)
    * Mark test_generate_with_static_cache as flaky for olmo and bigbird_pegasus (#48856)
    * Fix GLM rope_parameters dict shared mutation across test instances (#48895)
    * Fix Glm4MoeIntegrationTest: split into 3 tests, switch to GLM-4.5-Air (#48820)
    * Fix flaky RfDetr test_save_load (#48869)
    * docs: fix broken #combining-with-fsdp2 anchor in expert_parallelism.md (#48854)
    * Relax static-cache tolerance in test_generate_with_static_cache (1e-5 → 5e-5) (#48815)
    * Add integration tests for MuseGlimmerAssistantModel (#48796)
    * Fix Glm4vMoeIntegrationTest: offload_folder + MemoryCleanupMixin (#48776)
    * Switch daily CI to torch 2.14 — update expected outputs (#48750)
    * [DeepseekV3] OOM cascade root-cause investigation (generator ref leak in conversion_mapping) (#48720)
    * [CI] Replace hardcoded username allowlists with author_association check in workflow triggers (#48712)
    * [MusicgenMelody] Fix conditioning silently dropped at generation step 0 (#48679)
    * [fix] Fix GlmOcr integration tests: wrong token IDs and image token decode bug (#48650)
    * [tests] Fix NougatModelIntegrationTest: pin artifact revision and update golden values (#48638)
    * [CI] Deduplicate Nvidia/AMD CI reply comments and add headers (#48655)
* @molbap
    * Fix lost call (#49163)
    * 🚨 🚨Bring some dinos to modern standards (#46266)
    * [Fix] yolos offload issue (#48688)
* @remi-or
    * [CB] Fix failing tests discovered when using the B200 (#49171)
    * [CB] [Major] Upgrade the cache to support different attention types (#47809)
    * [Improvement] Rework the docstring and comments of mHC (#48888)
    * [CB] Add pause mechanism (#48462)
    * [Fix] Clean-up ternaries in the DeepSeek family (#48447)
* @jiqing-feng
    * Keep `attention_mask` as `None` in OPT's causal mask creation (#49002)
    * Register the remaining mamba-ssm kernel layers on XPU (#49035)
    * Only seed numpy in BigBird block-sparse attention during training (#49037)
    * Fix mask creation not being skipped under `torch.compile` (#48975)
    * Fix `StaticCache` for Mllama and enable `torch.compile` (#48141)
    * Fix `reset` on the dynamic cache layers (#48809)
    * Cast pixel values to the patch embedding dtype in DeepSeek-OCR-2 (#48632)
    * Fix TextToAudioPipeline crash for tokenizer-only models (#48505)
    * Fix slow integration tests on XPU (#48611)
    * Register activation kernel layers on XPU (#47858)
* @Wauplin
    * Bump huggingface_hub upper bound to <3.0 (transformers) (#49083)
    * [docs] Fix legacy hf CLI references (transformers) (#48988)
    * Resolve the Hub revision once per load instead of passing a private _commit_hash around (#47611)
    * Use huggingface_hub httpx export (#48685)
* @meatybobby
    * Add support for Nemotron Omni (#46509)
* @Sainava
    * Add pose estimation keypoint preprocessing to Sapiens2ImageProcessor (#47199)
* @jp1924
    * add HyperClovaX Vision (#44314)

## 笔记


