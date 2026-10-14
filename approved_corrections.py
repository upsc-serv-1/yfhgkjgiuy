"""approved_corrections.py — user-approved deviations from the raw source JSON.

Every entry is auditable and was explicitly authorised by the user's correction
instructions (remove stray fragments / fix facts after verification / restore
truncated content / fix spelling). The verifier consults this file before
flagging an ERROR, so genuine unapproved damage is still caught with 0 noise.
"""

# numbers that vanish because of approved removals / verified corrections
APPROVED_NUMBER_REMOVALS = {
    # C1: junk heading removed from end of conclusion
    'GS1-HIST-0007': {'18': 'junk heading "II. Modern Indian History (Mid-18th Century to Present)" removed'},
    'GS1-SOCI-0095': {'11': 'junk heading "11-A.Social Empowerment" removed'},
    # C4 verified fact corrections (each web-sourced; see corrections_log.md)
    'GS1-GEOG-0109': {'3.9%': 'wrong gas share replaced with verified ~6% (IEA/MoPNG)', '2026': 'unstamped year removed with the wrong figure'},
    'GS2-POLI-0198': {'27%': 'wrong women-MP share for 15th LS; 11% is correct (PRS)',
                      '15%': 'rounded-up women-MP share; replaced with 14% (78/543, The Hindu)',
                      '2013': 'ADR criminal-case year was 2019, not 2013'},
    'GS2-GOVE-0232': {'86': 'CPI rank year unstamped; updated to CPI 2025 (rank 91)'},
    'GS2-GOVE-0250': {'86': 'CPI rank year unstamped; updated to CPI 2025 (rank 91)',
                      '1994': 'Santhanam Committee report was 1964, not 1994 (CVC)'},
    'GS2-SOCI-0281': {'15': 'UNICEF age band is 10-19, not 15-24 (WHO/UNICEF)',
                      '24': 'UNICEF age band is 10-19, not 15-24 (WHO/UNICEF)'},
    'GS3-ENVI-0469': {'63': 'internal mismatch harmonised to the 65 MT figure used twice in the card'},
    'GS2-POLI-0218': {'2018': 'wrong year; NJAC was struck down in 2015 (SC Observer)'},
    'GS4-ETHI-0724': {'85/180': 'CPI rank updated to CPI 2025 (91/182)'},
    'GS2-GOVE-0255': {'1994': 'Santhanam Committee report was 1964, not 1994 (CVC)', '86': 'CPI rank updated to CPI 2025 (rank 91)'},
    'GS4-ETHI-0778': {'2.1': 'sub-numbering removed in corrected examples',
                      '2.2': 'sub-numbering removed in corrected examples'},
}

# numbers added/changed by verified fact corrections or PDF restorations
APPROVED_NUMBER_ADDITIONS = {
    'GS3-SCIE-0412': {'1': 'Aditya-L1 mission name added in second-pass rewrite (block 0412 intro)'},
    'GS1-HIST-0077': {'312': 'Art. 312 All-India Services added in card completion'},
    'GS1-GEOG-0115': {'2': 'RE card restored from source PDF: 2nd largest RE growth, 2x import bill',
                      '2030': 'RE card restored from PDF: import bill 2x by 2030',
                      '3': 'RE card restored from PDF: 3rd largest producer',
                      '4': 'RE card restored from PDF: Rs 4 cr/MW coal (P1 p.4)',
                      '6': 'RE card restored from PDF: Rs 6 cr/MW RE (P1 p.4)',
                      '50%': 'Panchamrit 50% RE (P1 p.4)', '500': 'Panchamrit 500 GW (P1 p.4)'},

    # C4 verified fact corrections
    'GS1-GEOG-0109': {'6': 'gas share of energy mix ~6% (IEA/MoPNG); replaces wrong 3.9%'},
    'GS2-POLI-0198': {'11': 'women MPs 11% in 15th LS (PRS)', '11%': 'women MPs 11% in 15th LS (PRS)',
                      '17': '17th Lok Sabha', '2009': 'year qualifier for 15th LS',
                      '2019': 'ADR 2019 report year', '543': 'Lok Sabha strength',
                      '78': '78 women MPs in 17th LS (The Hindu)', '14%': 'women MPs 14.39% in 17th LS'},
    'GS2-POLI-0210': {'1': 'Rs 1 contempt fine on Bhushan (BBC)', '2017': 'Karnan contempt year',
                      '2020': 'Bhushan contempt year'},
    'GS2-POLI-0218': {'2015': 'NJAC struck down 16 Oct 2015 (SC Observer)', '4': '4:1 bench split', '1': '4:1 bench split',
                      '16': '16 October 2015'},
    'GS2-GOVE-0232': {'182': 'CPI 2025 covers 182 countries', '2025': 'CPI 2025',
                      '91': 'India rank 91 (CPI 2025)'},
    'GS2-GOVE-0250': {'182': 'CPI 2025 covers 182 countries', '2025': 'CPI 2025',
                      '91': 'India rank 91 (CPI 2025)', '1964': 'Santhanam Committee report year (CVC)'},
    'GS2-SOCI-0281': {'10': 'UNICEF age band 10-19', '19': 'UNICEF age band 10-19'},
    'GS3-SCIE-0392': {'2018': 'NITI Aayog #AIforAll strategy year'},
    'GS3-ENVI-0469': {'65': 'harmonised to the 65 MT figure used elsewhere in the card'},
    'GS4-ETHI-0724': {'2025': 'CPI 2025', '91/182': 'India rank 91 of 182 (CPI 2025)'},
    'GS2-GOVE-0255': {'182': 'CPI 2025 covers 182 countries', '2025': 'CPI 2025', '91': 'India rank 91 (CPI 2025)', '1964': 'Santhanam Committee report year (CVC)'},
    'GS4-ETHI-0778': {'1961': 'Dowry Prohibition Act year', '375': 'IPC S.375 reference'},
}

