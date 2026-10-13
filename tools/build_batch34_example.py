import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS1-HIST-%04d' % i] = (status, blocks)

card(21, 'polished',
 introduction="Folk dances carry agrarian rhythms, festivals, and social bonding. Through the **Sanskritik Mahotsav** and **Virasat Programme**, they have come back as platforms of rural pride and community-led tourism.",
 examples="- Assam put **Bihu** on stage at the G20 cultural evening\n"
 "- **Kalbelia** now sits in District Cultural Mapping via the Culture Mapping Portal",
 conclusion="Folk forms gain incentives through the **Scheme for Financial Assistance for Promotion of Art and Culture** — cultural democracy and rural economic participation follow.")

card(22, 'polished',
 introduction="- Indian music spans a vast range of **classical, devotional, popular genres**, reflecting India's deep, diverse cultural heritage.\n"
 "- Dance has 4 dimensions (diagram): **story-telling, the devotional/spiritual element, artistic expression, cultural celebration**.",
 data="- **Music:**\n"
 "  - Narad Muni introduced it.\n"
 "  - IVC: the 7-holed flute.\n"
 "  - Vedic: the Sama Veda.\n"
 "  - Later Vedic: Bharata's Natyashastra.\n"
 "  - Classification: 1. ritualistic vs narrative, 3. classical vs folk.\n"
 "  - 3 pillars: Swar, raga, Taal.\n"
 "  - Carnatic vs Hindustani — the 2 sub-genres of classical music.\n"
 "  - Folk: no hard and fast rules, diverse themes, dance-centred.\n"
 "- **Dance:**\n"
 "  - Nandikeshwara's Abhinaya Darpan — 3 elements:\n"
 "    - Nritta — dance without expression\n"
 "    - Natya — drama\n"
 "    - Nritya — dance with sentiments and emotions\n"
 "  - Music, mudras, and the guru-shishya parampara play an important role.\n"
 "  - Classical forms (Sangeet Natak Akademi): Bharatnatyam, Kuchipuri, Kathakali, Mohiniattam, Odissi, Manipuri, Kathak, Sattriya.\n"
 "  - Folk dances:\n"
 "    - 1. Rajasthan — Kalbelia, Ghoomar.\n"
 "    - 2. Gujarat — Garba.\n"
 "    - 3. Andhra Pradesh — Burakatha.\n"
 "    - 4. Karnataka — Bhoota Aradhana.\n"
 "    - 5. Punjab — Bhangra, Gidda.\n"
 "    - 6. Himachal Pradesh — Charba.\n"
 "    - 7. Madhya Pradesh — Matki.\n"
 "    - 8. Sikkim — Singhi Chaam.\n"
 "    - 9. Assam — Bihu.\n"
 "    - 10. Goa — Tarangmal.\n"
 "- **Theatre:**\n"
 "  - The Sitabena and Jogimara caves — among the world's oldest amphitheatres.\n"
 "  - Bharat Muni's Natyashastra.\n"
 "  - Folk theatre: Gujarat — Bhavai; Maharashtra — Tamasha/Lavani; Madhya Pradesh — Maach; Odisha — Daskathia; Assam — Ankianaat; Uttar Pradesh — Nautanki/Ramlila; Andhra Pradesh — Burakatha; Karnataka — Yakshagana; Punjab — Swaang.",
 conclusion="- Today classical music lives on in the **Guru Shishya parampara**, alongside western, fusion and newer forms like Indie Pop. Preserving and mainstreaming classical and folk needs **SPICMACAY, Sangeet Natak Academy**.\n"
 "- **11K dancers** created a world record performing the **Bihu dance**.")

