#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_book.py — Dr. CSE · Data & Facts
Reads scripts/stage2/datafacts/df_book_map.json →
  1. emits modular partials to src/datafacts/ (df_*.html)
  2. assembles final_data_facts.html (fonts + inlined theme + sheets + page numbers)

Pagination: a sub-theme block (heading + rows) is atomic. Small cards are atomic.
Big cards flow across sheets: at a sheet flush the open card's markup is closed
on the old sheet and re-opened on the next sheet with a "— CONTINUED" strip.
Every sheet targets <= ~900px estimated content so it stays a true A4 page.
No card-count statistics anywhere.
"""
import json, os, re, math
import html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SRC = os.path.join(ROOT, 'src', 'datafacts')
BM = json.load(open(os.path.join(HERE, 'df_book_map.json')))

# ---------- height estimation ----------
# Vertical px budget per sheet. Usable content height on an A4 sheet (min-height
# 1123px) minus chrome (topbar+rule ~54, foot ~30, padding ~50) ≈ 990px; 900
# leaves estimation headroom.
CHARS_PER_LINE = 46
ROW_LINE_PX = 14.5
ROW_MARGIN = 5
STH_PX = 27
SHEET_BUDGET = 900
SEC_BAND_PX = 66
SUB_BAND_PX = 50
CARD_HEAD_PX = 58
CONT_PX = 40
TBL_HEAD_PX = 46      # table chrome (thead + wrap margins)
TBL_ROW_PX = 24       # per <tr> — tables SPAN BOTH COLUMNS (full height)
COL_COST = 0.55       # fact rows flow in 2 columns → sheet cost factor
CARD_MARGIN_PX = 18   # .card{margin:0 0 18px} — real box-model cost per card

def plain(s):
    return len(H.unescape(re.sub(r'<[^>]+>', '', s)))

def est_row(r):
    """Sheet-budget cost of one row."""
    if r['kind'] == 'table':
        n = max(r['html'].count('<tr'), 2)
        return TBL_HEAD_PX + TBL_ROW_PX * n     # column-span:all → full height
    lines = max(1, math.ceil(plain(r['html']) / CHARS_PER_LINE))
    return (lines * ROW_LINE_PX + ROW_MARGIN) * COL_COST

def est_block(b):
    col = (STH_PX if b['kind'] == 'sub' else 0) + sum(est_row(r) for r in b['rows'])
    return col

# ---------- chrome ----------
def topbar(stamp=''):
    st = f'<div class="stamp">{stamp}</div>' if stamp else ''
    return ('<div class="topbar"><div class="tb-brand">'
            '<img class="tb-logo" src="assets/images/logo_dr_cse.png" alt="Dr. CSE"/>'
            '<div class="tb-name">Dr. CSE — <b>Data &amp; Facts</b></div></div>' + st + '</div>'
            '<div class="rule"></div>')

def foot():
    return ('<div class="foot"><span>DR. CSE — DATA &amp; FACTS · VERIFIED, DATED, SOURCED</span>'
            '<span class="pg-n"></span></div>')

# ---------- packer with open-card continuation + keep-with-next ----------
class Packer:
    def __init__(self):
        self.sheets = []       # list of html strings
        self.buf = []
        self.est = 0
        self.open_card = None  # (cont_html, cont_px) to prepend after flush
        self.cur_ch = None     # current subject key, e.g. 'ch-5' → data-ch on sheets

    def add(self, html_str, px, keep_next=0):
        """Add one layout unit.

        keep_next = budget px of FOLLOWING content that must share the sheet
        with this unit (keep-with-next for heading units). If unit + keep_next
        does not fit in the remaining budget, THIS unit is moved to a fresh
        sheet first — so a heading can never be stranded at a page bottom
        with its body starting on the next page (the orphaned-heading bug).
        """
        if self.est > 0 and self.est + px + keep_next > SHEET_BUDGET:
            self.flush()
        if not self.buf and self.open_card is not None:
            cont, cont_px = self.open_card
            self.buf.append(cont)
            self.est += cont_px
        self.buf.append(html_str)
        self.est += px

    def flush(self):
        if not self.buf:
            return
        if self.open_card is not None:
            self.buf.append('</div></article>')   # close .rows + .card on this sheet
        attr = f' data-ch="{self.cur_ch}"' if self.cur_ch else ''
        # data-est: packer's estimated content px for this sheet (calibration hook,
        # compare against browser-measured heights — never rendered)
        self.sheets.append(f'<div class="sheet"{attr} data-est="{self.est}">' + topbar() +
                           ''.join(self.buf) + foot() + '</div>')
        self.buf, self.est = [], 0

    def open(self, card_head_html, cont_html, head_px, cont_px):
        """Start a card that may flow across sheets."""
        self.add(card_head_html, head_px)   # may flush previous content
        # card is now open — register continuation for future flushes
        self._pending = (cont_html, cont_px)

    def commit(self, closing_html, px):
        """Close the open card."""
        self._pending_set(None)
        self.add(closing_html, px)

    # -- helpers to manage open state --
    def _pending_set(self, v):
        self.open_card = v

    def begin_flow_card(self, head_html, cont_html, head_px, cont_px, first_px=0):
        """Open a card that may flow across sheets.

        The card head is placed only where head + its FIRST content unit
        (first_px) both fit — an orphaned card title at a sheet bottom is
        structurally impossible. Degenerate case (head + first unit alone
        bigger than a whole sheet budget) degrades to a partial chunk.
        """
        need = head_px + first_px
        if need > SHEET_BUDGET:
            need = head_px + min(first_px, 380)
        if self.est > 0 and self.est + need > SHEET_BUDGET:
            self.flush()
        self.open_card = None
        self.add(head_html + '<div class="rows">', head_px)
        self.open_card = (cont_html, cont_px)   # cont_html is self-contained (article+strip+rows)

    def stream_units(self, units):
        """Stream (html, px, kind) units of one card at row/table granularity.

        Heading units (sth / ssec) keep with the full run of headings that
        follow them plus the first content unit — a sub-theme heading always
        lands on the same sheet as its first rows.
        """
        i, n = 0, len(units)
        while i < n:
            html, px, kind = units[i]
            if kind in ('sth', 'ssec'):
                keep, j = 0, i + 1
                while j < n and units[j][2] in ('sth', 'ssec'):
                    keep += units[j][1]
                    j += 1
                if j < n:
                    keep += units[j][1]
                if px + keep > SHEET_BUDGET:      # degenerate mega-unit
                    keep = min(keep, 380)
                self.add(html, px, keep_next=keep)
            else:
                self.add(html, px)
            i += 1

    def end_flow_card(self, srcs, srcs_px):
        if self.open_card is not None:
            self.add((srcs or '') + '</div></article>', srcs_px + 10)
            self.open_card = None
        else:
            self.add('</div></article>', 10)

# ---------- card rendering ----------
def card_head_html(c):
    yr = H.escape(str(c['data_year']))
    chip = (f'<span class="card-yr" title="{yr}">DATA: {yr}</span>'
            if c['data_year'] and c['data_year'] != 'N/A (Meta-note)' else '')
    # No serial / taxonomy code chip: the card id lives only in the anchor
    # (id="card-…", still targetable from every index) — visible chrome shows
    # the title and the data window only.
    ids = f'<div class="card-ids">{chip}</div>' if chip else ''
    return (f'<article class="card {c["paper_key"]}" id="card-{c["id"]}">'
            f'<div class="card-h"><h4>{H.escape(c["title"])}</h4>{ids}</div>')

def cont_html(c):
    """Continuation opener for the next sheet: re-open the card box (no id —
    the anchor lives on the first fragment), CONTINUED strip, fresh .rows.
    Title only — no serial/taxonomy code in visible chrome."""
    return (f'<article class="card {c["paper_key"]} cont-art">'
            f'<div class="cont">'
            f'<span class="c-t">{H.escape(c["title"])}</span>'
            f'<span class="c-lab">CONTINUED</span></div>'
            '<div class="rows">')

def block_html(b):
    return ''.join(block_html_seq_dict(b))

def block_html_seq_dict(b):
    out = []
    if b['kind'] == 'section':
        out.append(f'<div class="ssec">{b["title"]}</div>')
    elif b['kind'] == 'sub':
        out.append(f'<div class="sth">{b["title"]}</div>')
    for r in b['rows']:
        if r['kind'] == 'table':
            out.append(f'<div class="tblwrap">{r["html"]}</div>')
        else:
            out.append(f'<div class="row l{r["level"]}">{r["html"]}</div>')
    return out

def block_units(c):
    """Stream a card's blocks as (html, est_px, kind) units at row granularity."""
    units = []
    for b in c['blocks']:
        if b['kind'] == 'section':
            units.append((f'<div class="ssec">{b["title"]}</div>', 42, 'ssec'))   # spans both columns
        elif b['kind'] == 'sub':
            units.append((f'<div class="sth">{b["title"]}</div>', STH_PX, 'sth'))
        if not b['rows']:
            continue
        for r in b['rows']:
            if r['kind'] == 'table':
                units.append((f'<div class="tblwrap">{r["html"]}</div>', est_row(r), 'table'))
            else:
                units.append((f'<div class="row l{r["level"]}">{r["html"]}</div>', est_row(r), 'row'))
    return units

