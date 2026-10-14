# C8 fixes part C: GS-4 blocks + all text-level (in-card substring) fixes.

BLOCKS_C = [
(637, 'introduction', '', 'emotional competencies', """Civil servants can build EI by **methodically training emotional competencies** — self-awareness, empathy, and social sensitivity. The tools: **coaching, honest feedback, and learning by doing**."""),

(639, 'examples', '', 'Wilma Rudolph', """- **Edison hired scientists** — awareness in action
- **Wilma Rudolph** — **motivation** against all odds
- **Geeta Phogat - won in 3rd round** — regulating her emotions under pressure
- **Empathy** — Kalam's team built light-weight prosthetics for patients
- **Social skill** — Anna Hazare rallied Ralegan for water harvesting"""),

(640, 'examples', '', 'Aligarh IPS', """- **Aligarh IPS story** — crowd management done with sensitivity
- **PM declared lockdown** — the tough call of lives over livelihood"""),

(651, 'detail', 'Concept', 'Mayer and Salovey', """- Mayer and Salovey's 4-branch model:
- first, Perceiving emotions
- then, **Understanding** them
- next, Using them to facilitate thought
- finally, Managing emotions"""),

(653, 'detail', 'Concept', 'Intrinsic motivation', """- Emotions working for us: they resolve stress and depression; build a Positive attitude - 'it is possible'; power **Empathy**, bonding, understanding.
  They also balance work and leisure, make us role models, and aid conflict resolution.
  Criticism becomes constructive feedback for growth; mental health stays stable; Intrinsic motivation grows.
- Us working for emotions: a poor work environment from workplace politics; communal tensions; reactionary policies; falling for propaganda; vulnerability to manipulation
- Dark side of EI: Manipulation for self interest; adding to offense; Self interest over public interest"""),

(655, 'detail', 'Concept', 'Self perception', """- At the personal level, EI rests on 5 pillars:
- knowing oneself (Self perception)
- expressing oneself (Self expression)
- relating to others (Interpersonal/ Relationship management)
- sound Decision making
- Stress management"""),

(718, 'detail', 'Concept', 'social contract', """- **Hobbes** frames the **social contract** between citizens and the state this way
- Government <-> Citizens (Powers <-> Rights)"""),

(747, 'detail', 'Concept', 'GOOD GOVERNANCE', """- The diagram traces the path: Communication, Openness, **Accountability** feed **Transparency**; **Ethical** Gov and Participative Gov follow; the destination is GOOD GOVERNANCE."""),

(749, 'introduction', '', 'behavioural norms', """**Work culture in governance is the shared values and behavioural norms that shape how public duties are performed**. It drives the **efficiency, accountability, and ethical climate** of institutions."""),
]

