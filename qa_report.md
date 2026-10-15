# qa_report.md — Phase 8 · QA Audit

**Audited:** 2026-10-16 · **Target:** `final_ebook.html` (assembled artifact, 1.23 MB, 239 sheets)
**Script:** `scripts/stage2/qa_check.py` (re-runnable; exit 1 on any failure) · **Raw data:** `scripts/stage2/qa_report_data.json`

---

## Verdict: PASS — all checklist items green

| # | PLAN.md §6 checklist item | Method | Result |
|---|---|---|---|
| 1 | All 551 v17 cards present | article/id scan of assembled HTML | ✅ 551 articles, 551 unique ids |
| 2 | Protected content survives verbatim | per-block normalized-text containment + per-card digit-sequence multiset (every number/year/percentage), final HTML vs v17 | ✅ 551/551 cards, 0 block mismatches, 0 digit mismatches |
| 3 | Images local, no hotlinks, alt present | img tag scan | ✅ 38 imgs, 0 hotlinked, 0 missing alt (image URLs → local files is by-design and verified via manifest) |
| 4 | TOC + index links resolve; hierarchy consistent | full href/id resolution + heading-level walk | ✅ 1,695 internal links, 0 unresolved, 0 duplicate ids, 0 skipped heading levels |
| 5 | Tone & terminology consistent | Phase-5 editorial audit + banned-words scan of NEW text | ✅ clean (see review_notes.md) |
| 6 | Visual parity with prototype | design tokens extracted from prototype CSS; component catalog 1:1 (design_tokens.md) | ✅ fonts (Fraunces / IBM Plex Sans / IBM Plex Mono), sage-gold palette, sheet/topbar/verdict/heatmap components |
| 7 | A4 print CSS | static CSS checks | ✅ `@page A4`, one sheet = one page, break-avoid for cards/blocks/figures, print-color-adjust exact |
| 8 | Spelling/grammar on NEW text | Phase-5 read-through + marker scan | ✅ no TODO/FIXME/lorem; easy-language rules verified |
| 9 | HTML sanity | structural checks | ✅ lang/title/meta, font fallbacks, no backdrop-filter, balanced tags, page numbers stamped (`NNN / 239`) |

## Book facts

- **551 cards** · 4 parts · 14 chapters · 48 sections · 209 subtopics · 70,145 body words
- **239 sheets** (screen pages) — cover counts as 1; every sheet carries running topbar + stamped page number + colophon foot
- **1.23 MB** HTML (relative image mode, user-locked) + 8.5 MB local images in `assets/images/`
- Fonts via Google Fonts with full system fallback stacks (offline-safe)
- Modular sources: 21 partials + `theme.css` in `src/` — rebuild with `python scripts/stage2/build.py` (add `--embed` for a base64 single file)

## Doubts carried to the user gate (from Phase 5, non-blocking)

1. Cover is typographic (no artwork) — matches the prototype's language.
2. Resource-guide PNG sits on the back cover as "Companion resources" — removal is a one-file edit.
3. Part openers / index sheets exceed one A4 screen and flow onto continuation pages in print.
4. No per-card mentor callouts (kept the card layer purely verbatim by design).
