import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS1-GEOG-%04d' % i] = (status, blocks)

card(121, 'polished',
 introduction="Per the **ISFR 2021 / GFRA 2025**, India's total forest + tree cover stands at **24.62%**. The NFP 1988 target is **33%**; India ranks **9th globally** in forest area.",
 data="- Recent dilution of the **Forest Conservation Rules, 2022**.\n"
 "- **Steps:**\n"
 "  - Green India\n"
 "  - Laws — CAMPA 2016\n"
 "  - NCAVES\n"
 "  - The NAP to combat desertification\n"
 "  - NDC — a 2.5-3 billion tonne carbon sink\n"
 "- **Best Practices:**\n"
 "  - JFM — the Maldharis of Gir\n"
 "  - Eco-feminism — 111 trees for every girl child",
 conclusion="- The outdated NFP 1988 should be replaced with one in tune with the **dynamic realities of the climate & development landscape**. It should incorporate the active participation of all stakeholders — indigenous communities and experts included — for sustainable forest management.\n"
 "- Forests hold a key role in the **Panchamrut goal of net 0 by 2070**.")

card(122, 'polished',
 introduction="The **FRA 2006** seeks to recognise the rights of indigenous and forest-dwelling communities over **Jal, Jangal & Jameen**, ensuring democratic forest governance and conservation.",
 data="- **Rights:**\n"
 "  - Title\n"
 "  - Use\n"
 "  - Relief from illegal eviction & displacement\n"
 "  - Forest management rights — Article 48A\n"
 "- **Issues:**\n"
 "  - Administrative apathy\n"
 "  - The Forest Bureaucracy's unwillingness to share powers\n"
 "  - Misuse and encroachment",
 conclusion="Emulate the **BP** of the **Budaguda Gram Panchayat** (OD) — civil society roped in for community mobilisation and hand-holding. Add the use of RTI to speed up claim settlement.")

card(123, 'polished',
 introduction="- These are minerals **essential for economic dev & national security**; their lack of availability can create supply chain vulnerabilities.\n"
 "- Ex: **lithium, cobalt, tungsten, rare earth**.",
 data="- Economic potential (cutting-edge uses, low substitutability, a GVA multiplier, etc) plus supply risk.\n"
 "- **100% imports** for most of them. Ex: lithium, cobalt, nickel.\n"
 "- **Steps:**\n"
 "  - KABIL\n"
 "  - 30 identified by the expert committee under the Ministry of Mines\n"
 "  - A CoE to be set up\n"
 "- **Demand is high:**\n"
 "  - Futuristic — EV, superconductivity\n"
 "  - Strategic — nuclear, defence\n"
 "  - Envt — Wind turbines",
 conclusion="- Investing in critical minerals today is **key for securing technological sovereignty & a green transition tomorrow**.\n"
 "- Suggestions — **bilateral ties with Australia, S Africa, Canada** etc; the **MSP** (Minerals Security Partnership of USA); **PMN**; the deep Ocean mission; **resource use efficiency**.")

card(124, 'polished',
 introduction="A set of **17 metallic elements** with unique magnetic & electrochemical properties and wide-ranging applications.",
 data="- **100% import dependence for 7/12**, with no declared sources.\n"
 "- **Resource grab — the Chinese control 95%**. The extraction dilemma (envt).\n"
 "- **Steps:**\n"
 "  - IREL — given a monopoly\n"
 "  - The Mines & Minerals Amendment Act — EODB\n"
 "- Why 'rare' — the tech difficulties of extracting them from low concentrations.\n"
 "- India has **6% of reserves but produces 1% of global output**.\n"
 "- **Global distribution:** Vietnam, Brazil, China, Russia, USA, Australia.",
 conclusion="Set up an **Indian Rare Earth Mission** on the lines of the semiconductor mission, to promote exploration & self-sufficiency.")

card(125, 'polished',
 introduction="**AKA white gold**, it is a lightweight, highly reactive metal known for its electrical properties & its imp role in **battery technologies**.",
 data="- B/w 2016-2019, **forex spend on lithium imports tripled**.\n"
 "- **4 Chinese mining firms control 75% of the global market**. Envt hazards in mining.\n"
 "- **Distribution:**\n"
 "  - **World:** the AB(Boliv)C triangle; RUCCA (Russia, US, China, Canada, Aus).\n"
 "  - **India:** Mandya (KN), Reasi district (JK), RJ, ML, MP, CG, JH, BH.\n"
 "- **Steps:**\n"
 "  - KABIL\n"
 "  - PLI for batteries\n"
 "  - India is building the world's largest grid-scale storage facility, at Ladakh & Kutch.",
 conclusion="Look for alternatives — **solid state batteries, aluminium-air batteries**. Explore **hydrogen fuel cells**.")

