"""采集器集合。

导入即注册：加新源时在这里 import 一行，编排层不用改。
"""

from . import aicpb, github, hackernews, huggingface, ia40, modelscope, newssearch, officialfeeds, producthunt, v2ex  # noqa: F401  导入触发注册
from .base import Http, HttpError, get_fetcher, register, registered_names

__all__ = [
    "Http",
    "HttpError",
    "get_fetcher",
    "register",
    "registered_names",
]
