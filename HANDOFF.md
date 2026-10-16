# HANDOFF.md — Live Handoff (any agent: read this FIRST, then PLAN.md)

**Last updated:** 2026-10-16 (v3 + documentation pass: **DESIGN.md** added) · **Phases 0–8 COMPLETE + v2 + v3 REVIEW FIXES + DOCS — final_ebook.html QA-PASSED — AWAITING USER ACCEPTANCE** · Branch: `ebook-build` (this branch IS the project) · Repo: `upsc-serv-1/yfhgkjgiuy`

**Reading order:** this file → `PLAN.md` (process + iron rules) → **`DESIGN.md` (design spec of the shipped book)** → `design_tokens.md` (token reference) → tail of `worklog.md`.

## Current state in one paragraph

The eBook is **built, QA-verified, and reworked twice per user review**. Book name: **"Replica (Exam Replicable) · Intro to Conclusion"** (a Dr. CSE publication). `final_ebook.html` (1.10 MB, **217 sheets**, all 551 v17 cards verbatim — 0 text/digit mismatches, 0 broken links, 0 hotlinks, every sheet fits A4). v3 changes: **renamed + rebranded** (Dr. CSE logo top-left of every page via a thin "Dr. CSE — Replica" running header; page number moved to the footer; the old book-name/section/subject header crumbs are GONE — cards start directly); **page 2 = Disclaimer + How to Approach** (with drcse.in · t.me/dr_cse · dr.cse.001@gmail.com, replacing foreword + how-to-use); **master index is 2-column** and EVERY level is clickable (paper → subject → section → **subtopic** → card title — e.g. "Buddhism" jumps to its band; auto-paginated into true-A4 sheets); **each subject page opens with its own clickable card index** (Ethics spans 2 A4 pages, compact 3-col); **no card-count statistics anywhere** (cover stats, "N CARDS" chips, "SECTION N OF 48" stamps all removed); **INTRODUCTION is now a boxed block** like the others; the **syllabus-point micro line is removed** from cards; **long DATA walls flow in 2 columns** (`.data-cols`, 25 cards incl. GS1-HIST-0012). Structure (217 sheets): cover → disclaimer+approach → 7 index sheets → 4 parts × 14 chapters → back cover. Rebuild: `python scripts/stage2/convert_cards.py && python scripts/stage2/build_front.py && python scripts/stage2/build_back.py && python scripts/stage2/build.py` then `python scripts/stage2/qa_check.py`. **GitHub `main` holds an OLD, superseded project — ignore it completely.**

## User decisions already locked (do not re-ask)