card(23, 'needs_review',
 introduction="Same as music's 4-dimension diagram — story-telling, the devotional/spiritual element (Ex: Kathakalli, Sattriya, Mohiniattam, Rasleela), artistic expression, cultural celebration.",
 examples="- **Bharata's Natyashastra**; Mythology — the Natraja community dancing — Bhimbetka/Lakhudiyar; the Bronze dancing girl of the IVC.\n"
 "- **CLASSICAL** — Nandikeshwara's Abhinay Darpan, 3 elements: Nritta (Dance without expression), Natya (Drama), Nritya (dance with sentiments and emotions); the important role of music, mudras, guru-shishya parampara, systematised rules, etc.\n"
 "- As per the **Sangeet Natak Academy** — 8 classical forms: Bharatnatyam, Kuchipuri, Kathakali, Mohiniattam, Odissi, Manipuri, Kathak, Sattriya.",
 conclusion="- **11K dancers** created a world record performing the Bihu dance. Same as music.\n"
 "- Kalbelia — intangible heritage.\n"
 "- Folk dances: spontaneous, crude, improvised, with local elements\n"
 "- RJ — Kalbelia, Ghoomar\n"
 "- GJ — Garba\n"
 "- AP — Burakatha\n"
 "- KN — Bhoota Aradhna\n"
 "- PB — Bhangra, Gidda\n"
 "- HP — Charba\n"
 "- MP — Matki\n"
 "- SK — Singhi Chaam\n"
 "- AS — Bihu\n"
 "- Goa — Tarangmal")

card(24, 'polished',
 introduction="Indian classical music links temples, courts, and global stages. Backed by **SPIC MACAY**, the **IGNCA**, and digital archiving, it blends legacy with modern innovation and international reach.",
 examples="- **Ustad Amjad Ali Khan's** concerts appear in India–Europe cultural diplomacy\n"
 "- **Carnatic concerts** join cultural tourism circuits under **Dekho Apna Desh**",
 conclusion="Expanding the **Guru-Shishya Parampara Scheme** and using digital platforms will keep this rich sonic heritage alive in contemporary society.")

card(25, 'polished',
 introduction="Folk music keeps oral history and social memory alive. With fresh attention under **NEP 2020** and **Kala Utsav**, it now enters classrooms and cultural policy, empowering grassroots storytelling.",
 examples="- The **Manganiyars** performed at the National Teachers' Conclave\n"
 "- **Baul singers** joined India's soft power delegation to ASEAN",
 conclusion="Archiving traditions and building artist cooperatives — backed by the **Sangeet Natak Akademi** and **IGNCA** — will stop these living narratives from fading.")

card(26, 'polished',
 introduction="From **Kutiyattam** to nukkad natak, Indian theatre mixes ritual, resistance, and reform. With the **Bharat Rang Mahotsav** and the **Performing Arts Grant Scheme**, it returns as a tool for civic dialogue.",
 examples="- **NSD's** tribal theatre showcase ran in Jharkhand under its outreach initiative\n"
 "- Street plays on electoral literacy were funded under **SVEEP** (Systematic Voters' Education and Electoral Participation)",
 conclusion="Empowering local theatre and regional scripts can make the performing arts a bridge between constitutional values and cultural expression.")

card(27, 'polished',
 introduction="India's puppetry taught villages long before formal schooling arrived. Now, with a digital revival through the **Indira Gandhi National Centre for the Arts** and a place in Heritage Education programmes, it is relevant again.",
 examples="- **Tholu Bommalata** featured in AR exhibitions by the **Ministry of Culture**\n"
 "- **Kathputli** artists appeared in urban storytelling festivals across metro cities",
 conclusion="Putting puppetry into school storytelling and tourism circuits under **Ek Bharat Shreshtha Bharat** offers revival with purpose and pride.")

card(28, 'polished',
 introduction="Martial arts like **Kalaripayattu** and **Gatka** now sit inside the **Fit India Movement** and **Khelo India Youth Games** — heritage blending with fitness and national pride.",
 examples="- A **Kalaripayattu** demo opened the **Yoga Mahotsav** session\n"
 "- **Thang-Ta** joined youth skill camps under the **Sankalp Scheme** in the Northeast",
 conclusion="Promoting martial arts as sport, self-defence, and cultural pride will keep India's ancient combat wisdom alive among the young.")