def block_html_seq(c):
    """Full html sequence of a card's blocks (small-card atomic path)."""
    out = []
    for b in c['blocks']:
        out.extend(block_html_seq_dict(b))
    return out

def srcs_html(c):
    if not c['sources']:
        return '', 0
    items = []
    for s in c['sources']:
        t, org = H.escape(str(s.get('title', ''))), H.escape(str(s.get('org', '')))
        yr, typ = H.escape(str(s.get('year', ''))), H.escape(str(s.get('type', '')))
        url = H.escape(str(s.get('url', '')), quote=True)
        link = f'<a href="{url}" target="_blank" rel="noopener">{t}</a>' if url else t
        chip = f'<span class="s-type">{typ}</span>' if typ else ''
        items.append(f'<div class="src">{org} · {link} ({yr}){chip}</div>')
    return ('<div class="srcs"><div class="s-lab">SOURCES</div>' + ''.join(items) + '</div>'), \
           26 + 15 * len(items)

def head_chunk_px(c):
    """Budget px that MUST follow a heading band on the same sheet:
    the next card's head plus its first content unit (flow cards), or the
    card's full body (atomic small cards). Used as keep_next for sec-h and
    sub-h bands so a band is never orphaned above a page break."""
    units = block_units(c)
    srcs, srcs_px = srcs_html(c)
    total = CARD_HEAD_PX + CARD_MARGIN_PX + sum(px for _, px, _ in units) + srcs_px
    if total <= 300 + CARD_MARGIN_PX:      # small card — atomic
        return total
    return CARD_HEAD_PX + CARD_MARGIN_PX + (units[0][1] if units else 60)

