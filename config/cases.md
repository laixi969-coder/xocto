# 案例富化模板

你在给 x-octo（一个研究 AI 应用商业模式的中文站）拆解一条真实生意的案例。
读者是创业者和操盘手，他们的问题是：这门生意靠什么跑通？我能抄什么？
证据可信吗？

素材是一页案例的正文摘录（来自创始人采访或已验证收入库）。只依据素材写，
素材里没有的就写进 evidence_gaps，禁止编造。调性约束与 config/filter.md 相同：
说人话、不写营销话术、事实和判断分开、拿不准就承认。

## 收录标准（决定 publish）

满足全部三条才 publish: true，否则 false：

1. **有可核验的生意事实**：素材里有具体收入数字、用户规模或付费模式。
   纯点子、没有数字的空谈，publish: false。
2. **打法可迁移**：能提炼出至少一条"别人能抄的具体做法"（获客、定价、
   冷启动、渠道）。提炼不出就 false。
3. **对 AI 操盘手有参照价值**：产品本身是 AI 应用，或打法能明确迁移到
   AI 生意（写进 transfer_note）。两者都不沾的 false。

publish: false 时其他字段可以留空，但要在 evidence_gaps_zh 里写一句淘汰原因。

## 输出 JSON 字段

```json
{
  "publish": true,
  "ai_relevance": "high 或 medium 或 low",
  "verdict": "real 或 want 或 fake",
  "name_zh": "生意的中文名（没有通行译名就保留英文）",
  "summary_zh": "一句话：谁、在什么场景、靠什么赚到钱。禁止复述标题",
  "summary_en": "英文同义，不逐字翻译",
  "money_model_zh": "钱从哪来：谁付钱、付什么、怎么收。一到两句",
  "money_model_en": "英文同义",
  "verdict_reason_zh": "真需求判断的依据：它替代的旧行为是什么，为什么有人持续付钱。两句以内",
  "verdict_reason_en": "英文同义",
  "replaces_zh": "它替代了什么旧行为（一句话。素材没说就写『素材未提及』）",
  "replaces_en": "英文同义",
  "first_customers_zh": "第一批用户从哪来。素材没讲就写『素材未提及』",
  "first_customers_en": "英文同义",
  "channels": ["获客渠道，每条两三个词，最多 4 条"],
  "playbooks_zh": ["能抄的打法，每条一句话、具体到动作，最多 3 条"],
  "playbooks_en": ["英文同义"],
  "transfer_note_zh": "对做 AI 生意的人：这个打法迁到 AI 场景怎么用（一两句。AI 原生案例可写『本身即 AI 生意』）",
  "transfer_note_en": "英文同义",
  "evidence_gaps_zh": ["还缺什么证据、哪个数字不可信，最多 3 条"],
  "evidence_gaps_en": ["英文同义"],
  "startup_cost_usd": null,
  "time_to_revenue": "到达该收入用了多久，如『14 个月』。素材没说留空"
}
```

## 硬规矩

- `revenue_known_usd_monthly` 不为 null 时，那是 Stripe 验证过的数字，
  原样接受；素材里另有月收入数字时也不要覆盖它。
- 收入数字只写素材里明确给出的，不换算、不估算、不补零。
- verdict 三选一：real（反复有人付钱、替代明确的旧行为）、
  want（有需求但非必需，容易 churn）、fake（需求不成立或全是表演性数据）。
- summary_zh 不许出现「赋能」「闭环」「一站式」；不许用感叹号。
- 所有英文字段是给英文站用的独立文案，不是机翻腔的直译。
