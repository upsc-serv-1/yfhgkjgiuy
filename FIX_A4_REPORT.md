# Fix-A4 Report — Dr. CSE · Data & Facts structural repair (Phases 0–9)

**Book:** `final_data_facts.html` (110 A4 sheets) + `final_data_facts.pdf` (110 pages)
**Branch:** `ebook-build` · **Phases:** 0–9 complete, every phase gated and green
**Deliverables:** `final_data_facts.html` (editable master), `final_data_facts.pdf`
(A4 print export), `inputs/updated_data.json` (source of truth — restructured,
canonical, highlight-marked), full modular `src/datafacts/` partials.

## Final validation — all 17 checklist items PASS (`verify_phase9.py`)

| # | Check | Result |
|---|-------|--------|
| 1 | A4 dimensions, preview + PDF | PASS — 110 sheets exactly 794×1123px; PDF 595.9×842.9pt A4, 110 pages |
| 2 | Disclaimer page fills properly | PASS — 56% fill, footer pinned at 24px (was: half-filled, footer floating at 580px) |
| 3 | Index order + no awkward splits | PASS — GS-I→GS-II→GS-III, subjects atomic, 0 orphaned headers |
| 4 | Footer consistent on every page | PASS — 108 stamped sheets all footGap=24px (2 covers exempt by design) |
| 5 | No content clipping | PASS — 0 horizontal overflow, 0 over-A4 sheets |
| 6 | No orphaned headings | PASS — DOM last-element scan, all sheets (Manufacturing Sector class included by construction) |
| 7 | Cards flow, no excess whitespace | PASS — median fill 69%; every <40% sheet audited = structural divider page (subject/index/front) |
| 8 | Two-column card layout | PASS — `.rows` computed columnCount = 2 |
| 9 | No serial numbers / taxonomy codes | PASS — 0 id-chips, 0 `SUBJECT NN` in visible text |
| 10 | Highlighting consistent across subjects | PASS — all 12 subjects, 46–558 spans each |
| 11 | Only exam data highlighted | PASS — every span carries a digit; 0 in headings/labels/tables |
| 12 | Nested sub-bullets proper levels | PASS — l0=1448, l1=393, l2=36; l1 indent 13px |
| 13 | No duplicate source listings | PASS — 1 panel = 1 zero-inline-citation card; all others inline-only |
| 14 | JSON updated (source of truth) | PASS — canonical grammar, 0 continuations, 0 artifacts, 0 raw tags |
| 15 | Persistence | PASS — 2407 markers = 2407 rendered; JSON-only regen byte-identical |
| 16 | HTML preview and PDF match | PASS — 110 = 110 pages, exact A4 both |
| 17 | Full-book visual review | PASS — 40+ screenshots; VLM sweeps 5/5, 8/8, 4/4, 6/6 PASS |

## Root cause per original bug

| Bug (as reported) | Root cause found | Fix (phase) |
|---|---|---|
| Half-filled disclaimer page, footer floating high | `.sheet` was `display:block` — no structural footer reservation; content height ruled the foot position | Flex-column sheets + `.foot{margin-top:auto}` (P1) |
| Footer floating mid-page on other pages | same as above + print `column-fill:auto` stacking rows into column 1 (doubled heights → 184 PDF pages) | Flex pinning + removed harmful print multicol rule (P1) |
| Index splitting awkwardly | Book+index order followed JSON first-appearance (GS-III first); paper headers appended before fit-check; fixed-height packing | Tree sorted GS1→GS2→GS3 at parse; atomic subject blocks; page numbers from final pagination via fixpoint (P3) |
| Manufacturing Sector card heading/body split | Packer had no keep-with-next; `begin_flow_card` used a 220px magic guard that failed before tall tables | `Packer.add(keep_next)` chains for sec-h/sub-h/card-head/sth/ssec/minor; head+first-unit requirement (P2) |
| Excess whitespace | blanket `.card{break-inside:avoid}` in print CSS | Selective avoid on micro-blocks only; cards flow via CONTINUED fragments (P2) |
| Serial numbers + taxonomy codes visible | card-id chips + `SUBJECT NN` hero tags in the renderer | Dropped from visible chrome; anchors keep ids (P4) |
| Dense paragraphs instead of bullet hierarchy | source JSON: soft-wrapped lines, multi-fact `;` bullets, label-bullets with broken-indent children, `###` generator artifacts, raw `<b>` tags (escaped to literal text by `inline()`) | JSON canonicalised (grammar + 233 logged ops, text-preservation guarantee); parser rule 3b + `.sth2` tier (P5) |
| Exam data not scannable | no highlighting convention | `{{hl}}` marker in JSON → `<b class="hl">` bold+orange #C2410C; 2407 spans, caps + flags (P6–7) |
| Duplicate source listings | `.srcs` panels repeated the 556 inline citations | Panel only for zero-inline-citation cards (1 card) (P8) |

