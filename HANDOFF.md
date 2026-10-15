# HANDOFF.md — Live Handoff (any agent: read this FIRST, then PLAN.md)

**Last updated:** 2026-10-16 (post-review v2) · **Phases 0–8 COMPLETE + v2 REVIEW FIXES APPLIED — final_ebook.html rebuilt and QA-PASSED — AWAITING USER ACCEPTANCE** · Branch: `ebook-build` (this branch IS the project) · Repo: `upsc-serv-1/yfhgkjgiuy`

## Current state in one paragraph

The eBook is **built, QA-verified, and reworked per the user's design review**: `final_ebook.html` (1.18 MB, 238 sheets, all 551 v17 cards verbatim — 0 text/digit mismatches, 0 broken links, 0 hotlinks). v2 changes: **all count-analytics removed** (pies/bands/heatmaps gone; "Book at a Glance" page deleted); the **subject-wise clickable index moved to front matter** (right after How-to-Use — all 551 card titles are links, verified by browser click-through); a **floating INDEX button** on every screen; every sheet breadcrumb ends in an INDEX link; and **cards are now white rounded boxes** (12px radius, paper-colour top edge, dashed title rule, coloured QUOTE/INTRODUCTION/EXAMPLES/DATA/CONCLUSION labels with tinted panels). Structure: cover → foreword → how-to-use → 5 index sheets → 4 parts × 14 chapters → back cover. Rebuild anytime: `python scripts/stage2/build.py` (or `--embed` for a portable single file). **GitHub `main` holds an OLD, superseded project — ignore it completely.**

## User decisions already locked (do not re-ask)

1. Final deliverable = **editable HTML** (`final_ebook.html`), magazine-style like the prototype — NOT a PDF. A4 `@media print` CSS included for print/export.
2. Title: **"PYQ Nano Analysis — GS Mains"** · subtitle "The Answer-Writing Playbook" (working title).
3. Audience: **UPSC GS Mains** answer-writing (Papers I–IV).
4. Repo layout: **both** modular `src/` partials AND assembled `final_ebook.html`, committed every phase.
5. Extra sections: **Foreword + "How to Use This Book"** (30/60/90-day plans) only. No quick-rev sheets / template appendix / PYQ-trend tables (user declined).
6. Design truth: **prototype HTML wins**; `inputs/DESIGN_MAGZ_SPEC.md` fills gaps.
7. Content truth: `inputs/merged_publish_ready_v17.md` — 551 cards, FINAL. Cards absent from v17 were intentionally excluded; never restore them.
8. All project work happens on branch **`ebook-build`**.
9. **Illustrations (user, 2026-10-16):** ~~include inline SVG illustrations of the TYPES the prototype uses~~ — **SUPERSEDED by decision #13**: count-analytics visuals are removed entirely.
10. **Index structure (user, 2026-10-16):** GS-wise (GS-1 → GS-4) at top level, subject-wise inside each GS, then section_group → subtopic.
11. **Card taxonomy (user):** the paper/subject/section_group/microtopic/subtopic fields on each card were assigned by the user for proper indexing — build all navigation from them.
12. **Phase-1 gate confirmations (user, 2026-10-16):** (a) images referenced via **relative paths** `assets/images/…` — primary mode, with an optional `--embed` base64 build flag; (b) "go with your recommendations" — all six recommendations in `content_inventory.md` §7 approved: Part=GS paper → Chapter=subject → Section=section_group → card-group=subtopic; GS-4 strong internal navigation + mini-index; detail cards render `:::detail label` headers and multi-quote cards render all quotes in sequence; the 5 universal_template cards are visually marked as practice skeletons.
13. **NO count-analytics (user review, 2026-10-16):** the book's aim is ready-made cards. Students do not care how many cards come from which subject — pies/bands/heatmaps/tier tables are REMOVED and must not return. Part openers are pure navigation pages.
14. **Index = clickable front matter (user review, 2026-10-16):** subject-wise index with card titles, placed where students find it (after How-to-Use); every title clickable straight to its card; persistent INDEX affordances (floating button + breadcrumb link).
15. **Card-in-a-box (user review, 2026-10-16):** one card = one rounded-edge box in a separate colour (white on sage), per the user's reference screenshot blended with the sage-gold design system — NOT a copy of the screenshot.

## What to do next (if you are picking this up)

1. Confirm you are on `ebook-build` (`git branch --show-current`). Clone with `git clone -b ebook-build <repo-url>` if starting fresh.
2. Read `PLAN.md` fully (phase table, iron rules, file map, open questions).
3. Read the tail of `worklog.md` for the latest completed Task ID.
4. **All phases 0–8 + the v2 review fixes are complete and QA-green.** Awaiting user acceptance of the v2 build. The 4 non-blocking doubts in `qa_report.md` may still be raised by the user (typographic cover, back-cover PNG, long sheets in print, no per-card callouts).
5. Rebuild after ANY src/ change: `python scripts/stage2/build.py` then `python scripts/stage2/qa_check.py` (both must stay green). Regenerating chapter partials also requires `python scripts/stage2/convert_cards.py` first.
6. After every change: update the status table in `PLAN.md`, update this file, append to `worklog.md`, then commit and push (`phase-N: summary`).

## DO NOT

- Do NOT use, merge, or "recover" anything from GitHub `main` — it is an old, superseded project.
- Do NOT edit card bodies or alter quotes, numbers, names, or data-list items (protected content — see PLAN.md §3).
- Do NOT add new content sections the user didn't approve (no quick-rev sheets, no template appendix).
- Do NOT reintroduce count-analytics visuals (pies/bands/heatmaps/tier tables) — removed by user decision #13.
- Do NOT restore the ~238 cards that v17 does not contain.
- Do NOT write the GitHub PAT (or any secret) into files, scripts, logs, or commits. Command line only.
- Do NOT push without a phase-gate self-audit.

## Verification tools

- Stage-2 scripts live in `scripts/stage2/` (audit_cards.py, download_images.py, …; build/check scripts come in later phases). Write new ones there — no throwaway inline code.
- QA gate checklist: PLAN.md §6.
