#!/usr/bin/env python3
"""Compile every note in notes/ to PDF and write the list page to _site/.

    python3 build.py            # compile PDFs + write the page
    python3 build.py --no-pdf   # only rewrite the page (fast preview)

A note is any notes/<section>/<name>.tex. Title and summary come from the file:
    \\title{...}
    % summary: one line shown under the title
    % draft      <- skipped (not compiled, not listed)
"""
import argparse
import datetime as dt
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTES = ROOT / "notes"
OUT = ROOT / "_site"


def tex_arg(src: str, cmd: str) -> str | None:
    """Contents of the first \\cmd{...}, with nested braces."""
    m = re.search(r"\\" + cmd + r"\s*\{", src)
    if not m:
        return None
    i = start = m.end()
    depth = 1
    while i < len(src) and depth:
        depth += {"{": 1, "}": -1}.get(src[i], 0)
        i += 1
    return src[start : i - 1].strip()


def comment(src: str, key: str) -> str | None:
    m = re.search(rf"^%\s*{key}:\s*(.+?)\s*$", src, re.M)
    return m.group(1) if m else None


def is_draft(src: str) -> bool:
    return re.search(r"^%\s*draft\s*$", src, re.M) is not None


def last_updated(path: Path) -> str:
    r = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(path)],
        cwd=ROOT, capture_output=True, text=True,
    )
    if r.returncode == 0 and r.stdout.strip():
        return r.stdout.strip()
    return dt.date.fromtimestamp(path.stat().st_mtime).isoformat()


def compile_pdf(tex: Path, dest: Path) -> bool:
    env = dict(os.environ, TEXINPUTS=f"{ROOT / 'tex'}{os.pathsep}")  # trailing sep keeps defaults
    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run(
            ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
             "-file-line-error", f"-outdir={tmp}", tex.name],
            cwd=tex.parent, env=env, capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(f"\n✗ {tex.relative_to(ROOT)} failed to compile:", file=sys.stderr)
            print("\n".join(r.stdout.splitlines()[-30:]), file=sys.stderr)
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(Path(tmp) / f"{tex.stem}.pdf", dest)
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-pdf", action="store_true", help="skip LaTeX, only write the page")
    args = ap.parse_args()

    site = tomllib.loads((ROOT / "site.toml").read_text())
    OUT.mkdir(exist_ok=True)
    shutil.copy(ROOT / "assets" / "style.css", OUT / "style.css")

    ok = True
    sections_html = []
    for sec in site["sections"]:
        items = []
        for tex in sorted((NOTES / sec["dir"]).glob("*.tex")):
            src = tex.read_text()
            if is_draft(src):
                continue
            rel = f"pdf/{sec['dir']}/{tex.stem}.pdf"
            if not args.no_pdf:
                print(f"• {tex.relative_to(ROOT)}")
                ok &= compile_pdf(tex, OUT / rel)
            title = tex_arg(src, "title") or tex.stem
            summary = comment(src, "summary")
            source = f"{site['repo']}/blob/main/{tex.relative_to(ROOT)}"
            items.append(
                "<li>"
                f'<a class="title" href="{rel}">{html.escape(title)}</a>'
                f'<span class="meta">{last_updated(tex)} · <a href="{source}">tex</a></span>'
                + (f'<p class="summary">{html.escape(summary)}</p>' if summary else "")
                + "</li>"
            )
        if items:
            sections_html.append(
                f"<section><h2>{html.escape(sec['name'])}</h2><ul>{''.join(items)}</ul></section>"
            )

    links = " · ".join(
        f'<a href="{html.escape(l["url"])}">{html.escape(l["name"])}</a>'
        for l in site.get("links", [])
    )
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(site['title'])}</title>
<link rel="stylesheet" href="style.css">
<script>window.MathJax = {{ tex: {{ inlineMath: [['$', '$']] }} }};</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>
<body>
<header>
  <h1>{html.escape(site['title'])}</h1>
  <p>{html.escape(site['intro'])}</p>
  <p class="links">{links}</p>
</header>
<main>
{''.join(sections_html) or '<p>No notes yet.</p>'}
</main>
<footer>{html.escape(site['author'])} · updated {dt.date.today().isoformat()}</footer>
</body>
</html>
"""
    (OUT / "index.html").write_text(page)
    print(f"\nwrote {OUT / 'index.html'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
