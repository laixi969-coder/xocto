"""Bounded, first-party product retrieval with explicit gaps and retry state."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, timedelta
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, urldefrag

import yaml

from .funding import FundingRound, safe_url, company_url
from .page_text import PageText
from .sources.base import Http
from .store import Store, _atomic_write
from .models import today

RESEARCH_VERSION = 2
ROLES = ('product', 'pricing', 'customer_case', 'documentation')
PATTERNS = {
    'product': r'product|platform|solution|feature|how.it.works|produkt|fonction|lösungen',
    'pricing': r'pricing|prices|tarif|preise|cennik|plans|piani|precios|priser|prijzen',
    'customer_case': r'case.stud|customer.stor|success.stor|customers|use.cases|our.work',
    'documentation': r'documentation|/docs|developers|technical|research',
}

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.rows=[]; self.href=''; self.label=[]
    def handle_starttag(self, tag, attrs):
        if tag == 'a': self.href=dict(attrs).get('href',''); self.label=[]
    def handle_data(self, data):
        if self.href: self.label.append(data)
    def handle_endtag(self, tag):
        if tag == 'a' and self.href:
            self.rows.append((self.href,' '.join(self.label))); self.href=''


def state_path(store: Store, record: FundingRound):
    return store.data_dir/'funding'/'research'/f'{record.company_id}.json'


def read_state(store: Store, record: FundingRound) -> dict:
    path=state_path(store,record)
    return json.loads(path.read_text()) if path.exists() else {}


def product_evidence(evidence: list[dict]) -> list[dict]:
    return [e for e in evidence if e.get('kind') == 'company_claim'
            and e.get('status','retrieved') == 'retrieved' and len(e.get('text','').strip()) >= 180]


def evidence_fingerprint(evidence: list[dict]) -> str:
    # Retrieval times and transient errors must not change a successful read.
    facts=[{k:e.get(k) for k in ('url','kind','role','text')} for e in evidence if e.get('status','retrieved')=='retrieved']
    return hashlib.sha256(json.dumps(facts,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def research_due(store: Store, record: FundingRound, analysis: dict, day: date) -> bool:
    state=read_state(store,record)
    if state.get('round_fingerprint') == record.fingerprint and state.get('last_attempt') == day.isoformat() and state.get('status')=='blocked':
        return False
    if not analysis or analysis.get('fingerprint')!=record.fingerprint or analysis.get('research_version',0)<RESEARCH_VERSION:
        return True
    if state.get('fingerprint') and analysis.get('research_fingerprint') != state['fingerprint']:
        return True
    checked=date.fromisoformat(analysis.get('checked_on') or '1970-01-01')
    interval=3 if state.get('gaps') else 14
    return (day-checked).days >= interval


def research(record: FundingRound, http: Http, *, store: Store | None = None,
             day: date | None = None, refresh: bool = False) -> list[dict]:
    day=day or today(); stamp=day.isoformat()
    overrides={}
    if store:
        config=store.config_dir/'funding-research.yaml'
        if config.exists(): overrides=(yaml.safe_load(config.read_text()) or {}).get('companies',{}).get(record.company_id,{})
        cached=read_state(store,record)
        interval=1 if cached.get('status')=='blocked' else 3 if cached.get('gaps') else 14
        if not refresh and cached.get('version')==RESEARCH_VERSION and cached.get('round_fingerprint')==record.fingerprint and cached.get('last_attempt') and (day-date.fromisoformat(cached['last_attempt'])).days < interval:
            return cached['evidence']
    website=company_url(overrides.get('website') or record.website)
    base_host=(urlsplit(website).hostname or '').removeprefix('www.')
    allowed={base_host,*overrides.get('owned_hosts',[])}-{''}
    def owned(url):
        host=(urlsplit(url).hostname or '').removeprefix('www.')
        return bool(host and any(host==root or host.endswith('.'+root) for root in allowed))
    evidence=[{'url':record.url,'kind':'funding','role':'funding','status':'retrieved','text':record.payload.get('source_quote') or record.description,'checked_on':stamp}]
    queue=[(website,'overview')] if website else []
    queue += [(safe_url(p['url']),p['role']) for p in overrides.get('pages',[]) if safe_url(p.get('url','')) and owned(p['url'])]
    attempted=set(); counts={role:0 for role in ROLES}; max_pages=int(overrides.get('max_pages',7))
    while queue and len(attempted)<max_pages:
        url,role=queue.pop(0); url=urldefrag(url)[0]
        if not url or url in attempted or not owned(url) or re.search(r'\.(?:pdf|zip|png|jpg|svg|mp4)(?:\?|$)',url,re.I): continue
        if role in counts and counts[role] >= (2 if role in {'product','customer_case'} else 1):continue
        attempted.add(url)
        if role in counts: counts[role]+=1
        entry={'url':url,'kind':'company_claim','role':role,'checked_on':stamp}
        try:
            html=http.get_text(url); page=PageText();page.feed(html);text=' '.join(page.parts)[:12000]
            if len(text)<180 or re.search(r'domain (?:is )?for sale|buy this domain|this website is for sale|verify you are human|checking your browser',text,re.I):
                raise ValueError('Page has no usable product text or is a parked/challenge page')
            entry.update(status='retrieved',text=text)
            links=Links();links.feed(html)
            for category in ROLES:
                candidates=[]
                for href,label in links.rows:
                    target=safe_url(urljoin(url,href))
                    # Long feature teasers can mention pricing or customers;
                    # they are not a pricing page or an actual case study.
                    signal=(label if len(label.strip())<100 else '')+' '+urlsplit(target).path
                    if category=='pricing' and not re.search(r'(?:^|[ /_-])(?:pricing|prices?|tarifs?|preise|cennik|plans|piani|precios|priser|prijzen)(?:$|[ /?#_-])',signal,re.I):
                        continue
                    if target and owned(target) and target not in attempted and re.search(PATTERNS[category],signal,re.I):
                        candidates.append((target,category))
                queue.extend(candidates[:2])
        except Exception as exc:
            entry.update(kind='retrieval_gap',status='unavailable',text='',error=f'{type(exc).__name__}: {str(exc)[:200]}')
        evidence.append(entry)
    retrieved=product_evidence(evidence)
    covered={e.get('role') for e in retrieved}
    gaps=[role for role in ROLES if role not in covered]
    if not website:gaps.insert(0,'official_website')
    state={'version':RESEARCH_VERSION,'company_id':record.company_id,'round_fingerprint':record.fingerprint,
           'last_attempt':stamp,'status':'ready' if retrieved else 'blocked','gaps':gaps,
           'evidence':evidence,'fingerprint':evidence_fingerprint(evidence)}
    if store: _atomic_write(state_path(store,record),json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    return evidence
