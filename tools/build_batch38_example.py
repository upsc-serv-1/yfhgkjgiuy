import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    pid = ('GS1-SOCI-%04d' if i <= 105 else 'GS1-GEOG-%04d') % i
    P[pid] = (status, blocks)

card(101, 'polished',
 introduction="A strong identification with, and sense of unity in, a specific geographic area. The drivers are often **common cultural, language, economic, or political factors**.",
 data="- **Map/Typologies:**\n"
 "  - Secession:\n"
 "    - 1. Greater nagalim.\n"
 "    - 2. Khalistan.\n"
 "  - Supra-state demands: the N-S divide.\n"
 "  - Inter-state disputes:\n"
 "    - 1. Belgaum.\n"
 "    - 2. Cauvery.\n"
 "  - Intra-state:\n"
 "    - 1. Vidharba.\n"
 "    - 2. Bodoland.\n"
 "  - Son-of-the soil:\n"
 "    - 1. Maharashtra.\n"
 "    - 2. Local job quotas.")

card(102, 'polished',
 introduction="The strong sense of identity and unity felt by people of a particular geographic area. It is usually rooted in **common cultural, language, economic, or political factors**.",
 examples="- Map of types\n"
 "- Secession: greater nagalim; khalistan\n"
 "- Supra-state: the N-S divide\n"
 "- Inter-state: belgaum; cauvery\n"
 "- Intra-state: vidharba; bodoland\n"
 "- Son of the soil: MH; local job quota")

card(103, 'polished',
 introduction="Indian secularism does not mean the absence of religion — it means equal respect for every faith. Where faiths intertwine, secularism is less a doctrine than a discipline of governance.",
 examples="- In the Northeast, the **Scheme for Promotion of Traditional and Indigenous Faiths** protects cultural pluralism\n"
 "- The judiciary has lately acted to protect religious freedoms and curb hate-driven laws — constitutional secularism in practice",
 conclusion="Secularism must live not only in laws but in lived experience — where every faith feels safe and no belief feels excluded.")

card(104, 'needs_review',
 introduction="India is witnessing a historic urban shift — villages aspire to become towns, cities strive for sustainability. But this urban tide brings challenges of planning, equity, and environment.",
 examples="- **PM e-Bus Sewa** brings green mobility to tier-2 and tier-3 cities, easing urban congestion and pollution\n"
 "- **Affordable Rental Housing Complexes** address migrant housing needs and slum growth",
 conclusion="Urbanisation must be driven by humane planning — cities should not just grow; they should include, breathe, and belong. Urban Governance")

card(105, 'polished',
 introduction="The **74th Constitutional Amendment** brought urban governance closer to the people. Yet real empowerment of local bodies remains uneven across India's complex urban fabric.",
 examples="- **Digital Municipal Platforms** in several states are improving tax collection and service delivery\n"
 "- Capacity-building under **AMRUT 2.0** trains urban functionaries in climate resilience and inclusive planning",
 conclusion="Strong urban governance is the foundation of liveable cities — it demands devolution, data, and dignity for the urban poor.")

card(106, 'polished',
 introduction="- The most important & abundant fossil fuel in India (**4th largest reserves**).\n"
 "- **TPPs — 42.5% of installed utility capacity (about 70% of total power generated)**.\n"
 "- The **2nd largest importer** despite the 4th largest reserves.",
 data="- **Distribution:**\n"
 "  - **Tertiary:** Rajasthan, Gujarat, Tamil Nadu, Assam\n"
 "  - **Gondwana:** the Damodar, Mahanadi, Godavari valleys\n"
 "  - **World:** China — Shanqxi; the US — Appalachian; Russia; Aust; S Af\n"
 "- **Issues:**\n"
 "  - High Ash (**20-30%**)\n"
 "  - Sulphur (**3-7%**)\n"
 "  - Techniques — open cast, rathole\n"
 "- **COP 26** — Phase down.\n"
 "- **2x more emissions than NG**. Coal India holds an **80% share**.",
 conclusion="- **JETP** for the energy transition of TPPs, along with a shift to cleaner tech like **coal gasification, CBM, CCUS**.\n"
 "- Steps: the **Natl Coal Gasification Mission — 100 MT 2030**; a Sustainable devel cell in the Coal ministry.")

card(107, 'polished',
 introduction="Renewable energy (RE), drawn from sunlight, wind, water, etc., offers an **eco-friendly alternative to fossil fuels**, adding to energy security and sustainability.",
 data="- India holds the **4th largest installed capacity of RE** in the world.\n"
 "- The **3rd largest oil importer**, with rising demand set to **2x our import bill by 2030**.\n"
 "- Decentralised Ex: Daman.\n"
 "- **Initial invt cost — 4cr/MW for coal vs 6 cr/MW for RE**. Prices are falling, so DISCOMS hesitate on LT PPAs.",
 conclusion="**Panchamrut — 50% RE, 500 GW**.")

