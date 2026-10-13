import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    pid = ('GS3-ENVI-%04d' if i <= 479 else 'GS3-DISA-%04d') % i
    P[pid] = (status, blocks)

card(477, 'polished',
 introduction="- The mission's budget allocation rose **23%**.\n"
 "- **JJM** hitting its target would avert **4 lakh diarrhoea deaths** — **WHO**.",
 data="- The budget allocation saw a **23%** increase.\n"
 "- **WHO:** **4 lakh deaths** from diarrhoea are avoidable.")

card(478, 'polished',
 introduction="**Definition:** excessive plant and algal growth caused when **sunlight, CO₂ and nutrients** — the growth-limiting factors photosynthesis needs — become more available.")

card(479, 'polished',
 introduction="- **8 million tonnes** of plastic flow into the oceans every year.\n"
 "- Plastic makes up **80% of all marine debris**.\n"
 "- **Bioaccumulation and biomagnification** — microbeads have shown up in newborns' blood.\n"
 "- **Indian Efforts:**\n"
 "  - 1. Plastic Waste Management Rules 2018.\n"
 "  - 2. Kerala's **Suchitwa Mission** (fishermen collect plastic).\n"
 "  - 3. **Puneet Sagar Abhiyan**.\n"
 "- **International Efforts:**\n"
 "  - 1. **GloLitter Partnership Project**.\n"
 "  - 2. **Ocean Clean-Up**.\n"
 "  - 3. **MARPOL** by the **IMO**.\n"
 "  - 4. **SDG 14**.\n"
 "- **Cocos Keeling Island** — an example of the impact marine litter can have.",
 data="- Every year, the ocean takes in **8 million tonnes** of plastic.\n"
 "- Of all marine debris, plastic is **80%**.")

card(480, 'polished',
 introduction="- **Impact dimensions:**\n"
 "  - 1. Socio-economic.\n"
 "  - 2. Infrastructure.\n"
 "  - 3. Environment.\n"
 "  - 4. Epidemics and pandemics.\n"
 "  - 5. Psychological.\n"
 "  - 6. Political/Governance.\n"
 "- **Indian Framework:**\n"
 "  - The **DM Act** sets up a 3-tier structure:\n"
 "    - 1. **NDMA**.\n"
 "    - 2. **SDMA**.\n"
 "    - 3. **DDMA**.\n"
 "  - The **NDMP 2016** brings India in line with the **Sendai Framework**.\n"
 "  - 1. **NDRF**.\n"
 "  - 2. **National Disaster Response Fund**.\n"
 "  - 3. **National Calamity Contingent Duty**.\n"
 "- The **SENDAI Framework** — reduce 4, increase 3:\n"
 "  - Reduce:\n"
 "    - 1. Mortality.\n"
 "    - 2. Affected people.\n"
 "    - 3. Economic loss.\n"
 "    - 4. Damage to critical infrastructure.\n"
 "  - Increase:\n"
 "    - 1. Countries with **DRR** strategies.\n"
 "    - 2. International cooperation.\n"
 "    - 3. Access to multi-hazard **EWS**.\n"
 "- **Keywords:**\n"
 "  - 1. **DRR, Vulnerability mapping, Prevention and Mitigation, Emergency response, L&D, Local genius, First responders**.\n"
 "  - 2. **3R's** (Relief, Rehabilitation, Reconstruction).\n"
 "  - 3. **BBB** (Build Back Better).",
 conclusion="- **\"Disasters are inevitable, but their impact is not.\"** With robust DM, risks can be mitigated, lives saved and communities made resilient.\n"
 "- **Tehri Dam case** — **SC**: DM forms part of the **right to sustainable development**.\n"
 "- **\"Prepare and prevent, not repair and repent\"** — this should become second nature everywhere.")

card(481, 'polished',
 introduction="**IPCC Definition:** events **rare at a particular place and time**.",
 data="- **CSE Report 2022:** EWEs showed up on **241/273 days** of the year.\n"
 "- **2022** gave India its warmest, driest and wettest days.\n"
 "- **75% of districts** felt EWEs.")

card(482, 'polished',
 introduction="- 1. **Safety culture**.\n"
 "- 2. **Decentralised, pro-active, preventive, community resilience, self-sufficiency**.\n"
 "- 3. A **parallel rather than sequential approach**.\n"
 "- 4. **Equitable**.\n"
 "- **Funding:** catastrophe bonds.\n"
 "- **Resilient Infra:**\n"
 "  - 1. SDG 9.\n"
 "  - 2. **CDRI**.\n"
 "- **EWS:** the Odisha **SATARK Mobile App**.\n"
 "- **WF mnemonic — RW wants LES VAT LSD:**\n"
 "  - 1. **R** — Risk coverage.\n"
 "  - 2. **W** — Women role.\n"
 "  - 3. **L** — Leadership.\n"
 "  - 4. **E** — EWS.\n"
 "  - 5. **S** — Sendai.\n"
 "  - 6. **V** — Vulnerability mapping.\n"
 "  - 7. **A** — Academia.\n"
 "  - 8. **T** — Tech.\n"
 "  - 9. **L** — Local capacity.\n"
 "  - 10. **S** — Social media.\n"
 "  - 11. **D** — DRR.",
 data="- ROI on mitigation: **$1 → $7 saved**.",
 conclusion="- **\"Every $1 spent on mitigation saves $7 on response and recovery\"** — Sendai.\n"
 "- The **Zero Casualty Approach**.\n"
 "- **Tehri Dam Case** — **SC**: DM is part of the right to **sustainable development**.")

