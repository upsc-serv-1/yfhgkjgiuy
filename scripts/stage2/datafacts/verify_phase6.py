#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_phase6.py — Phase 6 gate: exam-data highlighting (bold + orange).

Checks:
  1. TRACEABILITY: #{{hl}} markers in JSON == #<b class="hl"> in built HTML
     (every highlight traces to the source JSON, none invented in rendering);
     subject coverage: every subject with facts carries highlights.
  2. DISCIPLINE: per-card orange ratio ≤ 50% (target ≤ 40%); every hl span
     contains a digit (no junk); no hl inside tables / .sth / .sth2 / .ssec.
  3. GEOMETRY regression: sheets exactly A4, foot pinned, no orphaned headings
     (incl. .sth2), two-column .rows intact.
  4. INDEX regression: page numbers correct.
  5. SCREENSHOTS: pages spread across ≥ 10 subjects (Phase-6 checkpoint:
     15–20 pages) into shots/ for the visual 10-second scan review.
"""
import os, re, sys, json
from playwright.sync_api import sync_playwright

ROOT = '/home/z/my-project/ebook'
FILE = os.path.join(ROOT, 'final_data_facts.html')
SHOTS = os.path.join(ROOT, 'scripts/stage2/datafacts/shots')

def main():
    data = json.load(open(os.path.join(ROOT, 'inputs/updated_data.json')))
    doc = open(FILE).read()
    fails = []

    # ---- 1. traceability ----
    n_markers = sum(c['content_markdown'].count('{{hl}}') for c in data)
    n_hl = doc.count('<b class="hl">')
    print(f"markers in JSON: {n_markers} | rendered b.hl: {n_hl}")
    if n_markers != n_hl or n_hl == 0:
        fails.append(f'highlight traceability: {n_markers} markers vs {n_hl} rendered')

    # per-subject coverage from JSON
    by_sub = {}
    for c in data:
        n = c['content_markdown'].count('{{hl}}')
        by_sub.setdefault(c['subject'], [0, 0])
        by_sub[c['subject']][0] += n
        by_sub[c['subject']][1] += 1
    no_hl = [s for s, (n, _) in by_sub.items() if n == 0]
    print('subject coverage:', {s: v[0] for s, v in sorted(by_sub.items())})
    if no_hl:
        fails.append(f'subjects without any highlight: {no_hl}')

    # ---- 2. discipline ----
    # per-card ratio from JSON (visible chars inside markers vs fact rows)
    HL = re.compile(r'\{\{hl\}\}(.*?)\{\{/hl\}\}')
    over, over40 = [], []
    for c in data:
        md = c['content_markdown']
        hl_chars = sum(len(re.sub(r'<[^>]+>|\[\([^\]]*\)\]\([^)]*\)|\[[^\]]*\]\([^)]*\)', '', m.group(1)))
                       for m in HL.finditer(md))
        row_chars = 0
        for ln in md.split('<br>'):
            if re.match(r'^(?:&nbsp;)*- ', ln.strip()):
                row_chars += len(re.sub(r'<[^>]+>|\[\([^\]]*\)\]\([^)]*\)|\[[^\]]*\]\([^)]*\)|\*\*|\{\{/?hl\}\}', '', ln))
        if row_chars and hl_chars / row_chars > 0.5:
            over.append((c['card_title'], round(100*hl_chars/row_chars)))
        elif row_chars and hl_chars / row_chars > 0.4:
            over40.append((c['card_title'], round(100*hl_chars/row_chars)))
    print(f"cards over 50% cap: {over or 'none'} | 40-50%: {over40 or 'none'}")
    if over:
        fails.append(f'cards over orange cap: {over}')

    # junk spans: every hl span contains a digit
    junk = [m.group(1)[:40] for m in HL.finditer(
        ' '.join(c['content_markdown'] for c in data)) if not re.search(r'\d', m.group(1))]
    print(f"hl spans without any digit: {len(junk)} {junk[:5]}")
    if junk:
        fails.append(f'{len(junk)} highlight spans carry no digit')

    # no hl in tables / headings (built HTML structure scan)
    tbl_hl = len(re.findall(r'<div class="tblwrap">(?:(?!</div>).)*?<b class="hl">', doc, re.S))
    head_hl = len(re.findall(r'<div class="st(h|h2|sec)">[^<]*<b class="hl">', doc))
    print(f"hl inside tables: {tbl_hl} | inside headings: {head_hl}")
    if tbl_hl or head_hl:
        fails.append(f'hl in wrong context: {tbl_hl} tables, {head_hl} headings')

    # ---- 3+4. browser geometry + index + screenshots ----
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
                    footGap: fr ? Math.round(r.bottom - fr.bottom) : null,
                    lastCls: lastBefore ? (lastBefore.className || '').toString() : '',
                    nHl: el.querySelectorAll('b.hl').length,
                    sub: el.getAttribute('data-ch') || el.id || ''});
            });
            return out;
        }''')
        tall = [d['i'] for d in data_dom if d['h'] > 1125 or d['w'] != 794]
        badfoot = [d['i'] for d in data_dom if d['footGap'] is not None and d['footGap'] != 24]
        orph = [d['i'] for d in data_dom
                if re.search(r'sub-h|sec-h|ssec|card-h|ix-ch|ix-sec', d['lastCls'])
                or re.search(r'^sth2?$', d['lastCls'].strip())]
        print(f"sheets: {len(data_dom)} | non-A4 {tall or 'none'} | bad-foot {badfoot or 'none'} | orphans {orph or 'none'}")
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

        # screenshots across subjects: pick the first content sheet of each ch-N
        # with the most highlights, plus dense pages
        sheets = page.query_selector_all('.sheet')
        by_ch = {}
        for d in data_dom:
            if d['nHl'] > 0 and str(d['sub']).startswith('ch-'):
                by_ch.setdefault(d['sub'], []).append((d['nHl'], d['i']))
        picked = sorted((max(v)[1], k) for k, v in by_ch.items())
        n_shot = 0
        for idx, ch in picked:
            name = f'p6_hl_{ch}'
            el = sheets[idx - 1]
            el.scroll_into_view_if_needed()
            page.wait_for_timeout(100)
            el.screenshot(path=os.path.join(SHOTS, f'{name}.png'))
            n_shot += 1
        print(f"highlight screenshots: {n_shot} sheets across {len(picked)} subjects "
              f"(sheet #s: {[i for i, _ in picked]})")

        # 10-second scan visual density stat: orange share per shot sheet
        browser.close()

    print()
    if fails:
        print('PHASE 6 GATE: FAIL')
        for f in fails:
            print('  -', f)
        sys.exit(1)
    print('PHASE 6 GATE: PASS')

if __name__ == '__main__':
    main()
