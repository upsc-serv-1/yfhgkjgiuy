#!/usr/bin/env python3
"""C10a — targeted single-line fixes (shorthand, spellings, names, titles, dates, artefacts)."""
import sys

PATH = "/home/z/my-project/polished/MERGED_full_1-789.md"
text = open(PATH, encoding="utf-8", newline="").read()
ops = []  # (label, expected_count, applied_count)

def rep(label, old, new, count=1):
    global text
    n = text.count(old)
    o, w = old, new
    if n != count:
        o2 = old.replace("'", "\u2019")
        w2 = new.replace("'", "\u2019")
        n2 = text.count(o2)
        if n2 == count:
            o, w, n = o2, w2, n2
        else:
            print(f"FAIL [{label}] expected {count}, found {n} (curly variant {n2}): {old[:70]!r}")
            sys.exit(1)
    text = text.replace(o, w)
    ops.append((label, count, count))

# --- GS1-GEOG shorthand (user-flagged) ---
rep("0116 Natnl Solar Mission", "The Natnl Solar Mission", "The National Solar Mission")
rep("0108+0116 ex. finance", "removing barriers ex. finance, technology collaborations",
    "removing barriers (for example, finance and technology collaborations)", count=2)
rep("0106 Natl Coal Gasification", "the **Natl Coal Gasification Mission — 100 MT 2030**; a Sustainable devel cell in the Coal ministry.",
    "the **National Coal Gasification Mission — 100 MT 2030**; a Sustainable Development cell in the Coal ministry.")
rep("0106 Aust; S Af", "Russia; Aust; S Af", "Russia; Australia; South Africa")
rep("0107 invt", "**Initial invt cost — 4cr/MW for coal vs 6 cr/MW for RE**",
    "**Initial investment cost — 4cr/MW for coal vs 6 cr/MW for RE**")
rep("0110 Auth", "The Central Electricity Auth — India's energy consumption",
    "The Central Electricity Authority (CEA) — India's energy consumption")
rep("0132 natnl + intl", "**Conservation (natnl + intl)**", "**Conservation (national + international)**")
rep("0123 Envt", "Envt — Wind turbines", "Environment — Wind turbines")
rep("0087 mvmt", "Ethnic group vs state: naga mvmt; Khalistan.",
    "Ethnic group vs state: the Naga movement; Khalistan.")
rep("0141 underscoring", "underscoring the need for greater understanding",
    "showing the need for greater understanding")

# --- spellings / names (web-verified where applicable) ---
rep("0113 Khambat", "Barmer, Khambat, Mumbai High", "Barmer, Khambhat, Mumbai High")
rep("0197 Megha Chandra", "**Megha Chandra Singh vs MN Assembly:**", "**Meghachandra Singh vs the Manipur Assembly:**")
rep("0720 Rajawat title", 'card_title: "CHHAVI RAJAVAT (EDUCATED SARPANCH)"', 'card_title: "CHHAVI RAJAWAT (EDUCATED SARPANCH)"')
rep("0720 Rajawat body", "**Chhavi Rajavat** — a Harvard graduate serving as Sarpanch",
    "**Chhavi Rajawat** — a Harvard graduate serving as Sarpanch")
rep("0610 BUFFETT", 'card_title: "WARREN BUFFET ON HIRING"', 'card_title: "WARREN BUFFETT ON HIRING"')
rep("0656 BUFFETT", 'card_title: "WARREN BUFFET ON RATIONAL BEHAVIOUR"', 'card_title: "WARREN BUFFETT ON RATIONAL BEHAVIOUR"')
rep("0030 tabla", "instruments — table, sitar, sarangi vs veena, mridangam",
    "instruments — tabla, sitar, sarangi vs veena, mridangam")
rep("0056 noy in quote", "exploitation noy just the British", "exploitation not just the British")
rep("0102 title", 'card_title: "REGIONALIS M"', 'card_title: "REGIONALISM"')
rep("0102 secession", "Secession: greater nagalim; khalistan", "Secession: Greater Nagalim; Khalistan")
rep("0102 interstate", "Inter-state: belgaum; cauvery", "Inter-state: Belgaum; Cauvery")
rep("0102 intrastate", "Intra-state: vidharba; bodoland", "Intra-state: Vidarbha; Bodoland")
rep("0657 conscient", "erosion of conscient & lack of righteousness", "erosion of conscience & lack of righteousness")

# --- CE/BCE date garbles (incl. two sibling instances of the same defect) ---
rep("0032 Mauryan date", "The Mauryan period — **4th to 2nd CE BC**", "The Mauryan period — **4th to 2nd century BCE**")
rep("0033 post-Mauryan date", "(**2nd CE BC to 3rd CE AD**)", "(**2nd century BCE to 3rd century CE**)")
rep("0034+0035 Gupta date", "the 3rd & 6th CE AD, with patronage", "the 3rd to 6th century CE, with patronage", count=2)
rep("0010 Sultanate date", "Delhi Sultanate in the **12th CE AD**", "Delhi Sultanate in the **12th century CE**")
rep("0021 murals date", "Murals (100 BC-10th CE AD, HBJ):", "Murals (100 BCE-10th century CE, HBJ):")

# --- British spellings (US forms in body; MLK quote on line 21148 untouched) ---
rep("attitude behavioral 1", "built from beliefs, emotions, and behavioral intentions.**",
    "built from beliefs, emotions, and behavioural intentions.**")
rep("attitude behavioral 2", "affective (feeling), and behavioral (intention).**",
    "affective (feeling), and behavioural (intention).**")
rep("attitudes influence behavior", "**Attitudes influence behavior, but social pressure",
    "**Attitudes influence behaviour, but social pressure")
