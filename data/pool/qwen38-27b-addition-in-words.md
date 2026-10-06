---
slug: qwen38-27b-addition-in-words
name: Qwen3.8 27B
builder: ''
category: ''
summary_zh: 2026 年 10 月，一项在本地硬件（DGX Spark）上对 Qwen3.8-27B-Q4_K_M.gguf 进行的受控实验显示：关闭推理时，模型在“用文字返回大数相加结果”任务上的表现随数字增大而下降；开启推理后，169
  次一次性尝试中答对 167 次。该结果说明本地部署的中等规模模型在开启推理后可以完成此前需要更大模型或外部计算器的多位数运算，对本地推理的可用性与成本判断有参考意义；但这是单次实验、样本有限，不能据此推断整个行业已经转向。
inspiration: ''
summary_en: In October 2026, a controlled experiment on local hardware (a DGX Spark) with Qwen3.8-27B-Q4_K_M.gguf
  showed that with reasoning disabled the model's ability to return the sum of large numbers in words
  degraded as the numbers grew, while with reasoning enabled it answered 167 of 169 one-shot attempts
  correctly. The result suggests locally deployed mid-sized models can handle multi-digit arithmetic that
  previously required larger models or an external calculator, which is relevant to assessments of local
  inference usability and cost; however, this is a single experiment with limited samples and does not
  support concluding that the whole industry has shifted.
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
url: https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words/
canonical_url: https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words
summary: "Research:   Qwen3.8 27B addition in words  \n         Colin Frasier  posted on Bluesky  about\
  \ an experiment he ran over two years ago using GPT-4o to see how well it could \"compute the sum but\
  \ return the answer in words\" across increasingly large numbers. Here's the chart he shared of those\
  \ results: \n   \n I'm confident GPT-4o didn't cheat and use a calculator, especially since it got so\
  \ many of the calculations wrong, but I was inspired to run the experiment again on local hardware (a\
  \ DGX Spark) to explore the effect in a fully controlled environment. \n I pasted his image into a Codex\
  \ Remote session (GPT-6 Astra) and had it run the same experiment using  Qwen3.8-27B-Q4_K_M.gguf . Here's\
  \ the result for a run of 30 attempts per combination with reasoning disabled: \n   \n Then I ran it\
  \ again with reasoning enabled. This took a  lot longer  per pair, so instead of running 30 samples\
  \ per square I ran just one - which results in a much less visually appealing heatmap since each square\
  \ is either 100% or 0%: \n   \n It got the right answer in 167 out of 169 attempts, and since these\
  \ were one-shot I'm confident a second run would produce different results here. \n Here's a  version\
  \ of the report  that includes the reasoning traces from some of those larger calculations, which include\
  \ text like this: \n  Wait, let me redo this more carefully.\n\n4,299,366,105,622\n6,088,794,067,970\n\
  \nLet me align them:\n4 2 9 9 3 6 6 1 0 5 6 2 2\n6 0 8 8 7 9 4 0 6 7 9 7 0\n\nAdding from right to left:\n\
  Position 1 (units): 2 + 0 = 2\nPosition 2 (tens): 2 + 7 = 9\nPosition 3 (hundreds): 6 + 9 = 15, write\
  \ 5, carry 1\n  \n    \n    \n         Tags:  mathematics ,  ai ,  generative-ai ,  local-llms ,  llms\
  \ ,  qwen ,  llm-reasoning ,  dgx-spark"
first_seen: '2026-10-04T23:34:00Z'
last_seen: '2026-10-06T02:19:01Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words/
  seen_at: '2026-10-06T02:19:01Z'
  metrics: {}
  kind: news
---

# Qwen3.8 27B

Research:   Qwen3.8 27B addition in words  
         Colin Frasier  posted on Bluesky  about an experiment he ran over two years ago using GPT-4o to see how well it could "compute the sum but return the answer in words" across increasingly large numbers. Here's the chart he shared of those results: 
   
 I'm confident GPT-4o didn't cheat and use a calculator, especially since it got so many of the calculations wrong, but I was inspired to run the experiment again on local hardware (a DGX Spark) to explore the effect in a fully controlled environment. 
 I pasted his image into a Codex Remote session (GPT-6 Astra) and had it run the same experiment using  Qwen3.8-27B-Q4_K_M.gguf . Here's the result for a run of 30 attempts per combination with reasoning disabled: 
   
 Then I ran it again with reasoning enabled. This took a  lot longer  per pair, so instead of running 30 samples per square I ran just one - which results in a much less visually appealing heatmap since each square is either 100% or 0%: 
   
 It got the right answer in 167 out of 169 attempts, and since these were one-shot I'm confident a second run would produce different results here. 
 Here's a  version of the report  that includes the reasoning traces from some of those larger calculations, which include text like this: 
  Wait, let me redo this more carefully.

4,299,366,105,622
6,088,794,067,970

Let me align them:
4 2 9 9 3 6 6 1 0 5 6 2 2
6 0 8 8 7 9 4 0 6 7 9 7 0

Adding from right to left:
Position 1 (units): 2 + 0 = 2
Position 2 (tens): 2 + 7 = 9
Position 3 (hundreds): 6 + 9 = 15, write 5, carry 1
  
    
    
         Tags:  mathematics ,  ai ,  generative-ai ,  local-llms ,  llms ,  qwen ,  llm-reasoning ,  dgx-spark

## 笔记


