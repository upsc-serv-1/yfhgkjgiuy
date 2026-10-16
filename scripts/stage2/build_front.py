#!/usr/bin/env python3
"""Phase 4b (v3, post-review round 2) — generate front matter + part openers.

v3 review decisions baked in:
  - Book renamed: REPLICA (Exam Replicable) · Intro to Conclusion.
  - Cover: Dr. CSE logo top-left, NO card-count statistics (they scare
    students), website + Telegram contact strip.
  - Page 2 = Disclaimer + How to Approach (replaces foreword + how-to-use).
  - Thin running header everywhere: logo + "Dr. CSE — Replica".
  - Part openers: no counts, no GS-4 mini-index (each subject's own page now
    carries its full clickable card index).
  - Openers/index pages are true A4 pages (.a4).
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
    "GS-1": "Ready cards for heritage, history, geography, and society. Open any subject below and revise its cards in minutes.",
    "GS-2": "Ready cards for the Constitution, governance, social justice, and international relations. Click a subject to start revising.",
    "GS-3": "Ready cards for economy, security, agriculture, science, environment, and disasters. Click a subject to start revising.",
    "GS-4": "Ready cards for ethics, integrity, and aptitude. Click the subject below to open its full card index.",
}

LOGO = "assets/images/logo_dr_cse.png"


def esc(t):
    return html.escape(t, quote=False)


# thin running header + footer (shared with the rest of the book)
THIN = ('  <div class="topbar">\n'
        f'    <div class="tb-brand"><img class="tb-logo" src="{LOGO}" alt="Dr. CSE"/>'
        '<span class="tb-name">Dr. CSE — <b>Replica</b></span></div>\n'
        '  </div>\n  <div class="rule"></div>')
FOOT = ('  <div class="foot"><span>DR. CSE — REPLICA · INTRO TO CONCLUSION</span>'
        '<span class="pg-n">·</span></div>')


def sheet(inner, cls="", with_foot=True):
    c = f" {cls}" if cls else ""
    f = f"\n{FOOT}" if with_foot else ""
    return f'<div class="sheet{c}">\n{inner}{f}\n</div>'


# ============================================================ fm1 cover =====
def fm1():
    inner = f'''  <div class="topbar" style="min-height:0">
    <img class="cover-logo" src="{LOGO}" alt="Dr. CSE"/>
    <div class="stamp">FIRST EDITION<br/>2026</div>
  </div>
  <div class="rule"></div>
  <div style="padding:96px 0 0">
    <div class="lab" style="color:var(--gold)">EXAM REPLICABLE · INTRO TO CONCLUSION</div>
    <h1 id="fm-cover" style="font-size:76px;letter-spacing:-2.5px">Replica</h1>
    <p class="lede" style="font-size:14px;margin-top:16px;max-width:560px">GS Mains · Papers I–IV.
    Every examinable topic as one ready answer card — a quotable opening, a crisp introduction,
    evidence, data, and a conclusion you can replicate in the exam hall.</p>
    <div class="chips" style="margin-top:20px">
      <a class="chip" href="#ix-master">CONTENTS — CLICK ANY CARD TITLE TO JUMP TO IT</a>
      <a class="chip" href="#fm-disclaimer">DISCLAIMER · HOW TO APPROACH THIS BOOK</a>
    </div>
  </div>
  <div style="margin-top:84px;padding:0 2px">
    <p class="small" style="letter-spacing:1.2px;margin-bottom:10px">FROM THE DESK OF DR. CSE — MORE ANSWER-WRITING MATERIAL</p>
    <div class="cover-contact">
      <span><a href="https://drcse.in" target="_blank" rel="noopener">drcse.in</a></span>
      <span><a href="https://t.me/dr_cse" target="_blank" rel="noopener">t.me/dr_cse</a></span>
      <span><a href="mailto:dr.cse.001@gmail.com">dr.cse.001@gmail.com</a></span>
    </div>
    <p class="small" style="margin-top:12px">Quotes, figures, names and judgments inside every card are kept
    exactly as verified from standard sources.</p>
  </div>'''
    return sheet(inner, cls="p1", with_foot=False)


# ======================================== fm2 · disclaimer + how to approach ==
def fm2():
    inner = f'''{THIN}
  <div class="lab" style="color:var(--gold)">PLEASE READ FIRST</div>
  <h1 id="fm-disclaimer" style="font-size:30px">Disclaimer &amp; how to approach</h1>

  <div class="panel">
    <div class="p-t">DISCLAIMER</div>
    <p><strong>What this book is.</strong> A deck of ready answer cards for UPSC GS Mains,
    Papers I to IV. Each card replicates the full arc of a strong answer — quote, introduction,
    examples, data, conclusion — in language you can lift into the exam.</p>
    <p><strong>What this book is not.</strong> It is not a set of model answers to specific
    questions, not a prediction of the next paper, and not a guarantee that any topic will be
    asked. It is a revision deck, not a coaching course.</p>
    <p><strong>On facts.</strong> Quotes, figures, names, acts, schemes and judgments are kept
    exactly as verified from standard sources at the time of polishing. Always cross-check the
    most recent data from current affairs before you quote a figure in the exam.</p>
    <p><strong>On use.</strong> This deck is for personal exam preparation. Please do not
    redistribute or resell it. Share it the honest way — point a friend to
    <a href="https://drcse.in" target="_blank" rel="noopener">drcse.in</a> or
    <a href="https://t.me/dr_cse" target="_blank" rel="noopener">t.me/dr_cse</a>.</p>
  </div>

  <div class="panel">
    <div class="p-t">HOW TO APPROACH THIS BOOK</div>
    <p><strong>1 · Jump, do not read cover-to-cover.</strong> Open the subject-wise contents,
    click a subject, then click any card title. Every card is self-contained, so five spare
    minutes are enough to revise one.</p>
    <p><strong>2 · Read a card the way you will write it.</strong> Quote first — one verified
    line earns marks safely. Then the boxed introduction, the examples, the data, and the
    conclusion with its forward look. Each part sits in its own labelled box.</p>
    <p><strong>3 · Close the book and write.</strong> After every few cards, write one answer
    paragraph from memory. That single habit is worth more than any new material.</p>
    <p><strong>4 · Find any card in seconds.</strong> The round INDEX button at the
    bottom-right corner brings you back to the contents from anywhere. Every card also carries
    a short ID like <span class="mono" style="font-size:10px">GS1-HIST-0001</span> — search it
    with Ctrl+F.</p>
  </div>

  <div class="take" style="margin-top:4px"><strong>The one-line method.</strong> Open a card,
  read it once, close the book, and write its argument in your own words. Repeat until the
  exam feels familiar.</div>

  <div class="cover-contact" style="margin-top:16px">
    <span><a href="https://drcse.in" target="_blank" rel="noopener">drcse.in</a></span>
    <span><a href="https://t.me/dr_cse" target="_blank" rel="noopener">t.me/dr_cse</a></span>
    <span><a href="mailto:dr.cse.001@gmail.com">dr.cse.001@gmail.com</a></span>
  </div>'''
    return sheet(inner, cls="a4")


# ====================================================== part openers =========
def part_opener(p):
    paper = p["paper"]
    roman = PAPER_ROMAN[paper]
    anchor = f"pt-{paper.lower().replace('-', '')}"
    # subjects of this part, each with clickable section links — NO counts
    sub_blocks = []
    for ch in p["chapters"]:
        links = " ".join(
            f'<a href="#{s["anchor"]}">{esc(s["title"])}</a>'
            for s in ch["sections"]
        )
        sub_blocks.append(
            f'  <div class="ix-ch" style="margin:12px 0 3px">'
            f'<a class="t" href="#ch-{ch["chapter_no"]}">{esc(ch["display"])}</a></div>\n'
            f'  <div class="ix-cards" style="margin-bottom:2px">{links}</div>'
        )
    inner = f'''{THIN}
  <div style="margin-top:4px">
    <span class="gschip">{paper}</span>
    <div class="hero-tag" style="margin-top:10px">PART {roman} OF IV</div>
    <h1 id="{anchor}" style="font-size:32px;max-width:660px">{PAPER_TITLES[paper]}</h1>
    <p class="lede tight">{PAPER_LEDES[paper]}</p>
  </div>
  <div class="ix-hint">SUBJECTS IN THIS PART — CLICK A SUBJECT OR SECTION TO OPEN IT</div>
{chr(10).join(sub_blocks)}'''
    return sheet(inner, cls="a4")


# ==================================================================== main ==
def main():
    files = {
        "fm1_cover.html": fm1(),
        "fm2_disclaimer.html": fm2(),
        "pt1_gs1_opener.html": part_opener(MAP["parts"][0]),
        "pt2_gs2_opener.html": part_opener(MAP["parts"][1]),
        "pt3_gs3_opener.html": part_opener(MAP["parts"][2]),
        "pt4_gs4_opener.html": part_opener(MAP["parts"][3]),
    }
    for name, content in files.items():
        (SRC / name).write_text(content + "\n", encoding="utf-8")
        print(f"wrote src/{name}: {len(content):,} bytes")
    # retire the v2 front-matter partials (replaced by fm2_disclaimer)
    for stale in ("fm2_foreword.html", "fm3_how_to_use.html"):
        f = SRC / stale
        if f.exists():
            f.unlink()
            print(f"removed stale src/{stale}")
    print("front matter + part openers done (v3: Replica branding, disclaimer page, no counts)")


if __name__ == "__main__":
    main()
