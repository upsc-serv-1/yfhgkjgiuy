#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""restructure_json.py — Phase 5: JSON-level content restructuring.

Rewrites inputs/updated_data.json content_markdown into a CANONICAL grammar
(one fact per bullet, grouped subheadings, clean nested levels). The JSON is
the source of truth: all content-level fixes happen HERE, the renderer only
learns to respect the new grammar.

CANONICAL GRAMMAR (per line, '<br>'-separated):
  <!-- ... -->                      metadata comment (kept, parser drops)
  <b><u>Title</u></b>               card section heading   (.ssec)
  • <b><u>Sub-theme</u></b>         sub-theme heading      (.sth)
  • <b>Group label:</b>             MINOR group label      (.sth2)  ← NEW tier
  - fact text                       fact bullet, level 0
  &nbsp;×4N- fact text              fact bullet, level N (1..5)
  <table>…</table>                  atomic table

TRANSFORMATIONS (all structure-only, zero data change):
  A2  strip trailing '\n\n### Section Group: …' generator artifacts   [logged]
  A3  drop bare-&nbsp; spacer lines                                   [logged]
  B1  merge soft-wrap continuation lines into the previous row        [logged]
  B2  merge sentence-fragment bullets (ending and/or/,) with the next [logged]
  C1  bare full-bold lines → minor labels (short) or bold facts
  C2  label-only bullets (- **X:** / - **X** / - <b>X</b>) → • <b>X</b>
  C3  numbered rows (<b>5. X</b> / **5. X** / 5. X) → bullets, list
      number dropped                                                   [logged]
  C4  remaining bare prose fact-rows → bullets
  D1  broken label-children (level ≤ label level) → label level + 1   [logged]
  D2  hierarchy reconstruction: labels close containers → l0; facts
      emit at container depth + 1 (source levels decide WHO nests
      under whom, canonical levels decide HOW DEEP it shows)
  E1  split '; '-joined independent facts into separate bullets
      (only at paren-depth 0, right side starts uppercase/digit)      [logged]