card(483, 'needs_review')

card(484, 'polished',
 introduction="**Definition:** a disruption on a massive scale, natural or man-made, over a short or long period. It **affects the capacity of society to cope with its own resources**.",
 data="- **30 different types of disasters** threaten India.\n"
 "- 1. EQ — **60%**.\n"
 "- 2. Cyclones — **12%**.\n"
 "- 3. Floods — **12%**.\n"
 "- 4. Drought — **68%** of the country is vulnerable.\n"
 "- **5700/7500 km** of the coastline sits in the cyclone and tsunami zone.")

card(485, 'polished',
 introduction="- **Definition:** intense rain falling over a short span — **100 mm/hour** on a small area.\n"
 "- **Best Practice:**\n"
 "  - 1. The **Copenhagen Cloudburst Formula** — **blue-green infrastructure**.\n"
 "  - 2. City planning.\n"
 "- **Hotspot:** **CNP (Cherrapunji/Northeast)** — the world's most vulnerable spot for severe thunderstorm formation.",
 data="- Intensity: **100 mm/hr** on a small area.\n"
 "- Examples:\n"
 "  - 1. UK, 2021.\n"
 "  - 2. Jammu and Kashmir, 2010.\n"
 "- Terrain at risk: mountains, deserts, interiors of landmass.")

card(486, 'polished',
 introduction="**Bomb Cyclone (Bombogenesis):** a rapidly strengthening storm in which **pressure drops 24 mb within 24 hours**.")

card(487, 'polished',
 introduction="- **Definition:**\n"
 "  - 1. Rapid inward circulation of air around a **low-pressure area** — a perennial phenomenon in India.\n"
 "  - 2. Called the **\"silent killer\"**.\n"
 "- Colour-coded warnings come from the **IMD**.\n"
 "- For cyclone preparedness, the **Odisha Model** is the best practice.\n"
 "- **RIMES** — Regional Integrated Multi-Hazard Early Warning System.\n"
 "- **Conditions:**\n"
 "  - 1. Temperature above **27°C**.\n"
 "  - 2. Coriolis force.\n"
 "  - 3. Small variation in vertical wind speed.\n"
 "  - 4. Low pressure.\n"
 "  - 5. Upper air divergence.\n"
 "- **Why the Arabian Sea sees more of them:**\n"
 "  - 1. IOD heating.\n"
 "  - 2. GHG.\n"
 "  - 3. El Niño.\n"
 "  - 4. A weakening monsoon.\n"
 "  - 5. Low wind shear due to CO₂.\n"
 "- **Multiple engagement areas:**\n"
 "  - 1. Natural storm breaks (mangroves).\n"
 "  - 2. Technology (UAV, satellite).\n"
 "  - 3. Coordination.",
 data="- **10% of the world's tropical cyclones** occur in India.\n"
 "- **13 states and UTs** feel their impact.\n"
 "- Cost to the country: **2% of GDP**.\n"
 "- Crop damage from **Cyclone Nivar**: **23,000 acres**.")

card(488, 'polished',
 introduction="**Definition:** an **abnormal rise of sea level** when a cyclone crosses the coast — the coastal strip is inundated as a result.")

card(489, 'polished',
 introduction="- **Definition:** cyclones that develop in the **middle and high latitudes (35°–65° N&S)**, beyond the tropics.\n"
 "- The **Polar Front Theory** explains them.")

card(490, 'polished',
 introduction="- **Definition:** a period of **abnormally dry weather** that causes serious **hydrological imbalances** in the area.\n"
 "- **Note:** the **DM Act** does not define it as a disaster.\n"
 "- The **Drought Crisis Management Plan 2015** exists.\n"
 "- **Government steps:**\n"
 "  - 1. MGNREGA (employment).\n"
 "  - 2. Recharging groundwater.\n"
 "  - 3. Compensation for crop loss.\n"
 "- **Schemes:**\n"
 "  - 1. PMGSY.\n"
 "  - 2. Soil Health Card.\n"
 "  - 3. **PM Fasal Bima Yojana**.\n"
 "- **4 Types:**\n"
 "  - 1. Meteorological.\n"
 "  - 2. Hydrological.\n"
 "  - 3. Agricultural.\n"
 "  - 4. Ecological.",
 data="- **70%** of the country is drought-prone.\n"
 "- Drought-like conditions prevail over **20% of India's land**.")

