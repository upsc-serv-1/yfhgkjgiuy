#!/usr/bin/env python3
"""C1-prep v2: looser scan with context windows."""
import re

book = open('/home/z/my-project/polished/MERGED_full_1-789.md').read()
ids = [(m.start(), m.group(1)) for m in re.finditer(r'^id: (\S+)', book, re.M)]

def card_of(pos):
    cur = '?'
    for start, cid in ids:
        if start <= pos: cur = cid
        else: break
    return cur

PATTERNS = [
    (r"Great! Here's a continuation[^*\n]*", 'AI-CHATTER'),
    (r"Perfect! Continuing[^*\n]*", 'AI-CHATTER'),
    (r"II\.?\s*Modern Indian History[^*\n]*", 'STRAY-HEADING'),
    (r"Topic C:?\s*Architecture", 'STRAY-HEADING'),
    (r"11-A\.?\s*Social Empowerment", 'STRAY-HEADING'),
    (r"(?<!\w)Urban Governance(?!\w)", 'STRAY-HEADING'),
    (r"(?<!\w)Poverty & Development(?!\w)", 'STRAY-HEADING'),
    (r"(?<!\w)Gender Disparity & Laws/Reforms(?!\w)", 'STRAY-HEADING'),
    (r"Source Text", 'SOURCE-TEXT'),
    (r"Same as above", 'SAME-AS-ABOVE'),
    (r"\(Same as", 'SAME-AS-ABOVE2'),
    (r"Refer to (the )?(common|general)", 'XREF'),
    (r"same as", 'SAME-AS-LOWER'),
]

hits = {}
for pat, kind in PATTERNS:
    for m in re.finditer(pat, book):
        pos = m.start()
        ctx = book[max(0, pos-70):pos+90].replace('\n', ' ⏎ ')
        hits.setdefault((card_of(pos), kind), []).append(ctx)

for (cid, kind), ctxs in sorted(hits.items(), key=lambda x: (x[0][1], x[0][0])):
    for c in ctxs[:2]:
        print(f"{cid:16s} {kind:15s} …{c}…")
    if len(ctxs) > 2:
        print(f"{cid:16s} {kind:15s} (+{len(ctxs)-2} more)")
