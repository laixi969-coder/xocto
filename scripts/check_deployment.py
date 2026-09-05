"""Verify both published editions match the generated artifacts after Vercel deploys."""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
from pathlib import Path
import time
from urllib.error import URLError
from urllib.request import Request, urlopen


def matches(base_url: str, site: Path, day: str) -> bool:
    # Compare the actual public pages, not just deployment status or a footer date.
    for path in ('index.html', 'en/index.html', f'r/{day}.html', f'en/r/{day}.html'):
        expected = (site / path).read_bytes()
        url = base_url.rstrip('/') + '/' + path
        try:
            with urlopen(Request(url, headers={'Cache-Control': 'no-cache'}), timeout=15) as response:
                actual = response.read()
        except (URLError, TimeoutError):
            return False
        if hashlib.sha256(actual).digest() != hashlib.sha256(expected).digest():
            return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', required=True, type=date.fromisoformat)
    parser.add_argument('--url', default='https://xocto.vercel.app')
    parser.add_argument('--site', type=Path, default=Path('site'))
    args = parser.parse_args()
    deadline = time.monotonic() + 300
    while True:
        if matches(args.url, args.site, args.date.isoformat()):
            print(f'已核验线上中英文首页与 {args.date} 日报，与本次构建一致。')
            return 0
        if time.monotonic() >= deadline:
            print('部署核验失败：线上页面在五分钟内未更新到本次构建。')
            return 1
        time.sleep(15)


if __name__ == '__main__':
    raise SystemExit(main())
