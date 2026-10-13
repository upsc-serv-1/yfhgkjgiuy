import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(757, 'polished',
 introduction="**Strengthening values in governance** means making virtues like integrity, compassion, and impartiality routine — through systemic reform, ethical leadership, and norm-setting public behaviour.",
 examples="- **Mission Karmayogi** brings ethics modules into training.\n"
 "- **Ethics audits in government bodies** check the moral climate.\n"
 "- **Role models like Vinod Rai** spur ethical emulation.",
 conclusion="**Ethics in governance should grow like a habit**, not sit enforced like a rule.")

card(758, 'untouched')

card(759, 'untouched')

card(760, 'polished',
 detail="- In its broader sense, **Accountability** should be cultivated both outward (answerability) and inward (responsibility/**conscience**).")

card(761, 'polished',
 examples="- Eg: **CAG** audit, **CVC**, **CBI** enquiries.",
 detail="- Accountability is secured through laws and rules.")

card(762, 'polished',
 detail="- Intro: a **conflict of interest** arises when one's duties to profession, community and oneself stop pointing to one coherent answer. The options instead favour some at the cost of others.")

card(763, 'polished',
 detail="- **Resolution framework:** — 4Rs\n"
 "- Register the issue\n"
 "- Restrict the official's involvement\n"
 "- Recruit a 3rd party to oversee the process\n"
 "- Remove, or voluntary recusal\n"
 "- **Choose most suitable of the 5 approaches OR** — Steps\n"
 "- Recognise the potential for conflict\n"
 "- Keep a clear policy on disclosure\n"
 "- Disseminate relevant information to all stakeholders\n"
 "- Keep consequences proportionate in policy\n"
 "- Have a clear arrangement to deal with non-disclosure\n"
 "- Conclusion: Sunlight is the best disinfectant")

card(764, 'polished',
 examples="- **Personal vs public interests** — in the TV series 'Panchayat': where should the streetlight go, near one's home or by the public utilities\n"
 "- **Justice Kurien** — skipped a lunch hosted by the Italian government while hearing the case against the Italian marines\n"
 "- **Chanda Kochhar** — gave personal interest primacy while lending to Videocon")

card(765, 'polished',
 introduction="**Corporate ethics is the moral framework governing business conduct.** It demands **transparency, accountability, and stakeholder equity** — beyond mere legal compliance or shareholder gain.",
 examples="- The **Tata Group's** ethical legacy pairs **values with value creation**.\n"
 "- The **Infosys whistleblower case** showed internal ethical vigilance.\n"
 "- **CSR mandates under the Companies Act** gave business social responsibility a legal form.",
 conclusion="**Ethical corporates build moral ecosystems, not just markets** — growth there includes governance and conscience.")

card(766, 'untouched')

card(767, 'untouched')

card(768, 'untouched')

card(769, 'polished',
 examples="- **Volvo** — its 3-button seat belt: the IP rights were opened to all for safety")

card(770, 'polished',
 introduction="**Ethics in international relations reconciles national interest with global justice.** Foreign aid, diplomacy, and negotiations all pass through **principles of fairness, sovereignty, and human dignity**.",
 examples="- **India's Vaccine Maitri** was **compassion-driven diplomacy** at work.\n"
 "- The **IMF loan conditions** debate raises the **ethics of debt and sovereignty**.\n"
 "- On the **Russia–Ukraine war**, **India's stance** held **neutrality** alongside **humanitarian concerns**.",
 conclusion="**Ethical diplomacy earns global trust** — most of all when morality matches strategic clarity.")

card(771, 'untouched')

card(772, 'polished',
 examples="- Violence feeds a vicious cycle of more violence — the **Oromo-Tigray** conflict in **Ethiopia**.")

card(773, 'polished',
 detail="- **Machiavelli's realpolitik**: in international relations, a nation's foreign policy follows sovereign interests alone.")

card(774, 'polished',
 examples="- Global governance can drift into anarchism. Eg: the **weaponisation of space**, allowed because no explicit law forbids it.")

card(775, 'polished',
 examples="- **China vs India** — hard power reads as threat; soft power is celebrated\n"
 "- Countries with nuclear ties to India despite staying outside the **NPT** — faith in our **NFU** policy\n"
 "- **Brazil** thanked India for COVID vaccines with a Hanuman illustration")

card(776, 'polished',
 introduction="**Ethical concerns surface when institutional conduct drifts from normative standards of responsibility.** The result: **abuse of power, conflict of interest, and eroding public or stakeholder trust**.",
 examples="- **Banking scandals** (e.g., **PMC, Yes Bank**) bared **regulatory negligence and greed**.\n"
 "- The **Nirav Modi case** revealed **weak ethical oversight in public banking**.\n"
 "- Corporate **greenwashing** dresses up image-building as ethical responsibility.",
 conclusion="**Institutional ethics cannot rest on compliance alone** — it needs moral culture and individual accountability under it.")

build('/home/z/my-project/raw_batch31.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch31_cards757-776.md')
print('built batch 31: 20 cards')
