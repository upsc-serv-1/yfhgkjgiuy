import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS1-GEOG-%04d' % i] = (status, blocks)

card(141, 'polished',
 introduction="Jet streams are **geostrophic, high-velocity winds (400-500 km/hr)** blowing horizontally through the upper troposphere, west to east (**20K to 50K ft.**).",
 data="- **Determinants:**\n"
 "  - Air masses of varying temperature\n"
 "  - Pressure gradients\n"
 "  - The Coriolis force\n"
 "  - Landmasses (Ex: Tibet)",
 conclusion="In the Indian context — a significant role in the **onset & withdrawal of the monsoon**, underscoring the need for greater understanding.")

card(142, 'polished',
 introduction="The Earth breathes through its disasters — earthquakes, tsunamis, and volcanoes are not mere calamities but signatures of dynamic planetary systems. Understanding them is key to building climate resilience.",
 examples="- The **Early Warning Dissemination System** expansion under the **National Disaster Management Authority** is softening cyclone impacts in coastal states\n"
 "- **ISRO's** real-time earthquake monitoring network is strengthening micro-zonation in seismic-prone zones",
 conclusion="Mastering geophysical rhythms lets humans not conquer nature but coexist safely with its immense power.")

card(143, 'polished',
 introduction="Proposed by **Alfred Wegner in 1912**, the CDT holds that Earth's landmasses were once joined as a **single supercontinent** and have since drifted apart over geological time.",
 data="- The split began **200 million years ago**.",
 conclusion="- Geographers have combined the CDT, plate tectonics & other theories to explain the world's physical features and geological phenomena.\n"
 "- These theories, with modern tech advances, help humankind **predict disasters more efficiently** — making lives safer and the economy more resilient.")

card(144, 'needs_review',
 introduction="**Harry Hess's** sea-floor spreading theory held that **new oceanic crust forms at the mid-ocean ridges**, driving the slow movement of tectonic plates.",
 data="- It built on **Arthur Holmes' convection current theory** — heat from radioactive decay inside the earth creates magma that rises, forming convective currents: the force behind sea-floor spreading.\n"
 "- Evidence: **normal & reversing magnetic polarity**.",
 conclusion="(Same as Continental Drift theory).")

card(145, 'polished',
 introduction="Proposed by **Mckenzie, Parker & Morgan in 1967**, the PTT explains how **7 major & several minor lithospheric plates** move horizontally over the asthenosphere, shaping geological features through plate-boundary interactions.",
 conclusion="The PTT offers a **comprehensive framework** for understanding the distribution of continents, oceans, geological features, and geophysical phenomena — enabling more effective management of their effects.")

card(146, 'polished',
 introduction="- **El Nino** describes the **unusual warming of surface water** in the eastern tropical Pacific Ocean.\n"
 "- **La Nina** describes the **unusual cooling of surface water** in the eastern tropical Pacific Ocean.",
 data="- An inverse relation with the Indian monsoon — Ex: since 1871, **6 major droughts** are attributed to it.\n"
 "- **SEA forest fires**.\n"
 "- **Coastal flooding in S America**.\n"
 "- **Low hurricanes in the Atlantic (HP)**.\n"
 "- **Tornado & hurricane in N America**.",
 conclusion="- El Nino's disruption of the monsoon can **severely jeopardize Indian agriculture & food security** — adaptive strategies and resilient farming practices are urgently needed.\n"
 "- While La Nina benefits the Indian monsoon, the unpredictable & disruptive alternation of **El Ninos** can...")

card(147, 'needs_review',
 introduction="The **Southern Oscillation** is a coherent see-saw fluctuation of atmospheric pressure over the tropical Indo-Pacific. Since El Nino & the SO mostly coincide, the combination is called **ENSO**.",
 conclusion="(Same as El Nino/La Nina).")

card(148, 'needs_review',
 introduction="The **IOD** refers to the difference in sea surface temperature between the **western & eastern Indian Ocean**.",
 data="- A **+ve IOD is good for the Indian monsoon** — more cyclones in the AS.\n"
 "- El Nino — the Pacific Ocean.\n"
 "- The IOD — the Indian Ocean.",
 conclusion="(Same as ocean currents).")

