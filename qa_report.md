# qa_report.md — Phase 8 · QA Audit (v2, post-review rebuild)

**Audited:** 2026-10-16 · **Target:** `final_ebook.html` (assembled artifact, 1.18 MB, 238 sheets)
**Script:** `scripts/stage2/qa_check.py` (re-runnable; exit 1 on any failure) · **Raw data:** `scripts/stage2/qa_report_data.json`
**v2 scope:** user review fixes — analytics visuals removed, clickable subject-wise index moved to
front matter, card-in-rounded-box redesign, floating INDEX button. Protected content untouched.

---

## Verdict: PASS — all checklist items green

| # | PLAN.md §6 checklist item | Method | Result |
|---|---|---|---|
| 1 | All 551 v17 cards present | article/id scan of assembled HTML | ✅ 551 articles, 551 unique ids |
| 2 | Protected content survives verbatim | per-block normalized-text containment + per-card digit-sequence multiset (every number/year/percentage), final HTML vs v17 | ✅ 551/551 cards, 0 block mismatches, 0 digit mismatches (labels QUOTE/INTRODUCTION/DATA are NEW chrome text, no digits) |
| 3 | Images local, no hotlinks, alt present | img tag scan | ✅ 38 imgs, 0 hotlinked, 0 missing alt |
| 4 | Index links resolve; hierarchy consistent | full href/id resolution + heading-level walk | ✅ 1,678 internal links, 0 unresolved, 0 duplicate ids, 0 skipped heading levels |
| 5 | Tone & terminology consistent | Phase-5 editorial audit + banned-words scan of NEW text | ✅ clean (see review_notes.md) |
| 6 | Design matches book purpose (v2) | browser click-through + screenshots | ✅ zero analytics elements (`hm-c/band/dots/tier` = 0); cards render as white 12px-rounded boxes with paper-colour top edge; QUOTE/INTRODUCTION/EXAMPLES/DATA/CONCLUSION labels present |
| 7 | Navigation works for a student (v2) | headless-browser trusted clicks | ✅ cover → CONTENTS chip → index → card title click lands card at viewport top (y 19,503); INDEX button visible on every screen, jumps to `#ix-master` |
| 8 | A4 print CSS | static CSS checks | ✅ `@page A4`, one sheet = one page, `break-inside:avoid` for cards/blocks/figures, INDEX button hidden in print, print-color-adjust exact |
| 9 | HTML sanity | structural checks | ✅ lang/title/meta, font fallbacks, no backdrop-filter, balanced tags, page numbers stamped (`NNN / 238`) |

## Book facts (v2)

- **551 cards** · 4 parts · 14 chapters · 48 sections · 209 subtopics · 70,145 body words
- **238 sheets** — cover, foreword, how-to-use, **5 index sheets (front position, right after How-to-Use)**, 4 part openers, chapter sheets, back cover
- **1.18 MB** HTML (relative image mode, user-locked) + 8.5 MB local images in `assets/images/`
- Fonts via Google Fonts with full system fallback stacks (offline-safe)
- Modular sources: 20 partials + `theme.css` in `src/` — rebuild with `python scripts/stage2/build.py` (add `--embed` for a base64 single file)

## v2 review changes (user feedback, 2026-10-16)

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

## Doubts carried to the user gate (from Phase 5, non-blocking)

1. Cover is typographic (no artwork) — matches the prototype's language.
2. Resource-guide PNG sits on the back cover as "Companion resources" — removal is a one-file edit.
3. Part openers / index sheets exceed one A4 screen and flow onto continuation pages in print.
4. No per-card mentor callouts (kept the card layer purely verbatim by design).