card(108, 'polished',
 introduction="- **Solar:** an installed capacity of **60GW** against a potential of **750 GW** as per NISE.\n"
 "- **Wind:** an installed capacity of **40 GW** against a potential of **120 GW**. India is the **4th largest wind energy producer** in the world.",
 data="- The **GIBI issue**. Diagram — solar tariff.\n"
 "- **Steps:**\n"
 "  - ISA-OSOWOG\n"
 "  - PLI\n"
 "  - The Natnl Solar Mission\n"
 "  - KUSUM\n"
 "  - The Wind Solar Hybrid policy\n"
 "  - The National Offshore Wind energy policy",
 conclusion="- The task is not the govt's or one agency's alone — all stakeholders... removing barriers ex. finance, technology collaborations for **cheaper battery storage & private participation** for greater adoption.\n"
 "- The Panchamrit's **500GW RE** underscores the need for the shift.")

card(109, 'polished',
 introduction="- **CBM:** an unconventional form of natural gas found in coal deposits.\n"
 "- **Natural Gas:** the target is to raise its share to **15% by 2030** from the present **3.9% (2026)**.",
 data="- A **bridge fuel** (**6-15%**). It cuts dependence on coal & oil for energy demands (the **3rd largest energy consumer** — IEA).\n"
 "- **Distribution:**\n"
 "  - **India:** the Gulf of Kutchh & Khambhat, Mum High, K-G, Kaveri, Andaman\n"
 "  - **World:** the Gulf of Mexico, North Sea, Baltic Sea, Sakhalin, E Siberia\n"
 "- **Advantages:** pipeline access, diversified resources.\n"
 "- **Steps:**\n"
 "  - HELP — standard licensing + revenue sharing\n"
 "  - SATAT — compressed biogas for vehicles\n"
 "  - URJA Ganga\n"
 "  - The NE gas Grid\n"
 "  - An Indian Gas exchange — better price discovery",
 conclusion="- Panchamrit — cutting **carbon intensity by 45%** makes the shift necessary.\n"
 "- The **Kirit Parekh committee** — marketing & pricing freedom, GST cover, PPP for pipeline infra.")

card(110, 'polished',
 introduction="Total installed capacity stands at **533 GW (March 2026)**.",
 data="- **47.7% fossil fuels**\n"
 "- **52.3% RE incl large Hydro (271.9 GW)**\n"
 "  - 140.6 GW solar\n"
 "  - 54.6 GW wind\n"
 "- **3.9% Gas**",
 conclusion="The Central Electricity Auth — India's energy consumption is **set to double by 2040**.")

card(111, 'polished',
 introduction="- A radioactive element used as fuel in nuclear reactors to produce energy.\n"
 "- The **3-stage: PHWR, FBR, a Thorium-based breeder reactor**.",
 data="- India has only **2% of the world's Uranium reserves (import dependent) vs 25% of the world's Thorium reserves**.\n"
 "- **Distribution:**\n"
 "  - **India:** the Aravallis (RJ), the Bhima basin (KN), ML, JH — Jaduguda; AP — Pedagattu.\n"
 "- **Thorium advantages:**\n"
 "  - Proliferation x easy\n"
 "  - Safer\n"
 "  - Cheaper\n"
 "  - Less waste",
 conclusion="- A balanced approach is needed — harness the potential while **safeguarding against health & security risks**.\n"
 "- Given the vast thorium reserves, focused invt in R&D tech for expediting throium-based generators would make India **energy secure as well as leverage export potential**.")

card(112, 'polished',
 introduction="Nuclear energy is the **5th largest source of electricity** in India — **1.7% of total installed capacity (8.78 GW), contributing ~3% to generation**.",
 data="- An **NPP costs only 33-50% of a coal plant**. A reliable, high-density source that can be turned off/on any time.\n"
 "- The South Korean President recently changed energy policy to raise nuclear's share to **30% by 2030**. Japan & the UK are restarting reactors to diversify from coal and NG.\n"
 "- **Plants:**\n"
 "  - Rawatbhatta (RJ)\n"
 "  - Upcoming in Gorakhpur (HR)\n"
 "  - Kakrapar\n"
 "  - Jaitapur\n"
 "  - Kaiga\n"
 "  - Kalpakkam",
 conclusion="- Going for **small modular reactors** can help solve safety issues while ensuring energy security and sustainability.\n"
 "- Steps: India is working on **'Bhavni'** — a fully indigenous thorium-based NPP. The govt has allowed **JVs between NPCIL & PSUs**.")

