#!/usr/bin/env python3
"""Phase 2 — build the definitive book architecture from v17 taxonomy.

Outputs:
  scripts/stage2/book_map.json   — machine-readable architecture (build input)
  ebook_structure.md data section is written by make_structure_md.py

Architecture (user-locked):
  Book → Front matter → Part=GS paper → Chapter=subject (14)
       → Section=section_group → card-group=subtopic → cards
Anchors: #fm-*, #pt-gsN, #ch-N (N=1..14), #sg-N (sections 1..48),
         #st-N (subtopics 1..209), #card-<CARD_ID> (551)
"""
import json
import re
from collections import OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INV = json.loads((ROOT / "scripts" / "stage2" / "v17_inventory.json").read_text(encoding="utf-8"))
OUT = ROOT / "scripts" / "stage2" / "book_map.json"

# --- subject order inside each paper (v17 natural order) -------------------
SUBJECTS = {
    "GS-1": ["HISTORY", "GEOGRAPHY", "SOCIETY"],
    "GS-2": ["POLITY", "GOVERNANCE", "INTERNATIONAL RELATIONS", "SOCIAL JUSTICE"],
    "GS-3": ["INDIAN ECONOMY", "INTERNAL SECURITY", "AGRICULTURE",
             "SCIENCE & TECHNOLOGY", "ENVIRONMENT", "DISASTER MANAGEMENT"],
    "GS-4": ["ETHICS, INTEGRITY & APTITUDE"],
}

SLUGS = {
    "HISTORY": "history", "GEOGRAPHY": "geography", "SOCIETY": "society",
    "POLITY": "polity", "GOVERNANCE": "governance",
    "INTERNATIONAL RELATIONS": "ir", "SOCIAL JUSTICE": "social-justice",
    "INDIAN ECONOMY": "economy", "INTERNAL SECURITY": "security",
    "AGRICULTURE": "agriculture", "SCIENCE & TECHNOLOGY": "snt",
    "ENVIRONMENT": "environment", "DISASTER MANAGEMENT": "disaster",
    "ETHICS, INTEGRITY & APTITUDE": "ethics",
}
# title-case display names for chapter headers
DISPLAY = {
    "HISTORY": "History", "GEOGRAPHY": "Geography", "SOCIETY": "Society",
    "POLITY": "Polity", "GOVERNANCE": "Governance",
    "INTERNATIONAL RELATIONS": "International Relations",
    "SOCIAL JUSTICE": "Social Justice", "INDIAN ECONOMY": "Indian Economy",
    "INTERNAL SECURITY": "Internal Security", "AGRICULTURE": "Agriculture",
    "SCIENCE & TECHNOLOGY": "Science & Technology", "ENVIRONMENT": "Environment",
    "DISASTER MANAGEMENT": "Disaster Management",
    "ETHICS, INTEGRITY & APTITUDE": "Ethics, Integrity & Aptitude",
}

hier = INV["hierarchy"]
cards_by_id = {c["id"]: c for c in INV["cards"]}

# --- build ordered architecture --------------------------------------------
chapter_no = 0
section_no = 0
subtopic_no = 0
chapters = []
parts = []

