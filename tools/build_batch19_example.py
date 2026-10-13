import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS3-INTE-%04d' % i] = (status, blocks)

card(517, 'untouched')

card(518, 'polished',
 introduction="- India has a **7,517 km** coastline and **>1,200 islands** — highly exposed to maritime threats.\n"
 "- India's vision: **\"Neel Kranti se Arth Kranti\"**.\n"
 "- The threat from **China in the IOR** keeps rising.",
 data="- Coastline: **7,517 km**; islands: **>1,200**.",
 conclusion="India needs to **build capacity at home** along with an **International push**. Russia, for one, has proposed a dedicated maritime security body in the **UN Security Council**.")

card(519, 'polished',
 introduction="**Definition:** criminal acts — **robbery, hijacking or hostage-taking** — aimed at ships in international waters.")

card(520, 'polished',
 introduction="The **CERT-In directives** and the **Digital Personal Data Protection Act (DPDPA)** show India's resolve to guard its digital sovereignty. Together they anchor the vision of a **\"cyber-resilient Bharat\"** amid rising global threats.",
 examples="- Under CERT-In norms, breaches must be reported within **6 hours**.\n"
 "- The DPDPA set up the **Data Fiduciary & Principal** framework.\n"
 "- **Cyber Surakshit Bharat** trained **300+ officers** in data governance.",
 conclusion="India must build **capacity and ensure compliance** so that data protection becomes both enforceable and equitable.")

card(521, 'polished',
 introduction="**Definition:** keeping **digital systems, networks and data** safe from cyber threats, so their **confidentiality and integrity** hold.",
 data="- The Internet Security Threat Report puts India **3rd** among the most vulnerable to cyber threats.\n"
 "- **NCRB 2024:** cybercrimes surged **17%**, crossing 1 lakh reported cases (over 72% being financial fraud).")

card(522, 'polished',
 introduction="- **Definition:** information made up on purpose to **deceive** people into believing something false.\n"
 "- **Best Practice:** the **KL Model** of school education for media literacy.")

card(523, 'untouched')

card(524, 'polished',
 introduction="- **Definition:** an extra-judicial killing — a **mob** takes a person's life outside the courts (e.g., Udaipur, the Una flogging).\n"
 "- The SC recently sought updates on the action taken by the government.\n"
 "- **Steps**:\n"
 "  - 1. IT Rules 2021, 2023.\n"
 "  - 2. Amendment to the IPC, CrPC.\n"
 "  - 3. **Rajasthan (RJ) Protection from Lynching Bill 2019.**\n"
 "  - 4. **UAPA amendments.**\n"
 "- The **Tehseen Poonawala case** — the state must protect citizens and the country's \"**pluralistic social fabric**\".")

card(525, 'polished',
 introduction="- Flanked by the **Golden Triangle and Golden Crescent** and ringed by porous borders, India is highly vulnerable to drug trafficking.\n"
 "- **Steps**:\n"
 "  - 1. **Nasha Mukt Bharat.**\n"
 "  - 2. **NIDAAN portal.**\n"
 "  - 3. **NAPDDR** (National Action Plan for Drug Demand Reduction).\n"
 "  - 4. NDPS Act and NCB.\n"
 "- **Operation Samudragupta** — the NCB and Navy hauled in **₹15,000 crore** from the Arabian Sea.\n"
 "- **Best Practice:** **Mansa Village (Punjab)** — it turns youth energy toward community work — \"Mera Pind Mera Maan\".\n"
 "- **3-pronged reduction:** Demand + Supply + Harm.",
 data="- The NCB-Navy operation **Samudragupta** led to seizures worth **₹15,000 crore**.",
 conclusion="Under **Article 47**, the state is duty bound to prohibit drug consumption, to protect the **social fabric, public health and internal security**.")

card(526, 'polished',
 introduction="- **Definition:** the process that lets illegally earned money pose as income from a **legitimate source**.\n"
 "- **Stages:** **Placement → Layering → Integration**.\n"
 "- **Steps**:\n"
 "  - 1. **PMLA Rules 2023** (stringent KYC).\n"
 "  - 2. **Benami Transactions Prohibition Act.**\n"
 "  - 3. **PMLA Act 2003** (cognisable and non-bailable + confiscation).\n"
 "  - 4. **Black Money Act.**\n"
 "  - 5. Shell companies deregistered.",
 data="- **IMF:** **2–5% of world GDP** is laundered every year.")

card(527, 'polished',
 introduction="**FATF** is the world's watchdog against dirty money. It secures **international cooperation** and frames the **international standards** used to fight **ML & TF** (Money Laundering & Terrorist Financing).")

