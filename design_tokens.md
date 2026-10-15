# design_tokens.md — Phase 3 · Design System (v2, post-review)

**Generated:** 2026-10-16 · **v2 updated:** 2026-10-16 (user review) · **Status:** production · **Production CSS:** `src/theme.css`
**Truth order:** prototype CSS (extracted verbatim to `scripts/stage2/prototype_style_raw.css`) wins for tokens/typography/sheet system; the user's card-box reference screenshot (rounded white cards, labelled blocks) drives the CARD COMPONENT layer, blended into the sage-gold palette; `DESIGN_MAGZ_SPEC.md` fills remaining gaps. All values below are implemented in `src/theme.css`.

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
| `--teal` | `#4F8F86` | Primary accent: links, INTRODUCTION labels, data top-rules, take callouts, GS-2 card top edge |
| `--gold` | `#A97D2B` | Secondary accent: verdict bars, QUOTE labels + pull panels, detail bars, section kickers, GS-1 card top edge, INDEX button border |
| `--green` | `#6E9468` | Tertiary accent: EXAMPLES/CONCLUSION labels + tinted panels, GS-3 card top edge |
| `--deep` | `#1F4F52` | DATA labels, GS-4 card top edge |
| `--card` | `#FFFFFF` | Card box face (white on sage sheet = "separate colour") |
| `--t-gold` / `--t-teal` / `--t-green` | `rgba(169,125,43,.08)` / `rgba(79,143,134,.08)` / `rgba(110,148,104,.11)` | Whisper-quiet block tints inside cards |
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

## 4. Component catalog (v2: ONE CARD = ONE ROUNDED BOX)

Card box anatomy (user reference screenshot, blended with prototype palette):
`.card` = white `--card` face · 12px radius · hairline border · soft shadow · 18–22px padding,
with a **3px paper-colour top edge**: `.gs1` gold · `.gs2` teal · `.gs3` green · `.gs4` deep.
Header row: `h4` title + `.card-id` mono pill, over a **dashed rule**; then blocks in source order.

| v17 block | Component (class) | Anatomy (v2) |
|---|---|---|
| card wrapper | `.card .gsN` + `#card-<ID>` | white rounded box + paper-colour top edge; header `h4` + `.card-id` pill + dashed rule + `.card-micro` |
| `:::quote` | `.pull` + label | **QUOTE** gold label; pale-gold panel, gold 3px left bar, rounded right; Fraunces italic; `.attr` mono attribution |
| `:::introduction` | `.intro` + label | **INTRODUCTION** teal label; plain body — the liftable opening |
| `:::examples` | `.ex` + label | **EXAMPLES** green label; pale-green panel, green 2px left rule; verbatim lists |
| `:::data` | `.data` + label | **DATA** deep label; sage box + hairline + teal 2px top rule, 8px radius; mono rows (booktabs, spec §6) |
| `:::conclusion` | `.conc` + label | **CONCLUSION** green label; pale-green rounded panel |
| `:::detail label` | `.detail-p` | sage box + gold 3px left bar, rounded right; gold mono label header (spec drill-box) |
| `:::image` | `figure.fig` | local relative `assets/images/…`, hairline border, 6px radius, mono caption |
| practice skeleton | `.badge-skel` | gold outline chip in card header (5 cards) |
| editorial takeaway | `.verdict` / `.take` | gold-bar Fraunces statement / teal-bar tinted note — **NEW text only** |

Structural components: `.topbar` (brand / `.crumb` with trailing **INDEX** link / `.stamp` with `.pg-n`), `.foot` (colophon + page number, spec §7), `.sec-h` section band (gold mono kicker + h2 + count + subtopic chips), `.sub-h` subtopic band, `.gschip`/`.hero-tag` openers, `.chips`/`.chip` quick-nav (links only — count chips are spans), index rows `.ix-ch`/`.ix-sec`/`.ix-sub`/`.ix-cards`.

## 5. Navigation system (v2 — replaces the analytics library)

**User decision (2026-10-16 review): count-analytics visuals are REMOVED from the book.**
This is a ready-made card book — students jump to cards; card-count pies/bands/heatmaps add
nothing. The v1 analytics library (donut I1, bands I2, tiers I3, heatmap I4, dots I5,
subject illustration I6, cross-paper band I9) is deleted from `theme.css` and all partials.
Kept: I7-style card anatomy demo (How-to-Use, static) and I8 route tables (editorial).

What replaces it:

| Element | Where | Behaviour |
|---|---|---|
| Subject-wise index (`bm1_index.html`) | **front matter**, right after How-to-Use | all 551 card titles are links, grouped paper → subject → section → subtopic; `#ix-master` anchor |
| Floating INDEX button (`.to-ix`) | every screen, bottom-right | jumps to `#ix-master`; hidden in print |
| Breadcrumb INDEX link | every content sheet topbar | `… · INDEX` appended to the crumb trail |
| CONTENTS chips | cover + foreword + How-to-Use | direct links into the index and how-to-use |
| Part openers | 4 sheets | part title + chapter chips + syllabus-section links (+ GS-4 theme mini-index) — pure navigation, no charts |

## 6. Rules of use

1. Component classes above are the **only** vocabulary — no ad-hoc styling in partials; new needs go into `theme.css` first.
2. Verbatim card content is never restyled beyond these components; block order follows the card's ACTUAL blocks.
3. Gold = editorial judgment; teal = content/links; green = auxiliary. Don't mix accent roles.
4. Print rules are global in `theme.css` §12 — partials must not add `page-break` styles.
5. Every sheet partial opens with `.topbar` and closes with `.foot`; the build script stamps page numbers into `.pg-n`.

## 7. Self-audit (v2)

- [x] Every token value traces to prototype CSS, the user's card-box reference, or a documented spec adaptation
- [x] All v17 block types have exactly one component mapping, each with a visible coloured label
- [x] Fonts load with fallbacks; no `backdrop-filter`; no external assets besides Google Fonts (images all local)
- [x] Print CSS: one sheet = one page, `break-inside:avoid` for cards (cards are atomic boxes), INDEX button hidden, colors exact
- [x] Zero analytics components remain (verified in browser: `.hm-c/.band/.dots/.tier` count = 0)
- [x] Navigation verified by trusted click-through in a real browser (index link → card lands at viewport top)
