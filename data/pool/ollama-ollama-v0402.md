---
slug: ollama-ollama-v0402
name: Ollama
builder: ollama
category: ''
summary_zh: Ollama 是本地运行开源大模型的工具，开发者在自己机器上拉取并运行模型。本次 v0.40.2 把旧版本下载的模型在首次运行时后台升级为 llama.cpp 运行格式，并保留原文件作为回退备份，同时修复列表重复与上下文长度问题。
inspiration: ''
summary_en: Ollama is a tool for running open-source large models locally, letting developers pull and
  run models on their own machines. Release v0.40.2 upgrades models downloaded by earlier versions to
  the llama.cpp runner in the background on first run, keeps the original files as a rollback backup,
  and fixes duplicate listing and context-length issues.
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
url: https://github.com/ollama/ollama/releases/tag/v0.40.2
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.2
summary: "## Model upgrades\r\n\r\nModels downloaded with earlier versions of Ollama are upgraded in the\
  \ background the first time you run them, for better performance and compatibility when running on llama.cpp.\r\
  \n\r\nTo make downgrading safe, Ollama keeps the original copy as a backup, so upgraded models are temporarily\
  \ kept on disk. A future release will remove these backups automatically.\r\n\r\nTo remove backed up\
  \ models now (requires `jq`):\r\n\r\n```shell\r\ncurl -s localhost:11434/api/tags | jq -r '.models[].name'\
  \ | while read -r m; do\r\n  curl -s localhost:11434/api/show -d \"{\\\"model\\\":\\\"$m\\\"}\" | jq\
  \ -r \\\r\n    'select(any(.manifests[]?; .runner == \"llamacpp\")) | .manifests[] | select(.runner\
  \ == \"ggml\") | .digest'\r\ndone | sort -u | xargs -n1 ollama rm\r\n```\r\n\r\nThis only deletes the\
  \ backups. If you later downgrade to a version older than 0.40, you'll need to re-pull those models.\r\
  \n\r\n**Other changes**\r\n* `ollama list` no longer shows duplicate entries for upgraded models by\
  \ @dhiltgen in https://github.com/ollama/ollama/pull/18874\r\n* `ollama launch claude` uses the model's\
  \ full context length by @jberg5 in https://github.com/ollama/ollama/pull/18855\r\n* README: add oxi\
  \ to community integrations by @maziluiosif in https://github.com/ollama/ollama/pull/18739\r\n\r\n##\
  \ New Contributors\r\n* @maziluiosif made their first contribution in https://github.com/ollama/ollama/pull/18739\r\
  \n\r\n**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.1...v0.40.2-rc0"
first_seen: '2026-10-10T01:46:04Z'
last_seen: '2026-10-11T01:01:22Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.2
  seen_at: '2026-10-11T01:01:22Z'
  metrics:
    reactions: 28
  kind: news
---

# Ollama

## Model upgrades

Models downloaded with earlier versions of Ollama are upgraded in the background the first time you run them, for better performance and compatibility when running on llama.cpp.

To make downgrading safe, Ollama keeps the original copy as a backup, so upgraded models are temporarily kept on disk. A future release will remove these backups automatically.

To remove backed up models now (requires `jq`):

```shell
curl -s localhost:11434/api/tags | jq -r '.models[].name' | while read -r m; do
  curl -s localhost:11434/api/show -d "{\"model\":\"$m\"}" | jq -r \
    'select(any(.manifests[]?; .runner == "llamacpp")) | .manifests[] | select(.runner == "ggml") | .digest'
done | sort -u | xargs -n1 ollama rm
```

This only deletes the backups. If you later downgrade to a version older than 0.40, you'll need to re-pull those models.

**Other changes**
* `ollama list` no longer shows duplicate entries for upgraded models by @dhiltgen in https://github.com/ollama/ollama/pull/18874
* `ollama launch claude` uses the model's full context length by @jberg5 in https://github.com/ollama/ollama/pull/18855
* README: add oxi to community integrations by @maziluiosif in https://github.com/ollama/ollama/pull/18739

## New Contributors
* @maziluiosif made their first contribution in https://github.com/ollama/ollama/pull/18739

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.1...v0.40.2-rc0

## 笔记


