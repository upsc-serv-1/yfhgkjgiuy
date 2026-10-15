#!/usr/bin/env python3
"""Phase 4b (v2, post-review) — generate front matter + part openers.

Review decisions baked in:
  - NO count-analytics visuals (donut / stacked band / tier bars / dot rows /
    heatmaps). This is a ready-made card book: students jump to cards, they
    do not study card-count statistics.
  - fm4 "Book at a Glance" page REMOVED.
  - Part openers are navigation pages: part title + chapters + syllabus
    sections, all clickable.
  - The subject-wise master index (bm1) sits directly after How-to-Use.
All NEW editorial text follows the easy-language rules (12–20 word sentences,
everyday words, mentor tone).
"""
import html
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MAP = json.loads((REPO / "scripts" / "stage2" / "book_map.json").read_text(encoding="utf-8"))
SRC = REPO / "src"

PAPER_TITLES = {
    "GS-1": "Indian Heritage and Culture, History and Geography of the World and Society",
    "GS-2": "Governance, Constitution, Polity, Social Justice and International Relations",
    "GS-3": "Technology, Economic Development, Bio-diversity, Environment, Security and Disaster Management",
    "GS-4": "Ethics, Integrity and Aptitude",
}
PAPER_ROMAN = {"GS-1": "I", "GS-2": "II", "GS-3": "III", "GS-4": "IV"}
PAPER_LEDES = {
    "GS-1": "Ready cards for heritage, history, geography, and society. Open any section below and revise its cards in minutes.",
    "GS-2": "Ready cards for the Constitution, governance, social justice, and international relations. Click a section to start revising.",
    "GS-3": "Ready cards for economy, security, agriculture, science, environment, and disasters. Click a section to start revising.",
    "GS-4": "Ready cards for ethics, integrity, and aptitude — the largest part of this book. Use the mini-index below to jump to any theme.",
}


def esc(t):
    return html.escape(t, quote=False)


def topbar(crumb_left, crumb_right, stamp):
    return f'''  <div class="topbar">
    <div class="brand">PYQ Nano Analysis <span class="mono" style="font-size:9px;color:var(--mut)">GS MAINS</span></div>
    <div class="crumb">{crumb_left}{(' · ' + crumb_right) if crumb_right else ''}</div>
    <div class="stamp">{stamp}<br/><span class="pg-n">·</span></div>
  </div>
  <div class="rule"></div>'''


def foot():
    return ('  <div class="foot"><span>PYQ NANO ANALYSIS — GS MAINS · THE ANSWER-WRITING PLAYBOOK</span>'
            '<span class="pg-n">·</span></div>')


def sheet(inner, cls=""):
    c = f" {cls}" if cls else ""
    return f'<div class="sheet{c}">\n{inner}\n{foot()}\n</div>'


# ============================================================ fm1 cover =====
def fm1():
    t = MAP["totals"]
    inner = f'''  <div class="topbar" style="min-height:0">
    <div class="crumb">DR. CSE · GS MAINS ANSWER-WRITING SERIES</div>
    <div class="stamp">FIRST EDITION<br/>2026</div>
  </div>
  <div class="rule"></div>
  <div style="padding:110px 0 0">
    <div class="lab" style="color:var(--gold)">THE ANSWER-WRITING PLAYBOOK</div>
    <h1 id="fm-cover" style="font-size:56px;letter-spacing:-1.5px">PYQ Nano<br/>Analysis</h1>
    <p class="lede" style="font-size:14px;margin-top:14px">GS Mains · Papers I–IV · {t["cards"]} ready answer cards,
    built from previous-year questions and arranged the way the syllabus is examined.</p>
    <div class="chips" style="margin-top:18px">
      <a class="chip" href="#ix-master">CONTENTS — CLICK ANY CARD TITLE TO JUMP TO IT</a>
      <a class="chip" href="#fm-howto">HOW TO USE THIS BOOK</a>
    </div>
  </div>
  <div class="cover-stat">
    <div><div class="v">{t["cards"]}</div><div class="k">Answer cards</div></div>
    <div><div class="v">4</div><div class="k">GS papers</div></div>
    <div><div class="v">{t["chapters"]}</div><div class="k">Subjects</div></div>
    <div><div class="v">{t["subtopics"]}</div><div class="k">Subtopics</div></div>
    <div><div class="v">{t["sections"]}</div><div class="k">Syllabus sections</div></div>
  </div>
  <p class="small" style="margin-top:26px">Every card carries a quote where one exists, a crisp introduction,
  examples, data points, and a conclusion you can lift into an answer. The subject-wise index lists all
  {t["cards"]} card titles — every one of them is a clickable link.</p>'''
    return sheet(inner, cls="p1")