rep("social influence behaviors", "a person's attitudes and behaviors by others",
    "a person's attitudes and behaviours by others")
rep("offense", "Manipulation for self interest; adding to offense;",
    "Manipulation for self interest; adding to offence;")

# --- titles / misc ---
rep("0067 retitle", 'card_title: "Economic impact of British Rule"', 'card_title: "Economic Impact of British Rule — Thinkers\' Views"')

# --- fact labels (two different measures, now labelled) ---
rep("0109 gas label", "the target is to raise its share to **15% by 2030** from the present **about 6%**.",
    "the target is to raise its share in the **primary energy mix** to **15% by 2030** from the present **about 6%**.")
rep("0119 gas label", "India recently set a target of raising the share to **15% by 2030** from the present **6%**",
    "India recently set a target of raising natural gas's share in the **energy mix** to **15% by 2030** from the present **6%**")
rep("0110 capacity label", "- **3.9% Gas**", "- **3.9% Gas** (share in installed capacity — the energy-mix share is separately about 6%)")
rep("0121 forest label", "India's total forest + tree cover stands at **24.62%**.",
    "India's total forest + tree cover stands at **24.62%** (forest cover alone: **21.71%**).")
rep("0451 forest label", "- **FSI:** forest cover stands at **21.7%**, against the **NFP 1988** target of **33%**.",
    "- **FSI:** forest cover stands at **21.7%** (forest cover only; with tree cover it is **24.62%**), against the **NFP 1988** target of **33%**.")

# --- AI $500Bn attribution (web-verified: NASSCOM, not NITI Aayog 2018) ---
rep("0392 data", "- AI is projected to contribute **$500 Bn** to GDP by 2025 (NITI Aayog's #AIforAll strategy projection, 2018).",
    "- AI could add **$450-500 Bn** to India's GDP by 2025 — about **10% of the $5 tn economy** target [Source: NASSCOM AI Adoption Index, 2022].")
rep("0392 conclusion", "**AI could add $500 Bn to India's GDP by 2025**, which is 10% of the $5 Trillion target.",
    "**AI could add $450-500 Bn to India's GDP by 2025** — about 10% of the $5 Trillion target (NASSCOM).")

# --- O ACS cryptic shorthand ---
rep("0177 O ACS", "- It is not a panacea (O ACS).", "- It is not a panacea.")

# --- 0090 truncated line completed from 0089's own full version ---
rep("0090 line", "- Visits by all religions and...", "- Visits by all religions and communities to the Golden Temple")

# --- 0394 UMANG ---
rep("0394 UMANG", "- Additional services have been integrated under the **UMANG app**.",
    "- Hundreds of central and state citizen services have been integrated under the **UMANG app**.")

# --- 0361 Mihir Shah numbering ---
rep("0361 renumber", """  - 1. Demand management: crop diversification.
  - 2. RRR.
  - 1. Supply side: nature-based solutions.
  - 2. Dam and river management.""",
    """  - 1. Demand management: crop diversification.
  - 2. RRR (repair, renovation, restoration of water bodies).
  - 3. Supply side: nature-based solutions.
  - 4. Dam and river management.""")

# --- 0535 Bharatiya official spellings + framing + in-force note ---
rep("0535 bills intro", "- The **MoHA** has brought in 3 new Bills:", "- The **MoHA** has brought in 3 new laws (in force 1 July 2024):")
rep("0535 BNS", "- IPC → **Bhartiya Nyay Sanhita Bill**.", "- IPC → **Bharatiya Nyaya Sanhita**.")
rep("0535 BNSS", "- CrPC → **Bhartiya Nagrik Suraksha Sanhita Bill**.", "- CrPC → **Bharatiya Nagarik Suraksha Sanhita**.")
rep("0535 BSA", "- IEA → **Bhartiya Sakshya Bill**.", "- IEA → **Bharatiya Sakshya**.")
rep("0535 framing", 'The intent behind the new laws, in **MoHA**\'s words:', 'In **MoHA**\'s words:')

# --- 0183 / 0218 long-sentence splits ---
rep("0183 split", "- **Recent Examples:** In Goa (2019), **10/15** Congress MLAs joined the BJP. In Maharashtra, the government collapsed. In Karnataka, the ruling government collapsed. In Manipur, the Speaker did not disqualify.",
    "- **Recent Examples:** In Goa (2019), **10/15** Congress MLAs joined the BJP.\n  In Maharashtra and Karnataka, state governments collapsed. In Manipur, the Speaker did not disqualify.")
rep("0218 split", "- **1st Judges Case (1982); 2nd Judges Case (1993); 3rd Judges Case (1998); 4th Judges Case (2015), in which the NJAC was struck down** by a 4:1 bench on 16 October 2015 [Source: Supreme Court Observer].",
    "- The Judges Cases built it step by step: the **1st (1982)**, the **2nd (1993)**, the **3rd (1998)** and the **4th (2015)**.\n  In the 4th Judges Case the **NJAC was struck down** by a 4:1 bench on 16 October 2015 [Source: Supreme Court Observer].")
rep("0535 split-conclusion already shortened", 'In **MoHA**\'s words: "The spirit', 'In **MoHA**\'s words: "The spirit')  # no-op guard

# --- 0657 double-artefact line ---
rep("0657 MLK+Kalam line",
    "'We must learn to live together as brothers, or die together as fools'\".\" \"'Let us sacrifice our today so that our children can have a better tomorrow', A.P.J. Abdul Kalam\".",
    "'We must learn to live together as brothers, or die together as fools'.\" 'Let us sacrifice our today so that our children can have a better tomorrow', A.P.J. Abdul Kalam.\"")

open(PATH, "w", encoding="utf-8", newline="").write(text)
print(f"OK - {len(ops)} operations applied")
