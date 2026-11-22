---
slug: huggingface-transformers-release-v5240
name: 'huggingface/transformers: Release v5.24.0'
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
url: https://github.com/huggingface/transformers/releases/tag/v5.24.0
canonical_url: https://github.com/huggingface/transformers/releases/tag/v5.24.0
summary: "# Release v5.24.0\r\n\r\n## New Model additions\r\n\r\n### Inkling 2 Mini\r\n\r\n<img width=\"\
  80%\" alt=\"image\" src=\"https://github.com/user-attachments/assets/beefb5e0-39a9-4205-ab07-0ee707af95f2\"\
  \ />\r\n\r\nInkling 2 Mini is a multimodal model from Thinking Machines Lab that accepts text and image\
  \ inputs and generates text outputs. It is a smaller sibling of Inkling 2 Small, added in v5.23.0. It\
  \ has 24 decoder layers instead of 48, and compensates with a looping mechanism in which layers 6 to\
  \ 17 run three times. A learned message-passing mechanism mixes the residuals of the previous pass into\
  \ the attention and mixture-of-experts inputs of each loop layer. The decoder has a hidden size of 2304\
  \ and routes each token to 8 of 128 experts. The image encoder, tokenizer and processor are the same\
  \ as Inkling 2 Small's.\r\n\r\nA research checkpoint ([TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research))\
  \ has the same architecture but supports a variable number of loop passes. Fewer passes are faster,\
  \ and more passes improve quality. Both checkpoints contain NVFP4 and MXFP8 quantized layers, which\
  \ are dequantized at load time.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2_loop)\
  \ | [Blog Post](https://thinkingmachines.ai/news/inkling-2-mini/) | [HF Blog Post](https://huggingface.co/blog/inkling2mini)\r\
  \n\r\n* Add Inkling2 Mini (#51050) by @guarin\r\n\r\n### Apertus 1.5\r\n\r\nApertus 1.5 is a multimodal\
  \ model from the Swiss AI Initiative that accepts text, images and audio and generates text. It extends\
  \ the Apertus language model with the EMU3.5 vision tokenizer for images and WavTokenizer for audio.\
  \ The EMU3.5 tokenizer is an image-only VQGAN with the same encoder as Chameleon's, and it assigns codes\
  \ by the largest inner product with the codebook. The media tokenizers turn images and audio into discrete\
  \ tokens, which the language backbone processes alongside text in a shared input vocabulary. The output\
  \ vocabulary contains only text tokens, so image and audio generation are not supported.\r\n\r\n**Links:**\
  \ [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/apertus1p5)\r\n\r\n* Apertus\
  \ 1.5: add model (#47662) by @RaphaelKreft\r\n\r\n### WavTokenizer\r\n\r\nWavTokenizer encodes 24 kHz\
  \ mono audio into discrete tokens using a single codebook, at 40 or 75 tokens per second depending on\
  \ the checkpoint, and reconstructs audio from those tokens. `WavTokenizerModel` encodes and decodes,\
  \ and `WavTokenizerEncoderModel` only encodes. Speech, music/audio and unified checkpoints are available.\
  \ The 40-token-per-second variant is the audio tokenizer of Apertus 1.5. Training the codec is not supported.\r\
  \n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/wavtokenizer)\
  \ | [Paper](https://huggingface.co/papers/2408.16532)\r\n\r\n* Apertus 1.5: add model (#47662) by @RaphaelKreft\r\
  \n\r\n### Dory\r\n\r\nDory is a looped (latent-recurrent) language model from NVIDIA. It uses a normalized-GPT\
  \ architecture with interleaved sliding-window and full attention layers. A shared block of layers is\
  \ applied repeatedly, so Dory can spend more compute per token. The loop count can be changed at inference\
  \ time on the same checkpoint to trade speed against quality.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/dory)\
  \ | [Paper (nGPT)](https://huggingface.co/papers/2410.01131)\r\n\r\n* Add Dory model support (#50099)\
  \ by @shan18\r\n\r\n### HY4-VL\r\n\r\nHY4-VL (Hunyuan V4 Vision-Language) combines the HYV4 mixture-of-experts\
  \ text backbone with a vision encoder for image-text and video-text generation. It supports dynamic-resolution\
  \ visual inputs and uses multimodal rotary position embeddings (mRoPE) to represent temporal and spatial\
  \ positions. It builds on the Qwen2-VL design and shares its vision patch merger with HunYuan-VL.\r\n\
  \r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hy_v4_vl)\r\
  \n\r\n* Add HY4-VL (#50877) by @vasqu\r\n\r\n### Omnilingual ASR\r\n\r\nOmnilingual ASR is a suite of\
  \ multilingual speech-recognition models from Meta FAIR that covers more than 1,600 languages. Each\
  \ model pairs a Wav2Vec2-style audio encoder with one of two heads:\r\n\r\n* **CTC** (`OmniASRForCTC`):\
  \ a linear projection to the vocabulary, decoded non-autoregressively with greedy CTC.\r\n* **Audio\
  \ language model** (`OmniASRForConditionalGeneration`): audio embeddings are projected into a Llama\
  \ decoder that generates the transcription. It optionally takes a language code (e.g. `\"eng_Latn\"\
  `), which generally improves transcription quality.\r\n\r\nBoth variants come in 300M, 1B, 3B and 7B\
  \ sizes.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/omniasr)\
  \ | [CTC Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/omniasr_ctc) | [Paper](https://huggingface.co/papers/2511.09690)\r\
  \n\r\n* Adding Omnilingual ASR models (#43265) by @ebezzam\r\n\r\n### Lara Mini\r\n\r\nLara Mini is\
  \ a multilingual base language model from Translated with 7.2B total and 0.6B active parameters per\
  \ token. It is a hybrid of linear-time recurrent layers, sliding-window attention and a few global attention\
  \ layers, each followed by a fine-grained mixture of experts. The weights are released under the CC\
  \ BY-NC-SA 4.0 license (non-commercial use) in a gated repository.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/lara_mini)\
  \ | [Paper](https://huggingface.co/papers/2611.16956)\r\n\r\n* Add Lara Mini (#50819) by @ValeGian\r\
  \n\r\n### SarvamMLA\r\n\r\nSarvamMLA is the architecture of Sarvam-105B, a 105B-parameter mixture-of-experts\
  \ language model from Sarvam AI. It combines Multi-head Latent Attention (MLA) with sparse MoE routing:\
  \ 128 routed experts with 8 active per token, plus 1 shared expert. It uses sigmoid routing with group-based\
  \ top-k selection and YaRN rotary embeddings for contexts up to 131K tokens. The architecture is the\
  \ same as DeepSeek-V3, with a custom configuration.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/sarvam_mla)\r\
  \n\r\n* Add SarvamMLA model (sarvamai/sarvam-105b) (#44569) by @aashay-sarvam\r\n\r\n### SarvamMoE\r\
  \n\r\nSarvamMoE is the architecture of Sarvam-30B, Sarvam AI's 30B-parameter mixture-of-experts model.\
  \ It uses grouped-query attention with QK normalization, and 128 routed experts with 6 active per token,\
  \ plus 1 shared expert. The architecture is the same as GLM-4-MoE, so the auto classes load it with\
  \ the GLM-4-MoE implementation and only `SarvamMoEConfig` is specific to SarvamMoE.\r\n\r\n**Links:**\
  \ [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/sarvam_moe)\r\n\r\n* Add\
  \ SarvamMoE (sarvamai/sarvam-30b) (#51023) by @hmellor\r\n\r\n### EXAONE\r\n\r\nEXAONE covers the EXAONE\
  \ 3.0, EXAONE 3.5 and EXAONE Deep language models from LG AI Research. Their architecture is the same\
  \ as Llama, so the auto classes load them with `LlamaModel` and `LlamaForCausalLM`, and only `ExaoneConfig`\
  \ is specific to EXAONE. The released checkpoints are renamed to the Llama names when loading and back\
  \ when saving, so they no longer need `trust_remote_code=True`.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/exaone)\r\
  \n\r\n* Add EXAONE (#50966) by @hmellor\r\n\r\n### Model updates\r\n\r\n* **Ling 3.1 Flash** now loads\
  \ natively through `BailingHybrid`, like Ling 3.0 in v5.20.0 (#49737) by @icavan\r\n* **Beam** gains\
  \ a `BeamForTokenClassification` head (#50634) by @AymenKallala\r\n\r\n## Breaking changes\r\n\r\n###\
  \ Cache renaming: `past_key_values` / `cache_params` → `cache` (#50585, #50730)\r\n\r\n`past_key_values`\
  \ and `cache_params` are renamed to `cache` across the library. The old names still work with a deprecation\
  \ warning; see the dedicated section below.\r\n\r\n* \U0001F6A8\U0001F6A8 Rename `past_key_values`/`cache_params`\
  \ to `cache` (#50585) by @Cyrilvallez\r\n* Bump minimal peft version for cache name compatibility (#50730)\
  \ by @Cyrilvallez\r\n\r\nAttention models used to call their cache `past_key_values`, while Mamba-style\
  \ and linear-attention models called it `cache_params`. Hybrid models therefore had to juggle two names\
  \ for the same object. There is now a single name, `cache`, everywhere: model `forward` signatures,\
  \ `generate`, `prepare_inputs_for_generation`, the masking utilities, and every `ModelOutput`.\r\n\r\
  \n```python\r\n# Before\r\noutputs = model(input_ids, past_key_values=past_key_values, use_cache=True)\r\
  \nnext_cache = outputs.past_key_values\r\n\r\n# Now\r\noutputs = model(input_ids, cache=cache, use_cache=True)\r\
  \nnext_cache = outputs.cache\r\n```\r\n\r\n* **Fully backward compatible for now**: `past_key_values=`\
  \ / `cache_params=` are renamed to `cache` automatically, with a one-time deprecation warning. Model\
  \ `forward` and `prepare_inputs_for_generation` accept the old names until **v5.40.0**, and `generate`\
  \ accepts them until **v6.0.0**. Passing both an old name and `cache` raises a `ValueError`.\r\n* **Outputs\
  \ too**: `outputs.past_key_values`, `outputs.cache_params` and `outputs[\"past_key_values\"]` still\
  \ return the cache. Output classes can also still be built with the old field names (e.g. `CausalLMOutputWithPast(past_key_values=...)`),\
  \ so most remote-code models keep working unchanged.\r\n* **Custom code**: models defined outside the\
  \ library should rename their arguments to `cache`. Layers now call `cache.update(key_states, value_states,\
  \ layer_idx, kwargs=kwargs)`, so custom `Cache` subclasses that override `update` should accept the\
  \ extra `kwargs` argument.\r\n\r\n\U0001F6A8 `peft>=0.22.0` is now required.\r\n\r\n\U0001F4DA Docs:\
  \ <https://huggingface.co/docs/transformers/main/en/kv_cache>\r\n\r\n### Multimodal Outputs\r\n\r\n\
  Generative multimodal models now return shared output classes (`MultimodalBaseModelOutputWithPast`,\
  \ `MultimodalCausalLMOutputWithPast`, and their MoE variants) instead of one output class per model.\
  \ Code that checks for a model-specific output class should switch to these.\r\n\r\n* \U0001F6A8 Multimodal\
  \ Model Output for generative LMs (#50379) by @zucchini-nlp\r\n\r\n`modeling_attn_mask_utils.py` has\
  \ been removed. Every function in it had been deprecated in favor of `transformers.masking_utils`. Remote-code\
  \ models that still import `_prepare_4d_causal_attention_mask` or `AttentionMaskConverter` from it must\
  \ move to `transformers.masking_utils`.\r\n\r\n### Other things\r\n\r\n* Remove deprecated and unused\
  \ older mask API file (#50728) by @Cyrilvallez\r\n\r\nLayoutLMv3 (and the PP-DocLayoutV2 reading-order\
  \ model that shares its code) now go through the attention interface, so SDPA and flex attention are\
  \ supported. The relative position bias is built once per forward pass and passed to attention as `position_bias`.\r\
  \n\r\n* \U0001F6A8 LayoutLMv3: support SDPA through the attention interface, build the relative position\
  \ bias once (#50688) by @14H034160212\r\n\r\n## Cache\r\n\r\nBeyond the rename, this release adds static-cache\
  \ support to assisted decoding and fixes `generate` with flex attention and a static cache. `StaticCache`\
  \ now allocates values with the value states' dtype, and the cache is kept under activation checkpointing\
  \ when gradients are off. The `is_linear` / `is_croppable` properties are fixed for hybrid linear/full-attention\
  \ models, BigBird block-sparse decoding works with a KV cache, and KV sharing is restored for the Gemma\
  \ 4 assistants.\r\n\r\n* Support static cache in assisted decoding (#49415) by @jiqing-feng\r\n* Simplify\
  \ cache handling in generate (#50910) by @Cyrilvallez\r\n* Fix generate with flex attention and a static\
  \ cache (#50864) by @tarekziade\r\n* Allocate the StaticCache values with the value states' dtype (#49554)\
  \ by @qgallouedec\r\n* Keep the cache under activation checkpointing when gradients are off (#50890)\
  \ by @qgallouedec\r\n* [cache] Fix is_linear property to correctly remove hybrid layers (#51030) by\
  \ @Cyrilvallez\r\n* Fix is_croppable property for mixed linear-full attention classes (#51028) by @Cyrilvallez\r\
  \n* Fix BigBird block-sparse decoding with a KV cache (#49984) by @jiqing-feng\r\n* fix(gemma4): Restore\
  \ KV sharing for the Gemma 4 assistants and their targets (#50531) by @harshaljanjani\r\n* Fix Dory\
  \ vocabulary resizing, loop validation, and last-loop static caching (#50982) by @shan18\r\n* Fix device\
  \ placement in `test_bc_cache_name_{forward,generate}` (#50757) by @ydshieh\r\n* Update test_dynamic_cache_hard\
  \ expected values for A10G (#50822) by @ydshieh\r\n\r\n## Generation\r\n\r\nGeneration fixes cover sampled\
  \ beam search (candidates are sorted again before finalization), constrained sampling (batch IDs are\
  \ preserved), `generate` on MPS with encoder-decoder models, and `TextStreamer`, which no longer drops\
  \ spaces or lags on text without spaces such as Chinese, Japanese and Korean. `StopStringCriteria` initializes\
  \ faster, and its cache now actually hits.\r\n\r\n* Restore sorting of sampled beam candidates before\
  \ finalization (#50754) by @BlazeSR10hawk\r\n* fix(generate): preserve batch IDs in constrained sampling\
  \ (#50883) by @BlazeSR10hawk\r\n* Fix generate for mps and encoder-decoder models (#51032) by @Cyrilvallez\r\
  \n* Fix TextStreamer dropping spaces sometimes (#51036) by @Cyrilvallez\r\n* Fix long lagging when streaming\
  \ text without spaces and NJK chars (#36708) by @CNSeniorious000\r\n* Speed up StopStringCriteria init\
  \ and fix its cache never hitting (#50780) by @TheNetherWatcher\r\n\r\n## Continuous batching\r\n\r\n\
  Continuous batching now works under `torch.inference_mode()` and finds sharded key/value projections\
  \ under any decoder path. The per-token memory estimate scales with the TP size, warmup handles async\
  \ and static inputs correctly, and an out-of-bounds error in the top-k processor is fixed.\r\n\r\n*\
  \ [CB] Scale the per-token memory estimate by the TP size (#48566) by @qgallouedec\r\n* Continuous batching:\
  \ find the sharded key/value projections under any decoder path (#50366) by @qgallouedec\r\n* Fix continuous\
  \ batching under torch.inference_mode() (#50863) by @tarekziade\r\n* [CB] Re-order the warmup block\
  \ so async warms both sets of inputs (#50868) by @remi-or\r\n* Wait for each warmup forward before the\
  \ next one rewrites the static inputs (#50353) by @qgallouedec\r\n* Fix out-of-bounds error in continuous\
  \ batching top-k processor (#50282) by @khush-patel-09\r\n* [CB] Replace test prompts with less ambiguous\
  \ ones (#50876) by @remi-or\r\n\r\n## Chat templates, parsing and serving\r\n\r\nChat parsing gets a\
  \ new `python-call-list` content parser, better handling of bare keys and duplicate XML arguments, and\
  \ three further parser fixes. `apply_chat_template` accepts message objects, and assistant masks are\
  \ correct with left truncation. `transformers serve` handles a missing Hub cache, lists loaded models\
  \ in `/v1/models`, keeps local paths containing `@`, and keeps assistant content when `tool_calls` is\
  \ empty.\r\n\r\n* [Chat Parsing] Add `python-call-list` content parser (#50619) by @nico-martin\r\n\
  * [Chat Parsing] Quote bare keys that have whitespace around them with `unquoted_keys` (#50917) by @gagan-baghel\r\
  \n* [Chat Parsing] Preserve array values when merging duplicate XML arguments (#50760) by @crunz-ailab\r\
  \n* Fix three chat parsing bugs (#50655) by @Rocketknight1\r\n* Fix apply_chat_template with message\
  \ objects (#50818) by @Rocketknight1\r\n* Fix assistant tokens mask with left truncation (#50758) by\
  \ @yibol9768-alt\r\n* fix(chat templating): isolate concurrent assistant tracking (#50673) by @BlazeSR10hawk\r\
  \n* Just a small improvement in jinja (#50635) by @zucchini-nlp\r\n* Accept argument types in parentheses\
  \ in get_json_schema docstrings (#50745) by @miinimal\r\n* [serve] Handle missing Hub cache and include\
  \ loaded models in /v1/models (#50663) by @RyanMullins\r\n* [serve] Preserve local model paths containing\
  \ '@' in ModelManager (#50662) by @RyanMullins\r\n* [serve] Keep assistant content when tool_calls is\
  \ null or empty (#50707) by @AabhasK\r\n\r\n## Pipelines\r\n\r\nMultimodal pipelines now accept media-only\
  \ inputs and string assistant prefills, keep Mistral prefills in Voxtral, stop mutating generation kwargs,\
  \ and return chat messages as `input_text` when returning tensors. `pipeline` also respects a `device_map`\
  \ that targets a single device.\r\n\r\n* fix(pipelines): support media-only inputs in AnyToAnyPipeline\
  \ (#50856) by @BlazeSR10hawk\r\n* fix(pipelines): support string assistant prefill in multimodal full-t…\
  \ (#50679) by @BlazeSR10hawk\r\n* fix: preserve Mistral prefill in Voxtral and multimodal pipelines\
  \ (#50624) by @BlazeSR10hawk\r\n* fix(pipelines): avoid mutating multimodal generation kwargs (#50786)\
  \ by @BlazeSR10hawk\r\n* Return the chat messages as input_text when multimodal pipelines return tensors\
  \ (#50816) by @burrows99\r\n* Fix `pipeline` ignoring `device_map` when it targets a single device (#50645)\
  \ by @wanhakim\r\n\r\n## Vision\r\n\r\nVision fixes cover Muse Glimmer's embedding order, GotOCR2 and\
  \ Emu3 image sizes, Kimi video inputs, NemotronH Omni video forwarding, SAM3 RoPE precision in bf16,\
  \ and DETR-family configs with `dilation=None`. SigLIP2 and LFM2-VL now process all images at once with\
  \ tensor ops. Flash Attention is turned off for multimodal models whose image mask it would drop.\r\n\
  \r\n* Fix Muse Glimmer vision embedding order (#50847) by @sid-rp\r\n* Fix GotOCR2 image size (#50810)\
  \ by @guarin\r\n* Fix Emu3 image sizes after channel format conversion (#50615) by @stefanielizeth73-art\r\
  \n* Kimi video fix (#50633) by @zucchini-nlp\r\n* Fix NemotronH_Omni_Reasoning_V3 video forwarding and\
  \ MTP vision norm weight conversion (#49839) by @meatybobby\r\n* Keep SAM3's RoPE positions in fp32\
  \ when loading in bf16 (#50938) by @qgallouedec\r\n* Fix loading DETR-family configs that store dilation=None\
  \ (#50934) by @sibisrinivasb\r\n* SigLIP2: compute the position-embedding resize for all images with\
  \ tensor ops (#50736) by @IlyasMoutawwakil\r\n* LFM2-VL: run the projector on all images at once (#50734)\
  \ by @IlyasMoutawwakil\r\n* LFM2-VL: integration expectations after #50734 (A10, MI300X) (#50923) by\
  \ @IlyasMoutawwakil\r\n* Turn off Flash Attention support for multimodal models whose image mask it\
  \ drops (#50724) by @albertvillanova\r\n\r\n## Audio\r\n\r\nAudio fixes cover the OmniASR CTC blank\
  \ token, Qwen3 Omni audio kwargs, Qwen3-ASR's `truncation=False` default, PeAudioVideo loading with\
  \ timm 1.0.31, and the audio training examples.\r\n\r\n* Fix OmniASR CTC blank token ID (#51040) by\
  \ @taking-lying-flat\r\n* Add missing past_key_values deprecation decorator to OmniASRForCondit… (#50983)\
  \ by @RyanMullins\r\n* Fix Qwen3 Omni audio kwargs forwarding (#50616) by @remote-controlled-man\r\n\
  * Restore `truncation=False` default for Qwen3-ASR audio (#50740) by @hmellor\r\n* Fixes PeAudioVideo\
  \ model loading with timm 1.0.31. In that version, t… (#50862) by @sywangyi\r\n* FIx audio training\
  \ examples. (#50672) by @ebezzam\r\n\r\n## Quantization\r\n\r\nDequantized models are now saved without\
  \ the quantizer's weight conversions, and the unquantized weights of a dequantized FP8 checkpoint are\
  \ cast to the model's dtype. The quantization docs also get a standard template for each method.\r\n\
  \r\n* Save dequantized models without the quantizer's weight conversions (#50271) by @qgallouedec\r\n\
  * Cast the unquantized weights of a dequantized FP8 checkpoint to the model's dtype (#50595) by @qgallouedec\r\
  \n* Update inkling2 quant config (#50829) by @guarin\r\n* [docs] Standard template for quantization\
  \ methods (#50848) by @stevhliu\r\n\r\n## Parallelization\r\n\r\nFSDP2 modules are resharded before\
  \ the optimizer is created, pipeline parallelism spreads layers more evenly, and TP sharding of tied\
  \ weights is fixed.\r\n\r\n* Reshard FSDP2 modules before creating the optimizer (#50535) by @qgallouedec\r\
  \n* [perf] Spread layer over PP more evenly (#50693) by @francesco-bertolotti\r\n* Fixes an issue related\
  \ to TP sharding of tied weights (#50272) by @tengomucho\r\n\r\n## Exporters\r\n\r\nExported ONNX, OpenVINO\
  \ and ExecuTorch programs load without `trust_remote_code`. Pickled `.pt2` programs, which can run arbitrary\
  \ code when loaded, now require `trust_remote_code=True`.\r\n\r\n* Exporters: ONNX, OpenVINO and ExecuTorch\
  \ programs load without trust_remote_code (#50886) by @IlyasMoutawwakil\r\n* Exporters: require trust_remote_code\
  \ to load pickled (.pt2) programs (#50813) by @IlyasMoutawwakil\r\n* Fix OpenVINO generate export tests\
  \ for xLSTM and Bark (#50765) by @ydshieh\r\n\r\n## Bugfixes and improvements\r\n\r\n* Skip flaky Kosmos2\
  \ `test_generate_from_multimodal_encoder_outputs` (#51049) by @ydshieh\r\n* Fix flaky DeepseekV32 /\
  \ Whisper / HiggsAudioV2 CUDA graph capture failures (GC inside the capture, torch 2.15) (#50899) by\
  \ @ydshieh\r\n* [docs] Fix the custom ResNet example in the customizing models guide (#50999) by @AlexxRussell\r\
  \n* [serge] Fix 2 integration tests for model `seamless_m4t_v2` failing with `output_mismatch` (list\
  \ output differs (2)) (#48553) by @sergereview[bot]\r\n* [serge] Fix 2 integration tests for model `videomae`\
  \ failing with `other` (other (2)) (#49287) by @sergereview[bot]\r\n* Always ensure correct dtype for\
  \ _keep_in_fp32_modules_strict (#50975) by @Cyrilvallez\r\n* Fix DataCollatorWithFlattening crash on\
  \ empty examples (#50984) by @fruitstash\r\n* Require transformers-mic 0.1.3 for make run-mic (#51019)\
  \ by @tarekziade\r\n* Dory tests: build the recurrent-layer configs through the model tester (#51000)\
  \ by @tarekziade\r\n* Move older-style testers of 129 more models onto static small-config defaults\
  \ (#50976) by @tarekziade\r\n* Fix UMT5 decoder scaling for untied checkpoints (#50950) by @MonikaDvorackova\r\
  \n* Move older-style testers of 123 popular models onto static small-config defaults (#50972) by @tarekziade\r\
  \n* Fix typos in the English model and decoding guides (#50974) by @Ultroncn\r\n* [serge] Fix 2 integration\
  \ tests for model `ministral3` failing with `other` (other (2)) (#49336) by @sergereview[bot]\r\n* [serge]\
  \ Fix 2 integration tests for model `regnet` failing with `output_mismatch` (tensor values differ (2))\
  \ (#47616) by @sergereview[bot]\r\n* [serge] Fix 2 integration tests for model `efficientnet` failing\
  \ with `output_mismatch` (tensor values differ (2)) (#47840) by @sergereview[bot]\r\n* [serge] Fix 2\
  \ integration tests for model `pvt_v2` failing with `output_mismatch` (tensor values differ (2)) (#49243)\
  \ by @sergereview[bot]\r\n* Follow the SentencePiece model when converting a bare `tokenizer.model`\
  \ (#50555) by @hmellor\r\n* [serge] Fix 4 integration tests for model `pvt` failing with `output_mismatch`\
  \ (tensor values differ (4)) (#47750) by @sergereview[bot]\r\n* Migrate the remaining 95 testers to\
  \ static small-config defaults (#50944) by @tarekziade\r\n* Migrate testers for 20 popular models to\
  \ static small-config defaults (#50916) by @tarekziade\r\n* Use hf-internal-testing for the tiny Dbrx\
  \ and Bloom models and the example images (#49993) by @albertvillanova\r\n* Return an empty list from\
  \ batch_decode for an empty batch (#50873) by @zaidwhy\r\n* [LFM3] Hub causal-conv1d kernels and packed\
  \ sequences (#50732) by @paulpak58\r\n* Fix NewTokenizer example in custom tokenizers guide (#50840)\
  \ by @phatstraws\r\n* [Apertus1.5] Add A10G expectations for audio and batch generation integration\
  \ tests (#50924) by @ydshieh\r\n* Check python_multipart before multipart in is_multipart_available\
  \ (#50664) by @RyanMullins\r\n* feat(ci): scan the docker images with Wiz before they are pushed (#49150)\
  \ by @rtrompier\r\n* Remove now useless keys_to_ignore_at_inference in all configs (#50911) by @Cyrilvallez\r\
  \n* [SGLang CI] Fix the VLM teardown error on CPU (follow-up of #50913) (#50914) by @ydshieh\r\n* Set\
  \ _skip_keys_device_placement directly inside PreTrainedModel (#50909) by @Cyrilvallez\r\n* [SGLang\
  \ CI] Deselect a GPU-only VLM test (#50913) by @ydshieh\r\n* [vLLM CI] Fix the FireRedASR2 and MTP test\
  \ failures (missing dependency, GPU-only test) (#50912) by @ydshieh\r\n* Fix Reformer LM head bias not\
  \ applied since the weight-loading refactor (#50811) by @ydshieh\r\n* Fix error message and remove duplicate\
  \ code in convert_slow_tokenizer.py (#50077) by @samyuktahegde\r\n* Fix first-subword label assignment\
  \ in LayoutXLM, LayoutLMv2, and MarkupLM tokenizers (#50455) by @14H034160212\r\n* Skip added-token\
  \ trie scan when no token can match (#50781) by @TheNetherWatcher\r\n* [CI report] Upload the vLLM /\
  \ SGLang CI reports to the Hub and post a summary to Slack (#50896) by @ydshieh\r\n* Use lifespan instead\
  \ of on_event in pipeline web server guide (#50858) by @phatstraws\r\n* [CI] docs-check fixes (#50279)\
  \ by @stevhliu\r\n* Expose literal tester overrides and merged small-config defaults (#50462) by @tarekziade\r\
  \n* [SGLang CI] Add failure report job (shared with vLLM CI) (#50882) by @ydshieh\r\n* [`Apertus 1.5`]\
  \ Guard behind slow for gated repo (#50884) by @vasqu\r\n* avoid running this wf from fork (#50694)\
  \ by @tarekziade\r\n* bench test reproducibility (#50504) by @tarekziade\r\n* Fix timestamps (#50503)\
  \ by @tarekziade\r\n* [SGLang CI] Test against the latest published SGLang CPU release (#50878) by @ydshieh\r\
  \n* Keep AFMoE expert biases in FP32 on BF16 load (#50687) by @annekethvij\r\n* Fix seeded collator\
  \ generator selection (#50861) by @danarkhipov\r\n* Remove no_grad decorator on all _init_weights (#50831)\
  \ by @Cyrilvallez\r\n* Remove no_grad decorator on RoPE forward (#50828) by @Cyrilvallez\r\n* Update\
  \ expected logits slice for `Qwen2MoeIntegrationTest::test_model_a2_7b_logits` on A10G (#50845) by @ydshieh\r\
  \n* Check for an empty batch in convert_to_tensors without flattening it (#49942) by @jayzuccarelli\r\
  \n* [serge] Fix 2 integration tests for model `qwen2_moe` failing with `other` (other (2)) (#49480)\
  \ by @sergereview[bot]\r\n* [serge] Fix 1 integration test for model `flint` failing with `other`, raising\
  \ `RuntimeError` (other (1)) (#50283) by @sergereview[bot]\r\n* [serge] Fix 5 integration tests for\
  \ model `qwen3_vl_moe` failing with `other`, raising `RuntimeError` (other (5)) (#50145) by @sergereview[bot]\r\
  \n* Fixing training CI again  (#50747) by @SunMarc\r\n* Fix Mistral Large 4 LeRoPE training gradients\
  \ (#50727) by @taking-lying-flat\r\n* Keep MiMo-V2-Flash's router in float32 in bfloat16 models (#50722)\
  \ by @francesco-bertolotti\r\n* Fix NanoChat inheriting an incompatible rotary kernel (#50823) by @taking-lying-flat\r\
  \n* Fix `CwmIntegrationTest` GPU OOM on multi-GPU runners (cap per-GPU `max_memory` at 70%) (#50824)\
  \ by @ydshieh\r\n* Mark `OmDetTurboModelTest::test_batching_equivalence` as flaky (`topk` query selection)\
  \ (#50815) by @ydshieh\r\n* [docs] Fix imports that fail on main in four English docs (#50817) by @burrows99\r\
  \n* Fix duplicate JetMoE router logits in auxiliary loss (#50658) by @taking-lying-flat\r\n* docs: updates\
  \ to security policy in SECURITY.md (#50711) by @Michellehbn\r\n* [serge] Fix 2 integration tests for\
  \ model `utils` failing with `output_mismatch` (list output differs (2)) (#49407) by @sergereview[bot]\r\
  \n* Fix OOM in Mamba2IntegrationTest by using MemoryCleanupMixin (#50808) by @ydshieh\r\n* [docs] Fix\
  \ the any-to-any guide example using the removed infer_device (#50792) by @burrows99\r\n* Scale the\
  \ padding-free position_ids test tolerance to the logits (#50697) by @EvanZhuang\r\n* [docs] Fix PairClassificationPipeline\
  \ example using the removed self.framework (#50789) by @burrows99\r\n* [serge] Fix 2 integration tests\
  \ for model `hrm_text` failing with `output_mismatch` (tensor values differ (2)) (#50006) by @sergereview[bot]\r\
  \n* [serge] Fix 6 integration tests for model `bloom` failing with `output_mismatch` (list output differs\
  \ (4), other (2)) (#50469) by @sergereview[bot]\r\n* [serge] Fix 2 integration tests for model `ministral`\
  \ failing with `output_mismatch` (tensor values differ (2)) (#50146) by @sergereview[bot]\r\n* [serge]\
  \ Fix 1 integration test for model `deepseek_vl_hybrid` failing with `output_mismatch` (list output\
  \ differs (1)) (#49581) by @sergereview[bot]\r\n* [serge] Fix 2 integration tests for model `ovis2`\
  \ failing with `output_mismatch` (list output differs (2)) (#50233) by @sergereview[bot]\r\n* [docs]\
  \ Replace examples using pipeline tasks removed in v5 (#50625) by @rickygrosvenor-pramanick\r\n* [CI]\
  \ Fix external links (#50685) by @stevhliu\r\n* Update A10 expected outputs of FA2 integration tests\
  \ (#50738) by @ydshieh\r\n* Revert mark linguistic generated (#50735) by @vasqu\r\n* Update dev version\
  \ (#50725) by @vasqu\r\n\r\n**Full Changelog**: [`v5.23.0...v5.24.0`](https://github.com/huggingface/transformers/compare/v5.23.0...v5.24.0)"
