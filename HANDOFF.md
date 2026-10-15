# HANDOFF.md — Live Handoff (any agent: read this FIRST, then PLAN.md)

**Last updated:** 2026-10-16 · **Phases 0–8 COMPLETE — final_ebook.html built and QA-PASSED — AWAITING USER GATE (Phase 9)** · Branch: `ebook-build` (this branch IS the project) · Repo: `upsc-serv-1/yfhgkjgiuy`

## Current state in one paragraph

The eBook is **built and QA-verified**: `final_ebook.html` (1.23 MB, 239 sheets, all 551 v17 cards verbatim — 0 text mismatches, 0 digit mismatches, 0 broken links, 0 hotlinks, print-safe A4 CSS) plus its modular sources (21 `src/` partials + `theme.css`, all regenerable via `scripts/stage2/` pipeline). Structure: cover → foreword → how-to-use (30/60/90 routes) → book-at-a-glance analytics (recreated SVGs from our own data) → 4 parts × 14 chapters (auto-paginated sheets, running topbars) → GS-wise master index (all 551 cards) → back cover. **The orchestrator has reported the Phase-8 gate and is WAITING for user decisions** on the 4 non-blocking doubts in `qa_report.md` (typographic cover, back-cover resource-guide PNG, long opener/index sheets in print, no per-card callouts). Rebuild anytime: `python scripts/stage2/build.py` (or `--embed` for a portable single file). **GitHub `main` holds an OLD, superseded project — ignore it completely.**

## User decisions already locked (do not re-ask)

1. Final deliverable = **editable HTML** (`final_ebook.html`), magazine-style like the prototype — NOT a PDF. A4 `@media print` CSS included for print/export.
2. Title: **"PYQ Nano Analysis — GS Mains"** · subtitle "The Answer-Writing Playbook" (working title).
3. Audience: **UPSC GS Mains** answer-writing (Papers I–IV).
4. Repo layout: **both** modular `src/` partials AND assembled `final_ebook.html`, committed every phase.
5. Extra sections: **Foreword + "How to Use This Book"** (30/60/90-day plans) only. No quick-rev sheets / template appendix / PYQ-trend tables (user declined).
6. Design truth: **prototype HTML wins**; `inputs/DESIGN_MAGZ_SPEC.md` fills gaps.
7. Content truth: `inputs/merged_publish_ready_v17.md` — 551 cards, FINAL. Cards absent from v17 were intentionally excluded; never restore them.
8. All project work happens on branch **`ebook-build`**.
9. **Illustrations (user, 2026-10-16):** include inline SVG illustrations of the TYPES the prototype uses (marks-share donuts, tier/heatmap tables, chapter visuals) — recreated for this book's own content, never copied 1:1.
10. **Index structure (user, 2026-10-16):** GS-wise (GS-1 → GS-4) at top level, subject-wise inside each GS, then section_group → subtopic.
11. **Card taxonomy (user):** the paper/subject/section_group/microtopic/subtopic fields on each card were assigned by the user for proper indexing — build all navigation from them.
12. **Phase-1 gate confirmations (user, 2026-10-16):** (a) images referenced via **relative paths** `assets/images/…` — primary mode, with an optional `--embed` base64 build flag; (b) "go with your recommendations" — all six recommendations in `content_inventory.md` §7 approved: Part=GS paper → Chapter=subject → Section=section_group → card-group=subtopic; GS-4 strong internal navigation + mini-index; prototype-type SVG illustrations recreated for our content; detail cards render `:::detail label` headers and multi-quote cards render all quotes in sequence; the 5 universal_template cards are visually marked as practice skeletons.

## What to do next (if you are picking this up)

1. Confirm you are on `ebook-build` (`git branch --show-current`). Clone with `git clone -b ebook-build <repo-url>` if starting fresh.
2. Read `PLAN.md` fully (phase table, iron rules, file map, open questions).
3. Read the tail of `worklog.md` for the latest completed Task ID.
4. **All phases 0–8 are complete.** The Phase-8 user gate is pending: 4 non-blocking doubts listed in `qa_report.md` §"Doubts carried to the user gate". Apply user decisions (if any), then run `python scripts/stage2/qa_check.py` + commit.
5. Rebuild after ANY src/ change: `python scripts/stage2/build.py` then `python scripts/stage2/qa_check.py` (both must stay green).
6. After every change: update the status table in `PLAN.md`, update this file, append to `worklog.md`, then commit and push (`phase-N: summary`).

## DO NOT

- Do NOT use, merge, or "recover" anything from GitHub `main` — it is an old, superseded project.
- Do NOT edit card bodies or alter quotes, numbers, names, or data-list items (protected content — see PLAN.md §3).
- Do NOT add new content sections the user didn't approve (no quick-rev sheets, no template appendix).
- Do NOT restore the ~238 cards that v17 does not contain.
- Do NOT write the GitHub PAT (or any secret) into files, scripts, logs, or commits. Command line only.
- Do NOT push without a phase-gate self-audit.

## Verification tools

- Stage-2 scripts live in `scripts/stage2/` (audit_cards.py, download_images.py, …; build/check scripts come in later phases). Write new ones there — no throwaway inline code.
- QA gate checklist: PLAN.md §6.
