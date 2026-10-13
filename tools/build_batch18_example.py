import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    pid = ('GS3-DISA-%04d' if i <= 504 else 'GS3-INTE-%04d') % i
    P[pid] = (status, blocks)

card(497, 'polished',
 introduction="- **Definition:** the Earth's crust has an opening; through it, **molten rock (magma), gases and debris** erupt.\n"
 "- **Positive effects:**\n"
 "  - 1. Soil fertility.\n"
 "  - 2. Geothermal energy and hot springs.\n"
 "  - 3. Minerals.\n"
 "  - 4. **Cooling effect.**")

card(498, 'polished',
 introduction="- **Definition:** unpredictable major fires in combustible settings (dry forests); they burn **over a large area for a long time**.\n"
 "- **Steps**:\n"
 "  - 1. **National Action Plan on Forest Fires 2018**.\n"
 "  - 2. **FF Alert System**.\n"
 "  - 3. **i-Forest initiative**.",
 data="- **FSI:** **36%** of forests are vulnerable.\n"
 "- Example: Kullu Valley forest fire, 2021.\n"
 "- **FSI:** the cost of forest fires — **$1.5 Bn**.")

card(499, 'polished',
 introduction="- **Definition:** high water along a river or the coast that ends in **inundation of land**.\n"
 "- **NDMA guidelines** cover two kinds of measures — Structural (reservoirs, desilting, afforestation) and Non-structural (**flood plain zoning, EWS**).\n"
 "- **Best Practices:**\n"
 "  - 1. Buoyant buildings (Netherlands).\n"
 "  - 2. Bamboo houses (NE India).\n"
 "  - 3. Rain gardens.\n"
 "  - 4. Sponge Cities.\n"
 "  - 5. **Jabalpur — a property tax rebate for RWH.**",
 data="- **National Flood Commission:**\n"
 "  - 1. **40 mn ha** of land is flood-prone.\n"
 "  - 2. Cost — **$7 Bn**.\n"
 "- **80% of the rain falls in 3 months**, plus cloudbursts.\n"
 "- **12% of India** is vulnerable to floods.\n"
 "- India sees **1/5th of global flood deaths**.")

card(500, 'polished',
 introduction="- **LRIC** (Lightning Resilient India Campaign) — a joint effort of **IMD, NDMA** and others; aim: deaths below **<1,200/annum**.\n"
 "- **\"Damini\" app** — from **IITM Pune** — warns **3 hours** ahead.",
 data="- Between 2020–21, **1.85 crore lightning strikes** were on record.")

card(501, 'polished',
 introduction="- **Definition:** flooding that follows when a **glacial moraine wall** breaches, as the water behind it grows beyond what the wall can hold.\n"
 "- **Vulnerability:**\n"
 "  - 1. India — the **\"3rd pole\"**.\n"
 "  - 2. **8,800 glacial lakes.**\n"
 "  - 3. Climate change.\n"
 "  - 4. Tectonically active region.",
 data="- The **Kedarnath tragedy** of **2013**.\n"
 "- The **Chamoli disaster** in **Uttarakhand (UK)**, **2021**.\n"
 "- India holds **8,800 glacial lakes**.")

card(502, 'polished',
 introduction="- The **Public Liability Insurance Act** governs this field.\n"
 "- **Vulnerability:**\n"
 "  - 1. **22** functioning nuclear reactors.\n"
 "  - 2. It borders **2 nuclear states.**\n"
 "  - 3. The coastline hosts reactors (the **Kalpakkam NPP** was flooded by the **2004 tsunami**).",
 data="- India runs **22 functioning nuclear reactors**.")

card(503, 'polished',
 introduction="- **Definition:** a series of **extremely long waves** created when ocean water is displaced on a large scale and suddenly — by **EQ/volcanoes**.\n"
 "- **Way Forward:** **DOARS** (Deep Ocean Assessment and Reporting System).\n"
 "- **INCOIS** (under **MoES**) set up **ITWEC** (Indian Tsunami Early Warning Centre).\n"
 "- The **Sagar Vani app** sends alerts to communities.",
 data="- **2004 Tsunami:** **2.3 lakh people** lost their lives.")

card(504, 'polished',
 introduction="- **Definition:** when intense rain overloads the **drainage capacity**, the result is **inundation of urban infrastructure**.\n"
 "- **iFlows Mumbai** — an integrated flood management system.\n"
 "- **RWH (Rainwater Harvesting)** is a key solution.\n"
 "- **Germany:** Sponge Cities — the **Hamburg model**.")

card(505, 'polished',
 introduction="- **Definition:** the process through which a person takes up **extreme political or religious ideas and aspirations**.\n"
 "- **Best Practices:**\n"
 "  - 1. **Aqaba Process (Jordan).**\n"
 "  - 2. **Maharashtra Model** — counselling through 3 prongs (family + clergy + professionals), plus reintegration.")

