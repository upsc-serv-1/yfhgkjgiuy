#!/usr/bin/env python3
"""C0d: Extract full PDF original text for the 13 recoverable broken cards."""
import json, re, os

os.chdir('/home/z/my-project')
data = json.load(open('mains_intro_conclusions.json'))

PDFS = {
    'GS-1': 'pdf_text/GS1_fulltext.txt',
    'GS-2': 'pdf_text/GS2_fulltext.txt',
    'GS-3': 'pdf_text/GS3_fulltext.txt',
    'GS-4': 'pdf_text/GS4_fulltext.txt',
}
# raw (non-normalized) page texts
def load_pages(path):
    raw = open(path).read()
    chunks = re.split(r'<<<PAGE (\d+)>>>', raw)
    pages = {}
    for i in range(1, len(chunks), 2):
        pages[int(chunks[i])] = chunks[i+1]
    return pages

def norm(s):
    return re.sub(r'\s+', ' ', s).lower().strip()

PAGES = {p: load_pages(path) for p, path in PDFS.items()}

CARDS = [24, 31, 41, 42, 77, 83, 91, 92, 94, 95, 104, 279, 523]
out = []
for n in CARDS:
    c = data[n-1]
    paper = c['paper']
    title = norm(c.get('card_title') or '')
    tw = ' '.join(title.split()[:5])
    body = c.get('body') or ''
    words = norm(body).replace('*', '').replace('"', '').split()
    phrase = ' '.join(words[9:16]) if len(words) > 16 else ' '.join(words[:7])
    found = None
    for pno, ptxt in PAGES[paper].items():
        ntxt = norm(ptxt)
        if tw in ntxt or (len(phrase) > 20 and phrase in ntxt):
            found = (pno, ptxt)
            break
    out.append(f"\n{'='*100}\nCARD {n:03d} | {c.get('card_title','')} | {paper} | PDF page {found[0] if found else '?'}\n{'='*100}")
    if found:
        out.append(found[1].strip()[:3200])
    else:
        out.append("(not found)")

report = '\n'.join(out)
open('pdf_text/recovered_13_cards.txt', 'w').write(report)
print(report[:6000])
print(f"\n\n... full report saved to pdf_text/recovered_13_cards.txt ({len(report)} chars)")