first_seen: '2026-11-22T02:14:43Z'
last_seen: '2026-11-22T02:14:43Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/huggingface/transformers/releases/tag/v5.24.0
  seen_at: '2026-11-22T02:14:43Z'
  metrics:
    reactions: 0
  kind: news
---

# huggingface/transformers: Release v5.24.0

# Release v5.24.0

## New Model additions

### Inkling 2 Mini

<img width="80%" alt="image" src="https://github.com/user-attachments/assets/beefb5e0-39a9-4205-ab07-0ee707af95f2" />

Inkling 2 Mini is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs. It is a smaller sibling of Inkling 2 Small, added in v5.23.0. It has 24 decoder layers instead of 48, and compensates with a looping mechanism in which layers 6 to 17 run three times. A learned message-passing mechanism mixes the residuals of the previous pass into the attention and mixture-of-experts inputs of each loop layer. The decoder has a hidden size of 2304 and routes each token to 8 of 128 experts. The image encoder, tokenizer and processor are the same as Inkling 2 Small's.

A research checkpoint ([TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)) has the same architecture but supports a variable number of loop passes. Fewer passes are faster, and more passes improve quality. Both checkpoints contain NVFP4 and MXFP8 quantized layers, which are dequantized at load time.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2_loop) | [Blog Post](https://thinkingmachines.ai/news/inkling-2-mini/) | [HF Blog Post](https://huggingface.co/blog/inkling2mini)

* Add Inkling2 Mini (#51050) by @guarin

### Apertus 1.5

Apertus 1.5 is a multimodal model from the Swiss AI Initiative that accepts text, images and audio and generates text. It extends the Apertus language model with the EMU3.5 vision tokenizer for images and WavTokenizer for audio. The EMU3.5 tokenizer is an image-only VQGAN with the same encoder as Chameleon's, and it assigns codes by the largest inner product with the codebook. The media tokenizers turn images and audio into discrete tokens, which the language backbone processes alongside text in a shared input vocabulary. The output vocabulary contains only text tokens, so image and audio generation are not supported.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/apertus1p5)

* Apertus 1.5: add model (#47662) by @RaphaelKreft

### WavTokenizer

WavTokenizer encodes 24 kHz mono audio into discrete tokens using a single codebook, at 40 or 75 tokens per second depending on the checkpoint, and reconstructs audio from those tokens. `WavTokenizerModel` encodes and decodes, and `WavTokenizerEncoderModel` only encodes. Speech, music/audio and unified checkpoints are available. The 40-token-per-second variant is the audio tokenizer of Apertus 1.5. Training the codec is not supported.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/wavtokenizer) | [Paper](https://huggingface.co/papers/2408.16532)

* Apertus 1.5: add model (#47662) by @RaphaelKreft

### Dory

Dory is a looped (latent-recurrent) language model from NVIDIA. It uses a normalized-GPT architecture with interleaved sliding-window and full attention layers. A shared block of layers is applied repeatedly, so Dory can spend more compute per token. The loop count can be changed at inference time on the same checkpoint to trade speed against quality.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/dory) | [Paper (nGPT)](https://huggingface.co/papers/2410.01131)

* Add Dory model support (#50099) by @shan18

### HY4-VL

HY4-VL (Hunyuan V4 Vision-Language) combines the HYV4 mixture-of-experts text backbone with a vision encoder for image-text and video-text generation. It supports dynamic-resolution visual inputs and uses multimodal rotary position embeddings (mRoPE) to represent temporal and spatial positions. It builds on the Qwen2-VL design and shares its vision patch merger with HunYuan-VL.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hy_v4_vl)

* Add HY4-VL (#50877) by @vasqu

### Omnilingual ASR

Omnilingual ASR is a suite of multilingual speech-recognition models from Meta FAIR that covers more than 1,600 languages. Each model pairs a Wav2Vec2-style audio encoder with one of two heads:

* **CTC** (`OmniASRForCTC`): a linear projection to the vocabulary, decoded non-autoregressively with greedy CTC.
* **Audio language model** (`OmniASRForConditionalGeneration`): audio embeddings are projected into a Llama decoder that generates the transcription. It optionally takes a language code (e.g. `"eng_Latn"`), which generally improves transcription quality.

Both variants come in 300M, 1B, 3B and 7B sizes.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/omniasr) | [CTC Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/omniasr_ctc) | [Paper](https://huggingface.co/papers/2511.09690)

* Adding Omnilingual ASR models (#43265) by @ebezzam

### Lara Mini

Lara Mini is a multilingual base language model from Translated with 7.2B total and 0.6B active parameters per token. It is a hybrid of linear-time recurrent layers, sliding-window attention and a few global attention layers, each followed by a fine-grained mixture of experts. The weights are released under the CC BY-NC-SA 4.0 license (non-commercial use) in a gated repository.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/lara_mini) | [Paper](https://huggingface.co/papers/2611.16956)

* Add Lara Mini (#50819) by @ValeGian

### SarvamMLA

SarvamMLA is the architecture of Sarvam-105B, a 105B-parameter mixture-of-experts language model from Sarvam AI. It combines Multi-head Latent Attention (MLA) with sparse MoE routing: 128 routed experts with 8 active per token, plus 1 shared expert. It uses sigmoid routing with group-based top-k selection and YaRN rotary embeddings for contexts up to 131K tokens. The architecture is the same as DeepSeek-V3, with a custom configuration.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/sarvam_mla)

* Add SarvamMLA model (sarvamai/sarvam-105b) (#44569) by @aashay-sarvam

### SarvamMoE

SarvamMoE is the architecture of Sarvam-30B, Sarvam AI's 30B-parameter mixture-of-experts model. It uses grouped-query attention with QK normalization, and 128 routed experts with 6 active per token, plus 1 shared expert. The architecture is the same as GLM-4-MoE, so the auto classes load it with the GLM-4-MoE implementation and only `SarvamMoEConfig` is specific to SarvamMoE.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/sarvam_moe)

* Add SarvamMoE (sarvamai/sarvam-30b) (#51023) by @hmellor

### EXAONE

EXAONE covers the EXAONE 3.0, EXAONE 3.5 and EXAONE Deep language models from LG AI Research. Their architecture is the same as Llama, so the auto classes load them with `LlamaModel` and `LlamaForCausalLM`, and only `ExaoneConfig` is specific to EXAONE. The released checkpoints are renamed to the Llama names when loading and back when saving, so they no longer need `trust_remote_code=True`.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/exaone)

* Add EXAONE (#50966) by @hmellor

### Model updates

* **Ling 3.1 Flash** now loads natively through `BailingHybrid`, like Ling 3.0 in v5.20.0 (#49737) by @icavan
* **Beam** gains a `BeamForTokenClassification` head (#50634) by @AymenKallala

## Breaking changes

### Cache renaming: `past_key_values` / `cache_params` → `cache` (#50585, #50730)

`past_key_values` and `cache_params` are renamed to `cache` across the library. The old names still work with a deprecation warning; see the dedicated section below.

* 🚨🚨 Rename `past_key_values`/`cache_params` to `cache` (#50585) by @Cyrilvallez
* Bump minimal peft version for cache name compatibility (#50730) by @Cyrilvallez

Attention models used to call their cache `past_key_values`, while Mamba-style and linear-attention models called it `cache_params`. Hybrid models therefore had to juggle two names for the same object. There is now a single name, `cache`, everywhere: model `forward` signatures, `generate`, `prepare_inputs_for_generation`, the masking utilities, and every `ModelOutput`.

```python
# Before
outputs = model(input_ids, past_key_values=past_key_values, use_cache=True)
next_cache = outputs.past_key_values

# Now
outputs = model(input_ids, cache=cache, use_cache=True)
next_cache = outputs.cache
```

* **Fully backward compatible for now**: `past_key_values=` / `cache_params=` are renamed to `cache` automatically, with a one-time deprecation warning. Model `forward` and `prepare_inputs_for_generation` accept the old names until **v5.40.0**, and `generate` accepts them until **v6.0.0**. Passing both an old name and `cache` raises a `ValueError`.
* **Outputs too**: `outputs.past_key_values`, `outputs.cache_params` and `outputs["past_key_values"]` still return the cache. Output classes can also still be built with the old field names (e.g. `CausalLMOutputWithPast(past_key_values=...)`), so most remote-code models keep working unchanged.
* **Custom code**: models defined outside the library should rename their arguments to `cache`. Layers now call `cache.update(key_states, value_states, layer_idx, kwargs=kwargs)`, so custom `Cache` subclasses that override `update` should accept the extra `kwargs` argument.

🚨 `peft>=0.22.0` is now required.

📚 Docs: <https://huggingface.co/docs/transformers/main/en/kv_cache>

### Multimodal Outputs

Generative multimodal models now return shared output classes (`MultimodalBaseModelOutputWithPast`, `MultimodalCausalLMOutputWithPast`, and their MoE variants) instead of one output class per model. Code that checks for a model-specific output class should switch to these.

* 🚨 Multimodal Model Output for generative LMs (#50379) by @zucchini-nlp

`modeling_attn_mask_utils.py` has been removed. Every function in it had been deprecated in favor of `transformers.masking_utils`. Remote-code models that still import `_prepare_4d_causal_attention_mask` or `AttentionMaskConverter` from it must move to `transformers.masking_utils`.

### Other things

* Remove deprecated and unused older mask API file (#50728) by @Cyrilvallez

LayoutLMv3 (and the PP-DocLayoutV2 reading-order model that shares its code) now go through the attention interface, so SDPA and flex attention are supported. The relative position bias is built once per forward pass and passed to attention as `position_bias`.

* 🚨 LayoutLMv3: support SDPA through the attention interface, build the relative position bias once (#50688) by @14H034160212

## Cache

Beyond the rename, this release adds static-cache support to assisted decoding and fixes `generate` with flex attention and a static cache. `StaticCache` now allocates values with the value states' dtype, and the cache is kept under activation checkpointing when gradients are off. The `is_linear` / `is_croppable` properties are fixed for hybrid linear/full-attention models, BigBird block-sparse decoding works with a KV cache, and KV sharing is restored for the Gemma 4 assistants.

* Support static cache in assisted decoding (#49415) by @jiqing-feng
* Simplify cache handling in generate (#50910) by @Cyrilvallez
* Fix generate with flex attention and a static cache (#50864) by @tarekziade
* Allocate the StaticCache values with the value states' dtype (#49554) by @qgallouedec
* Keep the cache under activation checkpointing when gradients are off (#50890) by @qgallouedec
* [cache] Fix is_linear property to correctly remove hybrid layers (#51030) by @Cyrilvallez
* Fix is_croppable property for mixed linear-full attention classes (#51028) by @Cyrilvallez
* Fix BigBird block-sparse decoding with a KV cache (#49984) by @jiqing-feng
* fix(gemma4): Restore KV sharing for the Gemma 4 assistants and their targets (#50531) by @harshaljanjani
* Fix Dory vocabulary resizing, loop validation, and last-loop static caching (#50982) by @shan18
* Fix device placement in `test_bc_cache_name_{forward,generate}` (#50757) by @ydshieh
* Update test_dynamic_cache_hard expected values for A10G (#50822) by @ydshieh

## Generation

Generation fixes cover sampled beam search (candidates are sorted again before finalization), constrained sampling (batch IDs are preserved), `generate` on MPS with encoder-decoder models, and `TextStreamer`, which no longer drops spaces or lags on text without spaces such as Chinese, Japanese and Korean. `StopStringCriteria` initializes faster, and its cache now actually hits.

* Restore sorting of sampled beam candidates before finalization (#50754) by @BlazeSR10hawk
* fix(generate): preserve batch IDs in constrained sampling (#50883) by @BlazeSR10hawk
* Fix generate for mps and encoder-decoder models (#51032) by @Cyrilvallez
* Fix TextStreamer dropping spaces sometimes (#51036) by @Cyrilvallez
* Fix long lagging when streaming text without spaces and NJK chars (#36708) by @CNSeniorious000
* Speed up StopStringCriteria init and fix its cache never hitting (#50780) by @TheNetherWatcher

## Continuous batching

Continuous batching now works under `torch.inference_mode()` and finds sharded key/value projections under any decoder path. The per-token memory estimate scales with the TP size, warmup handles async and static inputs correctly, and an out-of-bounds error in the top-k processor is fixed.

* [CB] Scale the per-token memory estimate by the TP size (#48566) by @qgallouedec
* Continuous batching: find the sharded key/value projections under any decoder path (#50366) by @qgallouedec
* Fix continuous batching under torch.inference_mode() (#50863) by @tarekziade
* [CB] Re-order the warmup block so async warms both sets of inputs (#50868) by @remi-or
* Wait for each warmup forward before the next one rewrites the static inputs (#50353) by @qgallouedec
* Fix out-of-bounds error in continuous batching top-k processor (#50282) by @khush-patel-09
* [CB] Replace test prompts with less ambiguous ones (#50876) by @remi-or

## Chat templates, parsing and serving

Chat parsing gets a new `python-call-list` content parser, better handling of bare keys and duplicate XML arguments, and three further parser fixes. `apply_chat_template` accepts message objects, and assistant masks are correct with left truncation. `transformers serve` handles a missing Hub cache, lists loaded models in `/v1/models`, keeps local paths containing `@`, and keeps assistant content when `tool_calls` is empty.

* [Chat Parsing] Add `python-call-list` content parser (#50619) by @nico-martin
* [Chat Parsing] Quote bare keys that have whitespace around them with `unquoted_keys` (#50917) by @gagan-baghel
* [Chat Parsing] Preserve array values when merging duplicate XML arguments (#50760) by @crunz-ailab
* Fix three chat parsing bugs (#50655) by @Rocketknight1
* Fix apply_chat_template with message objects (#50818) by @Rocketknight1
* Fix assistant tokens mask with left truncation (#50758) by @yibol9768-alt
* fix(chat templating): isolate concurrent assistant tracking (#50673) by @BlazeSR10hawk
* Just a small improvement in jinja (#50635) by @zucchini-nlp
* Accept argument types in parentheses in get_json_schema docstrings (#50745) by @miinimal
* [serve] Handle missing Hub cache and include loaded models in /v1/models (#50663) by @RyanMullins
* [serve] Preserve local model paths containing '@' in ModelManager (#50662) by @RyanMullins
* [serve] Keep assistant content when tool_calls is null or empty (#50707) by @AabhasK

## Pipelines

Multimodal pipelines now accept media-only inputs and string assistant prefills, keep Mistral prefills in Voxtral, stop mutating generation kwargs, and return chat messages as `input_text` when returning tensors. `pipeline` also respects a `device_map` that targets a single device.

* fix(pipelines): support media-only inputs in AnyToAnyPipeline (#50856) by @BlazeSR10hawk
* fix(pipelines): support string assistant prefill in multimodal full-t… (#50679) by @BlazeSR10hawk
* fix: preserve Mistral prefill in Voxtral and multimodal pipelines (#50624) by @BlazeSR10hawk
* fix(pipelines): avoid mutating multimodal generation kwargs (#50786) by @BlazeSR10hawk
* Return the chat messages as input_text when multimodal pipelines return tensors (#50816) by @burrows99
* Fix `pipeline` ignoring `device_map` when it targets a single device (#50645) by @wanhakim

## Vision

Vision fixes cover Muse Glimmer's embedding order, GotOCR2 and Emu3 image sizes, Kimi video inputs, NemotronH Omni video forwarding, SAM3 RoPE precision in bf16, and DETR-family configs with `dilation=None`. SigLIP2 and LFM2-VL now process all images at once with tensor ops. Flash Attention is turned off for multimodal models whose image mask it would drop.

* Fix Muse Glimmer vision embedding order (#50847) by @sid-rp
* Fix GotOCR2 image size (#50810) by @guarin
* Fix Emu3 image sizes after channel format conversion (#50615) by @stefanielizeth73-art
* Kimi video fix (#50633) by @zucchini-nlp
* Fix NemotronH_Omni_Reasoning_V3 video forwarding and MTP vision norm weight conversion (#49839) by @meatybobby
* Keep SAM3's RoPE positions in fp32 when loading in bf16 (#50938) by @qgallouedec
* Fix loading DETR-family configs that store dilation=None (#50934) by @sibisrinivasb
* SigLIP2: compute the position-embedding resize for all images with tensor ops (#50736) by @IlyasMoutawwakil
* LFM2-VL: run the projector on all images at once (#50734) by @IlyasMoutawwakil
* LFM2-VL: integration expectations after #50734 (A10, MI300X) (#50923) by @IlyasMoutawwakil
* Turn off Flash Attention support for multimodal models whose image mask it drops (#50724) by @albertvillanova

## Audio

Audio fixes cover the OmniASR CTC blank token, Qwen3 Omni audio kwargs, Qwen3-ASR's `truncation=False` default, PeAudioVideo loading with timm 1.0.31, and the audio training examples.

* Fix OmniASR CTC blank token ID (#51040) by @taking-lying-flat
* Add missing past_key_values deprecation decorator to OmniASRForCondit… (#50983) by @RyanMullins
* Fix Qwen3 Omni audio kwargs forwarding (#50616) by @remote-controlled-man
* Restore `truncation=False` default for Qwen3-ASR audio (#50740) by @hmellor
* Fixes PeAudioVideo model loading with timm 1.0.31. In that version, t… (#50862) by @sywangyi
* FIx audio training examples. (#50672) by @ebezzam

## Quantization

Dequantized models are now saved without the quantizer's weight conversions, and the unquantized weights of a dequantized FP8 checkpoint are cast to the model's dtype. The quantization docs also get a standard template for each method.

* Save dequantized models without the quantizer's weight conversions (#50271) by @qgallouedec
* Cast the unquantized weights of a dequantized FP8 checkpoint to the model's dtype (#50595) by @qgallouedec
* Update inkling2 quant config (#50829) by @guarin
* [docs] Standard template for quantization methods (#50848) by @stevhliu

## Parallelization

FSDP2 modules are resharded before the optimizer is created, pipeline parallelism spreads layers more evenly, and TP sharding of tied weights is fixed.

* Reshard FSDP2 modules before creating the optimizer (#50535) by @qgallouedec
* [perf] Spread layer over PP more evenly (#50693) by @francesco-bertolotti
* Fixes an issue related to TP sharding of tied weights (#50272) by @tengomucho

## Exporters

Exported ONNX, OpenVINO and ExecuTorch programs load without `trust_remote_code`. Pickled `.pt2` programs, which can run arbitrary code when loaded, now require `trust_remote_code=True`.

* Exporters: ONNX, OpenVINO and ExecuTorch programs load without trust_remote_code (#50886) by @IlyasMoutawwakil
* Exporters: require trust_remote_code to load pickled (.pt2) programs (#50813) by @IlyasMoutawwakil
* Fix OpenVINO generate export tests for xLSTM and Bark (#50765) by @ydshieh

## Bugfixes and improvements

* Skip flaky Kosmos2 `test_generate_from_multimodal_encoder_outputs` (#51049) by @ydshieh
* Fix flaky DeepseekV32 / Whisper / HiggsAudioV2 CUDA graph capture failures (GC inside the capture, torch 2.15) (#50899) by @ydshieh
* [docs] Fix the custom ResNet example in the customizing models guide (#50999) by @AlexxRussell
* [serge] Fix 2 integration tests for model `seamless_m4t_v2` failing with `output_mismatch` (list output differs (2)) (#48553) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `videomae` failing with `other` (other (2)) (#49287) by @sergereview[bot]
* Always ensure correct dtype for _keep_in_fp32_modules_strict (#50975) by @Cyrilvallez
* Fix DataCollatorWithFlattening crash on empty examples (#50984) by @fruitstash
* Require transformers-mic 0.1.3 for make run-mic (#51019) by @tarekziade
* Dory tests: build the recurrent-layer configs through the model tester (#51000) by @tarekziade
* Move older-style testers of 129 more models onto static small-config defaults (#50976) by @tarekziade
* Fix UMT5 decoder scaling for untied checkpoints (#50950) by @MonikaDvorackova
* Move older-style testers of 123 popular models onto static small-config defaults (#50972) by @tarekziade
* Fix typos in the English model and decoding guides (#50974) by @Ultroncn
* [serge] Fix 2 integration tests for model `ministral3` failing with `other` (other (2)) (#49336) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `regnet` failing with `output_mismatch` (tensor values differ (2)) (#47616) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `efficientnet` failing with `output_mismatch` (tensor values differ (2)) (#47840) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `pvt_v2` failing with `output_mismatch` (tensor values differ (2)) (#49243) by @sergereview[bot]
* Follow the SentencePiece model when converting a bare `tokenizer.model` (#50555) by @hmellor
* [serge] Fix 4 integration tests for model `pvt` failing with `output_mismatch` (tensor values differ (4)) (#47750) by @sergereview[bot]
* Migrate the remaining 95 testers to static small-config defaults (#50944) by @tarekziade
* Migrate testers for 20 popular models to static small-config defaults (#50916) by @tarekziade
* Use hf-internal-testing for the tiny Dbrx and Bloom models and the example images (#49993) by @albertvillanova
* Return an empty list from batch_decode for an empty batch (#50873) by @zaidwhy
* [LFM3] Hub causal-conv1d kernels and packed sequences (#50732) by @paulpak58
* Fix NewTokenizer example in custom tokenizers guide (#50840) by @phatstraws
* [Apertus1.5] Add A10G expectations for audio and batch generation integration tests (#50924) by @ydshieh
* Check python_multipart before multipart in is_multipart_available (#50664) by @RyanMullins
* feat(ci): scan the docker images with Wiz before they are pushed (#49150) by @rtrompier
* Remove now useless keys_to_ignore_at_inference in all configs (#50911) by @Cyrilvallez
* [SGLang CI] Fix the VLM teardown error on CPU (follow-up of #50913) (#50914) by @ydshieh
* Set _skip_keys_device_placement directly inside PreTrainedModel (#50909) by @Cyrilvallez
* [SGLang CI] Deselect a GPU-only VLM test (#50913) by @ydshieh
* [vLLM CI] Fix the FireRedASR2 and MTP test failures (missing dependency, GPU-only test) (#50912) by @ydshieh
* Fix Reformer LM head bias not applied since the weight-loading refactor (#50811) by @ydshieh
* Fix error message and remove duplicate code in convert_slow_tokenizer.py (#50077) by @samyuktahegde
* Fix first-subword label assignment in LayoutXLM, LayoutLMv2, and MarkupLM tokenizers (#50455) by @14H034160212
* Skip added-token trie scan when no token can match (#50781) by @TheNetherWatcher
* [CI report] Upload the vLLM / SGLang CI reports to the Hub and post a summary to Slack (#50896) by @ydshieh
* Use lifespan instead of on_event in pipeline web server guide (#50858) by @phatstraws
* [CI] docs-check fixes (#50279) by @stevhliu
* Expose literal tester overrides and merged small-config defaults (#50462) by @tarekziade
* [SGLang CI] Add failure report job (shared with vLLM CI) (#50882) by @ydshieh
* [`Apertus 1.5`] Guard behind slow for gated repo (#50884) by @vasqu
* avoid running this wf from fork (#50694) by @tarekziade
* bench test reproducibility (#50504) by @tarekziade
* Fix timestamps (#50503) by @tarekziade
* [SGLang CI] Test against the latest published SGLang CPU release (#50878) by @ydshieh
* Keep AFMoE expert biases in FP32 on BF16 load (#50687) by @annekethvij
* Fix seeded collator generator selection (#50861) by @danarkhipov
* Remove no_grad decorator on all _init_weights (#50831) by @Cyrilvallez
* Remove no_grad decorator on RoPE forward (#50828) by @Cyrilvallez
* Update expected logits slice for `Qwen2MoeIntegrationTest::test_model_a2_7b_logits` on A10G (#50845) by @ydshieh
* Check for an empty batch in convert_to_tensors without flattening it (#49942) by @jayzuccarelli
* [serge] Fix 2 integration tests for model `qwen2_moe` failing with `other` (other (2)) (#49480) by @sergereview[bot]
* [serge] Fix 1 integration test for model `flint` failing with `other`, raising `RuntimeError` (other (1)) (#50283) by @sergereview[bot]
* [serge] Fix 5 integration tests for model `qwen3_vl_moe` failing with `other`, raising `RuntimeError` (other (5)) (#50145) by @sergereview[bot]
* Fixing training CI again  (#50747) by @SunMarc
* Fix Mistral Large 4 LeRoPE training gradients (#50727) by @taking-lying-flat
* Keep MiMo-V2-Flash's router in float32 in bfloat16 models (#50722) by @francesco-bertolotti
* Fix NanoChat inheriting an incompatible rotary kernel (#50823) by @taking-lying-flat
* Fix `CwmIntegrationTest` GPU OOM on multi-GPU runners (cap per-GPU `max_memory` at 70%) (#50824) by @ydshieh
* Mark `OmDetTurboModelTest::test_batching_equivalence` as flaky (`topk` query selection) (#50815) by @ydshieh
* [docs] Fix imports that fail on main in four English docs (#50817) by @burrows99
* Fix duplicate JetMoE router logits in auxiliary loss (#50658) by @taking-lying-flat
* docs: updates to security policy in SECURITY.md (#50711) by @Michellehbn
* [serge] Fix 2 integration tests for model `utils` failing with `output_mismatch` (list output differs (2)) (#49407) by @sergereview[bot]
* Fix OOM in Mamba2IntegrationTest by using MemoryCleanupMixin (#50808) by @ydshieh
* [docs] Fix the any-to-any guide example using the removed infer_device (#50792) by @burrows99
* Scale the padding-free position_ids test tolerance to the logits (#50697) by @EvanZhuang
* [docs] Fix PairClassificationPipeline example using the removed self.framework (#50789) by @burrows99
* [serge] Fix 2 integration tests for model `hrm_text` failing with `output_mismatch` (tensor values differ (2)) (#50006) by @sergereview[bot]
* [serge] Fix 6 integration tests for model `bloom` failing with `output_mismatch` (list output differs (4), other (2)) (#50469) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `ministral` failing with `output_mismatch` (tensor values differ (2)) (#50146) by @sergereview[bot]
* [serge] Fix 1 integration test for model `deepseek_vl_hybrid` failing with `output_mismatch` (list output differs (1)) (#49581) by @sergereview[bot]
* [serge] Fix 2 integration tests for model `ovis2` failing with `output_mismatch` (list output differs (2)) (#50233) by @sergereview[bot]
* [docs] Replace examples using pipeline tasks removed in v5 (#50625) by @rickygrosvenor-pramanick
* [CI] Fix external links (#50685) by @stevhliu
* Update A10 expected outputs of FA2 integration tests (#50738) by @ydshieh
* Revert mark linguistic generated (#50735) by @vasqu
* Update dev version (#50725) by @vasqu

**Full Changelog**: [`v5.23.0...v5.24.0`](https://github.com/huggingface/transformers/compare/v5.23.0...v5.24.0)

## 笔记


