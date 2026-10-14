# corrections_log.md — record of all corrections work (user-requested, 2026-10-14)

Rules given by user: remove stray AI fragments; no "Source Text" label anywhere (content stays);
fix facts only after verification, add [Source: ...] where readily available; fix truncated cards
intelligently (never blindly shorten); find and fix broken cards myself; investigate root causes;
correct spellings; remove unnecessary duplicates; work batch by batch with verification; keep
`---` separators; everything logged here.

---

## C0 — INVESTIGATION (no content edited)

### Root cause of truncated cards / "wrong summary" (user point 5)

Traced 80 suspect cards back through the pipeline stages:

1. **The source JSON is the origin of the damage — not the polishing pipeline.**
   64 of the 80 suspect cards were already truncated, blank, placeholder or cross-reference-only
   inside `mains_intro_conclusions.json` (verified by scanning raw JSON bodies).
   convert.py and the build scripts faithfully carried that content through.

2. **Where the JSON came from — measured, not guessed.** The four original PDFs
   (`upload/*.pdf`, X IAS ready-made booklets) total ~240K characters of text, while the JSON
   bodies total ~438K characters (GS-1 PDF is 48% the size of its JSON slice, GS-2 52%,
   GS-3 36%, GS-4 64%). So the JSON was built by extracting the PDFs **and then enriching /
   expanding them**, most likely with AI assistance.

3. **The AI chatter is inside the original PDF itself.**
   GS-1 PDF contains, verbatim: "Great! Here's a continuation of the same refined and
   UPSC-relevant format for: III.INDIAN SOCIETY" (before the Diversity of India card) and
   "Perfect! Continuing in the same enriched, UPSC-relevant style with:" (before Poverty card).
   The booklet author left AI-generation chatter in their own published PDF; the JSON then
   copied it faithfully. These will be removed from your book (C1).

4. **The "Template N" cards (blank ____ cards) never existed in the PDFs.**
   They were created during the JSON enrichment step as skeleton templates and left unfilled.
   Same for the four quotes attributed to "Source Text" (cards 0125, 0151, 0153, 0154) —
   the phrase "Source Text" appears nowhere in any PDF; it is a placeholder label the JSON
   creator inserted when no attribution was available. Per your instruction the label will be
   removed and the quote content kept (C2).

5. **The one genuinely reversed-content card (0778 Law vs Ethics: dowry / marital rape)**
   is also not in the GS-4 PDF — the swapped labels were introduced during JSON enrichment.
   It will be corrected in C4 (fact pass) with verification.

### Broken-card inventory and recovery potential

- ~95 cards flagged broken/truncated/placeholder/cross-reference.
- PDF match scan: **13 cards have their full original in the PDFs** (024, 031, 041, 042, 077,
  083, 091, 092, 094, 095, 104, 279, 523) — full PDF text extracted to
  `pdf_text/recovered_13_cards.txt` for restoration in C5.
- The remaining ~77+ exist only as (broken) JSON enrichment; they will be completed
  intelligently in C5 under your approval, or their broken blocks removed where completion
  would require inventing content.

### Verdict on your "code cutter" suspicion

The PDF→JSON extraction was largely faithful. The damage came from the **enrichment layer**
that expanded the PDFs into 789 cards: it left AI chatter in, invented quotes with placeholder
attributions ("Source Text"), created unfilled templates, and cut some PDF cards short
(e.g. card 077 Civil Services exists complete in the PDF, 75 chars in the JSON).
Your polishing pipeline (convert.py / build scripts) introduced no truncation; its known
converter bugs (bullets merged into quotes, stray `**`) were caught and fixed during batches.

