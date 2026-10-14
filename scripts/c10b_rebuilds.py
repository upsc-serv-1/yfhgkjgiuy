#!/usr/bin/env python3
"""C10b — block rebuilds (0035/0073/0011/0243/0044), placeholder fills, 0154 indent, stray punctuation, status flips."""
import sys

PATH = "/home/z/my-project/polished/MERGED_full_1-789.md"
text = open(PATH, encoding="utf-8", newline="").read()
fails = []

# ---------- helpers ----------
def card_span(cid):
    starts = [m.start() for m in __import__("re").finditer(r"(?m)^id: ", text)]
    ids = [text[m.start():text.index("\n", m.start())][4:].strip("\r") for m in __import__("re").finditer(r"(?m)^id: ", text)]
    i = ids.index(cid)
    return starts[i], (starts[i + 1] if i + 1 < len(starts) else len(text))

def rep_in_card(cid, label, old, new, count=1):
    global text
    s, e = card_span(cid)
    seg = text[s:e]
    n = seg.count(old)
    if n != count:
        o2 = old.replace("'", "\u2019"); n2 = seg.count(o2)
        if n2 == count:
            old, new, n = o2, new.replace("'", "\u2019"), n2
        else:
            fails.append(f"[{cid}] {label}: expected {count}, found {n} (curly {n2})")
            return
    text = text[:s] + seg.replace(old, new) + text[e:]

def rep(label, old, new, count=1):
    global text
    n = text.count(old)
    o, w = old, new
    if n != count:
        o2 = old.replace("'", "\u2019"); n2 = text.count(o2)
        if n2 == count:
            o, w, n = o2, new.replace("'", "\u2019"), n2
        else:
            fails.append(f"[GLOBAL] {label}: expected {count}, found {n} (curly {n2})")
            return
    text = text.replace(o, w)

# ---------- 0035 rebuild ----------
rep("0035 title", 'card_title: "GUPTA Contemp: Vakatakas, Ikshwakus Kalabhras, Gangas, Kadambas"',
    'card_title: "GUPTA Contemp: Vakatakas, Ikshvakus, Kalabhras, Gangas, Kadambas"')
rep_in_card("GS1-HIST-0035", "intro", 
    "The Golden period of Indian art & culture — the 3rd to 6th century CE, with patronage to Hindus (H), Buddhists (B) and Jains (J).",
    'The Gupta "golden age" (3rd to 6th century CE) had powerful contemporaries — the Vakatakas, Ikshvakus, Kalabhras, Gangas and Kadambas — who carried its artistic impulse into the Deccan and the south.')
rep_in_card("GS1-HIST-0035", "examples",
    """- Architecture, caves — North: Ajanta, Ellora, Bagh (MP — Rang Mahal), Udaygiri (Vidisha — Varaha), Junagarh (Buddhist); South: Badami (KN), Vijayawada (AP); East: Guntupalli, Anakapalle (AP). Traveller — Hiuen Tsang.
- Sculpture — Bronzes: Sarnath Sultanganj, Dhanesar Khera (Mathura style); Stone: Varaha (Udaygiri).
- Pillars — Mehrauli, Prayag Prashasti, Bhitari Pillar.
- Numismatics — Samudragupta: 8 types of coins (Veena, Saraswati), gold, silver and copper.
- Literature — Nagari script; Prayag Prashasti by Harisena (chaste sanskrit); Kalidasa, Visakhadatta, Sudraka; the Panchatantra by Vishnu Sharma; the Puranas and epics completed; Aryabhata — Surya Siddhanta.""",
    """- **Vakatakas** (Deccan, 3rd-5th CE): patrons of the **Ajanta caves** (Mahayana phase, 5th CE); sculptures in the **Amravati style** (Ex: Poophnar, MH).
- **Ikshvakus** (Andhra, 3rd-4th CE): **Nagarjunakonda** — stupas and monasteries; patronised both Hinayana and Mahayana Buddhism.
- **Kalabhras** (Tamil country, 3rd-7th CE): uprooted the Chera-Chola-Pandya rulers; their rule saw **Buddhism and Jainism** flourish in the Tamil land.
- **Western Gangas** (Karnataka, 4th-10th CE): patrons of **Jainism** — the **Gomateshwara (Bahubali) monolith at Shravanabelagola** (c. 983 CE, erected by the minister Chamundaraya).
- **Kadambas** (Banavasi, KN, 4th-6th CE): the first Kannada kingdom (founder **Mayurasharma**); the Madhukeshwara temple at Banavasi.""")
rep_in_card("GS1-HIST-0035", "conclusion",
    "- Template: Ajanta — Paintings: the flying Apsara, the Begging bowl, Padmapani; Sculpture: Mahaparinirvana, Mara Vijaya. Ellora — 34-HBJ; Cave 10 — Vishwakarma; Cave 16 — Kailashnath — Rashtrakutas.",
    "Regional patronage kept the Gupta template alive beyond the Gupta realm — these dynasties seeded the Deccan and southern schools that later flowered into the Pallava, Chola and Hoysala styles.")
