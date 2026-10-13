import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(557, 'polished',
 detail="- The diagram shows the linkages: **Righteousness** leading to World Peace, Order in Nation, Harmony in Home, and Good Character.")

card(558, 'polished',
 detail="- **Constitutional Morality** rests on: Sovereignty, Welfare State, Justice, Democracy, Equality, Secularism, Rule of law.")

card(559, 'polished',
 introduction="**Private relationships train us in moral values** — **trust, empathy, loyalty, and responsibility**. Later, these same values show up in a person's public conduct and character.",
 examples="- **Gandhi's confession to his father** showed the **deep-rooted honesty and guilt** possible in personal relationships.\n"
 "- **Sonu Sood's humanitarian work** grew out of **familial values and upbringing**.\n"
 "- **PM Modi's devotion to his mother** reflects **humility and rooted ethics**.",
 conclusion="**Private morality forms the core of public ethics**: a strong personal value system feeds stronger social and institutional ethics.")

card(560, 'polished',
 introduction="Public relationships demand **fairness, transparency, impartiality, and responsiveness**. With these, public servants exercise their duties with **integrity and accountability**.",
 examples="- **E. Sreedharan's leadership** on metro projects showed **honesty and public dedication**.\n"
 "- **S. R. Sankaran's service** to bonded labourers kept **empathy in governance** alive.\n"
 "- **COVID-19 frontline officials** put their own safety at risk — **duty-bound ethics** in action.",
 conclusion="Ethical public conduct builds institutional trust and keeps governance citizen-centric and morally accountable.")

card(561, 'untouched')

card(562, 'polished',
 examples="- Example: an IPS officer of the **MP cadre** was video-recorded beating his wife. His professional **integrity** — not harming the vulnerable section — becomes highly doubtful.")

card(563, 'polished',
 introduction="**Ethics operates across personal, interpersonal, societal, professional, and global domains**. Each domain demands the same consistent values; together they shape one's **moral reasoning and conduct** in diverse situations.",
 examples="- **Irom Sharmila's fast** was **personal ethics** in action against perceived state violence.\n"
 "- **President Rajendra Prasad's neutrality** in office was a lesson in **institutional ethics**.\n"
 "- **India's global climate stance** carries **ethical responsibility at the international level**.",
 conclusion="When these dimensions work in harmony, personal virtue and social duty coexist — that is **ethical maturity**.")

card(564, 'polished',
 detail="- Deontological theory — Kant.\n"
 "- **Consequentialism (JS Mill, Bentham)** — covers **utilitarian** and common-good thinking.")

card(565, 'polished',
 examples="- Moderates vs Extremists / Revolutionary Movement — all paths led to **Independence**\n"
 "- Here the ends justify the means; every set of freedom fighters is equally respected")

card(566, 'polished',
 examples="- **Consequentialism:** — keeping **nuclear weapons as a deterrent**\n"
 "- going to war for national interest\n"
 "- **Welfare of the state comes first** — our constitution says so (unity, integrity in the Preamble)")

card(567, 'polished',
 examples="- **Deontology:** — upholding **human rights**, as the work of the UNHCR does\n"
 "- why India has not jumped straight from socialism to capitalism — the justice approach\n"
 "- Gandhi's withdrawal of the NCM")

card(568, 'polished',
 introduction="**Law draws the external boundaries of behaviour**; **ethics rules the internal compass**. Ethics reaches for the ideal and often asks for more than the law does — the two reinforce each other.",
 examples="- **Ashok Khemka's transfer history** stands as **ethical resistance to legal misuse**.\n"
 "- **Gandhi's Civil Disobedience** put ethical pressure on **legally valid but unjust laws**.\n"
 "- Through PILs, **judicial activism** often reads **law through ethical reasoning**.",
 conclusion="Law without ethics is coercion; ethics without law is vulnerability. Together they deliver justice with conscience and accountability.")

card(569, 'polished',
 introduction="**Value conflict is the ethical friction between personal beliefs and professional expectations.** It tests **moral clarity**, **emotional courage, and ethical prioritisation** — conscience versus convenience.",
 examples="- An IAS officer who exposes corruption may face backlash from inside the system.\n"
 "- **Ratan Tata's refusal to bribe** put value above profit.\n"
 "- In corporate scams, **whistleblowers** uphold **public ethics over private loyalty**.",
 conclusion="Resolving a value conflict calls for principled balance: hold the ethical high ground without abandoning role-responsibility or human dignity.")

card(570, 'polished',
 examples="- When school teachers join students in **cheating in CBSE exams**, they become **poor role models**.")

card(571, 'polished',
 examples="- Example: the **disrobing of Draupadi** met with silence from elders like **Bhishm Pitamah** — Social morality itself degrading.")

card(572, 'polished',
 detail="- What follows when the trust deficit grows:\n"
 "- Personal level: Ethical compromise; Suspicion in relationships; Loneliness and rootlessness feeding mental health disorders; Fear and paranoia; Emotional breakdowns when trust breaks\n"
 "- Societal level: Unsafe space for weak, vulnerable; Increased exploitation — workers, trafficking; Breakdown of **social contract**; Cooperation hard even on vital issues; Increased violence, intolerance")

card(573, 'polished',
 introduction="The classroom is where **ethical citizenship** first grows — **educational institutions** turn intelligence into wisdom. With curriculum, mentorship and peer culture, they plant **empathy, service, and moral reasoning** in the next generation.",
 examples="- **CBSE** uses value education modules to build **life skills, empathy, and ethics**.\n"
 "- At **TISS**, **field immersion and reflection** push students toward **ethical public engagement**.\n"
 "- **Navodaya Vidyalayas** pass on **discipline, fraternity, and national integration**.",
 conclusion="When **education is rooted in values**, it gives society more than professionals — it gives **public-spirited individuals**, rich in both knowledge and character.")

card(574, 'polished',
 detail="- **Value education** — works through a reward and punishment mechanism, and through teachers of impeccable character.")

card(575, 'polished',
 examples="- Ordinary Citizens and Values — moral stories teach children life lessons\n"
 "- **Soft power — the 1971 Bangladesh war**: India did not overtake the new nation. That restraint added to our moral power and our adherence to the **Panchsheel** principles\n"
 "- The **PM's gift of the GITA** — a dialogue on ethics more than religion\n"
 "- **Japan's soft power** — the teachings of Taoism and Buddhism\n"
 "- Confucian thought sits behind Chinese diplomacy")

card(576, 'polished',
 examples="- **Positive:** — a teacher who does not shun a student but finds innovative ways to teach — **Sonam Wangchuk**")

build('/home/z/my-project/raw_batch21.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch21_cards557-576.md')
print('built batch 21: 20 cards')