card(29, 'polished',
 introduction="Jainism arose **2600 years ago** (600-400 BC) from the teachings of **Lord Mahavira** and the **previous 23 tirthankaras** — a heterodox tradition rooted in **non violence & self discipline** for attaining salvation.",
 data="- **Architecture:**\n"
 "  - 1. Decorated carvings, the chaumukh design, dome roofs, mountains of immortality/hill temples — Ex: Palitana/Shetrunjay, Sammed Shikharji, monoliths (KN)\n"
 "  - 2. Earlier rock-cut: Udaygiri (OD), Ellora, Sittanavasal\n"
 "  - 3. Rajasthan: Ranakpur, Dilwara\n"
 "  - 4. Madhya Pradesh: Khajuraho\n"
 "  - 5. Karnataka: Gomateshwara at Shravanbelgola\n"
 "  - 6. Maharashtra: Mangi Tungi",
 conclusion="- Rooted in non-violence — **ahimsa & anekantavada** — Jainism offers valuable lessons for most problems facing humanity today.\n"
 "- Forgiveness — **Samvatsari**.")

card(30, 'needs_review',
 introduction="Indian music spans a vast range of classical, devotional and popular genres, mirroring India's deep and diverse cultural heritage.",
 examples="- Narad Muni introduced music. IVC — the 7-holed flute. Vedic — the Sama Veda. Later Vedic — Bharata's Natyashastra.\n"
 "- Classification: ritualistic (Sangama) vs narrative (Jatigan); classical vs folk.\n"
 "- 3 pillars — Swar, raga, Taal. Carnatic vs Hindustani — the 2 sub-genres of classical.\n"
 "- Origin: Carnatic — the Bhakti movement; Hindustani — the Vedic period.\n"
 "- Similarities: the same 3 pillars; religious themes; 1 dominant swar in each raag; melody matters most.\n"
 "- Differences (Hindustani vs Carnatic):\n"
 "  - influence of Arabs, Persians etc. vs indigenous roots\n"
 "  - freedom to improvise — yes vs no\n"
 "  - Gharanas vs no gharanas\n"
 "  - instruments less important than vocals\n"
 "  - 6 vs 72 ragas\n"
 "  - instruments — table, sitar, sarangi vs veena, mridangam\n"
 "- Important people: Amir Khusro, Tansen vs Thyagaraja, Shyama Shastri. Hindustani genres — Dhrupad, khayal, tarana, thumri, tappa, ghazal.",
 conclusion="- Today classical coexists — in the Guru Shishya parampara and beside western, fusion and newer forms like Indie Pop. Preserving and mainstreaming classical and folk needs **SPICMACAY, Sangeet Natak Academy** etc.\n"
 "- Folk — no hard and fast rules, no Guru Shishya parampara, diverse themes, dance focus: Gujarat — Dandiya raas; Maharashtra — Powada, Lavani; Karnataka — Bhavgeete; Goa — Ovi (women's songs); West Bengal — Baulgeet; Assam — Bihugeet; Rajasthan — Maand (Rajput glory).")

card(31, 'polished',
 introduction="Medieval architecture wove Persian, Turkish, and Indian elements together — from the **Qutub Minar** to **Humayun's Tomb** — shaping India's syncretic aesthetics in stone, calligraphy, and gardens.",
 examples="- **Humayun's Tomb** restoration under the **Aga Khan Trust** and the **Ministry of Culture**\n"
 "- **Azadi Ka Amrit Mahotsav** featured 3D walks through Indo-Islamic monuments",
 conclusion="These structures record cultural confluence and deserve a place as symbols of pluralism in heritage education.")