card(506, 'polished',
 introduction="- **Over-Ground Workers (OGW)** — they move militants, supply ammunition and arrange accommodation.\n"
 "- **Hybrid militants** — absent from ultras lists, but radicalised enough to strike and then fade back into daily life (sleeper cells).\n"
 "- **Keywords**:\n"
 "  - 1. **Faceless militancy.**\n"
 "  - 2. **Mission Pehal.**\n"
 "  - 3. **Lone wolf.**\n"
 "- **Best Practice:** the **SL Restorative Justice Model** — LTTE militants are rehabilitated vocationally, spiritually, socially and psychologically into the mainstream.")

card(507, 'polished',
 introduction="- **Definition:** structured groups running **coordinated criminal activities** for financial gain.\n"
 "- The new Bills that replace the **IPC, CrPC** contain separate provisions on organised crime — a move in the right direction.")

card(508, 'polished',
 introduction="- **Definition:** using **violence or threats** unlawfully to frighten civilians or governments and so advance **political or ideological goals**.\n"
 "- India has suffered as a **victim for decades**, especially of **state-sponsored terrorism**.\n"
 "- The **UK's CONTEST Strategy — 4Ps**:\n"
 "  - 1. **Prevent** — work against radicalisation.\n"
 "  - 2. **Pursue** — detect, disrupt and prosecute (e.g., **NATGRID, NIA**).\n"
 "  - 3. **Protect** — restrict access, border security, cyber (e.g., **CIBMS**).\n"
 "  - 4. **Prepare** — resilience (e.g., **NSG**).\n"
 "- Others:\n"
 "  - 1. **UN CCIT.**\n"
 "  - 2. **FATF.**",
 conclusion="Technology grows more sophisticated by the day. The **\"War on Terror\"** therefore demands cooperation beyond borders, **suffocating terror finance**, and the building of **resilient societies and robust institutions**.")

card(509, 'needs_review',
 introduction="**Organised crime (OC) and terrorism converge** through **resource sharing and mutual facilitation**, and this poses a serious threat to **internal security and global stability**.",
 conclusion="Template — this **war is not any one agency's or one government's alone**.")

card(510, 'polished',
 introduction="- **Definition:** money or financial support that reaches individual terrorists or groups.\n"
 "- **New Delhi** recently hosted the **\"No Money for Terror**\" conference.\n"
 "- **Steps**:\n"
 "  - 1. UAPA Amendments.\n"
 "  - 2. Crypto KYC.\n"
 "  - 3. The NIA has a dedicated cell.\n"
 "  - 4. **Soft Demonetisation.**\n"
 "  - 5. FCRA was amended (NGOs).\n"
 "  - 6. **FATF + PMLA.**",
 conclusion="**Suffocating finance** matters, yet by itself it cannot defeat the **hydra-headed menace of terrorism**.")

card(511, 'polished',
 introduction="- India's **land border stretches >15,000 km across 7 countries**.\n"
 "- Every border brings its own **unique challenges** for internal security.",
 data="- **>15,000 km** of land border, shared with **7 countries**.",
 conclusion="Border security needs an **all-round view**: vibrant **P2P exchanges**, upgraded surveillance and **robust bilateral cooperation**.")

card(512, 'polished',
 introduction="- India's border with China runs **3,488 km** and is **disputed at multiple locations**.\n"
 "- Example: the recent **Ladakh standoff**.\n"
 "- The **Vibrant Village Program** — an initiative that develops border villages.\n"
 "- Issues: **Cartographic and Nomenclatural aggression**.",
 data="- The India-China border measures **3,488 km**.")

card(513, 'polished',
 introduction="- Nepal has an **open border** with India — citizens of either country travel without restrictions.\n"
 "- The Bhutan border follows a similar open-border arrangement.")

card(514, 'polished',
 introduction="- The border with Myanmar cuts across **4 states in Northeast India**.\n"
 "- The **Free Movement Regime (FMR)** marks this border — people can cross up to **16 km on either side**.\n"
 "- The reason: deep ethnic and cultural ties across it.",
 data="- The FMR allows movement up to **16 km** on either side.")

card(515, 'polished',
 introduction="- Pakistan, India's **northwestern neighbour**: the **Radcliffe Award of 1947** demarcated their maritime and land boundary.\n"
 "- Border management was reviewed by the **Madhukar Gupta Committee**.\n"
 "- Measures:\n"
 "  - 1. Village Defence Guards.\n"
 "  - 2. CIBMS (Comprehensive Integrated Border Management System).")

card(516, 'polished',
 introduction="Along India's **east and northeast region** lies a **long porous border** with Bangladesh — land, riverine and maritime.")

build('/home/z/my-project/raw_batch18.md', P,
      '/home/z/my-project/polished/GS3_DISA-INTE_batch18_cards497-516.md')
print('built batch 18: 20 cards')