1. Final deliverable = **editable HTML** (`final_ebook.html`), magazine-style like the prototype — NOT a PDF. A4 `@media print` CSS included for print/export.
2. **Title (v3): “Replica (Exam Replicable) · Intro to Conclusion”** — Dr. CSE publication. Running header “Dr. CSE — Replica” + logo; footer “DR. CSE — REPLICA · INTRO TO CONCLUSION” + page number.
3. Audience: **UPSC GS Mains** answer-writing (Papers I–IV).
4. Repo layout: **both** modular `src/` partials AND assembled `final_ebook.html`, committed every phase.
5. Front matter (v3): **cover + page-2 Disclaimer & How to Approach** only (foreword/how-to-use superseded). Back cover keeps the resource-guide image + contact.
6. Design truth: **prototype HTML wins**; `inputs/DESIGN_MAGZ_SPEC.md` fills gaps.
7. Content truth: `inputs/merged_publish_ready_v17.md` — 551 cards, FINAL. Cards absent from v17 were intentionally excluded; never restore them.
8. All project work happens on branch **`ebook-build`**.
9. **Illustrations:** count-analytics visuals are removed entirely (superseded by #13).
10. **Index structure:** GS-wise (GS-1 → GS-4) at top level, subject-wise inside each GS, then section_group → subtopic.
11. **Card taxonomy (user):** the paper/subject/section_group/microtopic/subtopic fields on each card were assigned by the user for proper indexing — build all navigation from them.
12. **Phase-1 gate confirmations:** (a) images via **relative paths** `assets/images/…` (+ optional `--embed` base64 flag); (b) part=GS paper → chapter=subject → section=section_group → card-group=subtopic; GS-4 strong internal navigation; detail cards render `:::detail label` headers; multi-quote cards render all quotes; 5 universal_template cards marked as practice skeletons.
13. **NO count-analytics (v2):** pies/bands/heatmaps/tier tables REMOVED; part openers are pure navigation.
14. **Index = clickable front matter (v2)** — and **v3: 2-column layout, subtopic names also clickable, no count badges**.
15. **Card-in-a-box (v2):** one card = one rounded-edge white box, paper-colour top edge, coloured block labels.
16. **No numbers that scare students (v3):** no card-count stats on cover, openers, index, or subject pages. (Card IDs like GS1-HIST-0001 are handles, not stats — they stay.)
17. **Subject pages (v3):** each subject name-page carries a clickable index of that subject's card titles, on a true-A4 sheet (Ethics = 2 sheets). No "N sections / N subtopics" bragging rows.
18. **Thin running header (v3):** logo + "Dr. CSE — Replica" only; no book-name/section/subject crumbs; page number in footer.
19. **Cards (v3):** INTRODUCTION boxed like other blocks; syllabus-point micro line removed; long DATA lists in 2 columns.
20. **Contact (v3):** drcse.in · t.me/dr_cse · dr.cse.001@gmail.com — shown on cover, disclaimer page, back cover. Logo asset: `assets/images/logo_dr_cse.png` (extracted from the prototype's embedded base64).

## What to do next (if you are picking this up)

1. Confirm you are on `ebook-build` (`git branch --show-current`). Clone with `git clone -b ebook-build <repo-url>` if starting fresh.
2. Read `PLAN.md` fully (phase table, iron rules, file map, open questions), then `DESIGN.md` (the design spec — components, prohibitions, change protocol).
3. Read the tail of `worklog.md` for the latest completed Task ID.
4. **All phases 0–8 + v2 + v3 review fixes + documentation pass are complete and QA-green.** Awaiting user acceptance of the v3 build.
5. Rebuild after ANY src/ change — full chain:
   `python scripts/stage2/convert_cards.py && python scripts/stage2/build_front.py && python scripts/stage2/build_back.py && python scripts/stage2/build.py && python scripts/stage2/qa_check.py` (all must stay green).
6. If index/opener pagination is tuned: re-measure sheet heights with a headless browser (see session scripts `measure_sheets.js` / `measure_ix.js` pattern) — every `.a4`/`.p1` sheet must stay ≤ ~1135px.
7. After every change: update the status table in `PLAN.md`, update this file AND `DESIGN.md` (§ that changed), append to `worklog.md`, then commit and push (`phase-N: summary`).

## DO NOT

- Do NOT use, merge, or "recover" anything from GitHub `main` — it is an old, superseded project.
- Do NOT edit card bodies or alter quotes, numbers, names, or data-list items (protected content — see PLAN.md §3).
- Do NOT add new content sections the user didn't approve.
- Do NOT reintroduce count-analytics visuals or card-count badges (#13, #16).
- Do NOT restore the ~238 cards that v17 does not contain.
- Do NOT write the GitHub PAT (or any secret) into files, scripts, logs, or commits. Command line only.
- Do NOT push without a phase-gate self-audit.

## Verification tools

- Stage-2 scripts live in `scripts/stage2/` (audit_cards.py, download_images.py, convert_cards.py, build_front.py, build_back.py, build.py, qa_check.py). Write new ones there — no throwaway inline code.
- QA gate checklist: PLAN.md §6 · Design prohibitions: DESIGN.md §11 · Change protocol: DESIGN.md §12.
