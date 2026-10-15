# PLAN.md — PYQ Nano Analysis — GS Mains · The Answer-Writing Playbook (HTML eBook build)

**Branch:** `ebook-build` — this branch IS the project. Live status: `HANDOFF.md`. History: `worklog.md`.

> **Branch policy (user, 2026-10-16):** everything on GitHub `main` is an OLD, superseded snapshot from a previous project.
> `inputs/merged_publish_ready_v17.md` on THIS branch is the **final, authoritative content**.
> Never source content from `main`; never merge `main` into this branch; never "restore" cards that v17 does not contain.

---

## START HERE — Stage status

| Phase | What | Output | Status |
|---|---|---|---|
| 0 | Setup: branch, inputs copied, this plan, HANDOFF.md | this file | ✅ DONE |
| 1 | Content audit — parse all v17 cards, categorize, internal-consistency check, download all images | `content_inventory.md` | ✅ DONE — gate CONFIRMED by user 2026-10-16 |
| 2 | Book architecture — reverse-engineer prototype, GS-parted TOC (GS → subject → section_group → subtopic), card→chapter map, illustration plan | `ebook_structure.md` | ✅ DONE — self-audited, pushed |
| 3 | Design tokens — extract fonts/colors/spacing from prototype + spec; catalog the prototype's SVG illustration TYPES for re-creation; build `src/theme.css` + card/callout templates | `design_tokens.md`, `src/theme.css` | ✅ DONE — pushed |
| 4 | Editorial layer — foreword, How-to-Use, chapter intros; card bodies VERBATIM into `src/` chapter partials | `src/*.html` | ✅ DONE — verbatim gate green, pushed |
| 5 | Student-review pass — aspirant read-through, doubt flags, callout suggestions, fixes | `review_notes.md` | ✅ DONE — sheet-pagination fix applied, pushed |
| 6 | TOC + index — GS-wise (GS-1→GS-4), subject-wise within each GS, built from the card taxonomy | `toc_index.md` | ✅ DONE — 551 index links verified, pushed |
| 7 | Assembly — build script merges `src/` + theme + images → `final_ebook.html` | `final_ebook.html` | ✅ DONE — 239 sheets, self-checks green, pushed |
| 8 | QA audit — vs prototype + spec + checklist; fix loop until pass | `qa_report.md` | ✅ DONE — ALL CHECKS GREEN — **USER GATE** |
| 9 | Final handoff — push, wrap up | repo state | ▶ awaiting user gate decisions |

**Gate rule:** after Phase 1 and after Phase 8, the orchestrator reports to the user and WAITS for confirmation. All other phases: orchestrator audits the subagent output, fixes or returns it, then proceeds and pushes.

---

## 1. Product definition

- **Deliverable:** ONE polished, editable, self-consistent HTML eBook (magazine style, like the reference prototype), committed alongside its modular sources.
- **Title / subtitle:** "PYQ Nano Analysis — GS Mains" / "The Answer-Writing Playbook" (working title — one string to change if the user renames).
- **Audience:** UPSC GS Mains aspirants (Papers I–IV), answer-writing focus. UPSC mentor tone: concise, exam-focused, guiding.
- **Print path:** `@media print` CSS (A4, clean chapter page-breaks) so anyone can File→Print→Save-as-PDF. The HTML itself is the primary deliverable (user decision 2026-10-16).
- **Illustrations (user, 2026-10-16):** the eBook must include inline SVG illustrations of the TYPES found in the prototype (marks-share donuts, tier/heatmap tables, chapter-opener visuals, data diagrams) — recreated for this book's own content and sections, never copied 1:1. All inline SVG (editable, print-safe).
- **Repo layout (user decision):** BOTH modular `src/` partials (one per chapter, for parallel agent edits and clean diffs) AND the assembled `final_ebook.html`, rebuilt and committed after every phase.

## 2. Inputs (in `inputs/`)

| File | Role |
|---|---|
| `merged_publish_ready_v17.md` | **Content source of truth.** 551 cards, `## id:` header format. User-confirmed final polished content. |
| `prototype_pyq_nano_gs_mains.html` | **Design source of truth** (5.5 MB, "prototype 25"). Style benchmark: fonts, colors, layout, index format, pedagogy, tone. |
| `DESIGN_MAGZ_SPEC.md` | Secondary design spec (magazine article-pages system). Fills gaps where the prototype is silent. |
| `upsc_readymade_resource_guide.png` | User-uploaded image; role TBD (cover art candidate). Phase 2 proposes, user confirms. |

## 3. Iron rules (NON-NEGOTIABLE)

