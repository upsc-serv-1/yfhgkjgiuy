#!/usr/bin/env python3
"""Phase 1 audit — parse inputs/merged_publish_ready_v17.md into a full card inventory.

Outputs:
  scripts/stage2/v17_inventory.json  — structured per-card data, distributions, hierarchy, issues
  stdout summary

Card format (v17):
  ## id: GS1-HIST-0001
  paper: "GS-1" ... (metadata lines until first block)
  :::quote / :::introduction / :::examples / :::data / :::conclusion / :::detail label="..." / :::image
  ... content ...
  :::            (closing fence; may be indented)

Re-run: python3 scripts/stage2/audit_cards.py
"""
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "inputs" / "merged_publish_ready_v17.md"
OUT = REPO / "scripts" / "stage2" / "v17_inventory.json"

ID_RE = re.compile(r"^##\s+id:\s*(\S+)\s*$")
META_RE = re.compile(r"^([A-Za-z_]+):\s*(.*)$")
HEAD_RE = re.compile(r"^#{1,6}\s")
URL_RE = re.compile(r"https?://[^\s)\"'>\]]+")
KNOWN_BLOCKS = {"quote", "introduction", "examples", "data", "conclusion", "detail", "image"}


def parse_blocks_and_meta(chunk, cid, issues):
    """Return (meta_dict, blocks_list). blocks: [{name,label,lines}]"""
    meta, blocks, cur = {}, [], None
    in_meta = True
    for l in chunk[1:]:
        ls = l.strip()
        if ls == ":::":
            if cur is None:
                issues.append({"card": cid, "type": "stray_close", "detail": f"line context: {l[:40]}"})
            else:
                blocks.append(cur)
                cur = None
        elif ls.startswith(":::") and len(ls) > 3:
            body = ls[3:].strip()
            m2 = re.match(r"([A-Za-z]+)\s*(.*)", body)
            if not m2:
                issues.append({"card": cid, "type": "malformed_open", "detail": ls[:60]})
                continue
            if cur is not None:
                issues.append({"card": cid, "type": "nested_open", "detail": f"{cur['name']} then {m2.group(1).lower()}"})
                blocks.append(cur)
                cur = None
            name = m2.group(1).lower()
            rest = m2.group(2).strip()
            label = None
            if rest.lower().startswith("label="):
                label = rest[6:].strip().strip("\"'")
            cur = {"name": name, "label": label, "lines": []}
            if rest and not rest.lower().startswith("label="):
                cur["lines"].append(rest)
            if name not in KNOWN_BLOCKS:
                issues.append({"card": cid, "type": "unknown_block", "detail": name})
            in_meta = False
        else:
            if cur is not None:
                cur["lines"].append(l)
            else:
                st = ls
                if not st:
                    continue
                if HEAD_RE.match(l):
                    issues.append({"card": cid, "type": "unexpected_heading", "detail": st[:80]})
                elif in_meta:
                    mm = META_RE.match(st)
                    if mm:
                        meta[mm.group(1)] = mm.group(2).strip()
                    else:
                        issues.append({"card": cid, "type": "unparsed_meta", "detail": st[:80]})
    if cur is not None:
        issues.append({"card": cid, "type": "unclosed_block", "detail": cur["name"]})
        blocks.append(cur)
    return meta, blocks


def clean(v):
    return (v or "").strip().strip("\"'")


def lst(v):
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    if not v:
        return []
    return [x.strip().strip("\"'") for x in v.split(",") if x.strip()]


