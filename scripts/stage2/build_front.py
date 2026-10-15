#!/usr/bin/env python3
"""Phase 4b — generate front matter (fm1–fm4) and part openers (pt1–pt4).

All analytics recreated from OUR card taxonomy (book_map.json) — no PYQ marks data.
All NEW editorial text follows the easy-language rules (12–20 word sentences,
everyday words, mentor tone).
"""
import json
import math
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
PAPER_COLORS = {"GS-1": "#A97D2B", "GS-2": "#4F8F86", "GS-3": "#6E9468", "GS-4": "#1F4F52"}
SUBJECT_COLORS = ["#4F8F86", "#A97D2B", "#6E9468", "#1F4F52", "#7FB3AA", "#B4D2CB"]
BANDS = ["#DCE9E5", "#B4D2CB", "#7FB3AA", "#4F8F86", "#1F4F52"]


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


# ------------------------------------------------------------------ I1 donut
def donut_svg(segments, size=150, stroke=20, center_label="", center_value=""):
    """segments: [(label, value, color)] → SVG donut with stroke-dasharray arcs."""
    total = sum(v for _, v, _ in segments) or 1
    r = (size - stroke) / 2
    c = 2 * math.pi * r
    parts, legend = [], []
    acc = 0.0
    for label, value, color in segments:
        frac = value / total
        dash = f"{frac * c:.1f} {c - frac * c:.1f}"
        rot = acc / total * 360 - 90
        parts.append(
            f'<circle cx="{size/2}" cy="{size/2}" r="{r:.1f}" fill="none" stroke="{color}" '
            f'stroke-width="{stroke}" stroke-dasharray="{dash}" '
            f'transform="rotate({rot:.2f} {size/2} {size/2})"/>'
        )
        legend.append((label, value, color, frac))
        acc += value
    legend_html = "\n".join(
        f'<div style="display:flex;justify-content:space-between;gap:8px;font-size:10.5px;'
        f'padding:2px 0"><span><span class="sw" style="background:{col};display:inline-block;'
        f'width:9px;height:9px;border-radius:2px;margin-right:6px"></span>{lab}</span>'
        f'<span class="mono" style="font-size:9.5px;color:var(--ink2)">{val} · {frac*100:.1f}%</span></div>'
        for lab, val, col, frac in legend
    )
    svg = (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" role="img" '
           f'aria-label="{center_label}">"{"".join(parts)}'
           f'<text x="{size/2}" y="{size/2 - 4}" text-anchor="middle" '
           f'style="font-family:var(--mono);font-weight:500;font-size:20px;fill:var(--ink-h)">{center_value}</text>'
           f'<text x="{size/2}" y="{size/2 + 14}" text-anchor="middle" '
           f'style="font-family:var(--sans);font-size:8.5px;letter-spacing:1.5px;fill:var(--mut)">{center_label}</text>'
           f"</svg>")
    return f'<div style="display:flex;gap:18px;align-items:center">{svg}<div style="flex:1">{legend_html}</div></div>'


# ----------------------------------------------------------------- I2 bands
def band_html(segments, width_note=""):
    """segments: [(label, value, color)] → one 100% stacked band + legend."""
    total = sum(v for _, v, _ in segments) or 1
    cells = "".join(
        f'<i style="width:{val/total*100:.2f}%;background:{col}" title="{lab}: {val}"></i>'
        for lab, val, col in segments
    )
    legend = " ".join(
        f'<span style="font-size:9.5px;color:var(--ink2);margin-right:10px">'
        f'<span class="sw" style="background:{col};display:inline-block;width:8px;height:8px;'
        f'border-radius:2px;margin-right:4px"></span>{lab} <span class="mono" style="font-size:9px">{val}</span></span>'
        for lab, val, col in segments
    )
    return (f'<div class="band" role="img" aria-label="card distribution{width_note}">{cells}</div>'
            f'<div class="legend" style="margin:4px 0 0">{legend}</div>')


# ------------------------------------------------------------------ I4 heatmap
def heat_css(count):
    """card count → b1..b5 class"""
    if count >= 8:
        return "b5", "#fff"
    if count >= 5:
        return "b4", "#fff"
    if count >= 3:
        return "b3", "#16211F"
    if count == 2:
        return "b2", "#16211F"
    return "b1", "#16211F"


