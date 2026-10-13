"""Usage: python3 verify_protected.py polished.md [original.md]
Compares polished cards against the converter output of the original JSON.
ERROR  = protected content changed (quote, data block, any number/year/article ref)
WARN   = capitalised name or acronym missing from polished text (check by eye)
"""
import re, sys, json, difflib
sys.path.insert(0, '.')
import convert

def split_cards(md):
    cards = {}
    for chunk in re.split(r'(?m)^---\nid: ', md)[1:]:
        cid = chunk.split('\n', 1)[0].strip()
        head, body = chunk.split('\n---\n', 1)
        st = re.search(r'status: (\w+)', head)
        cards[cid] = ('STATUS=' + (st.group(1) if st else '') + '\n') + body
    return cards

def blocks(body):
    return {(m.group(1), m.group(2) or ''): m.group(3).strip() for m in
            re.finditer(r'(?ms)^:::(\w+)(?: label="([^"]*)")?\n(.*?)\n:::', body)}

def plain(t): return re.sub(r'[\s*]+', ' ', t).strip()
def nums(t): return sorted(re.findall(r'\d[\d,./%]*\d%?|\d', re.sub(r'\*', '', t)))
def caps(t):
    t = re.sub(r'\*', '', t)
    out = set()
    for m in re.finditer(r'\b[A-Z][A-Za-z.\-]{1,}', t):
        before = t[:m.start()].rstrip(' -')
        if before == '' or before[-1] in '.:!?\n—–(': continue
        out.add(m.group(0).strip('.,;:()‘’“”"\''))
    return out

FANCY = {'spotlight','spotlights','stir','stirs','tapestry','testament','underscore','underscores','bolster','bolsters','embody','embodies',
 'navigate','navigates','foster','fosters','paradigm','myriad','plethora','pivotal','intricate','multifaceted','nuanced','epitomise','epitomises',
 'encapsulate','encapsulates','harbinger','linchpin','bedrock','cornerstone','ethos','overarching','holistic','synergy','catalyse','catalyses'}
INFORMAL = {'imp','b/w','obj','ppl','u/s','govt','w.r.t','dev','temp','approx','info','recd'}
def easy_check(cid, k, p):
    w = 0
    for sent in [x for line in p.split('\n') for x in re.split(r'(?<=[.!?])\s+', plain(line))]:
        n = len(sent.split())
        if n > 25: print(f'WARN  {cid}: {k} has a long sentence ({n} words) - split it'); w += 1
    bad = sorted(set(x.lower().strip('.,;:') for x in plain(p).split()) & FANCY)
    inf = sorted(set(x.lower().strip('.,;:()*') for x in plain(re.sub(r'\*\*.*?\*\*', ' ', p)).split()) & INFORMAL)
    if inf: print(f'WARN  {cid}: {k} still has informal shorthand {inf} - write it in full (SC, HC, PM, EC etc. are fine)'); w += 1
    if bad: print(f'WARN  {cid}: {k} uses hard words {bad} - use simpler words'); w += 1
    return w

def main(pol_path):
    d = json.load(open(convert.SRC))
    pol = split_cards(open(pol_path).read())
    errs = warns = 0
    for cid, pbody in pol.items():
        i = int(cid.rsplit('-', 1)[1])
        status = re.match(r'STATUS=(\w*)', pbody).group(1); pbody = pbody.split('\n', 1)[1]
        obody = convert.convert(i, d[i - 1]).split('\n---\n', 1)[1]
        ob, pb = blocks(obody), blocks(pbody)
        if set(ob) != set(pb): print(f'ERROR {cid}: block set changed {set(ob)^set(pb)}'); errs += 1
        for k in ob:
            if k not in pb: continue
            o, p = ob[k], pb[k]
            if k[0] in ('quote', 'image') and (plain(o) != plain(p)):
                print(f'ERROR {cid}: protected block {k} changed'); errs += 1
            elif k[0] in ('introduction', 'examples', 'conclusion', 'data', 'detail'):
                if k[0] in ('data', 'detail'):
                    lo = sum(1 for l in o.split('\n') if l.lstrip().startswith('-')); lp = sum(1 for l in p.split('\n') if l.lstrip().startswith('-'))
                    if lo != lp: print(f'ERROR {cid}: {k[0]} block list items changed ({lo} -> {lp})'); errs += 1
                if nums(o) != nums(p): print(f'ERROR {cid}: numbers differ in {k[0]}: {nums(o)} vs {nums(p)}'); errs += 1
                if status == 'polished':
                    r = difflib.SequenceMatcher(None, plain(o).lower().split(), plain(p).lower().split()).ratio()
                    if r > 0.70: print(f'WARN  {cid}: {k[0]} only lightly rewritten (similarity {r:.2f}) - rewrite more'); warns += 1
                if status == 'polished': warns += easy_check(cid, k[0], p)
                miss = caps(o) - caps(p) - set(re.findall(r'[A-Za-z]+', p))
                if miss: print(f'WARN  {cid}: names missing in {k[0]}: {sorted(miss)}'); warns += 1
    print(f'checked {len(pol)} cards: {errs} errors, {warns} warnings')

main(sys.argv[1])
