import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(677, 'polished',
 detail="- **Ram Rajya idea of Gandhi** — self-regulation, so the state becomes unnecessary")

card(678, 'untouched')

card(679, 'untouched')

card(680, 'untouched')

card(681, 'polished',
 detail="- **Plato**'s 'Knowledge is the true virtue' needs to be carried over to social media.")

card(682, 'untouched')

card(683, 'untouched')

card(684, 'untouched')

card(685, 'untouched')

card(686, 'polished',
 introduction="**Vivekananda's moral philosophy wove Vedantic spirituality into social uplift.** **Service, strength, and self-mastery** became tools of national regeneration and ethical self-realisation alike.",
 examples="- **Ramakrishna Mission** lives his **\"service as worship\"** doctrine.\n"
 "- In his **Chicago address** he pressed for **unity beyond religion**.\n"
 "- **Youth empowerment campaigns** draw from his vision: **inner character over outer achievement**.",
 conclusion="**Vivekananda** woke India's **moral confidence** up; ethics turned into an instrument of national and individual excellence.")

card(687, 'untouched')

card(688, 'polished',
 detail="- **Vivekananda**'s **Karmayoga**")

card(689, 'polished',
 detail="- **Daridra Narayana** — also written Daridranarayana or Daridra Narayan — is an axiom from the late-19th-century Indian sage Swami Vivekananda. It espouses that **service to the poor** equals service to God in importance and piety.\n"
 "- This exposition grew out of Vivekananda's wanderings...")

card(690, 'polished',
 introduction="**The lives of great leaders are living texts of values in motion.** Such leadership commands no power; it **persuades through virtue**, showing how **character fused with courage** drives lasting change.",
 examples="- **Gandhi's Dandi March** lived out **truth and non-violent resistance**.\n"
 "- **Dr. Kalam's** humility and scientific pursuit showed **service over self**.\n"
 "- **Nelson Mandela's** forgiveness after release proved **restorative justice and healing** possible.",
 conclusion="Great leaders stretch the moral imagination; they show values under pressure — a compass for citizens and statesmen alike.")

card(691, 'polished',
 introduction="**Reformers are society's moral engineers.** They fight entrenched injustice from **universal values** — liberty, equality, rationality — and turn tradition towards a moral and constitutional lens.",
 examples="- **Dr. Ambedkar's** fight for Dalit rights carried forward **dignity and social justice**.\n"
 "- **Raja Ram Mohan Roy's** campaign against Sati defended **women's rights and reason**.\n"
 "- **Vidyasagar's** push for widow remarriage embodied **compassion and gender equality**.",
 conclusion="Reformers inject ethics into history — values-driven activism turns personal conviction into collective transformation.")

card(692, 'polished',
 introduction="**Ethical administrators are an institution's conscience-keepers.** More than rule-enforcers, they **embed values like fairness, empathy, and integrity into governance**, so policy becomes ethical public service.",
 examples="- In public institutions, **T.N. Seshan's** electoral reforms reset **accountability and fearlessness**.\n"
 "- **Kiran Bedi's** prison reforms in Tihar grew from **dignity and rehabilitation**.\n"
 "- **IAS officer Pradeep Singh's** work in Naxal areas reflects **commitment to inclusive development**.",
 conclusion="Values-driven administrators win public trust; governance then holds both efficiency and ethical legitimacy.")

card(693, 'polished',
 introduction="**Ambedkar's moral vision aimed at pulling down inherited hierarchies — through rationality, equality, and constitutional ethics.** For him **dignity and justice were non-negotiable principles of public morality**.",
 examples="- **Gender justice** moved forward with the **Hindu Code Bill**.\n"
 "- **Social morality** entered **legal order** through **drafting the Constitution**.\n"
 "- Caste became **morally illegitimate** in his eyes — hence **conversion to Buddhism**.",
 conclusion="**Ambedkar gave modernity a moral spine**, so the Indian state's ethical architecture rests on liberty, justice, and equality.")

card(694, 'polished',
 introduction="**Tagore's ethics grew from aesthetic humanism.** In it, **freedom, creativity, and universal compassion** merge into a moral vision above borders, religions, and narrow nationalisms.",
 examples="- **Value-based creative education** was the hallmark of **Santiniketan**.\n"
 "- **Ethical universalism** powered his **critique of hyper-nationalism**.\n"
 "- **Gitanjali** blends **individual conscience with cosmic empathy** in poetic morality.",
 conclusion="For Indian ethics, **Tagore** was the **global voice** — beauty, freedom, and emotional universality at its root.")

card(695, 'polished',
 introduction="**Buddha's moral thought** was psychological, experiential and pragmatic — it centred on **suffering, mindfulness, and ethical causality**. To him, morality sprang from awareness and right action, not divine command.",
 examples="- **Ethical living through mindfulness** — that is the prescription of the **Eightfold Path**.\n"
 "- Buddhist ethics became **state policy** through **Ashoka's Dhamma**.\n"
 "- **Inner moral reform** in Indian prisons today runs on his method — **Vipassana**.",
 conclusion="**Buddha offered a self-cultivated ethics** — transformation starts within, then radiates into society.")

card(696, 'polished',
 introduction="**Mill's utilitarianism tied morality to consequences**: ethical action works to **maximize happiness and minimize harm**. Individual liberty stays safe under his famous **'harm principle'**.",
 examples="- **Greatest-good logic** drives **public health campaigns**.\n"
 "- **Mill's liberty ethics** underpins **free speech jurisprudence**.\n"
 "- **Welfare schemes** — each weighs a **cost-benefit ethical calculus**.",
 conclusion="Utility became ethically respectable with **Mill** — modern governance now joins liberal freedoms with collective welfare.")

build('/home/z/my-project/raw_batch27.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch27_cards677-696.md')
print('built batch 27: 20 cards')