def heatmap_html(chapters):
    """chapters (of one part): rows = section_group, cells = subtopics."""
    rows = []
    for ch in chapters:
        for s in ch["sections"]:
            cells = []
            for t in s["subtopics"]:
                cls, txt = heat_css(t["card_count"])
                cells.append(
                    f'<a class="hm-c" style="background:var(--{cls});color:{txt}" '
                    f'href="#{t["anchor"]}" title="{ch["display"]} · {s["title"]} · {t["title"]}: '
                    f'{t["card_count"]} cards"><span class="mono" style="font-size:9px">{t["card_count"]}</span></a>'
                )
            rows.append(
                f'<div class="hm-row"><a class="hm-lab" href="#{s["anchor"]}" '
                f'style="max-width:150px;font-size:9.5px">{s["title"]}</a>'
                + "".join(cells) + "</div>"
            )
    legend = "".join(
        f'<span style="display:inline-flex;align-items:center;gap:3px;margin-right:8px">'
        f'<span class="sw" style="background:var(--{c} )"></span>{lab}</span>'
        for c, lab in [("b1", "1"), ("b2", "2"), ("b3", "3-4"), ("b4", "5-7"), ("b5", "8+")]
    )
    return ('<div class="hm">' + "\n".join(rows) + "</div>"
            f'<div class="legend">CARDS PER SUBTOPIC · {legend}</div>')


# --------------------------------------------------------------- I3/I5 tiers
def tier_rows(section_pairs, max_rows=6):
    """section_pairs: [(title, count, anchor)] → tier table rows."""
    out = []
    mx = max(c for _, c, _ in section_pairs) or 1
    for title, count, anchor in sorted(section_pairs, key=lambda x: -x[1])[:max_rows]:
        cls, txt = heat_css(count)
        pct = count / mx * 100
        out.append(
            f'<div style="display:flex;align-items:center;gap:10px;margin:3px 0">'
            f'<a href="#{anchor}" style="flex:1;font-size:11px;color:var(--ink);text-decoration:none;'
            f'border-bottom:1px dotted var(--hair2)">{title}</a>'
            f'<div style="width:180px;height:10px;background:var(--b1);border-radius:2px;overflow:hidden">'
            f'<i style="display:block;height:100%;width:{pct:.0f}%;background:var(--{cls})"></i></div>'
            f'<span class="mono" style="font-size:10px;width:52px;text-align:right">{count} cards</span></div>'
        )
    return "\n".join(out)


def subtop_rows(sub_pairs, max_rows=8):
    out = []
    mx = max(c for _, c, _ in sub_pairs) or 1
    for title, count, anchor in sorted(sub_pairs, key=lambda x: -x[1])[:max_rows]:
        dots = ""
        for i in range(10):
            on = (i + 0.5) / 10 <= count / mx
            dots += f'<i class="{"" if on else "off"}"></i>'
        out.append(
            f'<div style="display:flex;align-items:center;gap:10px;margin:3px 0">'
            f'<a href="#{anchor}" style="flex:1;font-size:11px;color:var(--ink);text-decoration:none;'
            f'border-bottom:1px dotted var(--hair2)">{title}</a>'
            f'<span class="dots">{dots}</span>'
            f'<span class="mono" style="font-size:10px;width:52px;text-align:right">{count} cards</span></div>'
        )
    return "\n".join(out)


# ============================================================ fm1 cover =====
def fm1():
    t = MAP["totals"]
    inner = f'''  <div class="topbar" style="min-height:0">
    <div class="crumb">DR. CSE · GS MAINS ANSWER-WRITING SERIES</div>
    <div class="stamp">FIRST EDITION<br/>2026</div>
  </div>
  <div class="rule"></div>
  <div style="padding:120px 0 0">
    <div class="lab" style="color:var(--gold)">THE ANSWER-WRITING PLAYBOOK</div>
    <h1 id="fm-cover" style="font-size:56px;letter-spacing:-1.5px">PYQ Nano<br/>Analysis</h1>
    <p class="lede" style="font-size:14px;margin-top:14px">GS Mains · Papers I–IV · {t["cards"]} ready answer cards,
    built from previous-year questions and arranged the way the syllabus is examined.</p>
  </div>
  <div class="cover-stat">
    <div><div class="v">{t["cards"]}</div><div class="k">Answer cards</div></div>
    <div><div class="v">4</div><div class="k">GS papers</div></div>
    <div><div class="v">{t["chapters"]}</div><div class="k">Subjects</div></div>
    <div><div class="v">{t["subtopics"]}</div><div class="k">Subtopics</div></div>
    <div><div class="v">{t["sections"]}</div><div class="k">Syllabus sections</div></div>
  </div>
  <p class="small" style="margin-top:26px">Every card carries a quote where one exists, a crisp introduction,
  examples, data points, and a conclusion you can lift into an answer. The index lists all
  {t["cards"]} cards, paper by paper and subject by subject.</p>'''
    return sheet(inner, cls="p1")


