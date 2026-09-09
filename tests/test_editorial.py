import unittest

from xocto.editorial import has_context_copy
from xocto.brief import BriefError, _updates
from test_brief import product


class ContextCopyTests(unittest.TestCase):
    def test_rejects_placeholder_even_when_prefixed_with_company_name(self):
        self.assertFalse(has_context_copy("Uber：该 AI 产品提供了新的能力，但现有公开材料尚不足以确认其具体工作流价值。"))
        self.assertFalse(has_context_copy("这是一条关于 Broadcom 的新闻报道，标题暗示其分析师共识面临挑战，但内容未提供具体细节。"))
        self.assertTrue(has_context_copy("平台将推理价格下调 30%，使用该接口的应用成本随之下降。"))

    def test_model_output_cannot_publish_placeholder_market_context(self):
        with self.assertRaises(BriefError):
            _updates({"products": [{
                "slug": "example", "decision": "market_context",
                "summary_zh": "公开材料尚不足以确认具体工作流价值。",
                "summary_en": "A concrete change with an effect on costs.",
            }]}, [product()])