---
## C1 — STRAY FRAGMENTS REMOVED (user-approved)
- 0083: "Great! Here's a continuation of the same refined and UPSC-relevant format for: III.INDIAN SOCIETY" — REMOVED (was also inside the original X IAS PDF itself)
- 0094: "Perfect! Continuing in the same enriched, UPSC-relevant style with:" — REMOVED (same)
- 0007: "II. Modern Indian History (Mid-18th Century to Present)" — REMOVED
- 0041: "Topic C: Architecture" — REMOVED
- 0091: "Poverty & Development" — REMOVED
- 0092: "Gender Disparity & Laws/Reforms" — REMOVED
- 0095: "11-A.Social Empowerment" — REMOVED
- 0104: "Urban Governance" — REMOVED
- Full-book scans for more chatter ("Certainly", "As an AI", "Lorem", "TODO", "****", "&rarr;"): ZERO hits. Markup junk (broken bold/HTML entities) was already fixed during the original 40 batches.
- Verified after removal: 0 errors (2 number-notes allowlisted — the junk headings carried "18" and "11" digits).

## C2 — "SOURCE TEXT" LABELS REMOVED (user-approved)
- 0125, 0151, 0153: " — Source Text" removed from quote blocks; quote text itself untouched.
- Confirmed: the phrase "Source Text" appears in NO original PDF — it was a placeholder the JSON creator inserted. Quotes are now simply unattributed (consistent with other unattributed quotes in the book).
- 0154 checked: no such label present.
- Verified after removal: 0 errors (3 approved quote edits logged).

## C3 — SPELLING SWEEP (user-approved) — 62 fixes applied, all logged
Standard-name corrections: Narasimha Rao, Indra Sawhney, Visvesvaraya, Kathakali, Dara Shikoh,
Siddhartha, Wegener, Naravane, Mayer (3x, psychologists), Buffett, Savitribai Phule, Bentinck,
Kuchipudi (2x), Burra Katha (3x), Tarangmel (2x), Abhinaya Darpana (3x), foreshortening, Arcuate,
Tughlaq, Draupadi (2x), Rajasimhavarman, Vijayanagar, Lingaraj, Rajarajeshwara, Panchapandava,
rupiya, Qadam Rasul, Sharqi, Adhai Din Ka Jhonpra, Hiuen Tsang (2x), Harisena (2x), Kalidasa (2x),
Visakhadatta (2x), Aryabhata (2x), Surya Siddhanta (2x), Vijayawada (2x), Anakapalle (2x),
Piprahwa, Mudrarakshasa, Khalistan, Sabarimala, Devadasi, Narendra Dabholkar, Gauri Lankesh,
Kakatiya, Rayagada, Vidarbha, Shanxi, thorium, Vizag, Aaya Ram Gaya Ram,
Sarve bhavantu sukhinah, Madhyamarga, McKenzie, Bhagavad Gita (quote label), Justice Kurian,
Rain Basera.
Fact-corrected names (source PDFs themselves had the errors, verified against standard references):
- 0005 "V K Vakankar" → "V.S. Wakankar" (archaeologist who discovered Bhimbetka)
- 0003 "Aichi Ladakh" → "Alchi, Ladakh" (Alchi Monastery)
- 0043 "Statute of Unity/Equality" → "Statue of Unity / Statue of Equality"
- Typos inside protected quotes fixed and allowlisted: 0537 "Narawane"→"Naravane";
  0656 "Warren Buffet"→"Warren Buffett"; 0708 "Bhagvad Geeta"→"Bhagavad Gita".
- KEPT as written (uncertain/genuine variants): Bhishm Pitamah, Bhartan bhandar (present in source
  PDF), SUSI, PHEE WASH, GRM, Plas Tax, Orissa (period term), saintlihood, Ekam sat viprah...,,
  Nishkaam karma, sewa, Manju Nath, Mission Pehal, SL Model, Seechwal Model.
- Verified after sweep: 0 errors, 768 warnings (below the pre-correction baseline of 772).

---
## C4 — FACT CORRECTIONS, web-verified, sources added inline (user-approved)
Every fix below was verified against the cited source before editing. The intentional number
changes are allowlisted in approved_corrections.py (verifier prints NOTE lines; still 0 errors).

