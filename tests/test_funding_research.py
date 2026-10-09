from datetime import date
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from xocto.funding import FundingRound,read_analysis,save_rounds
from xocto.funding_research import RESEARCH_VERSION, product_evidence,read_state,research,research_due
from xocto.brief import run_funding,BriefError
from xocto.store import Store
from test_funding import items,row

BODY='A product for property managers. Connect customer records, schedule a tour, follow up with residents and deliver a completed service ticket. Pricing and reliability are measured for each property. '

class FundingResearchTests(unittest.TestCase):
    def record(self): return FundingRound.from_payload(items(row())[0].payload)
    def test_follows_product_pricing_and_case_links_only_on_the_owned_site(self):
        class Http:
            def __init__(self): self.calls=[]
            def get_text(self,url):
                self.calls.append(url)
                if url=='https://example.org':return BODY+'<a href="/product">Product</a><a href="/pricing">Pricing</a><a href="/customers/case">Customer story</a><a href="https://other.example/pricing">Prices</a>'
                return BODY
        http=Http();result=research(self.record(),http)
        self.assertEqual({e['role'] for e in product_evidence(result)}, {'overview','product','pricing','customer_case'})
        self.assertNotIn('https://other.example/pricing',http.calls)
    def test_failed_retrieval_is_persisted_and_retried_after_one_day(self):
        class Http:
            broken=True
            calls=0
            def get_text(self,url):
                self.calls+=1
                if self.broken: raise OSError('Temporary network failure')
                return BODY
        with tempfile.TemporaryDirectory() as directory:
            store=Store(Path(directory));http=Http();record=self.record()
            self.assertFalse(product_evidence(research(record,http,store=store,day=date(2026,10,8))))
            self.assertEqual(read_state(store,record)['status'],'blocked')
            http.broken=False
            research(record,http,store=store,day=date(2026,10,8));self.assertEqual(http.calls,1)
            self.assertTrue(product_evidence(research(record,http,store=store,day=date(2026,10,9))))
            self.assertEqual(http.calls,2)
    def test_unchanged_funding_still_refreshes_product_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            store=Store(Path(directory));record=self.record()
            analysis={'fingerprint':record.fingerprint,'research_version':RESEARCH_VERSION,'checked_on':'2026-09-20'}
            self.assertTrue(research_due(store,record,analysis,date(2026,10,8)))
            analysis['checked_on']='2026-10-07'
            self.assertFalse(research_due(store,record,analysis,date(2026,10,8)))
    def test_no_product_evidence_cannot_be_saved_as_completed_analysis(self):
        with tempfile.TemporaryDirectory() as directory:
            store=Store(Path(directory));save_rounds(store,items(row()))
            with patch('xocto.collect.load_config',return_value={}),patch('xocto.brief._read_config',return_value='rules'),patch('xocto.funding_research.research',return_value=[{'kind':'funding','text':'A large round.'}]),patch('xocto.brief._request') as request:
                with self.assertRaises(BriefError):run_funding(store,day=date(2026,10,8))
                request.assert_not_called()
                self.assertEqual(read_analysis(store,self.record()),{})

    def test_third_party_profiles_are_never_official_product_evidence(self):
        from dataclasses import replace
        from xocto.funding import company_url
        for url in ('https://funding.tech.eu/companies/123','https://www.producthunt.com/products/app','https://www.crunchbase.com/organization/app','https://pitchbook.com/profiles/company/app','https://www.theverge.com/ai/story'):
            self.assertEqual(company_url(url),'')
        http=unittest.mock.Mock()
        self.assertFalse(product_evidence(research(replace(self.record(),website='https://funding.tech.eu/companies/123'),http)))
        http.get_text.assert_not_called()

if __name__=='__main__':unittest.main()
