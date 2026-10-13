import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS1-HIST-%04d' % i] = (status, blocks)

card(1, 'polished',
 introduction="Bhakti and Sufi literature made religion democratic — love and personal devotion came before ritual. Singing in regional languages and images, the saints bound society across caste and creed.",
 examples="- The **Sant Kabir Akademi** was set up under the Scheme for Promotion of Culture of Saints.\n"
 "- **Sufi literature festivals** in **Rajasthan** built cultural harmony.",
 conclusion="Their teachings still speak to today's fractured socio-religious landscape, pointing the way to inclusive nationalism.")

card(2, 'polished',
 introduction="- **Bhakti:** a theistic devotional trend from medieval India that later **revolutionised society** — South India from the 7th-12th CE, then North India from the 15th CE.\n"
 "- **Sufi:** the Sufi movement of medieval India — a **spiritual and inclusive Islamic tradition** stressing divine love, tolerance, and inner spiritual experience.",
 data="- **Bhakti:**\n"
 "  - 1. South — the Alvar and Nayanar saints.\n"
 "  - 2. North — the Nirguna and Saguna streams.\n"
 "  - Features: a personal bond and salvation through intense loving devotion; universalism; opposition to rituals; no caste or gender discrimination; the need for a true Guru.\n"
 "  - Method: poetry, song, dance; kirtan (naam japna — Nanak — \"sangat pangat\").\n"
 "  - Women:\n"
 "    - Rajasthan: **Mirabai** (spoke against infanticide and sati)\n"
 "    - Tamil Nadu: **Andal Alvar** (contributed to the Divyaprabandham)\n"
 "    - Karnataka: **Akka Mahadevi** (Veershaivite — the soul has no gender)\n"
 "    - Jammu and Kashmir: **Lal Dedh** (Kashmiri Shaivite)\n"
 "    - Maharashtra: **Janabai** (Abhangs on Vithoba)\n"
 "  - Examples: **Guru Nanak** (PB), **JNET** (MH, Abhang), **Surdas** (Krishna — Sursagar), **Vallabhacharya** (UP, Pushti Marg), **Shankardev** (AS, Bhaona), **Basavanna** (KN, Vachanas in Kannada), **Chaitanya Mahaprabhu** (WB). Saints like **Kabir, Namdev, and Sheikh Farid** promoted inter-religious harmony.\n"
 "- **Sufi:**\n"
 "  - Wahadat-al-Wajud — the oneness of existence and humanity.\n"
 "  - Union with God; a spirit of tolerance and brotherhood; unity of religions.\n"
 "  - Rejected elaborate rituals. Pir Murshidi.\n"
 "  - Silsilas: Chisti, Suhrawardi, Nakshbandi.\n"
 "  - The **Dargah of Khwaja Moinuddin Chishti** in Ajmer — a centre of communal harmony.\n"
 "  - Qawwali music — Sama.\n"
 "  - Ishq — divine love.\n"
 "  - Sufi Khanqahs — centres of learning and education.\n"
 "  - Sufi poets like **Amir Khusro** enriched Indian languages by blending Persian with local vernaculars.",
 conclusion="- The principles of the Bhakti movement answer today's religious polarisation and caste and gender divides with **universal brotherhood, love and equality**.\n"
 "- They promoted a spirituality of universal love and harmony that still shows — ISKCON kirtans (Chaitanya Mahaprabhu), the Ankia Naat of Shankardev, the Warkaris of Maharashtra, the practice of langar, Sufi spiritual music, and visits to Sufi shrines by people of all faiths.")

card(3, 'polished',
 introduction="Buddhism arose **2600 years ago** (600–400 BC) from the teachings of **Siddharta Gautama** — a **heterodox tradition** built on the **middle path for salvation**.",
 data="- **Sites:**\n"
 "  - **Stupas:** Sanchi, Amravati\n"
 "  - **Temples:** Gaya Mahabodhi\n"
 "  - **Monasteries:** Aichi Ladakh, Namdroling (KN), Tawang, Rumtek, Ghum\n"
 "  - **Caves:** Ajanta, Ellora, Nashik, Karle\n"
 "- **Buddha's life:** Sarnath, Kushinagar, Gaya\n"
 "- **Literature:** Tripitak, Jatakas, Milinda Panho",
 conclusion="**Dukkha, Samudaya, Nirodha, Ashtangamarga Madhyamarga**.")

