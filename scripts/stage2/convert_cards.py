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
def card_html(c):
    mid = c["meta"]
    cid = c["id"]
    parts = [f'<article class="card" id="card-{esc(cid)}">']
    skel = ' <span class="badge-skel">PRACTICE SKELETON</span>' if cid in SKELETONS else ""
    parts.append(
        f'<div class="card-h"><h4>{inline(mid["card_title"])}{skel}</h4>'
        f'<span class="card-id">{esc(cid)}</span></div>'
    )
    micro = mid.get("microtopic", "").strip().strip("\"'")
    if micro:
        parts.append(f'<p class="card-micro">{esc(micro)}</p>')
    for b in c["blocks"]:
        n = b["name"]
        if n == "quote":
            parts.append(f'<div class="pull">{block_html(b, card_ctx(c))}</div>')
        elif n == "introduction":
            parts.append(f'<div class="lede tight">{block_html(b, card_ctx(c))}</div>')
        elif n == "examples":
            parts.append(f'<div class="ex"><div class="blk-lab">Examples</div>{block_html(b, card_ctx(c))}</div>')
        elif n == "data":
            parts.append(f'<div class="data">{block_html(b, card_ctx(c))}</div>')
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


CHAPTER_META = {  # for hero openers — NEW editorial text (mentor tone, easy language)
    1: ("History", "Indian Heritage, Culture, History and Geography of the World feed every GS-1 answer. These 54 cards cover art, ancient and medieval India, modern India, and world history in ready answer language."),
    2: ("Geography", "Physical and economic geography questions reward precise terms and clean diagrams. These 33 cards give you the core ideas, facts, and examples in exam-ready form."),
    3: ("Society", "Society questions test concepts more than facts. These 11 cards bring salient features, diversity, and change in one crisp layer you can quote in any answer."),
    4: ("Polity", "Polity is the highest-yield subject in GS-2. These 43 cards cover the Constitution, rights, parliament, judiciary, and federalism with exact articles and cases."),
    5: ("Governance", "Governance answers need working definitions, committee logic, and examples. These 32 cards organize that material so you can recall it under exam pressure."),
    6: ("International Relations", "IR answers blend facts with a clear point of view. These 26 cards carry the core relations, groupings, and doctrines with usable examples."),
    7: ("Social Justice", "Social Justice questions ask for schemes with purpose and gaps. These 15 cards pair each theme with the right evidence for a balanced answer."),
    8: ("Indian Economy", "Economy answers reward structure: concept, evidence, and impact. These 28 cards give you that structure across growth, fiscal, monetary, and external sectors."),
    9: ("Internal Security", "Security answers need current linkages and precise terms. These 37 cards map threats, agencies, and laws in a way you can reproduce in the hall."),
    10: ("Agriculture", "Agriculture questions connect schemes, ecology, and markets. These 22 cards join those threads so one example can serve many answers."),
    11: ("Science & Technology", "S&T answers reward simple explanations of complex ideas. These 39 cards carry space, defence, biotech, and digital themes with exam-ready data."),
    12: ("Environment", "Environment is the widest GS-3 subject. These 40 cards cover ecology, laws, climate, and governance with figures you can quote safely."),
    13: ("Disaster Management", "Disaster answers follow a fixed drill: hazard, vulnerability, response, resilience. These 22 cards give you that drill for every major theme."),
    14: ("Ethics, Integrity & Aptitude", "GS-4 rewards clarity, not memorised theory. These 149 cards cover terms, thinkers, case approaches, and governance themes with a shared answer grammar. This is the largest part of the book — use its mini-index to navigate."),
}