card(126, 'needs_review',
 introduction="- A strategic mineral with a very high melting point, known for its critical role in the **manufacture of lithium-ion batteries**, electronics & various strategic applications.\n"
 "- **One of the 30 minerals** identified by the expert committee.",
 data="- **Distribution:** RUCCA, Congo (DRC), the Indian & Pacific oceans.\n"
 "- **50% Chinese control on refining**.",
 conclusion="(Same as strategic minerals).")

card(127, 'polished',
 introduction="- Minerals: naturally occurring material holding a distinct place in modern industries and energy security.\n"
 "- **PMN:** rounded rock concretions found on the ocean floor, containing valuable metals like **manganese, nickel, copper, and cobalt**.",
 data="- **Belts:**\n"
 "  - Himalayan — gold, cu, coal, lead\n"
 "  - The NW Belt (RJ) — non-ferrous: uranium, gypsum, zinc, petroleum, silver, cu\n"
 "  - Central — marble, bauxite, limestone, gemstones\n"
 "  - The NE peninsula — 90% of iron, 80% of coal\n"
 "  - The SW belt — monazite, iron\n"
 "- **Steps:** pioneer investor status in the Central Indian Ocean — a **380 mn tonne** resource potential (**10% recovered would be enough to meet energy needs for 100 years**).",
 conclusion="- In line with commitments under **SDG 12**, we must seek **responsible extraction, equitable distribution, and sustainable use of minerals**.\n"
 "- The **Deep Ocean mission**, which is developing tech for deep-sea mining, can be a game changer — but it must proceed responsibly, without damaging deep-sea ecosystems.")

card(128, 'polished',
 introduction="Such regions hold **immense promise of diverse and potentially valuable resources** that could shape global economies, ecology & geopolitics.",
 data="- **Common resources:** minerals, energy (RE — HEP + oil, gas, coal, uranium etc), water, biodiversity (reefs), forests, trade routes.\n"
 "- The **3 Ps** = politics, petroleum, protein.\n"
 "- Fisheries — marine and inland — for livelihood; tourism, etc. Plus climate change and the blue economy.\n"
 "- Ghana — gold; Angola — diamonds; uranium — the Horn of Africa.",
 conclusion="Exploiting this potential unveils not only new opportunities and challenges, but also **responsibilities on a global scale**.")

card(129, 'needs_review',
 data="- Common resources include: **minerals**, **energy** (RE, HEP, oil, gas, coal, uranium, etc.), **water**, **biodiversity** (reefs), and **forests**.\n"
 "- Key strategic factors: **trade routes**, and the **3 Ps** (politics, petroleum, protein).\n"
 "- Other elements: fisheries (marine, inland), livelihood (tourism), climate change, and the blue economy.\n"
 "- Examples: Ghana (gold), Angola (diamond), the Horn of Africa (Uranium).")

card(130, 'needs_review',
 introduction="The **FRA 2006** aims to recognise the rights of indigenous and forest-dwelling communities over **Jal, Jangal & Jameen**, ensuring democratic forest governance and conservation.",
 examples="- **Rights:**\n"
 "  - Title\n"
 "  - Use\n"
 "  - Relief from illegal eviction & displacement\n"
 "  - Forest management rights — Article 48A\n"
 "- **Issues:**\n"
 "  - Administrative apathy\n"
 "  - The Forest Bureaucracy's unwillingness to share powers\n"
 "  - Misuse — encroachment",
 conclusion="Emulate the **BP** of the **Budaguda Gram Panchayat** (OD) — civil society roped in for community mobilisation and hand-holding. Add the use of RTI to speed up claim settlement.")

card(131, 'polished',
 introduction="As per the **Global Footprint Network**, humanity's demand for resources now equals that of **1.7 Earths**.",
 data="- **Strategies:**\n"
 "  - The 5Rs — linear to circular\n"
 "  - Localised, inclusive solutions — Ex: social forestry, IWSM + agro-climatic planning\n"
 "- **Tech to reduce waste & increase yield:**\n"
 "  - Ex: 3D printing, precision farming\n"
 "- **More from less:**\n"
 "  - Ex: HYV, micro irrigation\n"
 "- India's **LIFE mission + SDG 12** (demand & supply sides both imp).\n"
 "- **Conservation (natnl + intl):**\n"
 "  - Restoring degraded landscapes — Ex: Bonn\n"
 "  - EPR\n"
 "  - Cultural wisdom — sacred groves")