def emit_card(packer, c):
    srcs, srcs_px = srcs_html(c)
    units = block_units(c)
    body_total = sum(px for _, px, _ in units)
    total = CARD_HEAD_PX + CARD_MARGIN_PX + body_total + srcs_px

    if total <= 300 + CARD_MARGIN_PX:   # small card — atomic
        parts = [card_head_html(c), '<div class="rows">']
        for uh in block_html_seq(c):
            parts.append(uh)
        if srcs:
            parts.append(srcs)
        parts.append('</div></article>')
        packer.open_card = None
        packer.add(''.join(parts), max(total, 110))
        return

    # big card — flow across sheets at ROW granularity (never split a table)
    first_px = units[0][1] if units else 60
    packer.begin_flow_card(card_head_html(c), cont_html(c),
                           CARD_HEAD_PX + CARD_MARGIN_PX, CONT_PX + CARD_MARGIN_PX, first_px)
    packer.stream_units(units)
    packer.end_flow_card(srcs, srcs_px)

def emit_subject(packer, subject):
    links = ' '.join(f'<a href="#card-{c["id"]}">{H.escape(c["title"])}</a>'
                     for c in subject['all_cards'])
    paper_label = {'GS1': 'GS PAPER I', 'GS2': 'GS PAPER II', 'GS3': 'GS PAPER III'}[subject['paper']]
    html_s = (f'<div class="sheet" id="{subject["anchor"]}" data-ch="{subject["anchor"]}">' + topbar() +
              '<div style="padding:48px 0 0">'
              f'<div class="hero-tag">{paper_label}</div>'
              f'<div class="chap-t"><h1>{H.escape(subject["display"])}</h1></div>'
              '<div class="chdiv"></div>'
              '<div class="ix-hint">FACT SHEETS IN THIS SUBJECT — TAP ANY TITLE TO JUMP TO IT</div>'
              f'<div class="ix-cards" style="flex-direction:column;gap:6px">{links}</div>'
              '</div>' + foot() + '</div>')
    packer.flush()
    packer.sheets.append(html_s)
    packer.buf, packer.est, packer.open_card = [], 0, None
    packer.cur_ch = subject['anchor']

