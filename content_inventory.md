# Content Inventory — Phase 1

**Source:** `inputs/merged_publish_ready_v17.md` (sole content truth) · **Branch:** `ebook-build` · **Generated:** 2026-10-15 21:23 UTC
**Scripts:** `scripts/stage2/audit_cards.py`, `download_images.py`, `make_inventory_md.py` · **Raw data:** `scripts/stage2/v17_inventory.json`, `images_manifest.json`

---

## 1. Executive summary

- **551 cards parsed — clean.** All IDs unique, all `status: polished`, all fences balanced, no duplicate/empty/unknown blocks, no missing metadata, no stray headings or junk lines.
- **Composition:** 476 structured + 75 detail cards · **70,145 body words** (mean 127.3/card, range 28–485).
- **Taxonomy depth (user-assigned, for indexing):** 48 section groups → 209 subtopics → cards; 87 distinct microtopics (syllabus lines).
- **Images: 37 URLs on 36 cards — ALL downloaded and normalized** to `assets/images/` (0 broken; 1 AVIF auto-converted to PNG). No other external URLs exist anywhere in v17 → the final eBook can be 100% hotlink-free.
- **Benign notes:** 38 cards' `sections:` metadata lists a block type once while the actual blocks repeat it (31 multi-quote, 6 multi-detail, 1 multi-image) — schema-valid; the build must render ACTUAL blocks. Also 5 cards have no introduction/conclusion block (detail/quote-style cards, by design).
- **Blocking risks for Phase 2: none.**

## 2. Card inventory & distributions

### By paper
| Paper | Cards | % of book |
|---|---|---|
| GS-1 | 98 | 17.8 |
| GS-2 | 116 | 21.1 |
| GS-3 | 188 | 34.1 |
| GS-4 | 149 | 27.0 |

### By subject (within papers)
| Paper | Subject | Cards | % of book |
|---|---|---|---|
| GS-1 | HISTORY | 54 | 9.8 |
| GS-1 | GEOGRAPHY | 33 | 6.0 |
| GS-1 | SOCIETY | 11 | 2.0 |
| GS-2 | POLITY | 43 | 7.8 |
| GS-2 | GOVERNANCE | 32 | 5.8 |
| GS-2 | INTERNATIONAL RELATIONS | 26 | 4.7 |
| GS-2 | SOCIAL JUSTICE | 15 | 2.7 |
| GS-3 | ENVIRONMENT | 40 | 7.3 |
| GS-3 | SCIENCE & TECHNOLOGY | 39 | 7.1 |
| GS-3 | INTERNAL SECURITY | 37 | 6.7 |
| GS-3 | INDIAN ECONOMY | 28 | 5.1 |
| GS-3 | AGRICULTURE | 22 | 4.0 |
| GS-3 | DISASTER MANAGEMENT | 22 | 4.0 |
| GS-4 | ETHICS, INTEGRITY & APTITUDE | 149 | 27.0 |

### Card type / status / flags
| Item | Count |
|---|---|
| structured | 476 |
| detail | 75 |
| status: polished | 551 |
| flag: has_image | 36 |
| flag: format_fixed | 57 |
| flag: universal_template | 5 |

### Block types across the book
| Block type | Total occurrences |
|---|---|
| introduction | 546 |
| conclusion | 546 |
| quote | 302 |
| examples | 244 |
| data | 168 |
| detail | 82 |
| image | 37 |

*(Full section_group breakdown per subject: `scripts/stage2/v17_inventory.json` → `distributions.subject_section_groups`; full card-level hierarchy: `hierarchy`.)*

## 3. Metadata gaps & flagged cards

- **Missing metadata: none.** Every card has paper, subject, section_group, microtopic, subtopic, card_title, card_type, status.
- **`universal_template` cards (5):** GS3-ENVI-0462, GS3-DISA-0483, GS3-INTE-0517, GS3-INTE-0534, GS3-INTE-0543 — practice-skeleton cards; render as templates, not filled essays (Editor note).
- **`format_fixed` cards (57):** cosmetic Stage-1 flag; no action needed.
- **`has_image` cards (36):** see image manifest below.

## 4. Internal-consistency findings

