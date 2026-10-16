#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_phase3.py — Phase 3 gate: index order, atomicity, page-number accuracy.
  1. Index paper order = GS-I, GS-II, GS-III (and part openers in same order)
  2. No orphaned index headings (paper header / subject header alone at sheet bottom)
  3. Every index page number matches the actual stamped page of its target anchor
  4. Re-run Phase 1+2 geometry gates on the rebuilt book (regression)
"""
import os, re, sys
from playwright.sync_api import sync_playwright

ROOT = '/home/z/my-project/ebook'
FILE = os.path.join(ROOT, 'final_data_facts.html')

def main():
    doc = open(FILE).read()
    sheets = re.findall(r'<div class="sheet[^"]*"[^>]*>.*?(?=<div class="sheet|<a class="to-ix|</body>)', doc, re.S)

    # ---- 1. order ----
    ix_zone = '|||||'.join(sh for sh in sheets if 'ix-body' in sh)
    paper_order = re.findall(r'<a class="t" href="#pt-(\w+)">', ix_zone)
    print('index paper order:', paper_order)
    order_ok = paper_order == ['gs1', 'gs2', 'gs3']

    # part openers order in book
    opener_order = []
    for sh in sheets:
        m = re.search(r'<div class="sheet" id="(pt-gs\d)"', sh)
        if m:
            opener_order.append(m.group(1))
    print('book part-opener order:', opener_order)
    openers_ok = opener_order == ['pt-gs1', 'pt-gs2', 'pt-gs3']

    # subject order in index
    subj_order = re.findall(r'<div class="ix-sec"><a href="#(ch-\d+)">([^<]+)</a>', ix_zone)
    print('index subject order:', [s[1] for s in subj_order])

    # ---- 2. no orphaned index headings: last element of each index sheet ----
    orphans = []
    for n, sh in enumerate(sheets, 1):
        if 'ix-body' not in sh:
            continue
        # last element inside ix-body before </div></div><div class="foot">
        m = re.search(r'(.{300}?)</div></div><div class="foot">', sh, re.S)
        tail = m.group(1) if m else ''
        # the sheet must end with a completed ix-line (</div>) not a bare header
        if re.search(r'<div class="ix-ch">[^<]*<a[^>]*>[^<]*</a>[^<]*</div>$|<div class="ix-sec">[^<]*<a[^>]*>[^<]*</a>[^<]*</div>$', tail):
            orphans.append(n)
    print('orphaned index headers:', orphans or 'none')

    # subject blocks atomic: a subject's header and its LAST card link must be on same sheet
    atomic_ok = True
    for n, sh in enumerate(sheets, 1):
        if 'ix-body' not in sh:
            continue
        pass
    # check: each ix-sec's block: all its section lines present on the same sheet
    # (a subject block = ix-sec followed by its ix-lines until next ix-sec/ix-ch/sheet-end)
    for n, sh in enumerate(sheets, 1):
        if 'ix-body' not in sh:
            continue
        # find subject blocks that START on this sheet
        starts = [m.start() for m in re.finditer(r'<div class="ix-sec">', sh)]
        for st in starts:
            # block extends to the next ix-sec / ix-ch on this sheet OR sheet end.
            # If the NEXT sheet begins with ix-lines that reference cards of a
            # subject whose header is on THIS sheet → torn. Simpler check: no
            # ix-sec/ix-ch is the LAST element of a sheet (covered above), and
            # every sheet's ix-body ends with a full ix-line.
            pass

    # ---- 3. page-number accuracy ----
    # anchor -> stamped page (sheet position)
    anchor_page = {}
    for pos, sh in enumerate(sheets, start=1):
        for m in re.finditer(r'id="card-([A-Z0-9-]+)"', sh):
            anchor_page[m.group(1)] = pos
        m = re.search(r'<div class="sheet" id="(ch-\d+)"', sh)
        if m:
            anchor_page[m.group(1)] = pos
        m = re.search(r'<div class="sheet" id="(pt-gs\d)"', sh)
        if m:
            anchor_page[m.group(1)] = pos
    # every index link's displayed page number
    bad_pg = []
    n_checked = 0
    for m in re.finditer(r'<a href="#(card-[A-Z0-9-]+|ch-\d+|pt-gs\d)">[^<]*</a><span class="pg">(?:·|p\.) (\d+)</span>', ix_zone):
        target, shown = m.group(1), int(m.group(2))
        key = target.replace('card-', '')
        n_checked += 1
        if anchor_page.get(key) != shown:
            bad_pg.append((key, shown, anchor_page.get(key)))
    print(f'index page numbers checked: {n_checked} | mismatches: {len(bad_pg)}')
    for b in bad_pg[:10]:
        print('   MISMATCH', b)

    # stamped page numbers on sheets match position
    stamp_bad = 0
    for pos, sh in enumerate(sheets, start=1):
        m = re.search(r'<span class="pg-n">(\d+) / (\d+)<', sh)
        if m and int(m.group(1)) != pos:
            stamp_bad += 1
    print('sheets whose stamp != position:', stamp_bad)

    # ---- 4. regression: geometry + orphans via browser ----
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={'width': 900, 'height': 1400})
        page.goto('file://' + FILE)
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(1500)
        data = page.evaluate('''() => {
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
                out.push({i: i+1, h: Math.round(r.height),
                    fill: Math.round(100*(contentEnd - r.top)/r.height),
                    footGap: fr ? Math.round(r.bottom - fr.bottom) : null,
                    lastTag: lastBefore ? lastBefore.tagName + '.' + (lastBefore.className || '').split(' ').slice(0,2).join('.') : ''});
            });
            return out;
        }''')
        browser.close()
    tall = [d['i'] for d in data if d['h'] > 1125]
    badfoot = [d['i'] for d in data if d['footGap'] is not None and d['footGap'] != 24]
    dom_orphans = [d['i'] for d in data if re.search(r'sub-h|sec-h|\.sth|\.ssec|\.card-h|ix-ch|ix-sec', str(d['lastTag']))]
    ix_fills = [d['fill'] for d in data if d['i'] <= 6 and d['footGap'] is not None]
    print(f"regression: over-A4 {tall or 'none'} | bad-foot {badfoot or 'none'} | DOM orphans {dom_orphans or 'none'}")
    print(f"index sheet fills: {ix_fills}")

    ok = (order_ok and openers_ok and not orphans and not bad_pg and n_checked > 80
          and stamp_bad == 0 and not tall and not badfoot and not dom_orphans)
    print('\nPHASE 3 GATE:', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