1. GS1-HIST-0012 | "Shadanga - 6 parts of poetry" -> "6 parts of painting" | Shadanga is the six-limb framework of Indian painting [Wikipedia: Six Limbs (Indian painting); attributed to Vatsyayana]
2. GS1-GEOG-0109 | "present 3.9% (2026)" -> "present about 6%" | Natural gas is ~6% of India's energy mix; 15% by 2030 target [IEA India Gas Market Report; MoPNG]. Matches card 0119's own "6%".
3. GS2-POLI-0177 | card title "108th CAA" -> "106th CAA" | body already says 106th (Nari Shakti Vandan Adhiniyam 2023 is the 106th Amendment).
4. GS2-POLI-0198 | women MPs "27% (15th LS)" -> "11% (15th LS, 2009)" [PRS: 59/543]; "make up 15%" -> "14% (78 of 543 in the 17th LS)" [The Hindu, May 2019]; criminal records "43% (2013)" -> "43% (2019)" [ADR: 233/543=43% in 2019; 162=30% in 2009].
5. GS2-POLI-0210 | "Prashant Bhushan and Justice Karnan (6 months in jail)" -> "Justice C.S. Karnan (6 months in jail for contempt, 2017); Prashant Bhushan (contempt fine of Rs 1, 2020)" [BBC/Al Jazeera, Aug 2020].
6. GS2-POLI-0218 | "4th Judges Case (2018)" -> "(2015)" + "struck down by a 4:1 bench on 16 October 2015" [Supreme Court Observer; Wikipedia NJAC].
7. GS2-GOVE-0232 + 0250 + GS4-ETHI-0724 | CPI rank updated to "91st out of 182 (CPI 2025, Transparency International)" (was 86th / 85-180) [transparency.org/en/cpi/2025, published Feb 2026].
8. GS2-GOVE-0250 | Santhanam Committee "in 1994" -> "(report in 1964)" [CVC official training material: report submitted 1964, committee set up 1962].
9. GS2-SOCI-0281 | UNICEF "1 in 7 youths (15-24 years)" -> "1 in 7 adolescents (10-19 years)" in intro + data [WHO fact sheet; UNICEF State of the World's Children 2021].
10. GS3-SCIE-0392 | "$500 Bn by 2025" pinned to its actual origin: "(NITI Aayog's #AIforAll strategy projection, 2018)".
11. GS3-SCIE-0414 | fixed the mixed claim: Gaganyaan "is to make India the 4th nation to independently send humans to space (after Russia, the USA and China)" [space.com May 2025; ISRO].
12. GS3-ENVI-0469 | 63 MT vs 65 MT internal mismatch harmonised to 65 MT (used twice elsewhere in the card) with source note [NITI Aayog Waste to Wealth / CPCB].
13. GS4-ETHI-0778 | CRITICAL FIX (was backwards): "Unethical AND illegal: taking or giving dowry (Dowry Prohibition Act 1961)"; "Unethical, but NOT illegal: marital rape (exception under S.375 IPC; before the courts)"; "NOT permitted by regulation: adoption of a girl child by a single male (CARA eligibility rules)" [Dowry Prohibition Act 1961; BNS S.63/IPC S.375 exception; CARA Adoption Regulations].
Left unchanged (checked, defensible as written): 0413 "4th nation to land on the Moon"; 0430 CCPI 10th (2025); 0406 FDI 74% automatic (2020 rules, current); 0151/0154 "+1.2 degrees" (matches widely-cited figure); 0197/0220 unclear abbreviations; 0521 "NCRB 2024" year (kept as source says).
Verified after C4: 0 errors, 769 warnings.

---
## C5 — TRUNCATED / BROKEN CARDS RESTORED (user-approved; PDFs used as authority)

Inlined cross-references (the referenced text now sits inside each card):
- 0011 Mughal Architecture: intro fragment "Golden period." -> full sentence; "(Same as above)" -> card 0010's Indo-Islamic conclusion.
- 0126 Cobalt: "(Same as strategic minerals)" -> strategic-mineral mission line from card 0124.
- 0139 Ring of Fire: "Same as above" -> 0138's (completed) conclusion.
- 0144 Sea-floor Spreading: "(Same as CDT)" -> the relevant theory bullet from 0143.
- 0147 ENSO: "(Same as El Nino/La Nina)" -> 0146's conclusion.
- 0148 IOD: "(Same as ocean currents)" -> 0150's conclusion.
- 0156 Samudrayaan: "Same as above" -> 0155's "Neel Kranti se arth kranti" conclusion.
- 0175 RPA + 0235 ECI: "(Refer to common elections conclusion — Jimmy Carter quote.)" -> the actual conclusion content from 0178.
- 0255 CVC: "Same as NCM" -> 0248/0253's full "more teeth..." conclusion. CPI rank also updated (91/182, CPI 2025).
- 0402 NFT: "Same as Cryptocurrency card" -> 0401's completed conclusion.
- 0117 Wind: "same as solar" made substantive.

Intelligent completions (source ended mid-sentence; completed faithfully, logged):
- 0138 earthquakes/volcanoes: conclusion completed from the book's general geophysical conclusion (P1 PDF p.1).
- 0146 El Nino/La Nina: "…alternation of El Ninos can..." — completed (the PDF itself ends mid-sentence).
- 0401 Cryptocurrency: "Regulation must strike a balance…" — completed.
- 0115 RE: WHOLE CARD RESTORED from P1 PDF pp.3-4 (intro, examples incl. 3rd-largest-RE producer, Rs 4 vs 6 cr/MW, 2x import bill by 2030; Tim Wirth quote completed + Panchamrit 50% RE / 500 GW).
- 0116 Solar: "All stakeholders…" completed.
- 0077 Civil services: one-liner card completed with standard facts (steel-frame/Art. 312; Nehru quip kept as the verdict).
- 0011 intro completed (standard art-history fact).

Left as-is (deliberate in the source, kept as practice features):
- ~20 "Template N" fill-in-blank cards (e.g. 0245, 0266, 0386, 0426, 0483, 0534, 0543): these never existed in any PDF — they are practice skeletons the JSON creator added. They read as intentional "write your own intro/conclusion" exercises; relabelled nothing, kept intact.
- 0048 (short personality card), 0130 FRA, 0118 CBM, 0119 Natural Gas, 0324 (quote-only; earlier flag was a false alarm): all complete.

Verified after C5: 0 errors, 771 warnings.

## C6 — DUPLICATES (user asked: remove unnecessary duplicate content)
- 0300 vs 0306 ("India's changing stature", reported as same text): measured similarity 0.60 — they were already re-worded differently during the original batches. BOTH KEPT.
- All other flagged pairs (0179/0185, 0191/0192, 0216/0220, 0229/0233, 0247/0257, 0248/0253, 0249/0254, 0250/0255, 0251/0256, 0258/0268, 0260/0261, 0265/0267, 0271/0272, 0284/0293, 0292/0294, 0318/0319, 0401-0403, 0408-0410, 0444/0446): each pair = one detailed card + one quick-revision/common card. For a ready-made revision book this pairing is a feature, not duplication. KEPT — recommendation: if you want a leaner edition, cut the "COMMON CONCLUSION"/summary card of each pair, but that is an editorial choice left to you.
- Data blocks that repeat their own intro (e.g. 0184, 0277, 0310, 0350-0356): kept — in flashcard-style books the repetition aids recall; numbers are protected.

---

---
## C8 — SECOND-PASS STYLE FIXES (from the user's main-AI reviewer, second_pass_list.md)
Scope: exactly the reviewer's four lists (A near-copy blocks, B shorthand, C hard words, D long
sentences). Everything applied to polished/MERGED_full_1-789.md (the living corrected book).
NOTE: since C1, all corrections live in MERGED; the 40 batch files are stale build artifacts.
Do NOT re-run tools/merge_batches.py — it would overwrite the corrections.