1. **v17 is the sole content truth.** All 551 cards must appear in the final eBook. The ~238 cards absent from v17 (v17 was selected from a larger 789-card draft) were intentionally excluded by the user — never resurrect them, never ask about them again.
2. **Card bodies go in VERBATIM.** Protected content — quote text + attributions, every number/year/percentage, names of people/institutions/schemes/laws/article numbers/case judgments/place names/theory names, and every `data`/`detail` list item (order and nesting kept) — must reach the HTML unchanged. The editorial layer only ADDS around cards (foreword, how-to-use, chapter intros, transitions, callout boxes); it never rewrites card bodies.
3. **Easy-language rule for all NEW text** (inherited from the book's established style): everyday words, 12–20 word sentences (never above 25), one idea per sentence. No flowery/AI words (spotlight, tapestry, bedrock, pivotal, holistic, multifaceted…), no idioms. Test each line: "Can an average aspirant reproduce this in the exam hall?"
4. **Standard exam abbreviations stay as-is** (SC, HC, PM, VP, EC, CJI, IPC, UOI, FRs, DPSPs, UCC, RPA, GDP, NITI Aayog…). v17 already applies the correct policy.
5. **No external image hotlinks in the final HTML.** All images downloaded to `assets/images/` with normalized names (`<subject>_<topic-slug>_<NN>.png`), referenced locally, with alt text.
6. **Design truth order:** prototype wins; `DESIGN_MAGZ_SPEC.md` fills gaps; material conflicts are logged in HANDOFF.md.
7. **Push after every phase** to THIS branch (`ebook-build`) with message `phase-N: <summary>`, updating the status table in this file + HANDOFF.md in the same commit.
8. **Security:** the GitHub PAT lives only on the git command line — never in any file, log, or worklog. User should revoke/rotate after the project.
9. **Card taxonomy = the indexing skeleton (user, 2026-10-16):** every card carries paper → subject → section_group → microtopic → subtopic (user-assigned, for indexing). Book navigation and the index are built strictly from this hierarchy. Do not invent a different taxonomy.
10. **Index organization (user, 2026-10-16):** top level GS-wise (GS-1 → GS-2 → GS-3 → GS-4); within each GS, subject-wise; then section_group → subtopic → cards.

## 4. File map

```
inputs/                  ← frozen source inputs (4 files above)
assets/images/           ← downloaded + renamed card images (manifest in scripts/stage2/images_manifest.json)
src/                     ← modular HTML sources
  00_cover.html, 01_foreword.html, 02_how_to_use.html, 10_gs1_history.html … (one per chapter; naming finalized in Phase 2)
  theme.css              ← design tokens (Phase 3)
scripts/stage2/          ← build + QA scripts (audit_cards.py, download_images.py, build.py, check.py …)
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
A card can have several `:::quote` blocks. Only blocks the card originally had are present; `sections:` lists them in order. `card_type: detail` cards carry their content in `:::detail` blocks (e.g. `label="Concept"`).

## 6. QA gates (Phase 8 checklist)

- [ ] All 551 v17 cards present in final HTML (automated count + per-card anchor check)
- [ ] Protected-content check: every quote/number/data block from v17 survives verbatim (scripted comparison of final HTML against v17 itself)
- [ ] All images local, no hotlinks, no broken refs, alt text present
- [ ] Consistent heading hierarchy; TOC + index links resolve to anchors
- [ ] Tone + terminology consistent (mentor tone, easy language, abbreviation policy)
- [ ] Visual parity with prototype: fonts (Fraunces / IBM Plex Sans / IBM Plex Mono), palette, card/callout components
- [ ] A4 print CSS works (chapter page-breaks, no orphan headings)
- [ ] Spelling/grammar pass on NEW text only
- [ ] HTML sanity: font fallbacks present, no `backdrop-filter`, no overflow traps, images load locally

## 7. Open questions (resolve at gates)

1. ~~**Image embedding mode**~~ — **ANSWERED (user, Phase-1 gate, 2026-10-16):** relative `assets/images/` paths are the primary mode (editable folder deliverable). A `--embed` base64 build flag remains available for a portable single file, but relative is the committed default.
2. **Role of `upsc_readymade_resource_guide.png`** (cover art? appendix? exclude?). Phase 2 proposes.
3. ~~Prototype's PYQ analytics~~ — **ANSWERED (user, 2026-10-16):** include SVG illustrations of the prototype's TYPES, recreated for our book's own content. Phase 2 decides placement (front-matter analytics + per-GS visuals).
4. ~~Phase-2 architecture recommendations~~ — **ANSWERED (user, Phase-1 gate, 2026-10-16): "go with your recommendations"** — all six recommendations in `content_inventory.md` §7 are approved: (a) Part=GS paper → Chapter=subject (14) → Section=section_group → card-group=subtopic; (b) GS-4 gets strong internal navigation + its own mini-index; (c) prototype-type SVG illustrations recreated for our content; (d) images via relative paths; (e) detail cards render `:::detail label` headers, multi-quote cards render all quotes in sequence; (f) the 5 universal_template cards are visually marked as practice skeletons.

## 8. Worklog protocol (all agents)

Append to `worklog.md` (this branch, canonical) AND `/home/z/my-project/worklog.md` (session-local, when working in the Super Z sandbox):

```
---
Task ID: <phase or sub-task, e.g. 1, 2-a, 2-b>
Agent: <name>
Task: <what was asked>

Work Log:
- <steps>

Stage Summary:
- <results / decisions / artifacts>
```

Read the tail of `worklog.md` before starting any task. Never overwrite — append only.
