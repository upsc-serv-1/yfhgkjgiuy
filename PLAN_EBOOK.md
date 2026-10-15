# PLAN_EBOOK.md — Stage 2: Build the HTML eBook

**Book:** *PYQ Nano Analysis — GS Mains · The Answer-Writing Playbook* (working title)
**Stage:** 2 of 2 — Stage 1 (content polishing) is COMPLETE; see `PLAN.md` (kept unchanged, for reference).
**This file is the governing plan for Stage 2.** Live status pointer: `HANDOFF.md`. History: `worklog.md`.

---

## START HERE — Stage 2 status

| Phase | What | Output | Status |
|---|---|---|---|
| 0 | Setup: repo structure, inputs copied, this plan, HANDOFF.md | this file | ✅ DONE |
| 1 | Content audit — parse v17 cards, categorize, reconcile vs JSON, download all images | `content_inventory.md` | 🔄 IN PROGRESS |
| 2 | Book architecture — reverse-engineer prototype, full TOC, card→chapter map | `ebook_structure.md` | ⬜ |
| 3 | Design tokens — extract fonts/colors/spacing from prototype + spec; build `src/theme.css` + card/callout templates | `design_tokens.md` | ⬜ |
| 4 | Editorial layer — foreword, How-to-Use, chapter intros; card bodies VERBATIM into `src/` chapter partials | `src/*.html` | ⬜ |
| 5 | Student-review pass — aspirant read-through, doubt flags, callout suggestions, fixes | `review_notes.md` | ⬜ |
| 6 | TOC + alphabetical index generation | `toc_index.md` | ⬜ |
| 7 | Assembly — build script merges `src/` + theme + images → `final_ebook.html` | `final_ebook.html` | ⬜ |
| 8 | QA audit — vs prototype + spec + this checklist; fix loop until pass | `qa_report.md` | ⬜ |
| 9 | Final handoff — push, wrap up | repo state | ⬜ |

**Gate rule:** after Phase 1 and after Phase 8, the orchestrator reports to the user and WAITS for confirmation. All other phases: orchestrator audits the subagent output, fixes or returns it, then proceeds and pushes.

---

## 1. Product definition

- **Deliverable:** ONE polished, editable, self-consistent HTML eBook (magazine style, like the reference prototype), committed alongside its modular sources.
- **Title / subtitle:** "PYQ Nano Analysis — GS Mains" / "The Answer-Writing Playbook" (working title — one string to change if user renames).
- **Audience:** UPSC GS Mains aspirants (Papers I–IV), answer-writing focus. UPSC mentor tone: concise, exam-focused, guiding.
- **Print path:** `@media print` CSS (A4, clean chapter page-breaks) so anyone can File→Print→Save-as-PDF. The HTML itself is the primary deliverable (user decision 2026-10-16).
- **Repo layout (user decision):** BOTH modular `src/` partials (one per chapter, for parallel agent edits and clean diffs) AND the assembled `final_ebook.html`, rebuilt and committed after every phase.

## 2. Inputs (in `inputs/`)

| File | Role |
|---|---|
| `merged_publish_ready_v17.md` | **Content source of truth** (551 cards, `## id:` header format). User-uploaded, newest version. |
| `prototype_pyq_nano_gs_mains.html` | **Design source of truth** (5.5 MB, "prototype 25"). Style benchmark for fonts, colors, layout, index format, pedagogy, tone. |
| `DESIGN_MAGZ_SPEC.md` | Secondary design spec (Dr. CSE magazine article-pages system). Fills gaps where the prototype is silent. |
| `upsc_readymade_resource_guide.png` | User-uploaded image; role TBD (cover art candidate). Phase 2 proposes, user confirms. |
| (repo root) `mains_intro_conclusions.json` | Original 789-card source JSON — reconciliation reference only. |
| (repo) `polished/MERGED_full_1-789.md`, `c11_verify/MERGED_publish_ready_1-789.md` | Stage-1 outputs — reconciliation references. |

## 3. Iron rules (NON-NEGOTIABLE — inherited from Stage 1 + user brief)

