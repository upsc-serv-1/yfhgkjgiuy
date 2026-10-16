# DESIGN.md — REPLICA (Exam Replicable) · Intro to Conclusion · Dr. CSE

**The design specification of the built book.** This documents the design AS SHIPPED in
`final_ebook.html` (v3, 2026-10-16) — every rule below is implemented in `src/theme.css`
and the `src/*.html` partials.

| Related docs | Role |
|---|---|
| `design_tokens.md` | Token-level reference (every CSS variable and type size) |
| `ebook_structure.md` | Phase-2 architecture study (information architecture, book map) |
| `inputs/prototype_pyq_nano_gs_mains.html` | Design source of truth (STRUCTURE & IDEA only — never its analytics) |
| `inputs/DESIGN_MAGZ_SPEC.md` | Gap-filling spec (magazine article-page system) |
| `PLAN.md` / `HANDOFF.md` | Process plan & live status |

**Truth order:** prototype CSS (structure, tokens, sheet system) → the user's card-box
reference screenshot (card component) → `DESIGN_MAGZ_SPEC.md` (print-facing gaps) →
user review decisions v2 + v3 (which OVERRIDE all of the above where they conflict).

---

## 1. Design principles

1. **The book is a tool, not a brochure.** A student opens it, jumps to a card, and
   replicates the answer in the exam hall. Every design decision serves fast lookup,
   calm reading, and print fidelity.
2. **One card = one complete answer.** Each card stands alone: quotable opening →
   introduction → examples → data → conclusion. The visual system makes these five
   blocks instantly scannable.
3. **Never scare the student with numbers.** No card-count statistics anywhere — no
   pies, bands, heatmaps, tier tables, "N CARDS" chips, "SECTION N OF 48" stamps.
   (Card IDs like `GS1-HIST-0001` are navigation handles, not stats — they stay.)
4. **Everything clickable leads somewhere real.** Every heading level in the index,
   every chip, every card title is an anchor link that lands on its target.
5. **Content is sacred.** Card bodies are verbatim-protected; design only wraps them.
   Design never rewrites, reorders, or decorates protected text.
6. **Screen-first, print-exact.** The HTML is the deliverable; File → Print → A4 must
   produce a clean one-sheet-per-page book with background colours intact.

---

## 2. Design decision history (why the book looks like it does)

| Round | Decision | Rationale |
|---|---|---|
| v1 (build) | Prototype parity: Fraunces + IBM Plex, sage-gold palette, 794px sheets, recreated analytics visuals | Prototype was the agreed design truth |
| v2 review | **Count-analytics REMOVED** (donuts/bands/heatmaps/tiers); index moved to front matter as clickable subject-wise contents; cards redesigned as white rounded boxes with coloured block labels; floating INDEX button + breadcrumb links | "This is a ready-made card book — students jump to cards, charts add nothing" |
| v3 review | **Renamed REPLICA (Exam Replicable)**; Dr. CSE logo header on every sheet; page 2 = Disclaimer + How to Approach (foreword/how-to-use removed); index 2-column with every level clickable incl. subtopics; subject pages carry their own clickable card index on true-A4 sheets; NO counts anywhere; INTRODUCTION boxed; syllabus-point line removed; long DATA in 2 columns | "Don't scare students with numbers" + brand consolidation + index usability |

---

## 3. Book anatomy (as built, 217 sheets)

```
Sheet 1    Cover (.p1, true-A4)
Sheet 2    Disclaimer + How to Approach (.a4)                     — page 002
Sheets 3–9   Master index, "Every card, subject by subject" (7 .a4
              sheets, 2-column; auto-paginated — GS-3 alone spans 3)
Then 4 parts, each:
  1 sheet   Part opener — GS paper chip, subject chips, mentor note (.a4)
  per chapter (14 total):
    1 sheet Subject page — subject name + clickable card index of that
            subject (.a4; Ethics spans 2 — compact 3-col rows)
    N sheets  Card sheets (188 total) — section bands → subtopic bands →
              cards flowing as rounded boxes
Sheet 217  Back cover (.p1) — companion resources + contact
```

**Sheet census (217 total):** 2 × `.p1` (cover, back cover) · 27 × `.a4`
(1 disclaimer + 7 index + 4 part openers + 14 subject pages + 1 Ethics index
continuation) · 188 × `.sheet` content sheets.

