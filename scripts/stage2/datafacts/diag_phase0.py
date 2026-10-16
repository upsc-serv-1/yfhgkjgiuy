#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""diag_phase0.py — Phase 0 discovery evidence for Dr. CSE · Data & Facts
Measures, for every sheet:
  - rendered height (A4 target 1123px)
  - footer position: gap between content-end and foot-start, and foot bottom vs sheet bottom
  - whether the sheet is a flex container (root-cause probe for floating footer)
  - last child before .foot (to find orphaned headings at page bottoms)
Screenshots the disclaimer + all index sheets + sheets around the Manufacturing bug.
"""
import os, json, re
from playwright.sync_api import sync_playwright

ROOT = '/home/z/my-project/ebook'
FILE = os.path.join(ROOT, 'final_data_facts.html')
SHOTS = os.path.join(ROOT, 'scripts', 'stage2', 'datafacts', 'shots')
os.makedirs(SHOTS, exist_ok=True)

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
                // content end = bottom of the last element BEFORE .foot
                let contentEnd = 0, lastBefore = null;
                for (const ch of el.children) {
                    if (ch.classList.contains('foot')) break;
                    const cr = ch.getBoundingClientRect();
                    if (cr.bottom > contentEnd) { contentEnd = cr.bottom; lastBefore = ch; }
                }
                const cs = getComputedStyle(el);
                out.push({
                    i: i+1, id: el.id || (el.dataset.ch || ''),
                    h: Math.round(r.height),
                    display: cs.display,
                    footTopInSheet: fr ? Math.round(fr.top - r.top) : null,
                    footH: fr ? Math.round(fr.height) : null,
                    gapContentToFoot: fr ? Math.round(fr.top - contentEnd) : null,
                    contentEndInSheet: Math.round(contentEnd - r.top),
                    emptyBelowFoot: fr ? Math.round(r.bottom - fr.bottom) : null,
                    lastTag: lastBefore ? lastBefore.tagName + '.' +
                             (lastBefore.className || '').split(' ').slice(0,2).join('.') : null,
                    lastText: lastBefore ? (lastBefore.textContent || '').trim().slice(0, 60) : null
                });
            });
            return out;
        }''')

        print(f"{'#':>3} {'sheet':>7} {'h':>5} {'flex?':>6} {'footTop':>7} {'gap':>5} {'empty':>5}  last-element-before-foot")
        issues = {'floating_foot': [], 'tall': [], 'short_fill': [], 'orphan_suspects': []}
        for d in data:
            flex = 'flex' if 'flex' in d['display'] else 'block'
            # footer floating mid-page: foot ends well above sheet bottom on non-cover sheets
            floating = (d['emptyBelowFoot'] or 0) > 60 and d['i'] not in (1, len(data))
            if floating:
                issues['floating_foot'].append(d['i'])
            if d['h'] > 1135:
                issues['tall'].append(d['i'])
            # fill ratio: content end vs sheet height
            fill = (d['contentEndInSheet'] or 0) / d['h'] if d['h'] else 1
            if fill < 0.55 and d['i'] not in (1, len(data)):
                issues['short_fill'].append((d['i'], round(fill, 2)))
            # orphan suspects: sheet ends with a heading-ish element
            if d['lastTag'] and re.search(r'sub-h|sec-h|sth|card-h|ssec', str(d['lastTag'])):
                issues['orphan_suspects'].append((d['i'], d['lastTag'], d['lastText']))
            print(f"{d['i']:>3} {str(d['id'])[:7]:>7} {d['h']:>5} {flex:>6} "
                  f"{str(d['footTopInSheet']):>7} {str(d['gapContentToFoot']):>5} {str(d['emptyBelowFoot']):>5}  "
                  f"{d['lastTag']} | {d['lastText']}")

        print('\n=== ISSUE SUMMARY ===')
        print('floating footer sheets (foot >60px above sheet bottom):', issues['floating_foot'])
        print('tall sheets (>1135px):', issues['tall'])
        print('under-filled sheets (content<55% height):', issues['short_fill'])
        print('orphaned-heading suspects (sheet ends with heading element):')
        for t in issues['orphan_suspects']:
            print('   ', t)

        # screenshots: disclaimer, index sheets, sheets 12-15 (Manufacturing area)
        targets = [('#fm-disclaimer', 'p0_disclaimer'), ('#ix-master', 'p0_index1'), ('#ix-title', 'p0_index1')]
        # all index sheets = sheets between disclaimer and first opener
        ix_sheets = page.evaluate('''() => {
            const sheets = [...document.querySelectorAll('.sheet')];
            const out = [];
            for (let i = 0; i < sheets.length; i++) {
                if (sheets[i].id === 'ix-master' || sheets[i].querySelector('.ix-body')) out.push(i+1);
            }
            return out;
        }''')
        print('\nindex sheets:', ix_sheets)
        for n in ix_sheets:
            targets.append((f'.sheet >> nth={n-1}', f'p0_index_{n:02d}'))
        for n in (12, 13, 14, 15):
            targets.append((f'.sheet >> nth={n-1}', f'p0_sheet_{n:02d}'))
        for sel, name in targets:
            try:
                loc = page.locator(sel).first
                loc.scroll_into_view_if_needed()
                page.wait_for_timeout(200)
                loc.screenshot(path=os.path.join(SHOTS, f'{name}.png'))
                print('shot:', name + '.png')
            except Exception as e:
                print(f'shot FAILED {name}: {str(e)[:80]}')
        browser.close()

if __name__ == '__main__':
    main()