def main():
    text = SRC.read_text(encoding="utf-8")
    lines = text.splitlines()
    starts = [i for i, l in enumerate(lines) if ID_RE.match(l)]
    if not starts:
        print("FATAL: no '## id:' card headers found"); sys.exit(1)

    preamble = [l for l in lines[: starts[0]] if l.strip()]
    cards, issues = [], []
    for idx, s in enumerate(starts):
        e = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        chunk = lines[s:e]
        cid = ID_RE.match(chunk[0]).group(1)
        card = {"id": cid, "line": s + 1, "issues": []}
        meta, blocks = parse_blocks_and_meta(chunk, cid, issues)

        card.update({
            "paper": clean(meta.get("paper")),
            "subject": clean(meta.get("subject")),
            "section_group": clean(meta.get("section_group")),
            "microtopic": clean(meta.get("microtopic")),
            "subtopic": clean(meta.get("subtopic")),
            "card_title": clean(meta.get("card_title")),
            "card_type": clean(meta.get("card_type")),
            "sections_meta": lst(meta.get("sections")),
            "flags": lst(meta.get("flags")),
            "status": clean(meta.get("status")),
        })
        card["blocks"] = [{
            "name": b["name"], "label": b["label"],
            "line_count": len(b["lines"]),
            "word_count": sum(len(x.split()) for x in b["lines"]),
            "empty": not any(x.strip() for x in b["lines"]),
        } for b in blocks]
        card["block_names"] = [b["name"] for b in blocks]
        card["has_image"] = "image" in card["block_names"]
        card["image_urls"] = [" ".join(b["lines"]).strip() for b in blocks if b["name"] == "image"]
        chunk_urls = set(URL_RE.findall("\n".join(chunk[1:])))
        img_set = set(u.strip() for u in card["image_urls"] if u.strip())
        card["other_urls"] = sorted(chunk_urls - img_set)
        card["word_count"] = sum(b["word_count"] for b in card["blocks"])

        # per-card issue tags (mirrored from global issues for quick filtering)
        if card["sections_meta"] and card["sections_meta"] != card["block_names"]:
            card["issues"].append("sections-meta-mismatch")
            issues.append({"card": cid, "type": "sections_meta_mismatch",
                           "detail": f"meta={card['sections_meta']} actual={card['block_names']}"})
        for b in card["blocks"]:
            if b["empty"]:
                card["issues"].append(f"empty-block:{b['name']}")
                issues.append({"card": cid, "type": "empty_block", "detail": b["name"]})
        for f in ("card_title", "subtopic", "microtopic", "paper", "subject"):
            if not card[f]:
                card["issues"].append(f"missing-meta:{f}")
                issues.append({"card": cid, "type": "missing_meta", "detail": f})
        if not card["blocks"]:
            card["issues"].append("no-blocks")
            issues.append({"card": cid, "type": "no_blocks", "detail": ""})
        if card["status"] and card["status"] != "polished":
            issues.append({"card": cid, "type": "status_not_polished", "detail": card["status"]})
        cards.append(card)

    ids = Counter(c["id"] for c in cards)
    for k, n in ids.items():
        if n > 1:
            issues.append({"card": k, "type": "duplicate_id", "detail": f"{n} occurrences"})

    # ---- distributions ----
    paper_c = Counter(c["paper"] for c in cards)
    subject_c = Counter(c["subject"] for c in cards)
    paper_subject = defaultdict(Counter)
    subj_groups = defaultdict(Counter)
    hierarchy = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
    for c in cards:
        paper_subject[c["paper"]][c["subject"]] += 1
        subj_groups[f"{c['paper']} | {c['subject']}"][c["section_group"]] += 1
        hierarchy[c["paper"]][c["subject"]][c["section_group"]][c["subtopic"]].append(c["id"])
    card_type_c = Counter(c["card_type"] for c in cards)
    status_c = Counter(c["status"] for c in cards)
    flags_c = Counter(f for c in cards for f in c["flags"])
    block_c = Counter(b["name"] for c in cards for b in c["blocks"])
    words = [c["word_count"] for c in cards]
    image_cards = [c for c in cards if c["has_image"]]
    other_url_cards = [c for c in cards if c["other_urls"]]
    issue_types = Counter(i["type"] for i in issues)

    result = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "source": "inputs/merged_publish_ready_v17.md",
        "total_cards": len(cards),
        "preamble_lines": preamble,
        "distributions": {
            "paper": dict(paper_c),
            "subject": dict(subject_c.most_common()),
            "paper_subject": {p: dict(sc.most_common()) for p, sc in paper_subject.items()},
            "subject_section_groups": {k: dict(v.most_common()) for k, v in subj_groups.items()},
            "card_type": dict(card_type_c),
            "status": dict(status_c),
            "flags": dict(flags_c.most_common()),
            "block_types": dict(block_c),
        },
        "word_stats": {
            "total": sum(words), "mean": round(sum(words) / len(words), 1) if words else 0,
            "min": min(words) if words else 0, "max": max(words) if words else 0,
        },
        "image_cards": len(image_cards),
        "image_urls_total": sum(len(c["image_urls"]) for c in cards),
        "other_urls_total": sum(len(c["other_urls"]) for c in cards),
        "hierarchy": json.loads(json.dumps(hierarchy)),
        "issues": issues,
        "cards": cards,
    }
    OUT.write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")

    # ---- stdout summary ----
    print(f"CARDS: {len(cards)}  (ids unique: {len(ids) == len(cards)})")
    print(f"papers: {dict(paper_c)}")
    print("paper -> subject:")
    for p in sorted(paper_subject):
        print(f"  {p}: " + ", ".join(f"{s}={n}" for s, n in paper_subject[p].most_common()))
    print(f"card_type: {dict(card_type_c)}  status: {dict(status_c)}")
    print(f"flags: {dict(flags_c.most_common())}")
    print(f"block_types: {dict(block_c)}")
    print(f"words: total={result['word_stats']['total']} mean={result['word_stats']['mean']} "
          f"min={result['word_stats']['min']} max={result['word_stats']['max']}")
    print(f"image cards: {len(image_cards)}  image url blocks: {result['image_urls_total']}")
    print(f"cards with other external URLs: {len(other_url_cards)}  (total urls: {result['other_urls_total']})")
    print(f"ISSUES by type: {dict(issue_types) or 'NONE'}")
    if issues:
        by_card = Counter(i["card"] for i in issues)
        print(f"cards with issues: {len(by_card)}; top: {by_card.most_common(10)}")
    if preamble:
        print(f"preamble (non-empty lines before first card): {len(preamble)}")
        for l in preamble[:5]:
            print(f"  | {l[:80]}")
    print(f"\nJSON written: {OUT}")


if __name__ == "__main__":
    main()
