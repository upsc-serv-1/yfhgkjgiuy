import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build, mk

P = {}
def card(i, status, **blocks):
    pid = ('GS3-SCIE-%04d' if i <= 427 else 'GS3-ENVI-%04d') % i
    P[pid] = (status, blocks)

card(417, 'polished',
 introduction="- The Government has recently cleared the **environmental release of GM Mustard Hybrid DMH-11**.\n"
 "- **Definition:** An organism's characteristics can be changed by **transferring DNA from another organism** into it.\n"
 "- In area under GM cultivation, India holds the **5th largest** position.\n"
 "- Every GM decision must follow the **Precautionary Principle**.\n"
 "- The alternative path: \"**Safe agri-ecological solutions**\" — for example, System of Mustard Intensification.",
 data="- **DMH-11:** delivers **20–25% higher yield** (India's present yield is ½ of the global average).\n"
 "- **BT Cotton:** insecticide use fell by **over 50%** in Andhra Pradesh and Gujarat.\n"
 "- 1. Only **29/170 countries** grow GM crops.\n"
 "- 2. **5 countries alone hold 90%.**")

card(418, 'polished',
 introduction="India is updating its **IPR, localisation and deep tech frameworks** so that creators stay protected and new technology remains safe to build. The aim is a **“sandbox governance model”** suited to AI, blockchain and the tech frontiers of the future.",
 examples="- In the **Global Innovation Index (GII) 2025**, India placed **38th of the 139 economies** ranked.\n"
 "- Fintech and health apps must follow India's **data localisation norms**.\n"
 "- To prepare the policy roadmap, DPIIT has formed a **DeepTech Task Force**.",
 conclusion="For India’s digital rise to last, agile rules, **global alignment and innovation autonomy** must move forward together.")

card(419, 'polished',
 introduction="**Definition:** Legal rights that give protection to **original creations, inventions and ideas**.",
 conclusion="IPR reform should strike a balance between **incentives for advanced research** and the **larger public good**.")

card(420, 'polished',
 introduction="- **Definition:**\n"
 "  - 1. A field of research at the scale of **atoms and molecules**, in the **nanometre range (1–100 nm)**.\n"
 "  - 2. 1 nm is 1 billionth of a metre.\n"
 "- **Steps:**\n"
 "  - 1. **Nano S&T Initiative (NSTI).**\n"
 "  - 2. **Nano Mission 2007.**\n"
 "  - 3. **Visheswaraya PhD Scholarships.**\n"
 "- **Applications:**\n"
 "  - 1. Farming (nanosensors, **nano urea**, precision farming, nanogels).\n"
 "  - 2. Healthcare (controlled drug delivery, remote monitoring, **nanobots**).\n"
 "  - 3. Space applications.\n"
 "  - 4. Energy needs (solar paints, nanogenerators).\n"
 "  - 5. Building construction.\n"
 "  - 6. Electronics (nano batteries).\n"
 "  - 7. **Defence (stealth).**",
 conclusion="A **lab to field** approach is what will carry this research to the ground.")

card(421, 'polished',
 introduction="**DRDO, ISRO and CSIR** are leading India toward **indigenous R&D ecosystems**. Their innovations serve both security needs and society — a shift toward **“lab-to-field”** excellence for a self-reliant India.",
 examples="- DRDO's **Agni-5 MIRV missile** strengthens the country's credible deterrence.\n"
 "- ISRO's **INSAT-3DS** gives advanced weather data.\n"
 "- **Bio-based nanofertilizers** developed at CSIR make farming more sustainable.",
 conclusion="When these institutions work in step with each other, and **tech-commercial linkages** grow, India’s standing in global science will rise.")

card(422, 'polished',
 introduction="The push for **tech indigenisation** now covers semiconductors as well as defence platforms. It runs through Make in India, Strategic Technology Boards and FDI-linked innovation hubs. The goal matches the vision of **“design in India, for the world.”**",
 examples="- **Semiconductor fabs** with a **$10B outlay** have been approved under the Digital India push.\n"
 "- **IoT agriculture pilots** now run on indigenous **LoRa-based** chips.\n"
 "- HAL has been cleared to produce **Tejas Mk-1A fighter jets**.",
 conclusion="Real tech sovereignty will rest on strong IP ecosystems and **capacity built within the country**.")

card(423, 'polished',
 introduction="India’s **STI Policy**, **National R&D Policy** and rising budget support show a clear commitment to **science-led governance**. The push is toward **“Jan Bhagidari in Innovation”** and fairness in research opportunity.",
 examples="- **STIP 2020 draft:** it makes science more inclusive and backs open-access platforms.\n"
 "- The Union Budget has doubled the money for **R&D in clean energy**.\n"
 "- **Innovation Clusters** have begun under State S&T councils.",
 conclusion="R&D policy should combine **public accountability** with **private agility** so that the benefits reach the real world.")