card(528, 'polished',
 introduction="- **Definition:** left-wing radical ideology that seeks **socio-political change through armed struggle** against the established authorities.\n"
 "- **Steps**:\n"
 "  - 1. Aspirational Districts.\n"
 "  - 2. Connectivity — roads and Mobile towers.\n"
 "  - 3. **PESA, FRA, Van Dhan.**\n"
 "  - 4. Jal Jangal Jameen.\n"
 "  - 5. A surrender-cum-rehabilitation project.\n"
 "  - 6. A Joint Task Force for coordination across states.\n"
 "- **SAMADHAN Doctrine**:\n"
 "  - **S** — Smart leadership.\n"
 "  - **A** — Aggressive strategy (fortified police stations).\n"
 "  - **M** — Motivation and training (Greyhounds).\n"
 "  - **A** — Actionable intelligence.\n"
 "  - **D** — Dashboard-based KPIs.\n"
 "  - **H** — Harnessing Tech (UAVs, biometric smart guns).\n"
 "  - **A** — Action plan for each theatre.\n"
 "  - **N** — No access to finance (PMLA).",
 data="- LWE casualties fell by **53–55%**.",
 conclusion="LWE casualties have come down **53–55%**.")

card(529, 'polished',
 introduction="- **Definition:** pushing extreme ideologies or actions that defy **established norms and institutions**, using **unconstitutional and violent methods**.\n"
 "- Antonio Guterres quote on underdevelopment.")

card(530, 'untouched')

card(531, 'polished',
 introduction="**Definition:** armed conflicts and movements still running in India's Northeast, seeking **political and social change**.",
 conclusion="- Peace in the NE is key to safeguarding India's **SUSI**.\n"
 "- It also serves the PM's vision of **\"Act East, Act first through North East\"**.\n"
 "- Antonio Guterres quote on underdevelopment and inequality fits here.")

card(532, 'polished',
 introduction="- **Definition:** a state strikes through **unconventional methods** across many domains, yet **stops short of open hostilities**.\n"
 "- Examples:\n"
 "  - 1. Chinese apps harvesting sensitive information.\n"
 "  - 2. Lone wolf attacks.\n"
 "  - 3. Cyber warfare.")

card(533, 'needs_review',
 introduction="- **State actors** = foreign governments that indulge in terrorism against another state (e.g., **ISI, the Syrian war**).\n"
 "- **Non-state actors** = extended arms of the state, providing **plausible deniability** (e.g., **JeM, LeT** in relation to ISI).\n"
 "- Through conventional and unconventional warfare, __ has been posing **multifaceted security challenges** for India.")

card(534, 'untouched')

card(535, 'polished',
 introduction="- The **MoHA** has brought in 3 new Bills:\n"
 "- IPC → **Bhartiya Nyay Sanhita Bill**.\n"
 "- CrPC → **Bhartiya Nagrik Suraksha Sanhita Bill**.\n"
 "- IEA → **Bhartiya Sakshya Bill**.\n"
 "- The new provisions stand out for being **retributive, victim-centric, tech-enabled and simplified**.\n"
 "- **IPC new sections**:\n"
 "  - 1. S.110 (organised crime).\n"
 "  - 2. S.111 (terrorism).\n"
 "  - 3. Cyber crimes.\n"
 "  - 4. **Mob lynching — 7 years.**\n"
 "  - 5. Police accountability.\n"
 "- **CrPC changes**:\n"
 "  - 1. Zero FIR.\n"
 "  - 2. Videography made mandatory.\n"
 "  - 3. Timelines — chargesheet (**90 days**) and judgement (**30 days**).\n"
 "  - 4. Forensics made compulsory.\n"
 "  - 5. Community service.\n"
 "- **IEA changes**: admissibility of **electronic/digital records**.\n"
 "- **Issues**:\n"
 "  - 1. Hate speech has been removed.\n"
 "  - 2. Detention time has gone up.\n"
 "  - 3. Little focus on bail.\n"
 "  - 4. Terms remain vague.")

card(536, 'needs_review',
 introduction="- India is **highly vulnerable** to security threats: it sits at the **epicenter of terrorism and instability**, serves as a **drug transit nation**, has a long vulnerable coastline and **porous and contested borders**.\n"
 "- Solutions mnemonic — **SECURITY**:\n"
 "  - S — Security forces capacity building, fencing.\n"
 "  - E — Economy/Finance.\n"
 "  - C — Cooperation (bilateral/international).\n"
 "  - U — Upgraded surveillance.\n"
 "  - R — Regional development / Good governance.\n"
 "  - I — Intelligence (locals), Infra, PPP.\n"
 "  - T — Trade/tech.\n"
 "  - Y — Youth / WHAM.",
 conclusion="- **Chanakya — need 3 S** for all-round national power: **Shastra** (military prowess), **Shaastra** (academia/civil-military fusion), **Sanskriti** (ideals and principles).\n"
 "- **Multi-domain operations / Whole of Govt and society approach**.\n"
 "- The fight against __ requires **all nations and stakeholders** to come on the same platform.")

build('/home/z/my-project/raw_batch19.md', P,
      '/home/z/my-project/polished/GS3_INTE_batch19_cards517-536.md')
print('built batch 19: 20 cards')
