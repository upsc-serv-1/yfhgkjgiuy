#!/usr/bin/env python3
"""Phase 4 — convert v17 cards (551, VERBATIM) into src/chNN_*.html chapter partials.

Guarantees:
  - Card bodies byte-faithful in TEXT CONTENT: HTML-escaped, **bold**→<strong>,
    *italic*→<em>, bullets (incl. nested + continuation lines)→<ul> structure.
  - Built-in verification: for every block of every card, the tag-stripped,
    whitespace-normalized text of the output == normalized source text.
    One mismatch → abort (exit 1), no partials written.
  - Blocks rendered in ACTUAL order (never the sections: metadata).
  - Images: URL → local assets/images/<file> via images_manifest.json (relative).

Outputs: src/ch01_history.html … src/ch14_ethics.html (14 files)
"""
import html
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "inputs" / "merged_publish_ready_v17.md"
MAP = json.loads((REPO / "scripts" / "stage2" / "book_map.json").read_text(encoding="utf-8"))
MANIFEST = json.loads((REPO / "scripts" / "stage2" / "images_manifest.json").read_text(encoding="utf-8"))

SKELETONS = {"GS3-ENVI-0462", "GS3-DISA-0483", "GS3-INTE-0517", "GS3-INTE-0534", "GS3-INTE-0543"}

ID_RE = re.compile(r"^##\s+id:\s*(\S+)\s*$")
URL_TO_FILE = {}
for rec in MANIFEST["entries"]:
    URL_TO_FILE[rec["url"].strip()] = rec["local_filename"]


# ---------------------------------------------------------------- parsing ---
def parse_cards(text):
    """Reuse of the Phase-1 audit parser, keeping raw block lines."""
    lines = text.splitlines()
    starts = [i for i, l in enumerate(lines) if ID_RE.match(l)]
    cards = []
    for idx, s in enumerate(starts):
        e = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        chunk = lines[s:e]
        cid = ID_RE.match(chunk[0]).group(1)
        meta, blocks, cur = {}, [], None
        for l in chunk[1:]:
            ls = l.strip()
            if ls == ":::":
                if cur is not None:
                    blocks.append(cur)
                    cur = None
            elif ls.startswith(":::") and len(ls) > 3:
                body = ls[3:].strip()
                m2 = re.match(r"([A-Za-z]+)\s*(.*)", body)
                if not m2:
                    continue
                if cur is not None:
                    blocks.append(cur)
                name = m2.group(1).lower()
                rest = m2.group(2).strip()
                label = None
                if rest.lower().startswith("label="):
                    label = rest[6:].strip().strip("\"'")
                cur = {"name": name, "label": label, "lines": []}
                if rest and not rest.lower().startswith("label="):
                    cur["lines"].append(rest)
            else:
                if cur is not None:
                    cur["lines"].append(l)
                elif ls:
                    mm = re.match(r"^([A-Za-z_]+):\s*(.*)$", ls)
                    if mm:
                        meta[mm.group(1)] = mm.group(2).strip().strip("\"'")
        if cur is not None:
            blocks.append(cur)
        cards.append({"id": cid, "meta": meta, "blocks": blocks})
    return cards


# ------------------------------------------------------------ inline conv ---
def esc(t):
    return html.escape(t, quote=False)