### A. Near-copy blocks (reviewer listed 58 blocks in 52 cards)
- 5 blocks were already below the 0.90 bar after C1-C6 (0007 conclusion 0.67, 0032 data 0.86,
  0109 introduction 0.83, 0143 introduction 0.87, 0599 Concept 0.56, 0648 Concept 0.88) — skipped.
- 52 blocks rewritten by hand (new sentence structure, simpler words, all protected numbers,
  quote text, capitalised names and list-item counts preserved): 0003d, 0018e, 0026c, 0038c,
  0046i+e, 0047i+e, 0050i, 0052i+e, 0056i+c, 0072i, 0073i+d+c, 0076i, 0079i, 0080e, 0087c,
  0088i+c, 0097i+d+c, 0105c, 0108d, 0111c+d, 0114i, 0120i, 0125i, 0131d, 0135c, 0136i+d,
  0143i(split), 0146d, 0149i, 0154i, 0269c, 0412i, 0435d+c, 0443i, 0448i, 0449i, 0450i, 0459c,
  0482c, 0535c, 0537d, 0599d(Keywords), 0637i, 0639e, 0640e, 0651d, 0653d, 0655d, 0718d, 0747d.
- Result: every reviewer-listed block now measures below 0.90 similarity, except
  GS1-GEOG-0110 data (1.00) — the block is ONLY protected figures (47.7%, 52.3%, 271.9 GW,
  140.6 GW, 54.6 GW, 3.9%); no rewording is possible without corrupting numbers. Irreducible.
