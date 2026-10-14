#!/usr/bin/env python3
"""C0b-2: Extract the 3 'Paper N' PDFs and match broken cards against ALL 7 PDFs."""
import fitz, os, re, json

UP = '/home/z/my-project/upload'
OUT = '/home/z/my-project/pdf_text'
os.makedirs(OUT, exist_ok=True)

NEW = {
    'P1': 'Paper 1 intros & conclusions.pdf (1).pdf',
    'P2': 'Paper 2 Intro conclusions .pdf 1 (2).pdf',
    'P3': 'Paper 3 intro conclusions.pdf (1).pdf',
}
for tag, fname in NEW.items():
    doc = fitz.open(os.path.join(UP, fname))
    parts = []
    for i, page in enumerate(doc):
        parts.append(f"\n<<<PAGE {i+1}>>>\n{page.get_text('text')}")
    open(os.path.join(OUT, f'{tag}_fulltext.txt'), 'w').write(''.join(parts))
    print(f"{tag}: pages={len(doc)} chars={sum(len(p) for p in parts)}")
    doc.close()

# ---- match broken cards against all 7 PDFs ----
data = json.load(open('/home/z/my-project/mains_intro_conclusions.json'))
ALL = ['GS1', 'GS2', 'GS3', 'GS4', 'P1', 'P2', 'P3']

def norm(s):
    return re.sub(r'\s+', ' ', s).lower().strip()

PAGES = {}
for tag in ALL:
    raw = open(os.path.join(OUT, f'{tag}_fulltext.txt')).read()
    chunks = re.split(r'<<<PAGE (\d+)>>>', raw)
    PAGES[tag] = {int(chunks[i]): norm(chunks[i+1]) for i in range(1, len(chunks), 2)}

BROKEN = [11,13,14,23,30,35,41,42,43,48,77,83,90,91,92,94,95,98,104,113,115,116,117,118,119,
          125,126,129,130,132,138,139,144,147,148,151,153,154,156,172,175,215,235,245,252,255,
          264,266,279,280,284,292,296,307,314,318,319,385,386,404,405,415,424,426,427,460,462,
          483,509,517,523,530,533,534,536,543,545,556,561,596,603,605,740,744,778,24,31,56,70,75]

def phrases(body, n=3):
    words = norm(body).replace('*', '').replace('"', '').split()
    out, i = [], 0
    while i < len(words) and len(out) < n:
        if i + 7 <= len(words):
            out.append(' '.join(words[i:i+7])); i += 9
        else:
            break
    return out

print("\n=== BROKEN CARDS vs ALL 7 PDFs ===")
result = {}
for n in sorted(set(BROKEN)):
    c = data[n-1]
    title = norm(c.get('card_title') or '')
    tw = ' '.join(title.split()[:5])
    ps = phrases(c.get('body') or '')
    hits = {}
    for tag in ALL:
        found_pages = []
        for pno, ptxt in PAGES[tag].items():
            if (len(tw) > 8 and tw in ptxt) or any(len(ph) > 20 and ph in ptxt for ph in ps):
                found_pages.append(pno)
        if found_pages:
            hits[tag] = sorted(found_pages)[:3]
    status = 'FOUND:' + ','.join(f"{t}{p}" for t, p in hits.items()) if hits else 'NOT-IN-ANY-PDF'
    result[n] = hits
    print(f"[{n:03d}] {c.get('card_title','')[:42]:42s} {status}")

cnt = sum(1 for h in result.values() if h)
print(f"\nRecovered from some PDF: {cnt} / {len(set(BROKEN))}")
json.dump({str(k): v for k, v in result.items()}, open(os.path.join(OUT, 'broken_match_all7.json'), 'w'), indent=1)