- Every sheet carries: thin running header (logo + "Dr. CSE — **Replica**"), hairline
  rule, running footer (`DR. CSE — REPLICA · INTRO TO CONCLUSION · <page number>`),
  auto-stamped `NNN / 217` page number.
- Anchors: `#fm-cover` `#fm-disclaimer` `#ix-master` `#ix-gs1…gs4` `#pt-gs1…gs4`
  `#ch-1…14` and `#card-<CARD-ID>` for all 551 cards.
- One floating **INDEX** button (screen only, bottom-right) on every sheet.

---

## 4. Page system & geometry

### Screen
| Token | Value | Notes |
|---|---|---|
| Book width | `794px` | fixed, centered (`.book`) |
| Sheet padding | `26px 48px 24px` | content column ≈ 698px |
| Sheet gap / shadow | `18px` / `0 10px 30px rgba(0,0,0,.18)` | sheets lie on a desk |
| Desk colour | `#D5DCD6` light · `#0F1514` dark | sheets themselves never change |
| True-A4 sheets (`.p1`, `.a4`) | `min-height:1123px` | cover, openers, index, subject pages |

### Print (`@media print`)
- `@page { size: A4; margin: 10mm }` — **one sheet = one page** (`break-after: page`).
- Sheet chrome (shadow, padding, min-height) stripped; page units become the sheets.
- `print-color-adjust: exact` everywhere — sage sheets, card boxes, coloured labels
  survive printing (user must enable "background graphics" in the print dialog).
- Atomic in print: `.card`, `.blk`, `.detail-p`, `figure.fig`, `.take`, `.note`,
  `.panel`, `tr` are `break-inside: avoid`.
- No orphans: `h2/h3/h4`, `.sec-h`, `.sub-h`, `.chap-t` are `break-after: avoid`.
- Links print as plain text (inherit colour); the floating INDEX button is hidden.

---

## 5. Color system

### Surfaces & inks
| Token | Value | Use |
|---|---|---|
| `--page` | `#EEF2EE` | Sheet face (warm sage-ivory) |
| `--desk` | `#D5DCD6` | Screen background only |
| `--box` | `#F5F8F5` | Panel interiors (DATA boxes, detail panels, card-id pill) |
| `--card` | `#FFFFFF` | Card box face — white on sage = "separate colour" per card |
| `--ink` / `--ink-h` / `--ink2` / `--mut` | `#1E2A2A` / `#16211F` / `#43514F` / `#5B6B6C` | Body / headings / ledes / labels-captions |
| `--hair` / `--hair2` | `rgba(30,42,42,.16)` / `.30` | Light rules / strong + dotted rules |

### Accents — semantic, never decorative
| Token | Value | Meaning |
|---|---|---|
| `--gold` | `#A97D2B` | Editorial voice: QUOTE blocks, verdict bars, detail bars, section kickers, GS-1 card edge, GS chip, INDEX button border, "Replica" in header |
| `--teal` | `#4F8F86` | Content & links: INTRODUCTION blocks, DATA top-rules, take callouts, GS-2 card edge, all anchor links |
| `--green` | `#6E9468` | Support: EXAMPLES + CONCLUSION blocks, GS-3 card edge |
| `--deep` | `#1F4F52` | DATA labels, GS-4 card edge |

### Block tints (whisper-quiet, 8–11% alpha)
`--t-gold` `rgba(169,125,43,.08)` · `--t-teal` `rgba(79,143,134,.08)` ·
`--t-green` `rgba(110,148,104,.11)` — panel fills inside cards. Never saturated.

### Per-paper identity (the only place paper colour appears)
GS-1 **gold** · GS-2 **teal** · GS-3 **green** · GS-4 **deep** — as a 3px top edge on
every card. A student flipping pages sees the paper change at a glance.

---

## 6. Typography

**Fonts:** Fraunces (display/serif) + IBM Plex Sans (body) + IBM Plex Mono (data,
labels, IDs) — loaded from Google Fonts with full system fallbacks (Georgia /
system-ui / ui-monospace). Offline degradation changes texture, never layout.

