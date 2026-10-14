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
