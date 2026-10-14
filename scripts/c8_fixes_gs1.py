# C8 fixes part A: GS-1 cards. BLOCKS = (card, block_type, label, anchor, new_text)
# TEXTS = (card, old_substring, new_substring)  - must occur exactly once in card body.

BLOCKS_A = [
(3, 'data', '', 'Milinda Panho', """- **Sacred sites:**
  - **Stupas:** Sanchi, Amravati
  - **Temples:** Gaya Mahabodhi
  - **Monasteries:** Alchi (Ladakh), Namdroling (KN), Tawang, Rumtek, Ghum
  - **Caves:** Ajanta, Ellora, Nashik, Karle
- **Life of the Buddha:** Sarnath, Kushinagar, Gaya
- **Key texts:** Tripitak, Jatakas, Milinda Panho"""),

(18, 'examples', '', 'Kumbh Mela', """- **Core Concepts:**
  - a living bridge that carries the past into the present and the future.
  - it binds society together and builds inclusion.
  - it roots people in their identity and their ancestral inheritance.
  - it spans living traditions, oral heritage, and traditional crafts.
- **UNESCO Intangible Cultural Heritage List (India):**
  - *Vedic Chanting* (oral tradition).
  - *Ramlila* (traditional performance of the Ramayana).
  - *Kutiyattam* (Sanskrit theatre of Kerala).
  - *Ramman* (religious festival and ritual theatre of Garhwal).
  - *Mudiyettu* (ritual theatre and dance drama of Kerala).
  - *Kalbelia* (folk songs and dances of Rajasthan).
  - *Chhau Dance* (classical/folk dance of Eastern India).
  - *Buddhist Chanting of Ladakh* (recitation of sacred texts).
  - *Sankirtana* (ritual singing, drumming, and dancing of Manipur).
  - *Traditional brass and copper craft of utensil making among the Thatheras of Jandiala Guru, Punjab.*
  - *Yoga* (ancient practice for physical and mental well-being).
  - *Nowruz* (Persian/international New Year).
  - *Kumbh Mela* (major sacred pilgrimage).
- **Memory Mnemonic:**
  - *"PB me Yoga ke end me Kirtan me roz roz Ram Ram - chant - Mood Khud ba Khud achha Badhiya ho jata hai"*
  - This line helps recall: Punjab's Thatheras, Yoga, Sankirtana, Nowruz, Ramlila, Ramman, Chanting, Mudiyettu, Kutiyattam, Chhau, Kalbeliya."""),

(26, 'conclusion', '', 'Empowering local theatre', """If local theatre and regional scripts get real support, the performing arts can carry constitutional values into everyday cultural life."""),

(38, 'conclusion', '', 'Sangam literature', """When Sangam literature is read, translated, and taught more widely, it strengthens regional pride and balances a history told only through Vedic texts."""),

(46, 'introduction', '', 'intellectual fervour', """From Bengal's intellectual fervour to Punjab's martyrdom, from South India's press to the Northeast's uprisings — every region added its own rhythm. Together they composed India's anthem of resistance."""),

(46, 'examples', '', 'Freedom Trail Programmes', """- **Freedom Trail Programmes** in Northeast India trace local heroes such as **Rani Gaidinliu** and **Kanaklata Barua**
- **Heritage City walks** in Tamil Nadu bring freedom-era printing presses and underground networks back into public memory"""),

(47, 'introduction', '', 'mass mobilisation', """The freedom struggle was a mass mobilisation that wove diverse sections of society together. Women stood at its centre — "History" truly became "Herstory" as their **impact on the freedom struggle** won recognition."""),

(47, 'examples', '', 'Aadi Mahotsav', """- **Documentation & Repositories:**
  - *National Digital District Repositories:* record how every section of society contributed locally to the freedom struggle.
- **Tribal Contributions & Recognition:**
  - *Birsa Munda's birth anniversary:* observed as *Adivasi Gaurav Diwas* in honour of tribal freedom fighters.
  - *Adivasi Museums & Digital Repositories:* built across districts to keep tribal history alive.
  - *Aadi Mahotsav:* a national festival that showcases tribal culture, crafts, and heritage."""),

(50, 'introduction', '', 'mass participation', """Gandhi turned politics into mass participation — from salt to the spinning wheel. India's fight became moral, inclusive, and decentralised: the freedom struggle re-made as a people's movement."""),

(52, 'introduction', '', 'elite platforms', """Beyond the elite platforms, peasants, tribals, women, and Dalits carried the struggle into forests, fields, and homes. For them, freedom became a lived, local resistance to colonial and social oppression alike."""),

(52, 'examples', '', 'Tribal Freedom Fighter Museum', """- **Tribal Freedom Fighter Museum** projects bring little-known uprisings — the **Santhal** and **Bhil** revolts, for instance — before the public
- **Mera Gaon, Mera Gaurav** records the role of women and lower-caste leaders in village archives through local storytelling"""),

(56, 'introduction', '', '12MPRO framework', """- Structure any historical analysis with the **12MPRO framework**:
- **Ideologies**: Moderates, extremists, revolutionaries, socialists, communists, liberals, conservatives.
- **International events**: the World wars, the Great Depression, the French Revolution, the Industrial Revolution.
- **M - Movements**: Swadeshi, NCM, CDM, Quit India.
- **P - Participants**: Women, intelligentsia, workers, peasants, tribals, foreigners, capitalists, Muslims, civil society.
- **R - Rule through**: the Land revenue system (Ryotwari, Mahalwari, Zamindari), Brain Drain, Education, Admin, Press, Acts.
- **O - Opposition to INC**: the Muslim League, Princely states, etc."""),

(56, 'conclusion', '', 'Article 51 A', """**Article 51 A** makes this a moral duty for every citizen: to cherish the noble ideals of the freedom struggle."""),

(72, 'introduction', '', 'Moderates laid the foundation', """In the freedom struggle, the **Moderates laid the foundation** and the **extremists built the road**. The **revolutionaries strengthened it with their blood**, and finally **Gandhi walked it with the masses** towards independence."""),

(73, 'introduction', '', 'British EIC', """Discontent with the economic, social, political and military policies of the British EIC finally exploded in **1857**. It was the **first major organised revolt** against Company rule in India."""),

(73, 'data', '', 'Brain Drain', """- **Rule through:** the land revenue system — Ryotwari, Mahalwari, Zamindari (R, M, Z).
- **Brain Drain:** Education, Admin, Press.
- **New Acts.**
- **Opposition to INC:** the Muslim League, the Princely states, and others."""),

(73, 'conclusion', '', 'S B Choudhary', """- **RC Majumdar** — the 1857 revolt was neither 1st, nor war, nor for independence.
- **V D Savarkar** — the 1st national war of independence.
- **S B Choudhary** — for over a year, different regions led a concerted struggle to eject an alien power. Nothing like it had ever been seen in Indian history before.
- **Stanley Wolpert** — more than a mutiny, less than the 1st war of independence."""),

(76, 'introduction', '', 'centralised administration', """Through regulatory and legislative acts, the British laid the base of centralised administration in India. The civil services and institutions they created shaped the future governance structure and the federal set-up."""),

(79, 'introduction', '', 'Partition trauma', """Partition trauma, refugee influx, communalism, and secessionist threats repeatedly tested India's democratic foundations — and so did the **Emergency of 1975**. Each time, the Republic survived by adapting and reaffirming its constitutional resilience."""),

(80, 'examples', '', 'SRC', """- Fresh parliamentary reports on linguistic minorities go back to **SRC** principles to answer new demands from Bundelkhand and Tamil Nadu.
- Digital linguistic atlases funded by the **Ministry of Culture** now trace dialect diversity across the Northeast and the Deccan."""),

(87, 'conclusion', '', 'Kashi Tamil Sangamam', """- Solution:
  - 1. **Cultural sensitisation**; the government's **Ek Bharat Shreshtha Bharat** programme.
  - 2. The **Kashi Tamil Sangamam**. Schedule 6 protections. Inclusive growth with participative governance. Droupadi Murmu: the 1st tribal woman President."""),

(88, 'introduction', '', 'shyness of contact', """Such communities are marked by **geographic isolation, a shy reluctance of contact, economic backwardness, primitive traits, and a distinct culture**."""),

(88, 'conclusion', '', 'Confused modernity', """- Confused modernity: technology used for sex-selective abortion; social media spread hate speech.
  Caste still decides who gets sanitation work, and matrimony websites see few inter-caste matches.
- The **Dhebar Commission (1961)**: integrate tribal knowledge and language into the curriculum. OD model."""),

(97, 'introduction', '', 'integrated and interdependent', """- Under it, economies and societies grow **ever more integrated and interdependent**.
- The world becomes a **global village without borders** — distances shrink in space and time."""),

(105, 'conclusion', '', 'urban governance', """Cities become liveable only when urban governance is strong: power must be devolved, data must inform decisions, and the urban poor must get dignity."""),

(108, 'data', '', 'ISA-OSOWOG', """- The **GIBI issue** — see the solar tariff diagram.
- **Steps taken:**
  - ISA-OSOWOG
  - PLI
  - the National Solar Mission
  - KUSUM
  - the Wind-Solar Hybrid policy
  - the National Offshore Wind Energy Policy"""),

(111, 'conclusion', '', 'vast thorium reserves', """- A balanced approach is needed — harness the potential while **safeguarding against health & security risks**.
- Given the vast thorium reserves, focused investment in R&D would speed up thorium-based generators.
  That would make India **energy secure as well as leverage export potential**."""),

(114, 'introduction', '', 'sedimentary shale', """Shale gas is **natural gas locked inside sedimentary shale rock formations**."""),

(120, 'introduction', '', 'eastern coal belts', """How India uses its natural endowments — the eastern coal belts, the biodiversity of the Western Ghats — will decide its prosperity. Resource distribution shapes economic destiny, not just geography."""),

(125, 'introduction', '', 'white gold', """**Known as white gold**, this light, highly reactive metal is prized for its electrical properties and its **vital role in battery technologies**."""),

(131, 'data', '', 'sacred groves', """- **Strategies:**
  - The 5Rs — moving from linear to circular use
  - Localised, inclusive solutions — Ex: social forestry, IWSM + agro-climatic planning
- **Tech that cuts waste & raises yield:**
  - Ex: 3D printing, precision farming
- **More from less:**
  - Ex: HYV, micro irrigation
- India's **LIFE mission + SDG 12** (both demand and supply sides matter).
- **Conservation (national + international):**
  - Restoring degraded landscapes — Ex: Bonn
  - EPR
  - Cultural wisdom — sacred groves"""),

(135, 'conclusion', '', 'oceanographic research', """The goal is protecting both lives and ecology. Sustained investment in oceanographic research is essential to **keep marine ecosystems healthy** and secure the livelihoods that depend on them."""),

(136, 'introduction', '', 'convergent plate boundaries', """- They do not occur just anywhere. Their spread is best explained by the **interplay of plate tectonics, geological features & geophysical processes** inside the earth.
- **Pacific Ring of Fire:** a large arc of active convergent plate boundaries around the Pacific Ocean.
  It is marked by **high levels of volcanic & seismic activity**."""),

(136, 'data', '', 'devastating earthquakes', """- The Pacific Ring of Fire region accounts for **almost 90% of the world's volcanoes and 81% of its most devastating earthquakes**."""),

(143, 'introduction', '', 'single supercontinent', """Proposed by **Alfred Wegener in 1912**, the CDT holds that Earth's landmasses were once joined as a **single supercontinent**. They have since drifted apart over geological time."""),

(146, 'data', '', 'major droughts', """- An inverse relation with the Indian monsoon — Ex: since 1871, **6 major droughts** trace back to it.
- **SEA forest fires**.
- **Coastal flooding in S America**.
- **Low hurricanes in the Atlantic (HP)**.
- **Tornado & hurricane in N America**."""),

(149, 'introduction', '', 'temperature, salinity', """Ocean water keeps moving — pushed by external forces like **the sun and the winds**.
It is also steered by the water's own physical traits such as **temperature and salinity**."""),

(154, 'introduction', '', 'marine organisms', """- Studying ocean temperature matters because it explains
- how ocean currents move
- which marine organisms live at various depths, and how they are spread
- the climate of coastal areas"""),
]

BLOCKS_A += [
(97, 'data', '', 'gurbani', """- **Local in global:**
  - yoga
  - bollywood
  - the diaspora celebrating its festivals abroad
  - the saree on celebrities at Cannes
  - indian cuisines winning fans abroad
- **Global in local:**
  - Hinglish
  - McDonald serving veg during navaratri
  - remakes of global films: forest gump remade as laal singh chaddha
    religion:
    - 1. E darshan.
    - 2. Live telecast of gurbani.
  - chinese lights vs diyas"""),

(97, 'conclusion', '', 'GIAN', """- Dimensions:
  - 1. Education - GIAN.
  - 2. Brain drain; economy - choice.
  - 3. SoL.
  - 4. GVC.
  - 5. Tech; women; environment - SUP.
  - 6. Invasive species.
  - 7. Bio diversity.
  - 8. Eco tourism; culture — cultural imperialism, impact on tribals and traditions, effects on the elderly."""),
]