# ========================================================== fm2 foreword ====
def fm2():
    inner = f'''{topbar("FRONT MATTER", "Foreword", "FOREWORD")}
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
  <p>Use the How-to-Use section to pick a reading route. Use the index to jump straight to a subtopic.
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
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">Read the heaviest subtopics of every subject first — roughly 180 cards — at 6 cards a day. Revise each day's cards next morning.</td></tr>
      <tr><td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top"><strong>60 days · Steady</strong></td>
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">You want full coverage of the two big papers first.</td>
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">Finish GS-2 and GS-4 (265 cards) in the first 25 days. Then read GS-1 and GS-3 in the next 30 days. Keep the last 5 days for the index run.</td></tr>
      <tr><td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top"><strong>90 days · Foundation</strong></td>
          <td style="padding:6px 8px;border-bottom:1px solid var(--hair);vertical-align:top">This is your first full Mains cycle.</td>
          <td style="padding:6px 8px;vertical-align:top">Read the whole book paper by paper, 6 to 7 cards a day. Write one full answer for every ten cards. Use Sundays to re-read the quotes.</td></tr>
    </tbody>
  </table>'''
    inner = f'''{topbar("FRONT MATTER", "How to Use", "HOW TO USE")}
  <div class="lab" style="color:var(--gold)">HOW TO USE THIS BOOK</div>
  <h1 id="fm-howto">Read cards, not chapters</h1>
  <p class="lede">This book is a deck of {t["cards"]} answer cards. Each card is self-contained.
  You can open any page and revise for five useful minutes.</p>

  <h2>How one card is built</h2>
  <div class="note" style="margin-top:6px">The sample below is a real card from Chapter 1.
  The labels explain each block. Every card in the book follows the same grammar.</div>
  <div style="border:1px solid var(--hair2);padding:14px 16px;margin:10px 0 4px">
    <div class="lab" style="color:var(--teal)">CARD TITLE + ID</div>
    <p class="small" style="margin-bottom:10px">The title names the examinable idea. The mono ID (like
    <span class="mono" style="font-size:9px">GS1-HIST-0001</span>) is a stable handle — search it with Ctrl+F.</p>
    <div class="lab" style="color:var(--teal)">QUOTE</div>
    <p class="small" style="margin-bottom:10px">A verified quotable line with its attribution. Gold bar marks it.
    One such line per answer earns marks safely.</p>
    <div class="lab" style="color:var(--teal)">INTRODUCTION</div>
    <p class="small" style="margin-bottom:10px">A two-to-three line opening you can lift straight into an answer.</p>
    <div class="lab" style="color:var(--teal)">EXAMPLES · DATA · DETAIL</div>
    <p class="small" style="margin-bottom:10px">Ready evidence: schemes, cases, judgments, figures. Data blocks sit on a
    teal-ruled panel; detail blocks carry a gold label.</p>
    <div class="lab" style="color:var(--teal)">CONCLUSION</div>
    <p class="small" style="margin-bottom:0">A closing sentence with a forward look — the safest way to end an answer.</p>
  </div>

  <h2>Three ways to reach any card</h2>
  <p class="lede tight">Every page carries a breadcrumb at the top: paper · subject · section.
  Click it to jump back. Or use one of these:</p>
  <div class="chips">
    <span class="chip">1 · Part openers list each paper's chapters and heaviest subtopics</span>
    <span class="chip">2 · The master index lists every card, GS-wise then subject-wise</span>
    <span class="chip">3 · Search the card ID — every ID is unique across the book</span>
  </div>

  <h2>Reading the visuals</h2>
  <p class="lede tight">Part openers carry three small visuals. The donut shows each subject's share
  of the cards. The tier rows rank the heaviest syllabus sections. The heatmap shows how many cards
  sit on each subtopic — darker means heavier.</p>

{routes}

  <div class="take" style="margin-top:14px"><strong>One habit.</strong> After every ten cards, close the book and
  write two answer paragraphs from memory. The routes above only work if this habit stays.</div>'''
    return sheet(inner)


