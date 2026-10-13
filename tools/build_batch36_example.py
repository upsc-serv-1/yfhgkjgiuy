import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS1-HIST-%04d' % i] = (status, blocks)

card(61, 'polished',
 introduction="The Mughal Empire declined through weak successors, rising regional powers, and administrative collapse — the door opened for European interference and British dominance.",
 examples="- Rulers after Aurangzeb failed to check rising powers like the Marathas and the Sikhs.\n"
 "- By the mid-18th century, the nawabs of Awadh, Bengal, and Hyderabad were asserting autonomy.",
 conclusion="The Mughal decline was more than an imperial fall — it began India's fragmentation, leaving it ripe for colonial conquest by trade, treaties, and tactics.")

card(62, 'polished',
 introduction="Britain's conquest of India came less through open war than through alliances and betrayals. Battles like Plassey and Buxar turned the tide of British economic and political dominance.",
 examples="- **Plassey (1757)**: British political supremacy took root after the betrayal of Nawab Siraj-ud-Daulah.\n"
 "- **Buxar (1764)**: the Diwani rights of Bengal, Bihar, and Orissa came to the British — the financial base of empire.\n"
 "- **Anglo-Mysore Wars**: Tipu Sultan's fierce resistance, remembered today in Karnataka's cultural politics.\n"
 "- **Anglo-Maratha Wars**:\n"
 "  - 1. Dismantled the Maratha confederacy.\n"
 "  - 2. British annexation sealed with the Treaty of Bassein.",
 conclusion="These battles reshaped India's destiny — not wars alone, but tactical losses of sovereignty. They still inform debates on colonial legacy, federalism, and military diplomacy.")

card(63, 'polished',
 introduction="As war fatigue set in, the British turned to political tools — the **Subsidiary Alliance** and the **Doctrine of Lapse**. These policies ate away Indian sovereignty in the name of diplomacy.",
 examples="- Under the **Subsidiary Alliance (Lord Wellesley)**, Indian rulers — those of Hyderabad and Awadh, for example — had to keep British troops and surrender foreign policy.\n"
 "- Under the **Doctrine of Lapse (Lord Dalhousie)**, Jhansi, Satara, and Nagpur were annexed, ignoring local succession rights — resentment that echoed in 1857.\n"
 "- **Rani Lakshmibai's** resistance stands as the iconic anti-imperial defiance tied to this policy.",
 conclusion="These 'non-violent' policies were conquest tools that sowed deep political discontent. Their fallout pushed princely states towards resistance — an echo that remains in India's federal memory.")

card(64, 'polished',
 introduction="The British land revenue systems — **Zamindari, Ryotwari, Mahalwari** — put revenue above rural welfare. They broke community land rights and built the structural rural poverty that still echoes in land debates.",
 examples="- Land records are being digitised under the **Digital India Land Records Modernization Programme**, tackling legacy problems of colonial mapping\n"
 "- The **PM Kisan Samman Nidhi** gives income support to small farmers in a system that once had no state welfare",
 conclusion="Colonial systems extracted without empowering. Land and income-support schemes today try to reverse that historical marginalisation and restore agrarian dignity.")

card(65, 'polished',
 introduction="Colonial policy turned India from a maker of crafts into a supplier of raw material — deindustrialisation, trade imbalance, impoverishment — the seedbed of the 'Drain of Wealth' theory.",
 examples="- The **One District One Product** initiative revives crafts once destroyed by colonial trade policies\n"
 "- The **PLI Scheme** (Production Linked Incentive) boosts manufacturing to rebuild India's industrial self-reliance",
 conclusion="The colonial economy broke local enterprise. Today's industrial policies aim to rebuild India's lost productive capacity.")

card(66, 'polished',
 introduction="British rule brought Western education, new laws, and cultural change — sparking reform and resistance alike. It planted modern institutions but fractured traditional knowledge systems.",
 examples="- The **National Education Policy** promotes mother-tongue instruction — a shift away from colonial language imposition\n"
 "- The **Indian Knowledge Systems** initiative revives indigenous learning marginalised under British reforms",
 conclusion="Colonialism disturbed social equilibrium, yet also sparked reformist thought. Today's policies seek a balance between global skills and indigenous identity.")

card(67, 'polished',
 data="- **G V Joshi** — expenditure on the railways was an Indian subsidy to British industries.\n"
 "- **G S Iyer** — when foreign capital is sunk, administration becomes the concern of bond holders.\n"
 "- **RC Dutt** — taxation by the king is like moisture sucked by the sun, returning as fertilising rain.")

card(68, 'polished',
 introduction="Education: with English hammers, India broke the **British fetters**.")

card(69, 'polished',
 conclusion="The British and the princes needed each other to survive. India's need for either, however, is highly doubtful.")

card(70, 'untouched')