card(4, 'polished',
 introduction="From Harappa's urban planning to Gupta cave shrines and Nagara-Dravida temples, ancient Indian architecture joined material sophistication with spiritual imagination, shaping the aesthetics of a civilisation.",
 examples="- The **Rakhigarhi Museum** and a Harappan gallery by the **Archaeological Survey of India**.\n"
 "- The **PRASAD** scheme has revived ancient temple sites such as **Srisailam** and **Mahakaleshwar**.",
 conclusion="When ancient sites are preserved through archaeology and tourism, India's roots keep feeding its modern identity.")

card(5, 'polished',
 introduction="The time before written records — the **Paleolithic, Mesolithic, Neolithic** ages.",
 data="- **Map/Locations:**\n"
 "  - Jogimara (Chhattisgarh)\n"
 "  - Bhimbetka, Lakhudiyar (Vindhyas, Madhya Pradesh)\n"
 "  - Andhra Pradesh — Kurnool\n"
 "  - Karnataka — Piklihal, Taklakota\n"
 "  - Telangana — Kupgallu\n"
 "- **Discovery:** **1957-58**, by **V K Vakankar**.\n"
 "- **Importance:**\n"
 "  - harmony between man and nature\n"
 "  - beliefs, rituals, dances\n"
 "  - the evolution of family ties\n"
 "  - technology — paintings, tools\n"
 "  - tribal cultures",
 conclusion="The prehistoric period gives precious insight into how human civilisation began and grew, shaping the **course of human history**.")

card(6, 'polished',
 introduction="The **Harappan civilisation**, a Bronze-age culture (**2700 - 1900 BC**), was an **advanced urban civilisation** in city planning, trade and craftsmanship.",
 data="- **Artifacts:**\n"
 "  - Seals — Pasupati, unicorn\n"
 "  - Bronzes — the Dancing girl, lost-wax casting\n"
 "  - Terracotta — the Bearded priest, mother goddess (pinching method)\n"
 "  - Pottery, ornaments, spindles, toys\n"
 "  - Shell factory at **Lothal**\n"
 "- **Speciality:**\n"
 "  - Burnt bricks, grid planning, advanced drainage\n"
 "  - Grain storage\n"
 "  - Trade links (Dilmun, Mesopotamian seals)\n"
 "  - Flood-proofing\n"
 "  - Water harvesting (**Dholavira**)",
 conclusion="- The lessons the Harappan civilisation offers on **city planning, trade, and resilience** deserve study and application, above all for sustainable urban development (**SDG 11**).\n"
 "- The recent **UNESCO world heritage status to Dholavira** underlines its significance.")

card(7, 'polished',
 introduction="From colonial Indo-Gothic to **Charles Correa's** post-colonial works, modern Indian architecture tracks the move from imperial order to democratic imagination.",
 examples="- The **Central Vista Redevelopment Project** carries new architectural symbolism.\n"
 "- **INTACH** conserves colonial and early-modern urban heritage zones.",
 conclusion="Modern architecture must weigh innovation against contextual heritage, serving both utility and national ethos. II. Modern Indian History (Mid-18th Century to Present)")

card(8, 'polished',
 introduction="- It reflects the country's **rich history, & cultural diversity**.\n"
 "- It gathers **diverse influences & traditions** into one whole.",
 data="- **Awareness:** GI Tag, **SPICMACAY**, **ICCR**, curriculum — **NEP 2020**.\n"
 "- **Exchanges:** **Ek Bharat Shreshtha Bharat**, **Kashi Tamil Sangamam**.\n"
 "- **Leverage:** Cultural Tourism circuits, **ODOP**, **Swadesh Darshan**.\n"
 "- **Tech:** VR, metaverse.\n"
 "- **Maintenance:** **Adarsh Smarak**, **HRIDAY**, **Monument Mitra**, **PRASAD**, Adopt a Heritage programme, **CSR**.\n"
 "- **Institutions:** the recently set up **Indian Institute of Heritage (IIH)**; Documenting and capacity building of **ASI**; Tribal museums.\n"
 "- **Other:** Art 49, NFT, Modern Architecture (Parliament building, statues).\n"
 "- **TEMPLATE (MAD LiPS):**\n"
 "  - Music\n"
 "  - Architecture\n"
 "  - Dance, Drama\n"
 "  - Literature, language & coins\n"
 "  - Paintings\n"
 "  - Sculpture",
 conclusion="- The newly announced **PM Vishwakarma Kaushal Samman scheme (PM VIKAS)** supports traditional artisans. It can go a long way in preserving this rich cultural heritage.\n"
 "- **PM Modi** stresses harnessing heritage for development.\n"
 "- Under **Art 51A of Constitution**, valuing and preserving this rich heritage of our composite culture is now a **fundamental duty**.\n"
 "- The recently created **National Digital District Repositories** can also document, preserve and promote our rich cultural heritage.\n"
 "- As **G20 president**, India must engage through the **G20 culture minister's working group** to promote and exhibit India's rich cultural heritage.\n"
 "- Even today, the contributions of this period act as a bridge between past and present, and a powerful medium of creative and narrative expression.")