card(32, 'polished',
 introduction="The Mauryan period — **4th to 2nd CE BC** — marked a **transformative phase in history**: a powerful empire emerged, and culture advanced.",
 data="- **Key Feature:** all polished\n"
 "- **Court Art:**\n"
 "  - **Palace:** Kumrahar (BH)\n"
 "  - **Pillars:** Lauria nandangarh (Champaran), Sarnath\n"
 "  - **Stupa:** Sanchi, Piprawaha\n"
 "  - **Edicts**\n"
 "- **Popular Art:**\n"
 "  - **Cave arch/viharas:** Barabar, Lomas Rishi\n"
 "  - **Sculptures:** the Didarganj yakshini\n"
 "  - **Pottery:** NBPW\n"
 "  - **Literature:** the Arthashastra, Mukrarakshasa, SL chronicles",
 conclusion="The heritage of this period — the **Sarnath Capital emblem**, the **Arthashastra**, the spread of Buddhism and more — still shapes India's cultural, diplomatic and philosophical landscape.")

card(33, 'polished',
 introduction="From the Mauryas' decline to the Guptas' rise (**2nd CE BC to 3rd CE AD**), the **Indo-Greeks, Shakas, Kushanas** arrived in the North, the **Satavahanas** rose in the Deccan, and the **Shungas, Kanvas** held the east.",
 data="- **Greeks:**\n"
 "  - Strategos — military governors\n"
 "  - Chronology — Megasthenes\n"
 "  - Drama — the use of curtains\n"
 "  - Sculpture, coins, trade, cities\n"
 "- **Architecture:**\n"
 "  - **Rock-cut caves:** Karle, Ajanta, Udaygiri; Khandagiri (OD) — Kharavela.\n"
 "  - **Stupas:** Amravati, Bharhut, Sanchi (Shungas — the Torana).\n"
 "- **Sculpture:**\n"
 "  - **Gandhara (Greco-Buddhist):** the Bamiyan Buddha, Bodhisattvas in different mudras.\n"
 "  - **Amravati:** narrative art — the Buddha taming the elephant.\n"
 "  - **Mathura (HBJ):** the Jain Sarvatobhadra, Vima Kadphises, the Sarnath standing Buddha.\n"
 "- **Literature:**\n"
 "  - **Kushanas:** Vatsyayana's Kamasutra, Ashvaghosha's Buddhacharitra.\n"
 "  - **Shungas:** Panini's Ashtadhyayi, Patanjali's Yogasutra.",
 conclusion="- Template: **Greek vs Roman**.\n"
 "- Greek — strength, muscular, idealistic, marble-based, Gods shown.\n"
 "- Roman — realism, concrete, ornamentation & decoration, real events & people shown.")

card(34, 'polished',
 introduction="The **Golden period** of Indian art & culture — the 3rd & 6th CE AD, with patronage to Hindus (H), Buddhists (B) and Jains (J).",
 data="- **Architecture:**\n"
 "  - **Caves (North):** Ajanta, Ellora, Bagh (MP — Rang Mahal), Udaygiri (Vidisha — Varaha), Junagarh (Buddhist).\n"
 "  - **Caves (South):** Badami (KN), Vijaywada (AP).\n"
 "  - **Caves (East):** Guntupalli, Ankapallee (AP).\n"
 "  - **Traveller:** Huein Tsang.\n"
 "- **Sculpture:**\n"
 "  - **Bronzes:** Sarnath Sultanganj, Dhanesar Khera — Mathura style.\n"
 "  - **Stone:** Varaha (Udaygiri).\n"
 "  - **Pillars:** Mehrauli, Prayag Prashasti, Bhitari Pillar.\n"
 "- **Numismatics:**\n"
 "  - Samudragupta — 8 types of coins (Veena, Saraswati), gold, silver and copper.\n"
 "- **Literature:**\n"
 "  - Nagari script\n"
 "  - Prayag Prashasti by Harisen (chaste sanskrit)\n"
 "  - Kalidas, Vishakhadutta, Sudraka\n"
 "  - Panchatantra — Vishnu Sharma\n"
 "  - Puranas, epics completed\n"
 "  - Aryabhatt — Surya Siddhantika",
 conclusion="- Template: **Ajanta** — Paintings: the flying Apsara, the Begging bowl, Padmapani; Sculpture: Mahaparinirvana, Mara Vijaya.\n"
 "- **Ellora** — 34-HBJ. Cave 10 — Vishwakarma; Cave 16 — Kailashnath — Rashtrakutas.")