# text deleted from protected quote blocks (C2: "— Source Text" label removal)
APPROVED_QUOTE_DELETIONS = {
    'GS1-GEOG-0125': {'quote': ('— Source Text', 'C2: converter placeholder label removed, quote kept')},
    'GS1-GEOG-0151': {'quote': ('— Source Text', 'C2: converter placeholder label removed, quote kept')},
    'GS1-GEOG-0153': {'quote': ('— Source Text', 'C2: converter placeholder label removed, quote kept')},
}

# replacements inside protected quote blocks (C3: clear misspellings)
APPROVED_QUOTE_REPLACEMENTS = {
    'GS3-INTE-0537': {'quote': ('General Manoj Narawane', 'General Manoj Naravane', 'C3: COAS name spelling')},
    'GS4-ETHI-0656': {'quote': ('Warren Buffet', 'Warren Buffett', 'C3: spelling in quote label')},
    'GS4-ETHI-0708': {'quote': ('Bhagvad Geeta', 'Bhagavad Gita', 'C3: standard spelling in quote label')},
}

# list-item count changes approved for restoration work (C5)
APPROVED_LIST_CHANGES = {}

# capitalised tokens that vanish because an approved fragment removal/replacement contained them
APPROVED_CAPS_REMOVALS = {
    # C1 junk headings
    'GS1-HIST-0007': {'conclusion': ['II', 'Century', 'History', 'Indian', 'Present']},
    'GS1-HIST-0041': {'conclusion': ['Topic', 'C', 'Architecture']},
    'GS1-HIST-0083': {'conclusion': ['III.INDIAN', 'SOCIETY', 'UPSC-relevant']},
    'GS1-SOCI-0091': {'conclusion': ['Poverty', 'Development']},
    'GS1-SOCI-0092': {'conclusion': ['Gender', 'Disparity', 'Laws', 'Reforms']},
    'GS1-SOCI-0094': {'conclusion': ['Perfect', 'UPSC-relevant']},
    'GS1-SOCI-0095': {'conclusion': ['11', 'A.Social', 'Empowerment']},
    'GS1-SOCI-0104': {'conclusion': ['Urban', 'Governance']},
    # C3 spelling fixes (old misspelled tokens no longer in polished text)
    'GS1-GEOG-0106': {'*': ['Shanqxi']},
    'GS1-GEOG-0113': {'*': ['Vyzag', 'Khambat']},
    'GS1-GEOG-0143': {'*': ['Wegner', 'Alfred Wegner']},
    'GS1-GEOG-0145': {'*': ['Mckenzie']},
    'GS1-HIST-0003': {'*': ['Siddharta', 'Siddharta Gautama', 'Aichi Ladakh', 'Aichi']},
    'GS1-HIST-0005': {'*': ['V K Vakankar', 'Vakankar']},
    'GS1-HIST-0009': {'*': ['Dropadi', 'Lingraj', 'Narsimha:', 'Panchpandav', 'Rajarasjeshwara', 'Rajsimhavarman', 'Vijaynagar', 'Narsimha']},
    'GS1-HIST-0010': {'*': ['Adhai din ka jhopra', 'Arcuade', 'Quadam Rasul', 'Sharqui', 'Tuglaq']},
    'GS1-HIST-0019': {'*': ['Kathakalli', 'Dara Sikoh', 'Sikoh']},
    'GS1-HIST-0022': {'*': ['Burakatha', 'Kuchipuri', 'Tarangmal']},
    'GS1-HIST-0023': {'*': ['Kathakalli', 'Abhinay Darpan', 'Burakatha', 'Tarangmal', 'Abhinay', 'Darpan', 'Kuchipuri']},
    'GS1-HIST-0032': {'*': ['Mukrarakshasa', 'Piprawaha']},
    'GS1-HIST-0034': {'*': ['Ankapallee', 'Aryabhatt', 'Harisen', 'Huein Tsang', 'Kalidas', 'Surya Siddhantika', 'Vijaywada', 'Vishakhadutta', 'Siddhantika']},
    'GS1-HIST-0035': {'*': ['Ankapallee', 'Aryabhatt', 'Harisen', 'Huein Tsang', 'HueinTsang', 'Kalidas', 'Surya Siddhantika', 'Vijaywada', 'Vishakhadutta', 'Siddhantika']},
    'GS1-HIST-0043': {'*': ['Statute of Unity, Statute of Equality', 'Statute', 'Narsimha, Mahishasura', 'Narsimha']},
    'GS1-SOCI-0087': {'*': ['Dropadi', 'khalisatn']},
    'GS1-SOCI-0088': {'*': ['Kaktiya', 'rayagada']},
    'GS1-SOCI-0089': {'*': ['Gauri lankesh', 'narender Dabholkar', 'sabrimala', 'devdasi']},
    'GS1-SOCI-0101': {'*': ['Vidharba']},
    'GS1-GEOG-0111': {'*': ['throium']},
    'GS1-GEOG-0496': {'*': ['Rein Bashera', 'Bashera']},
    'GS3-DISA-0496': {'*': ['Rein Bashera', 'Bashera']},
    'GS3-SCIE-0420': {'*': ['Visheswaraya']},
    'GS2-POLI-0165': {'*': ['Indira Sawhney', 'Narsimha Rao', 'Narsimha']},
    'GS2-POLI-0183': {'*': ['AyaRam GayaRam', 'AyaRam', 'GayaRam']},
    'GS4-ETHI-0648': {'*': ['Mayor and Salovey', 'Mayor']},
    'GS4-ETHI-0651': {'*': ['Mayor and Salovey', 'Mayor']},
    'GS4-ETHI-0652': {'*': ['Mayor & Salovey', 'Mayor']},
    'GS4-ETHI-0697': {'*': ['Madhyammarga']},
    'GS4-ETHI-0719': {'*': ['Savitri Bai Phule', 'Bai']},
    'GS4-ETHI-0764': {'*': ['Justice Kurien', 'Kurien']},
}


