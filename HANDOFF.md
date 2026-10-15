# HANDOFF.md — Live Handoff (any agent: read this FIRST, then PLAN_EBOOK.md)

**Last updated:** 2026-10-16 · **Phase 1 (Content audit) IN PROGRESS** · Repo: `upsc-serv-1/yfhgkjgiuy` · Branch: `main`

## Current state in one paragraph

Stage 1 (content polishing of the 789-card UPSC Mains intro/conclusions book, passes C0–C11) is **complete and frozen** — see `PLAN.md`. Stage 2 (building the HTML eBook from the user's `inputs/merged_publish_ready_v17.md`, 551 cards, styled after `inputs/prototype_pyq_nano_gs_mains.html`) has just started. Phase 0 (setup) is done; Phase 1 (content audit + image download) is in progress. Nothing has touched any card body yet.

## User decisions already locked (do not re-ask)

1. Final deliverable = **editable HTML** (`final_ebook.html`), magazine-style like the prototype — NOT a PDF. A4 `@media print` CSS included for print/export.
2. Title: **"PYQ Nano Analysis — GS Mains"** · subtitle "The Answer-Writing Playbook" (working title).
3. Audience: **UPSC GS Mains** answer-writing (Papers I–IV).
4. Repo layout: **both** modular `src/` partials AND assembled `final_ebook.html`, committed every phase.
5. Extra sections: **Foreword + "How to Use This Book"** (30/60/90-day plans). No quick-rev sheets / template appendix / PYQ-trend tables (user declined).
6. Design truth: **prototype HTML wins**; `inputs/DESIGN_MAGZ_SPEC.md` fills gaps.
7. Content truth: `inputs/merged_publish_ready_v17.md` (551 cards).

## What to do next (if you are picking this up)

1. Read `PLAN_EBOOK.md` fully (phase table, iron rules, file map, open questions).
2. Read the tail of `worklog.md` for the latest completed Task ID.
3. Check `content_inventory.md` — if it exists and is complete, Phase 1 is done; continue with Phase 2 (ebook_structure.md). If not, finish Phase 1 per its section in PLAN_EBOOK.md.
4. Follow the gate rule: after Phase 1 and Phase 8, STOP and report to the user; other phases proceed after self-audit.
5. After every phase: update the status table in `PLAN_EBOOK.md`, update this file, append to `worklog.md` (both repo and `/home/z/my-project/worklog.md`), commit and push (`stage2/phase-N: summary`).

## DO NOT

- Do NOT edit card bodies, `polished/`, `c11_verify/`, Stage-1 scripts, `PLAN.md`, `corrections_log.md`, `review_queue.md`.
- Do NOT alter quotes, numbers, names, or data-list items (Stage-1 protected content).
- Do NOT add new content sections the user didn't approve (no quick-rev sheets, no template appendix).
- Do NOT re-merge Stage-1 batch files.
- Do NOT write the GitHub PAT (or any secret) into files, scripts, logs, or commits. Command line only.
- Do NOT push without a phase-gate self-audit.

## Verification tools you can reuse

- `python3 verify_protected.py` (Stage-1 checker; see GOTCHA in PLAN.md §11 about convert.py import).
- Stage-2 scripts live in `scripts/stage2/` (audit, build, QA). Write new ones there, never inline-throwaway.
