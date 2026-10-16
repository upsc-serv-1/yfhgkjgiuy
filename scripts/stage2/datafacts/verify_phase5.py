#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_phase5.py — Phase 5 gate: JSON restructuring (one fact per bullet,
grouped subheadings, clean nested levels).

Checks:
  1. STRUCTURE (built HTML): .sth2 count == book-map minor count; every minor
     label followed by at least one row on the same sheet fragment chain (no
     orphaned labels at sheet bottoms — DOM last-element scan);
     two-column .rows preserved; level census (no deeper than l3 except rare).
  2. TEXT: no '###' artifacts, no &lt;b&gt; escaped-tag leaks (already in QA
     residue, re-asserted here); verbatim gate green (qa_check_df).
  3. GEOMETRY regression (browser): all sheets exactly 794×1123, foot pinned
     24px on every sheet, no DOM orphans (sub-h/sec-h/sth/sth2/ssec/card-h
     never the last element before .foot).
  4. INDEX regression: every index page number still matches stamped position.
  5. PDF: Playwright print → exactly len(sheets) A4 pages.
  6. AFTER screenshots of the 5 densest cards (for before/after review).
"""
import os, re, sys, json
from playwright.sync_api import sync_playwright

ROOT = '/home/z/my-project/ebook'
FILE = os.path.join(ROOT, 'final_data_facts.html')
BM = json.load(open(os.path.join(ROOT, 'scripts/stage2/datafacts/df_book_map.json')))
SHOTS = os.path.join(ROOT, 'scripts/stage2/datafacts/shots')

def main():
    doc = open(FILE).read()
    fails = []

    # ---- 1. structure ----
    n_minor_bm = sum(1 for c in BM['cards_flat'] for b in c['blocks'] if b['kind'] == 'minor')
    n_sth2 = doc.count('<div class="sth2">')
    print(f"minor labels: book map {n_minor_bm} | rendered .sth2 {n_sth2}")
    if n_sth2 != n_minor_bm:
        fails.append(f'sth2 count mismatch {n_sth2} != {n_minor_bm}')

    # level census
    lv = {f'l{i}': doc.count(f'<div class="row l{i}">') for i in range(6)}
    print('row level census:', lv)
    if lv['l4'] + lv['l5'] > 0:
        fails.append(f"unexpected deep nesting: {lv['l4']} l4 + {lv['l5']} l5 rows")

    # two-column rows preserved
    if '.rows{columns:2' not in doc.replace(' ', ''):
        fails.append('two-column .rows rule missing')

    # ---- 2. text hygiene (re-assert; QA already gates) ----
    if '###' in doc:
        fails.append('### artifact present in built HTML')
    if '&lt;b&gt;' in doc:
        fails.append('escaped <b> tag leak present')

    # ---- 3+4. browser: geometry, orphans, index numbers ----
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
                out.push({i: i+1, w: Math.round(r.width), h: Math.round(r.height),
                    fill: Math.round(100*(contentEnd - r.top)/r.height),
                    footGap: fr ? Math.round(r.bottom - fr.bottom) : null,
                    lastCls: lastBefore ? (lastBefore.className || '').toString() : ''});
            });
            return out;
        }''')
        tall = [d['i'] for d in data if d['h'] > 1125 or d['w'] != 794]
        badfoot = [d['i'] for d in data if d['footGap'] is not None and d['footGap'] != 24]
        dom_orphans = [d['i'] for d in data
                       if re.search(r'sub-h|sec-h|sth2?$|ssec|card-h|ix-ch|ix-sec',
                                    re.sub(r'\s*\S*\s*$', '', d['lastCls']))]
        print(f"sheets: {len(data)} | non-A4 {tall or 'none'} | bad-foot {badfoot or 'none'} | "
              f"DOM orphans {dom_orphans or 'none'}")
        if tall: fails.append(f'non-A4 sheets: {tall[:10]}')
        if badfoot: fails.append(f'foot not pinned: {badfoot[:10]}')
        if dom_orphans: fails.append(f'orphaned headings: {dom_orphans[:10]}')

        # every .sth2 label followed by a row OR another heading on the same
        # sheet (nested label runs like 'Pain Points:' → 'Higher Education:' →
        # rows are legitimate; a heading must simply never be the LAST element)
        orphan_lbl = page.evaluate('''() => {
            const bad = [];
            document.querySelectorAll('.sheet').forEach((sh, i) => {
                const els = [...sh.querySelectorAll('.sth2, .row, .sth, .ssec, .card, .foot')];
                els.forEach((el, k) => {
                    if (el.classList.contains('sth2')) {
                        const next = els[k+1];
                        const ok = next && (next.classList.contains('row') ||
                                            next.classList.contains('sth2') ||
                                            next.classList.contains('sth') ||
                                            next.classList.contains('ssec'));
                        if (!ok) bad.push({sheet: i+1, label: el.textContent.slice(0,40)});
                    }
                });
            });
            return bad;
        }''')
        print(f"sth2 labels without following content (same sheet): {len(orphan_lbl)}")
        for o in orphan_lbl[:5]:
            print('   ', o)
        if orphan_lbl:
            fails.append(f'{len(orphan_lbl)} .sth2 labels not followed by content on the same sheet')

        # index page-number accuracy (regression)
        anchor_page = page.evaluate('''() => {
            const m = {};
            const sheets = [...document.querySelectorAll('.sheet')];
            sheets.forEach((sh, i) => {
                // the sheet's OWN id (opener pt-gsN / subject ch-N) counts too —
                // querySelectorAll on sh matches descendants only
                const ids = [sh.id, ...[...sh.querySelectorAll('[id]')].map(e => e.id)];
                ids.forEach(id => {
                    if (!id) return;
                    const key = id.replace(/^card-/, '');
                    if (!(key in m)) m[key] = i + 1;
                });
            });
            return m;
        }''')
        bad_pg = page.evaluate('''(anchorPage) => {
            const bad = [];
            let n = 0;
            // pair each <a> with the .pg span that IMMEDIATELY follows it
            // (a line may carry several card links, each with its own .pg)
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
        print(f"index page numbers checked: {bad_pg['n']} | mismatches: {len(bad_pg['bad'])}")
        for b in bad_pg['bad'][:8]:
            print('   MISMATCH', b)
        if bad_pg['bad'] or bad_pg['n'] < 80:
            fails.append(f"index page numbers wrong: {len(bad_pg['bad'])} mismatches")

        # fills report
        fills = [d['fill'] for d in data if d['footGap'] is not None]
        print(f"sheet fills: min {min(fills)}% median {sorted(fills)[len(fills)//2]}% "
              f"max {max(fills)}% | under-40% sheets: "
              f"{[d['i'] for d in data if d['footGap'] is not None and d['fill'] < 40] or 'none'}")

        # ---- 5. PDF page count ----
        pdf_path = os.path.join(SHOTS, 'phase5_check.pdf')
        page.pdf(path=pdf_path, format='A4', print_background=True,
                 margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        # ---- 6. AFTER screenshots ----
        sheets = page.query_selector_all('.sheet')
        targets = {}
        for i, sh_html in enumerate(
                re.findall(r'<div class="sheet[^"]*"[^>]*>.*?(?=<div class="sheet|<a class="to-ix|</body>)',
                           doc, re.S), start=1):
            for want, name in (('General', 'p5_after_general_gov'), ('Social Sector', 'p5_after_social_sector'),
                               ('Disaster Stats', 'p5_after_disaster_stats'),
                               ('Climate Change', 'p5_after_climate_change'), ('Energy', 'p5_after_energy')):
                if f'<h4>{want}</h4>' in sh_html:
                    targets.setdefault(name, i)
        for name, i in sorted(targets.items(), key=lambda kv: kv[1]):
            el = sheets[i - 1]
            el.scroll_into_view_if_needed()
            page.wait_for_timeout(120)
            el.screenshot(path=os.path.join(SHOTS, f'{name}.png'))
            print(f'shot {name}: sheet {i}')
        browser.close()

    # PDF page count via pypdf
    try:
        from pypdf import PdfReader
        n_pdf = len(PdfReader(pdf_path).pages)
        w = float(PdfReader(pdf_path).pages[0].mediabox.width)
        print(f"PDF: {n_pdf} pages, first page {w:.1f}pt (A4 = 595.3)")
        if n_pdf != len(data) or abs(w - 595.3) > 1:
            fails.append(f'PDF wrong: {n_pdf} pages vs {len(data)} sheets, width {w}')
    except ImportError:
        print('pypdf not available — skipping PDF page count (Playwright emitted OK)')

    print()
    if fails:
        print('PHASE 5 GATE: FAIL')
        for f in fails:
            print('  -', f)
        sys.exit(1)
    print('PHASE 5 GATE: PASS')

if __name__ == '__main__':
    main()
