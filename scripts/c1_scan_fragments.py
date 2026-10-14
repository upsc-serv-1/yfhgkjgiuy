#!/usr/bin/env python3
"""C1-prep: definitive inventory of stray AI fragments / junk headings in the book.
Scans polished/MERGED_full_1-789.md and prints every hit with card context."""
import re

book = open('/home/z/my-project/polished/MERGED_full_1-789.md').read()

# split into cards by YAML frontmatter
card_starts = [m.start() for m in re.finditer(r'^---\n', book, re.M)]
# cards are delimited by '---' pairs: frontmatter start/end. Simpler: split on '\n---\nid:'
ids = [(m.start(), m.group(1)) for m in re.finditer(r'^id: (\S+)', book, re.M)]

def card_of(pos):
    cur = '?'
    for start, cid in ids:
        if start <= pos:
            cur = cid
        else:
            break
    return cur

PATTERNS = [
    (r"[Gg]reat! Here's a continuation", 'AI-CHATTER'),
    (r"Perfect! Continuing", 'AI-CHATTER'),
    (r"continuation of the same", 'AI-CHATTER'),
    (r"UPSC-relevant (format|style)", 'AI-CHATTER'),
    (r"^\s*(Great|Perfect|Certainly|Absolutely|Sure)!?\s*$", 'AI-CHATTER-LINE'),
    (r"^II\.? ?Modern Indian History", 'STRAY-HEADING'),
    (r"^Topic C:? Architecture", 'STRAY-HEADING'),
    (r"^11-A\.?Social Empowerment", 'STRAY-HEADING'),
    (r"^Urban Governance\s*$", 'STRAY-HEADING'),
    (r"^Poverty & Development\s*$", 'STRAY-HEADING'),
    (r"^Gender Disparity & Laws/Reforms\s*$", 'STRAY-HEADING'),
    (r"Source Text", 'SOURCE-TEXT-LABEL'),
    (r"&rarr;|&larr;", 'HTML-ENTITY'),
    (r"\*\*\*\*", 'BROKEN-BOLD'),
    (r"Lorem|TODO|TBD\b", 'DEV-JUNK'),
]

found = {}
for pat, kind in PATTERNS:
    for m in re.finditer(pat, book, re.M):
        pos = m.start()
        # line boundaries
        ls = book.rfind('\n', 0, pos) + 1
        le = book.find('\n', pos)
        if le == -1: le = len(book)
        line = book[ls:le].strip()
        key = (card_of(pos), kind)
        found.setdefault(key, []).append(line[:110])

print(f"{'CARD':18s} {'KIND':18s} LINE")
for (cid, kind), lines in sorted(found.items(), key=lambda x: (x[0][1], x[0][0])):
    for l in lines[:3]:
        print(f"{cid:18s} {kind:18s} {l}")

# count per kind
import collections
kc = collections.Counter(k for (_, k) in found.keys())
print("\nPer-kind card counts:", dict(kc))
print("Total affected cards:", len(found))
