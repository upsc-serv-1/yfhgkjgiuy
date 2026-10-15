#!/usr/bin/env python3
"""Phase 7 (v2, post-review) — assemble final_ebook.html from src/ partials.

Order: fm1 cover · fm2 foreword · fm3 how-to-use · bm1 subject-wise index
       (clickable CONTENTS, front position) · pt1..pt4 part openers with their
       chapters interleaved · bm2 back cover.
Also: inlines src/theme.css into a single <style>, adds the floating INDEX
button, stamps sequential page numbers into every .pg-n placeholder, and
runs assembly self-checks (card count, anchor resolution).

Usage:
  python scripts/stage2/build.py            # relative image paths (default)
  python scripts/stage2/build.py --embed    # base64-embed images (portable single file)
"""
import base64
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "src"
OUT = REPO / "final_ebook.html"

ORDER = [
    "fm1_cover.html", "fm2_foreword.html", "fm3_how_to_use.html",
    # subject-wise clickable index — front position, right after How-to-Use
    "bm1_index.html",
    # GS-1
    "pt1_gs1_opener.html", "ch01_history.html", "ch02_geography.html", "ch03_society.html",
    # GS-2
    "pt2_gs2_opener.html", "ch04_polity.html", "ch05_governance.html", "ch06_ir.html",
    "ch07_social-justice.html",
    # GS-3
    "pt3_gs3_opener.html", "ch08_economy.html", "ch09_security.html", "ch10_agriculture.html",
    "ch11_snt.html", "ch12_environment.html", "ch13_disaster.html",
    # GS-4
    "pt4_gs4_opener.html", "ch14_ethics.html",
    # back matter
    "bm2_back_cover.html",
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport"/>
<title>PYQ Nano Analysis — GS Mains · The Answer-Writing Playbook</title>
<meta name="description" content="551 answer cards for UPSC GS Mains Papers I–IV: quotes, introductions, examples, data and conclusions in ready answer language."/>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&amp;family=IBM+Plex+Mono:wght@500&amp;family=IBM+Plex+Sans:wght@400;600&amp;display=swap" rel="stylesheet"/>
<style>
{css}
</style>
</head>
<body>
<a class="skip" href="#fm-cover">Skip to cover</a>
<a class="to-ix" href="#ix-master" title="Jump to the subject-wise index">INDEX</a>
<div class="book">
"""


def main():
    embed = "--embed" in sys.argv[1:]

    # ---- load partials in order ----
    parts = []
    for name in ORDER:
        p = SRC / name
        if not p.exists():
            sys.exit(f"FATAL: missing partial {name}")
        parts.append(p.read_text(encoding="utf-8"))
    body = "\n".join(parts)

    # ---- optional base64 image embedding ----
    if embed:
        refs = sorted(set(re.findall(r'src="(assets/images/[^"]+)"', body)))
        for ref in refs:
            f = REPO / ref
            if not f.exists():
                sys.exit(f"FATAL: missing image {ref}")
            mime = "image/png" if f.suffix == ".png" else "image/jpeg"
            b64 = base64.b64encode(f.read_bytes()).decode("ascii")
            body = body.replace(f'src="{ref}"', f'src="data:{mime};base64,{b64}"')
        print(f"embedded {len(refs)} images as base64")

    # ---- stamp sequential page numbers ----
    # every sheet carries two placeholders: <span class="pg-n">·</span>
    total_sheets = body.count('<div class="sheet')
    pages = []
    idx = 0
    pos = 0
    out = []
    pat = re.compile(r'(<div class="sheet)|(?:<span class="pg-n">·</span>)')
    page_no = 0
    for m in pat.finditer(body):
        if m.group(1):  # sheet open
            page_no += 1
            out.append(body[pos:m.start()])
            out.append(m.group(1))
            pos = m.end()
        else:  # placeholder
            out.append(body[pos:m.start()])
            out.append(f'<span class="pg-n">{page_no:03d} / {total_sheets:03d}</span>')
            pos = m.end()
    out.append(body[pos:])
    body = "".join(out)

    # ---- assemble ----
    css = (SRC / "theme.css").read_text(encoding="utf-8")
    html = HEAD.format(css=css) + body + "\n</div>\n</body>\n</html>\n"
    OUT.write_text(html, encoding="utf-8")

    # ---- self-checks ----
    n_cards = len(re.findall(r'<article class="card[^"]*" id="card-', html))
    ids = set(re.findall(r'id="([^"]+)"', html))
    hrefs = re.findall(r'href="#([^"]+)"', html)
    unresolved = sorted({h for h in hrefs if h not in ids})
    dups = len(ids) != len([i for i in re.findall(r'id="([^"]+)"', html)])
    imgs_ok = all((REPO / r).exists() for r in re.findall(r'src="(assets/images/[^"]+)"', html))
    print(f"final_ebook.html: {len(html)/1024/1024:.2f} MB · sheets: {total_sheets} · cards: {n_cards}")
    print(f"self-check → cards 551: {'OK' if n_cards == 551 else 'FAIL'} · "
          f"anchors unresolved: {len(unresolved)} {'OK' if not unresolved else unresolved[:5]} · "
          f"duplicate ids: {'YES' if dups else 'no'} · image files: {'OK' if imgs_ok else 'MISSING'}")
    if n_cards != 551 or unresolved or dups or not imgs_ok:
        sys.exit(1)
    print("ASSEMBLY OK")


if __name__ == "__main__":
    main()