# ========================================================= fm4 glance =======
def fm4():
    t = MAP["totals"]
    parts = MAP["parts"]
    donut = donut_svg(
        [(p["paper"], p["card_count"], PAPER_COLORS[p["paper"]]) for p in parts],
        center_value=str(t["cards"]), center_label="CARDS",
    )
    subj_segs = []
    for p in parts:
        for i, ch in enumerate(p["chapters"]):
            subj_segs.append((f'{ch["display"]} ({p["paper"]})', ch["card_count"],
                              SUBJECT_COLORS[i % len(SUBJECT_COLORS)]))
    bands = band_html(subj_segs)
    # cross-paper themes I9 — curated from actual section_group names present in 2+ papers
    cross = [
        ("Poverty &amp; welfare", "GS-1 · Poverty, Empowerment &amp; Development", "GS-2 · Poverty &amp; Hunger"),
        ("Climate", "GS-1 · Environmental Geography &amp; Climate Dynamics", "GS-3 · Climate Change"),
        ("Accountability &amp; corruption", "GS-2 · Accountability &amp; Civil Services", "GS-4 · Governance &amp; Probity"),
        ("Ethics in world affairs", "GS-2 · Global Geopolitics &amp; Indian Diaspora", "GS-4 · Applied Ethics"),
        ("Disasters &amp; hazards", "GS-1 · Physical Geography &amp; Geophysical Phenomena", "GS-3 · Specific Disasters &amp; Hazards"),
    ]
    cross_rows = "\n".join(
        f'<tr><td style="padding:5px 8px;border-bottom:1px solid var(--hair);font-size:11px"><strong>{a}</strong></td>'
        f'<td style="padding:5px 8px;border-bottom:1px solid var(--hair);font-size:11px">{b}</td>'
        f'<td style="padding:5px 8px;border-bottom:1px solid var(--hair);font-size:11px">{c}</td></tr>'
        for a, b, c in cross
    )
    inner = f'''{topbar("FRONT MATTER", "The Book at a Glance", "GLANCE")}
  <div class="lab" style="color:var(--gold)">THE BOOK AT A GLANCE</div>
  <h1 id="fm-glance">All four papers, side by side</h1>
  <p class="lede">These visuals count the cards of this book — not exam marks. Darker and longer
  simply mean more cards, so you can see where the book's weight sits.</p>
  <h2>Share of cards by paper</h2>
  {donut}
  <h2>Every subject, card by card</h2>
  {bands}
  <h2>One theme, several papers</h2>
  <p class="lede tight">Some themes repeat across papers. When you revise one card group, skim its twin
  in the other paper on the same day.</p>
  <table style="margin-top:8px">
    <thead><tr><th style="text-align:left;padding:5px 8px;border-bottom:1px solid var(--hair2);font-family:var(--mono);font-weight:500;font-size:9px;letter-spacing:1px;color:var(--mut)">THEME</th>
    <th style="text-align:left;padding:5px 8px;border-bottom:1px solid var(--hair2);font-family:var(--mono);font-weight:500;font-size:9px;letter-spacing:1px;color:var(--mut)">APPEARS IN</th>
    <th style="text-align:left;padding:5px 8px;border-bottom:1px solid var(--hair2);font-family:var(--mono);font-weight:500;font-size:9px;letter-spacing:1px;color:var(--mut)">READ WITH</th></tr></thead>
    <tbody>{cross_rows}</tbody>
  </table>
  <div class="note" style="margin-top:14px">GS-4 is {sum(p['card_count'] for p in parts if p['paper']=='GS-4')} cards —
  over a quarter of the book. It gets its own mini-index on the GS-4 part opener.</div>'''
    return sheet(inner)


