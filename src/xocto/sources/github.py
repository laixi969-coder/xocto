"""GitHub 新仓库里涨星快的项目。

开源项目常常比闭源产品早半年暴露出一个方向能不能成 —— 一个开发者工具
在 GitHub 上爆了，通常意味着半年后会有一批公司围着它做商业化。

走公共 Search API。匿名限流是每分钟 10 次，我们一天跑几次，够用。
如果哪天要提额度再加 token（那时才需要密钥）。
"""

from __future__ import annotations

from dataclasses import replace
from datetime import date, timedelta

from ..models import RawItem, now_iso
from .base import Http, HttpError, register, to_iso, parse_iso

API = "https://api.github.com/search/repositories"
ORGS_API = "https://api.github.com/orgs"
PER_PAGE = 30
MAX_PER_PAGE = 100
DEFAULT_WITHIN_DAYS = 21
DEFAULT_MIN_STARS = 40


@register("github")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    queries = cfg.get("queries") or []
    topics = cfg.get("topics") or []
    official_organizations = cfg.get("official_organizations") or []
    within_days = int(cfg.get("created_within_days") or DEFAULT_WITHIN_DAYS)
    min_stars = int(cfg.get("min_stars") or DEFAULT_MIN_STARS)
    since = (date.today() - timedelta(days=within_days)).isoformat()

    collected = now_iso()
    by_id: dict[str, RawItem] = {}

    def add(repo: dict, path: str, *, priority_review: bool = False) -> None:
        item = _parse_repo(repo, collected)
        if item is None:
            return
        existing = by_id.get(item.external_id)
        if existing is None:
            item = replace(
                item,
                extra={
                    **item.extra,
                    "discovery_paths": [path],
                    "priority_review": priority_review,
                },
            )
            by_id[item.external_id] = item
            return
        paths = list(existing.extra.get("discovery_paths") or [])
        if path not in paths:
            paths.append(path)
        by_id[item.external_id] = replace(
            existing,
            extra={
                **existing.extra,
                "discovery_paths": paths,
                "priority_review": bool(existing.extra.get("priority_review")) or priority_review,
            },
        )

    def search(query: str, path: str, *, per_page: int = PER_PAGE, priority_review: bool = False) -> None:
        try:
            payload = http.get_json(
                API,
                params={"q": query, "sort": "stars", "order": "desc", "per_page": per_page},
                headers={"Accept": "application/vnd.github+json"},
            )
        except HttpError as exc:
            # 匿名调用很容易撞限流，单个查询失败不该拖垮其他发现通道。
            print(f"    ! 查询「{path}」失败：{exc}")
            return

        repos = payload.get("items") or []
        print(f"    [{path}] {len(repos)} 条")

        for repo in repos:
            add(repo, path, priority_review=priority_review)

    # 语义检索：发现正常的新 AI 应用。结果页有限，不能承担完整性职责。
    for query in queries:
        search(f"{query} created:>{since} stars:>={min_stars}", query)

    # 专题检索：项目名或介绍没有通用关键词时，GitHub topic 是稳定的补充索引。
    for topic in topics:
        search(
            f"topic:{topic} created:>{since} stars:>={min_stars}",
            f"topic:{topic}",
            priority_review=True,
        )

    # 全局突破项目：新建数日内已经爆发的仓库必须进入人工/模型复核，即使名称和
    # 简介完全没出现既有关键词。这是对搜索词与 30 条结果页的独立兜底。
    breakout = cfg.get("breakout") or {}
    if breakout.get("enabled"):
        breakout_days = int(breakout.get("within_days") or 3)
        breakout_stars = int(breakout.get("min_stars") or 5000)
        breakout_since = (date.today() - timedelta(days=breakout_days)).isoformat()
        search(
            f"created:>{breakout_since} stars:>={breakout_stars}",
            "breakout",
            per_page=MAX_PER_PAGE,
            priority_review=True,
        )

    # 官方组织新仓库：产品发布有时只写在组织名、README 或 topic 中，根本没有
    # “AI agent” 一类的通用词。组织列表按创建时间取，不依赖全文搜索。
    for organization in official_organizations:
        organization = str(organization).strip()
        if not organization:
            continue
        try:
            repos = http.get_json(
                f"{ORGS_API}/{organization}/repos",
                params={"type": "sources", "sort": "created", "direction": "desc", "per_page": MAX_PER_PAGE},
                headers={"Accept": "application/vnd.github+json"},
            )
        except HttpError as exc:
            print(f"    ! 官方组织「{organization}」失败：{exc}")
            continue
        if not isinstance(repos, list):
            print(f"    ! 官方组织「{organization}」返回格式不对")
            continue
        recent = [repo for repo in repos if (repo.get("created_at") or "")[:10] > since]
        print(f"    [official:{organization}] {len(recent)} 条")
        for repo in recent:
            add(repo, f"official:{organization}", priority_review=True)

    return list(by_id.values())


def _parse_repo(repo: dict, collected: str) -> RawItem | None:
    repo_id = str(repo.get("id") or "").strip()
    full_name = (repo.get("full_name") or "").strip()
    if not repo_id or not full_name:
        return None

    # 有官网就用官网，没有就用仓库地址
    homepage = (repo.get("homepage") or "").strip()
    repo_url = (repo.get("html_url") or "").strip()
    url = homepage if homepage.startswith("http") else repo_url
    if not url:
        return None

    published = parse_iso(repo.get("created_at") or "")

    return RawItem(
        source="github",
        external_id=repo_id,
        # 用仓库名而不是 full_name，owner 放到 extra 里
        title=(repo.get("name") or full_name).strip(),
        url=url,
        summary=(repo.get("description") or "").strip(),
        published_at=to_iso(published) if published else "",
        collected_at=collected,
        metrics={
            "stars": repo.get("stargazers_count") or 0,
            "forks": repo.get("forks_count") or 0,
            "open_issues": repo.get("open_issues_count") or 0,
        },
        extra={
            "builder": (repo.get("owner") or {}).get("login") or full_name.split("/")[0],
            "full_name": full_name,
            "repo_url": repo_url,
            "homepage": homepage,
            "language": repo.get("language") or "",
            "topics": repo.get("topics") or [],
            "pushed_at": repo.get("pushed_at") or "",
        },
        payload=repo,
    )
