---
slug: python-3150-candidate-2-is-here
name: Python
builder: ''
category: ''
summary_zh: 该 AI 产品提供了新的能力，但现有公开材料尚不足以确认其具体工作流价值。
inspiration: ''
summary_en: This AI offering introduces a new capability, but public evidence is not yet sufficient to
  confirm its workflow value.
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
url: https://simonwillison.net/2026/Sep/1/python-315-rc-2/
canonical_url: https://simonwillison.net/2026/Sep/1/python-315-rc-2
summary: "Python 3.15.0 candidate 2 is here!   \nHugo van Kemenade (release manager for Python 3.14 and\
  \ 3.15) announces the final release candidate for Python 3.15, scheduled for release in October: \n\
  \ \n Entering the release candidate phase, only reviewed code changes which are clear bug fixes are\
  \ allowed between this release candidate and the final release. [...] \n We  strongly encourage  maintainers\
  \ of third-party Python projects to prepare their projects for 3.15 during this phase, and publish Python\
  \ 3.15 wheels on PyPI to be ready for the final release of 3.15.0, and to help other projects do their\
  \ own testing. Any binary wheels built against Python 3.15.0 release candidates  will work  with future\
  \ versions of Python 3.15. \n \n Back in 2021 I  found a bug in Python 3.10  by running my test suites\
  \ against it... but I hadn't done this during the RC period, so that bug had already shipped! Since\
  \ then I've always paid much closer attention to these RCs. \n The new RC isn't available for GitHub\
  \ Actions just yet - keep an eye on  actions/python-versions  for that. For the moment though you can\
  \ add this to a testing matrix: \n   strategy :\n   matrix :\n     python-version :  [\"3.14\", \"3.15\"\
  ] \n\n steps :\n  -  uses :  actions/setup-python@v7 \n     with :\n       python-version :  ${{ matrix.python-version\
  \ }} \n       allow-prereleases :  true \n       check-latest :  true   \n\n The  allow-prereleases\
  \  and  check-latest  flags mean that today this will test against RC1, and when RC2 lands it will automatically\
  \ switch to that version (and then the stable version once that comes out.)\n\n       Via  @hugovk.dev\
  \   \n\n\n     Tags:  open-source ,  python ,  github-actions"
first_seen: '2026-09-01T14:59:18Z'
last_seen: '2026-09-02T00:14:54Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/1/python-315-rc-2/
  seen_at: '2026-09-02T00:14:54Z'
  metrics: {}
  kind: news
---

# Python

Python 3.15.0 candidate 2 is here!   
Hugo van Kemenade (release manager for Python 3.14 and 3.15) announces the final release candidate for Python 3.15, scheduled for release in October: 
 
 Entering the release candidate phase, only reviewed code changes which are clear bug fixes are allowed between this release candidate and the final release. [...] 
 We  strongly encourage  maintainers of third-party Python projects to prepare their projects for 3.15 during this phase, and publish Python 3.15 wheels on PyPI to be ready for the final release of 3.15.0, and to help other projects do their own testing. Any binary wheels built against Python 3.15.0 release candidates  will work  with future versions of Python 3.15. 
 
 Back in 2021 I  found a bug in Python 3.10  by running my test suites against it... but I hadn't done this during the RC period, so that bug had already shipped! Since then I've always paid much closer attention to these RCs. 
 The new RC isn't available for GitHub Actions just yet - keep an eye on  actions/python-versions  for that. For the moment though you can add this to a testing matrix: 
   strategy :
   matrix :
     python-version :  ["3.14", "3.15"] 

 steps :
  -  uses :  actions/setup-python@v7 
     with :
       python-version :  ${{ matrix.python-version }} 
       allow-prereleases :  true 
       check-latest :  true   

 The  allow-prereleases  and  check-latest  flags mean that today this will test against RC1, and when RC2 lands it will automatically switch to that version (and then the stable version once that comes out.)

       Via  @hugovk.dev   


     Tags:  open-source ,  python ,  github-actions

## 笔记


