#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""qa_check_df.py — QA gate for Dr. CSE · Data & Facts (final_data_facts.html)
Checks:
  1. card anchors: all 83 cards present with unique ids
  2. internal links: every href="#..." target exists
  3. external links: 556 source links survive as <a href="http..."> (+ sources panel links)
  4. verbatim: every visible text line of every source card appears in the built HTML
  5. residue: no raw markdown (**, ](http), entities (&nbsp; &rarr; ...), <br>, <!--, 🢥
  6. tag balance: .card/.rows/<article>/<div> open-close balance across the document
  7. no count-statistics strings
  8. chrome: every sheet has topbar + foot; page numbers stamped NNN / TTT
"""
import json, re, sys, os
import html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
BM = json.load(open(os.path.join(HERE, 'df_book_map.json')))
DOC = open(os.path.join(ROOT, 'final_data_facts.html')).read()
# Tag-balance / residue checks must look at MARKUP ONLY — the inlined <style>
# block contains the literal string '<table>' inside a CSS comment, which is
# not parsed as an element by browsers.
MARKUP = re.sub(r'<style>.*?</style>', '', DOC, flags=re.S)

fails, warns = [], []

def check(name, ok, detail=''):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ''))
    if not ok:
        fails.append(f"{name}: {detail}")

# ---------- 1. card anchors ----------
cards = BM['cards_flat']
ids = re.findall(r'<article class="card[^"]*" id="card-([^"]+)"', DOC)
check('card anchors: 83 unique', len(ids) == 83 and len(set(ids)) == 83,
      f'{len(ids)} found, {len(set(ids))} unique')
expected_ids = {c['id'] for c in cards}
check('card ids match book map', set(ids) == expected_ids,
      f'missing: {expected_ids - set(ids) or "none"}')

# ---------- 2. internal links ----------
hrefs = re.findall(r'href="#([^"]+)"', DOC)
anchor_pool = set(re.findall(r'id="([^"]+)"', DOC))
broken = sorted({h for h in hrefs if h not in anchor_pool})
check('internal links resolve', not broken, f'broken: {broken[:8] or "none"} ({len(broken)})')

# ---------- 3. external links ----------
ext = re.findall(r'<a href="https?://[^"]+"', DOC)
n_src_links = sum(r['html'].count('<a href=') for c in cards for b in c['blocks'] for r in b['rows'])
n_panel_links = sum(1 for c in cards for s in c['sources'] if s.get('url'))
check('external links: content links preserved', len(ext) >= n_src_links,
      f'{len(ext)} <a> external vs {n_src_links} content + {n_panel_links} panel expected')

# ---------- 4. verbatim visible text ----------
def norm(s):
    s = H.unescape(s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

built_text = norm(re.sub(r'<[^>]+>', ' ', DOC))
missing_lines = []
for c in cards:
    # card title
    if norm(c['title']) and norm(c['title']) not in built_text:
        missing_lines.append((c['id'], 'TITLE', c['title']))
    # block titles
    for b in c['blocks']:
        if b['title'] is not None:
            t = norm(re.sub(r'<[^>]+>', ' ', b['title']))
            if t and t not in built_text:
                missing_lines.append((c['id'], 'HEADING', t[:70]))
        for r in b['rows']:
            t = norm(re.sub(r'<[^>]+>', ' ', r['html']))
            if t and t not in built_text:
                missing_lines.append((c['id'], 'ROW', t[:70]))
check('verbatim: every source line present', not missing_lines,
      f'{len(missing_lines)} missing' + (f' e.g. {missing_lines[:3]}' if missing_lines else ''))

# ---------- 5. residue ----------
# <br> inside a protected table cell is legitimate (source line break);
# anywhere else it is residue — count on markup with table spans removed.
NO_TBL = re.sub(r'<table.*?</table>', '', MARKUP, flags=re.S)
residue = {k: NO_TBL.count(k) for k in
           ['**', '](', '&nbsp;', '<br>', '<!--', '🢥', '&rarr;', '&rupee;', '&plusmn;', '&approx;']}
residue['[ ]('] = len(re.findall(r'\[[^\]]*\]\(http', NO_TBL))
# escaped source markup leaking as VISIBLE text (class of the EMERGENCY-table bug:
# a table torn apart by a <br> split renders literal &lt;/td&gt; on the card)
leaks = re.findall(r'&lt;/?t(able|body|head|r|h|d)[^&a-z]', MARKUP)
residue['escaped-table-markup'] = len(leaks)
bad = {k: v for k, v in residue.items() if v}
check('no raw markdown / entity residue', not bad, f'found: {bad or "none"}')

# ---------- 6. tag balance ----------
def balance(tag):
    o = len(re.findall(f'<{tag}[ >]', MARKUP))
    c = len(re.findall(f'</{tag}>', MARKUP))
    return o, c

for tag in ['article', 'div', 'span', 'a', 'table', 'thead', 'tbody', 'tr']:
    o, c = balance(tag)
    check(f'tag balance <{tag}>', o == c, f'{o} open / {c} close')

# rows divs: every sheet's fragment closes properly → count "rows" opens vs closes
o_rows = MARKUP.count('<div class="rows">')
c_rows = len(re.findall(r'</div></article>', MARKUP))
conts = MARKUP.count('<div class="cont">')
check('flow-card fragments balanced', o_rows == c_rows,
      f'{o_rows} rows-open vs {c_rows} card-close; {conts} continuation strips')

# ---------- 7. no count statistics ----------
bad_stats = [s for s in ['83 cards', '83 fact', 'cards in total', 'total cards',
                         '2010 rows', 'SECTION 1 OF', 'CARDS:'] if s in DOC]
check('no card-count statistics', not bad_stats, f'found: {bad_stats or "none"}')

# ---------- 8. chrome ----------
sheets = DOC.count('<div class="sheet')
tops = DOC.count('class="topbar"')
foots = DOC.count('class="foot"')
pgs = len(re.findall(r'class="pg-n">\d{3} / \d{3}<', DOC))
check('sheet chrome', sheets == tops and foots == sheets - 2,
      f'{sheets} sheets / {tops} topbars / {foots} foots (2 covers carry no foot)')
# both covers (.p1) carry no foot → no page number; every other sheet is stamped
check('page numbers stamped', pgs == sheets - 2,
      f'{pgs} stamped of {sheets} sheets (2 covers unstamped = {sheets-2})')

# fonts + title + print css
check('branding', 'Data &amp; Facts' in DOC and 'logo_dr_cse.png' in DOC and
      'Dr. CSE — <b>Data &amp; Facts</b>' in DOC)
check('print css present', '@page{size:A4' in DOC.replace(' ', '') or '@page' in DOC)

print()
if fails:
    print(f'❌ {len(fails)} FAILURES')
    for f in fails:
        print('  -', f)
    sys.exit(1)
print('✅ ALL CHECKS GREEN')