| Role | Font | Size / line |
|---|---|---|
| Cover h1 "Replica" | Fraunces 600 | 76 / 1.02, tracking −2.5px |
| Chapter title | Fraunces 600 | 34 / — |
| Part title | Fraunces 600 | 26 / 1.1 (`.ch`) |
| Section h2 | Fraunces 600 | 22 / 1.12 |
| Subtopic band h3 | Fraunces 600 | 15.5 / 1.3 |
| Card title h4 | Fraunces 600 | 16 / 1.25 |
| Body p | IBM Plex Sans 400 | 12 / 1.6 |
| Lede | IBM Plex Sans 400 | 12.5 / 1.55, capped 640px |
| Pull-quote | Fraunces 500 italic | 14 / 1.45 |
| Verdict (mentor) | Fraunces 600 | 18 / 1.28 |
| Block labels `.blk-lab` | IBM Plex Sans 600 | 8.5px, tracking 1.8px, uppercase |
| DATA panel | IBM Plex Mono 500 | 10 / 1.6–1.7 |
| IDs / stamps / crumbs | IBM Plex Mono 500 | 8.5–10px, tracked |

---

## 7. The card — core component

**One card = one white rounded box on the sage sheet** (user's reference screenshot,
blended into the sage-gold palette).

```
┌──────────────────────────────────────────────────┐  ← .card  white, 12px radius,
│ ▔▔▔ 3px paper-colour top edge (gs1 gold … gs4 deep)│     hairline border, soft shadow,
│                                                    │     16–20px padding, atomic
│ Card Title (Fraunces h4)          [GS1-HIST-0012] │  ← .card-h + dashed rule under
│ ┌ QUOTE ─────────────────────────────────────┐   │
│ │ "…" — attribution (gold panel, gold bar)    │   │  ← .pull
│ └─────────────────────────────────────────────┘   │
│ ┌ INTRODUCTION ──────────────────────────────┐   │
│ │ (pale-teal panel, teal left rule)          │   │  ← .intro  (boxed, v3)
│ └─────────────────────────────────────────────┘   │
│ ┌ EXAMPLES ──────────────────────────────────┐   │
│ │ (pale-green panel, green rule)             │   │  ← .ex
│ └─────────────────────────────────────────────┘   │
│ ┌ DATA ──────────────────────────────────────┐   │
│ │ (sage box, mono, teal top rule; long walls │   │  ← .data (+ .data-cols:
│ │  flow 2-column — 25 cards incl. GS1-HIST)  │   │     column-count:2)
│ └─────────────────────────────────────────────┘   │
│ ┌ CONCLUSION ────────────────────────────────┐   │
│ │ (pale-green rounded panel — the money block)│   │  ← .conc
│ └─────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────┘
```

Rules of the card:
- Blocks render **in the card's ACTUAL source order** (v17 `sections:` list) — never
  a forced template. Detail cards use `.detail-p` (sage panel, gold bar, mono label)
  per `:::detail label`. Multi-quote cards render all quotes in sequence.
- Every block opens with a coloured uppercase chip label (`.blk-lab`) — a student
  learns the five-block rhythm after two pages.
- The 5 `universal_template` cards wear a gold-outline **PRACTICE SKELETON** chip
  (`.badge-skel`) in the header.
- The v3 deletions are permanent: **no syllabus-point micro line**, no microtopic
  row, no count chips inside cards.
- `id="card-<ID>"` on every card = the link target for index, subject pages, chips.
- 38 image figures (`.fig`): local `assets/images/…`, hairline border, 6px radius,
  mono caption. No hotlinks anywhere.

---

## 8. Editorial components (NEW text only — never inside card bodies)

| Component | Look | Use |
|---|---|---|
| `.verdict` | 3px gold left bar, Fraunces 18px | One mentor takeaway per part opener |
| `.take` | Teal bar + 8% teal tint | Inline guidance notes |
| `.note` | Neutral 5% grey panel | Neutral asides |
| `.panel` + `.p-t` | Rounded 12px bordered box, gold mono kicker | Disclaimer & How-to-Approach blocks (page 2) |
| `.lede` | 12.5px, ink2, 640px cap | Openers & front matter intros |

---

## 9. Navigation system (what replaced the analytics library)

The v1 analytics visuals (donut, bands, heatmap, tiers, dots) were removed in v2 and
must never return. Navigation is 100% anchor-based:

| Element | Where | Behaviour |
|---|---|---|
| Master index (7 `.a4` sheets, pages 003–009) | Front matter, `#ix-master` | 2-column (`.ix-body`), every level clickable: paper → subject → section → **subtopic** → card title; compact variant (`.ix-compact`) for GS-4's 149 Ethics cards |
| Floating INDEX button (`.to-ix`) | Screen only, bottom-right of every sheet | Jumps to `#ix-master`; hidden in print |
| Subject-page card index | Each of the 14 subject pages | That subject's card titles as flat clickable rows (`.ix-cards`); Ethics spans 2 sheets |
| Part openers | 4 sheets | Paper chip + subject chips + section links — pure navigation, no charts |
| CONTENTS chips | Cover | `#ix-master`, `#fm-disclaimer` |

Index link styles: dotted underlines (`--hair2`), teal on hover — quiet on the page,
obvious when hunted.

---

## 10. Page specs

### Cover (`.p1`)
Logo top-left (46px) + `FIRST EDITION / 2026` stamp · gold kicker `EXAM REPLICABLE ·
INTRO TO CONCLUSION` · 76px Fraunces "Replica" · one-sentence lede · two CONTENTS
chips · contact strip `drcse.in · t.me/dr_cse · dr.cse.001@gmail.com` between
hairlines. **No stats, no counts.**

### Page 2 — Disclaimer & How to Approach (`.a4`)
Two `.panel` blocks: Disclaimer (educational use, verify against official sources,
© Dr. CSE) and How to Approach (the five-block card anatomy, how to use the index,
print tips: A4 + enable background graphics).

### Master index (8 `.a4` sheets)
Title "Every card, subject by subject" · mono hint line · 2-column body with
section rules · subject headers clickable → subject pages · subtopic names
clickable → subtopic bands · card titles clickable → cards.

### Part opener (4, one per GS paper)
GS chip (cream `#F7E3CF` / `#8A4308`) · hero-tag · Fraunces paper title · lede ·
mentor `.verdict` · "Inside this paper" subject chips → subject pages ·
section-group quick-links.

### Subject page (14, first sheet of each chapter)
`.chap-t` hero: chapter number + subject name + intro lede → then that subject's
clickable card index. No "N sections / N subtopics" rows.

### Card sheets (188)
`.sec-h` section band (gold mono kicker + Fraunces h2) when the section group
changes → `.sub-h` subtopic band (dotted underline) → cards flowing underneath,
3–5 per sheet. Sheets auto-paginate (~420 words) so no card is ever split.

### Back cover (`.p1`)
Closing panel + companion-resources image (`assets/images/cover_candidate_resource_guide.png`)
+ contact strip.

---

## 11. Hard prohibitions (design DO-NOTs)

1. **No count-analytics** — pies, bands, heatmaps, tiers, dot scales (user v2).
2. **No card-count numbers** presented as statistics (user v3) — not on cover,
   openers, index badges, or subject pages.
3. **No ad-hoc styling in partials** — the component vocabulary in `theme.css`
   §1–11 is the only language; new needs go into `theme.css` first.
4. **No restyling of verbatim content** beyond its mapped block component.
5. **No external image hotlinks**; no `backdrop-filter`; no layout-critical
   webfonts without fallbacks.
6. **No page-break styles in partials** — print rules are global in `theme.css` §11.
7. **Accent roles are fixed** — gold = editorial, teal = content/links,
   green = support. Never mix.
8. **No book-name/section/subject crumbs in the running header** (v3) — the header
   stays logo + "Dr. CSE — Replica"; cards start immediately.

---

## 12. Where the design lives (theme.css map)

| § | Section | Covers |
|---|---|---|
| 1 | Tokens | all CSS variables (colours, fonts, tints) |
| 2 | Base | reset, body, links, tables |
| 3 | Book & sheet system | `.book` `.sheet` `.p1` `.a4` `.topbar` `.tb-brand` `.foot` `.to-ix` |
| 4 | Headings & editorial | h1–h4, `.lede`, `.lab`, `.verdict`, `.take`, `.note`, `.panel` |
| 5 | Part & chapter openers | `.gschip` `.hero-tag` `.ch` `.chap-t` `.chips` `.chip` |
| 6 | Section & subtopic bands | `.sec-h` `.sub-h` |
| 7 | Card article | `.card .gsN` `.card-h` `.card-id` `.blk-lab` `.pull` `.intro` `.ex` `.data` `.conc` `.detail-p` `.fig` `.badge-skel` |
| 8 | Index | `.ix-body` `.ix-ch` `.ix-sec` `.ix-line` `.ix-cards` `.ix-compact` |
| 9 | Cover | `.cover-logo` `.cover-contact` |
| 10 | Utility | `.two` `.small` `.skip` |
| 11 | Print (A4) | one sheet = one page, atomicity, colour retention |

