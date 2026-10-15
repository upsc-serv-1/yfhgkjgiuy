# PLAN.md: UPSC Mains "Intro and Conclusions" ebook polish

> **⚠️ STAGE 2 HAS STARTED (2026-10-16).** This file documents **Stage 1 (content polishing), which is COMPLETE and FROZEN.**
> The project has moved to Stage 2: building the HTML eBook from the publish-ready cards.
> **Read `PLAN_EBOOK.md` (Stage-2 plan) and `HANDOFF.md` (live status) first.**
> The protected-content rules in this file (§3) STILL APPLY to every agent touching card content.

# START HERE (status at handoff, written when the previous agent stopped)

**Done:** **ALL 789 of 789 cards are polished.** `MERGED_full_1-789.md` covers every card and passes `verify_protected.py` with **0 errors** (772 warnings, all of the accepted kinds in section 14). GS-2, GS-3, GS-4 and GS-1 are all fully done.. All pass `verify_protected.py` with **0 errors** (no quote, number or data item lost or changed). About 456 warnings remain; they are the accepted kinds explained in section 14 (short fact lines, term-list cards, expanded abbreviations).
**Not done:** cards 1 to 156 (GS-1: History 1-85, Society 86-105, Geography 106-156) and **No cards remain.** The project is complete. Remaining work is user review of `review_queue.md` flags. **The user wants every batch pushed to GitHub** (repo `upsc-serv-1/yfhgkjgiuy`, token supplied in chat) with a commit named after the batch; batches 14-corrections, 15 through 40 are already pushed.

**What the user needs from you:** (1) continue polishing in batches of 20 using the method in sections 5, 7, 11, 14, 15; (2) after every batch run `verify_protected.py`, then update section 8, section 12 and `review_queue.md`; (3) keep replies short, because long replies get cut off by the chat; (4) never invent facts, never change quotes or numbers.

**Files the user will give you:** this `PLAN.md`, `review_queue.md`, `convert.py`, `verify_protected.py`, the `tools/` folder (has `bb.py` and example batch scripts `build_batch01..13_example.py`, plus `merge_batches.py`), the `polished/` folder, and the original JSON `*_mains_intro_conclusions.json`. Before starting, set `SRC` at the top of `convert.py` to the JSON path, and copy `convert.py` into the folder that `verify_protected.py` imports it from (see the GOTCHA in section 11).

**Ways to split the work between several agents (each needs the same files):**
- Agent A: Science and Technology 417-427 and Environment 428-479 (batches 14 to 16).
- Agent B: Disaster Management 480-504 and Internal Security 505-543.
- Agent C: Ethics 544-789 (246 cards, the biggest job; can be split into 544-666 and 667-789).
- Agent D: GS-1 cards 1-156 (History, Society, Geography).
- Agent E (second pass): re-polish the lightest batches (10, 11, 12, 13: Economy, Agriculture, Sci and Tech cards 337-416) with stronger rewriting if the user says they are still too close to the old edition.
- Agent F (review): resolve items in `review_queue.md` once the user decides (fill templates, verify quote attributions, fix flagged facts).
Each agent writes batch files named like `polished/<PAPER>_<SUBJECT>_batchNN_cardsA-B.md` with its own batch numbers (agree on ranges first), and a separate `review_queue_<agent>.md`; merge at the end with `python3 tools/merge_batches.py out.md`.
**Important when several agents work in parallel:** do not edit another agent's range; do not renumber cards; card IDs and numbers come from the original JSON order.

---


Handoff file. A new agent should read this fully, then continue from "Progress tracker".
The user supplies: this PLAN.md, the original JSON, and the files listed under "Tooling".

## 1. Project in one paragraph
The user is turning an earlier-edition JSON of UPSC Mains answer-writing cards (789 cards) into a new ebook edition.
The content must be **polished so it does not look like a copy of the old edition**, while academic quality is
maintained or improved and **protected content (quotes, data, facts) is never altered**. The final output is Markdown
with uniform tagged blocks so the user's designer AI agent can parse it with Python scripts and auto-style it.
The user writes in rough, typo-heavy English. Reply in simple clear English and keep replies short.

## 2. Source data
File: `*_mains_intro_conclusions.json`. A list of 789 objects with keys
`paper, subject, section_group, microtopic, subtopic, card_title, body, hierarchy_path`.
`body` is Markdown-like text with top-level labels such as `*   **Introduction:**`.
- Papers: GS-4 = 246 cards, GS-3 = 215, GS-2 = 172, GS-1 = 156.
- Subjects: Ethics 246, History 85, Polity 64, Governance 52, Environment 52, Geography 51, Sci and Tech 44,
  Internal Security 39, International Relations 33, Economy 31, Disaster Mgmt 25, Agriculture 24,
  Social Justice 23, Society 20.
