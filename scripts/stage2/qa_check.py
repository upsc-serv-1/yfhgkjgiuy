#!/usr/bin/env python3
"""Phase 8 — QA audit of final_ebook.html against the PLAN.md §6 checklist.

Checks:
  1. Card presence: 551 unique #card-<ID> articles
  2. PROTECTED CONTENT: per-block verbatim text diff of the ASSEMBLED HTML vs v17
     + digit-sequence multiset equality per card (every number/year/percentage)
  3. Images: all local, no hotlinks, alt text present on every <img>
  4. Links: all internal hrefs resolve; no duplicate ids
  5. Heading hierarchy: no skipped levels inside the document flow
  6. Print CSS: @page A4 + break rules + color-adjust present
  7. HTML sanity: lang, title, meta, font fallbacks, no backdrop-filter,
     no TODO/FIXME/lorem markers, balanced tags (rough)
Exit code 1 on any failure. Writes qa_report_data.json for the report generator.
"""
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
V17 = REPO / "inputs" / "merged_publish_ready_v17.md"
FINAL = REPO / "final_ebook.html"

sys.path.insert(0, str(REPO / "scripts" / "stage2"))
from convert_cards import parse_cards, card_ctx, render_block_for_verify  # noqa: E402

INLINE_TAG = re.compile(r"</?(?:strong|em)>")
BLOCK_TAG = re.compile(r"<[^>]+>")
results = {}


def norm_src(lines):
    t = " ".join(lines)
    t = t.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", t).strip()


def norm_html(h):
    t = INLINE_TAG.sub("", h)
    t = BLOCK_TAG.sub(" ", t)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def digits_of(text):
    return re.findall(r"\d+(?:[.,]\d+)?", text)


