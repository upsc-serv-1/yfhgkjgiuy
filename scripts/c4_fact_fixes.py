#!/usr/bin/env python3
"""C4: verified fact corrections. Every fix was web-verified (see log); sources
added inline in brackets as user requested. Changes are logged + allowlisted."""
import re

PATH = '/home/z/my-project/polished/MERGED_full_1-789.md'
book = open(PATH).read()
log = []

FIXES = [
    # (card, old, new, source)
    ("GS1-HIST-0012",
     "Vatsyayan's Kamasutra **Shadanga - 6 parts of poetry**.",
     "Vatsyayan's Kamasutra **Shadanga - 6 parts of painting**.",
     "Shadanga = the six limbs of Indian painting (Vatsyayana); [Source: Wikipedia - Six Limbs (Indian Painting)]"),

    ("GS1-GEOG-0109",
     "from the present **3.9% (2026)**.",
     "from the present **about 6%**.",
     "Gas share of India's energy mix is ~6%; 15% by 2030 target; [Source: IEA India Gas Market Report; MoPNG]"),

    ("GS2-POLI-0177",
     "card_title: \"WOMEN RESERVATION BILL (108th CAA)\"",
     "card_title: \"WOMEN RESERVATION BILL (106th CAA)\"",
     "Nari Shakti Vandan Adhiniyam 2023 is the 106th Amendment (matches card body)"),

    ("GS2-POLI-0198",
     "Women MPs went from **27% (15th LS)** to the current figure.",
     "Women MPs went from **11% (15th LS, 2009)** to the current figure.",
     "15th Lok Sabha had 59 women of 543 (~11%); [Source: PRS Legislative Research]"),

    ("GS2-POLI-0198",
     "**Women MPs:** make up 15%.",
     "**Women MPs:** make up 14% (78 of 543 in the 17th LS).",
     "[Source: The Hindu, May 2019 - 78 women MPs = 14.39%]"),

    ("GS2-POLI-0198",
     "**MPs with criminal records:** rose from 30% (2009) to 43% (2013).",
     "**MPs with criminal records:** rose from 30% (2009) to 43% (2019).",
     "[Source: ADR, 2019 Lok Sabha report - 233 of 543 (43%) in 2019; 162 (30%) in 2009]"),

    ("GS2-POLI-0210",
     "**Examples:** Prashant Bhushan and Justice Karnan (6 months in jail).",
     "**Examples:** Justice C.S. Karnan (6 months in jail for contempt, 2017); Prashant Bhushan (contempt fine of Rs 1, 2020).",
     "[Source: BBC/Al Jazeera, Aug 2020]"),

    ("GS2-POLI-0218",
     "**4th Judges Case (2018), in which the NJAC was struck down.**",
     "**4th Judges Case (2015), in which the NJAC was struck down** by a 4:1 bench on 16 October 2015 [Source: Supreme Court Observer].",
     "[Source: SCAObserver; Wikipedia - NJAC]"),

    ("GS2-GOVE-0232",
     "India ranks **86th** (see also the CVC card).",
     "India ranks **91st out of 182 (CPI 2025, Transparency International)** (see also the CVC card).",
     "[Source: transparency.org/en/cpi/2025]"),

    ("GS2-GOVE-0250",
     "conceptualised by the **Santhanam Committee** in 1994.",
     "conceptualised by the **Santhanam Committee** (report in 1964).",
     "[Source: CVC training material - report submitted 1964; committee set up 1962]"),

    ("GS2-GOVE-0250",
     "India ranks **86th**.",
     "India ranks **91st out of 182 (CPI 2025, Transparency International)**.",
     "[Source: transparency.org/en/cpi/2025]"),

    ("GS2-SOCI-0281",
     "**1 in 7 youths (15-24 years) reported mental health issues (UNICEF 2021)**.",
     "**1 in 7 adolescents (10-19 years) experiences a mental disorder (UNICEF, The State of the World's Children 2021)**.",
     "[Source: WHO fact sheet & UNICEF SOWC 2021 - 1 in 7 of 10-19-year-olds]"),

    ("GS2-SOCI-0281",
     "**1 in 7 youths (15-24 years) are affected (UNICEF 2021)**.",
     "**1 in 7 adolescents (10-19 years) are affected (UNICEF SOWC 2021)**.",
     "[Source: WHO fact sheet & UNICEF SOWC 2021]"),

    ("GS3-SCIE-0392",
     "AI is projected to contribute **$500 Bn** to GDP by 2025.",
     "AI is projected to contribute **$500 Bn** to GDP by 2025 (NITI Aayog's #AIforAll strategy projection, 2018).",
     "[Source: NITI Aayog National Strategy for AI, 2018]"),

    ("GS3-SCIE-0414",
     "ISRO has confirmed an **unmanned mission**, which will make India the **4th nation** to send humans to space.",
     "Gaganyaan is India's human spaceflight programme; it is to make India the **4th nation** to independently send humans to space (after Russia, the USA and China).",
     "[Source: space.com, May 2025; ISRO]"),

    ("GS3-ENVI-0469",
     "Of **63 MT**:",
     "Of this **65 MT** (NITI Aayog/CPCB estimate):",
     "Harmonised with the 65 MT figure used twice in this card; [Source: NITI Aayog Waste to Wealth / CPCB MSW annual report]"),

    ("GS4-ETHI-0724",
     "our **CPI (TI)** rank stands at **85/180**.",
     "our **CPI (TI)** rank stands at **91/182 (CPI 2025)**.",
     "[Source: transparency.org/en/cpi/2025]"),

    ("GS4-ETHI-0778",
     "- Unethical, but illegal in India: \"to take dowry.\".\n- Not illegal in India, but unethical: \"2.1. Marital rape\".\n- Not illegal in India, but unethical: \"2.2. Adopting a girl child by single male\".",
     "- Unethical **and illegal** in India: taking or giving dowry (Dowry Prohibition Act, 1961).\n- Unethical, but **not illegal** in India: marital rape (exception under S.375 IPC; the issue is before the courts).\n- **Not permitted** by regulation: adoption of a girl child by a single male (CARA eligibility rules).",
     "[Source: Dowry Prohibition Act 1961; Bharatiya Nyaya Sanhita S.63/IPC S.375 exception; CARA Adoption Regulations - a single male shall not be eligible to adopt a girl child]"),
]

for cid, old, new, src in FIXES:
    n = book.count(old)
    if n == 0:
        log.append(f"SKIP (0 found) {cid}: {old[:60]}...")
        continue
    if n > 1:
        log.append(f"SKIP (ambiguous {n}x) {cid}: {old[:60]}...")
        continue
    book = book.replace(old, new)
    log.append(f"FIXED {cid}: {old[:70]!r} -> {new[:70]!r}  | {src}")

open(PATH, 'w').write(book)
print('\n'.join(log))
