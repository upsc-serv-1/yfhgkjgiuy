#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""parse_data.py — Dr. CSE · Data & Facts
Parses inputs/updated_data.json (83 data cards) into a structured book map:
  paper → subject → section_group → subtopic → card → blocks → rows
Fidelity rules:
  - Visible text must survive VERBATIM (entity-decoded, glyph-mapped) into the HTML.
  - HTML comments (Theme/Sub-Theme/Sub-Sub-Theme) are non-visible metadata → dropped;
    visible markers are the structural truth.
  - CANONICAL GRAMMAR (Phase 5, see restructure_json.py):
      <b><u>Title</u></b>        → section  (.ssec, spans columns)
      • <b><u>Sub-theme</u></b>  → sub      (.sth, in-column heading)
      • <b>Group label:</b>      → minor    (.sth2, quiet in-column label)
      - fact / &nbsp;×4N- fact   → rows at level 0..N (one fact per bullet)
      <table>…</table>           → atomic table
  - First full-line title equal to card_title is a duplicate of the card header → skipped.
    (For multi-theme cards like CURRENT AFFAIRS, ALL inner titles are kept as sections.)
  - 🢥 (U+1F8A5, unrenderable in shipped fonts) → →  (same meaning, logged).
Output: scripts/stage2/datafacts/df_book_map.json
"""
import json, re, sys, os, html as htmllib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
IN_FILE = os.path.join(ROOT, 'inputs', 'updated_data.json')
OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'df_book_map.json')

PAPER_MAP = {'GS-I': 'GS1', 'GS-II': 'GS2', 'GS-III': 'GS3'}
SUBJ_ABBR = {
    'HISTORY': 'HIST', 'SOCIETY': 'SOC', 'POLITY': 'POL', 'GOVERNANCE': 'GOV',
    'INTERNATIONAL RELATIONS': 'IR', 'SOCIAL JUSTICE': 'SJ', 'INDIAN ECONOMY': 'ECO',
    'AGRICULTURE': 'AGRI', 'ENVIRONMENT': 'ENV', 'INTERNAL SECURITY': 'SEC',
    'SCIENCE & TECHNOLOGY': 'TECH', 'DISASTER MANAGEMENT': 'DM',
}
SUBJ_DISPLAY = {
    'HISTORY': 'History', 'SOCIETY': 'Society', 'POLITY': 'Polity',
    'GOVERNANCE': 'Governance', 'INTERNATIONAL RELATIONS': 'International Relations',
    'SOCIAL JUSTICE': 'Social Justice', 'INDIAN ECONOMY': 'Indian Economy',
    'AGRICULTURE': 'Agriculture', 'ENVIRONMENT': 'Environment',
    'INTERNAL SECURITY': 'Internal Security', 'SCIENCE & TECHNOLOGY': 'Science & Technology',
    'DISASTER MANAGEMENT': 'Disaster Management',
}

ENTITY_MAP = {
    '&approx;': '≈', '&plusmn;': '±', '&rupee;': '₹', '&rarr;': '→',
    '&uarr;': '↑', '&darr;': '↓', '&lt;': '<', '&gt;': '>', '&amp;': '&',
    '&deg;': '°', '&mdash;': '—', '&ndash;': '–', '&times;': '×',
}
GLYPH_MAP = {'🢥': '→'}   # unrenderable arrow → standard arrow (logged)

MD_LINK = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
MD_BOLD = re.compile(r'\*\*(.+?)\*\*')
NBSP_RUN = re.compile(r'^((?:&nbsp;)+)')
# Phase-6/7 exam-data highlight marker (documented convention — see
# highlight_json.py): {{hl}}…{{/hl}} wraps a data phrase; renders bold+orange.
HL_RE = re.compile(r'\{\{hl\}\}(.*?)\{\{/hl\}\}')

def decode_entities(s):
    for k, v in ENTITY_MAP.items():
        s = s.replace(k, v)
    return s

def map_glyphs(s):
    for k, v in GLYPH_MAP.items():
        if k in s:
            STATS['glyph_mapped'] += s.count(k)
            s = s.replace(k, v)
    return s

def esc(s):
    """Escape for HTML text nodes, AFTER entity decode and glyph map."""
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def inline(s):
    """Raw source line fragment → safe HTML fragment.
    Order: decode entities → map glyphs → escape <>& → markdown links →
    markdown bold → {{hl}} exam-data marker → <b class=hl> (bold + orange)."""
    s = decode_entities(s)
    s = map_glyphs(s)
    s = esc(s)
    s = MD_LINK.sub(lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', s)
    s = MD_BOLD.sub(lambda m: f'<b>{m.group(1)}</b>', s)
    s = HL_RE.sub(lambda m: f'<b class="hl">{m.group(1)}</b>', s)
    return s

def visible_text(s):
    """Canonical visible text of a raw source line (for verbatim QA)."""
    s = re.sub(r'<!--.*?-->', '', s)
    s = decode_entities(s)
    s = map_glyphs(s)
    s = re.sub(r'<[^>]+>', '', s)          # strip source tags
    s = MD_LINK.sub(lambda m: m.group(1), s)
    s = s.replace('**', '')
    s = s.replace('{{hl}}', '').replace('{{/hl}}', '')   # markers are styling, not text
    return s

def inline_table(s):
    """Sanitize + convert a source <table> line: entities/links/bold inside cells kept."""
    s = decode_entities(s)
    s = map_glyphs(s)
    # markdown links + bold may live inside cells; escape only text between tags
    parts = re.split(r'(<[^>]+>)', s)
    out = []
    for p in parts:
        if p.startswith('<') and p.endswith('>'):
            out.append(p)
        else:
            p = MD_LINK.sub(lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', p)
            p = MD_BOLD.sub(lambda m: f'<b>{m.group(1)}</b>', p)
            out.append(p.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
    return ''.join(out)

STATS = {'glyph_mapped': 0, 'links': 0, 'rows': 0, 'tables': 0, 'headings': 0,
         'minors': 0, 'continuations_joined': 0, 'title_dups_skipped': 0, 'sections_kept': 0}

TBL_PH = '\x00T{}\x00'
TBL_RE = re.compile(r'<table.*?</table>', re.S)
PH_RE = re.compile(r'\x00T(\d+)\x00')

def split_lines(md):
    """Split content_markdown on <br> WITHOUT breaking tables apart.
    Source tables may contain <br> inside cells — a naive split tears them
    into an unclosed <table> fragment plus a stray </table> fragment.
    Protect each full <table>...</table> span with a placeholder, split,
    then restore the table as ONE atomic line."""
    spans = TBL_RE.findall(md)
    idx = iter(range(len(spans)))
    masked = TBL_RE.sub(lambda m: TBL_PH.format(next(idx)), md)
    lines = masked.split('<br>')
    return [PH_RE.sub(lambda m: spans[int(m.group(1))], ln) for ln in lines]

def parse_card(card, serial_in_subject):
    paper = PAPER_MAP[card['paper']]
    subj = card['subject']
    abbr = SUBJ_ABBR[subj]
    cid = f"{paper}-{abbr}-{serial_in_subject:04d}"

    src = card.get('source')
    sources = src if isinstance(src, list) else ([src] if src else [])
    sources = [{k: s.get(k, '') for k in ('org', 'title', 'type', 'year', 'url',
                                          'data_year_or_period', 'last_checked')}
               for s in sources]

    blocks = []          # [{kind: lead|sub|section, title(html)|None, rows:[{level, html, kind}]}]
    title_seen = False

    def cur():
        return blocks[-1] if blocks else None

    def new_block(kind, title_html=None):
        blocks.append({'kind': kind, 'title': title_html, 'rows': []})

    raw_lines = split_lines(card['content_markdown'])
    for raw in raw_lines:
        line = raw
        # 1. drop HTML comments (non-visible)
        no_comment = re.sub(r'<!--.*?-->', '', line)
        if not no_comment.strip():
            continue
        # 2. table line
        if no_comment.strip().startswith('<table'):
            if cur() is None:
                new_block('lead')
            cur()['rows'].append({'level': 0, 'kind': 'table',
                                  'html': inline_table(no_comment.strip())})
            STATS['tables'] += 1
            continue
        # 3. full-line visible titles
        m = re.match(r'^\s*(?:•\s*)?<b><u>(.*?)</u></b>\s*$', no_comment)
        if m:
            is_sub = no_comment.lstrip().startswith('•')
            title_raw = m.group(1)
            if is_sub:
                new_block('sub', inline(title_raw))
                STATS['headings'] += 1
            else:
                first = not title_seen
                title_seen = True
                if first and title_raw.strip().lstrip('*').strip().lower() == card['card_title'].strip().lower():
                    STATS['title_dups_skipped'] += 1   # duplicate of card header
                else:
                    new_block('section', inline(title_raw))   # inner section (CURRENT AFFAIRS, meta-note)
                    STATS['sections_kept'] += 1
            continue
        # 3b. minor group label: • <b>X</b>  (bold, NO underline — Phase 5
        # canonical grammar: third heading tier under sub-themes; carries its
        # own rows like 'sub' blocks but renders as the quieter .sth2)
        m2 = re.match(r'^\s*•\s*<b>(.*?)</b>\s*$', no_comment)
        if m2:
            new_block('minor', inline(m2.group(1)))
            STATS['minors'] += 1
            continue
        # 4. bullet rows (with &nbsp; indent)
        mb = NBSP_RUN.match(no_comment)
        indent_entities = 0
        body = no_comment
        if mb:
            indent_entities = mb.group(1).count('&nbsp;')
            body = no_comment[mb.end():]
        if body.startswith('- ') or body.startswith('• '):
            if cur() is None:
                new_block('lead')
            body = body[2:]
            cur()['rows'].append({'level': min(round(indent_entities / 4), 6),
                                  'kind': 'row', 'html': inline(body)})
            STATS['rows'] += 1
            continue
        # 5. non-bullet content lines
        stripped = body.strip()
        if not stripped:
            continue
        if stripped.startswith('**') or re.match(r'^<b>', stripped) or re.match(r'^\d+[.)] ', stripped):
            # standalone fact row without bullet marker
            if cur() is None:
                new_block('lead')
            cur()['rows'].append({'level': 0, 'kind': 'row', 'html': inline(body)})
            STATS['rows'] += 1
            continue
        # 6. continuation of the previous row (soft wrap in source)
        target = cur()
        if target and target['rows']:
            # append to previous row at same level; strip the indent artefact
            prev = target['rows'][-1]
            if prev['kind'] == 'row':
                prev['html'] += ' ' + inline(stripped)
                STATS['continuations_joined'] += 1
                continue
        # no previous row to join → treat as a plain row
        if cur() is None:
            new_block('lead')
        cur()['rows'].append({'level': 0, 'kind': 'row', 'html': inline(stripped)})
        STATS['rows'] += 1

    return {
        'id': cid,
        'paper': card['paper'], 'paper_key': paper,
        'subject': subj, 'subject_display': SUBJ_DISPLAY[subj],
        'section_group': card['section_group'],
        'microtopic': card.get('microtopic', ''),
        'subtopic': card.get('subtopic', ''),
        'parameter': card.get('parameter', ''),
        'title': card['card_title'],
        'data_year': card.get('data_year', ''),
        'confidence': card.get('confidence', ''),
        'sources': sources,
        'hierarchy_path': card.get('hierarchy_path', []),
        'blocks': blocks,
        'qa_text': ' '.join(visible_text(l) for l in raw_lines if visible_text(l)),
        'qa_chars': len(card['content_markdown']),
    }

def main():
    data = json.load(open(IN_FILE))
    cards = []
    serial = {}
    for c in data:
        subj = c['subject']
        serial[subj] = serial.get(subj, 0) + 1
        cards.append(parse_card(c, serial[subj]))

    # ---- book tree: paper → subject → section_group → subtopic → cards (file order) ----
    # Papers are SORTED GS1 → GS2 → GS3 regardless of file appearance order (the
    # source JSON leads with GS-III cards; the book and index must read Paper I first).
    # Subject order within a paper follows source appearance (source taxonomy preserved).
    papers, subjects, sections, subtopics = {}, {}, {}, {}
    tree = []
    for c in cards:
        p = c['paper_key']
        if p not in papers:
            papers[p] = {'key': p, 'label': c['paper'], 'subjects': []}
            tree.append(papers[p])
        pnode = papers[p]
        if c['subject'] not in subjects:
            subjects[c['subject']] = {'key': c['subject'], 'display': c['subject_display'],
                                      'paper': p, 'sections': []}
            pnode['subjects'].append(subjects[c['subject']])
        snode = subjects[c['subject']]
        sg = c['section_group']
        if (c['subject'], sg) not in sections:
            sections[(c['subject'], sg)] = {'name': sg, 'subtopics': []}
            snode['sections'].append(sections[(c['subject'], sg)])
        sgnode = sections[(c['subject'], sg)]
        st = c['subtopic']
        if (c['subject'], sg, st) not in subtopics:
            subtopics[(c['subject'], sg, st)] = {'name': st, 'cards': []}
            sgnode['subtopics'].append(subtopics[(c['subject'], sg, st)])
        subtopics[(c['subject'], sg, st)]['cards'].append(c)

    tree.sort(key=lambda pnode: pnode['key'])   # GS1 → GS2 → GS3

    out = {
        'book': 'Dr. CSE — Data & Facts',
        'stats': {
            'cards': len(cards),
            'papers': len(tree),
            'subjects': len(subjects),
            'section_groups': len(sections),
            'subtopics': len(subtopics),
            **STATS,
        },
        'tree': tree,
        'cards_flat': cards,
    }
    json.dump(out, open(OUT_FILE, 'w'), ensure_ascii=False, indent=1)

    s = out['stats']
    print(f"parsed {s['cards']} cards | {s['papers']} papers | {s['subjects']} subjects | "
          f"{s['section_groups']} section groups | {s['subtopics']} subtopics")
    print(f"rows {s['rows']} | tables {s['tables']} | sub-headings {s['headings']} | "
          f"minor labels {s['minors']} | inner sections {s['sections_kept']} | title dups skipped {s['title_dups_skipped']}")
    print(f"links converted {sum(c['blocks'] and sum('[href' in r['html'] for b in c['blocks'] for r in b['rows']) for c in cards)} "
          f"| continuations joined {s['continuations_joined']} | glyph 🢥→→ {s['glyph_mapped']}")
    # sanity: any card with zero blocks?
    empty = [c['id'] for c in cards if not c['blocks']]
    print('empty cards:', empty or 'none')
    # block kind census
    from collections import Counter
    print('block kinds:', Counter(b['kind'] for c in cards for b in c['blocks']))

if __name__ == '__main__':
    main()
