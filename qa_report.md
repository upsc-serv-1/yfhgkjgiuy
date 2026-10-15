# qa_report.md — Phase 8 · QA Audit (v3, post-review rebrand rebuild)

**Audited:** 2026-10-16 · **Target:** `final_ebook.html` (assembled artifact, 1.10 MB, 217 sheets)
**Script:** `scripts/stage2/qa_check.py` (re-runnable; exit 1 on any failure) · **Raw data:** `scripts/stage2/qa_report_data.json`
**v3 scope:** user review fixes — renamed to "Replica (Exam Replicable) · Intro to Conclusion"; Dr. CSE logo thin header on every page; page-2 Disclaimer + How to Approach; 2-column master index with clickable subtopics; subject pages carry their own clickable card index (A4); all count statistics removed; INTRODUCTION boxed; syllabus-point line removed; wide DATA in 2 columns. Protected content untouched.

---

## Verdict: PASS — all checklist items green (v3, 2026-10-16)

| # | PLAN.md §6 checklist item | Method | Result |
|---|---|---|---|
| 1 | All 551 v17 cards present | article/id scan of assembled HTML | ✅ 551 articles, 551 unique ids |
| 2 | Protected content survives verbatim | per-block normalized-text containment + per-card digit-sequence multiset (every number/year/percentage), final HTML vs v17 | ✅ 551/551 cards, 0 block mismatches, 0 digit mismatches |
| 3 | Images local, no hotlinks, alt present | img tag scan | ✅ 0 hotlinked, 0 missing alt (external links only for drcse.in / t.me contact, as requested) |
| 4 | Index links resolve; hierarchy consistent | full href/id resolution + heading-level walk | ✅ 0 unresolved, 0 duplicate ids, 0 skipped heading levels |
| 5 | Tone & terminology consistent | editorial audit of NEW text (easy-language rules) | ✅ clean |
| 6 | Design matches book purpose (v3) | browser structure scan + screenshots | ✅ 0 count-stat elements (`.cover-stat`/`.chip.mono`/`SECTION N OF 48` = 0); 546 boxed INTRODUCTION blocks; 0 `.card-micro` syllabus lines; 25 two-column DATA walls; 216 thin "Dr. CSE — Replica" headers; VLM review of 8 key pages found no defects |
| 7 | Navigation works for a student (v3) | headless-browser trusted clicks | ✅ index subtopic "Buddhism" → `#st-2` band; index title → card; subject-page title → card; floating INDEX button → `#ix-master` |
| 8 | Pages fit A4 (v3) | headless-browser height measurement | ✅ every `.a4`/`.p1` sheet ≤ 1135px (index sheets filled 726–924px of ~950 usable; Ethics subject index split across 2 true-A4 sheets) |
| 9 | A4 print CSS | static CSS checks | ✅ `@page A4`, one sheet = one page, `break-inside:avoid` for cards/blocks/figures, INDEX button hidden in print, print-color-adjust exact |
| 10 | HTML sanity | structural checks | ✅ lang/title/meta, font fallbacks, no backdrop-filter, balanced tags, page numbers stamped (`NNN / 217`), no placeholder-text leaks |

## Book facts (v3)

- **551 cards** · 4 parts · 14 chapters · 48 sections · 209 subtopics · 70,145 body words
- **217 sheets** — cover, **page-2 Disclaimer & How to Approach**, **7 master-index sheets (2-column, front position)**, 4 part openers, 14 subject pages (Ethics = 2), chapter content sheets, back cover
- **1.10 MB** HTML (relative image mode, user-locked) + 8.5 MB local images in `assets/images/` (+ `logo_dr_cse.png` 420×140 transparent, extracted from the prototype)
- Fonts via Google Fonts with full system fallback stacks (offline-safe)
- Modular sources: 21 partials + `theme.css` in `src/` — full rebuild chain in HANDOFF.md §next (add `--embed` to `build.py` for a base64 single file)

## v3 review changes (user feedback, 2026-10-16)

1. **Removed all count-analytics** — donut/pie charts, stacked bands, tier bars, dot rows, and
   subtopic heatmaps deleted from every part opener and the (now deleted) "Book at a Glance"
   page. A ready-made card book is for jumping to cards, not studying card-count statistics.
2. **Subject-wise index is now front matter** — retitled "CONTENTS · Every card, subject by
   subject", placed directly after How-to-Use; all 551 card titles are links.
3. **Persistent navigation** — floating INDEX button on every screen (hidden in print) +
   `INDEX` link in every sheet breadcrumb + CONTENTS chips on the cover.
4. **Card-in-a-box redesign** — one card = one white rounded (12px) box, 3px paper-colour top
   edge (GS-1 gold / GS-2 teal / GS-3 green / GS-4 deep), dashed rule under the title,
   labelled blocks: QUOTE (gold panel), INTRODUCTION (teal label), EXAMPLES (green panel),
   DATA (mono panel), CONCLUSION (green panel), DETAIL (sage panel, gold bar).
5. Part openers are now pure navigation: part title + chapter chips + syllabus-section links
   (+ GS-4 theme mini-index kept).

**v3 (this build):**

6. **Renamed + rebranded** — “Replica (Exam Replicable) · Intro to Conclusion”; Dr. CSE logo
   (extracted from the prototype) top-left of the cover and in a thin running header on every
   sheet; footer carries the brand line + page number.
7. **No scary numbers** — cover stat band, “N CARDS / N SECTIONS / N SUBTOPICS” chips,
   “SECTION N OF 48” stamps and index count badges all removed.
8. **Page 2 = Disclaimer + How to Approach** (replaces foreword + how-to-use) with contact
   strip (drcse.in · t.me/dr_cse · email).
9. **Master index: 2-column, every level clickable** — subtopic names (e.g. “Buddhism”) now
   jump to their bands; auto-paginated into 7 true-A4 sheets.
10. **Subject pages carry their own clickable card index** on a true-A4 sheet (Ethics: 2 sheets,
    compact 3-column); stat chips replaced by the index.
11. **Card polish** — INTRODUCTION now a boxed block; syllabus-point micro line removed;
    long DATA walls flow in 2 columns (25 cards, e.g. GS1-HIST-0012).
12. **Thin headers** — book-name/section/subject crumbs removed; cards start directly under
    “Dr. CSE — Replica”.

## Doubts carried to the user gate (non-blocking)

1. Cover is typographic + contact strip (no artwork beyond the logo).
2. Resource-guide PNG sits on the back cover as “Companion resources” — removal is a one-file edit.
3. Ethics subject index spans 2 A4 sheets (149 cards) — the only subject that needs two pages.
4. No per-card mentor callouts (kept the card layer purely verbatim by design).
