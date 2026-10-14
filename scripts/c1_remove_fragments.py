#!/usr/bin/env python3
"""C1: remove the 8 stray AI fragments / junk headings from the book."""
import re

PATH = '/home/z/my-project/polished/MERGED_full_1-789.md'
book = open(PATH).read()
before = len(book)

FRAGMENTS = [
    " Great! Here's a continuation of the same refined and UPSC-relevant format for: III.INDIAN SOCIETY",
    " Perfect! Continuing in the same enriched, UPSC-relevant style with:",
    " II. Modern Indian History (Mid-18th Century to Present)",
    " Topic C: Architecture",
    " Poverty & Development",
    " Gender Disparity & Laws/Reforms",
    " 11-A.Social Empowerment",
    " Urban Governance",
]
report = []
for f in FRAGMENTS:
    n = book.count(f)
    if n != 1:
        report.append(f"SKIP (count={n}): {f!r}")
        continue
    # capture the card id before removal for the log
    pos = book.find(f)
    cid = '?'
    for m in re.finditer(r'^id: (\S+)', book, re.M):
        if m.start() < pos: cid = m.group(1)
        else: break
    book = book.replace(f, '')
    report.append(f"REMOVED from {cid}: {f.strip()!r}")

# tidy any double-spaces created at the removal seams (only '  ' -> ' ' inside lines)
book = re.sub(r'[ \t]{2,}(?=\n)', '', book)  # trailing spaces at line ends
book = re.sub(r'([.:!?])  +([A-Z0-9])', r'\1 \2', book)

open(PATH, 'w').write(book)
print('\n'.join(report))
print(f"\nBook size: {before} -> {len(book)} chars (delta {len(book)-before})")