- There are **44 distinct section-label combinations**. Cards are deliberately NOT uniform (sources differ).
  Top: Quote+Intro+Examples+Conclusion (221), Intro+Conclusion+Data (80), Intro+Conclusion (74),
  Concept only (73), Intro+Data (55), Quote only (50), Examples only (49), Intro only (36), Quote+Intro (34).
- Some bodies contain `<img ... src=...>` diagram links (47 cards). Keep them attached to their card.

## 3. Decisions made with the user (LATEST RULES WIN)
1. Do NOT force one template on all cards. Never add sections that a card did not have.
2. **Do not add anything new** (no new quotes, data, examples, keywords, "way forward" lines).
3. **Polish language** of `introduction`, `conclusion` and `examples` blocks in structured cards so the
   book feels freshly written. Improve clarity and flow; fix grammar, spelling and stray `*`.
4. **Protected, never change:** quotes (text and attribution), all numbers, years, percentages,
   names of people, institutions, schemes, laws, article numbers, case/judgment names, place names, theory names,
   and every item of a `data` or `detail` list (no item may be dropped, merged away or added; keep order and nesting).
   Reordering blocks is allowed. Changing protected facts is not.
   **UPDATE (user, after batch 01): shorthand and short forms MUST be expanded and wording improved everywhere, including inside `data` and `detail`
   blocks, because someone could claim the old text was reused.** Only quotes and image blocks stay exactly as they are.
   **ABBREVIATION POLICY (user): keep universally known exam abbreviations as they are. Do NOT expand SC, HC, PM, VP, EC, CJI, IPC, UOI, FRs, DPSPs,
   UCC, RPA, GDP, NITI Aayog-type names, etc. (for example keep "SC struck down...", never "Supreme Court" in place of SC).** Expand only informal note-taking
   shorthand that students would not write in an answer: imp, b/w, obj, ppl, u/s, govt, w.r.t, dev, temp, "Ex:" and similar. Never use an abbreviation for
   anything other than its standard meaning.
5. Chosen layout is **Design A**: clean labelled blocks, one block per element, quote shown as a pull-quote.
6. Output is Markdown, **one card = YAML metadata + `:::block` sections** (schema in section 4).
7. Cards that are just a topic with no quote or intro (Concept only, Examples only, Data only, etc.) become
   `card_type: detail`, with the original label kept as `:::detail label="Concept"`.
   For detail cards: fix grammar and stray `*` only. Do not restyle unless the user asks.
8. **Truncated or placeholder (`__`) cards:** do NOT invent missing text. Leave the broken sentence as is,
   flag it, set `status: needs_review`. The user will decide later.
9. Block order inside a card: quote, introduction, examples, data, conclusion (the conclusion always closes).
10. Keep useful bold on key terms. Remove stray or unbalanced `**`.
11. "Same as above" cards: keep text, flag `same_as_above`, and do not reorder cards in a way that breaks them.

## 4. Markdown schema (what the designer's script reads)
```
---
id: GS2-POLI-0159            # paper-subject4-globalIndex(1-based, original order)
paper: "GS-2"
subject: "POLITY"
section_group: "..."
microtopic: "..."
subtopic: "Amendments"
card_title: "Significant Provisions and Amendments"
card_type: structured         # or detail
sections: [quote, introduction, examples, conclusion, image]
flags: [has_image]            # truncated, placeholder_blank, placeholder_quote, same_as_above (also cross-refs like "Refer to..."), has_image, format_fixed
status: polished              # polished | untouched | needs_review
---

:::quote
"..." — Name
:::
:::introduction
paragraph
:::
:::examples
- bullet
:::
:::data
- **Label:** nested bullets allowed
:::
:::conclusion
paragraph
:::
:::detail label="Concept"
...
:::
:::image
https://...png
:::
```
A card can have several `:::quote` blocks (one per quote). Only blocks that existed in the original appear. `sections:` lists exactly the blocks present, in order.

## 5. Polish style guide (for introduction, conclusion, examples)
- **HARD RULE (user): LANGUAGE MUST BE EASY. A student must be able to remember it and write it in the exam.**
  Use everyday words and short sentences (aim for 12 to 20 words, never above 25). One idea per sentence.
  No bookish, flowery or "AI-sounding" words (spotlight, tapestry, bedrock, pivotal, holistic, multifaceted, etc.).
  No idioms or poetic phrases (for example "take to heart", "stir a connect"). Prefer "ability" to "capacity", "shows" to "underscores".
  Rewriting must change structure and words, but only into simpler or equally simple English, never harder English.
  Test each line: "Could an average aspirant reproduce this from memory in the exam hall?" If not, simplify it.
  `verify_protected.py` warns on sentences above 25 words and on a list of hard words; a human read is still needed.
- **LESSON FROM THE PILOT: the first pilot polish was too light (only grammar fixes, same sentences). The user compared it with the
  old file and saw it was nearly word-for-word the same. A polish MUST be a real rewrite:** new sentence structure, new
  vocabulary, same meaning. Only protected items (section 3, rule 4) stay as they were. Target: word similarity to the
  original below 0.70 for every polished block (`verify_protected.py` warns above 0.70).
