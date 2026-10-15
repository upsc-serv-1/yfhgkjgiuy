#!/usr/bin/env python3
"""Phase 4c — generate back matter: bm1_index.html (master index) + bm2_back_cover.html.

Index structure (user-locked): GS-wise (GS-1→GS-4) → subject → section_group →
subtopic → card links. Card titles from the verbatim v17 inventory.
"""
import html
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MAP = json.loads((REPO / "scripts" / "stage2" / "book_map.json").read_text(encoding="utf-8"))
INV = json.loads((REPO / "scripts" / "stage2" / "v17_inventory.json").read_text(encoding="utf-8"))
SRC = REPO / "src"

TITLES = {c["id"]: c["card_title"] for c in INV["cards"]}
ROMAN = {"GS-1": "I", "GS-2": "II", "GS-3": "III", "GS-4": "IV"}


def esc(t):
    return html.escape(t, quote=False)


def topbar(crumb_right, stamp):
    return f'''  <div class="topbar">
    <div class="brand">PYQ Nano Analysis <span class="mono" style="font-size:9px;color:var(--mut)">GS MAINS</span></div>
    <div class="crumb">BACK MATTER · {crumb_right}</div>
    <div class="stamp">{stamp}<br/><span class="pg-n">·</span></div>
  </div>
  <div class="rule"></div>'''


def foot():
    return ('  <div class="foot"><span>PYQ NANO ANALYSIS — GS MAINS · THE ANSWER-WRITING PLAYBOOK</span>'
            '<span class="pg-n">·</span></div>')


def bm1():
    t = MAP["totals"]
    # index pages: one sheet per part (+ a lead sheet)
    sheets = []
    lead = f'''{topbar("Master Index", "INDEX")}
  <div class="lab" style="color:var(--gold)">MASTER INDEX</div>
  <h1 id="ix-master">Every card, in syllabus order</h1>
  <p class="lede">The index follows the book's taxonomy: paper → subject → syllabus section →
  subtopic → cards. All {t["cards"]} cards are reachable from the four pages that follow.</p>
  <div class="chips">
    <a class="chip" href="#ix-gs1">GS-1 · {sum(p['card_count'] for p in MAP['parts'] if p['paper']=='GS-1')} cards</a>
    <a class="chip" href="#ix-gs2">GS-2 · {sum(p['card_count'] for p in MAP['parts'] if p['paper']=='GS-2')} cards</a>
    <a class="chip" href="#ix-gs3">GS-3 · {sum(p['card_count'] for p in MAP['parts'] if p['paper']=='GS-3')} cards</a>
    <a class="chip" href="#ix-gs4">GS-4 · {sum(p['card_count'] for p in MAP['parts'] if p['paper']=='GS-4')} cards</a>
  </div>
  <h2>Card ID quick reference</h2>
  <p class="lede tight">IDs follow <span class="mono" style="font-size:10px">GS&lt;paper&gt;-&lt;SUBJ&gt;-&lt;NNNN&gt;</span> —
  for example <span class="mono" style="font-size:10px">GS1-HIST-0001</span> is the first History card of GS-1.
  Search any ID with Ctrl+F to reach its card directly.</p>'''
    sheets.append(lead)

    for p in MAP["parts"]:
        paper = p["paper"]
        rows = [f'{topbar(f"Master Index · {paper}", f"INDEX · PART {ROMAN[paper]}")}']
        rows.append(f'  <div class="ix-ch" id="ix-{paper.lower().replace("-", "")}">')
        rows.append(f'    <a class="t" href="#pt-{paper.lower().replace("-", "")}">{paper}</a>')
        rows.append(f'    <span class="n">{p["card_count"]} CARDS · {len(p["chapters"])} SUBJECTS</span></div>')
        for ch in p["chapters"]:
            rows.append(f'  <div class="ix-ch" style="margin:16px 0 4px">')
            rows.append(f'    <a class="t" href="#ch-{ch["chapter_no"]}">{esc(ch["display"])}</a>')
            rows.append(f'    <span class="n">{ch["card_count"]} CARDS</span></div>')
            for s in ch["sections"]:
                rows.append(f'  <div class="ix-sec"><a href="#{s["anchor"]}" '
                            f'style="color:inherit;text-decoration:none">{esc(s["title"])}</a></div>')
                for t in s["subtopics"]:
                    links = " ".join(
                        f'<a href="#card-{cid}" title="{esc(TITLES.get(cid, cid))}">{esc(TITLES.get(cid, cid))}</a>'
                        for cid in t["card_ids"]
                    )
                    rows.append(f'    <div class="ix-sub"><span class="t">{esc(t["title"])}</span>'
                                f'<span class="n">{t["card_count"]}</span></div>')
                    rows.append(f'    <div class="ix-cards">{links}</div>')
        sheets.append("\n".join(rows))

    out = []
    for i, s in enumerate(sheets):
        out.append(f'<div class="sheet">\n{s}\n{foot()}\n</div>')
    return "\n".join(out)


def bm2():
    t = MAP["totals"]
    inner = f'''{topbar("Closing", "BACK COVER")}
  <div style="padding:40px 0 0">
    <div class="lab" style="color:var(--gold)">CLOSING NOTE</div>
    <h1 style="font-size:34px">Now write.</h1>
    <p class="lede" style="font-size:13px">This deck holds {t["cards"]} verified answer units across four papers.
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
    <p class="small">More answer-writing material from the same desk: PYQ Micro Analysis, Mains Model
    Answers, Answer-Writing Frameworks, Keywords Dictionary, and the Data &amp; Facts Compilation.</p>
    <div style="margin-top:56px;padding-top:14px;border-top:1px solid var(--hair2)"
         class="small mono">PYQ NANO ANALYSIS — GS MAINS · THE ANSWER-WRITING PLAYBOOK · FIRST EDITION 2026<br/>
      BUILT FROM THE VERIFIED PYQ NANO CARD ARCHIVE · DESIGN: DR. CSE MAGAZINE STANDARD</div>
  </div>'''
    return f'<div class="sheet p1">\n{inner}\n{foot()}\n</div>'


def main():
    (SRC / "bm1_index.html").write_text(bm1() + "\n", encoding="utf-8")
    (SRC / "bm2_back_cover.html").write_text(bm2() + "\n", encoding="utf-8")
    print(f"wrote src/bm1_index.html · src/bm2_back_cover.html")


if __name__ == "__main__":
    main()
