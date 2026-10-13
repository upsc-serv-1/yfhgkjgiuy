import json, re, sys

SRC = 'mains_intro_conclusions.json'
MAP = {'quote':'quote','quotes':'quote','introduction':'introduction','examples':'examples',
       'conclusion':'conclusion','data':'data'}
ORDER = ['quote','introduction','examples','data','conclusion']
LABEL = re.compile(r'^\*\s+\*\*([^*]+?):\*\*\s*(.*)$')
IMG = re.compile(r'<img[^>]*src="([^"]+)"[^>]*>')

def fix_bold(line, log):
    n = line.count('**')
    if n % 2 == 1:
        s = line.rstrip()
        if s.endswith('**'):
            line = s[:-2].rstrip()
        else:
            i = line.rfind('**'); line = line[:i] + line[i+2:]
        log.append('stray **')
    return line

def parse(body):
    sections, cur, imgs = [], None, []
    for raw in body.split('\n'):
        m = IMG.search(raw)
        if m: imgs.append(m.group(1)); continue
        if not raw.strip(): continue
        lm = LABEL.match(raw) if not raw.startswith((' ', '\t')) else None
        if lm and (not lm.group(2).strip() or lm.group(1).strip().lower() in MAP or lm.group(1).strip().lower().startswith(('concept','fill'))):
            cur = {'label': lm.group(1).strip(), 'lines': []}
            if lm.group(2).strip(): cur['lines'].append('*   ' + lm.group(2).strip())
            sections.append(cur)
        elif cur is not None:
            cur['lines'].append(raw)
        else:
            cur = {'label': 'Content', 'lines': [raw]}; sections.append(cur)
    return sections, imgs

def render_lines(lines, log, unwrap):
    ind = [len(l) - len(l.lstrip(' ')) for l in lines if l.strip() and not l.lstrip().startswith('>')]
    base = min(ind) if ind else 0
    out = []
    for l in lines:
        l = fix_bold(l, log)
        if l.lstrip().startswith('>'):
            continue
        l = l[base:] if l.startswith(' ' * base) else l.lstrip()
        m = re.match(r'^(\s*)\*\s+(.*)$', l)
        if m:
            out.append(('  ' * (len(m.group(1)) // 4)) + '- ' + m.group(2).strip())
        else:
            out.append(l.rstrip())
    top = [o for o in out if o.startswith('- ')]
    if unwrap and len(out) == 1 and out[0].startswith('- '):
        return out[0][2:]
    return '\n'.join(out)

def quote_text(lines):
    t = ' '.join(l.strip().lstrip('>').strip() for l in lines if l.strip())
    parts = re.split(r'\*\*\s+\*\*', t)
    out = []
    for p in parts:
        p = p.strip()
        p = re.sub(r'^\*\*', '', p); p = re.sub(r'\*\*$', '', p)
        if p.strip(): out.append(p.strip())
    return out

def convert(i, c):
    log = []
    secs, imgs = parse(c['body'])
    blocks, labels = {}, []
    extra = []
    for s in secs:
        k = MAP.get(s['label'].lower())
        if k == 'quote':
            ql = [l for l in s['lines'] if l.lstrip().startswith('>')]
            ol = [l for l in s['lines'] if not l.lstrip().startswith('>')]
            blocks.setdefault('quote', []).extend(quote_text(ql))
            if ol: extra.append(('Attached points', render_lines(ol, log, unwrap=False)))
        elif k:
            txt = render_lines(s['lines'], log, unwrap=k in ('introduction', 'conclusion'))
            blocks[k] = (blocks.get(k, '') + '\n' + txt).strip() if k in blocks else txt
        else:
            extra.append((s['label'], render_lines(s['lines'], log, unwrap=False)))
    structured = any(k in blocks for k in ('quote', 'introduction', 'conclusion'))
    out, seq = [], []
    for k in ORDER:
        if k in blocks:
            seq.append(k)
            if k == 'quote':
                for q in blocks[k]: out.append(f':::quote\n{q}\n:::')
            else:
                out.append(f':::{k}\n{blocks[k]}\n:::')
    for lab, txt in extra:
        seq.append('detail'); out.append(f':::detail label="{lab}"\n{txt}\n:::')
    for im in imgs:
        seq.append('image'); out.append(f':::image\n{im}\n:::')
    full = c['body']
    flags = []
    last = ''
    for k2 in ('conclusion', 'introduction'):
        txt = blocks.get(k2, '')
        if txt and not txt.lstrip().startswith('-'):
            last = re.sub(r'[\s*]+$', '', txt.strip().split('\n')[-1])
            if last and not re.search(r'[.!?)"”’\'\]]$', last): break
            last = ''
    if '__' in full or re.search(r'to be added|\bTBD\b|\[.*?(add|insert).*?\]', full, re.I): flags.append('placeholder_blank')
    if any(re.search(r'[—–-]\s*Source Text\s*$', q) for q in blocks.get('quote', [])): flags.append('placeholder_quote')
    if last:
        flags.append('truncated')
    if re.search(r'same as|as above|refer to', full, re.I): flags.append('same_as_above')
    if imgs: flags.append('has_image')
    if log: flags.append('format_fixed')
    pid = f"{c['paper'].replace('-','')}-{re.sub('[^A-Z]','',c['subject'])[:4]}-{i:04d}"
    meta = ['---',
      f'id: {pid}', f'paper: {json.dumps(c["paper"])}', f'subject: {json.dumps(c["subject"])}',
      f'section_group: {json.dumps(c["section_group"], ensure_ascii=False)}',
      f'microtopic: {json.dumps(c["microtopic"], ensure_ascii=False)}',
      f'subtopic: {json.dumps(c["subtopic"], ensure_ascii=False)}',
      f'card_title: {json.dumps(c["card_title"], ensure_ascii=False)}',
      f'card_type: {"structured" if structured else "detail"}',
      f'sections: [{", ".join(seq)}]', f'flags: [{", ".join(flags)}]', '---']
    return '\n'.join(meta) + '\n\n' + '\n\n'.join(out) + '\n'

if __name__ == '__main__':
    d = json.load(open(SRC))
    ids = [int(x) for x in sys.argv[2:]] if len(sys.argv) > 2 else range(1, len(d) + 1)
    res = '\n\n'.join(convert(i, d[i - 1]) for i in ids)
    open(sys.argv[1], 'w').write(res)
