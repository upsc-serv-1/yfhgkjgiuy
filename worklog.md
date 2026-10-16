# Worklog — PYQ Nano eBook build (branch: `ebook-build`)

Fresh log for the eBook build. The old content-polishing project's history lives on GitHub `main` — superseded; do not use. Append-only; template in PLAN.md §8.

---
Task ID: 0
Agent: Super Z (main, orchestrator)
Task: Phase 0 — project setup: inputs, governance docs, branch.

Work Log:
- User supplied Stage-2 inputs: merged_publish_ready_v17(1).md (551 cards, `## id:` format — FINAL polished content), DESIGN_MAGAZINE_ARTICLE_PAGES.md, prototype HTML "PYQ Nano Analysis — GS Mains (prototype 25)" (design benchmark), UPSC readymade resource guide PNG.
- User decisions locked: final = editable single-file HTML (not PDF) + A4 @media print CSS; title "PYQ Nano Analysis — GS Mains · The Answer-Writing Playbook"; GS Mains answer-writing audience; modular src/ + assembled final_ebook.html both committed; Foreword + How-to-Use section only; prototype = design source of truth.
- Read prototype structure: Fraunces (display serif) / IBM Plex Sans (body) / IBM Plex Mono (data labels); muted sage-gold editorial palette; inline SVG analytics (marks-share donuts, subject tier tables).
- Wrote PLAN.md (phases, iron rules, QA gates) + HANDOFF.md.

Stage Summary:
- Phase 0 complete. Next: Phase 1 content audit → content_inventory.md, then gate: report to user and WAIT.

---
Task ID: 0-b
Agent: Super Z (main, orchestrator)
Task: Branch restructure per user correction — new project must live on its own branch; repo's existing files are OLD content; v17 is the final truth.

Work Log:
- Mistake: Phase-0 files had been pushed to `main` alongside the old project. Fixed: reverted that commit on `main` (commit 2d89a14) and pushed — `main` is back to its prior state.
- Created orphan branch `ebook-build` containing ONLY this project: inputs/ (4 files), assets/images/, src/, scripts/stage2/, PLAN.md, HANDOFF.md, README.md, this worklog.
- Removed all reconciliation-with-old-repo tasks from the plan: v17 (551 cards) is the sole content truth; the ~238 cards absent from v17 were intentionally excluded by the user (never restore, never re-ask).
- Updated PLAN.md + HANDOFF.md with branch policy.

Stage Summary:
- Project now isolated on `ebook-build`. `main` untouched/old. Next: relaunch Phase 1 content audit (subagent) on this branch.

---
Task ID: 1
Agent: Super Z (main, orchestrator — executed directly; subagent launcher failed twice with "context canceled")
Task: Phase 1 — content audit & image ingestion → content_inventory.md

Work Log:
- Subagent delegation failed twice (Task tool "context canceled") → executed inline, same protocol (persisted scripts, deliverable file, worklog).
- User added requirements mid-phase (captured in PLAN.md §1/§3): SVG illustrations of the prototype's TYPES recreated for our book; index GS-wise → subject-wise within each GS; card taxonomy (paper/subject/section_group/microtopic/subtopic) = indexing skeleton.
- scripts/stage2/audit_cards.py → scripts/stage2/v17_inventory.json: 551 cards, all unique, all `polished`, zero structural defects. 476 structured + 75 detail; 70,145 body words (mean 127). Papers: GS-1=98, GS-2=116, GS-3=188, GS-4=149. 14 subjects (Ethics 149 largest). Taxonomy: 48 section groups → 209 subtopics; 87 microtopics.
- Consistency: 38 `sections:` metadata mismatches, ALL benign (31 multi-quote, 6 multi-detail, 1 multi-image GS4-ETHI-0721; dedupe-verified). 5 detail-led cards without intro/conclusion (GS3-ENVI-0462, GS3-DISA-0483, GS3-INTE-0517/0534/0543). Flags: has_image=36, format_fixed=57, universal_template=5 (practice skeletons).
- scripts/stage2/download_images.py → assets/images/: all 37 image URLs (36 cards) downloaded + normalized ({subject}_{subtopic}_{NN}.{ext}); 1 AVIF converted to PNG via ffmpeg; resume support; 0 broken; ≈8.5 MB. Manifest: scripts/stage2/images_manifest.json. Cover candidate PNG staged.
- scripts/stage2/make_inventory_md.py → content_inventory.md (137 lines, all tables generated from data).

Stage Summary:
- Phase 1 complete, no blockers. Deliverables: content_inventory.md, v17_inventory.json, images_manifest.json, 38 local images, 3 re-runnable scripts.
- GATE: findings reported to user; awaiting confirmation to start Phase 2 (book architecture: prototype reverse-engineering + GS-parted TOC + illustration plan).

---
Task ID: 2
Agent: Super Z (main, orchestrator)
Task: Phase 2 — book architecture: reverse-engineer prototype, define full book structure, card→chapter map, illustration plan.