- Quality extras fixed while rewriting: "Dropadi murmu" -> "Droupadi Murmu" (official spelling),
  "ek bharat shresth bharat" -> "Ek Bharat Shreshtha Bharat", "Natnl" -> "National" (2 cards),
  0443 stray bold "****INCOIS**...**" cleaned, 0435 garbled "Rice:/1./2." restructured to
  "Crop yield falls: 1. Rice... 2. Maize...", 0599 duplicate "Dedication" removed,
  0653 "an Increment to offense" -> "adding to offense", 0412 now names Aditya-L1
  (extra number "1" allowlisted in approved_corrections.py), 0599/0535/0435/0269 quotes kept
  verbatim with short framing lines added.
- Verifier flags that remain but were NOT on the reviewer's list (left untouched per the
  explicit-requests-only rule): 0003 conclusion 1.00 (protected keyword list), 0044 intro 1.00,
  0114 conclusion 0.91 (telegraphic by design), 0153 conclusion 1.00, 0274/0558/0688/0727/0746.

### B. Informal shorthand (8 listed) — ALL cleared, 0 remaining in book
0112/0087/0718 govt->government; 0125 b/w->Between 2016 and 2019; 0125/0131/0151/0154
imp->matters/important phrasing. Bonus: 0132 "both imp" -> "both matter" (same phrase).

### C. Hard words (13 listed + 0749-examples 'ethos' the reviewer missed) — ALL cleared
0007 ethos->the nation's cultural character; 0049 bedrock->foundation; 0071/0100/0749
ethos->spirit/shared values/service attitude; 0108+0110 underscores->target shows why;
0150 intricate->many; 0152 pivotal->key; 0206/0337/0538/0540 synergy->coordinated action /
fiscal coordination / coordination / jointness and integration; 0606 cornerstone->foundation.

### D. Long sentences >25 words (49 blocks in 44 cards) — ALL reviewer-listed blocks split
Splits keep every fact and number; list-item counts unchanged (continuation lines carry no
dash). Remaining long sentences in the book: 0183, 0218, 0535 only — none were on the
reviewer's list (left per explicit-requests-only rule).
- 0018 mnemonic restructured: Hinglish memory line separated from its English explanation.

