#!/usr/bin/env python3
"""Phase 4c (v3, post-review round 2) — back matter: bm1_index + bm2_back_cover.

Index (v3):
  - 2-COLUMN layout (user-locked) to keep the index compact.
  - EVERY level clickable: paper → subject → section → SUBTOPIC (new, e.g.
    "Buddhism" now jumps to its band) → card title.
  - No card counts anywhere (no "N CARDS" badges).
  - Auto-paginated into true-A4 sheets by a height-budget model so each
    index page is one clean page (no runaway sheets).
  - Subtopic line style: "Buddhism — Title · Title" (subtopic name links to
    its band; titles link to their cards).
"""
import html
import json
import math
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MAP = json.loads((REPO / "scripts" / "stage2" / "book_map.json").read_text(encoding="utf-8"))
INV = json.loads((REPO / "scripts" / "stage2" / "v17_inventory.json").read_text(encoding="utf-8"))
SRC = REPO / "src"

TITLES = {c["id"]: c["card_title"] for c in INV["cards"]}
LOGO = "assets/images/logo_dr_cse.png"


def esc(t):
    return html.escape(t, quote=False)


THIN = ('  <div class="topbar">\n'
        f'    <div class="tb-brand"><img class="tb-logo" src="{LOGO}" alt="Dr. CSE"/>'
        '<span class="tb-name">Dr. CSE — <b>Replica</b></span></div>\n'
        '  </div>\n  <div class="rule"></div>')
FOOT = ('  <div class="foot"><span>DR. CSE — REPLICA · INTRO TO CONCLUSION</span>'
        '<span class="pg-n">·</span></div>')


# ---------------------------------------------------- height budget model ---
# one A4 sheet's 2-column body can hold ~2080px of stacked (1-col) content
# (calibrated by browser measurement: 1780 left sheets 15–40% empty)
BUDGET = 2080
H_CH = 36            # subject header row
H_SEC = 32           # section header row


def line_h(t):
    """Estimated px height of one subtopic line in a ~337px column."""
    n = len(t["title"]) + 3 + sum(len(TITLES.get(c, c)) + 4 for c in t["card_ids"])
    return max(1, math.ceil(n / 56)) * 16 + 6


def sec_block(s):
    rows = [f'    <div class="ix-sec"><a href="#{s["anchor"]}">{esc(s["title"])}</a></div>']
    h = H_SEC
    for t in s["subtopics"]:
        links = ' <span class="sep">·</span> '.join(
            f'<a href="#card-{cid}" title="{esc(TITLES.get(cid, cid))}">{esc(TITLES.get(cid, cid))}</a>'
            for cid in t["card_ids"])
        rows.append(f'    <div class="ix-line"><a class="st" href="#{t["anchor"]}">'
                    f'{esc(t["title"])}</a> — {links}</div>')
        h += line_h(t)
    return "\n".join(rows), h


def render_sheet(rows, meta, intro=""):
    """meta = (paper, subject, is_continuation)."""
    if meta and meta[0]:
        cont = " · CONTINUED" if meta[2] else ""
        lab = (f'\n  <div class="ix-hint">CONTENTS · {esc(meta[0])} · '
               f'{esc(meta[1].upper())}{cont}</div>')
    else:
        lab = ""
    return (f'<div class="sheet a4">\n{THIN}\n{intro}{lab}\n'
            f'  <div class="ix-body">\n' + "\n".join(rows) + f'\n  </div>\n{FOOT}\n</div>')