def emit_content(packer):
    sec_state = {}
    for p in BM['tree']:
        for s in p['subjects']:
            emit_subject(packer, s)      # subject page = chapter opener, always a fresh sheet
            sec_key, sub_key = None, None
            for sg in s['sections']:
                for st in sg['subtopics']:
                    if sec_key != (s['key'], sg['name']):
                        sec_key = (s['key'], sg['name'])
                        sub_key = None
                        kicker = {'GS1': 'GS PAPER I', 'GS2': 'GS PAPER II', 'GS3': 'GS PAPER III'}[s['paper']]
                        # keep-with-next: section band must land with the following
                        # subtopic band + first card head + its first content unit
                        packer.add(f'<div class="sec-h"><span class="k">{kicker} · SECTION</span>'
                                   f'<h2>{H.escape(sg["name"])}</h2></div>', SEC_BAND_PX,
                                   keep_next=SUB_BAND_PX + head_chunk_px(st['cards'][0]))
                    if sub_key != st['name']:
                        sub_key = st['name']
                        # keep-with-next: subtopic band must land with the next
                        # card head + its first content unit
                        packer.add(f'<div class="sub-h"><h3>{H.escape(st["name"])}</h3></div>', SUB_BAND_PX,
                                   keep_next=head_chunk_px(st['cards'][0]))
                    for c in st['cards']:
                        emit_card(packer, c)
            packer.flush()

