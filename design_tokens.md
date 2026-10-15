# design_tokens.md — Phase 3 · Design System

**Generated:** 2026-10-16 · **Status:** Phase-3 deliverable (self-audited) · **Production CSS:** `src/theme.css`
**Truth order:** prototype CSS (extracted verbatim to `scripts/stage2/prototype_style_raw.css`) wins; `DESIGN_MAGZ_SPEC.md` fills gaps (box anatomy, booktabs tables, running footer). All values below are implemented in `src/theme.css`.

---

## 1. Color tokens (prototype parity)

| Token | Value | Use |
|---|---|---|
| `--page` | `#EEF2EE` | Sheet surface (warm sage-ivory) |
| `--desk` | `#D5DCD6` | Screen desk behind sheets (dark-mode: `#0F1514`, sheets unchanged) |
| `--box` | `#F5F8F5` | Panel interiors (data panels, detail panels) — sage-family adaptation of spec's soft-slate box |
| `--ink` | `#1E2A2A` | Body text |
| `--ink-h` | `#16211F` | Headings |
| `--ink2` | `#43514F` | Ledes, secondary text |
| `--mut` | `#5B6B6C` | Labels, crumbs, stamps, captions |
| `--hair` | `rgba(30,42,42,.16)` | Light rules |
| `--hair2` | `rgba(30,42,42,.30)` | Strong rules, dotted index underlines |
| `--teal` | `#4F8F86` | Primary accent: links, data top-rules, examples rule, take callouts |
| `--gold` | `#A97D2B` | Secondary accent: verdict bars, pull-quote bars, detail-panel bars, section kickers |
| `--green` | `#6E9468` | Tertiary accent (skeleton badges pair with gold; heatmaps) |
| `--b1…--b5` | `#DCE9E5 #B4D2CB #7FB3AA #4F8F86 #1F4F52` | 5-step intensity bands (heatmap cells, stacked bands, dot scales) |
| GS chip | `#F7E3CF` / `#8A4308` | Paper chip on part/chapter openers (prototype gschip) |

## 2. Typography (prototype parity; spec fills print-facing roles)

| Role | Font | Size / line | Notes |
|---|---|---|---|
| Display h1 | Fraunces 600 | 42 / 1.02 | Cover + front-matter sheet titles |
| Chapter title | Fraunces 600 | 36 / — | `.chap-t h1` |
| Section (h2) | Fraunces 600 | 22 / 1.12 | |
| Subtopic band (h3) | Fraunces 600 | 15.5 / 1.3 | `.sub-h h3` |
| Card title (h4) | Fraunces 600 | 15 / 1.25 | Card header |
| Body p | IBM Plex Sans 400 | 12 / 1.6 | Card bodies, editorial |
| Lede | IBM Plex Sans 400 | 12.5 / 1.55 | Introductions, front matter |
| Pull-quote | Fraunces 500 italic | 14.5 / 1.45 | `:::quote` blocks |
| Verdict | Fraunces 600 | 18 / 1.28 | Mentor takeaways (NEW text only) |
| Labels `.lab` | IBM Plex Sans 400 | 9.5–10 / — | letterspaced 1.5px, uppercase |
| Data panel | IBM Plex Mono 500 | 10 / 1.6 | `:::data` blocks |
| Stamps / crumbs / ids | IBM Plex Mono 500 | 8.5–10 | Running header, card-id, captions |

Font loading: Google Fonts `Fraunces:opsz,wght@9..144,600` + `IBM Plex Sans:wght@400;600` + `IBM Plex Mono:wght@500` with full system fallback stacks (Georgia / system-ui / ui-monospace) — offline-safe degradation, no layout shift.

## 3. Page geometry

- Sheet: **794 px** wide, padding `36px 48px 30px`, screen margin-bottom 18px, desk shadow.
- Cover `.p1`: min-height **1123 px** (true A4 ratio at 96 dpi) — the only fixed-height sheet.
- Content column: effectively ~698 px; ledes capped at 640 px.
- Print: `@page A4, margin 10mm`, sheet shadow/padding stripped, **one sheet = one page** (`break-after:page`).

