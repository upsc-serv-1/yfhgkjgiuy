"""Merge all polished batch files into one Markdown file, sorted by card number.
Usage: python3 merge_batches.py out.md   (run from the folder that has polished/)"""
import re, sys, glob
cards = {}
for f in glob.glob('polished/*batch*.md'):
    txt = open(f).read()
    for c in re.split(r'(?m)^(?=---\nid: )', txt):
        m = re.match(r'---\nid: \S+-(\d+)\n', c)
        if m: cards[int(m.group(1))] = c.rstrip() + '\n'
open(sys.argv[1], 'w').write('\n'.join(cards[k] for k in sorted(cards)))
print(len(cards), 'cards merged, from', min(cards), 'to', max(cards))
