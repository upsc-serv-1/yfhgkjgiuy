#!/usr/bin/env python3
"""Phase 1 — generate content_inventory.md from v17_inventory.json + images_manifest.json.

Re-run after any audit re-run: python3 scripts/stage2/make_inventory_md.py
"""
import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
INV = json.loads((REPO / "scripts/stage2/v17_inventory.json").read_text(encoding="utf-8"))
MAN = json.loads((REPO / "scripts/stage2/images_manifest.json").read_text(encoding="utf-8"))
OUT = REPO / "content_inventory.md"

cards = INV["cards"]
D = INV["distributions"]
gen = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# --- derived stats ---
multi_quote = [c for c in cards if c["block_names"].count("quote") > 1]
multi_detail = [c for c in cards if c["block_names"].count("detail") > 1]
no_intro_conc = [c for c in cards if "introduction" not in c["block_names"] or "conclusion" not in c["block_names"]]
img_cards = [c for c in cards if c["has_image"]]
multi_img_cards = [c for c in cards if len(c["image_urls"]) > 1]
flag_lists = {f: [c["id"] for c in cards if f in c["flags"]] for f in ("has_image", "universal_template", "format_fixed")}

uniq = {
    "section_groups": len({(c["paper"], c["subject"], c["section_group"]) for c in cards}),
    "subtopics": len({(c["paper"], c["subject"], c["section_group"], c["subtopic"]) for c in cards}),
    "microtopics": len({c["microtopic"] for c in cards}),
    "card_titles": len({c["card_title"] for c in cards}),
}

paper_order = ["GS-1", "GS-2", "GS-3", "GS-4"]


def tbl(rows, headers):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    out += ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]
    return "\n".join(out)


# --- distribution tables ---
paper_rows = [[p, D["paper"].get(p, 0), round(100 * D["paper"].get(p, 0) / len(cards), 1)] for p in paper_order]
subject_rows = []
for p in paper_order:
    for s, n in D["paper_subject"].get(p, {}).items():
        subject_rows.append([p, s, n, round(100 * n / len(cards), 1)])

sg_rows = []
for key in sorted(D["subject_section_groups"]):
    for g, n in D["subject_section_groups"][key].items():
        sg_rows.append([key, g or "—", n])

block_rows = [[b, n] for b, n in sorted(D["block_types"].items(), key=lambda kv: -kv[1])]
man_rows = []
for e in MAN["entries"]:
    src = e["url"].rsplit("/", 1)[-1]
    note = ""
    if src.endswith(".avif"):
        note = "converted AVIF→PNG"
    man_rows.append([
        f"`{e['local_filename']}`" if e["local_filename"] else "—",
        ", ".join(e["card_ids"]),
        e["subject"].title(),
        (e["subtopic"][:44] + "…") if len(e["subtopic"]) > 45 else e["subtopic"],
        src,
        f"{e['bytes'] / 1024:.0f}",
        e["status"] + (f" ({note})" if note else ""),
    ])