# ---------- front & back matter ----------
def cover_html():
    return '''<div class="sheet p1" id="fm-cover">
  <div class="topbar" style="min-height:0">
    <img class="cover-logo" src="assets/images/logo_dr_cse.png" alt="Dr. CSE"/>
    <div class="stamp">FIRST EDITION<br/>2026</div>
  </div>
  <div class="rule"></div>
  <div style="padding:92px 0 0">
    <div class="lab" style="color:var(--gold)">GS MAINS · PAPERS I–III · EVERY NUMBER SOURCED</div>
    <h1 style="font-size:76px;letter-spacing:-2.5px">Data &amp; Facts</h1>
    <p class="lede" style="font-size:14px;margin-top:16px;max-width:560px">GS Mains · Papers I–III.
    Each fact sheet carries verified numbers with their data window and their source —
    rankings, budgets, schemes, indices. Quote a figure, a year and a source name in one line,
    and your answer stands out.</p>
    <div class="chips" style="margin-top:20px">
      <a class="chip" href="#ix-title">CONTENTS — CLICK ANY FACT SHEET TO JUMP TO IT</a>
      <a class="chip" href="#fm-disclaimer">DISCLAIMER · HOW TO USE THIS BOOK</a>
    </div>
  </div>
  <div style="margin-top:88px;padding:0 2px">
    <p class="small" style="letter-spacing:1.2px;margin-bottom:10px">FROM THE DESK OF DR. CSE — MORE ANSWER-WRITING MATERIAL</p>
    <div class="cover-contact">
      <span><a href="https://drcse.in" target="_blank" rel="noopener">drcse.in</a></span>
      <span><a href="https://t.me/dr_cse" target="_blank" rel="noopener">t.me/dr_cse</a></span>
      <span><a href="mailto:dr.cse.001@gmail.com">dr.cse.001@gmail.com</a></span>
    </div>
    <p class="small" style="margin-top:12px">Every figure on every card is kept exactly as verified from its source,
    with the period it belongs to.</p>
  </div>
</div>'''

def disclaimer_html():
    return '''<div class="sheet" id="fm-disclaimer">
  ''' + topbar() + '''
  <h1 id="fm-disclaimer-h">Disclaimer &amp; how to use this book</h1>
  <p class="lede">Read this page before you quote anything. It takes one minute.</p>
  <div class="panel">
    <div class="p-t">DISCLAIMER</div>
    <p>This book is for education. Data moves — new reports replace old ones every year.
    Every card shows its data window and its source at the bottom. Before you quote a figure
    in the exam, check it once against the official source. The authors and Dr. CSE are not
    liable for any loss caused by the use of this material. © Dr. CSE 2026. All rights reserved.</p>
    <p class="small">Contact: drcse.in · t.me/dr_cse · dr.cse.001@gmail.com</p>
  </div>
  <div class="panel">
    <div class="p-t">HOW TO USE THIS BOOK</div>
    <p><b>How a card is built.</b> Title on top. The data window sits next to the card ID —
    it tells you which years the numbers belong to. Inside, facts sit in two columns, grouped
    by theme. Sources close the card.</p>
    <p><b>How to quote in the exam.</b> Give the number, the period, and the source name —
    one line. Example: <i>India ranked 9th on the Climate Risk Index for 1995–2024 (Germanwatch).</i></p>
    <p><b>How to move around.</b> Tap any fact-sheet title in the contents. Every subject page
    also lists its own cards. The floating INDEX button follows you on every page.</p>
    <p><b>Print.</b> A4, portrait, background graphics ON — one sheet prints as one page.</p>
  </div>
  <div class="note">Numbers with a small dotted underline are live source links. They open the
  original report in your browser.</div>
  ''' + foot() + '''
</div>'''

PART_INFO = {
    'GS1': dict(chip='GS PAPER I',
                name='Indian Heritage, History and Geography of the World and Society',
                lede='Paper I — Indian Heritage and Culture, History, Geography of the World and Society.',
                verdict='One dated number can lift a GS-1 answer above the rest.'),
    'GS2': dict(chip='GS PAPER II',
                name='Governance, Constitution, Polity, Social Justice and International Relations',
                lede='Paper II — Governance, Constitution, Polity, Social Justice and International Relations.',
                verdict='Governance answers score when they carry scheme numbers and years.'),
    'GS3': dict(chip='GS PAPER III',
                name='Technology, Economic Development, Environment, Security and Disaster Management',
                lede='Paper III — Technology, Economic Development, Bio-diversity, Environment, Security and Disaster Management.',
                verdict='GS-3 rewards data — budgets, indices, targets — more than any other paper.'),
}