for paper in ["GS-1", "GS-2", "GS-3", "GS-4"]:
    part = {
        "paper": paper,
        "anchor": f"pt-{paper.lower().replace('-', '')}",  # pt-gs1
        "chapters": [],
        "card_count": 0,
        "word_count": 0,
    }
    for subject in SUBJECTS[paper]:
        chapter_no += 1
        slug = SLUGS[subject]
        ch = {
            "chapter_no": chapter_no,
            "paper": paper,
            "subject": subject,
            "display": DISPLAY[subject],
            "slug": slug,
            "src_file": f"ch{chapter_no:02d}_{slug}.html",
            "anchor": f"ch-{chapter_no}",
            "sections": [],
            "card_count": 0,
            "word_count": 0,
        }
        sec_groups = hier[paper][subject]
        for sec_name in sec_groups:  # keep v17 order
            section_no += 1
            sec = {
                "title": sec_name,
                "no": section_no,
                "anchor": f"sg-{section_no}",
                "subtopics": [],
                "card_count": 0,
                "word_count": 0,
            }
            for sub_name in sorted(sec_groups[sec_name].keys()):  # alphabetical within group
                ids = sec_groups[sec_name][sub_name]
                subtopic_no += 1
                wc = sum(int(cards_by_id[i].get("word_count", 0)) for i in ids)
                sub = {
                    "title": sub_name,
                    "no": subtopic_no,
                    "anchor": f"st-{subtopic_no}",
                    "card_ids": ids,
                    "card_count": len(ids),
                    "word_count": wc,
                }
                sec["subtopics"].append(sub)
                sec["card_count"] += len(ids)
                sec["word_count"] += wc
            ch["sections"].append(sec)
            ch["card_count"] += sec["card_count"]
            ch["word_count"] += sec["word_count"]
        part["chapters"].append(ch)
        part["card_count"] += ch["card_count"]
        part["word_count"] += ch["word_count"]
        chapters.append(ch)
    parts.append(part)

# --- sanity checks -----------------------------------------------------------
total_cards = sum(c["card_count"] for c in chapters)
total_sections = sum(len(c["sections"]) for c in chapters)
total_subtopics = sum(len(s["subtopics"]) for c in chapters for s in c["sections"])
assert total_cards == 551, f"card count mismatch: {total_cards}"
assert total_sections == 48, f"section count mismatch: {total_sections}"
assert total_subtopics == 209, f"subtopic mismatch: {total_subtopics}"

# --- sheet estimates ---------------------------------------------------------
# magazine sheet ≈ 420 body words (measured vs prototype density); +1 opener sheet
for c in chapters:
    c["est_sheets"] = 1 + max(1, round(c["word_count"] / 420))

book = {
    "generated": str(date.today()),
    "title": "PYQ Nano Analysis — GS Mains",
    "subtitle": "The Answer-Writing Playbook",
    "structure_rule": "Book → Front matter → Part(paper) → Chapter(subject) → Section(section_group) → Card-group(subtopic) → Cards",
    "parts": parts,
    "chapters_flat": [
        {
            "chapter_no": c["chapter_no"], "paper": c["paper"],
            "subject": c["subject"], "display": c["display"],
            "src_file": c["src_file"], "anchor": c["anchor"],
            "sections": [
                {"no": s["no"], "title": s["title"], "anchor": s["anchor"],
                 "subtopics": [{"no": t["no"], "title": t["title"],
                                "anchor": t["anchor"], "cards": t["card_ids"]}
                               for t in s["subtopics"]]}
                for s in c["sections"]
            ],
            "card_count": c["card_count"], "word_count": c["word_count"],
            "est_sheets": c["est_sheets"],
        }
        for c in chapters
    ],
    "totals": {
        "cards": total_cards, "chapters": len(chapters),
        "sections": total_sections, "subtopics": total_subtopics,
        "body_words": sum(c["word_count"] for c in chapters),
        "est_body_sheets": sum(c["est_sheets"] for c in chapters),
    },
}
OUT.write_text(json.dumps(book, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"OK — {total_cards} cards · {len(chapters)} chapters · {total_sections} sections · {total_subtopics} subtopics")
print(f"body words: {book['totals']['body_words']:,} · est body sheets: {book['totals']['est_body_sheets']}")
for c in chapters:
    print(f"  ch{c['chapter_no']:>2} {c['paper']} {c['display']:<28} {c['card_count']:>3} cards "
          f"{len(c['sections']):>2} sec {sum(len(s['subtopics']) for s in c['sections']):>3} sub "
          f"{c['word_count']:>6,} words ~{c['est_sheets']:>3} sheets → {c['src_file']}")
