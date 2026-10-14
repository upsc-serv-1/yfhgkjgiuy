#!/usr/bin/env python3
"""C0c: Match every JSON card against its paper's PDF text.
Reports: PDF coverage per paper, and for each broken card, whether the PDF
contains a fuller original. Extracts PDF context for recoverable cards."""
import json, re, os, difflib

os.chdir('/home/z/my-project')
data = json.load(open('mains_intro_conclusions.json'))

PDFS = {
    'GS-1': 'pdf_text/GS1_fulltext.txt',
    'GS-2': 'pdf_text/GS2_fulltext.txt',
    'GS-3': 'pdf_text/GS3_fulltext.txt',
    'GS-4': 'pdf_text/GS4_fulltext.txt',
}

def norm(s):
    return re.sub(r'\s+', ' ', s).lower().strip()

pdf_text, pdf_pages = {}, {}
for paper, path in PDFS.items():
    raw = open(path).read()
    # split by page markers for page-level search
    chunks = re.split(r'<<<PAGE (\d+)>>>', raw)
    pages = {}
    for i in range(1, len(chunks), 2):
        pages[int(chunks[i])] = norm(chunks[i+1])
    pdf_text[paper] = norm(raw)
    pdf_pages[paper] = pages

# total size comparison
print("=== COVERAGE: JSON body chars vs PDF chars ===")
for paper in ['GS-1', 'GS-2', 'GS-3', 'GS-4']:
    jchars = sum(len(c.get('body') or '') for c in data if c['paper'] == paper)
    pchars = len(pdf_text[paper])
    print(f"{paper}: JSON={jchars:7d} chars | PDF={pchars:7d} chars | PDF/JSON={pchars/max(jchars,1):.2f}")

# distinctive phrase from each card = longest alphabetic run of 7+ words in body
def phrases(body, n=3):
    words = norm(body).replace('*', '').replace('"', '').split()
    out, i = [], 0
    while i < len(words) and len(out) < n:
        if i + 7 <= len(words):
            out.append(' '.join(words[i:i+7])); i += 9
        else:
            break
    return out

BROKEN = [11,13,14,23,30,35,41,42,43,48,77,83,90,91,92,94,95,98,104,113,115,116,117,118,119,
          126,129,130,132,138,139,144,147,148,156,172,175,215,235,245,252,255,264,266,279,280,
          284,292,296,307,314,318,319,385,386,404,405,415,424,426,427,460,462,483,509,517,523,
          530,533,534,536,543,545,556,561,596,778,125,151,153,154,56,24,31,70,75,603,605,740,744]

print("\n=== BROKEN-CARD PDF MATCH REPORT ===")
recoverable = {}
for n in sorted(set(BROKEN)):
    c = data[n-1]
    paper = c['paper']
    title = norm(c.get('card_title') or '')
    body = c.get('body') or ''
    ps = phrases(body)
    hits = []
    # title search (first 5 words of title)
    tw = title.split()[:5]
    if tw and len(' '.join(tw)) > 8:
        t = ' '.join(tw)
        for pno, ptxt in pdf_pages[paper].items():
            if t in ptxt:
                hits.append(('title', pno))
    # phrase search
    for ph in ps:
        for pno, ptxt in pdf_pages[paper].items():
            if ph in ptxt:
                hits.append(('phrase', pno))
                break
    status = 'IN-PDF' if hits else 'NOT-IN-PDF'
    pages = sorted(set(p for _, p in hits))[:4]
    recoverable[n] = (status, pages, paper)
    print(f"[{n:03d}] {c.get('id','?')} {paper} {status:11s} pages={pages} title='{(c.get('card_title') or '')[:45]}'")

import collections
cnt = collections.Counter(v[0] for v in recoverable.values())
print("\nSummary:", dict(cnt))
json.dump({str(k): v for k, v in recoverable.items()}, open('pdf_text/broken_card_match.json', 'w'), indent=1)
print("Saved: pdf_text/broken_card_match.json")
