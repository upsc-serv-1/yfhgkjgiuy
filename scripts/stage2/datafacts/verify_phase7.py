#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_phase7.py — Phase 7 gate: highlighting persisted in the JSON schema.

The convention: {{hl}}…{{/hl}} inside content_markdown (documented in
parse_data.py docstring, highlight_json.py header, DESIGN.md §14).
Renders as <b class="hl"> (bold + orange). Markers are STYLING, not text
(visible_text strips them; the verbatim QA gate is marker-blind).

Tests:
  A. MARKER WELL-FORMEDNESS: per card — equal open/close counts, no nesting,
     no markers inside <table> spans or heading/label lines.
  B. PERSISTENCE (JSON-only regeneration): wipe df_book_map.json + built
     HTML partials, rebuild PURELY from inputs/updated_data.json → identical
     highlight count (markers → b.hl 1:1) and QA green. No manual HTML.
  C. LEGACY BACKWARD-COMPAT: build with the pre-phase6 JSON (no markers) →
     0 b.hl, 0 '{{' residue, QA green — unmarked content renders unchanged.
     (Restores the marked JSON + rebuilds after.)
  D. DOCUMENTATION: DESIGN.md §14 carries the marker convention.
"""
import os, re, sys, json, shutil, subprocess

ROOT = '/home/z/my-project/ebook'
DF = os.path.join(ROOT, 'scripts/stage2/datafacts')
JSON_IN = os.path.join(ROOT, 'inputs', 'updated_data.json')
JSON_PRE6 = os.path.join(ROOT, 'inputs', 'updated_data.pre-phase6.json')

def run(cmd):
    r = subprocess.run(cmd, cwd=ROOT, shell=True, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr

def qa_green():
    rc, out = run('python scripts/stage2/datafacts/qa_check_df.py')
    return rc == 0 and 'ALL CHECKS GREEN' in out, out[-500:]

def main():
    fails = []
    data = json.load(open(JSON_IN))
    doc = open(os.path.join(ROOT, 'final_data_facts.html')).read()

    # ---- A. marker well-formedness ----
    bad_balance, nested, bad_ctx = [], [], []
    for c in data:
        md = c['content_markdown']
        if md.count('{{hl}}') != md.count('{{/hl}}'):
            bad_balance.append(c['card_title'])
        if re.search(r'\{\{hl\}\}[^{]*\{\{hl\}\}', md):
            nested.append(c['card_title'])
        for ln in md.split('<br>'):
            s = ln.strip()
            if s.startswith(('<table', '<b><u>', '• ')) and '{{hl}}' in ln:
                bad_ctx.append((c['card_title'], s[:40]))
    print(f"marker balance: {len(bad_balance)} bad | nested: {len(nested)} | "
          f"in table/heading/label lines: {len(bad_ctx)}")
    if bad_balance: fails.append(f'unbalanced markers: {bad_balance[:5]}')
    if nested: fails.append(f'nested markers: {nested[:5]}')
    if bad_ctx: fails.append(f'markers in structural lines: {bad_ctx[:5]}')

    n_markers = sum(c['content_markdown'].count('{{hl}}') for c in data)
    n_hl = doc.count('<b class="hl">')
    print(f"markers: {n_markers} | rendered: {n_hl}")

    # ---- B. persistence: JSON-only regeneration ----
    os.remove(os.path.join(DF, 'df_book_map.json'))
    for f in os.listdir(os.path.join(ROOT, 'src', 'datafacts')):
        if f.startswith('df_') and f.endswith('.html'):
            os.remove(os.path.join(ROOT, 'src', 'datafacts', f))
    rc, out = run('python scripts/stage2/datafacts/parse_data.py && '
                  'python scripts/stage2/datafacts/build_book.py')
    if rc != 0:
        fails.append('rebuild failed: ' + out[-300:])
    doc2 = open(os.path.join(ROOT, 'final_data_facts.html')).read()
    n_hl2 = doc2.count('<b class="hl">')
    same = doc2 == doc
    print(f"persistence: rebuilt b.hl = {n_hl2} (expect {n_markers}) | "
          f"byte-identical to prior build: {same}")
    if n_hl2 != n_markers:
        fails.append(f'persistence broken: {n_hl2} rendered vs {n_markers} markers')
    ok, out = qa_green()
    print('QA after regeneration:', 'GREEN' if ok else 'FAIL')
    if not ok:
        fails.append('QA not green after regeneration: ' + out[-300:])

    # ---- C. legacy backward-compat (no-marker JSON) ----
    if os.path.exists(JSON_PRE6):
        shutil.copyfile(JSON_IN, JSON_IN + '.phase7-keep')
        try:
            shutil.copyfile(JSON_PRE6, JSON_IN)
            rc, out = run('python scripts/stage2/datafacts/parse_data.py && '
                          'python scripts/stage2/datafacts/build_book.py')
            doc3 = open(os.path.join(ROOT, 'final_data_facts.html')).read()
            n_hl3 = doc3.count('<b class="hl">')
            n_res = doc3.count('{{')
            ok3, out3 = qa_green()
            print(f"legacy build: b.hl={n_hl3} | literal '{{' residue={n_res} | QA "
                  f"{'GREEN' if ok3 else 'FAIL'}")
            if n_hl3 != 0 or n_res != 0:
                fails.append(f'legacy build shows markers: b.hl={n_hl3}, residue={n_res}')
            if not ok3:
                fails.append('legacy QA: ' + out3[-300:])
        finally:
            shutil.copyfile(JSON_IN + '.phase7-keep', JSON_IN)
            os.remove(JSON_IN + '.phase7-keep')
            rc, out = run('python scripts/stage2/datafacts/parse_data.py && '
                          'python scripts/stage2/datafacts/build_book.py')
            ok, out = qa_green()
            print(f"restored marked JSON + rebuilt: b.hl={doc.count if False else open(os.path.join(ROOT, 'final_data_facts.html')).read().count('<b class=\"hl\">')} | QA {'GREEN' if ok else 'FAIL'}")
            if not ok:
                fails.append('restore QA: ' + out[-300:])
    else:
        print('pre-phase6 backup missing — legacy test skipped')

    # ---- D. documentation ----
    design = open(os.path.join(ROOT, 'DESIGN.md')).read()
    doc_ok = '{{hl}}' in design
    print('DESIGN.md documents marker convention:', doc_ok)
    if not doc_ok:
        fails.append('DESIGN.md does not document the {{hl}} convention')

    print()
    if fails:
        print('PHASE 7 GATE: FAIL')
        for f in fails:
            print('  -', f)
        sys.exit(1)
    print('PHASE 7 GATE: PASS')

if __name__ == '__main__':
    main()