rep_in_card("GS1-HIST-0035", "flags", "flags: [truncated]", "flags: []")
rep_in_card("GS1-HIST-0035", "status", "status: needs_review", "status: polished")

# ---------- 0073 data rebuild (1857 facts) ----------
rep_in_card("GS1-HIST-0073", "data",
    """- **Rule through:** the land revenue system — Ryotwari, Mahalwari, Zamindari (R, M, Z).
- **Brain Drain:** Education, Admin, Press.
- **New Acts.**
- **Opposition to INC:** the Muslim League, the Princely states, and others.""",
    """- **Causes:**
  - Political — the Doctrine of Lapse (Satara 1848, Jhansi 1853) and the annexation of Awadh (1856).
  - Economic — land revenue pressure, deindustrialisation, loss of patronage.
  - Socio-religious — reform laws and missionary activity seen as interference.
  - Military — sepoy grievances; the General Service Enlistment Act (1856).
  - Immediate — the greased cartridges; **Mangal Pandey** (Barrackpore, March 1857); the Meerut outbreak (10 May 1857).
- **Centres & leaders:**
  - Delhi — Bahadur Shah II (General Bakht Khan).
  - Kanpur — Nana Saheb and Tantia Tope.
  - Lucknow — Begum Hazrat Mahal.
  - Jhansi — Rani Lakshmibai.
  - Jagdishpur (Bihar) — Kunwar Singh.
  - Faizabad — Maulvi Ahmadullah Shah.
- **Suppression & aftermath:** Delhi fell (September 1857); Bahadur Shah II was exiled to Rangoon; the **GoI Act 1858** ended Company rule; the **Queen's Proclamation (1858)**; the army was reorganised.""")

# ---------- 0011 regional styles + own conclusion ----------
rep_in_card("GS2-POLI-0183", "guard", "Meghachandra Case", "Meghachandra Case")  # no-op
rep_in_card("GS1-HIST-0011", "data add",
    "- **Shahjahan:** the Red Fort, Jama Masjid, Shahjanabad, the Peacock Throne.",
    """- **Shahjahan:** the Red Fort, Jama Masjid, Shahjanabad, the Peacock Throne.
- **Regional styles:** Sikh — chattris, brass-copper decorations (the Golden Temple); Rajput — hanging balconies, arched cornices (Hawa Mahal, Jaipur).""")
rep_in_card("GS1-HIST-0011", "conclusion",
    """- A living proof of the harmonious blend of **cultural diversity & artistic ingenuity** that shaped India's architectural landscape.
- Adaptation to local traditions — temple elements like the **bell & chain, lotus, lintels in mihrabs, toranas**.""",
    """- The Mughal style — Persian symmetry married to Indian craft — peaked in Shahjahan's white-marble phase (the **Taj Mahal**).
- Its vocabulary passed into the Sikh and Rajput schools: Mughal architecture became the foundation of India's medieval architectural identity.""")
rep_in_card("GS1-HIST-0011", "flags", "flags: [same_as_above]", "flags: []")
rep_in_card("GS1-HIST-0011", "status", "status: needs_review", "status: polished")

# ---------- 0243 Cyber Crimes intro ----------
rep_in_card("GS2-GOVE-0243", "intro",
    "Data means information that is stored in digital format in a computer or network.",
    "Cyber crimes are unlawful acts committed using computers and networks — phishing, identity theft, ransomware, online financial fraud and cyberstalking. The **IT Act, 2000** (amended 2008) is the governing law; **I4C** coordinates the response.")

# ---------- 0044 Acts intro ----------
rep_in_card("GS1-HIST-0044", "intro", "(No specific intro provided).",
    "Every Act was a concession wrested under pressure — each widened Indian participation a little while keeping final power with the British. Nationalists judged each one unsparing:")

# ---------- 0075 socio-religious reform intro ----------
rep_in_card("GS1-HIST-0075", "intro", "(No specific intro provided).",
    "The 19th-century reforms (Brahmo Samaj, Prarthana Samaj, Arya Samaj, the Aligarh Movement, the Ramakrishna Mission) attacked superstition, caste rigidity and gender injustice while reviving what was rational and humane in tradition — modernising India without westernising it.")
