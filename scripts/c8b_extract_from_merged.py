"""C8 v2: extract reviewer-flagged items from the AUTHORITATIVE corrected book
(polished/MERGED_full_1-789.md), not the stale batch files.
Output: /home/z/my-project/c8_report2.txt
"""
import re, sys, json, difflib
sys.path.insert(0, '/home/z/my-project')
import convert

A = {3:['data'],7:['conclusion'],18:['examples'],26:['conclusion'],32:['data'],38:['conclusion'],
 46:['examples'],47:['examples'],52:['examples'],56:['introduction','conclusion'],73:['introduction','data'],
 79:['introduction'],80:['examples'],87:['conclusion'],88:['introduction'],97:['introduction','data','conclusion'],
 105:['conclusion'],108:['data'],109:['introduction'],110:['data'],111:['data'],114:['introduction'],
 120:['introduction'],125:['introduction'],131:['data'],135:['conclusion'],136:['introduction','data'],
 143:['introduction'],146:['data'],149:['introduction'],154:['introduction'],269:['conclusion'],
 412:['introduction'],435:['data','conclusion'],443:['introduction'],448:['introduction'],449:['introduction'],
 450:['introduction'],459:['conclusion'],482:['conclusion'],535:['conclusion'],537:['detail'],
 599:['detail'],637:['introduction'],639:['examples'],640:['examples'],648:['detail'],651:['detail'],
 653:['detail'],655:['detail'],718:['detail'],747:['detail']}
BC = [(7,'conclusion','ethos'),(49,'conclusion','bedrock'),(71,'introduction','ethos'),(87,'conclusion','govt'),
 (100,'introduction','ethos'),(108,'conclusion','underscores'),(112,'conclusion','govt'),
 (125,'introduction','imp'),(125,'data','b/w'),(131,'data','imp'),(150,'conclusion','intricate'),
 (151,'introduction','imp'),(152,'conclusion','pivotal'),(154,'introduction','imp'),(206,'introduction','synergy'),
 (337,'introduction','synergy'),(538,'introduction','synergy'),(540,'conclusion','synergy'),
 (606,'detail','cornerstone'),(718,'detail','govt'),(749,'introduction','ethos'),(749,'examples','ethos')]
D = [2,4,6,18,22,28,29,31,32,33,46,47,50,52,63,65,72,73,76,79,88,89,111,123,127,136,140,143,145,
 242,249,293,344,371,408,572,615,618,627,653,717,739,749,752]

def blocks(body):
    return {(m.group(1), m.group(2) or ''): m.group(3).strip() for m in
            re.finditer(r'(?ms)^:::(\w+)(?: label="([^"]*)")?\n(.*?)\n:::', body)}
def plain(t): return re.sub(r'[\s*]+', ' ', t).strip()

md = open('/home/z/my-project/polished/MERGED_full_1-789.md').read()
cards = {}
for chunk in re.split(r'(?m)^---\nid: ', md)[1:]:
    cid = chunk.split('\n', 1)[0].strip()
    _, body = chunk.split('\n---\n', 1)
    cards[cid] = body
by_num = {int(cid.rsplit('-', 1)[1]): (cid, body) for cid, body in cards.items()}

d = json.load(open(convert.SRC))
out = open('/home/z/my-project/c8_report2.txt', 'w')
def w(s): out.write(s + '\n')

def long_sents(p):
    res = []
    for line in p.split('\n'):
        for sent in re.split(r'(?<=[.!?])\s+', plain(line)):
            n = len(sent.split())
            if n > 25: res.append((n, sent))
    return res

w('=' * 90); w('SECTION A - NEAR-COPY BLOCKS (from corrected MERGED)'); w('=' * 90)
for i in sorted(A):
    cid, pbody = by_num[i]
    obody = convert.convert(i, d[i - 1]).split('\n---\n', 1)[1]
    ob, pb = blocks(obody), blocks(pbody)
    for bt in A[i]:
        for k, ptext in sorted(pb.items()):
            if k[0] != bt: continue
            otext = ob.get(k, '')
            if not otext:
                w(f'\n### CARD {i:04d} [{cid}] :: {bt} label={k[1]!r} -- NO ORIGINAL MATCH'); continue
            r = difflib.SequenceMatcher(None, plain(otext).lower().split(), plain(ptext).lower().split()).ratio()
            flag = 'STILL >=0.90 - REWRITE' if r >= 0.90 else 'already below 0.90'
            w(f'\n### CARD {i:04d} [{cid}] :: {bt} label={k[1]!r} sim={r:.2f} {flag}')
            w('--- CURRENT:'); w(ptext); w('--- ORIGINAL:'); w(otext)

w('\n' + '=' * 90); w('SECTIONS B+C - SHORTHAND & HARD WORDS (sentence context, from MERGED)'); w('=' * 90)
seen = set()
for (i, bt, word) in BC:
    key = (i, bt, word)
    if key in seen: continue
    seen.add(key)
    cid, pbody = by_num[i]
    pb = blocks(pbody)
    for k, ptext in sorted(pb.items()):
        if k[0] != bt: continue
        for line in ptext.split('\n'):
            pl = plain(line)
            if re.search(r'(?i)(?<![a-z])' + re.escape(word) + r'(?![a-z])', pl):
                w(f'\n### CARD {i:04d} [{cid}] :: {bt} word={word!r}')
                w('LINE: ' + pl)

w('\n' + '=' * 90); w('SECTION D - LONG SENTENCES >25 WORDS (from MERGED)'); w('=' * 90)
for i in sorted(D):
    cid, pbody = by_num[i]
    pb = blocks(pbody)
    any_ls = False
    for k, ptext in sorted(pb.items()):
        for n, sent in long_sents(ptext):
            if not any_ls:
                w(f'\n### CARD {i:04d} [{cid}]'); any_ls = True
            w(f'  [{k[0]}{" label="+k[1] if k[1] else ""}] ({n} words): {sent}')
    if not any_ls:
        w(f'\n### CARD {i:04d} [{cid}] -- NO long sentence found now (already fixed?)')
out.close()
print('written c8_report2.txt')