card(9, 'polished',
 introduction="Temples mattered not only as spiritual centres but also as hubs of **administration, learning and community life**.",
 data="- **Pallavas:**\n"
 "  - Mahendravarman: mandap\n"
 "  - Narsimha: sculpture rathas — Ex: Mahabalipuram's Panchpandav ratha & Dropadi ratha\n"
 "  - Rajsimhavarman: structural temples — Ex: the Mahabalipuram Shore temple, Kailashnath Kanchipuram\n"
 "  - Nandivarman: smaller temples — Vaikuntha Perumal (the model for Brihadeshwara)\n"
 "- **Nagara:**\n"
 "  - Ex: Deogarh, Dashavtara, Bhitargaon\n"
 "  - Odisha: the Konark Sun temple, Lingraj (no pillars, Rekhadeul & Jagmohan, lavish exteriors, Boundary wall)\n"
 "  - Khajuraho: Chandela — Kandariya Mahadev, Lakshamana, Chausath Yogini (Panchayatan, High platform, sandstone)\n"
 "- **Solanki:** the Modhera Sun temple — Surya kund, wooden carvings, torana, open mandap\n"
 "- **Dravidian:** Chola Gopuram, Panchayatana, only 1 vimana, Dwarpaal — Ex: Brihadeswar, Rajarasjeshwara\n"
 "- **Medieval Temples:**\n"
 "  - Chalukyas: Ladkhan (sloping like hills), Durg at Aihole (apsidal)\n"
 "  - Palas & Senas: Nalanda, Jagaddala, Odantapuri, Bangladesh (Bangla roofs, terracotta)\n"
 "  - Hoysala: Vesara, Jagati, Belur, Halebid, Sringeri\n"
 "- **Vijaynagar (Hampi):** combined all earlier influences with the Indo-Islamic influence of Bijapur. Gopurams on all sides, Yali, kalyana mandapa, secular buildings, large enclosing walls — Ex: the Vithalswami temple, Virupaksha at Hampi, the Lotus Mahal.\n"
 "- **Nayaka (16th-18th CE):** Islamic influence; Parakramas (huge corridors); the largest gopurams — Meenakshi, Madurai.",
 conclusion="As a spiritual capital of the world, India still nurtures its **rich tradition of temple making**, at home and abroad.")

card(10, 'polished',
 introduction="Indo-Islamic architecture is a striking fusion and synthesis of **Islamic and indigenous styles**. It began with the rise of the Delhi Sultanate in the **12th CE AD**.",
 data="- **Features:** Charbagh, foresightening, symmetry; Arcuade replaced trabeate, etc.\n"
 "- **Imperial Style:**\n"
 "  - **Slave:** the Mameluk style, remodelling Hindu buildings — Ex: Qutub minar, Adhai din ka jhopra\n"
 "  - **Khilji:** the Seljuk style — Siri fort, Alai Darwaza\n"
 "  - **Tuglaq:** batter walls, strength focus — Ex: Tughlaqabad city\n"
 "  - **Lodi:** double domes, no lavish decoration — Ex: Lodi gardens\n"
 "- **Indo Saracenic:** Indo-Islamic + Gothic — Ex: Parliament, VT, SC, St. Paul Cathedral Kolkata.\n"
 "- **Provincial style:**\n"
 "  - **Bengal:** black marble, Bangla roof — Ex: Quadam Rasul mosque\n"
 "  - **Malwa:** coloured stones, European influence, No minar, Envt adaptation — Ex: Hindola mahal, Jahaz mahal\n"
 "  - **Jaunpur:** the Sharqui style, no minars, bold characters on huge screens — Ex: Atal mosque\n"
 "  - **Bijapur:** a 3-arched facade, bulbous domes, cornices, iron clamps — Ex: Gol Gumbaz",
 conclusion="- A living proof of the harmonious blend of **cultural diversity & artistic ingenuity** that shaped India's architectural landscape.\n"
 "- Adaptation to local traditions — temple elements like the **bell & chain, lotus, lintels in mihrabs, toranas**.")