# ---------------------------------------------------------------------------
# C10 - THIRD-PASS ISSUE CLEANUP (user-reported list; web-verified facts where added)
# Generated by scripts/c10c_allowlist.py - full-quote pairs computed from the
# original JSON via convert.py so the verifier's single-replace check passes.
APPROVED_QUOTE_REPLACEMENTS.update({'GS1-HIST-0056': {'quote': ('"I am not interested in freeing India merely from the British Yoke '
                             'but from any yoke whatsoever. Thus the aim remained Swaraj from all '
                             'forms of exploitation noy just the British." — Mahatma Gandhi',
                             '"I am not interested in freeing India merely from the British Yoke '
                             'but from any yoke whatsoever. Thus the aim remained Swaraj from all '
                             'forms of exploitation not just the British." — Mahatma Gandhi',
                             "C10: obvious typo 'noy'->'not' inside quote, substance unchanged")},
 'GS1-GEOG-0153': {'quote': ('"The declaration of 2021- 2030 as the decade of ocean sciences '
                             'underscores the imperative to harness ocean resources responsibly '
                             'and collaboratively for a resilient and prosperous future." — Source '
                             'Text',
                             '"The declaration of 2021- 2030 as the decade of ocean sciences shows '
                             'the need to harness ocean resources responsibly and collaboratively '
                             'for a resilient and prosperous future."',
                             'C9: user-directed hard-word fix in unattributed placeholder quote')},
 'GS1-GEOG-0155': {'quote': ('"The declaration of 2021- 2030 as the decade of ocean sciences '
                             'underscores the imperative to harness ocean resources responsibly '
                             'and collaboratively for a resilient and prosperous future."',
                             '"The declaration of 2021- 2030 as the decade of ocean sciences shows '
                             'the need to harness ocean resources responsibly and collaboratively '
                             'for a resilient and prosperous future."',
                             'C9: user-directed hard-word fix in unattributed placeholder quote')},
 'GS4-ETHI-0581': {'quote': ('"Thus, Winston Churchill has rightly said, \'There is no doubt that '
                             'it is around the family that all the greatest institutions are '
                             'created, strengthened and maintained\'"."',
                             '"Thus, Winston Churchill has rightly said, \'There is no doubt that '
                             'it is around the family that all the greatest institutions are '
                             'created, strengthened and maintained\'."',
                             'C10: stray quote punctuation artefact removed')},
 'GS4-ETHI-0582': {'quote': ('"Thus, Plato has correctly said, \'What is honoured in a society is '
                             'cultivated there \'."."',
                             '"Thus, Plato has correctly said, \'What is honoured in a society is '
                             'cultivated there \'."',
                             'C10: stray quote punctuation artefact removed')},
 'GS4-ETHI-0657': {'quote': ('"We must remember, what Martin Luther King Jr. said, \'We must learn '
                             'to live together as brothers, or die together as fools\'"." "\'Let '
                             'us sacrifice our today so that our children can have a better '
                             'tomorrow\', A.P.J. Abdul Kalam"."',
                             '"We must remember, what Martin Luther King Jr. said, \'We must learn '
                             'to live together as brothers, or die together as fools\'." \'Let us '
                             'sacrifice our today so that our children can have a better '
                             'tomorrow\', A.P.J. Abdul Kalam."',
                             'C10: stray quote punctuation artefacts removed (MLK/Kalam line)')},
 'GS4-ETHI-0658': {'quote': ('"Kalam: corruption arises as a consequence of erosion of conscient & '
                             'lack of righteousness."',
                             '"Kalam: corruption arises as a consequence of erosion of conscience '
                             '& lack of righteousness."',
                             "C10: obvious misspelling 'conscient'->'conscience' in Kalam quote")},
 'GS4-ETHI-0743': {'quote': ('"Thus, the solution suggested by Kofi Annan holds ground. \'If '
                             'corruption is disease, transparency is the best treatment '
                             'available!\'"."',
                             '"Thus, the solution suggested by Kofi Annan holds ground. \'If '
                             'corruption is disease, transparency is the best treatment '
                             'available!\'"',
                             'C10: stray quote punctuation artefact removed (Annan quote)')},
 'GS4-ETHI-0787': {'quote': ('"On Marital rape: As noted by European Commission of Justice \'A '
                             'rapist is a rapist regardless of his relationship with the '
                             'victim!\'"."',
                             '"On Marital rape: As noted by European Commission of Justice \'A '
                             'rapist is a rapist regardless of his relationship with the '
                             'victim!\'"',
                             'C10: stray quote punctuation artefact removed (marital-rape quote)')}})