card(424, 'needs_review',
 introduction="- **Definition:** How materials act and are produced at **very low temperatures** (below **–153°C**).\n"
 "- **Applications:**\n"
 "  - 1. MRI.\n"
 "  - 2. Freeze drying.\n"
 "  - 3. Cryosurgery.\n"
 "  - 4. Cold treatment of tools (metallurgy).\n"
 "  - 5. **Cryo engines** (liquid H₂, O₂).",
 data="- Temperatures count as cryogenic when they fall below **–153°C**.",
 conclusion="(No specific conclusion provided — refer general S&T template)")

card(425, 'polished',
 introduction='Known as the "Rocket Woman of India", **Ritu Karidhal** played a key role in the **Chandrayaan** mission.')

card(426, 'needs_review')

card(427, 'needs_review')

card(428, 'polished',
 introduction="- **Definition:** The frozen parts of the Earth system, found on land and under the ocean surface — for example, **permafrost**.\n"
 "- **Permafrost holds 2× as much carbon** as the atmosphere holds.\n"
 "- Glaciers in danger: **Thwaites (Antarctica), Larsen C, Okjökull (Iceland)**.",
 data="- **10% of the world’s people** live in high mountain areas.\n"
 "- Per the **IPCC**, **80% of glaciers** could vanish by **2100**.")

card(429, 'polished',
 introduction="- **Ocean Acidification:** ocean pH falling **below 8** as the seas take up **CO₂**.\n"
 "- **AMOC** (Atlantic Meridional Overturning Circulation) is the Atlantic arm of the global **ocean conveyor belt**, which carries heat and nutrients across the seas.",
 data="- The **IPCC** finds the AMOC **\"very likely to decline\"** as the 21st century moves ahead.")

card(430, 'polished',
 introduction="- **Definition:** Long-term changes in the world's temperature, rainfall and wind patterns, unfolding over **several decades**.\n"
 "- **Panchamrit (India’s 5 commitments):**\n"
 "  - 1. Reach net zero by **2070**.\n"
 "  - 2. **500 GW of non-fossil energy by 2030**.\n"
 "  - 3. **Renewables to meet 50% of energy by 2030**.\n"
 "  - 4. **Cut total carbon emissions by 1 bn tonnes by 2030**.\n"
 "  - 5. **Cut carbon intensity by 45% by 2030**.\n"
 "- **Climate Paradox:** China emits the most, yet sits in the G77.\n"
 "- **Energy Trilemma:** Energy equity + Energy security + Environmental sustainability.\n"
 "- **Key Keywords:**\n"
 "  - 1. **6th mass extinction.**\n"
 "  - 2. **DALY.**\n"
 "  - 3. **Degrowth.**\n"
 "  - 4. **LiFE.**\n"
 "  - 5. **Circular economy.**\n"
 "  - 6. **Carbon colonialism.**\n"
 "  - 7. **Climate denialism.**\n"
 "  - 8. **Greenwashing.**\n"
 "  - 9. **Hothouse.**\n"
 "  - 10. **Tipping point.**",
 data="- **Atlas of Energy:**\n"
 "  - 1. China — **10 Gt CO₂.**\n"
 "  - 2. USA — **5 Gt.**\n"
 "  - 3. India — **2.3 Gt.**\n"
 "- **Per capita:**\n"
 "  - 1. US — **14 MT.**\n"
 "  - 2. China — **7 MT.**\n"
 "  - 3. India — **1.78 MT.**\n"
 "- India has the **10th rank in the Climate Change Performance Index (CCPI) for 2025** (Germanwatch).\n"
 "- 1. The Climate Risk Index (CRI) puts India **7th among the most vulnerable** countries.\n"
 "- 2. **#1 in fatalities, #2 in monetary losses.**\n"
 "- **1 person in the USA emits as much as 108 people in Ethiopia.**\n"
 "- **Carbon-negative countries:** Bhutan.\n"
 "- **IPCC:** for the **1.5°C goal**, GHG emissions must fall **43% by 2030** (from 2019 levels).\n"
 "- **MoES Assessment:**\n"
 "  - 1. Heatwaves could turn **3–4× more common by 2100.**\n"
 "  - 2. Droughts could **double in frequency within the next decade.**\n"
 "  - 3. The sea level could climb at **3.3 mm/year.**\n"
 "- The healthcare cost of climate change: **8.5% of GDP**.\n"
 "- **ILO:** productivity losses equal **34 million full-time jobs**.\n"
 "- Rising seas expose **20% of global assets**.",
 detail="  - 1. A panchayat that is carbon-neutral.\n"
 "  - 2. A GHG inventory.\n"
 "  - 3. **Tree Bank Project** — loans are given against the trees a person plants, with no collateral.\n"
 "  - 4. Interest is paid by the panchayat.\n"
 "- **Adaptation — NEED**: build the **North European Enclosure Dam**.")