**Change protocol:** edit `src/theme.css` (or the relevant partial) → rebuild
(`python scripts/stage2/build.py`) → re-run QA (`python scripts/stage2/qa_check.py`)
→ re-measure any `.a4` sheet heights headless (≤ ~1135px) → update this document +
`design_tokens.md` in the same commit → push.

---

# II. SIBLING BOOK — Dr. CSE · Data & Facts (`final_data_facts.html`)

A second book in the same design system, shipped from this repo. Where it follows
Replica it inherits the rules above; where it differs, §13 below is the spec.

## 13. What kind of book this is

- **Source:** `inputs/updated_data.json` — 83 verified, dated, sourced data cards
  (GS Papers I–III · 12 subjects · 31 section groups · 60 subtopics).
- **Job:** every number a student might quote in an answer — with its data window
  (`DATA:` chip) and its source panel (org · linked title · year · type chip).
- **Verbatim rule carries over:** fact rows are protected content; only chrome
  (labels, headings, panel titles) is editable. No count statistics, same as §11.

## 14. Anatomy of a data card (differs from Replica's card)

```
┌─ card (white rounded box, 3px paper top edge: GS-1 gold / GS-2 teal / GS-3 green)
│  TITLE h4 ······ [ID pill] [DATA: <period> chip]
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ (dashed rule)
│  INNER SECTION (.ssec — gold left bar, spans both columns)
│  SUB-THEME (.sth — teal small caps)
│  · fact row (.row, mono, 2-column flow via .rows{columns:2})
│  · fact row …                     [TABLE .tblwrap — spans both columns]
│  SOURCES panel (.srcs — spans both columns)
└──────────────────────────────────
```

- **Fact rows** are the unit: mono 9.5px, hanging bullet, `break-inside:avoid`.
  Indentation levels `.row.l1…l5` mirror the source's `&nbsp;` nesting.
- **Tables** are atomic (never split across sheets/columns) — the parser
  protects `<table>…</table>` spans from the `<br>` line split (a source table
  may contain `<br>` inside cells).
- **Flowing cards (unique to this book):** a big card may span several sheets.
  Each sheet fragment is a complete `<article class="card … cont-art">` box —
  the continuation re-opens the box with a **CONTINUED strip** (id · title ·
  CONTINUED) and a **dashed top edge**; the card's anchor `#card-<ID>` stays on
  its first fragment. Sheet budget ≈ 900 est-px (headless-verified: every sheet
  exactly 1123px A4).

## 15. Sheet system & book map (110 sheets, as built)

Cover (`.p1`) → Disclaimer & How to Use → **4 index sheets** (2-column, every
level clickable: paper → subject → section → card title) → per paper (GS-III →
GS-II → GS-I): part opener + subject pages (`#ch-N`, each carrying its own
clickable fact-sheet list) + card sheets (88, `data-ch="ch-N"` attribution) →
back cover (`.p1`, companion-guide figure at `max-width:480px`, contact strip).
Page numbers stamped `NNN / 110` in the footer (2 covers unstamped).

## 16. Pipeline (scripts/stage2/datafacts/)

`parse_data.py` (updated_data.json → df_book_map.json; entity decode, 🢥→→
glyph map, table protection, title-dup skip) → `build_book.py` (map →
`src/datafacts/df_*.html` partials + assembled `final_data_facts.html`;
Packer with open-card continuation + row-granularity streaming; table-height
estimator 46 + 24·rows) → `qa_check_df.py` (83 anchors, verbatim, tag balance
incl. `escaped-table-markup` leak check, chrome/page numbers, no stats)
→ `measure_df.py` (headless: heights ≤ 1135px, overflow, click-through,
screenshots into `shots/`).

**Change protocol:** edit `src/datafacts/theme.css` / `inputs/updated_data.json`
→ `python scripts/stage2/datafacts/parse_data.py && python scripts/stage2/datafacts/build_book.py && python scripts/stage2/datafacts/qa_check_df.py`
→ `measure_df.py` green → update this section in the same commit → push.