card(132, 'needs_review',
 introduction="As per the **Global Footprint Network**, humanity's demand for resources is now equivalent to that of over **1.7 Earths**.",
 examples="- **Strategies** — the 5Rs: linear to circular; localised inclusive solutions — Ex: social forestry, IWSM + agro-climatic planning\n"
 "- **Tech to reduce waste & increase yield** — Ex: 3D printing, precision farming\n"
 "- **More from less** — Ex: HYV, micro irrigation\n"
 "- **Mindfulness** — LIFE\n"
 "- **Conservation (natnl + intl)** — restoring degraded landscapes (Ex: Bonn); EPR; cultural wisdom — sacred groves",
 conclusion="The environment and the economy are really two sides of the same coin — you cannot sustain the economy without caring for the environment. — Bruce Lipton. India's **LIFE mission + SDG 12** — demand & supply sides both imp.")

card(133, 'polished',
 introduction="From textile mills by rivers to IT parks in urban cores, industry follows a location logic — raw material, labour, markets, and increasingly sustainability.",
 examples="- The **PLI** (Production-Linked Incentive) scheme has realigned electronics manufacturing hubs towards semi-urban clusters\n"
 "- The **National Industrial Corridor Development Programme** is reshaping connectivity and boosting tier-2 industrial zones",
 conclusion="Location is no longer just about proximity — it is about policy support, logistics, and the sustainability outlook.")

card(134, 'polished',
 introduction="From the Himalayas' receding glaciers to Rajasthan's encroaching deserts, Earth's features are changing fast. These shifts are not just physical — they are ecological alarms demanding action.",
 examples="- The **Namami Gange Mission's** glacier-monitoring extension now tracks glacial melt rates in the Ganga's origin basins\n"
 "- The **Desertification Atlas of India** triggered targeted afforestation in over **200** drought-prone districts",
 conclusion="Preserving the Earth's natural face is not just environmental — it is existential for civilisations built around rivers, forests, and coasts.")

card(135, 'polished',
 introduction="**Geophysical phenomena** — with vigilant monitoring, innovative modelling, and cross-disciplinary collaboration, we can better predict and address these events.",
 data="- The ocean covers **71% of the planet** and holds **97% of the water** — thus a key factor in storing & transferring heat energy.",
 conclusion="The aim is safeguarding lives and ecology. Investing in oceanographic research is imperative to **safeguard marine ecosystems** and secure dependent livelihoods.")

card(136, 'polished',
 introduction="- They do not occur just anywhere. Distribution is best explained by the **interplay of plate tectonics, geological features & geophysical processes** inside the earth.\n"
 "- **Pacific Ring of Fire:** a large arc of active convergent plate boundaries surrounding the Pacific Ocean, marked by **high levels of volcanic & seismic activity**.",
 data="- **Almost 90% of the world's volcanoes and 81% of the world's most devastating earthquakes** occur in the Pacific Ring of Fire region.",
 conclusion="Understanding the distribution, coupled with monitoring, modelling and interdisciplinary work, can help us better **safeguard vulnerable communities** from its effects & reduce ecological impacts.")

card(137, 'polished',
 conclusion="**Geophysical phenomena** — through vigilant monitoring, innovative modelling, and cross-disciplinary collaboration, we can better predict and address these events, safeguarding lives and ecology.")

card(138, 'needs_review',
 introduction="They do not occur just anywhere. Distribution is best explained by the interplay of plate tectonics, geological features & geophysical...",
 examples="- **Almost 90% of the world's volcanoes and 81% of the world's most devastating earthquakes** occur in the Pacific Ring of Fire region",
 conclusion="Same as geophysical phenomena (understanding the distribution of __ coupled with monitoring, modelling, interdisciplinary — can help us...")

card(139, 'needs_review',
 introduction="A large arc of active convergent plate boundaries surrounding the Pacific Ocean, marked by high levels of volcanic & seismic activity.",
 conclusion="Same as above.")

card(140, 'polished',
 introduction="**Counter-clockwise polar cyclones** in the upper atmosphere of both poles, caused by the **LP** that keeps colder polar air confined to the poles.",
 conclusion="The polar vortex highlights the **delicate equilibrium of the earth's climatic processes** — greater scientific study is needed to understand its behaviour, anticipate disruptions, and build resilience against the challenges it may pose.")

build('/home/z/my-project/raw_batch39.md', P,
      '/home/z/my-project/polished/GS1_GEOG_batch39_cards0121-0140.md')
print('built batch 39: 20 cards')
