#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""measure_df.py — headless verification for Dr. CSE · Data & Facts
  1. every .sheet rendered height <= 1135px (A4 1123 + rounding slack)
  2. no horizontal overflow inside sheets (content wider than the sheet box)
  3. click-through: index link -> card anchor lands in viewport
  4. screenshots of key pages (cover, disclaimer, index, opener, subject,
     continuation card, table cards) for visual review
Usage: python scripts/stage2/datafacts/measure_df.py
"""
import os
import sys
import json
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
FILE = os.path.join(ROOT, 'final_data_facts.html')
BM = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'df_book_map.json')))
SHOTS = os.path.join(ROOT, 'scripts', 'stage2', 'datafacts', 'shots')
os.makedirs(SHOTS, exist_ok=True)

MAX_H = 1135  # A4 @96dpi = 1123px + slack

def main():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={'width': 900, 'height': 1400})
        page.goto('file://' + FILE)
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(1200)  # webfont settle
        # deterministic anchor jumps for click-through checks (no smooth animation)
        page.add_style_tag(content='html{scroll-behavior:auto!important}')

        # ---- 1. sheet heights + 2. overflow ----
        data = page.evaluate('''() => {
            const out = [];
            document.querySelectorAll('.sheet').forEach((el, i) => {
                const r = el.getBoundingClientRect();
                // horizontal overflow: any child wider than the sheet content box
                let hOver = 0;
                el.querySelectorAll('*').forEach(ch => {
                    const cr = ch.getBoundingClientRect();
                    if (cr.width && cr.right > r.right + 1) hOver = Math.max(hOver, cr.right - r.right);
                });
                let id = el.id || (el.dataset.ch ? el.dataset.ch : '');
                out.push({i: i+1, id, h: Math.round(r.height), w: Math.round(r.width), hOver: Math.round(hOver)});
            });
            return out;
        }''')
        over_h = [d for d in data if d['h'] > MAX_H]
        over_w = [d for d in data if d['hOver'] > 2]
        heights = sorted(d['h'] for d in data)
        print(f"sheets: {len(data)} | height min/median/max: "
              f"{heights[0]}/{heights[len(heights)//2]}/{heights[-1]}px")
        print(f"sheets over {MAX_H}px: {len(over_h)}")
        for d in over_h[:12]:
            print(f"   TALL  sheet {d['i']:3d} [{d['id']}] {d['h']}px")
        print(f"sheets with horizontal overflow: {len(over_w)}")
        for d in over_w[:12]:
            print(f"   WIDE  sheet {d['i']:3d} [{d['id']}] +{d['hOver']}px")

        # ---- 3. click-through ----
        # any index link to the EMERGENCY card (index spans several sheets)
        target = page.locator('a[href="#card-GS2-POL-0006"]').first
        target.scroll_into_view_if_needed()
        target.click()
        page.wait_for_timeout(600)
        pos = page.evaluate('''() => {
            const el = document.getElementById('card-GS2-POL-0006');
            const r = el.getBoundingClientRect();
            return {top: Math.round(r.top), visible: r.top >= 0 && r.top < window.innerHeight};
        }''')
        print(f"click-through index link -> #card-GS2-POL-0006: top={pos['top']} visible={pos['visible']}")

        # INDEX floating button from a deep sheet
        page.evaluate("document.querySelector('#card-GS3-ECO-0008').scrollIntoView()")
        page.wait_for_timeout(400)
        page.click('.to-ix')
        page.wait_for_timeout(600)
        ix_top = page.evaluate('''() => {
            const el = document.getElementById('ix-title');
            return Math.round(el.getBoundingClientRect().top);
        }''')
        print(f"floating INDEX button -> #ix-title: top={ix_top}")

        # ---- 4. screenshots ----
        # subject anchors from the book map (POLITY, INDIAN ECONOMY)
        anchor_of = {}
        ch_n = 0
        for p in BM['tree']:
            for s in p['subjects']:
                ch_n += 1
                anchor_of[s['key']] = f'ch-{ch_n}'
        pol_anchor = anchor_of.get('POLITY', 'ch-1')
        shots = [
            ('cover', 'div.sheet.p1 >> nth=0'),
            ('disclaimer', '#fm-disclaimer'),
            ('index1', '#ix-master'),
            ('opener_gs2', '#pt-gs2'),
            ('subject_polity', f'div.sheet#{pol_anchor}'),
            ('card_emergency', '#card-GS2-POL-0006'),
            ('card_infra_tables', '#card-GS3-ECO-0008'),
            ('card_continuation', 'article.card.cont-art >> nth=0'),
        ]
        for name, sel in shots:
            loc = page.locator(sel).first
            try:
                loc.scroll_into_view_if_needed()
                page.wait_for_timeout(250)
                loc.screenshot(path=os.path.join(SHOTS, f'{name}.png'))
                print(f'shot: {name}.png')
            except Exception as e:
                print(f'shot FAILED: {name} — {type(e).__name__}: {str(e)[:90]}')

        browser.close()
        if over_h or over_w:
            print('\nRESULT: HEIGHT/OVERFLOW ISSUES FOUND')
            sys.exit(1)
        print('\nRESULT: ALL SHEETS OK')

if __name__ == '__main__':
    main()