card(11, 'needs_review',
 data="- **Babur:** the Panipat & Rohilkhand mosques.\n"
 "- **Humayun:** Dinpanah city — Persian style.\n"
 "- **SherShah:** Qila e Quhunah mosque (Delhi), Rohtas fort (Pak), the G T road.\n"
 "- **Akbar:** red sandstone; new elements like the 4-centred Tudor arch.\n"
 "  - Agra fort: Moti masjid, Diwan-e-aam/khaas, Sheesh mahal.\n"
 "  - Fatehpur Sikri (Hindu + Persian): Ibadat khana, Buland darwaza, Salim Chisti Tomb, Jodha Bai palace, Panchmahal.\n"
 "- **Jehangir:** focus on painting; Akbar's tomb at Sikandra, Shalimar Bagh (Kashmir).\n"
 "- **Nur Jahan:** the Itmad ud Daula tomb — marble.\n"
 "- **Shahjahan:** the Red Fort, Jama Masjid, Shahjanabad, the Peacock Throne.")

card(12, 'polished',
 introduction="Indian paintings, steeped in tradition and artistic finesse, are a visual record of the country's **vibrant cultural, religious & historic heritage**.",
 data="- **Pre-historic:**\n"
 "  - Upper paleo: Red & Green, Big figures.\n"
 "  - Meso: small, groups, headgears, Red ochre.\n"
 "  - Chalco: battle scenes, men riding horses — Ex: Jogimara, Chitwa Dongri (CH).\n"
 "  - IVC: painted pottery.\n"
 "- **Murals (100 BC-10th CE AD, HBJ):**\n"
 "  - Ajanta — the Jatakas\n"
 "  - Ellora, Armamalai, Sittanavasal (pond with lotus, Samwasarana), Bagh, Badami\n"
 "  - Vijayanagar — Lepakshi paintings & the Veerbhadra temple\n"
 "  - Kerala murals — Padmanabhapuram palace\n"
 "- **Miniature (< 25 sq inch, 8th CE onwards):**\n"
 "  - Pala: manuscripts, lonely figures, sinuous lines\n"
 "  - Apabhramsa: Geet Govinda, Kalpasutra\n"
 "- **Sultanate:** Persian + Indian — Nimatnanama (illustrated manuscript), the Lodi Khuladar styles.\n"
 "- **Mughal:**\n"
 "  - Babur: family tree, Bizhad.\n"
 "  - Humayun: Abdus Samad, Mir Syed Ali.\n"
 "  - Akbar: karkhana/Tasvir khana, 3D calligraphy, foreshortening, court life, Hamzanama, the Tutinama painted from the Sanskrit Sukasaptai.\n"
 "  - Jehangir: decorated margins, a private workshop, flora & fauna — zebra, cock — Ustad Mansoor.\n"
 "  - Shah Jahan: artificial elements, less lively, charcoal, pencil sketch, gold & silver.\n"
 "- **Regional (RJ, South India):**\n"
 "  - Mewar: Sahibdin, Tamasha.\n"
 "  - Kishangarh: Bani Thani.\n"
 "  - Bundi: Krishna, vegetation, a colourful sky with a red ribbon.\n"
 "  - Amber-Jaipur: Dhundar.\n"
 "  - Marwar: Man Singh.\n"
 "  - Pahari:\n"
 "    - 1. Jammu Dogra — Nainsukh, Manaku.\n"
 "    - 2. Basholi-Kangra — Krishna love scenes.\n"
 "  - South: Tanjore & Mysore.\n"
 "- **Folk paintings:**\n"
 "  - Madhubani (BH)\n"
 "  - Warli (MH)\n"
 "  - Pichwai (RJ) — Nathdwara\n"
 "  - Pithoro (GJ)\n"
 "  - Phad (RJ) — scroll\n"
 "  - Manjusha (BH)\n"
 "  - Kalamkari (AP) — Srikalahasti\n"
 "  - Patachitra (OD)\n"
 "  - Patua, Kalighat — WB\n"
 "  - Thangka — NE, Ladakh",
 conclusion="- From the prehistoric period to modern folk paintings, Rangolis & digital art in the form of **NFTS** — a continuous legacy.\n"
 "- Vatsyayan's Kamasutra **Shadanga - 6 parts of poetry**.")

