"""C8 apply v2: apply all second-pass fixes to polished/MERGED_full_1-789.md.
All fixes to one card are applied SEQUENTIALLY on an evolving body.
Safety: block fixes require their anchor; text fixes must match exactly once."""
import re, sys
from collections import defaultdict
sys.path.insert(0, '/home/z/my-project/scripts')
from c8_fixes_gs1 import BLOCKS_A
from c8_fixes_gs23 import BLOCKS_B, TEXTS_B
from c8_fixes_gs4_text import BLOCKS_C, TEXTS_C

BLOCKS = [(c, b, l, a, t) for (c, b, l, a, t) in BLOCKS_A] \
       + [(c, b, l, a, t) for (c, b, l, a, t) in BLOCKS_B] \
       + [(c, b, l, a, t) for (c, b, l, a, t) in BLOCKS_C]
DROP_TEXT_CARDS = {110, 111, 131, 718}  # covered by full-block rewrites / out of scope
TEXTS = [(c, o, n) for (c, o, n) in TEXTS_B if c not in DROP_TEXT_CARDS] \
      + [(c, o, n) for (c, o, n) in TEXTS_C if c not in DROP_TEXT_CARDS]

PATH = '/home/z/my-project/polished/MERGED_full_1-789.md'
md = open(PATH).read()

parts = re.split(r'(?m)^(---\nid: \S+-(\d+)\n)', md)
cards = {}
for i in range(1, len(parts), 3):
    sep, num = parts[i], int(parts[i + 1])
    cards[num] = (sep, parts[i + 2])

def get_body(chunk):
    return chunk.split('\n---\n', 1)[1]

BLOCK_RE = re.compile(r'(?ms)^(:::(\w+)(?: label="([^"]*)")?\n)(.*?)(\n:::)')

blocks_by_card = defaultdict(list)
for (c, bt, lab, anchor, new_text) in BLOCKS:
    blocks_by_card[c].append((bt, lab, anchor, new_text))

errors, applied_b, applied_t = [], 0, 0
new_chunks = {}
for c, fixes in sorted(blocks_by_card.items()):
    if c not in cards:
        errors.append(f'card {c} not found'); continue
    body = get_body(cards[c][1])
    for (bt, lab, anchor, new_text) in fixes:
        hits = [m for m in BLOCK_RE.finditer(body) if m.group(2) == bt and (m.group(3) or '') == lab]
        target = None
        for m in hits:
            if anchor in m.group(4): target = m
        if target is None:
            errors.append(f'BLOCK card {c} {bt}/{lab}: anchor {anchor[:40]!r} not found')
            continue
        body = body[:target.start()] + target.group(1) + new_text + target.group(5) + body[target.end():]
        applied_b += 1
    new_chunks[c] = body

for (c, old, new) in TEXTS:
    if c not in cards:
        errors.append(f'card {c} not found'); continue
    body = new_chunks[c] if c in new_chunks else get_body(cards[c][1])
    n = body.count(old)
    if n != 1:
        errors.append(f'TEXT card {c}: {n} matches for {old[:60]!r}')
        continue
    new_chunks[c] = body.replace(old, new)
    applied_t += 1

if errors:
    print('ABORT — errors:')
    for e in errors: print('  ', e)
    sys.exit(1)

res = [parts[0]]
for i in range(1, len(parts), 3):
    sep, num, chunk = parts[i], int(parts[i + 1]), parts[i + 2]
    if num in new_chunks:
        head = chunk.split('\n---\n', 1)[0]
        res.append(sep + head + '\n---\n' + new_chunks[num])
    else:
        res.append(sep + chunk)
open(PATH, 'w').write(''.join(res))
print(f'APPLIED: {applied_b} block rewrites, {applied_t} text fixes')
