#!/usr/bin/env python3
"""Phase 2 — reverse-engineer the structural skeleton of the prototype HTML.

Extracts: comments (section delimiters), sheet/section organization, heading
hierarchy, distinct class vocabulary with frequencies, id map, and the
component patterns (cards, heatmaps, donuts, TOC). Output: a readable skeleton
report at scripts/stage2/prototype_skeleton.md + raw data JSON.
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROTO = ROOT / "inputs" / "prototype_pyq_nano_gs_mains.html"
OUT_DIR = ROOT / "scripts" / "stage2"

html = PROTO.read_text(encoding="utf-8")

# --- 1. comments (often delimit logical sections) -------------------------
comments = re.findall(r"<!--\s*(.*?)\s*-->", html, flags=re.S)

# --- 2. structural elements in document order -----------------------------
# Sheets, sections, articles, headers, footers, navs + ids
tag_pat = re.compile(
    r"<(sheet|section|article|header|footer|nav|aside|main|div|table|svg)\b([^>]*)>",
    re.I,
)
events = []  # (pos, tag, id, classes)
for m in tag_pat.finditer(html):
    tag = m.group(1).lower()
    attrs = m.group(2)
    id_m = re.search(r'id="([^"]+)"', attrs)
    cls_m = re.search(r'class="([^"]+)"', attrs)
    # only keep structural anchors: elements with id or a known structural class
    cls = cls_m.group(1) if cls_m else ""
    classes = cls.split()
    keep = (
        id_m
        or tag in {"sheet", "section", "article", "header", "footer", "nav", "table", "svg"}
        or any(c.startswith(("p1", "part", "ch", "sheet", "book", "hm", "idx", "toc")) for c in classes)
    )
    if keep:
        events.append(
            {
                "pos": m.start(),
                "tag": tag,
                "id": id_m.group(1) if id_m else None,
                "classes": classes,
            }
        )

# --- 3. headings in order --------------------------------------------------
headings = []
for m in re.finditer(r"<(h[1-6])\b[^>]*>(.*?)</\1>", html, flags=re.S | re.I):
    text = re.sub(r"<[^>]+>", "", m.group(2))
    text = re.sub(r"\s+", " ", text).strip()
    headings.append({"level": m.group(1).lower(), "text": text[:120], "pos": m.start()})

# --- 4. class vocabulary ----------------------------------------------------
all_classes = Counter()
for cls_attr in re.findall(r'class="([^"]+)"', html):
    for c in cls_attr.split():
        all_classes[c] += 1

# --- 5. anchor links (TOC targets) -----------------------------------------
hrefs = Counter(re.findall(r'href="#([^"]+)"', html))
ids_defined = {m.group(1) for m in re.finditer(r'id="([^"]+)"', html)}

# --- 6. sheet organization --------------------------------------------------
sheets = re.findall(r'<div class="sheet[^"]*"[^>]*id="([^"]*)"', html)
sheet_count = html.count('class="sheet')
p1_count = len(re.findall(r'class="sheet p1', html))

# --- report -----------------------------------------------------------------
lines = []
A = lines.append
A("# Prototype structural skeleton — extracted " + __import__("datetime").date.today().isoformat())
A("")
A(f"- Total size: {len(html)/1024/1024:.2f} MB · lines: {html.count(chr(10))+1}")
A(f"- Comments ({len(comments)}): first 120 listed below")
A(f"- Sheets: {sheet_count} total · p1 (A4 min-height): {p1_count}")
A(f"- Headings: {len(headings)} · distinct classes: {len(all_classes)} · ids defined: {len(ids_defined)} · anchor-hrefs: {len(hrefs)}")
A(f"- Unresolved anchor targets (href without id): {len(set(hrefs) - ids_defined)}")
A("")
A("## Top-level comments (section delimiters, in order)")
A("")
for c in comments[:120]:
    c1 = re.sub(r"\s+", " ", c).strip()
    if len(c1) > 140:
        c1 = c1[:140] + "…"
    A(f"- {c1}")
A("")
A("## Heading hierarchy (document order)")
A("")
for h in headings:
    A(f"{'  ' * (int(h['level'][1]) - 1)}- ({h['level']}) {h['text']}")
A("")
A("## Class vocabulary (frequency-sorted, top 220)")
A("")
for c, n in all_classes.most_common(220):
    A(f"- `{c}` × {n}")
A("")
A("## Sheet ids (page anchors, in order)")
A("")
for s in sheets:
    A(f"- `{s}`")
A("")

(OUT_DIR / "prototype_skeleton.md").write_text("\n".join(lines), encoding="utf-8")

raw = {
    "comments": comments,
    "headings": headings,
    "class_counts": dict(all_classes.most_common()),
    "ids": sorted(ids_defined),
    "anchor_hrefs": dict(hrefs.most_common()),
    "sheets": sheets,
    "counts": {
        "sheets": sheet_count,
        "p1": p1_count,
        "headings": len(headings),
    },
}
(OUT_DIR / "prototype_skeleton.json").write_text(
    json.dumps(raw, ensure_ascii=False, indent=1), encoding="utf-8"
)
print(f"sheets={sheet_count} p1={p1_count} headings={len(headings)} classes={len(all_classes)} ids={len(ids_defined)} comments={len(comments)}")
print("wrote prototype_skeleton.md + .json")
