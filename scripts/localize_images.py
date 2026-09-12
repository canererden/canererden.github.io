#!/usr/bin/env python3
"""
Download remote images referenced from blog posts and rewrite the posts to point
at local copies under assets/img/blog/.

Why: 90+ images are currently hot-linked from miro.medium.com and i.imgur.com.
They bypass the site's own WebP pipeline and break the day those hosts change.

Usage (needs internet access):

    python3 scripts/localize_images.py            # download and rewrite
    python3 scripts/localize_images.py --dry-run  # just report what would happen

Requires: requests  (pip install requests)
"""

from __future__ import annotations

import argparse
import hashlib
import mimetypes
import os
import re
import sys
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("This script needs the 'requests' package: pip install requests")

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"
OUT_DIR = ROOT / "assets" / "img" / "blog"

# Hosts whose images we want to pull into the repository.
REMOTE_HOSTS = (
    "miro.medium.com",
    "cdn-images-1.medium.com",
    "i.imgur.com",
    "imgur.com",
)

# Markdown image syntax plus bare <img src="...">
MD_IMAGE = re.compile(r"!\[([^\]]*)\]\((https?://[^)\s]+?)(?:\s+\"[^\"]*\")?\)")
HTML_IMAGE = re.compile(r'<img([^>]*?)src="(https?://[^"]+)"')

EXT_BY_TYPE = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
}

USER_AGENT = "Mozilla/5.0 (compatible; canererden.com image localiser)"


def is_remote_target(url: str) -> bool:
    return any(host in url for host in REMOTE_HOSTS)


def local_name(url: str, content_type: str | None) -> str:
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    ext = os.path.splitext(url.split("?")[0])[1].lower()
    if ext not in EXT_BY_TYPE.values():
        ext = EXT_BY_TYPE.get((content_type or "").split(";")[0].strip(), "")
    if not ext:
        ext = mimetypes.guess_extension(content_type or "") or ".jpg"
    return f"{digest}{ext}"


def download(url: str, session: requests.Session) -> tuple[str, bytes] | None:
    try:
        resp = session.get(url, timeout=30, headers={"User-Agent": USER_AGENT})
        resp.raise_for_status()
    except Exception as exc:  # noqa: BLE001 - report and carry on
        print(f"    ! failed: {url}\n      {exc}")
        return None
    return resp.headers.get("Content-Type", ""), resp.content


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    cache: dict[str, str] = {}
    downloaded = failed = rewritten = 0

    for path in sorted(POSTS_DIR.glob("*.md")):
        text = original = path.read_text(encoding="utf-8")
        urls = {m.group(2) for m in MD_IMAGE.finditer(text) if is_remote_target(m.group(2))}
        urls |= {m.group(2) for m in HTML_IMAGE.finditer(text) if is_remote_target(m.group(2))}
        if not urls:
            continue

        print(f"{path.name}: {len(urls)} remote image(s)")
        for url in sorted(urls):
            if url in cache:
                local = cache[url]
            elif args.dry_run:
                print(f"    would download {url}")
                continue
            else:
                result = download(url, session)
                if result is None:
                    failed += 1
                    continue
                content_type, blob = result
                name = local_name(url, content_type)
                (OUT_DIR / name).write_bytes(blob)
                local = f"/assets/img/blog/{name}"
                cache[url] = local
                downloaded += 1
                print(f"    saved {name}  ({len(blob) // 1024} KB)")
            text = text.replace(url, local)

        if not args.dry_run and text != original:
            path.write_text(text, encoding="utf-8")
            rewritten += 1

    print(
        f"\nDone. downloaded={downloaded} failed={failed} posts_rewritten={rewritten}"
        f"\nImages are in {OUT_DIR.relative_to(ROOT)}"
    )
    if failed:
        print("Some images could not be fetched; those links were left untouched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
