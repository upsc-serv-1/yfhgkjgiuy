#!/usr/bin/env python3
"""C0 investigation: trace truncated/broken cards back to the source JSON.

For each suspicious card, determine WHERE the content was lost:
  STAGE A = already truncated/broken in the source JSON body  (upstream problem)
  STAGE B = lost between JSON and raw_batchN.md (convert.py problem)
  STAGE C = lost between raw md and polished (build/polish problem)
"""
import json, re, sys, os

os.chdir('/home/z/my-project')
SRC = 'mains_intro_conclusions.json'
data = json.load(open(SRC))
print(f"JSON records: {len(data)}")
print(f"JSON keys: {list(data[0].keys())}")

# Cards flagged as truncated / broken / placeholder in review_queue.md
SUSPECTS = [11, 13, 14, 23, 30, 35, 41, 42, 43, 48, 77, 83, 90, 91, 92, 94, 95, 98,
            104, 113, 115, 116, 117, 118, 119, 126, 129, 130, 132, 133, 137, 138, 139,
            144, 147, 148, 156, 172, 175, 215, 235, 245, 252, 255, 264, 266, 279, 280,
            284, 292, 296, 307, 314, 318, 319, 385, 386, 404, 405, 415, 424, 426, 427,
            460, 462, 483, 509, 517, 523, 530, 533, 534, 536, 543, 545, 556, 561, 596,
            778, 125]

def body_text(card):
    return card.get('body', '') or ''

# truncation symptoms to look for IN THE RAW JSON
def json_symptoms(txt):
    s = []
    if not txt.strip():
        s.append('EMPTY-BODY')
        return s
    if re.search(r'\bGreat!\b', txt): s.append('AI-GREAT')
    if re.search(r'continuation', txt, re.I): s.append('AI-CONTINUATION')
    if re.search(r'Perfect!', txt): s.append('AI-PERFECT')
    if re.search(r'Same as above', txt, re.I): s.append('SAME-AS-ABOVE')
    if re.search(r'Refer to (the )?(common|general)', txt, re.I): s.append('XREF')
    if re.search(r'_{2,}', txt): s.append('BLANKS')
    if re.search(r'To be filled|to be added|Sector-specific|scheme specific|sector specific', txt, re.I): s.append('PLACEHOLDER')
    # ends mid-word / mid-sentence
    t = txt.rstrip()
    if t and t[-1] not in '.!?:)"}': 
        s.append('NO-END-PUNCT')
    if re.search(r'\bTemplate\b', txt): s.append('TEMPLATE-NOTE')
    return s

results = {}
for n in sorted(set(SUSPECTS)):
    if n < 1 or n > len(data):
        continue
    card = data[n-1]  # card N = index N-1 (1-based numbering confirmed earlier)
    txt = body_text(card)
    results[n] = {
        'id': card.get('id', f'#{n}'),
        'title': (card.get('card_title') or '')[:50],
        'body_len': len(txt),
        'symptoms': json_symptoms(txt),
        'tail': txt[-90:].replace('\n', ' | '),
    }

print(f"\nSuspect cards traced: {len(results)}")
n_json_trunc = sum(1 for r in results.values() if r['symptoms'])
print(f"Cards showing problems ALREADY IN SOURCE JSON: {n_json_trunc}")
print()
for n, r in results.items():
    print(f"[{n:03d}] {r['id']} len={r['body_len']:4d} symptoms={r['symptoms']}")
    print(f"      tail: ...{r['tail']}")
