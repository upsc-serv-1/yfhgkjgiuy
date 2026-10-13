import re
def build(raw_path, P, out_path):
    raw = open(raw_path).read(); out = []
    for c in re.split(r'(?m)^(?=---\nid: )', raw):
        if not c.strip(): continue
        cid = re.match(r'---\nid: (\S+)', c).group(1)
        status, blocks = P[cid]
        for k, v in blocks.items():
            c, n = re.subn(r'(?ms)(^:::%s(?: label="[^"]*")?\n).*?(\n:::)' % k, lambda m: m.group(1) + v + m.group(2), c, count=1)
            assert n == 1, (cid, k)
        c = re.sub(r'(?m)^(flags: \[.*\])$', r'\1\nstatus: ' + status, c, count=1)
        out.append(c.rstrip() + '\n')
    open(out_path, 'w').write('\n'.join(out))
def mk(prefix='GS2-POLI'):
    P = {}
    def card(i, status, **blocks): P[f'{prefix}-{i:04d}'] = (status, blocks)
    return P, card
