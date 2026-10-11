---
slug: ollama-ollama-v0402
name: Ollama
builder: ollama
category: ''
summary_zh: 这是本地模型运行工具 Ollama 的一次版本更新，不是新的独立产品：它把用户此前下载的模型在首次运行时自动迁移到 llama.cpp 运行时，并保留原副本以便回退。对本地部署 AI
  的团队而言，升级不再需要手动重新拉取模型，但迁移期间会额外占用磁盘空间。
inspiration: ''
summary_en: 'This is a version update to the local model runner Ollama, not a new standalone product:
  models downloaded by earlier versions are migrated automatically to the llama.cpp runner on first run,
  with the original copy kept for rollback. For teams running AI locally, upgrades no longer require manually
  re-pulling models, though the migration temporarily uses extra disk space.'
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
status: market_context
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