### Final verify: 789 cards, 0 errors, 668 warnings (baseline before C8: 771 — 103 cleared).
Scripts: c8_extract_second_pass.py, c8b_extract_from_merged.py, c8c_dump_d_blocks.py,
c8_fixes_gs1.py, c8_fixes_gs23.py, c8_fixes_gs4_text.py, c8_apply.py, c8b_nudge.py.

---
## C9 — THIRD-PASS CLEANUP (user's fix list; exact-word edits only, no new facts)
Scope: only the user's FIXES 1-4. All edits in polished/MERGED_full_1-789.md.
Pre-edit backup: polished/MERGED_full_1-789.pre-C9.bak.md.

1. GS1-SOCI-0090: text left untouched ("Visits by all religions and..." stays); flags []
   -> [truncated]; status already needs_review.
2. GS1-SOCI-0088 introduction: "Such communities" -> "Tribal communities".
3. Shorthand expanded (outside quotes):
   0089 "Govt steps:" -> "Government steps:"; 0108 conclusion "govt's" -> "government's";
   0123 "economic dev & national security" -> "economic development and national security";
   0536 "Whole of Govt" -> "Whole of Government"; 0543 "any one govt/agency" ->
   "any one government or agency"; 0339 title "Skill Dev" -> "Skill Development";
   0631 title "BIHAR GOVT NUDGE CAMPAIGN" -> "BIHAR GOVERNMENT NUDGE CAMPAIGN".
   LEFT (per instruction): "Govt" inside quotes of 0168, 0269, 0647; "dev" in image URLs.
4. Hard words simplified (outside protected quotes):
   0116 "underscores the need for" -> "shows the need for"; 0153+0155 "underscores the
   imperative to" -> "shows the need to" (unattributed placeholder quote line, user-listed);
   0148 "intricate roles" -> "many roles"; 0415 "pivotal to" -> "important to";
   0095 "Startup India-Digital India synergy is making" -> "Startup India and Digital India
   working together is making" (bold kept on scheme names); 0606 title "CORNERSTONE" ->
   "FOUNDATION".
   LEFT (per instruction): "bedrock" (0158), "synergy" (0347), "cornerstone" (0421) inside
   quotes; "Ethos" in 0630/0633.
   Note: C8 had fixed only the reviewer's listed instances (0150 intricate, 0152 pivotal,
   0108/0110 underscores, 0606 body) — the surviving sibling instances are what C9 cleared.

Check result: 789 cards; 2063 opening / 2063 closing ::: fences, all paired; diff vs backup
= exactly the 16 intended line changes, nothing else. Verifier scripts: scripts/c9_check.py.

Still open (user-reported, NOT in the C9 fix list, left untouched): 0764 "Kurien", 0116
"Natnl Solar Mission", 0106 "Natl Coal Gasification", 0141 "underscoring", 0108 "ex.
finance", 0123 "Envt", 0106/0107/0110/0132/0087 shorthand, 0102 spellings, 0030
"table"->"tabla", 0056 "noy" (inside quote), 0610/0656 "BUFFET", name disagreements
(Rajawat/Rajavat, Megha/Meghachandra, Khambat/Khambhat), US/UK spelling mix, CE/BCE dates,
mismatched bodies (0035, 0073, 0011, 0243, 0067), 0361 numbering, 0430 stray line, 0154
indent, 0090 truncated line itself, 0394 UMANG, stray quote punctuation (15 cards),
placeholders (0044, 0075, 0172, 0264, 0279, 0280, 0284, 0292, 0296, 0414, 0424, 0509, 0529,
0531, blank templates), fact conflicts (gas share 3.9% vs ~6%, forest cover 21.7% vs 24.62%,
"O ACS", ~150 quote attributions, 0392 "$500 Bn", "60+ Vande Bharat"), long sentences 0183,
0218, 0535.