def opener_html(pk):
    info = PART_INFO[pk]
    p = next(q for q in BM['tree'] if q['key'] == pk)
    chips = ''.join(f'<a class="chip" href="#{s["anchor"]}">{H.escape(s["display"])}</a>'
                    for s in p['subjects'])
    return (f'<div class="sheet" id="pt-{pk.lower()}">' + topbar() +
            '<div style="padding:56px 0 0">'
            f'<span class="gschip">{info["chip"]}</span>'
            '<div class="chap-t" style="margin-top:18px">'
            f'<h1>{H.escape(info["name"])}</h1></div>'
            f'<p class="lede">{H.escape(info["lede"])}</p>'
            f'<div class="verdict"><p>{H.escape(info["verdict"])}</p></div>'
            '<div class="chdiv"></div>'
            '<div class="ix-hint">SUBJECTS IN THIS PAPER — TAP TO OPEN</div>'
            f'<div class="chips">{chips}</div>'
            '</div>' + foot() + '</div>')

def backcover_html():
    return ('<div class="sheet p1">' +
            topbar('DATA &amp; FACTS<br/>FIRST EDITION 2026') +
            '<div style="padding:70px 0 0;text-align:center">'
            '<div class="lab" style="color:var(--gold)">MORE ANSWER-WRITING MATERIAL FROM THE DESK OF DR. CSE</div>'
            '<h1 style="font-size:44px">Replica, Data &amp; Facts,<br/>and more</h1>'
            '<p class="lede" style="margin:14px auto 0">Companion guides for GS Mains — answer cards,'
            'verified data, and readymade resources. All on drcse.in.</p>'
            '</div>'
            '<figure class="fig" style="max-width:480px;margin:22px auto 0">'
            '<img src="assets/images/cover_candidate_resource_guide.png" alt="Dr. CSE companion resources guide"/>'
            '</figure>'
            '<div style="margin-top:26px;padding:0 2px">'
            # margin-top:0 — the wrapper above already provides the 26px gap;
            # flex sheets do not collapse parent/child margins, so keeping the
            # class default (26px) here would double the gap and spill past A4.
            '<div class="cover-contact" style="margin-top:0">'
            '<span><a href="https://drcse.in" target="_blank" rel="noopener">drcse.in</a></span>'
            '<span><a href="https://t.me/dr_cse" target="_blank" rel="noopener">t.me/dr_cse</a></span>'
            '<span><a href="mailto:dr.cse.001@gmail.com">dr.cse.001@gmail.com</a></span>'
            '</div>'
            '<p class="small" style="margin-top:12px;text-align:center">Dr. CSE — Data &amp; Facts · First Edition 2026</p>'
            '</div></div>')

# ---------- master index ----------
INDEX_BUDGET = 1060        # px; calibrated (sheet real capacity ~1039 minus safety)
IX_CHARS_PER_LINE = 60    # ~338px column at 10.5px IBM Plex Sans

def _pg_span(key, pm, prefix='· '):
    """Muted page-number span for an index entry (empty when pagemap absent)."""
    if pm and key in pm:
        return f'<span class="pg">{prefix}{pm[key]}</span>'
    return ''

def _ix_line_est(chars):
    """Estimated sheet-cost px of one index line (2-col balanced body).
    Calibrated against browser measurement: stacked cost (lines×20.3+4) with a
    ×0.30 net factor for balanced 2-column flow + wrap variance (measured
    est/real ratio was 1.95–1.98 before calibration — see worklog A4-3)."""
    lines = max(1, math.ceil(chars / IX_CHARS_PER_LINE))
    return (lines * 20.3 + 4) * 0.30