# (card, old_substring, new_substring) — old must occur exactly once in that card's body.
TEXTS_C = [
# --- GS-1 Section D sentence splits (list-count safe: continuations carry no dash) ---
(2, "- They promoted a spirituality of universal love and harmony that still shows — ISKCON kirtans (Chaitanya Mahaprabhu), the Ankia Naat of Shankardev, the Warkaris of Maharashtra, the practice of langar, Sufi spiritual music, and visits to Sufi shrines by people of all faiths.",
    "- Their spirituality of universal love and harmony is still visible today. It lives on in ISKCON kirtans (Chaitanya Mahaprabhu), the Ankia Naat of Shankardev, and the Warkaris of Maharashtra.\n  The practice of langar, Sufi spiritual music, and visits to Sufi shrines by people of all faiths carry the same spirit."),
(2, "- **Bhakti:** a theistic devotional trend from medieval India that later **revolutionised society** — South India from the 7th-12th CE, then North India from the 15th CE.",
    "- **Bhakti:** a theistic devotional trend from medieval India that later **revolutionised society**.\n  It rose in South India from the 7th-12th CE, then swept North India from the 15th CE."),
(2, "  - Features: a personal bond and salvation through intense loving devotion; universalism; opposition to rituals; no caste or gender discrimination; the need for a true Guru.",
    "  - Features: a personal bond and salvation through intense loving devotion; universalism; opposition to rituals.\n    No caste or gender discrimination; the need for a true Guru."),
(2, "  - Examples: **Guru Nanak** (PB), **JNET** (MH, Abhang), **Surdas** (Krishna — Sursagar), **Vallabhacharya** (UP, Pushti Marg), **Shankardev** (AS, Bhaona), **Basavanna** (KN, Vachanas in Kannada), **Chaitanya Mahaprabhu** (WB). Saints like **Kabir, Namdev, and Sheikh Farid** promoted inter-religious harmony.",
    "  - Examples: **Guru Nanak** (PB), **JNET** (MH, Abhang), **Surdas** (Krishna — Sursagar).\n    **Vallabhacharya** (UP, Pushti Marg), **Shankardev** (AS, Bhaona), **Basavanna** (KN, Vachanas in Kannada), **Chaitanya Mahaprabhu** (WB).\n    Saints like **Kabir, Namdev, and Sheikh Farid** promoted inter-religious harmony."),
(4, "From Harappa's urban planning to Gupta cave shrines and Nagara-Dravida temples, ancient Indian architecture joined material sophistication with spiritual imagination, shaping the aesthetics of a civilisation.",
    "From Harappa's urban planning to Gupta cave shrines and Nagara-Dravida temples, ancient Indian architecture joined material sophistication with spiritual imagination. It shaped the aesthetics of a whole civilisation."),
(6, "- The lessons the Harappan civilisation offers on **city planning, trade, and resilience** deserve study and application, above all for sustainable urban development (**SDG 11**).",
    "- The lessons the Harappan civilisation offers on **city planning, trade, and resilience** deserve study and application. The fit is closest with sustainable urban development (**SDG 11**)."),
(22, "  - Folk theatre: Gujarat — Bhavai; Maharashtra — Tamasha/Lavani; Madhya Pradesh — Maach; Odisha — Daskathia; Assam — Ankianaat; Uttar Pradesh — Nautanki/Ramlila; Andhra Pradesh — Burra Katha; Karnataka — Yakshagana; Punjab — Swaang.",
     "  - Folk theatre: Gujarat — Bhavai; Maharashtra — Tamasha/Lavani; Madhya Pradesh — Maach; Odisha — Daskathia; Assam — Ankianaat.\n    Uttar Pradesh — Nautanki/Ramlila; Andhra Pradesh — Burra Katha; Karnataka — Yakshagana; Punjab — Swaang."),
(28, "Martial arts like **Kalaripayattu** and **Gatka** now sit inside the **Fit India Movement** and **Khelo India Youth Games** — heritage blending with fitness and national pride.",
     "Martial arts like **Kalaripayattu** and **Gatka** now sit inside the **Fit India Movement** and **Khelo India Youth Games**. Heritage thus blends with fitness and national pride."),
(29, "Jainism arose **2600 years ago** (600-400 BC) from the teachings of **Lord Mahavira** and the **previous 23 tirthankaras** — a heterodox tradition rooted in **non violence & self discipline** for attaining salvation.",
     "Jainism arose **2600 years ago** (600-400 BC) from the teachings of **Lord Mahavira** and the **previous 23 tirthankaras**.\nThe tradition is heterodox — rooted in **non violence & self discipline** for attaining salvation."),
(31, "Medieval architecture wove Persian, Turkish, and Indian elements together — from the **Qutub Minar** to **Humayun's Tomb** — shaping India's syncretic aesthetics in stone, calligraphy, and gardens.",
     "Medieval architecture wove Persian, Turkish, and Indian elements together — from the **Qutub Minar** to **Humayun's Tomb**. The result: India's syncretic aesthetics in stone, calligraphy, and gardens."),
(32, "The heritage of this period — the **Sarnath Capital emblem**, the **Arthashastra**, the spread of Buddhism and more — still shapes India's cultural, diplomatic and philosophical landscape.",
     "The heritage of this period still shapes India's cultural, diplomatic and philosophical landscape. Think of the **Sarnath Capital emblem**, the **Arthashastra**, and the spread of Buddhism."),
(33, "From the Mauryas' decline to the Guptas' rise (**2nd CE BC to 3rd CE AD**), the **Indo-Greeks, Shakas, Kushanas** arrived in the North, the **Satavahanas** rose in the Deccan, and the **Shungas, Kanvas** held the east.",
     "From the Mauryas' decline to the Guptas' rise (**2nd CE BC to 3rd CE AD**), new powers filled the map.\nThe **Indo-Greeks, Shakas, Kushanas** arrived in the North, the **Satavahanas** rose in the Deccan, and the **Shungas, Kanvas** held the east."),
(63, "- Under the **Subsidiary Alliance (Lord Wellesley)**, Indian rulers — those of Hyderabad and Awadh, for example — had to keep British troops and surrender foreign policy.",
     "- Under the **Subsidiary Alliance (Lord Wellesley)**, Indian rulers had to keep British troops and surrender foreign policy. Hyderabad and Awadh signed, for example."),
(65, "Colonial policy turned India from a maker of crafts into a supplier of raw material — deindustrialisation, trade imbalance, impoverishment — the seedbed of the 'Drain of Wealth' theory.",
     "Colonial policy turned India from a maker of crafts into a supplier of raw material. Deindustrialisation, trade imbalance, and impoverishment followed — the seedbed of the 'Drain of Wealth' theory."),
(111, "- Given the vast thorium reserves, focused invt in R&D tech for expediting thorium-based generators would make India **energy secure as well as leverage export potential** .",
      "- Given the vast thorium reserves, focused investment in R&D would speed up thorium-based generators.\n  That would make India **energy secure as well as leverage export potential**."),
# --- Sections B/C word swaps ---
(49, "the intellectual bedrock for the mass resistance ahead", "the intellectual foundation for the mass resistance ahead"),
(71, "Their visions still inform the democratic ethos, grassroots reform", "Their visions still inform the democratic spirit, grassroots reform"),
(100, "it can strain the nation's integrative ethos", "it can strain the nation's integrative spirit"),
(108, "- The Panchamrit's **500GW RE** underscores the need for the shift.",
      "- The Panchamrit's **500GW RE** target shows why the shift cannot wait."),
(110, "The Panchamrit's **500GW RE** underscores the need for removing barriers ex. finance, technology collaborations for **cheaper battery storage & private participation** for greater adoption.",
      "The Panchamrit's **500GW RE** target shows why barriers like finance and technology collaborations must go, for **cheaper battery storage & private participation** and greater adoption."),
(112, "The govt has allowed **JVs between NPCIL & PSUs**.", "The government has allowed **JVs between NPCIL and PSUs**."),
(125, "- B/w 2016-2019, **forex spend on lithium imports tripled**.",
      "- Between 2016 and 2019, **forex spend on lithium imports tripled**."),
(131, "- India's **LIFE mission + SDG 12** (demand & supply sides both imp).",
      "- India's **LIFE mission + SDG 12** (both demand and supply sides matter)."),
(132, "India's **LIFE mission + SDG 12** — demand & supply sides both imp.",
      "India's **LIFE mission + SDG 12** — both demand and supply sides matter."),
(150, "to unravel their intricate roles", "to unravel their many roles"),
(151, "- Studying ocean temperature is imp for understanding", "- Studying ocean temperature matters for understanding"),
(152, "Salinity plays a pivotal role in ocean-current movement", "Salinity plays a key role in ocean-current movement"),
(206, "Ministries are moving **from silos to synergy**, from the", "Ministries are moving **out of silos into coordinated action**, from the"),
(337, "(**centre-state fiscal synergy**)", "(**fiscal coordination**)"),
(538, "aims to sharpen the **synergy, operational readiness and combat edge**", "aims to sharpen the **coordination, operational readiness and combat edge**"),
(540, "It must drive **synergy, jointness and integration**, plus a cohesive", "It must drive **jointness and integration across the forces**, plus a cohesive"),
(606, "Integrity is the **cornerstone of all ethical values**", "Integrity is the **foundation of all ethical values**"),
(718, "- Govt <-> Citizens (Powers <-> Rights)", "- Government <-> Citizens (Powers <-> Rights)"),
(749, "- Citizen feedback on the **SPARSH platform** lifts the **attitudinal ethos**.",
      "- Citizen feedback on the **SPARSH platform** lifts the **service attitude**."),
]