card(113, 'needs_review',
 introduction="**Known as 'Liquid gold,'** it is a complex hydrocarbon resource that powers economies, fuels industries, and underpins modern life.",
 data="- **Distribution:**\n"
 "  - **India:** Barmer, Khambat, Mumbai High, the Brahmaputra valley, KG.\n"
 "  - **World:** Venezuela, Siberia, W Africa — rest same as NG.\n"
 "- **Refineries:**\n"
 "  - **Oil-field based:** Mumbai, Digboi\n"
 "  - **Market-based:** Bhatinda, Panipat, Mathura, Guwahati\n"
 "  - **Port-based:** Vyzag, Jamnagar",
 conclusion="- A transition towards cleaner alternatives.\n"
 "- Market-based benefits: **market life > oil well life**. Ancillary industries: pharma, chemicals, plastics, fert. Insulation from political instability.")

card(114, 'polished',
 introduction="It refers to **natural gas that is trapped within sedimentary shale formations**.",
 data="- **Distribution:**\n"
 "  - **India:** Rajasthan, the Vindhya basin, Cambay, KG, Kaveri, Upper Assam, the Arakan basin\n"
 "  - **World:** the Gulf of Mexico, Patagonia, Russia, Xinjiang (China), the Gulf of Carpentaria (Australia)\n"
 "- **Issues:**\n"
 "  - Water intensive\n"
 "  - Water contamination\n"
 "  - Methane leakage\n"
 "  - The guar gum price rise\n"
 "  - Land acquisition",
 conclusion="**Abundant availability** can help reduce import dependence. SDG 6. Steps: HELP.")

card(115, 'needs_review',
 introduction="RE, drawn from sunlight,",
 examples="- India is the 3rd largest",
 conclusion="“Energy is necessary for")

card(116, 'needs_review',
 introduction="An installed capacity of **60GW** against a potential of **750 GW** as per NISE. Diagram — solar tariff.",
 examples="- The **GIBI issue**.",
 conclusion="- The task is not the govt's or one agency's alone. All stakeholders… The Panchamrit's **500GW RE** underscores the need for removing barriers ex. finance, technology collaborations for **cheaper battery storage & private participation** for greater adoption.\n"
 "- **Steps:**\n"
 "  - ISA — OSOWOG\n"
 "  - PLI\n"
 "  - The Natnl Solar Mission\n"
 "  - KUSUM\n"
 "  - The Wind Solar Hybrid policy")

card(117, 'needs_review',
 introduction="An installed capacity of **40 GW** against a potential of **120 GW**. India is the **4th largest wind energy producer** in the world.",
 conclusion="- The National Offshore Wind energy policy\n"
 "- The Wind-Solar Hybrid policy — same as solar")

card(118, 'needs_review',
 introduction="An unconventional form of natural gas found in coal deposits.",
 conclusion="Panchamrit — cutting **carbon intensity by 45%** makes the shift necessary.")

card(119, 'needs_review',
 introduction="India recently set a target of raising the share to **15% by 2030** from the present **6%** — **45% met through imports**. **GAIL holds a 70% share**.",
 examples="- It cuts dependence on coal & oil for energy demands (the **3rd largest energy consumer** — IEA)\n"
 "- **India:**\n"
 "  - The Gulf of Kutchh & Khambhat, Mum High, K-G, Kaveri-Andaman\n"
 "- **World:**\n"
 "  - The Gulf of Mexico, North Sea, Baltic Sea, Sakhalin, E Siberia. Advantages: pipeline access, diversified resources",
 conclusion="- The **Kirit Parekh committee** — marketing & pricing freedom, GST cover, PPP for pipeline infra. A bridge fuel.\n"
 "- **Steps:**\n"
 "  - HELP — standard licensing + revenue sharing\n"
 "  - SATAT — compressed biogas for vehicles\n"
 "  - URJA Ganga, the NE gas Grid\n"
 "  - An Indian Gas exchange — better price discovery")

card(120, 'polished',
 introduction="India's prosperity is tied to how it harnesses its endowments — from the eastern coal belts to the Western Ghats' biodiversity. Resource distribution defines not just geography but economic destiny.",
 examples="- **District Mineral Foundation** funds are being repurposed to uplift health and education in mining-affected areas\n"
 "- **Mera Gaon Mera Gaurav** connects agricultural scientists with resource-poor farmers to optimise cropping in drought-prone belts",
 conclusion="Equitable use of natural wealth decides whether growth becomes inclusive — or stays a privilege of the well-placed.")

build('/home/z/my-project/raw_batch38.md', P,
      '/home/z/my-project/polished/GS1_SOCI-GEOG_batch38_cards0101-0120.md')
print('built batch 38: 20 cards')
