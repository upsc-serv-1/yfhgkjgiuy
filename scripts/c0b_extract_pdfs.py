#!/usr/bin/env python3
"""C0b: Extract text from the 4 source PDFs (per-page, with markers)."""
import fitz, os, re, json

UP = '/home/z/my-project/upload'
OUT = '/home/z/my-project/pdf_text'
os.makedirs(OUT, exist_ok=True)

PDFS = {
    'GS1': 'readymade-intro and conclusion - GS-1 x ias.pdf',
    'GS2': 'GS 2 INTRO CONCLUSIONS BY X IAS.pdf',
    'GS3': 'GS3 READYMADE INTRO CONCLUSIONS BY X IAS.pdf',
    'GS4': 'ETHICS GS4 READYMADE INTRO CONCLUSIONS BY X IAS.pdf',
}

for tag, fname in PDFS.items():
    doc = fitz.open(os.path.join(UP, fname))
    parts = []
    for i, page in enumerate(doc):
        txt = page.get_text('text')
        parts.append(f"\n<<<PAGE {i+1}>>>\n{txt}")
    out_path = os.path.join(OUT, f'{tag}_fulltext.txt')
    with open(out_path, 'w') as f:
        f.write(''.join(parts))
    print(f"{tag}: {fname} | pages={len(doc)} | chars={sum(len(p) for p in parts)} -> {out_path}")
    doc.close()

# Also map paper -> card-number ranges from the JSON
data = json.load(open('/home/z/my-project/mains_intro_conclusions.json'))
ranges = {}
for idx, c in enumerate(data, 1):
    p = c.get('paper', '?')
    if p not in ranges:
        ranges[p] = [idx, idx]
    ranges[p][1] = idx
print("\nJSON paper -> card number ranges:")
for p, (a, b) in sorted(ranges.items()):
    print(f"  {p}: cards {a}..{b}  ({b-a+1} cards)")