card(13, 'needs_review',
 introduction="- ____ reflects the country's rich history and cultural diversity.\n"
 "- ____ gathers diverse influences and traditions into one whole.\n"
 "- A period of great cultural efflorescence — its impact is still visible today.",
 data="- Use the **MAD LiPS** template to evaluate cultural facets comprehensively: **M** (Music), **A** (Architecture), **D** (Dance, Drama), **LiPS** (Literature, language & coins), **P** (Paintings), **S** (Sculpture).",
 conclusion="- Even today, the contributions of this period act as a **bridge between the past & the present** and a powerful medium of creative & narrative expression.\n"
 "- ____ continue to resonate with audiences, reminding us of the timeless bond between human creativity and the divine.\n"
 "- Under **Art 51A of Constitution**, it is now upon us as a fundamental duty to value and preserve this rich heritage of our composite culture.")

card(14, 'needs_review',
 introduction="Nalanda and Takshashila drew travellers, scholars, even statesmen from everywhere — for multidisciplinary learning and cultural exchange.",
 examples="- BH: Vikramshila, Odantapuri\n"
 "- WB: Jagaddala\n"
 "- TN: Kanchipuram\n"
 "- Sharda Peeth — POK",
 conclusion="The recent **Kashi Tamil Sangamam** celebrated the links between the 2 centres of learning.")

card(15, 'polished',
 introduction="A blend of the Kashmiri style with local adaptations like sloping roofs, plus Islamic, Buddhist, Gandhara and Gupta influences.",
 examples="- **Kashmir (Karkota & Utpala periods):**\n"
 "  - Martand — the Sun Temple.\n"
 "  - Panderthan Temple — note the attached water tank.\n"
 "  - In Srinagar: Shalimar Bagh and Jama Masjid.\n"
 "  - *Key Features:* a square-shaped layout, trefoil arches, multi-level sloping roofs, tall spires in a pagoda shape, and no domes.\n"
 "- **Himachal Pradesh (Chamba):**\n"
 "  - The Lakshana Devi Temple.\n"
 "  - Narasimha and Mahishasuramardini temples.\n"
 "  - *Key Features:* distinctive yellow-coloured metal sculptures.\n"
 "- **Uttarakhand (Kumaon):**\n"
 "  - Nagara architectural influence.\n"
 "  - At Almora, the Jageshwar Temples; at Pithoragarh, the Champavati Temple.")

card(16, 'polished',
 introduction="All things crafted by hand — for utility and for decoration. Think pottery, metal craft, embroidery/block printing, wood & leather craft, toy making, paintings, basket making, jewellery, and more.",
 examples="- **Pottery:**\n"
 "  - a craft with a long history, reaching back to the Neolithic period.\n"
 "  - *Kagzi* pottery (Alwar, Rajasthan).\n"
 "  - *Black Pottery* (Manipur).\n"
 "  - *Blue Pottery* (Jaipur, Rajasthan).\n"
 "  - *Khurja* pottery (Uttar Pradesh).\n"
 "  - *Modern initiatives:* bringing back the sustainable *Kulhad* (clay cup).\n"
 "- **Metal Craft:**\n"
 "  - *Bidriware* (Karnataka).\n"
 "  - *Dhokra* metal casting (Chhattisgarh).\n"
 "  - *Utensils:* the *Thatheras* of Jandiala Guru (Punjab) and their traditional brass and copper craft.\n"
 "- **Embroidery & Block Printing:**\n"
 "  - the many regional traditional craft techniques.")

card(17, 'polished',
 introduction="Coins are a vital source for reconstructing history — they reveal political authority, economic prosperity, metallurgical technology, and religious beliefs.",
 examples="- **Vedic Period:** *Nishka* and *Krishnala* (early gold units/metals, the move to currency).\n"
 "- **Mahajanapadas:** irregularly shaped, punch-marked coins with standard weights.\n"
 "- **Mauryas:** silver and copper coins — a systematic end to the barter system.\n"
 "- **Indo-Greeks:** the first to issue gold coins, put portraits/names of kings on them, and record exact years.\n"
 "- **Kushanas:** standard gold coins showing the rulers' portraits.\n"
 "- **Satavahanas:** mostly lead and potin (silver/copper alloy) coins; utility placed above beauty.\n"
 "- **Western Shakas (Satraps):** recorded dates of the Saka era; showed the king's head beside Buddhist Stupa motifs.\n"
 "- **Guptas:** a Hindu cultural revival; gold (*dinaras*) and silver coins. They show the King performing the Ashvamedha, playing the lute, or with Goddess Lakshmi and Sanskrit inscriptions.\n"
 "- **Mughals:** the gold *mohur* and the standard silver *rupiah* (introduced by Sher Shah Suri); Akbar's *Ilahi* coins; Jahangir's poetic couplets and portraits.\n"
 "- **Cholas:** a standing king on one side, a seated goddess on the other.")