APPROVED_NUMBER_ADDITIONS.update({'GS1-HIST-0035': {'10': 'rebuild: 4th-10th CE Western Gangas',
                   '3': 'rebuild: 3rd-X CE dynasty date ranges',
                   '4': 'rebuild: 3rd/4th/6th CE date ranges',
                   '5': 'rebuild: 3rd-5th CE Vakatakas',
                   '6': 'rebuild: 4th-6th CE Kadambas',
                   '7': 'rebuild: 3rd-7th CE Kalabhras',
                   '983': 'rebuild: Gomateshwara erected c. 983 CE'},
 'GS1-HIST-0073': {'10': '1857 rebuild: Meerut outbreak 10 May 1857',
                   '1848': 'Doctrine of Lapse: Satara 1848',
                   '1853': 'Jhansi annexation 1853',
                   '1856': 'Awadh annexation + General Service Enlistment Act 1856',
                   '1857': '1857 revolt year / Barrackpore / Meerut',
                   '1858': "GoI Act 1858 + Queen's Proclamation 1858"},
 'GS1-HIST-0075': {'19': '19th-century reform movements intro added'},
 'GS1-GEOG-0110': {'6': 'energy-mix share ~6% clarifier (distinct from 3.9% capacity share)'},
 'GS1-GEOG-0121': {'21.71%': 'forest-cover-only figure added to separate the two measures'},
 'GS2-POLI-0172': {'153': 'IPC 153A',
                   '267': 'Law Commission 267th Report',
                   '295': 'IPC 295A',
                   '505': 'IPC 505'},
 'GS2-GOVE-0243': {'2000': 'IT Act 2000', '2008': 'IT Act amendment 2008', '4': 'I4C cyber centre'},
 'GS2-GOVE-0264': {'3': '3F (funds, functionaries, functions) reference'},
 'GS2-SOCI-0279': {'2020': 'NEP 2020',
                   '3': '5+3+3+4 school design',
                   '4': '5+3+3+4 school design',
                   '5': '5+3+3+4 school design',
                   '6': 'NEP 6% of GDP public-spending goal'},
 'GS2-SOCI-0280': {'2.5%': 'NHP 2017 2.5% GDP target', '2017': 'National Health Policy 2017'},
 'GS2-SOCI-0284': {'38': 'Art. 38 welfare state', '46': 'Art. 46 weaker sections'},
 'GS3-AGRI-0361': {'3': 'Mihir Shah list renumbered 1,2,1,2 -> 1,2,3,4',
                   '4': 'Mihir Shah list renumbered'},
 'GS3-SCIE-0392': {'10%': '~10% of $5 tn target retained',
                   '2022': 'NASSCOM AI Adoption Index 2022',
                   '450': 'NASSCOM $450-500 Bn range',
                   '5': '$5 tn economy target'},
 'GS3-SCIE-0414': {'2035': 'Bharatiya Antariksh Station roadmap (announced)',
                   '2040': 'Indian on Moon roadmap (announced)'},
 'GS3-SCIE-0424': {'1990': 'technology denial episode of the 1990s',
                   '2014': 'GSLV-D5 indigenous cryogenic success',
                   '5': 'GSLV-D5'},
 'GS3-ENVI-0451': {'24.62%': 'forest+tree cover figure added to separate the two measures'},
 'GS3-INTE-0535': {'1': 'new criminal laws in force 1 July 2024', '2024': 'in force 1 July 2024'}})