1. **Never lose content.** Every one of the 551 v17 cards must appear in the final eBook. Rewriting for layout is fine; deleting meaning is not.
2. **Card bodies are VERBATIM.** They are the product of 11 correction/verification passes (C0–C11, `verify_protected.py` 0 errors). Stage 2 does NOT re-polish them. Protected content (quotes + attributions, all numbers/years/percentages, names, schemes, laws, data-list items) must arrive in the HTML unchanged. The editorial layer only ADDS (foreword, how-to-use, chapter intros, transitions, callouts) around the cards.
3. **Stage-1 easy-language rule applies to all NEW text:** everyday words, 12–20 word sentences (never >25), no flowery/AI words (spotlight, tapestry, bedrock, pivotal, holistic…), no idioms. Test: "Can an average aspirant reproduce this in the exam hall?"
4. **No external image hotlinks in the final HTML.** All images downloaded to `assets/images/` with normalized names (`<subject>_<topic-slug>_<NN>.png`), referenced locally, with captions/alt text.
5. **Design truth order:** prototype wins; DESIGN_MAGZ_SPEC.md fills gaps; conflicts are logged in HANDOFF.md (only escalated to the user if material).
6. **Push after every phase** with message `stage2/phase-N: <summary>`. Keep PLAN_EBOOK.md status table + HANDOFF.md updated in the same commit.
7. **Security:** the GitHub PAT lives only on the git command line — never in any file, log, or worklog. (User should revoke/rotate after the project.)
8. **Stage-1 files are frozen:** do not edit `polished/`, `c11_verify/`, `scripts/c0–c11*`, `tools/`, `PLAN.md`, `corrections_log.md`, `review_queue.md`. Stage-2 scripts go in `scripts/stage2/`.

## 4. Stage-2 file map

```
inputs/                  ← frozen source inputs (copied from user uploads)
assets/images/           ← downloaded + renamed card images (manifest in content_inventory.md)
src/                     ← modular HTML sources
  00_cover.html, 01_foreword.html, 02_how_to_use.html, 10_gs1_history.html … (one per chapter),
  90_index.html …        ← naming finalized in Phase 2
  theme.css              ← design tokens (Phase 3)
scripts/stage2/          ← build + QA scripts (audit.py, build.py, check.py …)
content_inventory.md     ← Phase 1 deliverable
ebook_structure.md       ← Phase 2 deliverable
design_tokens.md         ← Phase 3 deliverable
review_notes.md          ← Phase 5 deliverable
toc_index.md             ← Phase 6 deliverable
qa_report.md             ← Phase 8 deliverable
final_ebook.html         ← Phase 7+ assembled artifact (rebuilt each phase)
```

## 5. Card schema reference (v17 format)

```
## id: GS1-HIST-0001
paper: "GS-1"            subject: "HISTORY"
section_group: "Art and Culture"
microtopic: "…"          subtopic: "Bhakti and Sufi movement"
card_title: "…"          card_type: structured | detail
sections: [quote, introduction, examples, data, conclusion, image]
flags: [has_image, truncated, same_as_above, …]     status: polished | needs_review
:::quote / :::introduction / :::examples / :::data / :::conclusion / :::detail label="…" / :::image <url>
```
Known distribution (original 789): GS-4 Ethics 246, GS-3 215, GS-2 172, GS-1 156. v17 = 551 cards — the audit must document exactly which 238 are absent and why (C11 manual-review list, Tier D/E quote issues, or a later user cut).

## 6. QA gates (Phase 8 checklist)

- [ ] All 551 v17 cards present in final HTML (automated count + per-card anchor check)
- [ ] Protected-content spot check: quotes/numbers/data survive verbatim (script vs JSON for a sample + all flags)
- [ ] All images local, no hotlinks, no broken refs, alt text present
- [ ] Consistent heading hierarchy; TOC + index links resolve to anchors
- [ ] Tone + terminology consistent (mentor tone, easy language, abbreviation policy per PLAN.md §3)
- [ ] Visual parity with prototype: fonts (Fraunces / IBM Plex Sans / IBM Plex Mono), palette, card/callout components
- [ ] A4 print CSS works (chapter page-breaks, no orphan headings)
- [ ] Spelling/grammar pass on NEW text only
- [ ] HTML validates (no overflow-hidden traps, no backdrop-filter, font fallbacks present)

## 7. Open questions (resolve at gates)

1. **789 → 551 card delta:** intentional user cut or accidental? Phase 1 reports the exact missing list; user decides at the Phase 1 gate whether any come back.
2. **Image embedding mode:** relative `assets/images/` paths (editable, folder-based) vs base64-embedded (true single file, heavy). Default: relative paths + repo/zip as the deliverable unit; a `--embed` build flag can produce a portable single file. Confirm at Phase 1 gate.
3. **Role of `upsc_readymade_resource_guide.png`** (cover art? appendix? exclude?).
4. **Prototype's PYQ analytics** (marks-share donuts, subject heatmaps): include as book front-matter "GS Mains paper anatomy" section, or treat prototype as style-only? Phase 2 proposes.

## 8. Worklog protocol (all agents)

Append to `worklog.md` (repo, canonical) AND `/home/z/my-project/worklog.md` (session-local):

```
---
Task ID: <stage2 phase or sub-task, e.g. 1, 2-a, 2-b>
Agent: <name>
Task: <what was asked>

Work Log:
- <steps>

Stage Summary:
- <results / decisions / artifacts>
```

Read the tail of `worklog.md` before starting any task. Never overwrite — append only.