## 4. Component catalog (v17 block → component)

| v17 block | Component (class) | Anatomy |
|---|---|---|
| card wrapper | `.card` + `#card-<ID>` | header: `h4` title + `.card-id` mono stamp + `.card-micro` microtopic line; then ACTUAL blocks in source order |
| `:::quote` | `.pull` | gold 3px left bar; Fraunces italic; `.attr` mono attribution; multi-quote → sequence of `.pull` |
| `:::introduction` | `.lede` paragraph(s) | plain magazine lead — no box |
| `:::examples` | `.ex` | `.blk-lab` "Examples"; teal 2px left rule; verbatim lists |
| `:::data` | `.data` | box bg + hairline border + **teal 2px top rule** (booktabs flavor, spec §6); mono rows |
| `:::conclusion` | `.conc` | hairline top rule; `.blk-lab` "Conclusion" |
| `:::detail label` | `.detail-p` | box bg + hairline + **gold 3px left bar** (spec drill-box anatomy); gold mono label header |
| `:::image` | `figure.fig` | local relative `assets/images/…`, hairline border, mono caption (card id + subject) |
| practice skeleton | `.badge-skel` | gold outline chip in card header (5 cards) |
| editorial takeaway | `.verdict` / `.take` | gold-bar Fraunces statement / teal-bar tinted note — **NEW text only** |

Structural components: `.topbar` (brand / `.crumb` / `.stamp` with `.pg-n` auto page number), `.foot` (colophon + page number, spec §7), `.sec-h` section band (gold mono kicker + h2 + card count + subtopic chips), `.sub-h` subtopic band, `.hero` + `.gschip` part/chapter openers, `.chips`/`.chip` quick-nav, index rows `.ix-ch`/`.ix-sec`/`.ix-sub`/`.ix-cards`.

## 5. Analytics component library (recreated SVG types I1–I9)

Construction: all inline SVG or pure CSS; **data = book's own taxonomy** (from `book_map.json`); no PYQ-marks data; never copied 1:1 from the prototype.

| ID | Component | Construction | Data binding |
|---|---|---|---|
| I1 | Donut | SVG circle strokes, 5-band palette, center total | cards per paper / per subject |
| I2 | Subject bands | `.band` flex 100%-stacked | 14 subjects × card counts |
| I3 | Tier table | `.tier` pills (b1–b5 bg) + count | heaviest section_groups per paper |
| I4 | Heatmap | `.hm-row` grid of `.hm-c` cells (b1–b5) | cards per subtopic, per subject |
| I5 | Top-10 table | booktabs rows + `.dots` scale | subtopics by card count |
| I6 | Subject illustration | abstract SVG geometry, palette-consistent | section-group split of the chapter |
| I7 | Card anatomy diagram | exploded labeled sample card | static (How-to-Use) |
| I8 | Route tables | `.chips` timeline per route | 30/60/90-day plans (fixed editorial) |
| I9 | Cross-paper band | two-row `.band` alignment | section_group names shared across papers |

## 6. Rules of use

1. Component classes above are the **only** vocabulary — no ad-hoc styling in partials; new needs go into `theme.css` first.
2. Verbatim card content is never restyled beyond these components; block order follows the card's ACTUAL blocks.
3. Gold = editorial judgment; teal = content/links; green = auxiliary. Don't mix accent roles.
4. Print rules are global in `theme.css` §12 — partials must not add `page-break` styles.
5. Every sheet partial opens with `.topbar` and closes with `.foot`; the build script stamps page numbers into `.pg-n`.

## 7. Self-audit (Phase-3 gate)

- [x] Every token value traces to prototype CSS (extracted raw file committed) or documented spec adaptation (`--box`)
- [x] All v17 block types have exactly one component mapping
- [x] Fonts load with fallbacks; no `backdrop-filter`; no external assets besides Google Fonts (images all local)
- [x] Print CSS: one sheet = one page, break control for cards/blocks/figures, colors exact
- [x] Analytics library covers all 9 illustration types planned in `ebook_structure.md` §6