def bm1():
    # ---- atomic blocks: paper/subject headers ride with their first section ----
    atoms = []   # (html, height, paper, subject, starts_new_group)
    for p in MAP["parts"]:
        paper = p["paper"]
        ptag = paper.lower().replace("-", "")
        p_head = f'  <div class="ix-ch" id="ix-{ptag}"><a class="t" href="#pt-{ptag}">{paper}</a></div>'
        for i, ch in enumerate(p["chapters"]):
            ch_head = (f'  <div class="ix-ch"><a class="t" href="#ch-{ch["chapter_no"]}">'
                       f'{esc(ch["display"])}</a></div>')
            for j, s in enumerate(ch["sections"]):
                blk, h = sec_block(s)
                pre, ph, new_group = "", 0, False
                if j == 0:
                    pre += ch_head + "\n"
                    ph += H_CH
                    new_group = True
                if i == 0 and j == 0:
                    pre = p_head + "\n" + pre
                    ph += H_CH + 4
                atoms.append((pre + blk, ph + h, paper, ch["display"], new_group))

    # ---- pack into sheets by the height budget ----
    # sheet 1 also carries the full-width intro block (~300px) → lower budget
    INTRO_H = 300
    sheets, cur, cur_h = [], [], 0
    cur_meta, n_sheets = None, 0
    for blk, h, paper, subject, new_group in atoms:
        budget = BUDGET - (INTRO_H if n_sheets == 0 else 0)
        if cur and cur_h + h > budget:
            sheets.append(render_sheet(cur, cur_meta))
            cur, cur_h = [], 0
            n_sheets += 1
        if not cur:
            cur_meta = (paper, subject, not new_group)
        cur.append(blk)
        cur_h += h
    if cur:
        sheets.append(render_sheet(cur, cur_meta))

    # ---- first sheet: full-width intro rides ABOVE the 2-column body ----
    chips = " ".join(
        f'<a class="chip" href="#ix-{p["paper"].lower().replace("-", "")}">{p["paper"]}</a>'
        for p in MAP["parts"])
    intro = ('  <div class="lab" style="color:var(--gold)">CONTENTS · SUBJECT-WISE INDEX</div>\n'
             '  <h1 id="ix-master" style="font-size:30px">Every card, subject by subject</h1>\n'
             '  <p class="lede tight">Paper by paper, then subject, syllabus section, and subtopic.\n'
             '  Click a subject, a section, a subtopic, or any card title — <strong>every name below\n'
             '  is a link</strong>. On screen, the round INDEX button at the bottom-right corner\n'
             '  brings you back here from anywhere.</p>\n'
             f'  <div class="chips" style="margin-top:6px">{chips}</div>\n')
    sheets[0] = sheets[0].replace(
        '  <div class="ix-body">\n', intro + '  <div class="ix-body">\n', 1)
    return "\n".join(sheets)


def bm2():
    inner = f'''{THIN}
  <div style="padding:30px 0 0">
    <div class="lab" style="color:var(--gold)">CLOSING NOTE</div>
    <h1 style="font-size:34px">Now write.</h1>
    <p class="lede" style="font-size:13px">This deck holds verified answer units across four papers.
    Reading them is half the work. The other half is your pen, five days a week, against the clock.</p>
    <div class="verdict" style="margin:22px 0"><p>Open any card. Close the book. Write the answer.
    Repeat until the exam feels familiar.</p></div>
    <h2>Companion resources</h2>
    <figure class="fig" style="max-width:520px">
      <img src="assets/images/cover_candidate_resource_guide.png"
           alt="Dr. CSE ready-made resource guide — companion publications overview"
           loading="lazy">
      <figcaption>DR. CSE · READY-MADE RESOURCE GUIDE — COMPANION PUBLICATIONS</figcaption>
    </figure>
    <p class="small">More answer-writing material from the same desk — find it all at
    <a href="https://drcse.in" target="_blank" rel="noopener">drcse.in</a> and on Telegram at
    <a href="https://t.me/dr_cse" target="_blank" rel="noopener">t.me/dr_cse</a>.</p>
    <div style="margin-top:46px;padding-top:14px;border-top:1px solid var(--hair2)"
         class="small mono">REPLICA (EXAM REPLICABLE) · INTRO TO CONCLUSION · FIRST EDITION 2026<br/>
      A DR. CSE PUBLICATION · BUILT FROM THE VERIFIED CARD ARCHIVE · DESIGN: DR. CSE MAGAZINE STANDARD</div>
  </div>'''
    return f'<div class="sheet p1">\n{inner}\n</div>'


def main():
    idx = bm1()
    (SRC / "bm1_index.html").write_text(idx + "\n", encoding="utf-8")
    (SRC / "bm2_back_cover.html").write_text(bm2() + "\n", encoding="utf-8")
    print(f"wrote src/bm1_index.html ({idx.count('<div class="sheet')} sheets) · "
          f"src/bm2_back_cover.html")


if __name__ == "__main__":
    main()