Work Log:
- Locked Phase-1 gate decisions into PLAN.md/HANDOFF.md (relative image paths; all six recommendations approved) and pushed (2de99a3).
- prototype_skeleton.py → prototype_skeleton.md/.json: 39 sheets, 158 headings, 272 classes, 4,204 ids, 0 unresolved anchors. Prototype anatomy mapped: sheet/topbar/crumb/stamp system, hero openers, donut/band/tier/heatmap/dots analytics, fl-sec/fl-mic/fl-sub index rows, ill-<subject> per-subject illustrations; qm/qr/qx question rows NOT adopted (our unit = article card).
- build_book_map.py → book_map.json: full tree Part(GS)→Chapter(subject, ch01–ch14)→Section(section_group, sg-1..48)→subtopic(st-1..209)→cards(#card-<ID>, 551). Asserts 551/48/209 pass. Body 70,145 words, ~182 body sheets (~205 total incl. front/back matter).
- Wrote ebook_structure.md (Phase-2 deliverable): architecture rule, prototype adopt/adapt table, chapter map, reading flow, card rendering spec (verbatim layer incl. multi-quote, detail labels, practice-skeleton badge, image figures), 9 recreated SVG illustration types I1–I9 driven by our own card data, anchor scheme, GS-4 mini-index, src/ decomposition (21 partials + theme.css), resource-guide PNG back-cover proposal (reversible), out-of-scope list, self-audit.

Stage Summary:
- Phase 2 complete and self-audited: hierarchy == user taxonomy exactly, all 551 cards anchored, images local+relative. Next: Phase 3 design tokens (extract from prototype CSS → design_tokens.md + src/theme.css + component templates).

---
Task ID: 3
Agent: Super Z (main, orchestrator)
Task: Phase 3 — design tokens: extract prototype CSS, build src/theme.css + design_tokens.md.

Work Log:
- Extracted prototype <style> (98.5KB) → scripts/stage2/prototype_style_raw.css; pulled key component rules (book/sheet/topbar/verdict/take/note/hero/gschip/chips/hm heatmap/tier/dots/ov blocks/print media queries).
- Read DESIGN_MAGZ_SPEC.md fully (box anatomy: context/drill/factsheet boxes with left accent bars; booktabs table standard; running footer spec).
- Wrote src/theme.css (12 sections): prototype-parity tokens, sheet system, topbar/foot, headings, card components (pull/ex/data/conc/detail-p/fig/badge-skel), section/subtopic bands, analytics components (band/tier/dots/hm grid), index rows, cover stat strip, A4 print block (one sheet = one page).
- Wrote design_tokens.md: color tokens, type scale, geometry, v17-block→component catalog, I1–I9 illustration library with data bindings, rules of use, self-audit.

Stage Summary:
- Phase 3 complete: design system implemented and documented; every v17 block type has exactly one component mapping; box interior (#F5F8F5) is the only spec-adapted token (logged). Next: Phase 4 editorial layer — foreword, How-to-Use, chapter intros (NEW text) + 551 card bodies VERBATIM into src/ partials via card→HTML converter.

---
Task ID: 4
Agent: Super Z (main, orchestrator)
Task: Phase 4 — editorial layer: 551 card bodies VERBATIM into src/ chapter partials + all front/back matter partials.

Work Log:
- convert_cards.py: v17 → HTML with text-fidelity verification gate (fails hard on any mismatch). Fixed 3 defect classes found by the verifier: (a) leading paragraphs before bullets → element model (parse_elements: 'p' + 'ul' runs); (b) triple-star nested emphasis (**a *b***) via marker pre-pass, em-then-bold order; (c) entity/normalization in the verifier itself. RESULT: VERBATIM VERIFICATION PASSED — all non-image blocks of all 551 cards text-identical to v17.
- 14 chapter partials (ch01–ch14): chapter hero (meta chips + "In this chapter" anchor list), section sheets (kicker + h2 + subtopic chips), subtopic bands + 551 card articles (pull/ex/data/conc/detail-p components, card-id stamps, microtopic lines, PRACTICE SKELETON badges on the 5 flagged cards, image figures via manifest with relative paths).
- build_front.py: fm1 cover (typographic + stat strip), fm2 foreword (NEW mentor text), fm3 how-to-use (card anatomy, 3 navigation paths, visual legend, 30/60/90-day route tables — NEW), fm4 glance (I1 donut by paper, I2 subject bands, I9 cross-paper table — all from book's own data), pt1–pt4 openers (I1 subject donut, I3 tier rows, I5 top-subtopic dot rows, I4 section×subtopic heatmap with links; GS-4 opener carries the locked mini-index).
- build_back.py: bm1 master index (lead sheet + 4 GS-wise sheets: subject → section → subtopic → 551 card links), bm2 back cover (closing note + companion-resources panel with resource-guide PNG per Phase-2 proposal).
- Counts verified: 551 card articles, 551 index links, 209 subtopic rows, 21 partials + theme.css.

Stage Summary:
- Phase 4 complete. All content partials exist; verbatim gate green. Next: Phase 5 student-review pass (editorial text read-through, doubt flags) → review_notes.md; then Phase 6 (toc_index.md), Phase 7 (build.py assembly → final_ebook.html), Phase 8 (QA → qa_report.md → USER GATE).

---
Task ID: 5
Agent: Super Z (main, orchestrator)
Task: Phase 5 — student-review pass: link/nav integrity, editorial text audit, rendering edge cases, fixes.

Work Log:
- Scripted integrity: found 4 unresolved #fm-glance links (missing id) → fixed (+ added fm-cover/fm-foreword/fm-howto ids); 0 duplicate ids; 551 card articles; 551 index links; 38/38 image files exist.
- STRUCTURAL DEFECT FOUND & FIXED: cards were emitted outside .sheet containers (would render on desk background). Rewrote section emission as emit_section() with auto-pagination (~420 words/sheet), running topbars (crumb + SECTION NN · CONT. stamps) + feet. Book now = 239 sheets. Verbatim gate re-run: PASSED.
- Editorial audit: route math verified (265 = GS-2+GS-4), softened "full official syllabus" → "follow the official syllabus", rebuilt fm4 cross-paper table from real section names (5 defensible pairs), banned-words scan on all NEW text = clean.
- review_notes.md written: findings, fixes, 4 non-blocking doubts flagged for the Phase-8 user gate (typographic cover, back-cover PNG role, long opener/index sheets in print, no per-card callouts by design).

Stage Summary:
- Phase 5 complete — no blockers. Next: Phase 6 (toc_index.md), Phase 7 (build.py → final_ebook.html with page-number stamping), Phase 8 (QA audit → qa_report.md → USER GATE).

---
Task ID: 6-7-8
Agent: Super Z (main, orchestrator)
Task: Phases 6–8 — TOC/index documentation, assembly, QA audit (final gate before user).

Work Log:
- toc_index.md: navigation surfaces table, anchor namespace (832+ ids, 0 dupes), index counts, page-numbering scheme.
- build.py: assembles final_ebook.html in reading order (fm → pt+ch interleaved → bm), inlines theme.css, stamps sequential page numbers (NNN / 239) into every .pg-n (topbar stamp + foot), supports --embed base64 mode, runs self-checks. OUTPUT: 1.23 MB, 239 sheets, 551 cards, 0 unresolved anchors.
- qa_check.py (PLAN §6 checklist): card presence 551/551; protected-content verbatim diff of the ASSEMBLED file vs v17 (0 block mismatches, 0 digit mismatches — digit check excludes image blocks whose URLs→local files by design); images 38/38 local with alt; 1,695 links 0 unresolved; heading hierarchy 0 skips; print CSS complete; HTML sanity green (lang/title/meta/fallbacks/no backdrop-filter/balanced tags/page numbers). VERDICT: QA PASSED — all checks green.
- qa_report.md written with full results table + 4 non-blocking doubts for the user gate.
- PLAN.md status table → all phases 0–8 ✅; HANDOFF.md → complete state + rebuild instructions.

Stage Summary:
- Book complete: final_ebook.html (551 verbatim cards, 239 sheets) + 21 modular src/ partials + full pipeline scripts. Phase-8 USER GATE: reported, WAITING for decisions on the 4 doubts (typographic cover / back-cover PNG / long opener sheets in print / no per-card callouts).

---
Task ID: 8R
Agent: Super Z (main, orchestrator)
Task: User design review fixes (v2) — remove blind-copied analytics, make index clickable/prominent, restyle cards as rounded boxes.

Work Log:
- Analyzed user's reference screenshot (VLM): white rounded cards, ~10px radius, soft shadow, coloured section labels (QUOTE/INTRODUCTION/EXAMPLES/CONCLUSION), tinted quote panel.
- Diagnosed v1 defects: part openers + "Book at a Glance" page full of count-analytics (donuts, stacked bands, tier bars, dot rows, 210 heatmap cells); index buried at sheet 228/239; cards rendered as unboxed flows (no visual card boundary).
- theme.css v2: card = white 12px-rounded box + 3px paper-colour top edge (.gs1 gold/.gs2 teal/.gs3 green/.gs4 deep), dashed rule under title, card-id pill; coloured labels + tinted rounded panels for QUOTE (gold)/INTRODUCTION (teal)/EXAMPLES (green)/DATA (deep)/CONCLUSION (green); DETAIL kept sage+gold; analytics CSS (ov/band/tier/dots/hm/legend, --b1..b5) deleted; .to-ix floating INDEX button added (hidden in print).
- convert_cards.py: per-paper card classes; QUOTE/INTRODUCTION/DATA labels added (chrome text only — verbatim gate unaffected); INDEX link appended to every sheet breadcrumb; 551/551 verbatim verification re-passed.
- build_front.py rewritten: fm4 glance page DELETED; part openers rebuilt as pure navigation (part title + chapter chips + syllabus-section links + GS-4 mini-index kept); cover gains CONTENTS + HOW TO USE chips; how-to-use rewritten (card anatomy demo in a real card box, "How to reach any card" = index / INDEX button / breadcrumbs); analytics helpers removed.
- build_back.py: index retitled "CONTENTS · Every card, subject by subject" with explicit click-to-jump lede; back-cover topbar fixed.
- build.py: ORDER now cover → foreword → how-to-use → bm1 INDEX (front position) → parts/chapters → back cover; floating INDEX button injected; card-count regex updated for .gsN classes. qa_check.py regexes updated likewise.
- Rebuilt: 238 sheets, 1.18 MB. qa_check.py ALL GREEN (551 cards, 0 text/digit mismatches, 0 unresolved links, 0 dup ids, headings clean).
- Browser verification (agent-browser): INDEX button click → #ix-master works; trusted click on card title "Medieval Bhakti and Sufi Literature" → card lands at viewport top (y=19503); screenshots vision-checked: card boxes/labels render correctly, part opener has zero charts, index titles clearly clickable.
- Docs updated: design_tokens.md (v2 card system + navigation system replaces analytics library), qa_report.md (v2 numbers + browser checks), toc_index.md (front-position index), PLAN.md (phase 8R + iron rules 11-12), HANDOFF.md (decisions 13-15, #9 superseded).

Stage Summary:
- v2 build complete and pushed: analytics-free, clickable front-matter index, card-in-rounded-box design. All 551 cards still verbatim. Awaiting user acceptance.

---
Task ID: 8R2
Agent: Super Z (main, orchestrator)
Task: User review fixes round 2 (v3 / rebrand) — rename the book, de-clutter pages, make every index level clickable, 2-column index, boxed intro, 2-column data, disclaimer page, logo + contact, no counts anywhere.

Work Log:
- Extracted the Dr. CSE logo (base64 PNG) from the prototype HTML → assets/images/logo_dr_cse.png (420×140, transparent). Brand info pulled from prototype: drcse.in · t.me/dr_cse · dr.cse.001@gmail.com.
- theme.css v3: thin running header (.tb-brand logo + "Dr. CSE — Replica"), .a4 true-A4 pages, boxed .intro (pale-teal panel), .data-cols (2-col DATA walls), .ix-body 2-col index (+ .cols-3/.ix-compact variants), .ix-line subtopic rows, .cover-contact strip; removed .brand/.crumb/.stamp chrome, .card-micro, .cover-stat, all count badges.
- convert_cards.py: microtopic (syllabus point) line removed from cards; chapter heroes rebuilt as SUBJECT PAGES with their own clickable card index (A4, no stat chips; Ethics 149 cards split across 2 compact 3-col sheets); section sheets emit thin header only, no crumb/stamp/counts; is_wide_data() → .data-cols (25 cards incl. GS1-HIST-0012); CHAPTER_META ledes rewritten without counts.
- build_front.py: new cover (logo top-left, "Replica" title, subtitle "EXAM REPLICABLE · INTRO TO CONCLUSION", no stats, contact strip, no footer); NEW fm2_disclaimer.html = page-2 Disclaimer + How to Approach (panels + take + contact strip) replacing foreword + how-to-use (stale partials deleted); part openers simplified (no counts, GS-4 mini-index removed — superseded by Ethics subject-page index).
- build_back.py: master index rebuilt — 2-column, EVERY level clickable (paper/subject/section/SUBTOPIC "Buddhism" → #st-N/card titles), .ix-line rows, auto-paginated by browser-calibrated height budget (BUDGET 1780→2080 after measuring 15–40% under-fill; first-sheet budget reduced by intro block), 7 true-A4 sheets, no counts; back cover rebranded + contact links. Fixed a literal "{FOOT}" leak (non-f-string segment) caught by VLM screenshot review.
- build.py: ORDER updated (fm2_disclaimer), title/meta → "Replica (Exam Replicable) — Intro to Conclusion · Dr. CSE". qa_check.py title assertion updated.
- Rebuilt: 14 chapter partials (551 cards verbatim gate PASSED) + front/back matter + final_ebook.html (1.10 MB, 217 sheets; self-checks OK: 551 cards, 0 unresolved anchors, 0 dup ids).
- Verification: qa_check.py ALL GREEN (protected content 0 mismatches, links, images, print CSS, sanity). Browser measurement: every .a4/.p1 sheet ≤ 1135px (index sheets filled 726–924px). Structure scan: 0 micro lines, 546 boxed intros, 25 data-cols, 216 thin headers, 0 count-stat elements. Click-through (headless): Buddhism → #st-2 ✓, index title → card ✓, subject-page link → card ✓, INDEX button → #ix-master ✓. VLM review of 8 key pages: no defects.
- Docs updated: PLAN.md (phase 8R2 row + product definition v3), HANDOFF.md (full v3 rewrite, decisions #16–#20), design_tokens.md (v3 layer changes), toc_index.md (v3 navigation map), qa_report.md (v3 verdict table + change log).

Stage Summary:
- final_ebook.html v3 complete on branch ebook-build: "Replica (Exam Replicable) · Intro to Conclusion", 217 sheets, all 551 cards verbatim, QA green, browser-verified. Awaiting user acceptance.

---
Task ID: 9D
Agent: Super Z (main, orchestrator)
Task: Documentation pass — DESIGN.md (new), HANDOFF.md refresh, PLAN.md update, README rebrand; push.

Work Log:
- Fact-audited the shipped book directly from final_ebook.html: 217 sheets (2 .p1 cover/back, 27 .a4 = 1 disclaimer + 7 index pages 003–009 + 4 part openers + 14 subject pages + 1 Ethics index continuation, 188 content); 551 cards; 25 .data-cols cards; 38 image figures; 89 detail panels; 5 practice-skeleton chips; 1 floating INDEX button; 215 stamped page numbers.
- Caught + fixed a count error: an earlier anchor-walk suggested 8 index sheets; per-sheet content walk proved 7 (the 8th IX-flagged sheet is the GS-1 part opener carrying ix-cards chips). HANDOFF/PLAN/DESIGN all state 7 now.
- WROTE DESIGN.md: design principles; v1→v2→v3 decision history; book anatomy with sheet census; screen geometry + A4 print rules; full color system (surfaces, semantic accents, tints, per-paper edges); type scale; card component anatomy (ASCII diagram) with rules; editorial components; navigation system; page specs (cover/disclaimer/index/openers/subject pages/card sheets/back cover); hard prohibitions (§11); theme.css §1–11 map + change protocol (§12).
- HANDOFF.md: reading order now includes DESIGN.md; doc-maintained-in-same-commit rule added; §9D status; index-count correction.
- PLAN.md: Phase 9D row added to status table; file map now lists REAL src/ filenames (old planned names removed) + DESIGN.md.
- README.md: rebranded from stale "PYQ Nano Analysis" title to "Replica (Exam Replicable) · Intro to Conclusion — Dr. CSE"; DESIGN.md added to reading order + deliverables chain; no-analytics rule surfaced.

Stage Summary:
- DESIGN.md is the canonical design spec of the shipped book; design_tokens.md remains the token reference. All four docs consistent with the built artifact. Docs-only commit — no HTML/CSS changes, no rebuild needed.

---
Task ID: 10-DF
Agent: Super Z (main, orchestrator)
Task: Book 2 — "Dr. CSE — Data & Facts": finish the interrupted build (fix defects found mid-pipeline), verify, document.

Work Log:
- Found the previous session's untracked WIP: inputs/updated_data.json (83 data cards), scripts/stage2/datafacts/{parse_data,build_book,qa_check_df}.py + df_book_map.json, src/datafacts/ partials, final_data_facts.html — build was interrupted mid-way with 6 QA failures and no worklog entry.
- Diagnosis (6 QA fails → 4 root causes): (a) parse_data.py split content_markdown on '<br>' which TEARS APART tables containing <br> inside cells — GS2-POL-0006 EMERGENCY rendered an unclosed <table> + literal escaped '</td></tr>' text on the card; (b) Packer.flush() emitted content fragments WITHOUT the .sheet wrapper (no page background/padding/print pagination, no subject attribution, partials never persisted); (c) continuation fragments never re-opened <article> (83 open / 123 close); (d) table height estimator was flat 95px (a 17-row table is ~370px+) → overflow risk; plus QA-script bugs (counted '<table>' inside a CSS comment, page-number expectation -1 instead of -2).
- parse_data.py: split_lines() now protects <table>...</table> spans with placeholders before the <br> split, restores them as atomic lines → EMERGENCY table whole; source scanned clean for other cross-fragment tag hazards (0).
- build_book.py: flush() wraps every content sheet in <div class="sheet" data-ch="ch-N">; subject pages carry id + data-ch; cont_html re-opens <article class="card gsN cont-art"> (dashed top edge) with CONTINUED strip + fresh .rows so every fragment is a complete box (anchor stays on first fragment); emit_card streams at ROW granularity via block_units() (tables atomic); table-aware estimator (46 + 24·<tr>, full height; fact rows ×0.55 for 2-col flow); attribution + partial persistence via data-ch regex → all 110 partials now persisted (df_ch-N_MM.html fragments included).
- Mid-fix regression caught by QA: my first block_units() rewrite dropped the ROWS of 'section' blocks via a stray continue (24 rows lost on GS3-ENV-0001 alone, 181 lines missing book-wide) — fixed; also removed the double '<div class="rows">' begin_flow_card appended to the now self-contained cont_html (49 unbalanced divs) — fixed.
- theme.css (datafacts): added .card.cont-art{border-top-style:dashed}; .fig/.fig img for the back-cover companion figure; back-cover figure constrained to max-width:480px (was full-width → 1427px tall sheet; now every sheet exactly 1123px).
- qa_check_df.py: strips <style> before tag-balance; page-number expectation sheets-2 (both covers carry no foot); residue scan ignores <br> inside protected tables; NEW escaped-table-markup leak check (catches the EMERGENCY bug class).
- measure_df.py (new, persisted): headless playwright — sheet heights (min/median/max 1123/1123/1123, 0 over 1135), horizontal overflow 0, click-through index link → #card-GS2-POL-0006 lands top=12 visible, floating INDEX → #ix-title top=12; 8 screenshots.
- Rebuilt: final_data_facts.html 110 sheets / 471 KB; qa_check_df.py ALL GREEN (83 anchors, verbatim 0 missing, tag balance all equal, 136/136 flow-card fragments, chrome + page numbers consistent, no stats). VLM review of 8 key pages (cover, disclaimer, index, opener, subject page, EMERGENCY table card, INFRASTRUCTURE tables card, continuation fragment): 8/8 PASS.
- Docs: DESIGN.md §II (§13–§16: data-card anatomy, flowing cards, sheet map, pipeline + change protocol); HANDOFF.md Book-2 section + refreshed header/reading order; README.md restructured as two-book library with both rebuild chains.

Stage Summary:
- Book 2 "Dr. CSE — Data & Facts" complete: final_data_facts.html (110 A4 sheets, 83 verbatim data cards, every number dated + sourced, full clickable navigation) + complete modular src/datafacts/ partials + self-contained pipeline (parse→build→qa→measure, all green). Same iron rules as Book 1 (verbatim rows, no count stats, relative-path images, ebook-build only). Awaiting user acceptance.

---
Task ID: A4-1
Agent: Super Z (main, orchestrator)
Task: Multi-phase structural repair of Book 2 (Dr. CSE — Data & Facts) — Phase 0 discovery + Phase 1 A4 geometry/footer.

Work Log:
- PHASE 0 (diag_phase0.py, measurements on all 110 sheets): pipeline = build-time Python Packer (parse_data.py → df_book_map.json → build_book.py → final_data_facts.html) + Chromium print-to-PDF; screen .sheet = block 794×1123.
- Root causes measured: (1) footer floats — .sheet display:block, no pinning (disclaimer foot at 580px, 525px dead space below); (2) index/book order GS3→GS2→GS1 (JSON first-appearance order rules the tree); index sheets fill 17–47%, paper headers appended before fit-check; (3) 13 orphaned-heading sheets (sub-h/sec-h last element before foot; Manufacturing Sector = sheet 13, card on 14) — Packer lacks keep-with-next; begin_flow_card 220px guard insufficient for tall tables; (4) card-id chips + "SUBJECT NN" serials visible; (5) parse rule 6 merges soft-wrapped lines into dense rows; (6) .srcs panels duplicate 556 inline citations (only GS2-GOV-0007 has none inline).
- PHASE 1 (theme.css §3/§11, build_book.py backcover): .sheet flex column + .foot margin-top:auto → footer pinned at exact 24px offset on every sheet regardless of content; print rebuilt full-bleed: @page A4 margin:0, .sheet width 210mm min-height 296.5mm, html background sage (sliver cover), removed .rows{column-fill:auto} (print-only multicol non-fragmentation stacked all rows into col 1 → 50 sheets doubled → 184 PDF pages; root cause, not a CSS patch: build-time pagination means print must mirror screen balance); back cover: cover-contact margin-top:0 inline (flex doesn't collapse parent/child margins; was 13px over A4).
- Gates: verify_phase1.py — 110/110 sheets exactly 794×1123 flex; footGap min/max 24/24px; PDF via Playwright page.pdf(A4,0,printBackground) = exactly 110 pages, all exactly 595.3×841.9pt; qa_check_df.py ALL GREEN; VLM visual check 6/6 (disclaimer, short, full, 3 random): footer bottom-pinned, no clipping.

Stage Summary:
- Phase 0 + 1 complete and committed (7fdb750). Next: Phase 2 — keep-with-next in Packer (card heads, sec-h/sub-h bands, sth sub-headings) to kill all 13 orphaned headings incl. Manufacturing Sector; then Phase 3 index rebuild with GS1→GS2→GS3.

---
Task ID: A4-2
Agent: Super Z (main, orchestrator)
Task: Phase 2 — page-break/chapter-break rules (keep-with-next).

Work Log:
- build_book.py Packer rebuilt: add(html,px,keep_next) — heading units move to a fresh sheet BEFORE placement unless their required following content fits (kills orphaned headings at the root, not via CSS patches).
- Keep chains: sec-h → sub-h → card head → first content unit (full px, capped only in degenerate mega-unit case); sth/ssec → run of following headings + first row/table. begin_flow_card(head+first_px) replaces the 220px magic guard that orphaned titles above tall tables.
- Estimator: CARD_MARGIN_PX=18 added per card fragment (real box-model cost was unaccounted — caused sheet 67 @1130px overflow); flush() stamps data-est for calibration (real/est 0.76–1.06, median 0.90 → healthy headroom).
- theme.css print: blanket .card{break-inside:avoid} removed (long cards flow via CONTINUED fragments; selective .card-h/.row/.sth/.tblwrap avoids kept). No column-fill:auto (see A4-1).
- Verified: 114 sheets; 0 orphaned headings (DOM last-element scan, all sheets — stronger than the 10-transition spot check); Manufacturing Sector band + SECONDARY SECTOR card same sheet; all subject pages fresh-sheet chapter openers; fills median 75%, under-40% sheets are hero/front pages only; PDF = 114 pages all A4; qa_check_df.py green.

Stage Summary:
- Phase 2 complete (commit 2nd of fix-A4 series). Next: Phase 3 — index rebuild with GS1→GS2→GS3 paper order (tree sorted at parse level), atomic subject blocks, no orphaned paper headers, balanced fill.

---
Task ID: A4-3
Agent: Super Z (main, orchestrator)
Task: Phase 3 — rebuild the index (order, atomicity, page numbers).

Work Log:
- parse_data.py: tree.sort(key=paper key) — root fix for GS-III-first order (JSON appearance order ruled book+index); subject order within papers preserved from taxonomy.
- build_book.py index rewritten: _subject_block() atomic blocks; paper header concatenated with first subject block; _ix_line_est calibrated (browser-measured est/real 1.95–1.98 → x0.30 line factor, IX chars 60); INDEX_BUDGET 1060 (tuned 930→1060 empirically; 3 sheets [65/58/18] → 2 sheets [73/58]).
- Page numbers: build_pagemap() from final ordered sheets; index_sheets(pm) fixpoint-iterated in main() until count stable + convergence assert; .pg spans (cards '· N', subjects/papers 'p. N') styled muted mono in theme.css §8.
- Stale partial cleanup on rebuild (df_*.html wiped — paper renumbering ch-1..ch-12 changes filenames between runs).
- Verified: index order GS-I→GS-II→GS-III (+ book openers same); subjects in taxonomy order; 0 orphaned headers; 95/95 index page numbers == stamped positions; stamps==positions all sheets; geometry regression (A4/foot/orphans) clean; VLM visual 2/2 (hierarchy clear, no stranded headings, footers pinned). Book now 112 sheets.

Stage Summary:
- Phase 3 complete. Next: Phase 4 — card visual cleanup (remove card-id chips 'GS3-ECO-0002' from heads+CONTINUED strips, drop 'SUBJECT NN' serials from subject pages; anchors untouched).

---
Task ID: A4-4
Agent: Super Z (main, orchestrator)
Task: Phase 4 — card visual cleanup.

Work Log:
- build_book.py: card_head_html() drops the card-id chip (kept DATA: year chip; empty card-ids div omitted); cont_html() drops c-id span; emit_subject() hero-tag now 'GS PAPER N' (SUBJECT NN serial removed). Anchors untouched — 83/83 intact, all index/subject-page links resolve.
- theme.css: dead .card-id / .cont .c-id rules removed.
- Verified: 0 taxonomy codes in visible text (regex over tag-stripped doc), 0 serials, sample titles clean across subjects; geometry regression (112 sheets, 0 tall, 0 bad-foot, 0 orphans); VLM 5/5 pages — no codes visible, cards clean/distinct/scannable, no defects.

Stage Summary:
- Phase 4 complete. Next: Phase 5 — JSON-level content restructuring (dense cards → clean bullet hierarchy) — the first content-truth phase; verbatim gate will be re-baselined against the restructured JSON.

---
Task ID: A4-5
Agent: Super Z (main, orchestrator)
Task: Phase 5 — JSON-level content restructuring (one fact per bullet, grouped subheadings, clean nested levels).

Work Log:
- Discovery (analyze_density.py): 83 cards = 2009 rows, 17 prose rows, 16 soft-wrap continuations (parse rule 6 joins → dense rows), 94 long bullets (>220 chars), 133 multi-fact bullets, 79 broken-indent children (level-0 facts directly after label bullets), 10 visible '\n\n### Section Group:' generator artifacts (rendered as literal text — QA residue scan had no ### check), 29 raw <b> tags outside headings/tables that parse's inline() ESCAPES into visible literal '<b>' text (3+ confirmed rendering in the shipped book; verbatim gate blind to it because entities unescape+strip as tags during checking). BEFORE screenshots + VLM review of the 5 densest cards (General/GOV, Social Sector, Disaster Stats, Climate Change, Energy) confirmed all defect classes visually.
- restructure_json.py (new, persisted): canonicalises inputs/updated_data.json content_markdown into a documented grammar — <b><u> → section; • <b><u> → sub; • <b>Label</b> → NEW minor tier; - fact / &nbsp;×4N- fact → rows level 0..N; <table> atomic. 233 logged operations: 27 fact splits at paren-depth-0 ';', 21 continuation joins, 5 fragment-bullet merges, 144 label promotions (• <b> form), 19 broken-child indent fixes, 10 artifact drops, 10 list-number drops, 3 bare→bullet; hierarchy reconstructed via container-stack (labels reset depth, children = container+1; source levels decide WHO nests, canonical levels decide HOW DEEP). GUARANTEE: per-card alphanumeric-stream equality before/after, every deviation a position-anchored logged drop (artifact/number) — OK 83/83.
- Review discipline: all 27 splits + 5 merges checked one-by-one; 4 false-positive labels force-kept as facts (Target: 2500 / Operational: 314 / No state has > 20% women MLAs / No Institute in TOP 100 — numbers must stay in body for Phase 6 highlighting); 'Advancing women's equality ->' arrow stripped; Energy's broken 2-line intro (bold head + MoSPI citation) merged then promoted via new C5 rule.
- Parser: rule 3b recognises • <b>X</b> → kind 'minor' (STATS.minors=144). Builder: minor → .sth2 unit (STH2_PX=20) + keep-with-next chains include 'minor'. CSS: .sth2 quiet label (sans 600 9.5px, ink-h, gold tick ::before, in-column — NOT column-span) + print break-inside/after rules. qa_check_df.py: residue scan now also catches '###' and &lt;b&gt;/&lt;/b&gt;/&lt;u&gt; escaped-tag leaks.
- Bug caught mid-phase: serializer wrote 1 &nbsp; per level but parser computes level = entities/4 → all 393 l1 rows collapsed to l0 (verify census all-l0 exposed it); fixed to 4 entities/level, restored JSON from backup, re-applied, rebuilt.
- Gate (verify_phase5.py): 144/144 .sth2 rendered; levels l0=1448/l1=393/l2=36/l3+=0; 0 .sth2 orphans; 114 sheets all exactly A4 794×1123, foot pinned 24px everywhere, 0 DOM orphans; 98 index page numbers all correct (fixed 2 verify-script bugs: .pg pairing in multi-card lines, sheet-own-id anchor capture); PDF=114 A4 pages; qa ALL GREEN; VLM 5/5 PASS (labels as headings w/ gold tick, nested hierarchy visible, zero junk, one fact per bullet).

Stage Summary:
- Phase 5 complete: JSON is canonical + fully verbatim-preserved; book renders 3-tier hierarchy (sub-theme → group label → nested facts). Next: Phase 6 — exam-data highlighting (bold + orange), subject-by-subject with batch self-checks.

---
Task ID: A4-6/7
Agent: Super Z (main, orchestrator)
Task: Phase 6 (exam-data highlighting, bold+orange) + Phase 7 (persist highlighting in JSON schema).

Work Log:
- highlight_json.py (new, persisted): adds {{hl}}…{{/hl}} markers to fact rows in inputs/updated_data.json. P1 = author-bold data spans (digits, not label-colon, not list-number-prefix; link-bearing spans split — link text stays plain, digit segments highlighted). P2 = unit-regex numeric phrases (money ₹/Rs/$/USD + number + multiplier chain incl. lakh-crore, %, per cent, GW/MW/km/kg/cm/tonnes…, ranges N–N, bare ordinals 1st/2nd/…, multiplier+physical-unit '1 lakh MW'). P3 = closed-list extensions ('% of GDP/land/…', ordinal + ≤3 words, 'in/by/since FYxx/20xx'). Flags: 73 counted-noun data points ('1,522 mandis') left plain for human review.
- Review-driven regex fixes (all caught by span dump review, never shipped): (1) NUM alternation spliced un-parenthesized → split the whole phrase pattern ('Rs 73' without unit, '5%' out of '92.5%'); (2) MONEY? attached its ? to the trailing \s, making the money prefix MANDATORY (every unprefixed number missed); (3) EXT_OF open noun list matched verbs/preps ('of women run') → closed examy-noun list; (4) numbered labels ('5. Small Hydro energy') excluded; (5) link regions never highlighted.
- Renderer: parse_data inline() converts marker → <b class="hl"> (after MD_BOLD); visible_text strips markers (verbatim gate marker-blind). theme.css: --hl #C2410C (orange-700, 5.2:1) + .row b.hl. qa_check_df residue now also guards literal {{hl}} in HTML.
- Applied: 2407 spans / 83 cards / 14.8% of fact-row chars; 0 cards over the 50% cap (1 card at 48% — Climate Risk Index, tiny data-dense card, accepted + logged); all 12 subjects covered (46–558 spans).
- Gate verify_phase6: 2407 markers == 2407 rendered b.hl (traceability); 0 junk spans (all contain digits); 0 hl in tables/headings; geometry/orphans/index clean; 16 pages screenshotted across all 12 subjects; VLM 10-second scan test 8/8 PASS (numbers pop, consistent, no junk, no misses, density reasonable).
- Phase 7 (verify_phase7): marker well-formedness (0 unbalanced/nested/misplaced); PERSISTENCE — wiped book map + partials, JSON-only regeneration → byte-identical build, 2407 b.hl, QA green; LEGACY backward-compat — pre-phase6 unmarked JSON builds 0 b.hl, 0 residue, QA green; convention documented in DESIGN.md §14 + parse_data docstring + highlight_json header. (Op note: one --apply run died on SIGPIPE from `| head` before json.dump — detected by the gate's 0-marker count, re-run cleanly; lesson: no pipes on apply runs.)
- Backups: inputs/updated_data.pre-phase6.json.

Stage Summary:
- Phases 6+7 complete: exam data now bold+orange, persisted in the JSON, reproducible from source alone. Next: Phase 8 — remove duplicate SOURCES panels (keep inline citations; panel only for cards that lack inline citations).