def inline(t):
    """Escape + bold/em. Applied AFTER structural parsing, on plain text only."""
    t = esc(t)
    # triple-star boundary: bold-close adjacent to em-close (e.g. **a *b***)
    t = re.sub(r"(\S)\*\*\*(?!\*)", "\\1*\uE000**", t)
    t = re.sub(r"(?<![\w*])\*([^*\s](?:[^*]*[^*\s])?)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = t.replace("\uE000", "")
    return t


def strip_inline_tags(t):
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\s+", " ", t).strip()


BULLET_RE = re.compile(r"^(\s*)\*\s+(.*)$")


def block_html(block, ctx):
    """Convert one block's lines → HTML string. ctx: dict with card info."""
    name, lines = block["name"], block["lines"]
    out = []

    if name == "image":
        for raw in lines:
            url = raw.strip()
            if not url:
                continue
            f = URL_TO_FILE.get(url)
            if not f:
                raise SystemExit(f"FATAL: image URL not in manifest: {url} ({ctx['id']})")
            alt = esc(f"{ctx['subject'].title()} — {ctx['subtopic']}")
            cap = esc(f"{ctx['id']} · {ctx['subject'].title()} · {ctx['subtopic']}")
            out.append(
                f'<figure class="fig"><img src="assets/images/{f}" alt="{alt}" loading="lazy">'
                f"<figcaption>{cap}</figcaption></figure>"
            )
        return "\n".join(out)

    if name == "quote":
        for p in split_paragraphs(lines):
            # attribution as separate leading-dash line → styled .attr (text unchanged)
            if p and p[0].lstrip().startswith(("—", "–")):
                out.append(f'<p class="attr">{inline(p[0].strip())}</p>')
                if len(p) > 1:
                    out.append(f"<p>{inline(' '.join(p))}</p>")
                continue
            out.append(f"<p>{inline(' '.join(p))}</p>")
        return "\n".join(out)

    # list-capable blocks: introduction, conclusion, examples, data, detail
    elems = parse_elements(lines)
    if elems is None:  # pure paragraphs (no bullets at all)
        for p in split_paragraphs(lines):
            out.append(f"<p>{inline(' '.join(p))}</p>")
        return "\n".join(out)
    for kind, payload in elems:
        if kind == "p":
            out.append(f"<p>{inline(' '.join(payload))}</p>")
        else:
            out.append(list_html(payload))
    return "\n".join(out)


def split_paragraphs(lines):
    """Non-empty line groups → list of paragraphs (each = list of lines)."""
    paras, cur = [], []
    for l in lines:
        if l.strip():
            cur.append(l)
        elif cur:
            paras.append(cur)
            cur = []
    if cur:
        paras.append(cur)
    return paras


def parse_elements(lines):
    """Parse block into ordered elements: ('p', [lines]) paragraphs and
    ('ul', [items]) bullet runs. items: {text, children}. Continuation rule:
    a non-bullet line after a bullet continues the nearest open item.
    Returns None when the block has no bullets (pure paragraph block)."""
    elems = []
    para = []          # pending paragraph lines (before/outside lists)
    top = []           # current bullet run (top-level items)
    stack = []         # open item stack: (indent, item)
    saw_bullet = False

    def flush_para():
        if para:
            elems.append(("p", list(para)))
            para.clear()

    def flush_list():
        nonlocal top, stack
        if top:
            elems.append(("ul", top))
            top, stack = [], []

    for l in lines:
        if not l.strip():
            continue  # blank lines never close a list (v17 separates items with blanks)
        m = BULLET_RE.match(l)
        if m:
            if not saw_bullet:
                flush_para()  # leading paragraph(s) before the first bullet
            saw_bullet = True
            indent = len(m.group(1))
            item = {"text": m.group(2).strip(), "children": []}
            while stack and stack[-1][0] >= indent:
                stack.pop()
            if not stack:
                top.append(item)
            else:
                stack[-1][1]["children"].append(item)
            stack.append((indent, item))
        else:
            if not saw_bullet:
                para.append(l)
            elif stack:
                stack[-1][1]["text"] += " " + l.strip()
            else:
                flush_list()
                para.append(l)
    if not saw_bullet:
        return None
    flush_para()
    flush_list()
    return elems


def list_html(items):
    out = ["<ul>"]
    for it in items:
        if it["children"]:
            out.append(f"<li>{inline(it['text'])}\n{list_html(it['children'])}</li>")
        else:
            out.append(f"<li>{inline(it['text'])}</li>")
    out.append("</ul>")
    return "\n".join(out)


# ---------------------------------------------------------- verification ---
def verify_text_fidelity(cards, render):
    """Text-model comparison: inline tags (strong/em) → nothing; block tags → space;
    both sides whitespace-collapsed. Must be equal for every block."""
    INLINE_TAG = re.compile(r"</?(?:strong|em)>")
    BLOCK_TAG = re.compile(r"<[^>]+>")
    fails = []
    for c in cards:
        for b in c["blocks"]:
            if b["name"] == "image":
                continue  # URLs → local files; checked separately
            src_txt = " ".join(b["lines"])
            src_txt = re.sub(r"\*\*", "", src_txt)
            src_txt = src_txt.replace("*", "")
            src_txt = re.sub(r"\s+", " ", src_txt).strip()
            got = render(b, c)
            got_txt = INLINE_TAG.sub("", got)
            got_txt = BLOCK_TAG.sub(" ", got_txt)
            got_txt = html.unescape(got_txt)
            got_txt = re.sub(r"\s+", " ", got_txt).strip()
            if src_txt != got_txt:
                # locate first divergence for the report
                i = next((k for k in range(min(len(src_txt), len(got_txt)))
                          if src_txt[k] != got_txt[k]), min(len(src_txt), len(got_txt)))
                fails.append((c["id"], b["name"],
                              f"@{i}: {src_txt[max(0,i-25):i+45]!r}",
                              f"@{i}: {got_txt[max(0,i-25):i+45]!r}"))
    return fails


# ------------------------------------------------------------- rendering ---
GS_CLASS = {"GS1": "gs1", "GS2": "gs2", "GS3": "gs3", "GS4": "gs4"}

# v3 thin running header — logo + institute name only; cards start directly
THIN = ('  <div class="topbar">\n'
        '    <div class="tb-brand"><img class="tb-logo" src="assets/images/logo_dr_cse.png" '
        'alt="Dr. CSE"/><span class="tb-name">Dr. CSE — <b>Replica</b></span></div>\n'
        '  </div>\n  <div class="rule"></div>')
FOOT = ('  <div class="foot"><span>DR. CSE — REPLICA · INTRO TO CONCLUSION</span>'
        '<span class="pg-n">·</span></div>\n</div>')


def is_wide_data(b):
    """Long DATA fact walls (e.g. GS1-HIST-0012) flow in 2 columns to save
    page space. Rule: at least 6 top-level bullets, or at least 90 words."""
    words = sum(len(l.split()) for l in b["lines"])
    tops = sum(1 for l in b["lines"] if BULLET_RE.match(l) and not l[:1].isspace())
    return words >= 90 or tops >= 6


def card_html(c):
    mid = c["meta"]
    cid = c["id"]
    gscls = GS_CLASS.get(cid.split("-")[0], "gs1")
    parts = [f'<article class="card {gscls}" id="card-{esc(cid)}">']
    skel = ' <span class="badge-skel">PRACTICE SKELETON</span>' if cid in SKELETONS else ""
    parts.append(
        f'<div class="card-h"><h4>{inline(mid["card_title"])}{skel}</h4>'
        f'<span class="card-id">{esc(cid)}</span></div>'
    )
    for b in c["blocks"]:
        n = b["name"]
        if n == "quote":
            parts.append(f'<div class="pull"><div class="blk-lab">Quote</div>{block_html(b, card_ctx(c))}</div>')
        elif n == "introduction":
            parts.append(f'<div class="intro"><div class="blk-lab">Introduction</div>{block_html(b, card_ctx(c))}</div>')
        elif n == "examples":
            parts.append(f'<div class="ex"><div class="blk-lab">Examples</div>{block_html(b, card_ctx(c))}</div>')
        elif n == "data":
            cls = "data data-cols" if is_wide_data(b) else "data"
            parts.append(f'<div class="{cls}"><div class="blk-lab">Data</div>{block_html(b, card_ctx(c))}</div>')
        elif n == "conclusion":
            parts.append(f'<div class="conc"><div class="blk-lab">Conclusion</div>{block_html(b, card_ctx(c))}</div>')
        elif n == "detail":
            lab = esc(b["label"] or "Detail")
            parts.append(f'<div class="detail-p"><div class="lab">{lab}</div>{block_html(b, card_ctx(c))}</div>')
        elif n == "image":
            parts.append(block_html(b, card_ctx(c)))
        else:
            raise SystemExit(f"FATAL: unknown block {n} in {cid}")
    parts.append("</article>")
    return "\n".join(parts)


def card_ctx(c):
    m = c["meta"]
    return {"id": c["id"], "subject": m["subject"], "subtopic": m["subtopic"]}


CHAPTER_META = {  # for hero openers — NEW editorial text (mentor tone, easy language, NO counts)
    1: ("History", "Indian Heritage, Culture, History and Geography of the World feed every GS-1 answer. These cards cover art, ancient and medieval India, modern India, and world history in ready answer language."),
    2: ("Geography", "Physical and economic geography questions reward precise terms and clean diagrams. These cards give you the core ideas, facts, and examples in exam-ready form."),
    3: ("Society", "Society questions test concepts more than facts. These cards bring salient features, diversity, and change in one crisp layer you can quote in any answer."),
    4: ("Polity", "Polity is the highest-yield subject in GS-2. These cards cover the Constitution, rights, parliament, judiciary, and federalism with exact articles and cases."),
    5: ("Governance", "Governance answers need working definitions, committee logic, and examples. These cards organize that material so you can recall it under exam pressure."),
    6: ("International Relations", "IR answers blend facts with a clear point of view. These cards carry the core relations, groupings, and doctrines with usable examples."),
    7: ("Social Justice", "Social Justice questions ask for schemes with purpose and gaps. These cards pair each theme with the right evidence for a balanced answer."),
    8: ("Indian Economy", "Economy answers reward structure: concept, evidence, and impact. These cards give you that structure across growth, fiscal, monetary, and external sectors."),
    9: ("Internal Security", "Security answers need current linkages and precise terms. These cards map threats, agencies, and laws in a way you can reproduce in the hall."),
    10: ("Agriculture", "Agriculture questions connect schemes, ecology, and markets. These cards join those threads so one example can serve many answers."),
    11: ("Science & Technology", "S&T answers reward simple explanations of complex ideas. These cards carry space, defence, biotech, and digital themes with exam-ready data."),
    12: ("Environment", "Environment is the widest GS-3 subject. These cards cover ecology, laws, climate, and governance with figures you can quote safely."),
    13: ("Disaster Management", "Disaster answers follow a fixed drill: hazard, vulnerability, response, resilience. These cards give you that drill for every major theme."),
    14: ("Ethics, Integrity & Aptitude", "GS-4 rewards clarity, not memorised theory. These cards cover terms, thinkers, case approaches, and governance themes with a shared answer grammar — the largest part of this book."),
}


def render_block_for_verify(b, c):
    return block_html(b, card_ctx(c))


WORDS_PER_SHEET = 420  # magazine sheet budget (body words) for auto-pagination


def emit_section(L, paper, ch_no, disp, s, by_id, card_wc):
    """Emit one section_group as 1..n sheets: opener sheet carries the section
    header + subtopic chips; content auto-paginates at ~WORDS_PER_SHEET words.
    v3: thin Dr. CSE — Replica header only (no crumb/stamp/counts); cards
    start directly under the header."""
    header = (f'\n  <div class="sec-h" id="{s["anchor"]}">\n'
              f'    <span class="k">SECTION {s["no"]:02d} · {esc(paper)} · {esc(disp).upper()}</span>\n'
              f'    <h2>{esc(s["title"])}</h2>\n'
              '  </div>\n  <div class="chips">\n' + "\n".join(
                  f'    <a class="chip" href="#{t["anchor"]}">{esc(t["title"])}</a>'
                  for t in s["subtopics"]) + '\n  </div>')

    body, wc = [header], 14

    def close_sheet():
        nonlocal body, wc
        L.append('<div class="sheet">\n' + THIN + "\n" + "\n".join(body) + "\n" + FOOT)
        body, wc = [], 0

    for t in s["subtopics"]:
        cids = t["cards"]
        band = (f'\n  <div class="sub-h" id="{t["anchor"]}">\n'
                f'    <h3>{esc(t["title"])}</h3>\n  </div>')
        body.append(band)
        body.append(card_html(by_id[cids[0]]))
        wc += 10 + card_wc[cids[0]]
        for cid in cids[1:]:
            cwc = card_wc[cid]
            if wc + cwc > WORDS_PER_SHEET:
                close_sheet()
            body.append(card_html(by_id[cid]))
            wc += cwc
    if body:
        close_sheet()


def main():
    text = SRC.read_text(encoding="utf-8")
    cards = parse_cards(text)
    assert len(cards) == 551, f"expected 551 cards, got {len(cards)}"

    fails = verify_text_fidelity(cards, render_block_for_verify)
    if fails:
        print(f"VERBATIM VERIFICATION FAILED: {len(fails)} blocks")
        for f in fails[:10]:
            print(f"  {f[0]} :: {f[1]}\n    src: {f[2]}\n    got: {f[3]}")
        sys.exit(1)
    print("VERBATIM VERIFICATION PASSED: all non-image blocks of 551 cards text-identical")

    by_id = {c["id"]: c for c in cards}
    titles = {c["id"]: c["meta"]["card_title"] for c in cards}
    n_files = 0
    for ch in MAP["chapters_flat"]:
        no = ch["chapter_no"]
        disp, intro = CHAPTER_META[no]
        L = []
        # ---- chapter hero: SUBJECT PAGE with its own clickable card index ----
        # (v3: no stat chips; every card title of the subject is a link)
        sec_groups = []  # one html chunk per syllabus section
        for s in ch["sections"]:
            rows = [f'    <div class="ix-sec"><a href="#{s["anchor"]}">{esc(s["title"])}</a></div>']
            links = " ".join(
                f'<a href="#card-{cid}" title="{esc(titles.get(cid, cid))}">{esc(titles.get(cid, cid))}</a>'
                for t in s["subtopics"] for cid in t["cards"])
            rows.append(f'    <div class="ix-cards">{links}</div>')
            sec_groups.append("\n".join(rows))

        if ch["card_count"] > 100:
            # very large subject (Ethics): split the index across two A4 pages
            counts = [sum(len(t["cards"]) for t in s["subtopics"]) for s in ch["sections"]]
            best, bi = None, 1
            for k in range(1, len(counts)):
                d = abs(sum(counts[:k]) - sum(counts[k:]))
                if best is None or d < best:
                    best, bi = d, k
            g1, g2 = sec_groups[:bi], sec_groups[bi:]
            L.append(f'''<!-- PART {ch['paper']} · CHAPTER {no} · {esc(disp)} · src {esc(ch['src_file'])} -->
<div class="sheet a4">
{THIN}
  <div class="chap-t">
    <div class="hero-tag">PART {esc(ch['paper'])} · CHAPTER {no:02d}</div>
    <h1 id="ch-{no}">{esc(disp)}</h1>
    <p class="lede">{esc(intro)}</p>
  </div>
  <div class="ix-hint">IN THIS SUBJECT — CLICK ANY CARD TITLE TO OPEN IT · CARD INDEX 1 OF 2</div>
  <div class="ix-body cols-3 ix-compact">
{chr(10).join(g1)}
  </div>
{FOOT}''')
            L.append(f'''<div class="sheet a4">
{THIN}
  <div class="ix-hint">{esc(disp).upper()} · CARD INDEX 2 OF 2 — CLICK ANY TITLE TO OPEN IT</div>
  <div class="ix-body cols-3 ix-compact">
{chr(10).join(g2)}
  </div>
{FOOT}''')
        else:
            L.append(f'''<!-- PART {ch['paper']} · CHAPTER {no} · {esc(disp)} · src {esc(ch['src_file'])} -->
<div class="sheet a4">
{THIN}
  <div class="chap-t">
    <div class="hero-tag">PART {esc(ch['paper'])} · CHAPTER {no:02d}</div>
    <h1 id="ch-{no}">{esc(disp)}</h1>
    <p class="lede">{esc(intro)}</p>
  </div>
  <div class="ix-hint">IN THIS SUBJECT — CLICK ANY CARD TITLE TO OPEN IT</div>
  <div class="ix-body">
{chr(10).join(sec_groups)}
  </div>
{FOOT}''')
        # ---- sections (auto-paginated sheets with running topbars) ----
        card_wc = {c["id"]: sum(len(l.split()) for b in c["blocks"] for l in b["lines"])
                   for c in cards}
        for s in ch["sections"]:
            emit_section(L, ch["paper"], no, disp, s, by_id, card_wc)
        out = "\n".join(L) + "\n"
        (REPO / "src" / ch["src_file"]).write_text(out, encoding="utf-8")
        n_files += 1
        print(f"wrote src/{ch['src_file']}: {ch['card_count']} cards, {len(out):,} bytes")
    print(f"\nDONE: {n_files} chapter partials · all 551 cards verbatim-verified")


if __name__ == "__main__":
    main()