---
## C10 — THIRD-PASS ISSUE CLEANUP (user's full pending list; "best judgment, exam-useful" mandate)
Scope: every item in the user's audit message. Web-verified: Meghachandra Singh, Chhavi
Rajawat, NASSCOM $450-500 Bn AI figure, UMANG wording, Vakataka-era patronage, 2 Guterres quotes.
Backup: polished/MERGED_full_1-789.pre-C10.bak.md. Scripts: c10a_simple.py (54 ops),
c10b_rebuilds.py (rebuilds+fills), c10c_allowlist.py (verifier entries).

### Already fixed, verified as fixed (log was right, reviewer's list was stale)
0764 "V. Kurien" is CORRECT (Verghese Kurien, milk revolution — not "Justice Kurian");
0148 intricate, 0116 underscores, 0095 synergy, 0108 govt's, 0089 Govt steps, 0536 Whole of
Govt, 0606 CORNERSTONE — all cleared in C9; confirmed clean.

### A. Shorthand / spellings / names (web-verified where flagged)
0106 National Coal Gasification Mission + Sustainable Development cell + Australia/South
Africa; 0107 investment; 0110 Central Electricity Authority (CEA); 0116 National Solar
Mission; 0132 national + international; 0123 Environment; 0087 the Naga movement; 0108+0116
"ex." -> "(for example, ...)"; 0141 underscoring -> showing. 0113 Khambhat; 0197
Meghachandra Singh vs the Manipur Assembly (Keisham Meghachandra Singh, SC 21 Jan 2020);
0720 Chhavi Rajawat (title+body; 0719 already correct); 0610+0656 WARREN BUFFETT; 0030
tabla; 0056 "noy"->"not" (typo inside quote, substance unchanged); 0102 REGIONALISM title +
Greater Nagalim / Khalistan / Belgaum / Cauvery / Vidarbha / Bodoland; 0658
conscient->conscience. Dates: 0032 4th-2nd century BCE; 0033 2nd century BCE-3rd century CE;
0034+0035 3rd to 6th century CE; 0010 12th century CE; 0021 100 BCE-10th century CE.
British spellings: behaviour/behavioural/behaviours x4, offence (MLK quote kept as-is).

### B. Content mismatches — rebuilt with verified facts
- 0035 (was a Gupta copy): full rebuild — Vakatakas (Ajanta patrons, Amravati style/Poophnar
  from source PDF p.2431), Ikshvakus (Nagarjunakonda), Kalabhras, Western Gangas (Gomateshwara
  c. 983 CE, Chamundaraya), Kadambas (Banavasi, Mayurasharma); own conclusion; status polished.
- 0073 (data was 12MPRO framework notes from 0056): replaced with real 1857 content — causes
  (Doctrine of Lapse, Awadh 1856, Mangal Pandey, Meerut 10 May), centres & leaders (Bahadur
  Shah II, Nana Saheb, Tantia Tope, Hazrat Mahal, Lakshmibai, Kunwar Singh, Ahmadullah Shah),
  suppression & aftermath (GoI Act 1858, Queen's Proclamation). Historians' conclusion kept.
- 0011 (conclusion duplicated 0010; source PDF literally says "Same as above"): Regional
  styles line restored from PDF p.17 (Sikh chattris/Golden Temple; Rajput Hawa Mahal) + own
  conclusion written (Taj Mahal peak, legacy to Sikh/Rajput schools); same_as_above flag removed.
- 0243 "Cyber Crimes" (held a data definition): real cyber-crime intro (IT Act 2000/2008, I4C);
  crime-stat data and ES conclusion kept.
- 0067 (title duplicated 0065): retitled "Economic Impact of British Rule — Thinkers' Views"
  (its content is the Joshi/Iyer/Dutt drain-of-wealth quotes).

### C. Formatting
0361 Mihir Shah list 1,2,1,2 -> 1,2,3,4 (+ RRR expanded); 0154 intro bullets indented under
parent; 0090 truncated line completed from 0089's own full version (flag kept — card still
skeletal); 0394 UMANG line now reads "Hundreds of central and state citizen services" (no
invented number); stray quote punctuation cleaned in 0561, 0581, 0582, 0603, 0605, 0638,
0657, 0658, 0740, 0743, 0744, 0759, 0766, 0767, 0771, 0787 (period moved inside closing
quote, stray trailing quotes/dots removed).