rep_in_card("GS1-HIST-0075", "status", "status: untouched", "status: polished")

# ---------- 0172 hate speech intro ----------
rep_in_card("GS2-POLI-0172", "intro", "(Introductory definition to be added from notes)",
    "Hate speech has **no formal legal definition** in India. In practice it means expression that incites violence or spreads hatred against a group on grounds of religion, race, caste, community or sex. The law scatters it across IPC **153A, 295A and 505**; the **Law Commission (267th Report)** has recommended adding specific offences.")
rep_in_card("GS2-POLI-0172", "flags", "flags: [placeholder_blank]", "flags: []")
rep_in_card("GS2-POLI-0172", "status", "status: needs_review", "status: polished")

# ---------- 0264 schemes framework ----------
rep_in_card("GS2-GOVE-0264", "data", "- (Scheme-specific)",
    "- **Universal evaluation path:** beneficiary identification -> formulation -> capacity (3F) -> implementation -> monitoring (the detail block below is the checklist).")
rep_in_card("GS2-GOVE-0264", "conclusion", "(Use scheme-specific conclusions + SDG references from Social Justice section)",
    "A scheme is judged by outcomes, not outlays — convergence, last-mile delivery and honest monitoring turn allocations into impact on the ground.")
rep_in_card("GS2-GOVE-0264", "status", "status: needs_review", "status: polished")

# ---------- 0279 education intro ----------
rep_in_card("GS2-SOCI-0279", "intro", "(To be filled)",
    "Education is the engine of social mobility and human capital. The **NEP 2020** — its 5+3+3+4 design, foundational literacy-numeracy (NIPUN Bharat) and a **6% of GDP** public-spending goal — anchors the reform agenda.")
rep_in_card("GS2-SOCI-0279", "status", "status: needs_review", "status: polished")

# ---------- 0280 health intro ----------
rep_in_card("GS2-SOCI-0280", "intro", "(Sector-specific data to be added)",
    "Health underpins human capital. The **NHP 2017** targets **2.5% of GDP** public health spending, and **Ayushman Bharat** pairs **PM-JAY** coverage with Health & Wellness Centres for primary care.")
rep_in_card("GS2-SOCI-0280", "flags", "flags: [placeholder_blank]", "flags: []")
rep_in_card("GS2-SOCI-0280", "status", "status: needs_review", "status: polished")

# ---------- 0284 social justice framework ----------
rep_in_card("GS2-SOCI-0284", "intro",
    """- **Data** (sector specific).
- **O ACS:** Voice, Choice.""",
    """- **Structure:** one humanising statistic -> the vulnerability defined -> the constitutional vision (Art. 38, 46) -> scheme performance -> way forward.
- **Voice & choice:** citizens' voice and choice — feedback, social audits and exit options — keep services accountable.""")
rep_in_card("GS2-SOCI-0284", "data", "- (Sector-specific)",
    "- **Universal anchors to pick from:** MPI headcount, female LFPR, out-of-school children, out-of-pocket health expenditure — use the one that fits the question.")
rep_in_card("GS2-SOCI-0284", "status", "status: needs_review", "status: polished")

# ---------- 0292 vulnerable sections intro ----------
rep_in_card("GS2-SOCI-0292", "intro", "(Sector and scheme specific)",
    "Welfare succeeds when it moves from outlay to outcome — with the participation of the vulnerable, not just provisioning for them.")
rep_in_card("GS2-SOCI-0292", "status", "status: needs_review", "status: polished")

# ---------- 0296 economic diplomacy ----------
rep_in_card("GS2-INTE-0296", "intro line",
    "- Using **____ diplomacy** enables use of expertise in the **____** field to advance the country's **strategic interest**.",
    "- In practice it spans **trade, energy, science & technology and development-partnership diplomacy** — each converts expertise abroad into strategic advantage at home.")
rep_in_card("GS2-INTE-0296", "flags", "flags: [placeholder_blank]", "flags: []")
rep_in_card("GS2-INTE-0296", "status", "status: needs_review", "status: polished")

# ---------- 0414 / 0424 / 0509 / 0529 / 0531 ----------
rep_in_card("GS3-SCIE-0414", "conclusion", "(No specific conclusion provided — same template as Aditya L1)",
    "Gaganyaan is capability-building as much as spaceflight — a human-rated launch vehicle, crew-escape and life-support systems built at home, with spillovers into materials, medicine and robotics, and the road ahead to the **Bharatiya Antariksh Station (2035)** and an Indian on the **Moon (2040)**.")