def _subject_block(s, pm):
    """One subject's index block (subject header + section + subtopic card lines).
    Rendered and packed as an ATOMIC unit — a subject never tears across sheets."""
    parts = [f'<div class="ix-sec"><a href="#{s["anchor"]}">{H.escape(s["display"])}</a>'
             + _pg_span(s['anchor'], pm, 'p. ') + '</div>']
    est = 48
    for sg in s['sections']:
        parts.append(f'<div class="ix-line"><span class="st">{H.escape(sg["name"])}</span></div>')
        est += 24
        for st in sg['subtopics']:
            links, chars = [], 0
            for c in st['cards']:
                pgno = pm.get(c['id']) if pm else None
                pg_s = f'<span class="pg">· {pgno}</span>' if pgno else ''
                links.append(f'<a href="#card-{c["id"]}">{H.escape(c["title"])}</a>{pg_s}')
                chars += len(c['title']) + (len(str(pgno)) + 4 if pgno else 0) + 3
            parts.append('<div class="ix-line">' + ' <span class="sep">·</span> '.join(links) + '</div>')
            est += _ix_line_est(chars)
    return ''.join(parts), est

def index_sheets(pm=None):
    """Build the master index sheets.

    Pagination rules (Phase 2 break logic applied to the index):
      - a paper header is CONCATENATED with its first subject block → a paper
        heading can never be orphaned at a sheet bottom;
      - subject blocks are atomic (all-or-nothing per sheet);
      - page numbers (pm) come from the FINAL ordering — main() iterates to a
        fixpoint so displayed numbers always match stamped pagination.
    """
    sheets, buf, est = [], [], 0

    def flush(first):
        nonlocal buf, est
        if not buf:
            return
        head = ('<h1 id="ix-title">Every fact sheet, subject by subject</h1>' if first
                else '<div class="ix-hint">CONTENTS — CONTINUED</div>')
        hint = ('<div class="ix-hint">PAPER → SUBJECT → SECTION → THEME — EVERY LINE IS CLICKABLE</div>'
                if first else '')
        sid = ' id="ix-master"' if first else ''
        sheets.append(f'<div class="sheet"{sid} data-est="{est}">' + topbar() + head + hint +
                      '<div class="ix-body">' + ''.join(buf) + '</div>' + foot() + '</div>')
        buf.clear()
        est = 0

    first = True
    for p in BM['tree']:                       # GS1 → GS2 → GS3 (sorted at parse)
        head_html = ('<div class="ix-ch"><a class="t" href="#pt-{k}">{lab}</a>{pg}</div>'
                     .format(k=p['key'].lower(), lab=H.escape(p['label']),
                             pg=_pg_span(f'pt-{p["key"].lower()}', pm, 'p. ')))
        for si, s in enumerate(p['subjects']):
            s_html, s_est = _subject_block(s, pm)
            head_now, head_est = (head_html, 40) if si == 0 else ('', 0)
            if est > 0 and est + head_est + s_est > INDEX_BUDGET:
                flush(first)
                first = False
            buf.append(head_now + s_html)      # paper header rides with first subject
            est += head_est + s_est
    flush(first)
    return sheets

def build_pagemap(ordered):
    """card/subject/part anchor → printed page number (position in final order)."""
    pm = {}
    for pos, sh in enumerate(ordered, start=1):
        for m in re.finditer(r'id="card-([A-Z0-9-]+)"', sh):
            pm.setdefault(m.group(1), pos)
        m = re.search(r'<div class="sheet" id="(ch-\d+)"', sh)
        if m:
            pm[m.group(1)] = pos
        m = re.search(r'<div class="sheet" id="(pt-gs\d)"', sh)
        if m:
            pm[m.group(1)] = pos
    return pm