- Do not just swap synonyms. Restructure the sentence (reorder clauses, change the opening, merge or split sentences).
- Good vs bad (Empathy card). Original: "Empathy is the ability to perceive and internalize others' emotions, experiences, and struggles."
  Bad (too light): "Empathy is the ability to perceive and internalise others' emotions, experiences and struggles."
  Good (simple AND different): "Empathy is the ability to understand and share what others feel."
  Too fancy (do not do this): "Empathy is the capacity to sense what others feel and to take their struggles to heart."
- Goal: sound fresh, crisp and exam-ready, not like a paraphrase of the old text. Fix awkward or ambiguous grammar.
- Introduction: 1 to 2 sentences, defines or frames the topic. Conclusion: 1 sentence, forward-looking or value-based.
- Examples: parallel, short bullets, each ending with a full stop. Start with the named entity in **bold** where natural.
- Spelling: Indian/British style (internalise, programme). Use "and" not "&" in prose. Serial comma is not required.
- Keep standard abbreviations (SC, HC, PM, EC, FRs...). Expand only informal shorthand. Do not swap an entity for a different one.
- Never add a fact, number, example or claim that is not in the original card. Never "improve" a quote.
- If an example looks factually doubtful, DO NOT fix it silently. Leave it and add it to `review_queue.md`.
- Keep the two-layer feel: short and scannable first, nothing bulky.
- Worked reference: compare `pilot_cards.md` (before) with `pilot_cards_polished.md` (after, second and stronger pass).

## 6. Tooling (files the user keeps and re-shares)
- `convert.py`: JSON to schema-valid Markdown (no polishing, just structure, flags, and `**` fixes).
  `python3 convert.py out.md 159 11 138`  (ids are 1-based positions in the JSON list). Omit ids for all 789.
  **Update `SRC` at the top** to the actual JSON path in the new session.
- `verify_protected.py`: run on every polished batch: `python3 verify_protected.py batch.md`.
  ERROR = quote or image changed, a data/detail list lost or gained items, or any number differs. Must be zero errors before delivery.
  WARN = a capitalised name or acronym is missing (check by eye; expanded acronyms are fine), or a polished block is
  still more than 70% similar to the original (rewrite it more). Stray warnings such as a sentence-start word like "It" can be ignored.
  It reads originals through `convert.py`, so both must be in the same folder or on the path.