APPROVED_NUMBER_REMOVALS.update({'GS1-HIST-0035': {'8': 'Samudragupta 8 coin-types detail removed in rebuild',
                   '10': 'Cave 10 detail removed in rebuild',
                   '16': 'Cave 16 detail removed in rebuild',
                   '34': 'Ellora 34 caves detail removed in rebuild'},
 'GS3-AGRI-0361': {'1': 'duplicate list number removed (1,2,1,2 -> 1,2,3,4)',
                   '2': 'duplicate list number removed (1,2,1,2 -> 1,2,3,4)'},
 'GS3-SCIE-0392': {'2018': 'NITI Aayog 2018 attribution removed; figure re-sourced to NASSCOM 2022 '
                           '(web-verified)'},
 'GS3-SCIE-0414': {'1': 'Aditya L1 placeholder conclusion replaced with real Gaganyaan conclusion'}})

APPROVED_LIST_CHANGES.update({'GS1-HIST-0011': {'data': (9, 10, 'Regional styles line restored from source PDF p.17')},
                              'GS1-HIST-0073': {'data': (4, 14, '12MPRO framework notes replaced with real 1857 content (causes/centres/aftermath)')}})

# C10 addendum: Vande Bharat figure refreshed (was "60+ trains", a 2024 snapshot)
APPROVED_NUMBER_ADDITIONS.update({'GS3-INDI-0348': {'164': 'Vande Bharat services operational by Dec 2025 (Indian Railways)',
                                                    '2025': 'December 2025 milestone',
                                                    '7.5': '7.5 crore passengers carried (Indian Railways)'}})
APPROVED_NUMBER_REMOVALS.update({'GS3-INDI-0348': {'60': 'outdated 2024 snapshot replaced with Dec 2025 figure'}})
