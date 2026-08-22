"""GitHub 新仓库里涨星快的项目。

开源项目常常比闭源产品早半年暴露出一个方向能不能成 —— 一个开发者工具
在 GitHub 上爆了，通常意味着半年后会有一批公司围着它做商业化。

走 GitHub Search API。每日 Actions 用内置的短期 token，避免更宽的关键词、专题、
发布方和 Release 巡检互相挤掉；本地无 token 时仍可匿名运行。
"""

from __future__ import annotations

import os
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone

from ..models import RawItem, now_iso
from .base import Http, HttpError, register, to_iso, parse_iso

API = "https://api.github.com/search/repositories"
ORGS_API = "https://api.github.com/orgs"
REPOS_API = "https://api.github.com/repos"
PER_PAGE = 30
MAX_PER_PAGE = 100
DEFAULT_WITHIN_DAYS = 21
DEFAULT_MIN_STARS = 40
DEFAULT_RELEASE_LOOKBACK_HOURS = 72


def _api_headers() -> dict[str, str]:
    """GitHub Actions 有短期 token 时用它，扩大检索面但不要求本地配置密钥。

    匿名 Search API 的限额很低；一旦关键词、专题和发布方共同跑起来，后面的
    查询会被限流，所谓“扩大来源”反而只剩前几条查询。Actions 内置的 token
    只在运行期存在，绝不写入数据、日志或仓库；本地没设时照旧走匿名 API。
    """
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


@register("github")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    queries = cfg.get("queries") or []
    topics = cfg.get("topics") or []
    official_organizations = cfg.get("official_organizations") or []
    official_releases = cfg.get("official_releases") or []
    within_days = int(cfg.get("created_within_days") or DEFAULT_WITHIN_DAYS)
    min_stars = int(cfg.get("min_stars") or DEFAULT_MIN_STARS)
    since = (date.today() - timedelta(days=within_days)).isoformat()

    collected = now_iso()
    by_id: dict[str, RawItem] = {}
    headers = _api_headers()

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
                headers=headers,
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
                headers=headers,
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

    # 重点维护方的 Release 往往比新仓库更有用：它能捕捉模型、SDK、框架的
    # 重大能力变化，但只作为日报背景信号，不会伪装成一个新产品进入产品池。
    release_since = datetime.now(timezone.utc) - timedelta(
        hours=float(cfg.get("release_lookback_hours") or DEFAULT_RELEASE_LOOKBACK_HOURS)
    )
    for repository in official_releases:
        repository = str(repository).strip()
        if not repository or "/" not in repository:
            continue
        try:
            release = http.get_json(
                f"{REPOS_API}/{repository}/releases/latest",
                headers=headers,
            )
        except HttpError as exc:
            print(f"    ! 官方 Release「{repository}」失败：{exc}")
            continue
        item = _parse_release(release, repository, collected)
        published = parse_iso(item.published_at) if item else None
        if item is None or published is None or published < release_since:
            print(f"    [release:{repository}] 0 条")
            continue
        by_id[item.external_id] = item
        print(f"    [release:{repository}] 1 条")

    return list(by_id.values())


def _parse_release(release: object, repository: str, collected: str) -> RawItem | None:
    if not isinstance(release, dict):
        return None
    release_id = str(release.get("id") or release.get("tag_name") or "").strip()
    link = str(release.get("html_url") or "").strip()
    published = parse_iso(str(release.get("published_at") or release.get("created_at") or ""))
    if not release_id or not link or published is None:
        return None
    tag = str(release.get("tag_name") or "").strip()
    name = str(release.get("name") or tag or "Release").strip()
    reactions = release.get("reactions") or {}
    return RawItem(
        source="github",
        external_id=f"release:{repository}:{release_id}",
        title=f"{repository}: {name}",
        url=link,
        summary=str(release.get("body") or "").strip(),
        published_at=to_iso(published),
        collected_at=collected,
        metrics={"reactions": int(reactions.get("total_count") or 0)},
        extra={
            "kind": "news",
            "builder": repository.split("/", 1)[0],
            "official": True,
            "official_release": True,
            "repository": repository,
        },
        payload=release,
    )


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