rep_in_card("GS3-SCIE-0414", "status", "status: needs_review", "status: polished")
rep_in_card("GS3-SCIE-0424", "conclusion", "(No specific conclusion provided — refer general S&T template)",
    "Indigenous cryogenics was born of technology denial in the 1990s and proved itself with **GSLV-D5 (2014)**; today it powers heavy-lift launches, and its applications reach MRI, cryosurgery and food preservation — denial turned into capability.")
rep_in_card("GS3-SCIE-0424", "status", "status: needs_review", "status: polished")
rep_in_card("GS3-INTE-0509", "conclusion", "Template — this **war is not any one agency's or one government's alone**.",
    "The crime-terror nexus is one war on many fronts: intelligence fusion, financial chokepoints (**PMLA**, **FATF** standards), global cooperation (**UNTOC**) and development in the war economy's catchments — all stakeholders, one platform.")
rep_in_card("GS3-INTE-0509", "status", "status: needs_review", "status: polished")
rep_in_card("GS3-INTE-0529", "guterres pointer", "- Antonio Guterres quote on underdevelopment.",
    '- "Poverty, inequalities and social exclusion give terrorism fuel." — Antonio Guterres')
rep_in_card("GS3-INTE-0531", "guterres pointer", "- Antonio Guterres quote on underdevelopment and inequality fits here.",
    '- "A more secure world begins by investing at least as much in fighting poverty as we do in fighting wars." — Antonio Guterres')

# ---------- 0154 intro indent ----------
rep("0154 indent",
    """- Studying ocean temperature matters because it explains
- how ocean currents move
- which marine organisms live at various depths, and how they are spread
- the climate of coastal areas""",
    """- Studying ocean temperature matters because it explains
  - how ocean currents move
  - which marine organisms live at various depths, and how they are spread
  - the climate of coastal areas""")

# ---------- stray quote punctuation (period inside closing quote) ----------
rep("0561 IPS wife", '- "Eg. case of **IPS beating his wife**. (MP)".', '- "Eg. case of **IPS beating his wife** (MP)."')
rep("0561 adherence", '- "**Adherence to laws** may not be followed in **private sphere of life**.".',
    '- "**Adherence to laws** may not be followed in **private sphere of life**."')
rep("0581 churchill", "are created, strengthened and maintained'\".", "are created, strengthened and maintained'.\"")
rep("0581+0582 plato", "is **cultivated there**'.\".", "is **cultivated there**'.\"")
rep("0603 prabhat", "arrested his son involved in liquor smuggling.\".", "arrested his son involved in liquor smuggling.\"")
rep("0603+0605 pankaj", "sent his daughter to local Anganwadi, instead of private school.\".", "sent his daughter to local Anganwadi, instead of private school.\"")
rep("0638 divya", "to **solve their concerns**.\".", "to **solve their concerns**.\"")
rep("0638 EI", '- "EI enables one to be empathetic and solve the problem constructively".', '- "EI enables one to be empathetic and solve the problem constructively."')
rep("0740 hyderabad", "when electricity/water supplies are cut.\".", "when electricity/water supplies are cut.\"")
rep("0743 annan", "transparency is the best treatment available!'\".", "transparency is the best treatment available!'\"")
rep("0743+0744 rti", "received **MGNREGA** wages without working.\".", "received **MGNREGA** wages without working.\"")
rep("0744 further", "- \"Further, when public asks for information, **corruption** cannot continue any further.\".",
    "- \"Further, when public asks for information, **corruption** cannot continue any further.\"")
rep("0759 social audit", "30,000 government officials involved in **corruption**.\".", "30,000 government officials involved in **corruption**.\"")
rep("0766 LG Polymers", "leading to leakage and harming its growth potential by harming public\".", "leading to leakage and harming its growth potential by harming public.\"")
rep("0766+0767 satyam", "fudging by Satyam computers led to closure of the company.\".", "fudging by Satyam computers led to closure of the company.\"")
rep("0771 vaccine", "question the ethicality of vaccine passports.\".", "question the ethicality of vaccine passports.\"")
rep("0787 marital rape", "'A rapist is a rapist regardless of his relationship with the victim!'\".", "'A rapist is a rapist regardless of his relationship with the victim!'\"")

if fails:
    print(f"FAILED {len(fails)}:")
    for f in fails: print(" ", f)
    sys.exit(1)
open(PATH, "w", encoding="utf-8", newline="").write(text)
print("OK - all C10b operations applied")