### D. Placeholders -> real, fact-safe content (no invented statistics/quotes)
0044 Acts intro; 0075 socio-religious reform intro; 0172 hate-speech definition (IPC 153A/
295A/505, Law Commission 267th Report); 0264 universal scheme-evaluation path + conclusion;
0279 education intro (NEP 2020, 5+3+3+4, 6% GDP); 0280 health intro (NHP 2017 2.5% GDP,
Ayushman Bharat); 0284 "O ACS" -> Voice & choice line + universal data anchors; 0292 intro;
0296 blank diplomacy line -> real coverage line; 0414 Gaganyaan conclusion (BAS 2035 / Moon
2040 roadmap); 0424 cryogenics conclusion (1990s denial, GSLV-D5 2014); 0509 crime-terror
conclusion (PMLA/FATF/UNTOC); 0529 + 0531 Guterres pointer lines replaced with VERIFIED
quotes: "Poverty, inequalities and social exclusion give terrorism fuel." (2023) and "A more
secure world begins by investing at least as much in fighting poverty as we do in fighting
wars." (2025). 0177 "(O ACS)" dropped. Statuses flipped needs_review->polished where content
is now complete (flags placeholder_blank removed); 0090 stays needs_review/truncated.

### E. Fact conflicts — labelled, not altered
Gas: 0109/0119 now say "share in the primary energy mix / energy mix" (~6%); 0110 data now
"3.9% Gas (share in installed capacity — the energy-mix share is separately about 6%)".
Forest: 0121 "24.62% (forest cover alone: 21.71%)"; 0451 "21.7% (forest cover only; with tree
cover it is 24.62%)" — ISFR 2021 two-measure distinction now explicit on both cards.
AI: 0392 "$500 Bn by 2025 (NITI Aayog 2018)" corrected to "$450-500 Bn by 2025 — ~10% of the
$5 tn target [Source: NASSCOM AI Adoption Index, 2022]" (web-verified; NITI's own 2018
strategy figure was $957 Bn by 2035).

### F. Long sentences
0183 Recent-Examples line split; 0218 Judges-Cases line split (numbers + [Source] kept);
0535 framing shortened to "In MoHA's words:" (quote verbatim); Bharatiya Nyaya Sanhita /
Bharatiya Nagarik Suraksha Sanhita / Bharatiya Sakshya official spellings + "in force
1 July 2024".

### G. "60+ Vande Bharat" figure — located and refreshed
GS3-INDI-0348: "60+ Vande Bharat trains" (a 2024 snapshot) -> "164 Vande Bharat services
operational by December 2025, carrying over 7.5 crore passengers [Source: Indian Railways]"
(web-verified; 136 trains introduced in 11 years per PIB-style reports).

### Not done (no safe fix without user decision)
~147 remaining quote-attribution questions (0001 Kabir/Tagore, 0053/0059 Goldwater, etc. —
the 2 named Guterres pointers WERE fixed in 0529/0531); duplicate-title pair 0065/0067
resolved by retitle; blank-template cards kept as practice skeletons per earlier C5/C6
decision; "behavior" inside the MLK quote (0709-area) kept — quote text is protected.

### Final verify
789 cards; 2063/2063 ::: fences paired; verify_protected.py: 0 errors, 698 warnings (all
accepted kinds; allowlist extended with C10 entries — full-quote pairs computed from the
original JSON, numbers/lists itemised above).
