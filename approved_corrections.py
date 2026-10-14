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
