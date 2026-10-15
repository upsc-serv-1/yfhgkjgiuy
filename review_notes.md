# review_notes.md — Phase 5 · Student-Review Pass

**Reviewed:** 2026-10-16 · **Reviewer:** orchestrator, in aspirant mode (read-through + scripted checks)
**Scope:** NEW editorial text (foreword, how-to-use, routes, part/chapter intros, cover, back cover), navigation coherence, rendering edge cases, link integrity. Card bodies are verbatim-locked and were NOT re-edited (iron rule 2).

---

## 1. Scripted checks (all re-run after fixes)

| Check | Result |
|---|---|
| Internal anchors | 1,695 hrefs → **0 unresolved** (was 4: `#fm-glance` missing — fixed by adding `id` to fm4 h1; `fm-cover`/`fm-foreword`/`fm-howto` ids added for scheme completeness) |
| Duplicate ids | **0** across 836 ids |
| Card articles | **551/551** present with unique `#card-<ID>` anchors |
| Index links | 551 card links, 209 subtopic rows — every card reachable |
| Image references | 38 refs → all files exist locally (37 card images + resource guide) |
| Sheet pagination | 239 sheets total; every content sheet carries topbar + crumb + stamp + foot |
| Hotlinks | 0 external image srcs; only Google Fonts `<link>` remains (documented, degrades to system fonts offline) |

## 2. Structural defect found & FIXED

**Cards rendered outside sheet containers.** The first build emitted subtopic bands and card articles after each section sheet's closing `</div>` — they would have appeared on the desk background, outside the sage page. **Fix:** `emit_section()` in `convert_cards.py` now auto-paginates section content into magazine sheets (~420 body words per sheet), each with the running topbar (crumb: paper · subject · section), a `SECTION NN · CONT.` stamp on continuation sheets, and the colophon foot. Verbatim verification re-run after the change: PASSED.

## 3. Editorial text review (easy-language audit of NEW text)

- Sentence length spot-checks: all NEW sentences ≤ 20 words (a few route-table cells run to ~22 words in table context — acceptable in tables, not prose).
- No flagged words (spotlight, tapestry, bedrock, pivotal, holistic, multifaceted…) in any NEW text. Verified by scan.
- Route arithmetic verified: GS-2 + GS-4 = 116 + 149 = **265 cards** (as stated in the 60-day route); 30-day sprint ≈ 180 cards ≈ 6/day; 90-day = 551 cards ≈ 6.5/day.
- **Claim softened:** part-opener lede said cards "cover the full official syllabus" — overpromise. Now reads "follow the official syllabus of the paper" + pointer to the tier table.
- **Cross-paper table rebuilt** (fm4): the first draft paired sections within the same paper and used names that don't exist verbatim. Now five defensible pairs built from actual section_group names: Poverty & welfare (GS-1↔GS-2), Climate (GS-1↔GS-3), Accountability & corruption (GS-2↔GS-4), Ethics in world affairs (GS-2↔GS-4), Disasters & hazards (GS-1↔GS-3).
- Tone check: mentor voice consistent (second person, imperative, exam-focused). No idioms found.

## 4. Rendering edge cases reviewed

- Long card titles (up to ~90 chars) wrap cleanly in `.card-h` flex; card-id stamp stays right-aligned.
- 5 practice-skeleton cards carry the `PRACTICE SKELETON` badge; their multi-detail blocks render as labeled panels — no forced intro/conclusion.
- Multi-quote cards (31) render each quote as its own `.pull` — no merges.
- GS4-ETHI-0721's two images render as two separate figures.
- Heatmap rows with 13–15 cells fit the 698px content width (28px cells + 150px label).
- Very long microtopic strings (some >200 chars, e.g. Probity in Governance) wrap in `.card-micro` at 9.5px — acceptable density, kept because they are syllabus text the user assigned.

## 5. Doubts flagged for the user (non-blocking — listed again at the Phase-8 gate)

1. **Cover is typographic** (no artwork) — matches the prototype's design language. Alternative: the resource-guide PNG could be re-purposed, but it is a product sheet, not cover art.
2. **Resource-guide PNG sits on the back cover** as a "Companion resources" figure (Phase-2 proposal). Removal is a one-file edit (`bm2_back_cover.html`).
3. **Part openers and index sheets are longer than one A4 screen**; in print they flow onto continuation pages before the sheet break. Chapter content sheets are budgeted (~420 words) and paginate naturally.
4. **No per-card mentor callouts** were added on top of cards (only front-matter verdict/take blocks). Reason: iron rule 2 keeps the card layer purely verbatim; callouts would blur the boundary. Flag if you want a light "mentor note" layer added in a later edition.

## 6. Verdict

Content layer is structurally sound and navigation-complete. Editorial text meets the easy-language standard. No blockers for assembly (Phase 7).