# ========================================================== fm2 foreword ====
def fm2():
    inner = f'''{topbar('<a href="#ix-master">CONTENTS</a>', "Foreword", "FOREWORD")}
  <div class="lab" style="color:var(--gold)">FOREWORD</div>
  <h1 id="fm-foreword">Why this book exists</h1>
  <p class="lede">Mains is not a knowledge test. It is a recall-and-writing test under a strict clock.
  This book turns previous-year questions into small answer units you can revise fast.</p>
  <p>Most aspirants already own thick books. The problem is not material. The problem is shape:
  a 600-page book cannot be revised in the last thirty days. So we cut each topic into
  <strong>nano cards</strong>. Each card answers one examinable idea. Each carries a quotable line,
  a two-line introduction, ready examples, safe data, and a closing sentence.</p>
  <p>The {MAP["totals"]["cards"]} cards in this edition were selected and polished from the full PYQ
  archive of GS Papers I to IV. We kept only what the exam rewards. Every quote, number, name, and
  judgment is kept exactly as verified. Nothing you read here is paraphrased theory.</p>
  <div class="verdict"><p>Read a card, close the book, and write one answer paragraph from memory.
  That one habit is worth more than any new material.</p></div>
  <p>Open the subject-wise index on the next pages and click any card title to reach it directly.
  Then trust the cards, and trust your practice.</p>
  <p class="small" style="margin-top:22px;letter-spacing:1px">— THE MENTOR DESK · DR. CSE</p>'''
    return sheet(inner)


# ======================================================== fm3 how-to-use ====
def fm3():
    t = MAP["totals"]
    routes = f'''  <h2>Three reading routes</h2>
  <p class="lede tight">Pick one route and finish it before the exam. Each route reads the same cards —
  only the order and the daily load change.</p>
  <table style="font-size:11px;line-height:1.55;margin:10px 0 6px">
    <thead><tr>
      <th style="text-align:left;padding:5px 8px;border-bottom:1px solid var(--hair2);font-family:var(--mono);font-weight:500;font-size:9px;letter-spacing:1px;color:var(--mut)">ROUTE</th>
      <th style="text-align:left;padding:5px 8px;border-bottom:1px solid var(--hair2);font-family:var(--mono);font-weight:500;font-size:9px;letter-spacing:1px;color:var(--mut)">WHO IT SUITS</th>
      <th style="text-align:left;padding:5px 8px;border-bottom:1px solid var(--hair2);font-family:var(--mono);font-weight:500;font-size:9px;letter-spacing:1px;color:var(--mut)">PLAN</th>
    </tr></thead>
    <tbody>
      <tr><td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top"><strong>30 days · Sprint</strong></td>
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">Mains is close and you have read the syllabus once.</td>
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">Read the biggest subtopics of every subject first — roughly 180 cards — at 6 cards a day. Revise each day's cards next morning.</td></tr>
      <tr><td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top"><strong>60 days · Steady</strong></td>
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">You want full coverage of the two big papers first.</td>
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">Finish GS-2 and GS-4 (265 cards) in the first 25 days. Then read GS-1 and GS-3 in the next 30 days. Keep the last 5 days for the index run.</td></tr>
      <tr><td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top"><strong>90 days · Foundation</strong></td>
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">This is your first full Mains cycle.</td>
          <td style="padding:6px 8px;vertical-align:top">Read the whole book paper by paper, 6 to 7 cards a day. Write one full answer for every ten cards. Use Sundays to re-read the quotes.</td></tr>
    </tbody>
  </table>'''
    inner = f'''{topbar('<a href="#ix-master">CONTENTS</a>', "How to Use", "HOW TO USE")}
  <div class="lab" style="color:var(--gold)">HOW TO USE THIS BOOK</div>
  <h1 id="fm-howto">Read cards, not chapters</h1>
  <p class="lede">This book is a deck of {t["cards"]} answer cards. Each card is self-contained.
  You can open any page and revise for five useful minutes.</p>

  <h2>How one card is built</h2>
  <p class="lede tight">Every card sits in its own white rounded box, with its paper's colour on the
  top edge. Inside, each part of the answer carries a clear label:</p>
  <div class="card gs1" style="margin-top:8px">
    <div class="card-h"><div style="font-family:var(--serif);font-weight:600;font-size:16px;line-height:1.25;color:var(--ink-h)">Card title</div><span class="card-id">GS1-HIST-0001</span></div>
    <div class="pull"><div class="blk-lab">Quote</div>
      <p>A verified quotable line with its attribution, on a soft gold panel. One such line per answer earns marks safely.</p></div>
    <div class="intro"><div class="blk-lab">Introduction</div>
      <p>A two-to-three line opening you can lift straight into an answer.</p></div>
    <div class="ex"><div class="blk-lab">Examples</div>
      <p>Ready evidence: schemes, cases, judgments, committees, and reports.</p></div>
    <div class="data"><div class="blk-lab">Data</div>
      <p>Safe figures and dates on a teal-ruled mono panel.</p></div>
    <div class="conc"><div class="blk-lab">Conclusion</div>
      <p>A closing sentence with a forward look — the safest way to end an answer.</p></div>
  </div>
  <p class="small">Cards may also carry <strong>detail</strong> panels (gold label, extra depth) and
  <strong>images</strong> where a diagram helps. The mono ID on every card is a stable handle —
  search it with Ctrl+F.</p>

  <h2>How to reach any card</h2>
  <div class="note" style="margin-top:6px">
    <strong>1 · Subject-wise index.</strong> The pages right after this one list all {t["cards"]} card titles,
    grouped paper by paper, then subject, section, and subtopic. <a href="#ix-master">Click any title to jump
    straight to its card</a>.</div>
  <div class="note"><strong>2 · The INDEX button.</strong> On screen, a round INDEX button stays at the
  bottom-right corner of every page. One click brings you back to the index from anywhere in the book.</div>
  <div class="note"><strong>3 · Breadcrumbs.</strong> Every page carries a trail at the top — paper, subject,
  section. Click any step to jump back, or search a card ID with Ctrl+F.</div>

{routes}

  <div class="take" style="margin-top:14px"><strong>One habit.</strong> After every ten cards, close the book and
  write two answer paragraphs from memory. The routes above only work if this habit stays.</div>'''
    return sheet(inner)


