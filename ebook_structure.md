# ebook_structure.md — Phase 2 · Book Architecture

**Book:** PYQ Nano Analysis — GS Mains · The Answer-Writing Playbook
**Generated:** 2026-10-16 · **Status:** Phase-2 deliverable (self-audited) · **Machine-readable map:** `scripts/stage2/book_map.json`
**Locked by user (Phase-1 gate, 2026-10-16):** relative image paths · Part=GS paper → Chapter=subject → Section=section_group → card-group=subtopic · GS-4 strong internal navigation + mini-index · prototype-type SVG illustrations recreated for our content · detail/multi-quote full rendering · practice-skeleton marking.

---

## 1. Architecture in one line

**Book → Front matter → Part (= GS paper, 4) → Chapter (= subject, 14) → Section (= section_group, 48) → Card group (= subtopic, 209) → Cards (551, VERBATIM)** — then Back matter (GS-wise master index, back cover).

This hierarchy is exactly the user-assigned card taxonomy (`paper → subject → section_group → microtopic → subtopic`). Nothing is re-invented; navigation is generated from `book_map.json`.

## 2. Prototype anatomy (what we adopt, what we adapt)

The prototype (39 A4 "sheets", 794 × 1123 px design grid) is the design truth. Its architecture, reverse-engineered in `scripts/stage2/prototype_skeleton.md`:

| Prototype pattern | Class vocabulary | Our adaptation |
|---|---|---|
| **Sheet page unit** — 794px page, 36/48px padding, shadow on desk background, only the cover is `min-height` A4 | `.book` `.sheet` `.p1` `.desk` | Adopted 1:1. Sheets flow with auto height; `@media print` maps 1 sheet → 1 A4 page. |
| **Running header** — logo, brand, breadcrumb, stamp, hairline rule | `.topbar` `.logo` `.brand` `.crumb` `.stamp` `.rule` | Adopted. Crumb = `GS-1 · History · Art and Culture`; stamp = sheet label + page number (auto-numbered at build). |
| **Magazine article pages** — h1/h2 in Fraunces, lede paragraphs, verdict callouts, labeled stat rows | `h1` `.lede` `.lab` `.verdict` `.note` `.take` | Adopted for card articles and editorial text. |
| **Hero chapter openers** — split hero with chip, big numeral, intro column | `.hero` `.hero-l` `.hero-r` `.gschip` `.chdiv` | Adopted for the 4 part openers + 14 chapter openers. |
| **Analytics visual types** — marks-share donut, subject bands, tier tables, heatmap grids, dot scales | `.band` `.tier` `.dots` `.ovc` `.hm-*` `.hmh-*` `.ov-*` | **Recreated with OUR card data** (never PYQ marks data): card-share donuts, subject bands, subtopic heatmaps, section tier tables. All inline SVG / CSS. |
| **Per-subject illustrations** | `.illus` `.ill-<subject>` × 2 each | Recreated: one abstract chapter-opener visual per subject driven by its section-group split. |
| **Index pages** — compact hierarchical rows | `.fl-sec` `.fl-mic` `.fl-sub` `.r-*` `.flat-h` `.subj-h` | Adopted for our GS-wise master index (sec → subtopic → card links). Microtopic level shown as small row label where useful. |
| **Content rows** — question list rows | `.qm` `.qr` `.qx` `.qtp` (~3,400 questions) | **NOT adopted** — our unit is the full article card, not a question row. We use the magazine-article style from `DESIGN_MAGZ_SPEC.md` for card bodies. |
| **Practice Set / Papers by Year / More from Dr. CSE** | `.pr-*` `.topper` `.qt` | **NOT adopted as content** (user declined extra sections). The back cover carries only a compact companion-resources panel (see §8). |

## 3. Book map — parts & chapters

Global chapter numbering 1–14 (used in anchors, filenames, topbar crumbs). Subtopics alphabetical within each section group; v17 section-group order preserved.

| Part | Ch # | Chapter (= subject) | Cards | Sections | Subtopics | Words | Est. sheets | src file |
|---|---|---|---|---|---|---|---|---|
| GS-1 | 1 | History | 54 | 4 | 21 | 7,885 | ~20 | `ch01_history.html` |
| GS-1 | 2 | Geography | 33 | 3 | 9 | 4,099 | ~11 | `ch02_geography.html` |
| GS-1 | 3 | Society | 11 | 5 | 9 | 1,836 | ~5 | `ch03_society.html` |
| GS-2 | 4 | Polity | 43 | 4 | 20 | 4,744 | ~12 | `ch04_polity.html` |
| GS-2 | 5 | Governance | 32 | 3 | 11 | 4,436 | ~12 | `ch05_governance.html` |
| GS-2 | 6 | International Relations | 26 | 3 | 6 | 4,111 | ~11 | `ch06_ir.html` |
| GS-2 | 7 | Social Justice | 15 | 3 | 8 | 2,127 | ~6 | `ch07_social-justice.html` |
| GS-3 | 8 | Indian Economy | 28 | 3 | 14 | 2,902 | ~8 | `ch08_economy.html` |
| GS-3 | 9 | Internal Security | 37 | 4 | 13 | 3,733 | ~10 | `ch09_security.html` |
| GS-3 | 10 | Agriculture | 22 | 3 | 14 | 2,243 | ~6 | `ch10_agriculture.html` |
| GS-3 | 11 | Science & Technology | 39 | 3 | 10 | 4,952 | ~13 | `ch11_snt.html` |
| GS-3 | 12 | Environment | 40 | 3 | 13 | 7,231 | ~18 | `ch12_environment.html` |
| GS-3 | 13 | Disaster Management | 22 | 2 | 10 | 3,174 | ~9 | `ch13_disaster.html` |
| GS-4 | 14 | Ethics, Integrity & Aptitude | 149 | 5 | 51 | 16,672 | ~41 | `ch14_ethics.html` |
| | | **Total** | **551** | **48** | **209** | **70,145** | **~182** | |

