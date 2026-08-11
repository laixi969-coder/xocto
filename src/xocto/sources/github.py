"""GitHub 新仓库里涨星快的项目。

开源项目常常比闭源产品早半年暴露出一个方向能不能成 —— 一个开发者工具
在 GitHub 上爆了，通常意味着半年后会有一批公司围着它做商业化。

走公共 Search API。匿名限流是每分钟 10 次，我们一天跑几次，够用。
如果哪天要提额度再加 token（那时才需要密钥）。
"""

from __future__ import annotations

from datetime import date, timedelta

from ..models import RawItem, now_iso
from .base import Http, HttpError, register, to_iso, parse_iso

API = "https://api.github.com/search/repositories"
PER_PAGE = 30
DEFAULT_WITHIN_DAYS = 21
DEFAULT_MIN_STARS = 40


@register("github")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    queries = cfg.get("queries") or []
    if not queries:
        print("    （没配 queries，跳过）")
        return []

    within_days = int(cfg.get("created_within_days") or DEFAULT_WITHIN_DAYS)
    min_stars = int(cfg.get("min_stars") or DEFAULT_MIN_STARS)
    since = (date.today() - timedelta(days=within_days)).isoformat()

    collected = now_iso()
    by_id: dict[str, RawItem] = {}

    for query in queries:
        q = f"{query} created:>{since} stars:>={min_stars}"
        try:
            payload = http.get_json(
                API,
                params={"q": q, "sort": "stars", "order": "desc", "per_page": PER_PAGE},
                headers={"Accept": "application/vnd.github+json"},
            )
        except HttpError as exc:
            # 匿名调用很容易撞限流，单个 query 失败不该拖垮整个源
            print(f"    ! 查询「{query}」失败：{exc}")
            continue

        repos = payload.get("items") or []
        print(f"    [{query}] {len(repos)} 条")

        for repo in repos:
            item = _parse_repo(repo, collected)
            if item is not None and item.external_id not in by_id:
                by_id[item.external_id] = item

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