card(149, 'polished',
 introduction="The movement of ocean water is influenced by physical characteristics like **temperature, salinity**, and external forces like **the sun and the winds**.",
 data="- The ocean covers **71% of the planet** and holds **97% of the water** — thus a key factor in storing & transferring heat energy.",
 conclusion="Investing in oceanographic research is imperative — it protects **marine ecosystems** and the livelihoods that depend on them.")

card(150, 'polished',
 introduction="- **Continuous horizontal movements** of sea water, circulating through the world's oceans.\n"
 "- Ex: **warm & cold, surface (up to 400 m) & deep-water currents**.",
 data="- **Primary forces:**\n"
 "  - Insolation\n"
 "  - Gravity\n"
 "  - The Coriolis force\n"
 "  - Atmospheric circulation (Ex: the Monsoon)\n"
 "- **Secondary forces:**\n"
 "  - Salinity\n"
 "  - Temperature\n"
 "  - Land obstruction",
 conclusion="Ocean currents — **the Earth's silent climate conductors** — call for focused research and global collaboration to unravel their intricate roles.")

card(151, 'polished',
 introduction="- It determines the type & distribution of marine organisms at depth.\n"
 "- Studying ocean temperature is imp for understanding the **movement of ocean currents** and the **coastal climate**.",
 data="- The average ocean temperature is **17 degrees**, measured by **isotherms**.\n"
 "- Ocean temperature has **risen by 1.2 degrees** since pre-industrial levels.\n"
 "- **Climate change impacts:**\n"
 "  - Marine heatwaves\n"
 "  - Stratification\n"
 "  - Deoxygenation\n"
 "  - Algal blooms\n"
 "  - Arctic amplification")

card(152, 'polished',
 introduction="It refers to the **total content of dissolved salts** in seawater — shaped by evaporation, temperature & precipitation.",
 conclusion="Salinity plays a pivotal role in ocean-current movement and in climatic processes like **evaporation & precipitation** — it needs greater attention and understanding.")

card(153, 'polished',
 introduction="- Recently the **MoES** developed the **Deep Ocean Mission** to support the government's blue economy initiatives.\n"
 "- The recent implosion of the Titan submersible has renewed focus on India's **Samudrayaan mission 2026**.",
 data="- **Components of the DOM:**\n"
 "  - Tech development for deep-sea mining\n"
 "  - Ocean climate change advisory\n"
 "  - Bioprospecting — deep-sea flora & fauna\n"
 "  - OTEC-powered desalination\n"
 "- Other scheme: **OMSART**.\n"
 "- **Samudrayaan details:**\n"
 "  - Three people to a **6000 m** depth in the **MATSYA 6000**\n"
 "  - **12 hours** of endurance\n"
 "  - Designed by NIOT\n"
 "- Other blue economy initiatives: **Sagarmala, the India Norway TF on BE, ICZMP**.",
 conclusion="**\"Neel Kranti se arth kranti\"**")

card(154, 'polished',
 introduction="- The study of ocean temperature is imp for understanding\n"
 "- the movement of ocean currents\n"
 "- the type & distribution of marine organisms at various depths\n"
 "- the coastal climate",
 examples="- The average ocean temperature is **17 degrees**, measured by **isotherms**. Ocean temperature has **risen by 1.2 degrees** since pre-industrial levels. Climate change impacts: marine heatwaves, stratification, deoxygenation, algal blooms, Arctic amplification.")

card(155, 'polished',
 introduction="Recently the **MoES** developed the **Deep Ocean Mission** to support the government's blue economy initiatives.",
 examples="- **Components** —\n"
 "  - Tech development for deep-sea mining\n"
 "  - Ocean climate change advisory\n"
 "  - Bioprospecting — deep-sea flora & fauna\n"
 "  - OTEC-powered desalination. Other scheme: **OMSART**.",
 conclusion="**Neel Kranti se arth kranti**")

card(156, 'needs_review',
 introduction="The recent implosion of the Titan submersible has renewed focus on India's **Samudrayaan mission 2026**.",
 examples="- Three people to a **6000 m** depth in the **'MATSYA 6000'** — **12 hours** endurance, NIOT-designed\n"
 "- Other blue economy initiatives: **Sagarmala**, the **India Norway TF on BE**, **ICZMP**",
 conclusion="Same as above.")

build('/home/z/my-project/raw_batch40.md', P,
      '/home/z/my-project/polished/GS1_GEOG_batch40_cards0141-0156.md')
print('built batch 40: 16 cards')