- **38 `sections_meta_mismatch` — ALL benign** (verified: deduplicated type sequences identical for every card). Actual blocks repeat a type that the `sections:` list mentions once: 31 multi-quote cards (e.g. GS1-HIST-0054 has 3 quotes, metadata lists 1), 6 multi-detail cards (GS3-ENVI-0462, GS3-DISA-0483, GS3-INTE-0517, GS3-INTE-0534, GS3-INTE-0543, GS4-ETHI-0599), 1 multi-image card (GS4-ETHI-0721). The eBook build must use ACTUAL blocks, not the `sections:` list.
- **Cards without introduction or conclusion blocks (5):** GS3-ENVI-0462, GS3-DISA-0483, GS3-INTE-0517, GS3-INTE-0534, GS3-INTE-0543 — these are quote/data-led cards; do not force intro/conclusion structure on them in layout.
- No stray close fences, no nested opens, no unknown block names, no duplicate IDs, no unexpected headings, no preamble junk. v17 is structurally sound.

## 5. Image audit

**37 unique URLs → 1 downloaded OK, 0 broken.** One source file was AVIF and was converted to PNG (`ethi_social-influence-and-persuasion_01.png`). Total local weight ≈ 8.5 MB. Card with multiple images: GS4-ETHI-0721.
Also staged: `cover_candidate_resource_guide.png` (user-uploaded resource guide; role TBD — cover art candidate).

