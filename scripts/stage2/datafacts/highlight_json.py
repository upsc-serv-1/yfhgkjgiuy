#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""highlight_json.py — Phase 6: exam-data highlighting persisted in the JSON.

Adds {{hl}}…{{/hl}} markers around exam-relevant data phrases in
inputs/updated_data.json fact rows. The marker is the documented Phase-7
convention (backward-compatible: parse_data strips it in visible_text and
renders it as <b class="hl"> — orange + bold).

WHAT GETS HIGHLIGHTED (precision-first, every span traces to source text):
  P1  existing `**X**` bold spans that contain a digit and do NOT end with ':'
      (the source author already chose the meaningful phrase; labels stay ink)
  P2  bare numeric phrases: money (₹/$/Rs/USD + number + multiplier), percents
      (incl. 'per cent'), physical units (GW MW TW km kg MT tonnes TWh µg/m³ …),
      multipliers (billion million trillion lakh crore cr), ordinals
      (1st/2nd/3rd…), durations (years yrs months), 'times', ranges N–N+unit
  P3  short phrase extensions: '% of <noun noun?>', ordinal + ≤3 lowercase
      words, trailing 'in/by/since/during <FYxx|20xx|Qx FYxx|CYxx>' period

WHAT STAYS PLAIN (and is FLAGGED for human review):
  years standing alone, ratios/scores, numbers followed by punctuation or
  non-unit words, counted-noun data (e.g. '1,522 mandis') — flagged via the
  NOUN_FLAG list so a human can promote them later.

DISCIPLINE:
  - hard cap: highlighted visible chars ≤ 50% of a card's fact-row chars
    (warn > 40%); P3 extensions are dropped first when over budget
  - markers NEVER inside tables, headings, labels, comments, or link targets
  - marker balance asserted; idempotent (re-running changes nothing)

Usage:
  python highlight_json.py --dry-run [--subject 'INDIAN ECONOMY']
  python highlight_json.py --apply