GUARANTEE: verify pass compares alphanumeric character streams
before/after; every deviation must be an explicitly logged drop
(list numbers, ### artifacts). No other change is legal.

Usage:
  python restructure_json.py --dry-run    # writes staging + log, touches nothing
  python restructure_json.py --apply      # backup + rewrite inputs/updated_data.json
"""
import json, re, os, sys, copy, argparse
import html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
IN_FILE = os.path.join(ROOT, 'inputs', 'updated_data.json')
BAK_FILE = os.path.join(ROOT, 'inputs', 'updated_data.pre-phase5.json')
STAGE = os.path.join(HERE, 'restructured_staging.json')
LOGF = os.path.join(HERE, 'restructure_log.json')

NBSP = '&nbsp;'
TBL_RE = re.compile(r'<table.*?</table>', re.S)
MD_LINK = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')

# Manually reviewed overrides (see restructure_log review, Phase 5):
# fully-bold short bullets that look like labels but are FACTS carrying data —
# they must stay in the body so exam data stays highlightable (Phase 6).
FORCE_FACT = {
    'Target: 2500',                      # JUDICIARY — Gram Nyayalayas target figure
    'Operational: 314',                  # JUDICIARY — operational count
    'No state has > 20% women MLAs',     # ELECTIONS — factual claim w/ data
    'No Institute in TOP 100',           # EDUCATION — factual claim w/ data
}

def visible(s):
    """Canonical visible text of a raw line (mirrors parse_data.visible_text)."""
    s = re.sub(r'<!--.*?-->', '', s)
    for k, v in {'&approx;': '≈', '&plusmn;': '±', '&rupee;': '₹', '&rarr;': '→',
                 '&uarr;': '↑', '&darr;': '↓', '&lt;': '<', '&gt;': '>',
                 '&amp;': '&', '&deg;': '°', '&mdash;': '—', '&ndash;': '–',
                 '&times;': '×', '&nbsp;': ' '}.items():
        s = s.replace(k, v)
    s = re.sub(r'<[^>]+>', '', s)
    s = MD_LINK.sub(lambda m: m.group(1), s)
    return re.sub(r'\s+', ' ', s.replace('**', '')).strip()

def alnum_stream(s):
    """Alphanumeric-only character stream (punctuation/whitespace stripped).
    Structural markers (•, ·) are NOT content — strip before filtering."""
    return re.sub(r'[^0-9A-Za-z\u0080-\uFFFF]', '', visible(s).replace('•', '').replace('·', ''))

# --------------------------------------------------------------------------
class CardFixer:
    def __init__(self, card, log):
        self.card = card
        self.log = log                      # shared list of log entries
        self.cid = f"{card['paper']}/{card['card_title']}"

    def L(self, kind, detail, dropped='', context_after=''):
        self.log.append({'card': self.cid, 'op': kind, 'detail': detail[:400],
                         'dropped': dropped, 'context_after': context_after})

    # ---- line classification ------------------------------------------------
    @staticmethod
    def split_keep_tables(md):
        spans = TBL_RE.findall(md)
        it = iter(range(len(spans)))
        masked = TBL_RE.sub(lambda m: f'\x00T{next(it)}\x00', md)
        lines = masked.split('<br>')
        return [re.sub(r'\x00T(\d+)\x00', lambda m: spans[int(m.group(1))], ln)
                for ln in lines]

    def classify(self, ln):
        """→ dict(kind, nbsp, text, raw) — kind: comment|table|blank|heading|
        subheading|bullet|bare."""
        raw = ln
        s = ln.strip()
        nbsp_n = 0
        m = re.match(r'^((?:&nbsp;)+)', ln)
        if m:
            nbsp_n = m.group(1).count(NBSP)
            body = ln[m.end():].strip()
        else:
            body = s
        # comments can ride at line start
        no_comment = re.sub(r'<!--.*?-->', '', body).strip()
        if not no_comment:
            # keep a line that is ONLY a comment (metadata) — attached to next
            if re.search(r'<!--.*?-->', body):
                return dict(kind='comment', nbsp=0, text='', raw=raw)
            return dict(kind='blank', nbsp=0, text='', raw=raw)
        if no_comment.startswith('<table'):
            return dict(kind='table', nbsp=0, text='', raw=raw)
        # heading forms (bold + underline; optional •)
        mh = re.match(r'^(?:•\s*)?<b><u>(.*?)</u></b>\s*$', no_comment)
        if mh:
            is_sub = no_comment.startswith('•')
            return dict(kind='subheading' if is_sub else 'heading',
                        nbsp=nbsp_n, text=mh.group(1), raw=raw)
        is_bul = body.startswith('- ') or body.startswith('• ')
        txt = body[2:].strip() if is_bul else no_comment
        return dict(kind='bullet' if is_bul else 'bare',
                    nbsp=nbsp_n, text=txt, raw=raw)

    # ---- stage A+B: artifacts, spacers, merges --------------------------------
    def clean_and_merge(self, lines):
        out = []
        # A2: strip generator artifacts '\n\n### Section Group: …'
        cleaned = []
        for ln in lines:
            m = re.search(r'\n+###\s*Section Group:.*$', ln)
            if m:
                self.L('A2_drop_artifact', f"dropped '{visible(m.group(0))[:80]}'",
                       dropped=alnum_stream(m.group(0)))
                ln = ln[:m.start()]
            cleaned.append(ln)
        # classify once
        items = [self.classify(ln) for ln in cleaned]
        # A3: drop blank/nbsp-only spacers
        items = [it for it in items if it['kind'] != 'blank']
        # B1/B2 merges — walk backwards-attaching
        i = 0
        while i < len(items):
            it = items[i]
            if it['kind'] == 'bare':
                prev = out[-1] if out else None
                # B1 continuation: previous bullet/bare-fact absorbs this line
                if prev and prev['kind'] in ('bullet', 'bare'):
                    joiner = ' ' if not prev['text'].rstrip().endswith('[') else ''
                    prev['text'] = prev['text'].rstrip() + joiner + it['text'].strip()
                    self.L('B1_join_continuation',
                           f"'{visible(it['text'])[:60]}' → merged into previous row")
                    i += 1
                    continue
            if it['kind'] == 'bullet':
                # B2 fragment merge: ends with and/or/,/& ; next same-level bullet
                vt = visible(it['text']).rstrip()
                if i + 1 < len(items) and re.search(r'(\band\b|\bor\b|,|&)\s*$', vt) \
                        and not vt.endswith(']:') and not vt.endswith(':'):
                    nxt = items[i + 1]
                    if nxt['kind'] == 'bullet' and nxt['nbsp'] == it['nbsp']:
                        nvt = visible(nxt['text'])
                        if re.match(r'^[a-z0-9(“\']', nvt):
                            it['text'] = it['text'].rstrip() + ' ' + nxt['text'].strip()
                            self.L('B2_merge_fragment',
                                   f"'{vt[-45:]}' + '{nvt[:45]}' → one bullet")
                            items.pop(i + 1)
                            continue
                out.append(it)
                i += 1
                continue
            out.append(it)
            i += 1
        return out

    # ---- stage C: structure promotion ----------------------------------------
    def promote(self, items):
        out = []
        for idx, it in enumerate(items):
            if it['kind'] not in ('bullet', 'bare'):
                out.append(it)
                continue
            txt = it['text'].strip()
            # fully-bold text?  **X** / **X:** / <b>X</b> / <b>X:</b>
            mb = re.match(r'^(?:\*\*(.+?)\*\*|<b>(.+?)</b>)$', txt)
            if mb:
                inner = (mb.group(1) or mb.group(2)).strip()
                # C3 numbered row inside bold → fact bullet, number dropped
                mn = re.match(r'^(\d{1,2})[.)]\s*(.+)$', inner, re.S)
                if mn:
                    self.L('C3_number_dropped',
                           f"'{mn.group(1)}.' dropped from '{visible(inner)[:70]}'",
                           dropped=mn.group(1),
                           context_after=alnum_stream(mn.group(2))[:15])
                    out.append(dict(kind='bullet', nbsp=it['nbsp'],
                                    text=f'**{mn.group(2).strip()}**', raw=''))
                    continue
                # C1/C2 label: fully-bold SHORT text, followed by a bullet
                nxt = next((x for x in items[idx + 1:] if x['kind'] != 'comment'), None)
                is_label_next = nxt is not None and nxt['kind'] == 'bullet'
                if inner in FORCE_FACT:
                    out.append(dict(kind='bullet', nbsp=it['nbsp'],
                                    text=f'**{inner}**', raw=''))
                    self.L('C2_force_fact', f"'{visible(inner)[:60]}' kept as fact (manual override)")
                    continue
                if len(visible(inner)) <= 60 and (is_label_next or it['kind'] == 'bare'):
                    # strip a trailing structural arrow from label text
                    lab = re.sub(r'\s*-+&gt;\s*$', '', inner).strip()
                    lab = re.sub(r'\s*->\s*$', '', lab).strip()
                    self.L('C12_label_promoted' if it['kind'] == 'bullet' else 'C1_label_promoted',
                           f"'{visible(inner)[:60]}' → minor heading")
                    out.append(dict(kind='minorlabel', nbsp=0, text=lab, raw=''))
                    continue
                # fully-bold but long / not followed by bullets → bold fact
                out.append(dict(kind='bullet', nbsp=it['nbsp'],
                                text=f'**{inner}**', raw=''))
                if it['kind'] == 'bare':
                    self.L('C4_bare_to_bullet', f"'{visible(inner)[:60]}' → bullet")
                continue
            # bold HEAD + trailing bracket-citation TAIL  →  minor label that
            # keeps its citation (text order unchanged; only tag placement moves)
            mbt = re.match(r'^(?:\*\*(.+?)\*\*|<b>(.+?)</b>)\s*(\[\s*\S[^\n]*\])\s*$', txt, re.S)
            if mbt and '](' in (mbt.group(3) or '') and len(visible(mbt.group(1) or mbt.group(2))) <= 60:
                head = (mbt.group(1) or mbt.group(2)).strip()
                tail = mbt.group(3).strip()
                self.L('C5_boldhead_citation_label',
                       f"'{visible(head)[:50]}' + citation tail → minor heading")
                out.append(dict(kind='minorlabel', nbsp=0, text=f'{head} {tail}', raw=''))
                continue
            # C3 numbered non-bold bare row  "5. X…" / "**5. X…**"
            if it['kind'] == 'bare':
                mn = re.match(r'^(?:\*\*)?(\d{1,2})[.)]\s*(.+)$', txt, re.S)
                if mn:
                    self.L('C3_number_dropped',
                           f"'{mn.group(1)}.' dropped from '{visible(txt)[:70]}'",
                           dropped=mn.group(1),
                           context_after=alnum_stream(mn.group(2))[:15])
                    rest = mn.group(2).strip()
                    rest = rest.replace('**', '', 2) if rest.startswith('**') and rest.endswith('**') else rest
                    out.append(dict(kind='bullet', nbsp=it['nbsp'], text=rest, raw=''))
                    continue
                # C4 plain bare fact-row (starts ** or <b> partial) → bullet
                out.append(dict(kind='bullet', nbsp=it['nbsp'], text=txt, raw=''))
                self.L('C4_bare_to_bullet', f"'{visible(txt)[:60]}' → bullet")
                continue
            out.append(it)
        return out

    # ---- stage D: hierarchy reconstruction ------------------------------------
    def rebuild_levels(self, items):
        """D1 fix broken label-children, D2 canonical depth via container stack.
        Source levels (nbsp/4) decide WHO nests under whom; emitted depth is a
        clean 0/1/2 cascade: labels reset to 0, children at container+1."""
        lvl = lambda it: it['nbsp'] // 4
        # D1: bullet at level ≤ label level directly after a minorlabel → label+1
        fixed = []
        for it in items:
            if (it['kind'] == 'bullet' and fixed and fixed[-1]['kind'] == 'minorlabel'
                    and lvl(it) <= 0):
                # label is always emitted at nbsp 0 → children must be ≥ 1
                it = dict(it, nbsp=4)
                self.L('D1_child_indent_fix',
                       f"'{visible(it['text'])[:60]}' → nested under "
                       f"'{visible(fixed[-1]['text'])[:40]}'")
            fixed.append(it)
        # D2: walk with container stack keyed on SOURCE levels
        out, stack = [], []          # stack: [source_level] of open containers
        for it in fixed:
            if it['kind'] in ('heading', 'subheading'):
                stack = []
                out.append(it)
            elif it['kind'] == 'minorlabel':
                stack = []
                it = dict(it, nbsp=0)
                out.append(it)
            elif it['kind'] in ('table', 'comment'):
                out.append(it)
            else:  # bullet
                sl = lvl(it)         # source level decides nesting
                while stack and stack[-1] >= sl:
                    stack.pop()
                depth = len(stack)
                it = dict(it, nbsp=4 * depth)
                stack.append(sl)
                out.append(it)
        return out

    # ---- stage E: one fact per bullet (splits) ---------------------------------
    def split_facts(self, items):
        out = []
        for it in items:
            if it['kind'] != 'bullet':
                out.append(it)
                continue
            txt = it['text']
            # candidate ';' positions at paren-depth 0 (ignore those inside
            # markdown links […] or (…))
            parts, depth, last, i = [], 0, 0, 0
            in_link = 0
            while i < len(txt):
                c = txt[i]
                if c == '&':
                    # HTML entity (&gt; &nbsp; …): never split inside it
                    j = txt.find(';', i)
                    if j != -1 and j - i <= 8:
                        i = j + 1
                        continue
                    i += 1
                    continue
                if c == '[':
                    in_link += 1
                elif c == ']':
                    in_link = max(0, in_link - 1)
                elif c in '([':
                    depth += 1
                elif c in ')]':
                    depth = max(0, depth - 1)
                elif c == ';' and depth == 0 and in_link == 0:
                    # does the remainder start a standalone fact?
                    rest = txt[i + 1:].lstrip()
                    if re.match(r'^[A-Z0-9₹$~>]', rest):
                        parts.append(txt[last:i])
                        last = i + 1
                i += 1
            parts.append(txt[last:])
            if len(parts) > 1:
                self.L('E1_fact_split',
                       ' ⏎ '.join(f"'{visible(p)[:50]}'" for p in parts))
                for p in parts:
                    out.append(dict(it, text=p.strip(), raw=''))
            else:
                out.append(it)
        return out

    # ---- serialize -------------------------------------------------------------
    def serialize(self, items):
        lines = []
        pending_comments = []
        for it in items:
            if it['kind'] == 'comment':
                cm = re.search(r'<!--.*?-->', it['raw'])
                if cm:
                    pending_comments.append(cm.group(0))
                continue
            if it['kind'] == 'table':
                lines.extend(pending_comments); pending_comments = []
                lines.append(re.sub(r'^\s*(?:&nbsp;)+', '', it['raw']))
                continue
            if it['kind'] == 'heading':
                lines.extend(pending_comments); pending_comments = []
                lines.append(f"<b><u>{it['text']}</u></b>")
                continue
            if it['kind'] == 'subheading':
                lines.extend(pending_comments); pending_comments = []
                lines.append(f"• <b><u>{it['text']}</u></b>")
                continue
            if it['kind'] == 'minorlabel':
                lines.extend(pending_comments); pending_comments = []
                lines.append(f"• <b>{it['text']}</b>")
                continue
            # bullet — canonical form carries NO raw <b>/<i> tags (the parser's
            # inline() would escape them into visible text). Convert to markdown.
            # Indent = FOUR &nbsp; entities per level (parse_data convention:
            # level = round(entities / 4)).
            lines.extend(pending_comments); pending_comments = []
            indent = NBSP * it['nbsp']
            txt = re.sub(r'<b>(.*?)</b>', r'**\1**', it['text'])
            txt = re.sub(r'<i>(.*?)</i>', r'*\1*', txt)
            lines.append(f"{indent}- {txt}".rstrip())
        return '<br>'.join(lines)

    def run(self):
        lines = self.split_keep_tables(self.card['content_markdown'])
        items = self.clean_and_merge(lines)
        items = self.promote(items)
        items = self.rebuild_levels(items)
        items = self.split_facts(items)
        return self.serialize(items), items

# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    data = json.load(open(IN_FILE))
    orig = copy.deepcopy(data)
    log, new_cards = [], []
    for card in data:
        fx = CardFixer(card, log)
        new_md, items = fx.run()
        card['content_markdown'] = new_md
        new_cards.append(card)

    # ---------- GUARANTEE: alphanumeric stream preservation ----------
    # Position-anchored drop application: every logged drop must remove the
    # dropped text at ITS position, never arbitrary look-alike characters.
    def alnum(s):
        return re.sub(r'[^0-9A-Za-z]', '', s)

    def apply_drops(stream, card_log):
        for e in card_log:
            d = alnum(e['dropped'])
            if not d:
                continue
            if e['op'] == 'A2_drop_artifact':
                if stream.count(d) != 1:
                    return None, f"artifact drop not unique ({stream.count(d)}x): {d[:50]}"
                stream = stream.replace(d, '', 1)
            elif e['op'] == 'C3_number_dropped':
                ctx = alnum(e.get('context_after', ''))
                target = d + ctx
                if not ctx or target not in stream:
                    return None, f"number drop anchor not found: {d!r}+{ctx[:20]!r}"
                stream = stream.replace(target, ctx, 1)
        return stream, None

    violations = []
    for i in range(len(data)):
        expect = alnum_stream(orig[i]['content_markdown'])
        got = alnum_stream(data[i]['content_markdown'])
        card_log = [e for e in log if e['card'] == f"{data[i]['paper']}/{data[i]['card_title']}"]
        expect2, err = apply_drops(expect, card_log)
        if err:
            violations.append((i, orig[i]['card_title'], err))
        elif expect2 != got:
            j = 0
            while j < min(len(expect2), len(got)) and expect2[j] == got[j]:
                j += 1
            violations.append((i, orig[i]['card_title'],
                               f'streams differ at {j}: expected …{expect2[j:j+30]!r} got …{got[j:j+30]!r}'))
    print(f"cards: {len(data)} | log entries: {len(log)}")
    from collections import Counter
    print('ops:', dict(Counter(e['op'] for e in log)))
    if violations:
        print(f"\n!! TEXT-PRESERVATION VIOLATIONS ({len(violations)}):")
        for i, t, a, b in violations[:10]:
            print(f"   card {i} '{t}': expected {a} alnum chars, got {b}")
        sys.exit(1)
    print('text preservation: OK (all 83 cards, alnum streams identical after logged drops)')

    json.dump({'entries': log}, open(LOGF, 'w'), ensure_ascii=False, indent=1)
    if args.dry_run:
        json.dump(data, open(STAGE, 'w'), ensure_ascii=False, indent=2)
        print(f'DRY RUN — staged to {STAGE}, log to {LOGF} (inputs/updated_data.json untouched)')
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