card(71, 'polished',
 introduction="These leaders were not just freedom fighters; they architected India's moral, constitutional, and educational framework. Their visions still inform the democratic ethos, grassroots reform, and inclusive policy thinking.",
 examples="- **Mera Yuva Bharat (MY Bharat)** invokes the youth nationalism of **Swami Vivekananda** and **Tilak**, fostering civic participation\n"
 "- The **Ambedkar Social Innovation Incubation Mission** empowers Dalit entrepreneurs — Ambedkar's vision of social mobility through education and enterprise",
 conclusion="Their philosophies are living ideas, not relics — embedded in the Constitution, development schemes, and social equity narratives that shape India's journey.")

card(72, 'polished',
 introduction="In the freedom struggle, the **Moderates laid the foundation**, the **extremists built the road**, the **revolutionaries strengthened it with their blood**, and finally **Gandhi walked it with the masses** towards independence.")

card(73, 'polished',
 introduction="The 1857 revolt was the **first major organised resistance** to the economic, social, political & military policies of the British EIC in India.",
 data="- **Rule through:** the Land revenue system — R, M, Z.\n"
 "- **Brain Drain:** Education, Admin, Press.\n"
 "- **Acts.**\n"
 "- **Opposition to INC:** the Muslim League, Princely states, etc.",
 conclusion="- **RC Majumdar** — the 1857 revolt was neither 1st, nor war, nor for independence.\n"
 "- **V D Savarkar** — the 1st national war of independence.\n"
 "- **S B Choudhary** — the first time that, for over a year, different regions led a concerted struggle to eject an alien power — never before seen in Indian history.\n"
 "- **Stanley Wolpert** — more than a mutiny, less than the 1st war of independence.")

card(74, 'polished',
 introduction="**Savitribai Phule**, **Pandita Ramabai**, and **Rokeya Sakhawat Hossain** led social reform — not only challenging patriarchy but building educational and institutional alternatives.",
 examples="- **Beti Bachao Beti Padhao** aligns with the educational empowerment these reformers pioneered\n"
 "- The **Mahila Samman Savings Certificate Scheme** promotes financial inclusion, echoing their call for women's agency",
 conclusion="These pioneers redefined reform from the margins — today's women-centric schemes draw straight from their legacy of grassroots empowerment.")

card(75, 'untouched')

card(76, 'polished',
 introduction="Through regulatory and legislative acts, the British laid the base of centralised administration in India — civil services and institutions that shaped the future governance structure and federal set-up.",
 examples="- The **Indian Civil Services** legacy lives on in the **UPSC's** selection of public administrators\n"
 "- The **Government of India Act, 1935** served as the template for India's constitutional architecture",
 conclusion="Colonial in intent, these reforms still enabled India's administrative continuity after 1947. **Mission Karmayogi** builds on that legacy for a citizen-centric bureaucracy.")

card(77, 'needs_review',
 conclusion="Nehru — neither Indian, nor Civil, nor a service.")

card(78, 'polished',
 introduction="Unifying over **560 princely states** after independence was India's first internal test. **Sardar Patel's** diplomacy — aided by civil servants and the military — forged a coherent union from fragmented sovereignties.",
 examples="- The **Statue of Unity** complex now has digital exhibits on the Hyderabad and Junagadh integrations\n"
 "- Civic curriculum updates under the **National Education Policy** include case studies on Sardar Patel's unification efforts",
 conclusion="Patel's realpolitik saved India from Balkanisation. Political consolidation built the platform for democratic deepening and institutional stability in a newly free nation.")

card(79, 'polished',
 introduction="Partition trauma, refugee influx, communalism, secessionist threats, and the **1975 Emergency** all tested India's democratic foundations — yet the Republic survived by adapting and reaffirming its constitutional resilience.",
 examples="- **National Integration Tour Programmes**, led by the Army in Manipur and J&K, engage youth from conflict-prone areas\n"
 "- The **Emergency@50** awareness series in schools revisits constitutional amendments and press restrictions to build democratic literacy",
 conclusion="India's nation-building was never linear. It demanded course corrections, civic awakening, and constitutional commitment — a legacy that still calls for reflection and reform.")

card(80, 'polished',
 introduction="Balancing linguistic identity with national unity produced the **States Reorganisation Act, 1956** — a transformative exercise that respected cultural diversity while tightening administrative coherence.",
 examples="- New parliamentary reports on linguistic minorities revisit **SRC** principles to address rising demands in Bundelkhand and Tamil Nadu.\n"
 "- Digital linguistic atlases funded by the **Ministry of Culture** now map dialect diversity in the Northeast and the Deccan.",
 conclusion="Reorganisation on linguistic lines nurtured regional pride without hurting national unity — pluralism managed through constitutional structure.")

build('/home/z/my-project/raw_batch36.md', P,
      '/home/z/my-project/polished/GS1_HIST_batch36_cards0061-0080.md')
print('built batch 36: 20 cards')
