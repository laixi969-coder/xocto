"""ModelScope 开源项目发现。

ModelScope 是中文生态的重要开源发布面。它与 GitHub/Hugging Face 并列，
用于发现模型、工具和工作流项目的早期采用信号；并不把单个基础模型直接
包装成应用机会，后续仍由编辑规则与 `/req` 判断其是否值得公开收录。
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from ..models import RawItem, now_iso
from .base import Http, parse_iso, register, to_iso

API = "https://modelscope.cn/openapi/v1/models"


@register("modelscope")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    lookback = float(cfg.get("lookback_hours") or 96)
    min_likes = int(cfg.get("min_likes") or 3)
    min_downloads = int(cfg.get("min_downloads") or 25)
    limit = min(max(int(cfg.get("limit") or 100), 1), 200)
    since = datetime.now(timezone.utc) - timedelta(hours=lookback)
    payload = http.get_json(API, params={"PageNumber": 1, "PageSize": limit})
    models = ((payload.get("data") or {}).get("models") or []) if isinstance(payload, dict) else []
    collected = now_iso()
    rows: list[RawItem] = []
    for model in models:
        if not isinstance(model, dict):
            continue
        model_id = str(model.get("id") or "").strip()
        created = parse_iso(str(model.get("created_at") or ""))
        likes = int(model.get("likes") or 0)
        downloads = int(model.get("downloads") or 0)
        if not model_id or created is None or created < since:
            continue
        if likes < min_likes or downloads < min_downloads:
            continue
        name = str(model.get("display_name") or model_id).strip()
        rows.append(RawItem(
            source="modelscope",
            external_id=model_id,
            title=name,
            url=f"https://modelscope.cn/models/{model_id}",
            summary=str(model.get("description") or "").strip(),
            published_at=to_iso(created),
            collected_at=collected,
            metrics={"likes": likes, "downloads": downloads},
            extra={
                "kind": "product",
                "ecosystem": "zh",
                "market": "CN",
                "open_source": True,
                "project_kind": "open_source",
            },
            payload=model,
        ))
    print(f"    [ModelScope] {len(rows)}/{len(models)} 条")
    return rows
