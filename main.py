#!/usr/bin/env python3
"""Entrypoint for the news-image-20261118 entry.

Usage:
    python3 main.py --check     validate the entry files
    python3 main.py --serve     serve this directory over HTTP
    python3 main.py             same as --check (validate and exit)

Checks: index.html exists and references ad.png, ad.png exists and is
<= 8 MB, index.html is <= 2 MB, and README.md carries the make.fun badges.
"""

import argparse
import functools
import http.server
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MAX_IMAGE_MB = 8
MAX_PAGE_MB = 2


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    return ok


def run_checks():
    results = []

    html_path = os.path.join(ROOT, "index.html")
    html_ok = os.path.isfile(html_path)
    results.append(check("index.html exists", html_ok))
    html = ""
    if html_ok:
        with open(html_path, encoding="utf-8") as f:
            html = f.read()
        results.append(check("index.html references ad.png", "ad.png" in html))
        size_mb = os.path.getsize(html_path) / (1024 * 1024)
        results.append(check(
            "index.html <= 2 MB", size_mb <= MAX_PAGE_MB,
            f"{size_mb:.2f} MB"))

    img_path = os.path.join(ROOT, "ad.png")
    img_ok = os.path.isfile(img_path)
    results.append(check("ad.png exists", img_ok))
    if img_ok:
        size_mb = os.path.getsize(img_path) / (1024 * 1024)
        results.append(check(
            "ad.png <= 8 MB", size_mb <= MAX_IMAGE_MB,
            f"{size_mb:.2f} MB"))

    readme_path = os.path.join(ROOT, "README.md")
    readme_ok = os.path.isfile(readme_path)
    results.append(check("README.md exists", readme_ok))
    if readme_ok:
        with open(readme_path, encoding="utf-8") as f:
            readme = f.read()
        results.append(check(
            "README.md contains make.fun badges",
            "make.fun/badge" in readme))
        results.append(check(
            "README badge URLs name this competition",
            "news-image-20261118" in readme))

    return results


def serve(port):
    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler, directory=ROOT)
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Serving {ROOT} at http://127.0.0.1:{port}/ (Ctrl-C to stop)")
        httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true",
                       help="validate the entry files and exit")
    group.add_argument("--serve", action="store_true",
                       help="serve the entry over HTTP")
    parser.add_argument("--port", type=int, default=8000,
                        help="port for --serve (default 8000)")
    args = parser.parse_args()

    if args.check:
        results = run_checks()
        ok = all(results)
        print(f"{sum(results)}/{len(results)} checks passed."
              if ok else "Some checks FAILED.")
        sys.exit(0 if ok else 1)
    if args.serve:
        serve(args.port)
    # No arguments: validate the entry files and exit, so a plain run
    # completes instead of serving forever.
    results = run_checks()
    ok = all(results)
    print(f"{sum(results)}/{len(results)} checks passed."
          if ok else "Some checks FAILED.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
