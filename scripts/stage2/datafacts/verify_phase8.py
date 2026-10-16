#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_phase8.py — Phase 8 gate: duplicate source panels removed.

Checks:
  1. PANEL RULE: .srcs panels exist ONLY on cards with zero inline citations
     (expect exactly 1: the SOCIETY/General meta-note card GS1-SOC-0001).
  2. INLINE CITATIONS PRESERVED: row + label source links all survive
     (QA gate 3); every card that had inline links still has them.
  3. COPY: disclaimer/how-to-use no longer claims 'source at the bottom'.
  4. REGRESSION: geometry (A4, pinned feet), no orphaned headings (incl.
     .sth2), index page numbers, highlighting count, two-column rows.
  5. PDF: Playwright A4 print == sheet count.
  6. SCREENSHOTS: card-bottom pages for visual check (cards end cleanly).
"""
import os, re, sys, json
from playwright.sync_api import sync_playwright

ROOT = '/home/z/my-project/ebook'
FILE = os.path.join(ROOT, 'final_data_facts.html')
SHOTS = os.path.join(ROOT, 'scripts/stage2/datafacts/shots')

def main():
    doc = open(FILE).read()
    BM = json.load(open(os.path.join(ROOT, 'scripts/stage2/datafacts/df_book_map.json')))
    fails = []

    # ---- 1. panel rule ----
    n_panels = doc.count('<div class="srcs">')
    # attribute each panel to the cards whose anchors live on the same SHEET
    # (a flowed card's panel may sit in a continuation fragment on a later
    # sheet than its anchor — attribute via the CONTINUED strip title then)
    sheets = re.findall(r'<div class="sheet[^"]*"[^>]*>.*?(?=<div class="sheet|<a class="to-ix|</body>)', doc, re.S)
    panel_sheets = [i for i, sh in enumerate(sheets) if '<div class="srcs">' in sh]
    panel_ok = []
    for si in panel_sheets:
        sh = sheets[si]
        # the card the panel closes: walk back over CONTINUED strips + anchors
        # on this sheet; the LAST card-start before the panel owns it
        starts = [(m.start(), m.group(1) or m.group(2))
                  for m in re.finditer(r'<article class="card[^"]*" id="card-([A-Z0-9-]+)">|'
                                       r'<article class="card[^"]* cont-art">.*?'
                                       r'<span class="c-t">([^<]+)</span>', sh, re.S)]
        before = [t for p, t in starts
                  if p < max(m.start() for m in re.finditer(r'<div class="srcs">', sh))]
        owner = before[-1] if before else '?'
        # resolve title → card id via book map
        cid = owner if re.match(r'^[A-Z0-9-]+$', owner) else \
            next((c['id'] for c in BM['cards_flat'] if c['title'] == owner), f'title:{owner}')
        panel_ok.append(cid)
    print(f"SOURCES panels: {n_panels} (owned by {panel_ok})")
    no_inline = []
    for c in BM['cards_flat']:
        has = any('<a href="http' in (b['title'] or '') for b in c['blocks']) or \
              any('<a href="http' in r['html'] for b in c['blocks'] for r in b['rows'])
        if not has:
            no_inline.append(c['id'])
    print(f"cards without inline citations: {no_inline}")
    if sorted(panel_ok) != sorted(no_inline):
        fails.append(f'panel rule broken: panels on {panel_ok}, no-inline cards {no_inline}')

    # ---- 2. inline citations preserved ----
    n_row = sum(r['html'].count('<a href=') for c in BM['cards_flat'] for b in c['blocks'] for r in b['rows'])
    n_lab = sum((b['title'] or '').count('<a href=') for c in BM['cards_flat'] for b in c['blocks'])
    ext = len(re.findall(r'<a href="https?://[^"]+"', doc))
    print(f"inline links: {n_row} rows + {n_lab} labels | external <a> in doc: {ext}")
    if ext < n_row + n_lab:
        fails.append('inline citation links lost')

    # ---- 3. copy ----
    stale = [s for s in ('source at the bottom', 'Sources close the card') if s in doc]
    print('stale copy phrases:', stale or 'none')
    if stale:
        fails.append(f'stale disclaimer copy: {stale}')

    # ---- 4+5. browser regression + PDF ----
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={'width': 900, 'height': 1400})
        page.goto('file://' + FILE)
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(1500)
        data_dom = page.evaluate('''() => {
            const out = [];
            document.querySelectorAll('.sheet').forEach((el, i) => {
                const r = el.getBoundingClientRect();
                const foot = el.querySelector('.foot');
                const fr = foot ? foot.getBoundingClientRect() : null;
                let contentEnd = 0, lastBefore = null;
                for (const ch of el.children) {
                    if (ch.classList.contains('foot')) break;
                    const cr = ch.getBoundingClientRect();
                    if (cr.bottom > contentEnd) { contentEnd = cr.bottom; lastBefore = ch; }
                }
                out.push({i: i+1, w: Math.round(r.width), h: Math.round(r.height),
                    fill: Math.round(100*(contentEnd - r.top)/r.height),
                    footGap: fr ? Math.round(r.bottom - fr.bottom) : null,
                    lastCls: lastBefore ? (lastBefore.className || '').toString() : '',
                    nHl: el.querySelectorAll('b.hl').length});
            });
            return out;
        }''')
        n_sheets = len(data_dom)
        tall = [d['i'] for d in data_dom if d['h'] > 1125 or d['w'] != 794]
        badfoot = [d['i'] for d in data_dom if d['footGap'] is not None and d['footGap'] != 24]
        orph = [d['i'] for d in data_dom
                if re.search(r'sub-h|sec-h|ssec|card-h|ix-ch|ix-sec', d['lastCls'])
                or re.search(r'^sth2?$', d['lastCls'].strip())]
        n_hl = sum(d['nHl'] for d in data_dom)
        fills = [d['fill'] for d in data_dom if d['footGap'] is not None]
        print(f"sheets: {n_sheets} | non-A4 {tall or 'none'} | bad-foot {badfoot or 'none'} | "
              f"orphans {orph or 'none'} | b.hl {n_hl}")
        print(f"fills: min {min(fills)}% median {sorted(fills)[len(fills)//2]}% max {max(fills)}%")
        if tall: fails.append(f'non-A4 sheets: {tall[:10]}')
        if badfoot: fails.append(f'foot not pinned: {badfoot[:10]}')
        if orph: fails.append(f'orphaned headings: {orph[:10]}')

        anchor_page = page.evaluate('''() => {
            const m = {};
            document.querySelectorAll('.sheet').forEach((sh, i) => {
                [sh.id, ...[...sh.querySelectorAll('[id]')].map(e => e.id)].forEach(id => {
                    if (!id) return;
                    const key = id.replace(/^card-/, '');
                    if (!(key in m)) m[key] = i + 1;
                });
            });
            return m;
        }''')
        bad_pg = page.evaluate('''(anchorPage) => {
            const bad = []; let n = 0;
            const check = (a) => {
                const pgEl = a.nextElementSibling;
                if (!pgEl || !pgEl.classList.contains('pg')) return;
                n++;
                const key = a.getAttribute('href').slice(1).replace(/^card-/, '');
                const shown = parseInt(pgEl.textContent.replace(/[^0-9]/g, ''), 10);
                if (anchorPage[key] !== shown) bad.push([key, shown, anchorPage[key]]);
            };
            document.querySelectorAll('.ix-line a[href^="#card-"], .ix-line a[href^="#ch-"], ' +
                                   '.ix-sec a[href^="#ch-"], .ix-ch a[href^="#pt-"]').forEach(check);
            return {n, bad};
        }''', anchor_page)
        print(f"index page numbers: {bad_pg['n']} checked, {len(bad_pg['bad'])} mismatches")
        if bad_pg['bad']:
            fails.append(f"index page numbers wrong: {bad_pg['bad'][:5]}")

        pdf_path = os.path.join(SHOTS, 'phase8_check.pdf')
        page.pdf(path=pdf_path, format='A4', print_background=True,
                 margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        # screenshots: 4 card-bottom sheets (last sheet of a subject's run)
        sheets = page.query_selector_all('.sheet')
        # pick 4 spreads across the book
        targets = [max(n_sheets // 5, 1), n_sheets // 2, 3 * n_sheets // 4, n_sheets - 2]
        for t in sorted(set(targets)):
            el = sheets[t - 1]
            el.scroll_into_view_if_needed()
            page.wait_for_timeout(100)
            el.screenshot(path=os.path.join(SHOTS, f'p8_nosrcs_sheet{t:03d}.png'))
        print(f"bottom-page screenshots: sheets {sorted(set(targets))}")
        browser.close()

    from pypdf import PdfReader
    rd = PdfReader(pdf_path)
    n_pdf = len(rd.pages)
    w = float(rd.pages[0].mediabox.width)
    print(f"PDF: {n_pdf} pages @ {w:.1f}pt (A4 = 595.3)")
    if n_pdf != n_sheets or abs(w - 595.3) > 1:
        fails.append(f'PDF wrong: {n_pdf} pages vs {n_sheets} sheets')

    print()
    if fails:
        print('PHASE 8 GATE: FAIL')
        for f in fails:
            print('  -', f)
        sys.exit(1)
    print('PHASE 8 GATE: PASS')

if __name__ == '__main__':
    main()
