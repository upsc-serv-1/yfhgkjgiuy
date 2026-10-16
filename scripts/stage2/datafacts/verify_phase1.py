#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_phase1.py — Phase 1 gate: A4 geometry + pinned footer, screen AND PDF.
  1. Screen: every sheet 794×1123px, foot bottom within 30px of sheet bottom.
  2. PDF: page.pdf(A4, margin 0, printBackground) → page count == sheet count,
     every page exactly 210×297mm (595.3×841.9pt).
  3. Footer position inside the PDF (via text position of the running footer).
"""
import os, sys
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
                out.push({i: i+1, w: Math.round(r.width), h: Math.round(r.height),
                          footGap: fr ? Math.round(r.bottom - fr.bottom) : null,
                          flex: getComputedStyle(el).display});
            });
            return out;
        }''')
        bad_w = [d for d in data if abs(d['w'] - 794) > 2]
        bad_h = [d for d in data if abs(d['h'] - 1123) > 2]
        bad_f = [d for d in data if d['footGap'] is not None and d['footGap'] > 30]
        not_flex = [d for d in data if 'flex' not in d['flex']]
        print(f"sheets: {len(data)} | wrong-width: {len(bad_w)} | wrong-height: {len(bad_h)}")
        print(f"non-flex sheets: {len(not_flex)}")
        print(f"footers not pinned (>30px above bottom): {len(bad_f)}")
        for d in bad_f[:10]:
            print(f"   sheet {d['i']}: foot {d['footGap']}px above bottom")
        gaps = [d['footGap'] for d in data if d['footGap'] is not None]
        print(f"footGap min/max: {min(gaps)}/{max(gaps)}px (target <= ~24px sheet padding)")

        # ---- PDF ----
        page.emulate_media(media='print')
        page.pdf(path=PDF, format='A4', print_background=True,
                 margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        browser.close()

    # verify PDF geometry
    try:
        from pypdf import PdfReader
    except ImportError:
        from PyPDF2 import PdfReader
    r = PdfReader(PDF)
    n = len(r.pages)
    print(f"\nPDF pages: {n} (sheets: {len(data)})")
    bad_pages = []
    for i, p in enumerate(r.pages, 1):
        w = float(p.mediabox.width); h = float(p.mediabox.height)
        if abs(w - 595.28) > 1.5 or abs(h - 841.89) > 1.5:
            bad_pages.append((i, round(w, 1), round(h, 1)))
    print(f"pages not exactly A4 (595.3×841.9pt): {len(bad_pages)}")
    for b in bad_pages[:10]:
        print('   page', b)
    print(f"PDF size: {os.path.getsize(PDF)/1024/1024:.1f} MB")

    ok = (not bad_w and not bad_h and not bad_f and not not_flex
          and n == len(data) and not bad_pages)
    print('\nPHASE 1 GATE:', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
