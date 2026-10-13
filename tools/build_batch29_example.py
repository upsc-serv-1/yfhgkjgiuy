import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(717, 'polished',
 detail="- According to **Lord Krishna** in the **Bhagavad Gita**, Karma yoga is the spiritual practice of 'selfless action performed for the benefit of others'.\n"
 "- Karma yoga is a path to moksha (spiritual liberation) reached through work.\n"
 "- It is rightful action without attachment to fruits — a **dedication** to one's duty: give one's best, stay neutral to outcomes like success or failure.\n"
 "- [**Vivekananda**'s **Karmayoga** philosophy]")

card(718, 'polished',
 detail="- **Hobbes** presents the **social contract** between citizens and the government as follows\n"
 "- Govt <-> Citizens (Powers <-> Rights)")

card(719, 'polished',
 examples="- **Savitri Bai Phule**\n"
 "- **Mother Teresa**\n"
 "- **Chhavi Rajawat** — Sarpanch\n"
 "- **Gandhi** in the Noakhali riots while the rest of the country celebrated independence\n"
 "- Volunteers who fed the poor during COVID")

card(720, 'polished',
 examples="- **Chhavi Rajavat** — a Harvard graduate serving as Sarpanch")

card(721, 'polished',
 introduction="**Corruption is the unethical use of entrusted power for private gain.** It eats away **trust, weakens institutions**, and bends the **moral foundation** of public service and development.",
 examples="- The **2G** and coal scams damaged transparency in resource allocation.\n"
 "- **PDS and MGNREGA leakages** broke **last-mile trust**.\n"
 "- **PC Act (1988)** amendments and the **Lokpal** work towards checking corruption.",
 conclusion="**Corruption is not just a legal failure — it is a moral collapse**, calling for reform, transparency, and inner restraint.")

card(722, 'untouched')

card(723, 'polished',
 detail="- Eg: for public or constitutional offices, persons facing **bankruptcy** / **Insolvency** are barred, since they may be tempted into bribery.")

card(724, 'polished',
 detail="- 'People's indifference is best breeding ground for corruption' — our **CPI (TI)** rank stands at **85/180**. That is why this matters to us.")

card(725, 'polished',
 detail="- **Kaushik Basu** has spoken of the **sanskritisation of corruption** in society, because everybody accepts it.")

card(726, 'polished',
 detail="- The **Vohra Committee** report highlighted the ethical tangle between bureaucrat, politician and businessman.\n"
 "- Favouritism — one such issue.")

card(727, 'polished',
 detail="- **Monopoly + Discretion - Accountability** — Corruption")

card(728, 'polished',
 detail="- What the diagram captures: a vicious cycle running between **corruption**, **probity**, and political will.")

card(729, 'polished',
 data="- **Lokniti Survey** — **₹67,000 cr** was spent in the 2019 general elections\n"
 "- Orb media survey: the country's youth lean more towards protest culture than institutional politics")

card(730, 'polished',
 introduction="**Citizen's Charters are public declarations of service commitments, timelines, and grievance redressal.** They build **transparency, accountability, and responsiveness** into public service delivery.",
 examples="- **Passport Seva Kendras** work under **defined service charters**.\n"
 "- **Railways and hospitals** put up **time-bound commitments for public services**.\n"
 "- **E-Seva in Andhra Pradesh** added **charters with real-time tracking**.",
 conclusion="**Citizen's charters make ethical governance operational**, turning intent into accessible, time-bound delivery.")

card(731, 'polished',
 detail="- The citizens' charter: an organisation's written promise to the clients/citizens it serves.\n"
 "- 6 Principles: CSAT QV\n"
 "- **C-Choice** — wherever possible\n"
 "- **S-Standards** — spelling out what to expect and what to do if standards are not met\n"
 "- A - Accountability\n"
 "- T-Transparency\n"
 "- Q- Quality\n"
 "- V-Value for taxpayers' money\n"
 "- Keep it simple. Framing should involve not just senior experts but the staff too")

card(732, 'polished',
 introduction="**Codes of Ethics give aspirational moral standards; Codes of Conduct set enforceable behavioural rules.** Together they build an ethical infrastructure for professional accountability in public service.",
 examples="- **All India Services Conduct Rules (1968)** govern **civil servant behaviour**.\n"
 "- The **Model Code of Conduct** during elections secures **fairness and neutrality**.\n"
 "- Many **PSUs** keep internal Codes of Ethics for managing conflicts.",
 conclusion="**Ethical codes turn values into action** — they give public functionaries clarity, consistency, and institutional conscience.")

card(733, 'polished',
 detail="- Mentions of a **Code of Ethics** for MPs/MLAs appear in **ARC-II**.")

card(734, 'polished',
 detail="- The **2nd ARC** recommended legislation like a Civil Services Bill, to fix the tenure of senior civil servants. It also proposed monitoring their **ethical** conduct through a Central Civil Services Authority (CCSA), so that postings and transfers stay objective.\n"
 "- Improving **ethics** through: passing a **Code of Ethics**, and Repealing Article 311 to incentivise **ethical** civil servants.\n"
 "- A **Code of Ethics** for Politicians, to clean up the politician-bureaucrat nexus.")

card(735, 'polished',
 examples="- Eg: the Civil service (Conduct) Rules, 1964.",
 detail="- A **Code of conduct** states the behaviour an organisation expects from its employees.")

card(736, 'polished',
 introduction="**Public service is the ethical obligation to use state authority for collective welfare**. It rests on **duty, neutrality, compassion, and responsible stewardship of public trust**.",
 examples="- **Lal Bahadur Shastri's** resignation after a train accident was **moral accountability** in action.\n"
 "- **Ashok Khemka's** frequent transfers mirror his **unwavering dedication to integrity**.\n"
 "- In **aspirational districts**, civil servants show **mission-mode selflessness**.",
 conclusion="**Public service turns office into obligation** — power becomes a moral commitment to lifting the weakest, without bias or fear.")

build('/home/z/my-project/raw_batch29.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch29_cards717-736.md')

# 0727 has a second detail block (Concept) that bb.build cannot target; patch it directly.
_out = '/home/z/my-project/polished/GS4_ETHI_batch29_cards717-736.md'
_t = open(_out).read()
_old = "- Corruption is a blanket term that covers malpractices related to abuse/ misuse of position/ power or authority reposed in an individual/ entity"
_new = "- Corruption is a blanket term for malpractices tied to abuse or misuse of the position, power, or authority reposed in an individual or entity"
assert _old in _t, '0727 concept block not found'
open(_out, 'w').write(_t.replace(_old, _new, 1))
print('built batch 29: 20 cards')