card(431, 'polished',
 introduction="- **Definition:** Net zero is the point where GHG put into the air are **absorbed back in equal measure**.\n"
 "- **India’s net zero deadline:** **2070**.\n"
 "- **New NDCs:**\n"
 "  - 1. Emission intensity to fall **at least 45%**.\n"
 "  - 2. **50% non-fossil fuel energy**.\n"
 "  - 3. An added carbon sink of **2.5–3 bn tonnes**.\n"
 "- **Steps:**\n"
 "  - 1. **OSOWOG.**\n"
 "  - 2. **IRIS** (Infrastructure for Resilient Island States).\n"
 "  - 3. **CDRI.**",
 data="- The net zero year for India: **2070**.")

card(432, 'polished',
 introduction="- It sets out the path to **net zero by 2070**:\n"
 "- 1. **Low carbon electricity:** 50% from non-fossil sources; RPOs; nuclear capacity up **3× by 2032**.\n"
 "- 2. **Transport:** 20% ethanol blending; **railways net zero by 2030**.\n"
 "- 3. **Urban efficiency:** via the National Urban Policy Framework.\n"
 "- 4. **Innovation and low emission industry:** Green H₂; National Mission for Enhanced Energy Efficiency.\n"
 "- 5. **CO₂ removal:** through **CCUS**.\n"
 "- 6. **Forest cover:** NDC target — **2.5–3 bn tonnes CO₂ equivalent by 2030**; Green India Mission.\n"
 "- 7. **Economic and financial:** low-carbon strategies for business.")

card(433, 'polished',
 introduction="- Farming produces **18% of GHG emissions**.\n"
 "- Irrigation alone takes **70% of the energy used in agriculture**.\n"
 "- Per the **Economic Survey 2018**, climate change could cut farmer incomes by **15–18%** in irrigated areas and **20–25%** in unirrigated ones.\n"
 "- **GM Crops context:**\n"
 "  - 1. Only **29/170 countries** grow GM crops.\n"
 "  - 2. **90% of the area lies in 5 countries** (USA, Canada, Brazil, Argentina, India).\n"
 "  - 3. India holds the **5th largest area** under GM cultivation — **11 mn ha**.",
 data="- Farming’s share of GHG emissions: **18%**.\n"
 "- Climate change (CC) may cut farm incomes by **15–25%**.")

card(434, 'polished',
 introduction="- **Definition:** A market-based way to cut GHG emissions — industries get an **economic reason** to keep their emissions down.\n"
 "- **Issues:**\n"
 "  - 1. Double counting.\n"
 "  - 2. Poor transparency in the market.\n"
 "  - 3. **Greenwashing.**\n"
 "- **India:**\n"
 "  - 1. **REC (Renewable Energy Certificates)**.\n"
 "  - 2. **Energy Saving Certificates** under **PAT (Perform Achieve Trade)**.",
 conclusion="India should shift step by step from **PAT to a Cap and Trade** system.")

card(435, 'polished',
 introduction="- Yearly emissions in **2010–19 were higher than in any decade before** — but the speed of growth has come down.\n"
 "- The **urban share** of world emissions keeps rising.\n"
 "- **Suggestions:**\n"
 "  - 1. Place mitigation within the **wider development context**.\n"
 "  - 2. Form **equitable partnerships** — civil society, political actors, businesses and youth.\n"
 "  - 3. Avoid **Maladaptation** — through inclusive planning, biodiversity and autonomous adaptation.\n"
 "  - 4. Work toward **climate resilient development**.\n"
 "- **Impact on food production:**\n"
 "  - 1. **CC affects 69% of Indian marine fisheries**.\n"
 "  - 2. Rice output could fall **10–30%**.\n"
 "  - 3. Maize output could fall **25–70%**.",
 data="- **2019 — India:** **4 mn disaster-induced displacements**.\n"
 "- Rice:\n"
 "  - 1. **10–30%** decline.\n"
 "  - 2. Maize: **25–70%** decline.",
 conclusion='**"A brief and rapidly closing window of opportunity to secure a liveable and sustainable future for all."**')

card(436, 'polished',
 introduction="Through its **Panchamrit pledges**, its role in **COPs** and the **LiFE Mission**, India is pointing toward **“pro-planet lifestyles”**. Its climate diplomacy stands for **climate justice for the Global South**.",
 examples="- The **International Solar Alliance** took shape with India as a co-leader, alongside the **CEM missions**.\n"
 "- Schools and colleges — more than **1 lakh+** of them — now run LiFE campaigns.\n"
 "- A **45% emissions intensity cut** was added when the **INDCs** were updated.",
 conclusion="In the decades to come, low-carbon growth must stay at the heart of India’s **development-climate alignment**.")

build('/home/z/my-project/raw_batch14.md', P,
      '/home/z/my-project/polished/GS3_SCITECH-ENVI_batch14_cards417-436.md')
print('built batch 14: 20 cards')