card(491, 'polished',
 introduction="- **Definition:** drought that sets in with a **rapid and intense onset** — over a **few weeks or months**, unlike the traditional kind. Behind it: high temperatures, reduced precipitation, low soil moisture and increased evaporation.\n"
 "- **Best Practices:**\n"
 "  - 1. The **Seechwal Model**.\n"
 "  - 2. The **Israel case study**.\n"
 "  - 3. **Agro-climatic agriculture**.",
 data="- A study warns of **more flash droughts in India by end of century**.")

card(492, 'polished',
 introduction="- **Definition:** shaking of the Earth's surface when **seismic waves** arrive after energy is suddenly released in the **Earth's crust or upper mantle**.\n"
 "- **Way Forward:** an EIA should precede mining and dam construction.\n"
 "- **Best Practices:**\n"
 "  - 1. **Bhungas (Kutch)**.\n"
 "  - 2. **Ikra Bamboo Houses (Sikkim)**.\n"
 "- **Steps:**\n"
 "  - 1. National Retrofit Program 2014.\n"
 "  - 2. National EQ Risk Mitigation Project.\n"
 "  - 3. **EQ Disaster Risk Indexing**.\n"
 "- **Best Practice (International):** Japan — **80% compliance** with quake-resistant buildings.",
 data="- Major EQs:\n"
 "  - 1. Gujarat, 2001.\n"
 "  - 2. Nepal, 2015.\n"
 "  - 3. Sikkim, 2011.\n"
 "- **60% of India's land** is vulnerable, covering **80% of population**.")

card(493, 'polished',
 introduction="- **Definition:**\n"
 "  - 1. Many low-magnitude earthquakes strike one localised region over **days to months** — **no clear foreshock/main shock/aftershock sequence** appears.\n"
 "  - 2. **Difficult to predict**.\n"
 "- **Causes:**\n"
 "  - 1. Hydro-seismicity.\n"
 "  - 2. Magnetic activity.\n"
 "  - 3. Weak crust.\n"
 "- **Example:** Palghar, Maharashtra — **30 low-intensity EQs in 2 months**.")

card(494, 'polished',
 introduction="- **Definition:** the downward and outward movement of slope material — rock, debris, earth — under **gravity**.\n"
 "- **Way Forward:**\n"
 "  - 1. NDMA's **NLRMS** (National Landslide Risk Mitigation Strategy).\n"
 "  - 2. The National Landslide Risk Mitigation Project.\n"
 "- **Steps:**\n"
 "  - 1. GSI hazard zonation maps using **UAV**.\n"
 "  - 2. **Microzonation**.\n"
 "  - 3. Capacity building.\n"
 "- **Best Practices:**\n"
 "  - 1. Maharashtra — **geo-textile**.\n"
 "  - 2. Uttarkashi — **EWS + stabilisation**.\n"
 "- **70 HEPs in Himalayan states** carry the risk of EQ-triggered landslides.",
 data="- **GSI:** **12% of land area** is prone to landslides.\n"
 "- Vulnerable areas: the **Himalayas, the Northeast and the Western Ghats**.\n"
 "- **182 landslides** hit 10 states in 2022.")

card(495, 'polished',
 introduction="- **Definition:** a spell of **abnormally high temperature** — it kills humans and animals.\n"
 "- **Way Forward:**\n"
 "  - 1. NDMA guidelines.\n"
 "  - 2. A **sensitive approach** — find the most vulnerable first.\n"
 "- **Best Practices:**\n"
 "  - 1. **Nagpur** — a Heat Action Plan plus a Heat Wave Index.\n"
 "  - 2. **Ahmedabad** — Cool Roofs Program for slums, plus colour-coded heat alerts.",
 data="- **IMD:**\n"
 "  - 1. Above **40°C** in plains.\n"
 "  - 2. Above **27°C** on the coast.\n"
 "  - 3. Above **30°C** in hills, with **5–6°** above normal.\n"
 "- **1,800** died in the **2015 New Delhi heat wave**.\n"
 "- In **2022**, over **20,000** died across **Europe, North America and China**.\n"
 "- **World Bank:**\n"
 "  - 1. **75% of Indian labour force** faces heat exposure.\n"
 "  - 2. The situation **could break the human survivability limit**.")

card(496, 'polished',
 introduction="- **Definition:** temperature falls rapidly within **24 hours**; farming, industry and social activity then need much more protection.\n"
 "- **Best Practice:** **Rein Bashera** (night shelters) in Delhi.\n"
 "- The need: an **action plan** for cold wave management.",
 data="- Conditions: plains below **10°C**, plus **4.5° below normal**, for 2 days running.\n"
 "- **IMD:** a **3× increase** in cold wave days (2017–20).")

build('/home/z/my-project/raw_batch17.md', P,
      '/home/z/my-project/polished/GS3_ENVI-DISA_batch17_cards477-496.md')
print('built batch 17: 20 cards')
