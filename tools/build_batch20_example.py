import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    pid = ('GS3-INTE-%04d' if i <= 543 else 'GS4-ETHI-%04d') % i
    P[pid] = (status, blocks)

card(537, 'polished',
 introduction="India spends the **5th largest** defence budget in the world.",
 data="- India's defence exports stand at **$1.5 Bn**, against a global market of **$500 Bn**.",
 detail="- 1. Critical deficiencies.\n"
 "- 2. Force multiplier.\n"
 "- 3. Combat edge.\n"
 "- **Defence exports**: **$1.5 billion**, against a global market of **$500 billion**.")

card(538, 'polished',
 introduction="A recent wave of reforms aims to sharpen the **synergy, operational readiness and combat edge** of the Indian Armed Forces.",
 conclusion="The goal is a **comprehensive National Security Strategy** built on **Chanakya's 3 S** — Shastra, Shaastra, Sanskriti. **Implementation will be key**.")

card(539, 'polished',
 introduction="- The **NIA** is India's **Central Counter-Terrorism Law Enforcement Agency**.\n"
 "- The NIA should be strengthened on the **4 F** to protect **SUSI**.")

card(540, 'polished',
 introduction="- The **CDS** is the **highest-ranking military officer** in India; the job is to coordinate and streamline **overall military strategy and operations**.\n"
 "- **>70 countries** have a CDS equivalent.\n"
 "- **Roles**:\n"
 "  - 1. Principal military advisor.\n"
 "  - 2. Chairman COSC.\n"
 "  - 3. Head of the Dept of Military Affairs.\n"
 "  - 4. Member of the **DAC & Defence Planning Committee.**\n"
 "  - 5. Advisor to the **NCA (nuclear).**\n"
 "- The post rests on the **Kargil Review Committee + Shekatkar Committee** recommendations.",
 data="- **>70 countries** — each has a CDS-equivalent post.",
 conclusion="The **21st-century security challenges of a two-front war** demand a proactive CDS. It must drive **synergy, jointness and integration**, plus a cohesive **National Security Strategy**.")

card(541, 'polished',
 introduction="- **Definition:** pooling the capabilities and potential of the **3 services** for **greater integration and resource optimisation**.\n"
 "- The **Kargil Review Committee** recommended it.",
 conclusion="It will work only when backed by **military modernisation** and a **comprehensive National Security Strategy**.")

card(542, 'polished',
 introduction="Through the **Agnipath Scheme**, young people are recruited into the armed forces by the government for a **short duration of 4 years**.",
 data="- The service period lasts **4 years**.")

card(543, 'untouched')

card(544, 'polished',
 detail="- **Leopold's Land Ethics** — humans cannot regard themselves as **dominators of nature**; they are **citizens of a larger biotic community**.")

card(545, 'untouched')

card(546, 'polished',
 detail="- The environment covers everything; non-violence as a principle reaches all beings — **Sentientism** (Jain and Buddhist roots).")

card(547, 'polished',
 introduction="An ethical act does more than produce an immediate result. Its **long-term ripples** run through society — strengthening **trust, institutions, and justice** — or eroding them when ethical principles give way.",
 examples="- **Durga Shakti Nagpal** enforced the law against illegal mining even under **political threats**.\n"
 "- The **Vaccine Maitri** initiative won India global goodwill through value-driven diplomacy.\n"
 "- **SEBI's regulatory actions** pushed **ethical practices in financial markets** forward.",
 conclusion="An action's **moral weight** shows in its **long-term impact** — it builds **trust, justice**, and **sustainable legitimacy**.")

card(548, 'polished',
 examples="- **Short term view** — the road to **climate change** and **environmental destruction**\n"
 "- **Materialism**, **consumerism**\n"
 "- Selfishness over **altruism**\n"
 "- When ends matter more than means, the result is **corruption, crony capitalism, scams, inequality, crimes**\n"
 "- **Self-centredness** — atomism")

card(549, 'polished',
 introduction="The **determinants of ethics** are the inner and external factors that shape the **moral worth of human action**. They include **intentions, motives, consequences, culture, upbringing, and reason** — and they matter most in ethically conflicting situations.",
 examples="- **Lal Bahadur Shastri** resigned after a train mishap — **motive-led moral responsibility** in action.\n"
 "- The **Swachh Bharat Abhiyan** began with the ethical **intent to restore dignity** to sanitation work.\n"
 "- **S. Manjunath**, an IOCL officer, fought corruption and gave his life for integrity.",
 conclusion="**Knowing the determinants of ethics** helps one choose in ways that protect both **personal integrity** and **public interest**.")

card(550, 'polished',
 introduction="**Moral relativism accepts that ethical norms differ** across societies. **Moral universalism holds that timeless values** — human dignity, justice, equality — apply everywhere, in every culture and context.",
 examples="- The **abolition of Sati** showed **universal human rights** outweighing cultural practice.\n"
 "- At the UN, **India's stand on gender rights** reflects **ethical universalism**.\n"
 "- Through the **Triple Talaq verdict**, **universal gender justice** prevailed over traditional custom.",
 conclusion="The balance is to respect culture while never letting tradition override universal moral principles.")

card(551, 'polished',
 introduction="**Ethics is the architecture of inner conviction**. This silent force turns action into duty. It ties action to universal values — **justice, compassion, integrity, and self-restraint** — with no need for external compulsion or law.",
 examples="- **IAS Armstrong Pame** built a 100-km road through crowdfunding, moved purely by **moral duty**.\n"
 "- **ISRO scientists** toil relentlessly, often past the call of duty — **silent ethical commitment**.\n"
 "- Sanitation workers kept serving through COVID-19 amid personal risk, without complaint or recognition.",
 conclusion="Ethics humanises authority and roots public behaviour in moral legitimacy, so that decisions are not just lawful but righteous.")

card(552, 'polished',
 detail="- **Good life** — to **realise every aspect** of it: **material, social, psychological, aesthetic, moral, ethical, human values**.")

card(553, 'polished',
 detail="- **Matsya Nyaya** (Sanskrit: मात्स्यन्याय; IAST: mātsyanyāya) — an ancient Indian philosophy. It stands for the **principle of the Law of Fish**.\n"
 "- It is the **fundamental law of nature**. The proverb explains it: the **big fish devouring the smaller fish** — the **strong devour the weak**.")

card(554, 'polished',
 detail="- **Values** — the **important, lasting beliefs** a person holds about **good/ bad, desirable/ undesirable**.\n"
 "- **Ethics** — a **reasoned framework of principles** built to **govern human conduct**; it looks at the **good of individual and society**.")

card(555, 'polished',
 detail="- For the **Hindu texts**, life itself is 'Anubhav Dhara' — a **series of experiences**.")

card(556, 'untouched')

build('/home/z/my-project/raw_batch20.md', P,
      '/home/z/my-project/polished/GS3_INTE-GS4_ETHI_batch20_cards537-556.md')
print('built batch 20: 20 cards')