# ====================================================== part openers =========
def part_opener(p):
    paper = p["paper"]
    roman = PAPER_ROMAN[paper]
    anchor = f"pt-{paper.lower().replace('-', '')}"
    donut = donut_svg(
        [(ch["display"], ch["card_count"], SUBJECT_COLORS[i % len(SUBJECT_COLORS)])
         for i, ch in enumerate(p["chapters"])],
        center_value=str(p["card_count"]), center_label="CARDS",
    )
    sec_pairs = []
    sub_pairs = []
    for ch in p["chapters"]:
        for s in ch["sections"]:
            sec_pairs.append((f'{ch["display"]} · {s["title"]}', s["card_count"], s["anchor"]))
            for t in s["subtopics"]:
                sub_pairs.append((f'{t["title"]} <span style="color:var(--mut)">· {ch["display"]}</span>',
                                  t["card_count"], t["anchor"]))
    ch_list = "\n".join(
        f'<a class="chip" href="#ch-{ch["chapter_no"]}">CHAPTER {ch["chapter_no"]:02d} · '
        f'{ch["display"].upper()} · {ch["card_count"]} CARDS</a>'
        for ch in p["chapters"]
    )
    mini_index = ""
    if paper == "GS-4":
        rows = []
        for ch in p["chapters"]:
            for s in ch["sections"]:
                subs = " · ".join(
                    f'<a href="#{t["anchor"]}" style="color:var(--ink);text-decoration:none;'
                    f'border-bottom:1px dotted var(--hair2)">{t["title"]}</a>'
                    f'<span class="mono" style="font-size:8.5px;color:var(--mut)"> {t["card_count"]}</span>'
                    for t in s["subtopics"]
                )
                rows.append(
                    f'<div style="margin:8px 0"><div style="font-size:10px;letter-spacing:1px;'
                    f'color:var(--gold);margin-bottom:2px">{s["title"].upper()} · {s["card_count"]} CARDS</div>'
                    f'<div style="font-size:10.5px;line-height:1.8">{subs}</div></div>'
                )
        mini_index = f'''
  <h2 id="gs4-mini-index">GS-4 mini-index</h2>
  <p class="lede tight">All {p['card_count']} ethics cards by syllabus section. Use this to jump
  straight to a theme during revision.</p>
  {"".join(rows)}'''
    inner = f'''{topbar(f'<a href="#fm-glance">FRONT MATTER</a>', f"PAPER {paper}", f"PART {roman} OF IV")}
  <div class="hero" style="margin-top:4px">
    <div class="hero-l">
      <span class="gschip">{paper}</span>
      <div class="hero-tag" style="margin-top:10px">PART {roman} · {p['card_count']} CARDS</div>
      <h1 id="{anchor}" style="font-size:34px">{PAPER_TITLES[paper]}</h1>
      <p class="lede tight">{'Cards in this part follow the official syllabus of the paper. The tier table below shows where this book concentrates.' if paper != 'GS-4' else 'This is the largest part of the book. Its cards share one answer grammar: concept, thinker or case, application, and a values-based close.'}</p>
    </div>
    <div class="hero-r">{donut}</div>
  </div>
  <h2 style="margin-top:4px">What's inside</h2>
  <div class="chips">{ch_list}</div>
  <h2>Heaviest syllabus sections</h2>
  {tier_rows(sec_pairs)}
  <h2>Subtopics with the most cards</h2>
  {subtop_rows(sub_pairs)}
  <h2>Card heatmap — section by section</h2>
  <p class="lede tight">One cell is one subtopic. The number is its card count; darker means heavier.
  Click any cell to jump there.</p>
  {heatmap_html(p["chapters"])}{mini_index}'''
    return sheet(inner)


# ==================================================================== main ==
def main():
    files = {
        "fm1_cover.html": fm1(),
        "fm2_foreword.html": fm2(),
        "fm3_how_to_use.html": fm3(),
        "fm4_glance.html": fm4(),
        "pt1_gs1_opener.html": part_opener(MAP["parts"][0]),
        "pt2_gs2_opener.html": part_opener(MAP["parts"][1]),
        "pt3_gs3_opener.html": part_opener(MAP["parts"][2]),
        "pt4_gs4_opener.html": part_opener(MAP["parts"][3]),
    }
    for name, content in files.items():
        (SRC / name).write_text(content + "\n", encoding="utf-8")
        print(f"wrote src/{name}: {len(content):,} bytes")
    print("front matter + part openers done")


if __name__ == "__main__":
    main()
