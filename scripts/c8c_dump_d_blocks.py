"""Dump RAW current text of specific blocks from MERGED for C8 D-fixes."""
import re, sys
md = open('/home/z/my-project/polished/MERGED_full_1-789.md').read()
cards = {}
for chunk in re.split(r'(?m)^---\nid: ', md)[1:]:
    cid = chunk.split('\n', 1)[0].strip()
    _, body = chunk.split('\n---\n', 1)
    cards[int(cid.rsplit('-', 1)[1])] = (cid, body)

WANT = {
 2: [('conclusion',''),('introduction','')], 4: [('introduction','')], 6: [('conclusion','')],
 22: [('data','')], 28: [('introduction','')], 29: [('introduction','')], 31: [('introduction','')],
 32: [('conclusion','')], 33: [('introduction','')], 46: [('introduction','')], 47: [('introduction','')],
 50: [('introduction','')], 52: [('introduction','')], 63: [('examples','')], 65: [('introduction','')],
 72: [('introduction','')], 73: [('conclusion','')], 76: [('introduction','')],
 89: [('conclusion','')], 111: [('conclusion','')], 123: [('conclusion','')],
 127: [('conclusion',''),('data','')], 136: [('introduction','')], 140: [('conclusion','')],
 145: [('conclusion',''),('introduction','')], 242: [('conclusion','')], 249: [('introduction','')],
 293: [('conclusion','')], 344: [('introduction','')], 371: [('introduction','')], 408: [('data','')],
 572: [('detail','Concept')], 615: [('detail','Concept')], 618: [('detail','Concept')],
 627: [('detail','Concept')], 717: [('detail','Concept')], 739: [('introduction','')],
 752: [('detail','Concept')],
}
def blocks(body):
    return {(m.group(1), m.group(2) or ''): m.group(3).strip() for m in
            re.finditer(r'(?ms)^:::(\w+)(?: label="([^"]*)")?\n(.*?)\n:::', body)}

for i in sorted(WANT):
    cid, body = cards[i]
    pb = blocks(body)
    for (bt, lab) in WANT[i]:
        for k, t in pb.items():
            if k[0] == bt and (not lab or k[1] == lab):
                print(f'@@@ CARD {i} [{cid}] {bt} label={k[1]!r}')
                print(t)
                print('@@@ END')
