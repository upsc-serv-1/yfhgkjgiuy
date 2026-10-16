# REPLICA (Exam Replicable) · Intro to Conclusion — Dr. CSE

HTML eBook — 551 polished UPSC GS Mains answer-writing cards as one magazine-style,
editable, print-exact HTML book. Open `final_ebook.html` in any browser; print to A4
with background graphics on for a clean paper copy.

**This branch (`ebook-build`) is the project.** GitHub `main` contains an old, superseded project — ignore it.

## Any agent picking this up

1. Read `HANDOFF.md` (live status) → `PLAN.md` (full plan + iron rules) → `DESIGN.md` (design spec of the shipped book).
2. Content truth: `inputs/merged_publish_ready_v17.md` (551 cards, final).
3. Design truth: `inputs/prototype_pyq_nano_gs_mains.html` for structure/tokens only (spec fills gaps: `inputs/DESIGN_MAGZ_SPEC.md`); user review decisions v2/v3 override both.
4. Work only on `ebook-build`; commit + push after every phase (`phase-N: summary`).
5. Card bodies are verbatim-protected (quotes, numbers, names, data lists). New text = easy exam language.
6. No count-analytics, no card-count statistics — removed by user review; never reintroduce (see DESIGN.md §11).

## Deliverables

`content_inventory.md` → `ebook_structure.md` → `design_tokens.md` → `DESIGN.md` → `src/` partials → `review_notes.md` → `toc_index.md` → `final_ebook.html` → `qa_report.md`
