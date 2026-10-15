# HANDOFF.md — Live Handoff (any agent: read this FIRST, then PLAN.md)

**Last updated:** 2026-10-16 · **Phase 1 (Content audit) COMPLETE — awaiting user gate to start Phase 2** · Branch: `ebook-build` (this branch IS the project) · Repo: `upsc-serv-1/yfhgkjgiuy`

## Current state in one paragraph

The project converts `inputs/merged_publish_ready_v17.md` (551 polished UPSC GS Mains cards — the user-confirmed FINAL content) into a magazine-style, editable HTML eBook (`final_ebook.html`) designed after `inputs/prototype_pyq_nano_gs_mains.html`. **Phase 1 is complete** (executed directly by the orchestrator after two subagent-launch failures): `content_inventory.md` documents all 551 cards (clean — no structural defects), taxonomy depth (48 section groups → 209 subtopics), and all 37 images downloaded + normalized into `assets/images/` (0 broken, 1 AVIF→PNG). **The orchestrator has reported the Phase-1 findings to the user and is WAITING for confirmation to start Phase 2 (book architecture).** Nothing has touched any card body yet. **GitHub `main` holds an OLD, superseded project — ignore it completely.**

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

## What to do next (if you are picking this up)

1. Confirm you are on `ebook-build` (`git branch --show-current`). Clone with `git clone -b ebook-build <repo-url>` if starting fresh.
2. Read `PLAN.md` fully (phase table, iron rules, file map, open questions).
3. Read the tail of `worklog.md` for the latest completed Task ID.
4. `content_inventory.md` EXISTS and is complete — Phase 1 is done. Once the user confirms the gate, start Phase 2 (`ebook_structure.md`) per PLAN.md.
5. Follow the gate rule: after Phase 1 and Phase 8, STOP and report to the user; other phases proceed after self-audit.
6. After every phase: update the status table in `PLAN.md`, update this file, append to `worklog.md`, then commit and push (`phase-N: summary`).

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
