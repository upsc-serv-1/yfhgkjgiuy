# Dr. CSE — eBook Library (branch `ebook-build`)

Two HTML eBooks in one repo, sharing the Dr. CSE design system:

| Book | Artifact | Contents |
|---|---|---|
| **Replica (Exam Replicable) · Intro to Conclusion** | `final_ebook.html` | 551 UPSC GS Mains answer-writing cards, 217 A4 sheets |
| **Dr. CSE — Data & Facts** | `final_data_facts.html` | 83 verified, dated, sourced data fact-sheets (GS Papers I–III), 110 A4 sheets |

Both are magazine-style, editable, print-exact HTML books. Open either file in any
browser; print to A4 with background graphics on for a clean paper copy.

**This branch (`ebook-build`) is the project.** GitHub `main` contains an old, superseded project — ignore it.

## Any agent picking this up

1. Read `HANDOFF.md` (live status) → `PLAN.md` (full plan + iron rules) → `DESIGN.md` (§I Replica spec, §II Data & Facts spec).
2. Content truth: Book 1 `inputs/merged_publish_ready_v17.md` (551 cards, final); Book 2 `inputs/updated_data.json` (83 data cards).
3. Design truth: `inputs/prototype_pyq_nano_gs_mains.html` for structure/tokens only (spec fills gaps: `inputs/DESIGN_MAGZ_SPEC.md`); user review decisions v2/v3 override both.
4. Work only on `ebook-build`; commit + push after every phase (`phase-N: summary`).
5. Card bodies are verbatim-protected (quotes, numbers, names, data lists, fact rows). New text = easy exam language.
6. No count-analytics, no card-count statistics — removed by user review; never reintroduce (see DESIGN.md §11).

## Rebuild chains (must stay ALL GREEN)

- **Book 1 (Replica):** `python scripts/stage2/convert_cards.py && python scripts/stage2/build_front.py && python scripts/stage2/build_back.py && python scripts/stage2/build.py && python scripts/stage2/qa_check.py`
- **Book 2 (Data & Facts):** `python scripts/stage2/datafacts/parse_data.py && python scripts/stage2/datafacts/build_book.py && python scripts/stage2/datafacts/qa_check_df.py && python scripts/stage2/datafacts/measure_df.py`

## Deliverables

Book 1: `content_inventory.md` → `ebook_structure.md` → `design_tokens.md` → `DESIGN.md` → `src/` partials → `review_notes.md` → `toc_index.md` → `final_ebook.html` → `qa_report.md`

Book 2: `inputs/updated_data.json` → `scripts/stage2/datafacts/df_book_map.json` → `src/datafacts/` partials → `final_data_facts.html` (QA + measurement green)