## Files modified (by phase)

- **P1** `src/datafacts/theme.css` (flex sheets, print full-bleed A4, multicol fix), `scripts/stage2/datafacts/build_book.py` (back-cover margin), `verify_phase1.py`
- **P2** `build_book.py` (Packer keep-with-next, CARD_MARGIN_PX, selective print avoids), `theme.css`, `verify_phase2.py`
- **P3** `parse_data.py` (tree sort), `build_book.py` (index rebuild, fixpoint page numbers, `_ix_line_est`), `theme.css` (.pg), `verify_phase3.py`
- **P4** `build_book.py` (no id-chips/serials), `theme.css` (dead rules removed), `verify_phase4` folded into gate runs
- **P5** `restructure_json.py` (new), `inputs/updated_data.json` (canonicalised; backup `.pre-phase5.json`), `parse_data.py` (rule 3b, grammar docs), `build_book.py` (.sth2 + minor units), `theme.css` (.sth2 + print rules), `qa_check_df.py` (### and escaped-tag residue), `analyze_density.py`, `shot_phase5_before.py`, `verify_phase5.py`, `restructure_log.json`
- **P6+7** `highlight_json.py` (new), `inputs/updated_data.json` (2407 `{{hl}}` markers; backup `.pre-phase6.json`), `parse_data.py` (marker render + marker-blind verbatim), `theme.css` (--hl, .row b.hl), `qa_check_df.py` (marker residue), `verify_phase6.py`, `verify_phase7.py`, `highlight_log.json`
- **P8** `build_book.py` (panel rule + copy), `qa_check_df.py` (link expectation + panel check), `verify_phase8.py`
- **P9** `verify_phase9.py`, this report, `final_data_facts.pdf` regenerated
- **Docs** `DESIGN.md` §14–16 (grammar, marker convention, pipeline, 110-sheet map), `HANDOFF.md`, `PLAN.md`, worklogs

## Assumptions made (stated, not silently guessed)

1. `###` `Section Group:` fragments were generator artifacts, not content (removed, all 10 logged).
2. Leading list numbers (`5.` `14.`) on orphaned rows are list markers, not data (dropped, all 10 logged; every drop position-anchored in the preservation check).
3. Entirely-bold short bullets are group LABELS; 4 look-alikes force-kept as facts (`Target: 2500`, `Operational: 314`, `No state has > 20% women MLAs`, `No Institute in TOP 100`).
4. Table cells are intentionally NOT highlighted (tables are already all-data; whole-cell orange would break the ≤50% discipline).
5. Author-bolded date phrases (e.g. "September 2026") inherit highlighting via the author-bold rule (P1) — dates of a statistic are quotable context.
6. Subject divider pages are intentionally sparse (design pages, like chapter openers); under-fill there is not a packing defect.
7. `.sth2` in-column labels cannot control CSS multi-COLUMN breaks (browser-balanced); sheet-level keep-with-next is enforced, column-level fragmentation left to the balancer — no visual defect observed in any sweep.

## Flagged for human review

- **73 counted-noun data points left unhighlighted** (e.g. "1,522 mandis", "37 supercomputers", "25 operable reactors") — quotable but pattern-unsafe to auto-highlight; full list in `scripts/stage2/datafacts/highlight_log.json` (`flags` per card). Promote any of them by wrapping the phrase in `{{hl}}…{{/hl}}` in the JSON and rebuilding.
- **1 card at 48% orange** (`Climate Risk Index 2025`) — tiny 5-fact card, naturally data-dense; within the 50% cap but above the 40% review band.
- **2 cards carry no highlights** (no unit-regex or author-bold data found).
- **`Finalise/Force-fact overrides`** — see assumption 3; re-classify freely, the transformer is rerunnable.