card(18, 'polished',
 introduction="The vast inheritance of traditions, knowledge, practices & expressions handed down through generations.",
 examples="- **Core Concepts:**\n"
 "  - a living link from past to present to future.\n"
 "  - it builds inclusivity and social cohesion.\n"
 "  - it gives a strong sense of identity and ancestral inheritance.\n"
 "  - it covers living traditions, oral heritage, and traditional crafts.\n"
 "- **UNESCO Intangible Cultural Heritage List (India):**\n"
 "  - *Vedic Chanting* (oral tradition).\n"
 "  - *Ramlila* (traditional performance of the Ramayana).\n"
 "  - *Kutiyattam* (Sanskrit theatre of Kerala).\n"
 "  - *Ramman* (religious festival and ritual theatre of Garhwal).\n"
 "  - *Mudiyettu* (ritual theatre and dance drama of Kerala).\n"
 "  - *Kalbelia* (folk songs and dances of Rajasthan).\n"
 "  - *Chhau Dance* (classical/folk dance of Eastern India).\n"
 "  - *Buddhist Chanting of Ladakh* (recitation of sacred texts).\n"
 "  - *Sankirtana* (ritual singing, drumming, and dancing of Manipur).\n"
 "  - *Traditional brass and copper craft of utensil making among the Thatheras of Jandiala Guru, Punjab.*\n"
 "  - *Yoga* (ancient practice for physical and mental well-being).\n"
 "  - *Nowruz* (Persian/international New Year).\n"
 "  - *Kumbh Mela* (major sacred pilgrimage).\n"
 "- **Memory Mnemonic:**\n"
 "  - *\"PB me Yoga ke end me Kirtan me roz roz Ram Ram - chant - Mood Khud ba Khud achha Badhiya ho jata hai\"* (helps remember Punjab's Thatheras, Yoga, Sankirtana, Nowruz, Ramlila, Ramman, Chanting, Mudiyettu, Kutiyattam, Chhau, Kalbeliya).")

card(19, 'polished',
 examples="- Symbolises the religious traditions/beliefs — Ex: the ritual bath, Mother goddess, the bhakti cult\n"
 "- Assimilates the cultural diversity & multiple influences of the time — Ex: Vesara, Indo-Islamic\n"
 "- Technological/scientific advancements of the time — Ex: metallurgy — Mehrauli\n"
 "- Economic life — Ex: grandeur, gold coins from trade prosperity\n"
 "- Social life — Ex: the depiction of women, community life\n"
 "- Reflects common values — Ex: Kathakalli's good over evil, the Statue of Unity\n"
 "- Political life — Ex: kings depicted",
 conclusion="- Pluralism — Literature: the Razmnama Mahabharat, the Sirr-e- Akbar Upanishads of Dara Sikoh; Urdu — Hindi + Persian\n"
 "- Pluralism — Architecture: Indo-Islamic, with the Panchmahal, Jodha Bai Palace, the lotus-bell chain in Humayun Tomb")

card(20, 'polished',
 introduction="Rooted in sacred texts, India's classical dances now serve diplomacy. Under **Ek Bharat Shreshtha Bharat** and the **Indian Council for Cultural Relations**, heritage links with the country's rising global cultural stature.",
 examples="- **Kuchipudi** was showcased at the Shanghai cultural expo under **Azadi Ka Amrit Mahotsav**\n"
 "- **Odissi** found a place in India's pavilion at the World Tourism Expo",
 conclusion="Schemes like the **Kala Sanskriti Vikas Yojana** and art integration under **NEP 2020** hold the key to keeping traditional forms alive. They also grow India's cultural footprint worldwide.")

build('/home/z/my-project/raw_batch33.md', P,
      '/home/z/my-project/polished/GS1_HIST_batch33_cards0001-0020.md')
print('built batch 33: 20 cards')