Full section→subtopic→card tree with anchors: `scripts/stage2/book_map.json` (`chapters_flat`).

## 4. Reading flow & page anatomy

1. **Cover** (`fm1_cover.html`) — the only `min-height:1123px` sheet. Typographic cover (Fraunces h1, gold accent), stat strip: 551 cards · 4 papers · 14 subjects · 209 subtopics. Mentor byline line.
2. **Foreword** (`fm2_foreword.html`) — 1–2 sheets, NEW text, mentor voice, easy-language rules.
3. **How to Use This Book** (`fm3_how_to_use.html`) — 2–3 sheets: how a card is built (anatomy diagram of one sample card with labeled blocks), how to navigate (topbar crumb, index, part mini-indexes), and the **30/60/90-day reading routes** (three route tables: revision sprint / steady build / deep foundation), plus a small "read a heatmap" legend for the part-opener visuals.
4. **The Book at a Glance** (`fm4_glance.html`) — 2–3 sheets of recreated analytics (§6).
5. **Part openers** (`pt1..pt4_*.html`) — 1 sheet each (GS-4: 2 sheets incl. mini-index). Big part numeral, paper chip, "what's inside" chapter list with card counts, recreated subject-split donut + heaviest-subtopics tier table, 3–4 sentence mentor guidance (NEW text).
6. **Chapter openers** (first sheet of each `chNN_*.html`) — hero header: chapter number, subject display name, meta row (cards · subtopics · est. read time), subject illustration (recreated SVG), 2–3 sentence intro (NEW text), "In this chapter" section list with anchors.
7. **Card pages** — within a chapter: each section_group opens on a fresh sheet with a section band header; each subtopic opens a card group with a group header band; cards flow as magazine articles under it. NOT one-card-per-page — cards are compact articles (~127 words mean), 3–5 per sheet.
8. **Master index** (`bm1_index.html`) — GS-wise → subject → section_group → subtopic → card titles (each linking to its card anchor). ~7 sheets.
9. **Back cover** (`bm2_back_cover.html`) — closing panel + compact companion-resources strip (§8 proposal).

Estimated total: ~205 sheets (≈205 printed A4 pages).

## 5. Card rendering spec (VERBATIM layer)

Every card renders, in this wrapper:

```
<article class="card" id="card-GS1-HIST-0001">
  <header>  card_title (h4, Fraunces) · mono card-id stamp · microtopic label (small, muted)
  <blocks>  ACTUAL blocks in source order — never the sections: metadata list
</article>
```

| Block | Render |
|---|---|
| `:::quote` | Pull-quote panel (Fraunces, gold hairline); attribution line if present. **Multi-quote cards: every quote in sequence, verbatim.** |
| `:::introduction` | Lede paragraph(s). |
| `:::examples` | "Examples" labeled block; lists kept exactly (order + nesting). |
| `:::data` | Data panel (IBM Plex Mono), dash/table rows exactly as source. |
| `:::conclusion` | "Conclusion" labeled block closing the card. |
| `:::detail label="X"` | Labeled panel with mono label header X — detail cards (75) render as a sequence of labeled panels. |
| `:::image <url>` | `<figure>` → local `assets/images/<normalized>.png|jpg` (relative path), alt text derived from card title + subject, caption line with card id. |

Special cases (locked):
- **5 practice-skeleton cards** (GS3-ENVI-0462, GS3-DISA-0483, GS3-INTE-0517, GS3-INTE-0534, GS3-INTE-0543): badge `PRACTICE SKELETON` in card header; bodies verbatim; no forced intro/conclusion styling.
- **5 cards without intro/conclusion**: layout does not add them.
- **Images**: 37 files, all local; card GS4-ETHI-0721 has 2 images.
- Protected content (quotes, numbers, names, list items) — byte-identical from v17; QA re-diff against v17.

## 6. Illustration plan (recreated SVG types)

All inline SVG/CSS (editable, print-safe), driven by **our card data** only:

| # | Prototype type | Recreation | Placement |
|---|---|---|---|
| I1 | Marks-share donut | Card-share donut by paper (98/116/188/149) + per-part subject split | `fm4_glance`, 4 part openers |
| I2 | Subject year-band chart | 14-subject card-count bands (100% stacked) | `fm4_glance` |
| I3 | Tier table | "Heaviest section groups" tier rows (cards + share) per paper | 4 part openers |
| I4 | Heatmap grid | Subtopic weight heatmap (cards per subtopic) per subject — section_group rows × intensity dots | 4 part openers (compact) |
| I5 | Top-10 subtopic table | Top subtopics by card count, per paper | 4 part openers |
| I6 | Subject illustration | Abstract geometric visual per subject (14), palette-consistent, echoing prototype's `ill-<subject>` style | 14 chapter openers |
| I7 | Card anatomy diagram | Labeled exploded view of a sample card | `fm3_how_to_use` |
| I8 | Route tables | 30/60/90-day routes as chip-timelines | `fm3_how_to_use` |
| I9 | Cross-paper theme band | Themes appearing in multiple papers (e.g., Governance ↔ Ethical Governance, Environment ↔ Disaster) — computed from section_group names | `fm4_glance` |

No PYQ-marks analytics are reproduced — the data behind every visual is the book's own 551-card taxonomy.

## 7. Navigation & anchor scheme

| Object | Anchor | Example |
|---|---|---|
| Front-matter sheets | `#fm-<name>` | `#fm-cover`, `#fm-foreword`, `#fm-howto`, `#fm-glance` |
| Part openers | `#pt-gs1` … `#pt-gs4` | |
| Chapters | `#ch-1` … `#ch-14` | |
| Sections | `#sg-1` … `#sg-48` | global numbering |
| Subtopics | `#st-1` … `#st-209` | global numbering |
| Cards | `#card-<CARD_ID>` | `#card-GS1-HIST-0001` — all 551, QA-checked |

Navigation elements:
1. **Topbar crumb** on every sheet: `GS-1 · History · Art and Culture` (paper · subject · current section), brand left, stamp right (`PYQ NANO · GS MAINS` + auto sheet number).
2. **Master index** (`bm1_index.html`): GS-wise → subject → section_group → subtopic → card titles. Compact `fl-*` rows. GS-4's 51-subtopic block gets its own sheet + is duplicated in miniature on the GS-4 part opener (locked mini-index).
3. **Part opener "what's inside"**: chapter list with card counts (links).
4. **Chapter opener "In this chapter"**: section list with subtopic counts (links).
5. **Section quick-nav chips** at each section_group header (subtopic chips) — applied to ALL chapters (GS-4 gets them automatically given 51 subtopics).
6. Print TOC: the master index prints first in `@media print` after cover (linked page numbers omitted in HTML — anchors resolve on click; print users navigate by sheet order).

## 8. Open-question proposal — `upsc_readymade_resource_guide.png`

**Proposal:** do NOT use as cover art (the prototype cover is typographic; a product-guide image would break the design language). Instead, place it — scaled to a compact figure — on the **back-cover sheet** as a "Companion Resources" panel (echoing the prototype's `pr-*` product-card row, reduced to one modest strip), alt-texted and locally referenced. If the user declines at the Phase-8 gate, removal is one partial (`bm2_back_cover.html`) — zero impact on the 551-card body. Default until then: **include on back cover only.**

## 9. src/ decomposition (Phase 4 build units)

```
src/
  fm1_cover.html            fm2_foreword.html       fm3_how_to_use.html
  fm4_glance.html           pt1_gs1_opener.html     pt2_gs2_opener.html
  pt3_gs3_opener.html       pt4_gs4_opener.html     (incl. GS-4 mini-index)
  ch01_history.html … ch14_ethics.html             (14 chapter partials)
  bm1_index.html            bm2_back_cover.html
  theme.css                 (Phase 3: tokens + components)
```
21 partials + `theme.css`. `build.py` concatenates in fixed order, inlines `theme.css` into a single `<style>`, auto-numbers sheets (stamp), and writes `final_ebook.html` at repo root. Relative image paths stay as-is (`assets/images/…`) — user-locked. Optional `--embed` flag inlines images as base64 for a portable single file (not the default).

## 10. Explicitly OUT (user-declined — do not add)

Quick-revision sheets · template appendix · PYQ-trend tables · practice question sets · "More from Dr. CSE" multi-product promo · any restoration of the ~238 cards cut from v17.

## 11. Self-audit (Phase-2 gate)

- [x] 551/551 cards mapped (build assert: 551 = Σ chapters)
- [x] 48 sections, 209 subtopics, hierarchy = user taxonomy exactly
- [x] Every card has a unique anchor; anchors globally unique (fm/pt/ch/sg/st/card namespaces)
- [x] All 37 images local; relative-path policy locked
- [x] Prototype types cataloged; every illustration recreated from our own data
- [x] Extra sections limited to Foreword + How-to-Use (user-locked); back-cover proposal isolated and reversible
- [x] New-text surfaces identified (foreword, how-to-use, part/chapter intros, callouts) — all subject to easy-language + mentor-tone rules in Phase 4/5