card(35, 'needs_review',
 introduction="The Golden period of Indian art & culture — the 3rd & 6th CE AD, with patronage to Hindus (H), Buddhists (B) and Jains (J).",
 examples="- Architecture, caves — North: Ajanta, Ellora, Bagh (MP — Rang Mahal), Udaygiri (Vidisha — Varaha), Junagarh (Buddhist); South: Badami (KN), Vijaywada (AP); East: Guntupalli, Ankapallee (AP). Traveller — Huein Tsang.\n"
 "- Sculpture — Bronzes: Sarnath Sultanganj, Dhanesar Khera (Mathura style); Stone: Varaha (Udaygiri).\n"
 "- Pillars — Mehrauli, Prayag Prashasti, Bhitari Pillar.\n"
 "- Numismatics — Samudragupta: 8 types of coins (Veena, Saraswati), gold, silver and copper.\n"
 "- Literature — Nagari script; Prayag Prashasti by Harisen (chaste sanskrit); Kalidas, Vishakhadutta, Sudraka; the Panchatantra by Vishnu Sharma; the Puranas and epics completed; Aryabhatt — Surya Siddhantika.",
 conclusion="- Template: Ajanta — Paintings: the flying Apsara, the Begging bowl, Padmapani; Sculpture: Mahaparinirvana, Mara Vijaya. Ellora — 34-HBJ; Cave 10 — Vishwakarma; Cave 16 — Kailashnath — Rashtrakutas.")

card(36, 'polished',
 examples="- Literature: **Harshavardhana** wrote the Nagananda, Ratnavali and Priyadarshika.")

card(37, 'polished',
 introduction="Vedic literature is the philosophical and ritual foundation of Indian civilisation. From the hymns of the Samhitas it deepened into the metaphysical inquiry of the Upanishads, shaping Indian ethics, rituals, and education.",
 examples="- **NEP 2020** encourages Sanskrit and Indic knowledge systems in curricula\n"
 "- The **Indira Gandhi National Centre for the Arts** digitised Rigveda manuscripts for public access",
 conclusion="Mainstreaming Vedic texts through digital access and curriculum reform lets ancient wisdom nurture modern minds.")

card(38, 'polished',
 introduction="Sangam literature from ancient Tamilakam gives a secular, humanist account of life, love, war, and trade. Those secular themes make it a unique non-Vedic lens on early South Indian civilisation.",
 examples="- **Keeladi excavations** tied archaeological finds to literary references\n"
 "- Sangam texts appear in the **PM Museum's** civilizational gallery on ancient India",
 conclusion="Reviving Sangam literature builds regional pride and offers a counter-narrative to Vedic-centric historiography.")

card(39, 'polished',
 introduction="Jain and Buddhist texts enriched Indian moral philosophy — Ahimsa, Dhamma, Syadvada. Their literary forms, the Tripitakas and Agamas, widened India's ethical and linguistic landscape.",
 examples="- The **Nav Nalanda Mahavihara** translated Pali texts for international students\n"
 "- The **Jain Agamas** joined the **National Mission for Manuscripts** preservation list",
 conclusion="Their ethical universality and pan-Asian reach make these texts vital to India's global soft power.")

card(40, 'polished',
 introduction="Persian flourished as India's administrative and literary language under the Delhi Sultanate and the Mughals. It produced chronicles, poetry, and translations that bridged cultures and preserved statecraft.",
 examples="- The **Ain-i-Akbari** joined the **National Archives** digitisation project\n"
 "- The **Maulana Azad Centre for Persian Studies** promotes research into Persian literary heritage",
 conclusion="Persian literature reminds us of India's cultural syncretism and needs steady academic support.")

build('/home/z/my-project/raw_batch34.md', P,
      '/home/z/my-project/polished/GS1_HIST_batch34_cards0021-0040.md')
print('built batch 34: 20 cards')