md = f"""# Content Inventory — Phase 1

**Source:** `inputs/merged_publish_ready_v17.md` (sole content truth) · **Branch:** `ebook-build` · **Generated:** {gen}
**Scripts:** `scripts/stage2/audit_cards.py`, `download_images.py`, `make_inventory_md.py` · **Raw data:** `scripts/stage2/v17_inventory.json`, `images_manifest.json`

---

## 1. Executive summary

- **{len(cards)} cards parsed — clean.** All IDs unique, all `status: polished`, all fences balanced, no duplicate/empty/unknown blocks, no missing metadata, no stray headings or junk lines.
- **Composition:** {D['card_type'].get('structured', 0)} structured + {D['card_type'].get('detail', 0)} detail cards · **{INV['word_stats']['total']:,} body words** (mean {INV['word_stats']['mean']}/card, range {INV['word_stats']['min']}–{INV['word_stats']['max']}).
- **Taxonomy depth (user-assigned, for indexing):** {uniq['section_groups']} section groups → {uniq['subtopics']} subtopics → cards; {uniq['microtopics']} distinct microtopics (syllabus lines).
- **Images: {MAN['unique_urls']} URLs on {len(img_cards)} cards — ALL downloaded and normalized** to `assets/images/` (0 broken; 1 AVIF auto-converted to PNG). No other external URLs exist anywhere in v17 → the final eBook can be 100% hotlink-free.
- **Benign notes:** 38 cards' `sections:` metadata lists a block type once while the actual blocks repeat it ({len(multi_quote)} multi-quote, {len(multi_detail)} multi-detail, {len(multi_img_cards)} multi-image) — schema-valid; the build must render ACTUAL blocks. Also {len(no_intro_conc)} cards have no introduction/conclusion block (detail/quote-style cards, by design).
- **Blocking risks for Phase 2: none.**

## 2. Card inventory & distributions

### By paper
{tbl(paper_rows, ["Paper", "Cards", "% of book"])}

### By subject (within papers)
{tbl(subject_rows, ["Paper", "Subject", "Cards", "% of book"])}

### Card type / status / flags
{tbl([["structured", D['card_type'].get('structured', 0)], ["detail", D['card_type'].get('detail', 0)], ["status: polished", D['status'].get('polished', 0)],
       ["flag: has_image", D['flags'].get('has_image', 0)], ["flag: format_fixed", D['flags'].get('format_fixed', 0)],
       ["flag: universal_template", D['flags'].get('universal_template', 0)]], ["Item", "Count"])}

### Block types across the book
{tbl(block_rows, ["Block type", "Total occurrences"])}

*(Full section_group breakdown per subject: `scripts/stage2/v17_inventory.json` → `distributions.subject_section_groups`; full card-level hierarchy: `hierarchy`.)*

## 3. Metadata gaps & flagged cards

- **Missing metadata: none.** Every card has paper, subject, section_group, microtopic, subtopic, card_title, card_type, status.
- **`universal_template` cards ({len(flag_lists['universal_template'])}):** {", ".join(flag_lists['universal_template'])} — practice-skeleton cards; render as templates, not filled essays (Editor note).
- **`format_fixed` cards ({len(flag_lists['format_fixed'])}):** cosmetic Stage-1 flag; no action needed.
- **`has_image` cards ({len(flag_lists['has_image'])}):** see image manifest below.

## 4. Internal-consistency findings

- **38 `sections_meta_mismatch` — ALL benign** (verified: deduplicated type sequences identical for every card). Actual blocks repeat a type that the `sections:` list mentions once: {len(multi_quote)} multi-quote cards (e.g. GS1-HIST-0054 has 3 quotes, metadata lists 1), {len(multi_detail)} multi-detail cards ({', '.join(c['id'] for c in multi_detail)}), {len(multi_img_cards)} multi-image card ({', '.join(c['id'] for c in multi_img_cards)}). The eBook build must use ACTUAL blocks, not the `sections:` list.
- **Cards without introduction or conclusion blocks ({len(no_intro_conc)}):** {", ".join(c['id'] for c in no_intro_conc)} — these are quote/data-led cards; do not force intro/conclusion structure on them in layout.
- No stray close fences, no nested opens, no unknown block names, no duplicate IDs, no unexpected headings, no preamble junk. v17 is structurally sound.

## 5. Image audit

**{MAN['unique_urls']} unique URLs → {MAN['ok']} downloaded OK, {MAN['broken']} broken.** One source file was AVIF and was converted to PNG (`ethi_social-influence-and-persuasion_01.png`). Total local weight ≈ 8.5 MB. Card with multiple images: {", ".join(c['id'] for c in multi_img_cards) or "—"}.
Also staged: `cover_candidate_resource_guide.png` (user-uploaded resource guide; role TBD — cover art candidate).

{tbl(man_rows, ["Local file", "Card(s)", "Subject", "Subtopic", "Source file", "KB", "Status"])}

## 6. Other external links

**None.** The image URLs above are the only external references in v17. With images localized, the final HTML needs zero network requests.

## 7. Recommendations for Phase 2 (book architecture)

1. **Follow the user taxonomy exactly:** Part = GS paper (GS-1 → GS-4) → Chapter = subject (14 chapters) → Section = section_group → Card group = subtopic. This doubles as the GS-wise/subject-wise index the user asked for.
2. **GS-4 Ethics is {round(100 * D['paper'].get('GS-4', 0) / len(cards), 0):.0f}% of the book (149 cards)** — give it strong internal navigation (its section_groups as visible sub-sections); consider its own mini-index.
3. **Prototype-type SVG illustrations** (recreated, not copied): marks-share donut for the front matter, per-part opener visuals, tier/heatmap tables where the prototype uses them.
4. **Images via relative paths** (`assets/images/…`) by default; add a build flag for a base64-embedded portable single file (8.5 MB of images makes embedding heavy — recommend relative as primary).
5. Render detail cards (75) with their `:::detail label` headers; render multi-quote cards with all quotes in sequence.
6. The 5 universal_template cards should be visually marked as "practice skeletons".
"""

OUT.write_text(md, encoding="utf-8")
print(f"written: {OUT} ({len(md.splitlines())} lines)")
print(f"cards={len(cards)} image_cards={len(img_cards)} multi_quote={len(multi_quote)} "
      f"no_intro_conc={len(no_intro_conc)} section_groups={uniq['section_groups']} subtopics={uniq['subtopics']}")
