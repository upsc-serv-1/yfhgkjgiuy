import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(577, 'untouched')

card(578, 'polished',
 introduction="**Human values are the invisible architecture of human dignity and ethical purpose.** They are inner moral ideals that lift behaviour from **instinct to intention**, from **habit to humanity** — the moral base on which civilisation stands.",
 examples="- **Raja Ram Mohan Roy's reformist zeal** grew from the value of **human dignity**.\n"
 "- **Gandhi's Satya and Ahimsa** gave the **non-violent struggle** its **spiritual core**.\n"
 "- Through the **Aspirational Districts Programme**, **NITI Aayog** pushes **equity and justice** for the most underserved.",
 conclusion="Human values grow the soul of a just society — development then rests on compassion, fairness, and dignity for all.")

card(579, 'polished',
 introduction="**Family is the crucible where the first moral impressions are forged.** It teaches less by rules than by **example**, steering a child's compass through **unspoken lessons in empathy, honesty, and discipline**.",
 examples="- **Gandhi's respect for truth** took root in his **mother's spiritual discipline**.\n"
 "- **Dr. Kalam credited his father** with teaching him **honesty and austerity**.\n"
 "- Many civil servants trace their **service ethics** to **family role-modelling**.",
 conclusion="A family rich in values raises ethical citizens — public integrity is laid on the foundation of private morality.")

card(580, 'polished',
 introduction="**Society works as a collective moral ecosystem**: it shapes ethics through **traditions, culture, peer behaviour, and collective narratives**. On its stage, personal values are either **reinforced or resisted**.",
 examples="- **LGBTQ+ rights** find growing **societal acceptance** — a sign of **inclusivity and empathy**.\n"
 "- **Environmental and indigenous values** powered the movement called **Narmada Bachao Andolan**.\n"
 "- **Solidarity and compassion** marked the **COVID-19 community kitchens**.",
 conclusion="**A just society nurtures ethical reflexes** — moral action becomes the norm, not the exception, in public and private life.")

card(581, 'untouched')

card(582, 'untouched')

card(583, 'polished',
 introduction="**Empathy** — the ability to understand and share what others feel: their emotions, experiences and struggles. It bridges the gap between **policy intent and lived realities**, above all for the vulnerable.",
 examples="- **IAS officer Rohini Sindhuri's work for manual scavengers** showed **deep human empathy**.\n"
 "- During the lockdowns, **district-level helplines for migrant workers** grew from **empathetic governance**.\n"
 "- The **PM's 'Mann Ki Baat'** often shares stories that build **public emotional connect**.",
 conclusion="**Empathy creates emotionally intelligent leadership**, so the state acts not like a machine but like a moral organism.")

card(584, 'polished',
 introduction="**Compassion is not charity; it is moral responsiveness.** The inner call is to **uplift the vulnerable with dignity**. Governance must never neglect those most in need of care and protection.",
 examples="- During the pandemic, the **PM Garib Kalyan Yojana** brought the poor quick support.\n"
 "- **Mission Antyodaya and DAY-NRLM** are development models driven by **compassion**.\n"
 "- With tribal communities, **IAS officers** practise administration that is **culturally sensitive and inclusive**.",
 conclusion="**Compassion ensures justice reaches the last citizen** — welfare turns from a policy on paper into a promise kept with empathy.")

card(585, 'polished',
 examples="- A hospital for adivasis in Maoist areas — **Eg: Tamboli Ayyaj**.")

card(586, 'polished',
 examples="- **To bring reform** — empathy at work: Eg. **IPS Kiran Bedi**'s **prison reforms** in **Tihar jail**.")

card(587, 'polished',
 examples="- Bangladesh helped the **Rohingyas** rather than condemning them.")

card(588, 'polished',
 examples="- **Nagendra Prasad, Rural Dept of UP** — **uplifted** the **Bawariya community** out of **poverty and prejudice**.")

card(589, 'polished',
 detail="- **Altruism** — treating help to others as a **moral obligation**; reflected in **DPSP**, **surrogacy**, Art 15(2).")

card(590, 'polished',
 introduction="**Aptitude** — an ability, inborn or learnt, to understand, act, and adapt well in a given context. It combines **mental sharpness, emotional regulation, and ethical clarity**, the base of sound public decision-making.",
 examples="- Consistent preparation made **IAS topper Pradeep Singh** a case of **analytical aptitude** with **emotional discipline**.\n"
 "- In disaster zones, **District collectors** show **crisis aptitude** along with **empathetic field leadership**.\n"
 "- Under pressure, **Aptitude tests in UPSC exams** measure **problem-solving, comprehension, and judgment**.",
 conclusion="**Aptitude keeps efficiency tied to integrity** — civil servants stay competent, sensitive and ethically balanced as governance settings change.")

card(591, 'polished',
 introduction="**Objectivity is the ability to decide on evidence, logic, and fairness — not on emotions, bias, or external pressures.** Equitable governance and rational public service delivery depend on it.",
 examples="- **Evidence-based decision-making** got a permanent place through the **Right to Information (RTI)**.\n"
 "- **Objective and neutral** by design — the standard for **UPSC interview panels**.\n"
 "- With **e-governance tools such as the JAM trinity**, **subjectivity in welfare distribution** falls.",
 conclusion="**Objectivity lets fairness prevail over favouritism**, giving public institutions credibility and predictability.")

card(592, 'polished',
 introduction="Where there is **dedication to public service**, collective welfare comes before personal gain. Duty becomes **devotion**; the office becomes an **instrument of justice and compassion**.",
 examples="- **IAS Armstrong Pame** built roads in Manipur out of **selfless administrative commitment**.\n"
 "- During COVID-19, **healthcare workers** embodied **sacrifice for public well-being**.\n"
 "- Under constant risk, **civil servants in LWE regions** provide **unwavering service**.",
 conclusion="With **dedication** comes **ethical resilience** — the quality that makes civil servants true agents of inclusive and responsive governance.")

card(593, 'polished',
 introduction="**Tolerance is the willingness to accept views, behaviours, or beliefs different from one's own.** It shows **maturity in pluralism** and keeps a diverse, democratic society harmonious.",
 examples="- **India's constitutional protection of religious and linguistic minorities** grows from **tolerance**.\n"
 "- **Civil society protests (e.g., Anna Hazare Movement)** were largely respected in a **tolerant democratic framework**.\n"
 "- **Public officials facing aggressive stakeholders** often practise **patience and restraint**.",
 conclusion="In conflict, **tolerance builds bridges**; peaceful coexistence and inclusive progress then become not just possible but lasting.")

card(594, 'polished',
 detail="- '**Ekam sat viprah Bahudha vadanti**' — Truth is one; the learned interpret it differently.\n"
 "- Hence we should nurture the **Sarva dharma sam bhava** spirit.")

card(595, 'untouched')

card(596, 'untouched')

build('/home/z/my-project/raw_batch22.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch22_cards577-596.md')
print('built batch 22: 20 cards')