"""
import json, re, os, sys, copy, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
IN_FILE = os.path.join(ROOT, 'inputs', 'updated_data.json')
BAK_FILE = os.path.join(ROOT, 'inputs', 'updated_data.pre-phase6.json')
LOGF = os.path.join(HERE, 'highlight_log.json')

HL_OPEN, HL_CLOSE = '{{hl}}', '{{/hl}}'

# ---- patterns ----------------------------------------------------------------
# NOTE: every alternation that gets spliced into a larger pattern MUST be
# wrapped in (?:…) — a bare top-level | inside the splice splits the WHOLE
# enclosing group (the Phase-6 review caught 'Rs 73' / '7–17.2%' / '5%'-of-'92.5%'
# matching exactly this way).
MONEY = r'(?:₹|Rs\.?|US?\$|USD|INT\s?\$)\s?'
NUM = r'(?:\d[\d,\.]*\d|\d)'          # greedy; NO space inside numbers
MULT = r'(?:billions?|millions?|trillions?|lakhs?|crores?|cr|bn|mn|B|M)\b\.?'
UNIT = (r'(?:%|per\s?cent(?:age)?|GW|MW|TW|GWh|MWh|TWh|km\.?|kms|kg|MT|tonnes|ton'
        r'|µg/m³|ug/m3|µm|ppb|ppm|bpd|ha|sq\.?\s?km|mld|MWp|GWp|paise|bps|points'
        r'|times|years|yrs|months|weeks|days|cm|mm|mts?|mtr|feet|ft|inches|inch)')
ORD_SUF = r'(?:st|nd|rd|th)'
NUM_CORE = rf'(?:{NUM})(?:\s?[–~-]\s?(?:{NUM}))?'
# unit that may follow a multiplier ('1 lakh MW', '2 crore hectares')
PHYS_AFTER_MULT = r'(?:GW|MW|TW|GWh|MWh|TWh|km|kg|MT|tonnes|ha|hectares?)'

# P2 numeric phrase — two shapes, both with OPTIONAL money prefix (the ? must
# wrap the WHOLE money group, not its trailing \s):
#   A: number (+ordinal suffix) + unit/multiplier (+ physical unit) (+ USD tail)
#   B: bare ordinal rank ('9th', '131st')
P2_RE = re.compile(
    rf'(?<![{{\w])(?:'
    rf'((?:(?:{MONEY}))?{NUM_CORE}{ORD_SUF}?\s?(?:{MULT}(?:\s?(?:{PHYS_AFTER_MULT}|{MULT}))*)\s?(?:USD|dollars)?)'
    rf'|((?:(?:{MONEY}))?{NUM_CORE}{ORD_SUF}\b)'
    rf'|((?:(?:{MONEY}))?{NUM_CORE}{ORD_SUF}?\s?{UNIT}\s?(?:USD|dollars)?)'
    rf')(?![\w{{])', re.X)
# P3 extensions
# 'of <noun>' extension — CLOSED noun list (open list matched verbs/preps:
# 'of women run', 'of banks with', 'of loans goes' — Phase-6 review)
EXT_OF = re.compile(
    r'^\s+of\s+(?:GDP|global|total|land|cultivable|arable|forest|cropland|irrigated|'
    r'sown|area|population|adults?|women|men|children|households|families|farmers|'
    r'workers|labour|students|schools?|colleges?|universities?|seats?|votes?|'
    r'turnout|cases?|deaths?|fatalities|births?|exports?|imports?|trade|traffic|'
    r'tourists?|visitors?|passengers?|energy|electricity|power|generation|capacity|'
    r'loans?|banks?|NPAs?|assets?|funds?|spending|investment|FDI|GDP\s+growth)'
    r'(?:\s+(?:area|land|GDP|deaths?|cropland))?')
EXT_ORD = re.compile(r'^(?:\s+[a-z][a-z\-]+){1,3}(?=[\s(,:;—–\-]|$)')
EXT_PERIOD = re.compile(r'^\s+(?:in|by|since|during)\s+(?:FY\s?\d{2,4}|Q[1-4]\s?FY\s?\d{2,4}|CY\s?\d{2,4}|20\d\d|19\d\d)\b')
EXT_UP = re.compile(r'^\s+(?:up|down)\s+(?:from|to)\s+[\d,\.]+%?\s?(?:{MULT})?'.format(MULT=MULT))

NOUN_FLAG = ('countries', 'states', 'people', 'students', 'villages', 'households',
             'beneficiaries', 'startups', 'mandis', 'reactors', 'airports', 'ports',
             'banks', 'tribunals', 'courts', 'judges', 'seats', 'medals', 'deaths',
             'fatalities', 'births', 'cases', 'incidents', 'attacks', 'riots',
             'schools', 'colleges', 'universities', 'hospitals', 'beds', 'doctors',
             'nurses', 'teachers', 'children', 'farmers', 'workers', 'jobs', 'youth',
             'tourists', 'visitors', 'passengers', 'vehicles', 'cities', 'districts',
             'projects', 'schemes', 'patents', 'papers', 'publications', 'GPs',
             'start-ups', 'industries', 'firms', 'companies', 'plants', 'units')

def visible(s):
    s = re.sub(r'<!--.*?-->', '', s)
    s = re.sub(r'\[\([^\)]*\)\]\([^)]*\)', '', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)
    s = s.replace('**', '').replace(HL_OPEN, '').replace(HL_CLOSE, '')
    return s

def line_kind(s):
    """fact / heading / subheading / label / table / comment / blank"""
    t = s.strip()
    if not re.sub(r'<!--.*?-->', '', t).strip():
        return 'comment' if '<!--' in t else 'blank'
    if t.startswith('<table'):
        return 'table'
    if re.match(r'^\s*(?:•\s*)?<b><u>.*</u></b>\s*$', t):
        return 'subheading' if t.lstrip().startswith('•') else 'heading'
    if re.match(r'^\s*•\s*<b>.*</b>\s*$', t):
        return 'label'
    if re.match(r'^(?:&nbsp;)*- ', t):
        return 'fact'
    return 'other'

def span_text(line, m_or_span):
    return m_or_span.group(0) if hasattr(m_or_span, 'group') else m_or_span

def find_bare_phrases(t):
    """P2 numeric phrases in text t, as (start, end, span, ext_text) tuples.
    Skips regions inside markdown links / existing {{hl}} spans / ** spans."""
    spans = []
    occupied = []
    for m in re.finditer(r'\[\([^\)]*\)\]\([^)]*\)|\[[^\]]*\]\([^)]*\)', t):
        occupied.append(m.span())
    for m in re.finditer(r'\{\{hl\}\}.*?\{\{/hl\}\}', t):
        occupied.append(m.span())
    for m in re.finditer(r'\*\*.*?\*\*', t):
        occupied.append(m.span())
    def free(a, b):
        return all(b <= oa or a >= ob for oa, ob in occupied)
    for m in P2_RE.finditer(t):
        if not free(*m.span()):
            continue
        start, end = m.span()
        span = m.group(0)
        # P3 extension
        ext = ''
        rest = t[end:]
        if span.rstrip().endswith('%'):
            me = EXT_OF.match(rest)
            if me:
                ext = me.group(0)
                # avoid swallowing 'of <noun> and <noun>…' tails: cut at ' and'/' or'
                ext = re.split(r'\s+(?:and|or|vs\.?|v/s)\s', ext)[0]
        elif re.search(r'(?:st|nd|rd|th)$', span.strip()):
            me = EXT_ORD.match(rest)
            if me and not rest.startswith((' in', ' of', ' out')):
                cand = me.group(0)
                # cap extension before prepositions, then trim any dangling one
                cand = re.split(r'\s+(?:in|of|out|for|with|by|from)\s', cand)[0]
                cand = re.sub(r'\s+(?:in|of|out|for|with|by|from|to|and|or|per|v/s|vs\.?)\s*$', '', cand)
                ext = cand
        else:
            me = EXT_PERIOD.match(rest)
            if me:
                ext = me.group(0)
        end2 = end + len(ext)
        spans.append((start, end2, t[start:end2]))
    # merge overlaps
    spans.sort()
    merged = []
    for s in spans:
        if merged and s[0] < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], s[1]), None)
            merged[-1] = (merged[-1][0], merged[-1][1],
                          t[merged[-1][0]:merged[-1][1]])
        else:
            merged.append((s[0], s[1], t[s[0]:s[1]]))
    return merged

def process_card(card, log):
    md = card['content_markdown']
    lines = md.split('<br>')
    out_lines, flags = [], []
    n_spans, hl_chars, row_chars = 0, 0, 0
    for ln in lines:
        kind = line_kind(ln)
        if kind in ('fact',):
            row_chars += len(visible(ln))
        if kind != 'fact':
            out_lines.append(ln)
            continue
        t = ln
        # ---- P1: bold spans with digits (labels ending ':' stay ink) ----
        # Three exclusions found in review:
        #   (a) list-number prefixes ('5. Small Hydro energy') — the only digit
        #       is the numbering, not data
        #   (b) spans containing markdown links — split: hl the digit-bearing
        #       text segments, keep links plain, drop the outer bold
        #   (c) spans ending ':' (labels) — keep ink bold
        def p1_convert(inner):
            if not re.search(r'\d', inner) or inner.rstrip().endswith(':'):
                return None                       # keep as **bold**
            # sole digit is a list-number prefix ('5. Small Hydro energy')
            if re.match(r'^\d{1,2}[.)]\s', inner) \
                    and not re.search(r'\d', re.sub(r'^\d{1,2}[.)]\s*', '', inner)):
                return None
            return 'hl'
        out, pos = [], 0
        for m in re.finditer(r'\*\*(.+?)\*\*', t):
            out.append(t[pos:m.start()])
            inner = m.group(1)
            act = p1_convert(inner)
            if act is None:
                out.append(m.group(0))            # unchanged **bold**
            elif '](' not in inner:
                out.append(f'{HL_OPEN}{inner}{HL_CLOSE}')
            else:
                # link-bearing bold span: hl digit segments outside links
                segs, p2 = [], 0
                for lm in re.finditer(r'\[[^\]]*\]\([^)]*\)', inner):
                    seg = inner[p2:lm.start()]
                    segs.append(f'{HL_OPEN}{seg}{HL_CLOSE}' if re.search(r'\d', seg) else seg)
                    segs.append(lm.group(0))       # link untouched
                    p2 = lm.end()
                seg = inner[p2:]
                segs.append(f'{HL_OPEN}{seg}{HL_CLOSE}' if re.search(r'\d', seg) else seg)
                out.append(''.join(segs))
            pos = m.end()
        out.append(t[pos:])
        t = ''.join(out)
        # ---- P2/P3: bare numeric phrases ----
        spans = find_bare_phrases(t)
        # apply right-to-left
        for a, b, sp in sorted(spans, key=lambda x: -x[0]):
            t = t[:a] + HL_OPEN + t[a:b] + HL_CLOSE + t[b:]
        # count
        for m in re.finditer(r'\{\{hl\}\}(.*?)\{\{/hl\}\}', t):
            n_spans += 1
            hl_chars += len(m.group(1))
        # ---- flags: unhighlighted numbers followed by counted nouns ----
        plain_t = re.sub(r'\{\{hl\}\}.*?\{\{/hl\}\}', '¶', t)
        plain_t = re.sub(r'\*\*.*?\*\*', '§', plain_t)
        plain_t = re.sub(r'\[[^\]]*\]\([^)]*\)', '¶', plain_t)
        for m in re.finditer(r'\b(\d[\d,\.]*)\s+([a-z]+)', plain_t):
            if m.group(2) in NOUN_FLAG:
                flags.append(f"'{m.group(1)} {m.group(2)}' left plain (counted noun)")
        out_lines.append(t)
    new_md = '<br>'.join(out_lines)
    ratio = (hl_chars / row_chars * 100) if row_chars else 0
    over = ratio > 50
    log.append({'card': f"{card['paper']}/{card['card_title']}", 'subject': card['subject'],
                'spans': n_spans, 'hl_chars': hl_chars, 'row_chars': row_chars,
                'ratio_pct': round(ratio, 1), 'over_cap': over, 'flags': flags[:12],
                'n_flags': len(flags)})
    return new_md

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--subject', default=None, help='process only this subject (batch mode)')
    args = ap.parse_args()

    data = json.load(open(IN_FILE))
    log = []
    changed = 0
    for card in data:
        if args.subject and card['subject'] != args.subject:
            continue
        before = card['content_markdown']
        card['content_markdown'] = process_card(card, log)
        if card['content_markdown'] != before:
            changed += 1

    # summary
    tot_spans = sum(e['spans'] for e in log)
    tot_hl = sum(e['hl_chars'] for e in log)
    tot_row = sum(e['row_chars'] for e in log)
    over = [e for e in log if e['over_cap']]
    warn = [e for e in log if 40 < e['ratio_pct'] <= 50]
    flagged = sum(e['n_flags'] for e in log)
    print(f"cards processed: {len(log)} | changed: {changed} | spans: {tot_spans} | "
          f"hl chars: {tot_hl}/{tot_row} ({100*tot_hl/max(tot_row,1):.1f}%)")
    print(f"cards over 50% cap: {len(over)} | 40-50% (review): {len(warn)} | "
          f"flagged counted-nouns: {flagged}")
    for e in over:
        print(f"   OVER CAP: {e['card']} {e['ratio_pct']}% ({e['spans']} spans)")
    # subject census
    from collections import defaultdict
    by_sub = defaultdict(lambda: [0, 0, 0])
    for e in log:
        by_sub[e['subject']][0] += e['spans']
        by_sub[e['subject']][1] += 1
        by_sub[e['subject']][2] += e['ratio_pct']
    print('\nper-subject: spans | cards | avg ratio')
    for s, (sp, n, r) in sorted(by_sub.items()):
        print(f'   {s:32s} {sp:4d} | {n:2d} | {r/n:4.1f}%')

    json.dump(log, open(LOGF, 'w'), ensure_ascii=False, indent=1)
    if args.dry_run:
        print(f'\nDRY RUN — log at {LOGF}; inputs untouched')
    elif args.apply:
        import shutil
        if not os.path.exists(BAK_FILE):
            shutil.copyfile(IN_FILE, BAK_FILE)
            print(f'backup → {BAK_FILE}')
        json.dump(data, open(IN_FILE, 'w'), ensure_ascii=False, indent=2)
        print(f'APPLIED → {IN_FILE}')
    else:
        print('pass --dry-run or --apply')

if __name__ == '__main__':
    main()