def render_block_for_verify(b, c):
    return block_html(b, card_ctx(c))


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
    n_files = 0
    for ch in MAP["chapters_flat"]:
        no = ch["chapter_no"]
        disp, intro = CHAPTER_META[no]
        L = []
        # ---- chapter hero (first sheet of the partial) ----
        est_read = max(1, round(ch["word_count"] / 220))  # ~220 wpm
        L.append(f'''<!-- PART {ch['paper']} · CHAPTER {no} · {esc(disp)} · {ch['card_count']} cards · src {esc(ch['src_file'])} -->
<div class="sheet">
  <div class="topbar">
    <div class="brand">PYQ Nano Analysis <span class="mono" style="font-size:9px;color:var(--mut)">GS MAINS</span></div>
    <div class="crumb"><a href="#pt-{ch['paper'].lower().replace('-', '')}">{esc(ch['paper'])}</a> · {esc(disp)}</div>
    <div class="stamp">CHAPTER {no:02d} OF 14<br/><span class="pg-n">·</span></div>
  </div>
  <div class="rule"></div>
  <div class="chap-t">
    <div class="hero-tag">PART {esc(ch['paper'])} · CHAPTER {no:02d}</div>
    <h1 id="ch-{no}">{esc(disp)}</h1>
    <p class="lede">{esc(intro)}</p>
  </div>
  <div class="chips" style="margin-bottom:16px">
    <span class="chip mono">{ch['card_count']} CARDS</span>
    <span class="chip mono">{len(ch['sections'])} SECTIONS</span>
    <span class="chip mono">{sum(len(s['subtopics']) for s in ch['sections'])} SUBTOPICS</span>
    <span class="chip mono">~{est_read} MIN READ</span>
  </div>
  <h2 style="margin-top:8px">In this chapter</h2>
  <div class="chips">''' + "\n".join(
            f'    <a class="chip" href="#{s["anchor"]}">{esc(s["title"])} · {sum(len(t["cards"]) for t in s["subtopics"])} cards</a>'
            for s in ch["sections"]) + '''
  </div>
  <div class="foot"><span>PYQ NANO ANALYSIS — GS MAINS · THE ANSWER-WRITING PLAYBOOK</span><span class="pg-n">·</span></div>
</div>''')
        # ---- sections ----
        for s in ch["sections"]:
            sub_count = sum(len(t["cards"]) for t in s["subtopics"])
            L.append(f'''
<div class="sheet">
  <div class="topbar">
    <div class="brand">PYQ Nano Analysis <span class="mono" style="font-size:9px;color:var(--mut)">GS MAINS</span></div>
    <div class="crumb"><a href="#pt-{ch['paper'].lower().replace('-', '')}">{esc(ch['paper'])}</a> · <a href="#ch-{no}">{esc(disp)}</a> · {esc(s['title'])}</div>
    <div class="stamp">SECTION {s['no']:02d} OF 48<br/><span class="pg-n">·</span></div>
  </div>
  <div class="rule"></div>
  <div class="sec-h" id="{s['anchor']}">
    <span class="k">SECTION {s['no']:02d} · {esc(ch['paper'])}</span>
    <h2>{esc(s['title'])}</h2>
    <span class="n">{sub_count} CARDS · {len(s['subtopics'])} SUBTOPICS</span>
  </div>
  <div class="chips">''' + "\n".join(
                f'    <a class="chip" href="#{t["anchor"]}">{esc(t["title"])}</a>'
                for t in s["subtopics"]) + '''
  </div>
  <div class="foot"><span>PYQ NANO ANALYSIS — GS MAINS · THE ANSWER-WRITING PLAYBOOK</span><span class="pg-n">·</span></div>
</div>''')
            # ---- subtopic groups + cards ----
            for t in s["subtopics"]:
                L.append(f'''
  <div class="sub-h" id="{t['anchor']}">
    <h3>{esc(t['title'])}</h3>
    <span class="cnt">{len(t['cards'])} CARD{'S' if len(t['cards']) > 1 else ''}</span>
  </div>''')
                for cid in t["cards"]:
                    L.append(card_html(by_id[cid]))
        out = "\n".join(L) + "\n"
        (REPO / "src" / ch["src_file"]).write_text(out, encoding="utf-8")
        n_files += 1
        print(f"wrote src/{ch['src_file']}: {ch['card_count']} cards, {len(out):,} bytes")
    print(f"\nDONE: {n_files} chapter partials · all 551 cards verbatim-verified")


if __name__ == "__main__":
    main()