def main():
    doc = FINAL.read_text(encoding="utf-8")
    cards_src = parse_cards(V17.read_text(encoding="utf-8"))
    fails = []

    # ---- 1. card presence ----
    art_ids = re.findall(r'<article class="card" id="card-([^"]+)"', doc)
    n_unique = len(set(art_ids))
    results["cards_present"] = {
        "articles": len(art_ids), "unique": n_unique,
        "pass": len(art_ids) == 551 and n_unique == 551 and len(cards_src) == 551,
    }
    if not results["cards_present"]["pass"]:
        fails.append("card presence")

    # ---- 2. verbatim protected content on the ASSEMBLED file ----
    block_fail = 0
    digit_fail = []
    src_by_id = {c["id"]: c for c in cards_src}
    for cid, c in src_by_id.items():
        m = re.search(rf'<article class="card" id="card-{re.escape(cid)}">(.*?)</article>', doc, re.S)
        if not m:
            block_fail += len(c["blocks"])
            digit_fail.append((cid, "MISSING CARD"))
            continue
        art = m.group(1)
        # text-level compare per block (same model as generation gate)
        art_txt = norm_html(art)
        for b in c["blocks"]:
            if b["name"] == "image":
                continue
            exp = norm_src(b["lines"])
            if exp and exp not in art_txt:
                block_fail += 1
                if block_fail <= 5:
                    print(f"  BLOCK MISS {cid} :: {b['name']} :: {exp[:80]!r}")
        # digit multiset per card (protects every number; image blocks are
        # covered by the images check — their URLs become local filenames BY DESIGN)
        src_digits = Counter()
        for b in c["blocks"]:
            if b["name"] == "image":
                continue
            for d in digits_of(" ".join(b["lines"])):
                src_digits[d] += 1
        got_digits = Counter(digits_of(re.sub(r"<[^>]+>", " ", art)))
        # ignore digits introduced by chrome (card id is inside art, page numbers are outside)
        got_digits.subtract(Counter(digits_of(cid.replace("-", " "))))
        if any(v > 0 for v in (src_digits - got_digits).values()):
            digit_fail.append((cid, dict(src_digits - got_digits)))
    results["protected_content"] = {
        "cards_compared": len(src_by_id), "block_mismatches": block_fail,
        "digit_mismatch_cards": len(digit_fail), "sample": digit_fail[:5],
        "pass": block_fail == 0 and not digit_fail,
    }
    if not results["protected_content"]["pass"]:
        fails.append("protected content")

    # ---- 3. images ----
    imgs = re.findall(r"<img\b[^>]*>", doc)
    hot = [i for i in imgs if 'src="http' in i]
    no_alt = [i[:80] for i in imgs if "alt=" not in i]
    ext_src = re.findall(r'src="(http[^"]+)"', doc)
    results["images"] = {
        "imgs": len(imgs), "hotlinked": len(hot), "missing_alt": len(no_alt),
        "external_srcs": [s for s in ext_src if "fonts.g" not in s][:5],
        "pass": not hot and not no_alt,
    }
    if not results["images"]["pass"]:
        fails.append("images")

    # ---- 4. links & ids ----
    ids = re.findall(r'id="([^"]+)"', doc)
    hrefs = re.findall(r'href="#([^"]+)"', doc)
    unresolved = sorted({h for h in hrefs if h not in set(ids)})
    results["links"] = {
        "ids": len(ids), "hrefs": len(hrefs), "unresolved": unresolved[:5],
        "duplicate_ids": [k for k, v in Counter(ids).items() if v > 1][:5],
        "pass": not unresolved and len(ids) == len(set(ids)),
    }
    if not results["links"]["pass"]:
        fails.append("links")

    # ---- 5. heading hierarchy (no skipped levels) ----
    skips = []
    level = 0
    for m in re.finditer(r"<(h[1-4])[^>]*>", doc):
        lv = int(m.group(1)[1])
        if lv > level + 1:
            skips.append((level, lv))
        level = lv
    results["headings"] = {"skipped_levels": len(skips), "pass": not skips}
    if not results["headings"]["pass"]:
        fails.append("headings")

    # ---- 6. print CSS ----
    need = ["@media print", "@page", "size:A4", "break-after:page",
            "print-color-adjust:exact", "break-inside:avoid"]
    missing_css = [n for n in need if n not in doc]
    results["print_css"] = {"missing": missing_css, "pass": not missing_css}
    if not results["print_css"]["pass"]:
        fails.append("print css")

    # ---- 7. HTML sanity ----
    sanity = {
        "lang_attr": '<html lang="en">' in doc,
        "title": "PYQ Nano Analysis — GS Mains" in doc,
        "meta_desc": 'name="description"' in doc,
        "font_fallbacks": "Georgia" in doc and "system-ui" in doc and "ui-monospace" in doc,
        "no_backdrop_filter": "backdrop-filter" not in doc,
        "no_todo_markers": not re.search(r"\b(TODO|FIXME|lorem)\b", doc, re.I),
        "pg_numbers_stamped": bool(re.search(r'class="pg-n">\d{3} / \d{3}<', doc)),
        "tags_balanced": all(doc.count(f"<{t}") == doc.count(f"</{t}>")
                            for t in ("div", "article", "section", "figure", "table", "ul")),
    }
    results["sanity"] = {"checks": sanity, "pass": all(sanity.values())}
    if not results["sanity"]["pass"]:
        fails.append(f"sanity: {[k for k, v in sanity.items() if not v]}")

    # ---- summary ----
    results["overall_pass"] = not fails
    results["sheets"] = doc.count('<div class="sheet')
    results["size_mb"] = round(len(doc) / 1024 / 1024, 2)
    (REPO / "scripts" / "stage2" / "qa_report_data.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: (v["pass"] if isinstance(v, dict) and "pass" in v else v)
                      for k, v in results.items()}, indent=1))
    if fails:
        print("QA FAILED:", fails)
        sys.exit(1)
    print("QA PASSED — all checks green")


if __name__ == "__main__":
    main()
