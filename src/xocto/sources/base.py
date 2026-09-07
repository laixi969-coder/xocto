"""采集器公共设施：HTTP 客户端与注册表。

每个采集器是一个函数：fetch(cfg, http) -> list[RawItem]
抛异常是允许的 —— 编排层会捕获、记录、继续跑其他源。
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable

import httpx

from ..models import ISO_FMT, RawItem

# 采集器函数签名
Fetcher = Callable[[dict, "Http"], list[RawItem]]

_REGISTRY: dict[str, Fetcher] = {}


def register(name: str) -> Callable[[Fetcher], Fetcher]:
    """把采集器注册进表。用装饰器，加新源不用改编排代码。"""

    def deco(fn: Fetcher) -> Fetcher:
        _REGISTRY[name] = fn
        return fn

    return deco


def get_fetcher(name: str) -> Fetcher | None:
    return _REGISTRY.get(name)


def registered_names() -> tuple[str, ...]:
    return tuple(sorted(_REGISTRY))


class HttpError(RuntimeError):
    """HTTP 层的失败。带上足够定位问题的信息。"""


@dataclass(frozen=True)
class Http:
    """薄封装的 HTTP 客户端。

    只对 5xx、429 和网络错误重试；4xx 直接失败 —— 那是我们请求写错了，
    重试没有意义，应该尽早暴露。
    """

    timeout: float = 25.0
    # UA 里带上项目地址：源站运维要是觉得我们抓得不对，
    # 有个地方能找到人，而不是直接把 UA 拉黑。
    user_agent: str = "x-octo/0.1 (+https://github.com/laixi969-coder/xocto)"
    retries: int = 2
    backoff: float = 2.0

    def get_text(self, url: str, *, params: dict | None = None, headers: dict | None = None) -> str:
        return self._request(url, params=params, headers=headers).text

    def get_bytes(self, url: str, *, params: dict | None = None, headers: dict | None = None) -> bytes:
        """二进制响应。gzip 压缩的 sitemap 之类必须拿原始字节，text 解码会把压缩包变成乱码。"""
        return self._request(url, params=params, headers=headers).content

    def get_json(self, url: str, *, params: dict | None = None, headers: dict | None = None) -> Any:
        resp = self._request(url, params=params, headers=headers)
        try:
            return resp.json()
        except ValueError as exc:
            raise HttpError(f"{url} 返回的不是合法 JSON: {exc}") from exc

    def _request(self, url: str, *, params: dict | None, headers: dict | None) -> httpx.Response:
        merged = {"User-Agent": self.user_agent, **(headers or {})}
        last_error: Exception | None = None

        for attempt in range(self.retries + 1):
            resp: httpx.Response | None = None
            try:
                resp = httpx.get(
                    url,
                    params=params,
                    headers=merged,
                    timeout=self.timeout,
                    follow_redirects=True,
                )
            except httpx.HTTPError as exc:
                last_error = exc
            else:
                if resp.status_code < 400:
                    return resp
                if resp.status_code < 500 and resp.status_code != 429:
                    raise HttpError(f"{url} 返回 {resp.status_code}（请求有问题，不重试）")
                last_error = HttpError(f"{url} 返回 {resp.status_code}")

            if attempt < self.retries:
                time.sleep(self._wait(attempt, resp))

        raise HttpError(f"{url} 重试 {self.retries} 次仍失败: {last_error}")

    def _wait(self, attempt: int, resp: httpx.Response | None) -> float:
        """退避时长。

        对方回了 Retry-After 就听它的 —— 那是源站明确告诉我们该等多久，
        无视它继续按自己的节奏敲，是最容易被永久封的行为。
        没给就指数退避（2/4/8…），不是线性：源站正在过载时，
        线性退避的第二次重试往往还落在同一个故障窗口里。
        """
        if resp is not None and resp.status_code == 429:
            raw = resp.headers.get("Retry-After", "").strip()
            if raw.isdigit():
                return min(float(raw), 120.0)   # 封顶，别让单次采集挂死
        return self.backoff * (2**attempt)


def to_iso(dt: datetime) -> str:
    """任意 datetime 统一成 UTC 的 ISO8601 字符串。"""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime(ISO_FMT)


def parse_iso(value: str) -> datetime | None:
    """宽松解析 ISO8601。解析不了返回 None，不抛异常。

    各源格式不统一（带 Z、带 +08:00、带毫秒），统一在这里兜住。
    """
    if not value:
        return None
    text = value.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def hours_since(value: str) -> float | None:
    """距今多少小时。解析不了返回 None。"""
    dt = parse_iso(value)
    if dt is None:
        return None
    return (datetime.now(timezone.utc) - dt).total_seconds() / 3600