# ---------- main ----------
def main():
    # assign subject anchors + flat card lists
    ch_n = 0
    for p in BM['tree']:
        for s in p['subjects']:
            ch_n += 1
            s['anchor'] = f'ch-{ch_n}'
            s['ch_n'] = ch_n
            s['paper'] = p['key']
            s['key'] = s['key']
            s['all_cards'] = [c for sg in s['sections'] for st in sg['subtopics'] for c in st['cards']]

    packer = Packer()
    emit_content(packer)

    openers = {p['key']: opener_html(p['key']) for p in BM['tree']}

    # group content sheets by paper (via data-ch attribution), interleave with openers
    by_paper = {p['key']: [] for p in BM['tree']}
    ch2paper = {s['anchor']: s['paper'] for p in BM['tree'] for s in p['subjects']}
    cur_paper = None
    for sh in packer.sheets:
        m = re.search(r'(?:id|data-ch)="(ch-\d+)"', sh)
        if m:
            cur_paper = ch2paper[m.group(1)]
        if cur_paper:
            by_paper[cur_paper].append(sh)

    def assemble(ix):
        ordered = [cover_html(), disclaimer_html()] + ix
        for p in BM['tree']:
            ordered.append(openers[p['key']])
            ordered += by_paper[p['key']]
        ordered.append(backcover_html())
        return ordered

    # INDEX IS GENERATED LAST: iterate to a fixpoint — index page numbers depend
    # on the final ordering, and the ordering depends on the index sheet count.
    # Converged when the count stops changing (numbers then cannot shift pages).
    ix = index_sheets(None)
    ordered = assemble(ix)
    for _ in range(6):
        pm = build_pagemap(ordered)
        new_ix = index_sheets(pm)
        if len(new_ix) == len(ix):
            ix = new_ix
            break
        ix = new_ix
        ordered = assemble(ix)
    ordered = assemble(ix)
    # stability assertion: page numbers in the shipped index match final pagination
    pm_final = build_pagemap(ordered)
    assert len(index_sheets(pm_final)) == len(ix), 'index pagination did not converge'

    total = len(ordered)
    stamped = []
    for i, sh in enumerate(ordered, start=1):
        pn = f'{i:03d} / {total:03d}'
        stamped.append(re.sub(r'(<span class="pg-n">)</span>', r'\g<1>' + pn + '</span>', sh, count=1))

    css = open(os.path.join(SRC, 'theme.css')).read()
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Dr. CSE — Data &amp; Facts · GS Mains</title>
<meta name="description" content="Dr. CSE — Data &amp; Facts: verified, dated, sourced numbers for UPSC GS Mains Papers I–III."/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet"/>
<style>
{css}
</style>
</head>
<body>
<a class="skip" href="#ix-title">Skip to contents</a>
<a class="to-ix" href="#ix-title">INDEX</a>
<div class="book">
{''.join(stamped)}
</div>
</body>
</html>'''

    out_path = os.path.join(ROOT, 'final_data_facts.html')
    open(out_path, 'w').write(doc)
    print(f'assembled {out_path}: {total} sheets, {os.path.getsize(out_path)/1024:.0f} KB')

    # persist partials — wipe stale df_*.html first (paper reordering changes
    # ch-N numbering and index sheet counts between runs)
    for f in os.listdir(SRC):
        if f.startswith('df_') and f.endswith('.html'):
            os.remove(os.path.join(SRC, f))
    parts = {'df_fm1_cover.html': cover_html(),
             'df_fm2_disclaimer.html': disclaimer_html(),
             'df_bm2_back.html': backcover_html()}
    for p in BM['tree']:
        parts[f'df_pt_{p["key"].lower()}_opener.html'] = openers[p['key']]
    for i, sh in enumerate(ix, 1):
        parts[f'df_bm1_index_{i:02d}.html'] = sh
    seq = {}
    for sh in packer.sheets:
        m = re.search(r'(?:id|data-ch)="(ch-\d+)"', sh)
        if not m:
            continue
        k = m.group(1)
        seq[k] = seq.get(k, 0) + 1
        parts[f'df_{k}_{seq[k]:02d}.html'] = sh
    for name, content in parts.items():
        open(os.path.join(SRC, name), 'w').write(content + '\n')
    print(f'wrote {len(parts)} partials to src/datafacts/')

if __name__ == '__main__':
    main()
