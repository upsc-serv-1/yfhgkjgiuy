#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_phase2.py — Phase 2 gate: keep-with-next, no orphans, no overflow,
plus estimator calibration (data-est vs real content height).
  GATES:
  1. 0 orphaned headings (DOM last-element check)
  2. every sheet exactly A4 (<=1123px +2 rounding)
  3. footer pinned (24px) everywhere
  4. Manufacturing Sector: sub-h band + SECONDARY SECTOR card on same sheet
  5. PDF pages == sheets, all A4
  CALIBRATION: report real-content-height / data-est ratio stats.
"""
import os, re, sys, statistics
from playwright.sync_api import sync_playwright

ROOT = '/home/z/my-project/ebook'
FILE = os.path.join(ROOT, 'final_data_facts.html')
PDF = os.path.join(ROOT, 'final_data_facts.pdf')

def main():
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
                out.push({i: i+1, h: Math.round(r.height), est: +(el.dataset.est || 0),
                          fill: Math.round(100*(contentEnd - r.top)/r.height),
                          footGap: fr ? Math.round(r.bottom - fr.bottom) : null,
                          lastTag: lastBefore ? lastBefore.tagName + '.' +
                                   (lastBefore.className || '').split(' ').slice(0,2).join('.') : '',
                          lastText: lastBefore ? (lastBefore.textContent || '').trim().slice(0, 60) : ''});
            });
            return out;
        }''')

        orphans = [d for d in data if re.search(r'sub-h|sec-h|\.sth|\.ssec|\.card-h', str(d['lastTag']))]
        tall = [d for d in data if d['h'] > 1125]
        badfoot = [d['i'] for d in data if d['footGap'] is not None and d['footGap'] != 24]

        # Manufacturing test case
        mfg = page.evaluate('''() => {
            const sheets = [...document.querySelectorAll('.sheet')];
            for (const sh of sheets) {
                const band = [...sh.querySelectorAll('.sub-h h3')].find(h => h.textContent.trim() === 'Manufacturing Sector');
                if (band) {
                    const card = sh.querySelector('#card-GS3-ECO-0002');
                    return {same: !!card, cardVisibleTop: card ? Math.round(card.getBoundingClientRect().top - sh.getBoundingClientRect().top) : null};
                }
            }
            return {same: false};
        }''')

        # calibration on packer sheets only (data-est present)
        cal = [d for d in data if d['est'] > 0]
        ratios = [ (d['fill']/100*1123 - 84) / d['est'] for d in cal ]  # 84px chrome approx
        rstats = (round(min(ratios),3), round(statistics.median(ratios),3), round(max(ratios),3))

        print(f"sheets: {len(data)} | orphans: {len(orphans)} | over-A4: {len(tall)} | bad-foot: {len(badfoot)}")
        for d in tall: print('   TALL', d['i'], d['h'], d['lastTag'], d['lastText'][:40])
        print(f"Manufacturing Sector band + SECONDARY SECTOR card same sheet: {mfg['same']} (card top {mfg.get('cardVisibleTop')}px in sheet)")
        fills = [d['fill'] for d in data if d['footGap'] is not None]
        print(f"fills: min {min(fills)}% / median {statistics.median(fills)}% / max {max(fills)}%")
        print(f"est-calibration real/est (chrome-adjusted): min/med/max = {rstats}")

        # PDF
        page.emulate_media(media='print')
        page.pdf(path=PDF, format='A4', print_background=True,
                 margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        browser.close()

    from pypdf import PdfReader
    r = PdfReader(PDF)
    bad_pages = [(i+1, round(float(p.mediabox.width),1), round(float(p.mediabox.height),1))
                 for i, p in enumerate(r.pages)
                 if abs(float(p.mediabox.width) - 595.28) > 1.5 or abs(float(p.mediabox.height) - 841.89) > 1.5]
    print(f"PDF: {len(r.pages)} pages (sheets {len(data)}) | non-A4 pages: {len(bad_pages)}")

    ok = (not orphans and not tall and not badfoot and mfg['same']
          and len(r.pages) == len(data) and not bad_pages)
    print('\nPHASE 2 GATE:', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
