from dataclasses import replace
from types import SimpleNamespace
import unittest

from xocto.demand import demand_read
from xocto.models import Sighting
from test_req_review import product


class UsageReasonTests(unittest.TestCase):
    def test_traffic_never_fills_in_for_user_motivation(self):
        item = replace(product(), sightings=(Sighting('aicpb', 'https://example.com',
                       '2026-08-23T10:00:00Z', {'metric': 'visits', 'value': 5160000,
                       'raw_value': '516万', 'mom_percent': -12.37}),))
        for english in (False, True):
            with self.subTest(english=english):
                read = demand_read(item, None, (), english=english)
                self.assertTrue(read.usage_reason)
                for metric in ('516', '12.37', '环比', 'month-over-month'):
                    self.assertNotIn(metric, read.usage_reason)

    def test_existing_editorial_reason_is_preserved(self):
        review = SimpleNamespace(usage_reason='历史判断原文', usage_reason_en='Existing editorial reasoning.', gates=())
        self.assertEqual(demand_read(product(), review, ()).usage_reason, '历史判断原文')
        self.assertEqual(demand_read(product(), review, (), english=True).usage_reason, 'Existing editorial reasoning.')
