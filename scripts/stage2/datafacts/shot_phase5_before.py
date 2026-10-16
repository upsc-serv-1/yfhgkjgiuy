#!/usr/bin/env python3
"""shot_phase5_before.py — BEFORE screenshots of the 5 densest cards (Phase 5 gate)."""
from playwright.sync_api import sync_playwright

FILE = '/home/z/my-project/ebook/final_data_facts.html'
OUT = '/home/z/my-project/ebook/scripts/stage2/datafacts/shots/'
TARGETS = {   # sheet index (1-based) -> name
    20: 'p5_before_general_gov',
    25: 'p5_before_social_sector',
    62: 'p5_before_disaster_stats',
    88: 'p5_before_climate_change',
    93: 'p5_before_energy',
}

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={'width': 900, 'height': 1200}, device_scale_factor=1.5)
    page.goto('file://' + FILE)
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(1200)
    sheets = page.query_selector_all('.sheet')
    for idx, name in TARGETS.items():
        el = sheets[idx - 1]
        el.scroll_into_view_if_needed()
        page.wait_for_timeout(150)
        el.screenshot(path=f'{OUT}{name}.png')
        print(f'shot {name}: sheet {idx}')
    browser.close()
print('done')
