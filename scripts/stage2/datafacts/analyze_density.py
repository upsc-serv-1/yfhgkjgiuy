#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyze_density.py — Phase 5 discovery: which cards are DENSE?

Density = paragraph-shaped or multi-fact content instead of the target
"one fact per bullet" hierarchy. Metrics per card (from SOURCE JSON, since
Phase 5 edits the JSON):
  - prose_lines   : non-bullet, non-title, non-table lines (paragraph text)
  - joined_conts  : soft-wrap continuation lines (parse rule 6 joins them)
  - long_bullets  : bullets whose visible text > 220 chars
  - multi_fact    : bullets carrying >= 2 distinct facts (heuristic: >=2
                    segments ending in ; or . that each contain a number)
  - no_bullets    : card has zero bullet rows (pure prose)
Output: per-card table sorted by density score + totals.
"""
import json, re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_data import split_lines, visible_text  # table-safe <br> split

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
IN_FILE = os.path.join(ROOT, 'inputs', 'updated_data.json')

NUM = re.compile(r'\d')

def facts_in(text):
    """Heuristic count of distinct facts in one visible-text blob:
    split on '; ' / '. ' boundaries; a segment counts as a fact if it
    contains a digit. Sentence period must be followed by space+capital
    or end to avoid splitting decimals / abbreviations."""
    segs = re.split(r';(?= )|(?<=[a-z\)%\d])\.\s+(?=[A-Z(])', text)
    return sum(1 for s in segs if NUM.search(s or '')), segs

def analyze_card(card):
    raw_lines = split_lines(card['content_markdown'])
    prose, conts, bullets, long_b, multi = [], [], 0, 0, 0
    total_chars, bullet_chars = 0, 0
    for raw in raw_lines:
        line = re.sub(r'<!--.*?-->', '', raw)
        if not line.strip():
            continue
        if line.strip().startswith('<table'):
            continue
        # full-line title
        if re.match(r'^\s*(?:•\s*)?<b><u>.*</u></b>\s*$', line):
            continue
        body = re.sub(r'^((?:&nbsp;)+)', '', line)
        vt = visible_text(line).strip()
        total_chars += len(vt)
        if body.startswith('- ') or body.startswith('• '):
            bullets += 1
            bullet_chars += len(vt)
            if len(vt) > 220:
                long_b += 1
            nf, _ = facts_in(vt)
            if nf >= 2:
                multi += 1
        else:
            # prose candidate; rule-6 continuation iff previous line was a row
            if re.match(r'^\*\*|^<b>|^\d+[.)] ', body.strip()):
                prose.append(('fact-row', vt))
            else:
                conts.append(vt)
    score = (len(prose) * 3 + len(conts) * 2 + long_b * 2 + multi)
    return dict(title=card['card_title'], subject=card['subject'],
                prose=len(prose), conts=len(conts), bullets=bullets,
                long_b=long_b, multi=multi, no_bul=bullets == 0,
                chars=total_chars, score=score,
                prose_ex=[p[1][:90] for p in prose[:2]],
                cont_ex=conts[:1])

def main():
    data = json.load(open(IN_FILE))
    rows = [analyze_card(c) for c in data]
    rows.sort(key=lambda r: -r['score'])
    print(f"{'CARD':44s} {'prose':>5s} {'cont':>4s} {'buls':>4s} {'long':>4s} {'multi':>5s} {'score':>5s}")
    for r in rows:
        if r['score'] > 0 or r['no_bul']:
            print(f"{r['title'][:43]:44s} {r['prose']:5d} {r['conts']:4d} {r['bullets']:4d} "
                  f"{r['long_b']:4d} {r['multi']:5d} {r['score']:5d}{'  NO-BULLETS' if r['no_bul'] else ''}")
    tot = lambda k: sum(r[k] for r in rows)
    print(f"\nTOTALS: prose_rows={tot('prose')} continuations={tot('conts')} "
          f"long_bullets={tot('long_b')} multi_fact_bullets={tot('multi')} "
          f"cards_without_bullets={sum(1 for r in rows if r['no_bul'])}")
    print("\n--- top prose examples ---")
    for r in rows[:6]:
        if r['prose_ex'] or r['cont_ex']:
            print(f"\n[{r['subject']}] {r['title']}")
            for p in r['prose_ex']:
                print(f"  PROSE: {p}")
            if r['cont_ex']:
                print(f"  CONT : {r['cont_ex'][0][:90]}")

if __name__ == '__main__':
    main()