| Local file | Card(s) | Subject | Subtopic | Source file | KB | Status |
|---|---|---|---|---|---|---|
| `soju_education_01.jpg` | GS2-SOCI-0278 | Social Justice | Education | diagram_p12.png | 38 | ok |
| `ir_indian-diaspora_01.png` | GS2-INTE-0315 | International Relations | Indian Diaspora | diagram_p15.png | 123 | ok |
| `ir_united-nations-and-its-agencies_01.png` | GS2-INTE-0317 | International Relations | United Nations and its Agencies | diagram_p16.png | 212 | ok |
| `gove_government-schemes-and-policies_01.jpg` | GS2-GOVE-0262 | Governance | Government Schemes and Policies | diagram_p7.png | 36 | ok |
| `gove_civil-society_01.png` | GS2-GOVE-0258 | Governance | Civil Society | diagram_p8.png | 34 | ok |
| `agri_cropping-pattern_01.png` | GS3-AGRI-0363 | Agriculture | Cropping pattern | diagram_p10.png | 54 | ok |
| `agri_agri-marketing_01.png` | GS3-AGRI-0369 | Agriculture | Agri-Marketing | diagram_p11.png | 48 | ok |
| `econ_lpg-reform-and-impact_01.png` | GS3-INDI-0332 | Indian Economy | LPG Reform and Impact | diagram_p16.png | 122 | ok |
| `econ_airports-x-infrastructure_01.png` | GS3-INDI-0348 | Indian Economy | Airports X Infrastructure | diagram_p18.png | 45 | ok |
| `scitech_innovative-technologies_01.png` | GS3-SCIE-0388 | Science & Technology | Innovative Technologies | diagram_p21.png | 75 | ok |
| `envi_unfccc_01.png` | GS3-ENVI-0436 | Environment | UNFCCC | diagram_p23.png | 90 | ok |
| `envi_eia_01.png` | GS3-ENVI-0445 | Environment | EIA | diagram_p24.png | 83 | ok |
| `econ_investment_01.png` | GS3-INDI-0340 | Indian Economy | Investment | diagram_p6.png | 83 | ok |
| `econ_fiscal-policy_01.png` | GS3-INDI-0336 | Indian Economy | Fiscal Policy | diagram_p9.png | 40 | ok |
| `ethi_accountability-and-ethical-governance_01.png` | GS4-ETHI-0758 | Ethics, Integrity & Aptitude | Accountability and Ethical Governance | diagram_accountability.png | 208 | ok |
| `poli_constitutional-morality_01.png` | GS2-POLI-0558 | Polity | Constitutional Morality | diagram_constitutional_morality.png | 913 | ok |
| `ethi_challenges-of-corruption_01.png` | GS4-ETHI-0721 | Ethics, Integrity & Aptitude | Challenges of Corruption | diagram_corruption_equation.png | 793 | ok |
| `ethi_ei-concept-and-utility_01.jpg` | GS4-ETHI-0648 | Ethics, Integrity & Aptitude | EI: Concept and utility | diagram_ei_models.jpg | 34 | ok |
| `ethi_teachings-of-great-leaders_01.png` | GS4-ETHI-0718 | Ethics, Integrity & Aptitude | Teachings of Great Leaders | diagram_hobbes_social_contract.png | 215 | ok |
| `ethi_integrity-x-intelligence-x-energy_01.png` | GS4-ETHI-0612 | Ethics, Integrity & Aptitude | Integrity X Intelligence X Energy | diagram_integrity_intelligence_energy.png | 900 | ok |
| `ethi_attitude-for-individuals_01.png` | GS4-ETHI-0621 | Ethics, Integrity & Aptitude | Attitude for Individuals | diagram_p11_img6.png | 47 | ok |
| `ethi_ei-concept-and-utility_02.png` | GS4-ETHI-0641 | Ethics, Integrity & Aptitude | EI: Concept and utility | diagram_p16_img9.png | 90 | ok |
| `ethi_ei-concept-and-utility_03.png` | GS4-ETHI-0644 | Ethics, Integrity & Aptitude | EI: Concept and utility | diagram_p17_img12.png | 78 | ok |
| `ethi_ei-in-administration_01.png` | GS4-ETHI-0636 | Ethics, Integrity & Aptitude | EI in Administration | diagram_p18_img13.png | 81 | ok |
| `ethi_teachings-of-great-leaders_02.png` | GS4-ETHI-0694 | Ethics, Integrity & Aptitude | Teachings of Great Leaders | diagram_p20_img15.png | 112 | ok |
| `ethi_ethical-issues-in-international-relation_01.png` | GS4-ETHI-0770 | Ethics, Integrity & Aptitude | Ethical Issues in International Relations an… | diagram_p24_img17.png | 98 | ok |
| `ethi_quality-of-service-delivery_01.png` | GS4-ETHI-0739 | Ethics, Integrity & Aptitude | Quality of Service Delivery | diagram_p27_img18.png | 102 | ok |
| `ethi_challenges-of-corruption_02.png` | GS4-ETHI-0721 | Ethics, Integrity & Aptitude | Challenges of Corruption | diagram_p28_img19.png | 101 | ok |
| `ethi_essence-of-ethics_01.png` | GS4-ETHI-0551 | Ethics, Integrity & Aptitude | Essence of Ethics | diagram_p4_img1.png | 67 | ok |
| `ethi_essence-of-ethics_02.png` | GS4-ETHI-0563 | Ethics, Integrity & Aptitude | Essence of Ethics | diagram_p5_img2.png | 98 | ok |
| `ethi_term-based_01.png` | GS4-ETHI-0568 | Ethics, Integrity & Aptitude | Term Based | diagram_p7_img3.png | 68 | ok |
| `ethi_teachings-of-great-leaders_03.png` | GS4-ETHI-0691 | Ethics, Integrity & Aptitude | Teachings of Great Leaders | diagram_p8_img4.png | 68 | ok |
| `ethi_value-based-questions_01.png` | GS4-ETHI-0580 | Ethics, Integrity & Aptitude | Value Based Questions | diagram_p9_img5.png | 66 | ok |
| `ethi_social-influence-and-persuasion_01.png` | GS4-ETHI-0630 | Ethics, Integrity & Aptitude | Social influence and persuasion | diagram_rhetorical_appeals.avif | 533 | ok (converted AVIF→PNG) |
| `ethi_essence-of-ethics_03.png` | GS4-ETHI-0557 | Ethics, Integrity & Aptitude | Essence of Ethics | diagram_righteousness.png | 207 | ok |
| `ethi_transparency-x-rti_01.png` | GS4-ETHI-0741 | Ethics, Integrity & Aptitude | Transparency X RTI | diagram_transparency_good_governance.png | 861 | ok |
| `ethi_challenges-of-corruption_03.png` | GS4-ETHI-0728 | Ethics, Integrity & Aptitude | Challenges of Corruption | diagram_vicious_cycle_corruption.png | 1044 | ok |

## 6. Other external links

**None.** The image URLs above are the only external references in v17. With images localized, the final HTML needs zero network requests.

## 7. Recommendations for Phase 2 (book architecture)

1. **Follow the user taxonomy exactly:** Part = GS paper (GS-1 → GS-4) → Chapter = subject (14 chapters) → Section = section_group → Card group = subtopic. This doubles as the GS-wise/subject-wise index the user asked for.
2. **GS-4 Ethics is 27% of the book (149 cards)** — give it strong internal navigation (its section_groups as visible sub-sections); consider its own mini-index.
3. **Prototype-type SVG illustrations** (recreated, not copied): marks-share donut for the front matter, per-part opener visuals, tier/heatmap tables where the prototype uses them.
4. **Images via relative paths** (`assets/images/…`) by default; add a build flag for a base64-embedded portable single file (8.5 MB of images makes embedding heavy — recommend relative as primary).
5. Render detail cards (75) with their `:::detail label` headers; render multi-quote cards with all quotes in sequence.
6. The 5 universal_template cards should be visually marked as "practice skeletons".
