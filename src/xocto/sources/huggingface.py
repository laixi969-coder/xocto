"""Hugging Face Hub：从公开 Spaces 和模型仓库发现早期 AI 应用与基础项目。"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from ..models import RawItem, now_iso
from .base import Http, HttpError, parse_iso, register, to_iso

API = "https://huggingface.co/api"
DEFAULT_LOOKBACK_HOURS = 72
# 新建仓库速度很快，前 100 条经常全是尚无互动的试验项目；Hub 支持单次
# 返回更多结果，因此默认多取一页后再由本地质量阈值裁剪。
DEFAULT_LIMIT = 1000


@register("huggingface")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    """只收近期创建且已有最低社区信号的公开仓库，避免把 Hub 当垃圾场。"""
    lookback = float(cfg.get("lookback_hours") or DEFAULT_LOOKBACK_HOURS)
    limit = max(1, min(int(cfg.get("limit") or DEFAULT_LIMIT), 1000))
    since = datetime.now(timezone.utc) - timedelta(hours=lookback)
    collected = now_iso()
    items: list[RawItem] = []

    spaces = cfg.get("spaces") or {}
    if spaces.get("enabled", True):
        try:
            rows = http.get_json(
                f"{API}/spaces",
                params={"sort": "createdAt", "direction": "-1", "limit": limit, "full": "true"},
            )
        except HttpError as exc:
            print(f"    ! Spaces 拉取失败：{exc}")
            rows = []
        min_likes = int(spaces.get("min_likes") or 0)
        selected = _recent(rows, since, min_likes, "likes")
        print(f"    [spaces] {len(selected)}/{len(rows) if isinstance(rows, list) else 0} 条")
        items.extend(_parse_space(row, collected) for row in selected)

    models = cfg.get("models") or {}
    if models.get("enabled", True):
        try:
            rows = http.get_json(
                f"{API}/models",
                params={"sort": "createdAt", "direction": "-1", "limit": limit, "full": "true"},
            )
        except HttpError as exc:
            print(f"    ! Models 拉取失败：{exc}")
            rows = []
        min_likes = int(models.get("min_likes") or 0)
        min_downloads = int(models.get("min_downloads") or 0)
        selected = [
            row for row in _recent(rows, since, min_likes, "likes")
            if int(row.get("downloads") or 0) >= min_downloads
        ]
        print(f"    [models] {len(selected)}/{len(rows) if isinstance(rows, list) else 0} 条")
        items.extend(_parse_model(row, collected) for row in selected)

    return items


def _recent(rows: object, since: datetime, minimum: int, metric: str) -> list[dict]:
    if not isinstance(rows, list):
        return []
    selected: list[dict] = []
    for row in rows:
        if not isinstance(row, dict) or row.get("private"):
            continue
        created = parse_iso(str(row.get("createdAt") or ""))
        if created is None or created < since or int(row.get(metric) or 0) < minimum:
            continue
        selected.append(row)
    return selected


def _parse_space(row: dict, collected: str) -> RawItem:
    space_id = str(row.get("id") or "").strip()
    card = row.get("cardData") or {}
    title = str(card.get("title") or space_id.rsplit("/", 1)[-1]).strip()
    created = parse_iso(str(row.get("createdAt") or ""))
    return RawItem(
        source="huggingface",
        external_id=f"space:{space_id}",
        title=title,
        url=f"https://huggingface.co/spaces/{space_id}",
        summary=str(card.get("short_description") or "").strip(),
        published_at=to_iso(created) if created else "",
        collected_at=collected,
        metrics={"likes": int(row.get("likes") or 0)},
        extra={
            "kind": "product",
            "builder": str(row.get("author") or space_id.split("/", 1)[0]),
            "hub_type": "space",
            "tags": row.get("tags") or [],
            "sdk": str(row.get("sdk") or card.get("sdk") or ""),
        },
        payload=row,
    )


def _parse_model(row: dict, collected: str) -> RawItem:
    model_id = str(row.get("id") or row.get("modelId") or "").strip()
    created = parse_iso(str(row.get("createdAt") or ""))
    return RawItem(
        source="huggingface",
        external_id=f"model:{model_id}",
        title=model_id.rsplit("/", 1)[-1],
        url=f"https://huggingface.co/{model_id}",
        # 新模型常还没有 model card；保留 tags 作为最小可读上下文，让编辑模型
        # 能区分语言模型、视觉模型和纯权重镜像，而不是只能猜仓库名。
        summary=_model_summary(row),
        published_at=to_iso(created) if created else "",
        collected_at=collected,
        metrics={"likes": int(row.get("likes") or 0), "downloads": int(row.get("downloads") or 0)},
        extra={
            "kind": "product",
            "builder": str(row.get("author") or model_id.split("/", 1)[0]),
            "hub_type": "model",
            "tags": row.get("tags") or [],
            "gated": bool(row.get("gated")),
        },
        payload=row,
    )


def _model_summary(row: dict) -> str:
    description = str((row.get("cardData") or {}).get("description") or "").strip()
    if description:
        return description
    tags = [str(tag).strip() for tag in (row.get("tags") or []) if str(tag).strip()]
    return "Open model tags: " + ", ".join(tags[:8]) if tags else ""