- `pilot_cards.md`, `pilot_cards_polished.md`: 5-card style reference (Amendments, Mughal Architecture,
  Volcano distribution, Empathy, Leopold's Land Ethics).
- Integrity test already run: the converter changes **zero words** across all 789 cards (markup and ordering only).
  Dry-run stats: 646 structured, 143 detail; flags: format_fixed 74, truncated 63, has_image 47,
  placeholder_blank 24, same_as_above 2. The `truncated` flag is a heuristic (no end punctuation); expect some false positives.

## 7. Workflow for the next agent
1. Run `convert.py` for one batch (about 25 to 40 cards, same subject) to get structured Markdown.
2. Polish the introduction, conclusion and examples blocks by hand-writing the new wording (no automated rewriting).
   Keep every protected item. Set `status: polished`. Leave truncated cards untouched with `status: needs_review`.
   Leave detail cards `status: untouched` (grammar and `*` fixes only).
3. Run `verify_protected.py`; fix every ERROR; read every WARN.
4. Save to `polished/<PAPER>_<SUBJECT>_batchNN.md`; present the file; update section 8 below.
5. Keep a running `review_queue.md` of: truncated cards, `__` blanks, doubtful facts, doubtful quote attributions,
   "same as above" cards.
6. At the end: merge batches, run verify on the merged file, hand to the user.

## 8. Progress tracker (update this table every batch)
Card numbers are 1-based positions in the original JSON list. Ranges below were computed from the file.
| Paper / subject | Cards (range) | Count | Polished | Notes |
|---|---|---|---|---|
| Pilot | 5 cards | 5 | done | style reference only |
| GS-1 History | 1-85 | 85 | 85 DONE | batches 33-37 |
| GS-1 Society | 86-105 | 20 | 20 DONE | batches 37, 38 |
| GS-1 Geography | 106-156 | 51 | 51 DONE | batches 38, 39, 40 |
| GS-2 Polity | 157-220 | 64 | 64 DONE | batches 01 to 04 |
| GS-2 Governance | 221-272 | 52 | 52 DONE | batches 04 to 06 |
| GS-2 Social Justice | 273-295 | 23 | 23 DONE | batches 06, 07 |
| GS-2 International Relations | 296-328 | 33 | 33 DONE | batches 07 to 09 |
| GS-3 Indian Economy | 329-359 | 31 | 31 DONE | batches 09 to 11 |
| GS-3 Agriculture | 360-383 | 24 | 24 DONE | batches 11, 12 |
| GS-3 Science and Technology | 384-427 | 44 | 44 DONE | batches 12 to 14 |
| GS-3 Environment | 428-479 | 52 | 52 DONE | batches 14 to 17 |
| GS-3 Disaster Management | 480-504 | 25 | 25 DONE | batches 17, 18 |
| GS-3 Internal Security | 505-543 | 39 | 39 DONE | batches 18 to 20 |
| GS-4 Ethics, Integrity and Aptitude | 544-789 | 246 | 246 DONE | batches 20, 31, 32 |

**PROJECT COMPLETE: 789 of 789 cards polished; full merge verified at 0 errors.**

## 9. Open questions still to ask the user
- One big Markdown file, or one file per paper or subject? (Per subject suggested for the designer's script.)
- Did the designer's script accept the tag names `:::quote`, `:::detail` and the metadata fields? Adjust the schema before the full run if not.
- Should a separate pass flag doubtful **quote attributions** (flag only, never change)? Known examples:
  a Kabir line credited to Tagore (Medieval Bhakti and Sufi Literature card), and "Sant Kabir Akademi" (unverified).
- Should `detail` cards also get light polishing, or stay as they are?
- Do the original-order "Same as above" cards need a fix (for example by pointing to the card title)?
- Known original defects found: missing space after a comma-bold join (Empathy card, "struggles,**It bridges"), dangling
  fragments (Mughal Architecture intro "Golden period."), truncated Geography intro and conclusion.

## 10. Hard rules recap
Never alter quotes or data. Never invent. Never remove a card. Never reorder cards in a way that breaks
"same as above". Always run the verifier. Always flag, never silently fix, anything doubtful.

## 11. Lessons from batch 01 (read before starting a batch)
- **Subject index ranges are NOT guessed.** Always compute them: `[i+1 for i,x in enumerate(d) if x['subject']=='POLITY']`. Polity is 157 to 220.
- Real cards are often **notes-style** (shorthand like "imp", "b/w", "obj", "u/s", "ppl"). Intros and conclusions often hold bullet lists of
  facts (case names, articles, committees). For those: rewrite the wording in easy English, keep every case name, article, committee, number and
  quoted phrase. Expanding informal shorthand (not standard abbreviations like SC, HC, PM) in intro, conclusion and examples is welcome. **Data and detail blocks are also polished (user decision after batch 01):** expand shorthand, fix grammar, reword in easy English, but keep every list item, number, name and theory.
- Fact-dense short lines (for example "SC struck down electoral bonds scheme") have little room to reword. A similarity warning on these is acceptable.
  Do not change meaning just to beat the check.
- Never change a name's spelling, even if it looks wrong (for example "Narsimha Rao"); list it in `review_queue.md`.
- Cards that have only quotes, or placeholder or cross-reference text, are not polished. Mark `status: untouched` or `needs_review`.
- `convert.py` was patched in batch 01: multiple quotes are split into separate blocks, placeholder text and fake "Source Text" attributions are flagged,
  truncation is judged only on paragraph-style intros and conclusions, and cross-references ("Refer to", "Same as") are flagged.
- `verify_protected.py` was patched: name-check noise from sentence-opening words was removed.
- **Converter bug fixed in batch 02:** lines after a `Quote` label that did not start with `>` were glued into the quote. Now only `>` lines are the quote;
  other lines go into `:::detail label="Attached points"`. Affects cards 187, 197 and 385 only.
- **GOTCHA:** `verify_protected.py` imports `convert.py` from `/mnt/user-data/outputs` FIRST. After every change to `convert.py`, copy it there
  (`cp convert.py /mnt/user-data/outputs/`), or the verifier will compare against an outdated converter and report false errors.
- Example build scripts for the dict-and-replace method are in `tools/build_batch01_example.py` and `tools/build_batch02_example.py`.
  Copy one, change the card dict and the id range and output name.
- Be careful with numbers like "10/15" (a single token for the checker): keep such forms exactly as written. Keep "17-18" style forms too.
- When a card gives a long list of examples inside one bullet (for example Best Practices), splitting it into nested bullets is allowed and reads better.
- Build method that worked: convert a batch, then write a Python dict {card_id: (status, {block: new_text})} and a small script that replaces
  only introduction, examples and conclusion blocks in the converted Markdown (so quotes, data and metadata can never be touched by accident).
  Then run the verifier and fix warnings. `verify_protected.py` also warns on informal shorthand left behind (imp, b/w, obj, ppl, u/s, govt...).

## 12. Batch log
| Batch | Cards | File | Result |
|---|---|---|---|
| 01 | Polity 157 to 176 (20 cards) | `polished/GS2_POLITY_batch01_cards157-176.md` | 0 errors; data/detail blocks of 0167, 0168, 0169 re-polished after the shorthand decision; SC/VP kept as abbreviations after the abbreviation decision; see `review_queue.md` |
| 02 | Polity 177 to 196 (20 cards) | `polished/GS2_POLITY_batch02_cards177-196.md` | 0 errors; only accepted warnings; see `review_queue.md` |
| 03 | Polity 197 to 216 | `polished/GS2_POLITY_batch03_cards197-216.md` | 0 errors; 0215 untouched; see `review_queue.md` |
| 04 | Polity 217-220 + Governance 221-236 | `polished/GS2_POLITY-GOVERNANCE_batch04_cards217-236.md` | 0 errors; 0235 needs_review (cross-reference) |
| 05 | Governance 237 to 256 | `polished/GS2_GOVERNANCE_batch05_cards237-256.md` | 0 errors; 0245, 0252, 0255 needs_review |
| 06 | Governance 257-272 + Social Justice 273-276 | `polished/GS2_GOVERNANCE-SOCIALJUSTICE_batch06_cards257-276.md` | 0 errors; 0264, 0266 needs_review |
| 07 | Social Justice 277-295 + IR 296 | `polished/GS2_SOCIALJUSTICE-IR_batch07_cards277-296.md` | 0 errors; 0279, 0280, 0284, 0292, 0296 needs_review |
| 08 | IR 297 to 316 | `polished/GS2_IR_batch08_cards297-316.md` | 0 errors; templates 0297, 0307, 0314 needs_review (0319, 0318 in batch 09) |
| 09 | IR 317-328 + Economy 329-336 | `polished/GS2-IR_GS3-ECONOMY_batch09_cards317-336.md` | 0 errors; 0318, 0319 needs_review; 0322, 0324 untouched |
| 10 | Economy 337 to 356 | `polished/GS3_ECONOMY_batch10_cards337-356.md` | 0 errors; about 25 warnings (light rewrite, see queue note) |
| 11 | Economy 357-359 + Agriculture 360-376 | `polished/GS3_ECONOMY-AGRICULTURE_batch11_cards357-376.md` | 0 errors; about 20 accepted warnings (one-line examples have little room to reword) |
| 12 | Agriculture 377-383 + Sci and Tech 384-396 | `polished/GS3_AGRICULTURE-SCITECH_batch12_cards377-396.md` | 0 errors; 0385, 0386 needs_review |
| 13 | Sci and Tech 397 to 416 | `polished/GS3_SCITECH_batch13_cards397-416.md` | 0 errors; 0402, 0404, 0405, 0414, 0415 needs_review |
| 14 | Sci and Tech 417-427 + Environment 428-436 | `polished/GS3_SCITECH-ENVI_batch14_cards417-436.md` | 0 errors; 8 accepted warnings; 0424, 0426, 0427 needs_review; corrected after review (see queue) |
| 15 | Environment 437 to 456 | `polished/GS3_ENVI_batch15_cards437-456.md` | 0 errors; 17 accepted warnings (term-list cards 0443, 0448, 0449, 0450 cannot be reworded more); see `review_queue.md` |
| 16 | Environment 457 to 476 | `polished/GS3_ENVI_batch16_cards457-476.md` | 0 errors; 13 accepted warnings (term-list cards 0459, 0472; number-dense lines 0461, 0469, 0475); 0460, 0462 needs_review; see `review_queue.md` |
| 17 | Environment 477-479 + Disaster Mgmt 480-496 | `polished/GS3_ENVI-DISA_batch17_cards477-496.md` | 0 errors; 21 accepted warnings (mnemonic/quote cards 0482, term lists); 0483 needs_review; pushed to GitHub as `batch-17`; see `review_queue.md` |
| 18 | Disaster Mgmt 497-504 + Internal Security 505-516 | `polished/GS3_DISA-INTE_batch18_cards497-516.md` | 0 errors; 5 accepted warnings (definition + fixed-list cards 0497, 0498, 0499, 0508, 0512); 0509 needs_review (template conclusion); pushed to GitHub as `batch-18`; see `review_queue.md` |
| 19 | Internal Security 517-536 | `polished/GS3_INTE_batch19_cards517-536.md` | 0 errors; 11 accepted warnings (SAMADHAN mnemonic 0528, statute lists 0535, protected MoHA quote); 0533, 0536 needs_review (blanks); 4 untouched quote/template cards; pushed to GitHub as `batch-19`; see `review_queue.md` |
| 20 | Internal Security 537-543 + Ethics 544-556 | `polished/GS3_INTE-GS4_ETHI_batch20_cards537-556.md` | 0 errors; 17 accepted warnings (concept/detail cards 0544-0555; 'synergy' term of art); 0543, 0545, 0556 untouched; pushed to GitHub as `batch-20`; see `review_queue.md` |
| 21 | Ethics 557-576 | `polished/GS4_ETHI_batch21_cards557-576.md` | 0 errors; 16 accepted warnings (concept cards 0.70-0.79; 0572 5-item list line reads long); 0561 untouched (quoted blocks); pushed to GitHub as `batch-21`; see `review_queue.md` |
| 22 | Ethics 577-596 | `polished/GS4_ETHI_batch22_cards577-596.md` | 0 errors; 15 accepted warnings (0.71-0.79 short example lines); 5 untouched quote/term-list cards; broken bullets repaired (0590, 0593); pushed to GitHub as `batch-22`; see `review_queue.md` |
| 23 | Ethics 597-616 | `polished/GS4_ETHI_batch23_cards597-616.md` | 0 errors; 14 accepted warnings (0.71-0.79; 0615 8-item list line; 'cornerstone' term of art); 5 untouched (quoted lines 0603/0605, quotes 0607/0610/0614); pushed to GitHub as `batch-23`; see `review_queue.md` |
| 24 | Ethics 617-636 | `polished/GS4_ETHI_batch24_cards617-636.md` | 0 errors; 17 accepted warnings (0.71-0.79; 0627 5-item list line); 3 untouched term-list cards (0630, 0633); broken bullets repaired (0620, 0621, 0636); pushed to GitHub as `batch-24`; see `review_queue.md` |
| 25 | Ethics 637-656 | `polished/GS4_ETHI_batch25_cards637-656.md` | 0 errors; 20 accepted warnings (incl. term lists 0648/0651/0653/0655 at 0.92-0.96); 4 untouched (0638, 0647, 0650, 0656); fragments re-joined (0641, 0644); pushed to GitHub as `batch-25`; see `review_queue.md` |
| 26 | Ethics 657-676 (Moral Thinkers) | `polished/GS4_ETHI_batch26_cards657-676.md` | 0 errors; 5 accepted warnings (0.71-0.79); 9 untouched quote-only cards; broken bold repaired (0671, 0673); pushed to GitHub as `batch-26`; see `review_queue.md` |
| 27 | Ethics 677-696 (Moral Thinkers/Leaders) | `polished/GS4_ETHI_batch27_cards677-696.md` | 0 errors; 8 accepted warnings (0.71-0.78; 0688 markup-fix at 1.00); 8 untouched quote-only cards; pushed to GitHub as `batch-27`; see `review_queue.md` |
| 28 | Ethics 697-716 (quote collection) | `polished/GS4_ETHI_batch28_cards697-716.md` | 0 errors; 2 accepted warnings (0.71-0.72); 13 untouched quote-only cards; pushed to GitHub as `batch-28`; see `review_queue.md` |
| 29 | Ethics 717-736 (Probity) | `polished/GS4_ETHI_batch29_cards717-736.md` | 0 errors; 21 warnings, all accepted (0735 name card 0.86; rest 0.70-0.78); broken bolds repaired (0717, 0725, 0733, 0734); pushed to GitHub as `batch-29`; see `review_queue.md` |
| 30 | Ethics 737-756 (Probity II) | `polished/GS4_ETHI_batch30_cards737-756.md` | 0 errors; 21 warnings, all accepted ('ethos' term, 0752 5-item inline list); 3 untouched (0740, 0743, 0744); pushed to GitHub as `batch-30`; see `review_queue.md` |
| 31 | Ethics 757-776 (Accountability/Corporate/IR) | `polished/GS4_ETHI_batch31_cards757-776.md` | 0 errors; 12 warnings, all accepted (0763 framework card 0.85); 6 untouched; Acccountability typo fixed; pushed to GitHub as `batch-31`; see `review_queue.md` |
| 32 | Ethics 777-789 (final, 13 cards) | `polished/GS4_ETHI_batch32_cards777-789.md` | 0 errors; 5 accepted warnings (0781 fixed comparison list 0.88); 5 untouched; 0778 label swap flagged; pushed to GitHub as `batch-32`; see `review_queue.md` |
| 33 | GS-1 Art & Culture 1-20 | `polished/GS1_HIST_batch33_cards0001-0020.md` | 0 errors; 39 warnings, all accepted (name-dense lists 0002/0009/0010/0012, fixed UNESCO list 0018); 3 needs_review (0011 same-as-above, 0013 template, 0014 truncated); 2 numeric errors caught and fixed (0009 '1 vimana', 0014 '2 centres'); pushed to GitHub as `batch-33`; see `review_queue.md` |
| 34 | GS-1 Art & Culture 21-40 | `polished/GS1_HIST_batch34_cards0021-0040.md` | 0 errors; 44 warnings, all accepted (state-code expansions, name-dense inventories); 3 needs_review (0023, 0030, 0035 truncated); pushed to GitHub as `batch-34`; see `review_queue.md` |
| 35 | GS-1 Modern History 41-60 | `polished/GS1_HIST_batch35_cards0041-0060.md` | 0 errors; 27 warnings, all accepted (epigram list 0044, framework 0056); 4 needs_review (0041-0043, 0048 truncated); 5 untouched quote-only; Gandhi quote typo 'noy' flagged; pushed to GitHub as `batch-35`; see `review_queue.md` |
| 36 | GS-1 61-80 (Colonial Rule, 1857, Post-Independence) | `polished/GS1_HIST_batch36_cards0061-0080.md` | 0 errors; 38 warnings, all accepted (prose 0.70-0.82); 2 untouched (0070, 0075); 1 needs_review (0077 truncated); typos fixed (lyer/Iyer, school's); pushed to GitHub as `batch-36`; see `review_queue.md` |
| 37 | GS-1 81-100 (World History + Society) | `polished/GS1_HIST-SOCI_batch37_cards0081-0100.md` | 0 errors; 37 warnings, all accepted; 7 needs_review (truncated + stray AI-fragments flagged); 2 numeric/list errors caught and fixed (0089 '29-30,46', 0097 item count); pushed to GitHub as `batch-37`; see `review_queue.md` |
| 38 | GS-1 101-120 (Regionalism/Urbanisation + Energy Geography) | `polished/GS1_SOCI-GEOG_batch38_cards0101-0120.md` | 0 errors; 44 warnings, all accepted; 7 needs_review (0104, 0113, 0115-0119 truncated/duplicates); gas-share inconsistency 3.9% vs 6% flagged; pushed to GitHub as `batch-38`; see `review_queue.md` |
| 39 | GS-1 121-140 (Forests/Minerals + Geophysical Phenomena) | `polished/GS1_GEOG_batch39_cards0121-0140.md` | 0 errors; 50 warnings, all accepted; 6 needs_review (0126, 0129, 0130, 0132, 0138, 0139); 0125 placeholder-quote 'Source Text' flagged; pushed to GitHub as `batch-39`; see `review_queue.md` |
| 40 | GS-1 141-156 (Jet Streams, Earth Theories, Monsoon, Oceanography) — FINAL | `polished/GS1_GEOG_batch40_cards0141-0156.md` | 0 errors; 37 warnings, all accepted; 4 needs_review (0144, 0147, 0148 same_as_above; 0156 truncated); FULL MERGE `MERGED_full_1-789.md` verified 0 errors; pushed to GitHub as `batch-40`; see `review_queue.md` |

## 13. How to resume (for the next agent)
1. Read this file fully, then `review_queue.md`, then look at the last batch file as the style reference.
2. Ask the user for the original JSON if it is not attached; set `SRC` in `convert.py`.
3. PROJECT COMPLETE. The full merged file is `polished/MERGED_full_1-789.md` (0 errors). No further batches. User review of review_queue.md flags is the next step: compute the subject's index range, convert 20 cards, write the polish dict, build, verify, deliver, update sections 8, 12 and `review_queue.md`, then push to GitHub with a commit named `batch-40` (plus the full-merge file) (remote already has the token in the clone at /home/z/ghrepo — refresh files from /home/z/my-project first).
4. Always end your reply with the three files the user must keep: `PLAN.md`, the latest batch `.md`, and `review_queue.md` (plus `convert.py` and `verify_protected.py`).

## 14. Lessons from batches 03 to 07 (read these too)
- **Helper:** `tools/bb.py` has `build(raw_path, P, out_path)`. Each batch script defines `P` with `card(id, status, introduction=..., examples=..., conclusion=..., data=..., detail=...)`.
  Only the blocks you pass are replaced. See `tools/build_batch07_example.py`. Card IDs use the subject's first four letters (POLI, GOVE, SOCI, INTE);
  batches that cross a subject boundary need a prefix rule (see `build_batch04_example.py`).
- **Workflow per batch (about 20 cards):** `python3 convert.py raw.md $(seq A B)`, read the raw cards, write the dict, build, run the verifier,
  rewrite lines flagged as "lightly rewritten" or "long sentence", re-run, then update the plan and queue.
- **Similarity warnings:** Aim below 0.70. Short fact lines, names and quoted phrases cannot be changed much; accept those. Fix every warning above about 0.80 and every long sentence.
  Slogans or quoted phrases that appear in conclusion blocks (for example "Sahi Poshan, Desh Roshan") are quotes and stay untouched (similarity 1.00 is fine there).
- **Duplicate cards are common** (same topic from different sources). Polish them with different wording so they do not look copied from each other.
- **Do NOT fix wrong facts silently.** Keep them as written and list them in `review_queue.md` (wrong years, mismatched ranks, doubtful quotes, generic examples).
- **Placeholder, template and cross-reference cards:** leave the placeholder text alone, polish only the real parts, set `status: needs_review`, and list them in the queue.
- **Numbers:** keep forms like "6/7", "102/123", "120/100", "36K", "17-18", "10/15" exactly as written (the verifier compares number tokens).
- **Do not turn a quote into a paraphrase.** Text inside quotation marks in intro, conclusion, examples or data blocks is treated as protected even if it is not in a `:::quote` block.
- **Remaining subjects:** see the tracker in section 8 for the exact, computed card ranges. Do not guess ranges; recompute them with a short script if unsure.

## 15. Lessons from batches 08 to 10
- IDs use the paper and the first four letters of the subject, for example `GS2-INTE-0297`, `GS3-INDI-0329` (Indian Economy), `GS3-AGRI-`, `GS3-SCIE-`, `GS3-ENVI-`, `GS3-DISA-`, `GS3-INTE-` (Internal Security; note the same four letters as IR but a different paper), `GS4-ETHI-`.
  The IDs come from `convert.py`; check one converted card to see the exact prefix before writing the batch dict.
- **First drafts are usually too light.** In batch 08 the first draft had 32 warnings. Aim to restructure sentences (change the opening, split or merge, swap order of clauses) and not only swap words.
  Economy cards (batch 10) are packed with bold catchphrases and one-line examples; keep the bold catchphrases but rebuild the sentence around them.
- **Never add a number or fact.** In batch 10 the checker caught an added number ("Only 2 countries..."). The verifier compares number tokens; trust it.
- Misplaced bold markers in the original (for example "Inclusive growth** is driven by...") should be fixed as formatting while rewriting.
- Quotes that sit inside intro/conclusion/data blocks (for example slogans) stay exactly as written.
- Template cards with blanks (`____`): do not invent the missing words. Polish the real parts and mark `needs_review`.
- Long turns can be cut off by the chat. Work in batches of 20, and update `PLAN.md` and `review_queue.md` after each batch so a new agent can resume at any time.

## 16. Rules added after the user's review of batch 14 (read before every batch)
These came from checking the second AI's batch 14. Follow them in all remaining batches.
1. **Do not add words that carry new meaning.** Examples to avoid: "announced", "recently", "officially", "only", "now", "also" when the original does not say it. Only restructure and simplify.
2. **Keep units and nouns exactly.** If the original says "4 mn disaster-induced displacements", do not write "4 mn people displaced" (events are not people). If it says "Field of research", do not turn it into "science of matter".
3. **Keep section labels as written** in the original ("Steps", "Applications", "Issues", "Definition"). Do not rename them (for example "Steps" must not become "Steps announced").
4. **Never drop or merge list items** in any block. The verifier checks data/detail lists automatically; for intro, conclusion and examples, count the items yourself.
5. Expanded shorthand (Govt, AP, GJ, CC) is fine, but list each expansion you were unsure about in `review_queue.md`.
6. Keep replies short (long replies get cut off). Save files and update the docs after every batch.
7. A reviewer (the user, or a review agent) will check each delivered batch with `verify_protected.py` and a read-through; expect corrections and apply them quickly.

### Corrections still pending for batch 14 (apply first, then re-run the verifier)
- Card 435, data block: change "**4 mn** people were displaced by disasters" back to keep the unit: "**4 mn** disaster-induced displacements".
- Card 431, introduction: change the label "Steps announced" back to "Steps".
- Card 420, introduction: change "The science of matter at a very small scale — atoms and molecules" to keep the noun: "A field of research at the scale of atoms and molecules, in the nanometre range (1–100 nm)".
- After fixing, save the file and mention the fix in `review_queue.md` ("batch 14 corrected after review").

## 17. Final merge (when everything is done, or at any checkpoint)
Run `python3 tools/merge_batches.py polished/MERGED_cards<first>-<last>.md` from the folder containing `polished/`. The merged file on disk is `polished/MERGED_full_1-789.md` — the complete, final ebook source (all 789 cards, 0 errors). Delete older merged files so the user does not open an outdated one.

## 20. CORRECTIONS PHASE (Edition 2 hardening, October 2026) — COMPLETE
All 789 cards went through a user-directed corrections pass (C0-C6). Full audit trail: `corrections_log.md`.
Approved-changes allowlist: `approved_corrections.py` (verify_protected.py consults it; NOTE lines = approved, everything else still hard-checked).
- C0 root cause: source JSON = PDFs + AI enrichment; broken cards came from that layer. 4+3 source PDFs in `upload/`, extracted text in `pdf_text/`.
- C1 removed 8 stray AI fragments; C2 removed all "Source Text" labels (quotes kept).
- C3 applied 60+ spelling fixes (logged old->new).
- C4 applied 18 web-verified fact corrections with inline [Source: ...] (CPI 2025 91/182, NJAC 2015, Santhanam 1964, ADR 2019, UNICEF 10-19, dowry/marital-rape labels corrected in 0778, etc.).
- C5 inlined 11 cross-references + restored/complete 9 truncated cards from the original PDFs.
- C6 duplicates: measured; kept (detailed card + revision card design; 0300/0306 already re-worded).
- Status: 789 cards, 0 errors, 771 accepted warnings.
- OUTSTANDING: GitHub push pending (PAT re-send needed); ~150 quote attributions still flagged in review_queue.md (user decision pending; suggestions available on request).