BLOCKS_C += [
(572, 'detail', 'Concept', 'trust deficit', """- What follows when the trust deficit grows:
- Personal level: Ethical compromise; Suspicion in relationships; Loneliness and rootlessness feeding mental health disorders; Fear and paranoia.
  Emotional breakdowns follow once trust breaks.
- Societal level: Unsafe space for weak, vulnerable; Increased exploitation — workers, trafficking; Breakdown of **social contract**.
  Cooperation becomes hard even on vital issues; violence and intolerance rise."""),

(615, 'detail', 'Concept', 'confidences safe', """- Initiatives at personal level:
  a strong personal **code of ethics**; Harmony among thoughts, words and actions; Transparent and accountable conduct; Keep confidences safe.
  Set boundaries and respect them; Serve others with no expectation of rewards; Show reliability in action; Keep every commitment."""),

(618, 'detail', 'Concept', 'Life wisdom', """- **Factors of positive attitude** — happiness curriculum, mindfulness, family conditioning, communication and cooperation
- Cognitive: life and work of role models; Happiness curriculum; Mindfulness; Communication; Philosophical knowledge; Life wisdom; Skill levels.
  Add to these an attempt to look for overt and hidden benefits in every situation.
- Affective: happiness tied to duty; alignment with personal beliefs/ethics; Family conditioning
- Behavioural: past experience proving one can handle things well"""),

(627, 'detail', 'Concept', 'vote banks', """- Ways to bring them (use when a change in attitude is needed)
- Cognitive: try Internships to meet politicians; push Electoral reforms that cut the role of money and muscle power.
  Build Awakened citizens who vote on real issues, not vote banks.
  Design Curriculums that carry the good parts of domestic politics and of other countries; demand Transparency from the government.
- **Affective: Sense of duty** — **deontology**; Patriotism; As service to society — utilitarian
- Behavioural: Role models; Better incentives for ethical behaviour and stronger disincentives for unethical behaviour in politics; Engagement through youth parliament and university"""),

(717, 'detail', 'Concept', 'attachment to fruits', """- According to **Lord Krishna** in the **Bhagavad Gita**, Karma yoga is the spiritual practice of 'selfless action performed for the benefit of others'.
- Karma yoga is a path to moksha (spiritual liberation) reached through work.
- It is rightful action without attachment to fruits — a **dedication** to one's duty.
  Give one's best, and stay neutral to outcomes like success or failure.
- [**Vivekananda**'s **Karmayoga** philosophy]"""),

(739, 'introduction', '', 'procedural efficiency', """**Quality of service delivery** asks how effectively, fairly, and empathetically public goods and services reach beneficiaries. It measures both **procedural efficiency and moral inclusiveness**."""),

(752, 'detail', 'Concept', 'Weber', """- **Max Weber** lists the markers of a Bureaucratic work culture.
  1) division of work; 2) hierarchy of authority; 3) rule-based order; 4) merit-based succession; 5) top-down structure."""),
]

TEXTS_C += [
(7, "serving both utility and national ethos.", "serving both utility and the nation's cultural character."),
]