# ====================================================== part openers =========
def part_opener(p):
    paper = p["paper"]
    roman = PAPER_ROMAN[paper]
    anchor = f"pt-{paper.lower().replace('-', '')}"
    ch_list = "\n".join(
        f'<a class="chip" href="#ch-{ch["chapter_no"]}">CHAPTER {ch["chapter_no"]:02d} · '
        f'{esc(ch["display"].upper())} · {ch["card_count"]} CARDS</a>'
        for ch in p["chapters"]
    )
    # per-chapter syllabus-section link lists (navigation, not analytics)
    sec_blocks = []
    for ch in p["chapters"]:
        links = " ".join(
            f'<a href="#{s["anchor"]}" title="{s["card_count"]} cards">{esc(s["title"])}</a>'
            for s in ch["sections"]
        )
        sec_blocks.append(
            f'<div style="margin:0 0 12px">\n'
            f'  <div class="ix-ch" style="margin:10px 0 2px">'
            f'<a class="t" href="#ch-{ch["chapter_no"]}">{esc(ch["display"])}</a>'
            f'<span class="n">{ch["card_count"]} CARDS · {len(ch["sections"])} SECTIONS</span></div>\n'
            f'  <div class="ix-cards" style="margin-bottom:2px">{links}</div>\n'
            f'</div>'
        )
    # GS-4 keeps its theme mini-index (it is 149 cards — pure navigation aid)
    mini_index = ""
    if paper == "GS-4":
        rows = []
        for ch in p["chapters"]:
            for s in ch["sections"]:
                subs = " · ".join(
                    f'<a href="#{t["anchor"]}" style="color:var(--ink);text-decoration:none;'
                    f'border-bottom:1px dotted var(--hair2)">{esc(t["title"])}</a>'
                    f'<span class="mono" style="font-size:8.5px;color:var(--mut)"> {t["card_count"]}</span>'
                    for t in s["subtopics"]
                )
                rows.append(
                    f'<div style="margin:8px 0"><div style="font-size:10px;letter-spacing:1px;'
                    f'color:var(--gold);margin-bottom:2px">{esc(s["title"].upper())} · {s["card_count"]} CARDS</div>'
                    f'<div style="font-size:10.5px;line-height:1.8">{subs}</div></div>'
                )
        mini_index = f'''
  <h2 id="gs4-mini-index">GS-4 mini-index</h2>
  <p class="lede tight">All {p['card_count']} ethics cards by syllabus section. Use this to jump
  straight to a theme during revision.</p>
  {"".join(rows)}'''
    inner = f'''{topbar('<a href="#ix-master">CONTENTS</a>', f"PAPER {paper}", f"PART {roman} OF IV")}
  <div style="margin-top:4px">
    <span class="gschip">{paper}</span>
    <div class="hero-tag" style="margin-top:10px">PART {roman} OF IV · {p['card_count']} CARDS · {len(p['chapters'])} SUBJECTS</div>
    <h1 id="{anchor}" style="font-size:34px;max-width:660px">{PAPER_TITLES[paper]}</h1>
    <p class="lede tight">{PAPER_LEDES[paper]}</p>
  </div>
  <h2 style="margin-top:8px">Chapters in this part</h2>
  <div class="chips">{ch_list}</div>
  <h2>Syllabus sections — click to jump</h2>
  {"".join(sec_blocks)}{mini_index}'''
    return sheet(inner)


# ==================================================================== main ==
def main():
    files = {
        "fm1_cover.html": fm1(),
        "fm2_foreword.html": fm2(),
        "fm3_how_to_use.html": fm3(),
        "pt1_gs1_opener.html": part_opener(MAP["parts"][0]),
        "pt2_gs2_opener.html": part_opener(MAP["parts"][1]),
        "pt3_gs3_opener.html": part_opener(MAP["parts"][2]),
        "pt4_gs4_opener.html": part_opener(MAP["parts"][3]),
    }
    for name, content in files.items():
        (SRC / name).write_text(content + "\n", encoding="utf-8")
        print(f"wrote src/{name}: {len(content):,} bytes")
    print("front matter + part openers done (no analytics, fm4 removed)")


if __name__ == "__main__":
    main()
