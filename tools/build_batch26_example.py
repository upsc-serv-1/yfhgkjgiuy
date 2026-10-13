import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(657, 'untouched')

card(658, 'untouched')

card(659, 'polished',
 examples="- **Kalam** led with one rule — praise in public, criticise in private")

card(660, 'polished',
 examples="- **Kalam** did not accept personal gifts during his tenure as President")

card(661, 'polished',
 introduction="**Aristotle's virtue ethics centred on forming character through habituated excellence.** His **'Golden Mean'** steered moral action between deficiency and excess in real-life situations.",
 examples="- **Courage** and **caution** stay in balance inside **civil servant neutrality**.\n"
 "- When **honesty** is **practised with discretion**, **virtue sits in equilibrium**.\n"
 "- **Moral habit, not just knowledge** — that is what **ethics training in the services** aims at.",
 conclusion="**Aristotle made ethics a lived craft** — moral maturity becomes a matter of trained disposition.")

card(662, 'untouched')

card(663, 'untouched')

card(664, 'polished',
 introduction="**Kant's deontological ethics placed morality in rational autonomy.** Ethical action flows not from outcomes but from **duty governed by reason and universalizability**.",
 examples="- **Whistleblowers like Satyendra Dubey** acted on **duty, not utility**.\n"
 "- **Kant's respect for moral law** echoes today in **rule-following across public institutions**.\n"
 "- The **right to dignity** in constitutional law carries **Kantian influence**.",
 conclusion="**Kant's rational ethics safeguards dignity**; law becomes a servant of reason and conscience.")

card(665, 'untouched')

card(666, 'untouched')

card(667, 'polished',
 detail="- **Categorical imperative test** — ask what would happen if everyone else did the same")

card(668, 'untouched')

card(669, 'polished',
 detail="- **Rawls** — natural justice gives every human being an inviolability of their own")

card(670, 'polished',
 detail="- **Kautilya** — saam, daam, dand, bheda — all for the happiness of the people")

card(671, 'polished',
 detail="- 'Material well being of citizens is supreme' — the point where **Machiavelli** and **Kautilya** agree.")

card(672, 'polished',
 detail="- In short, '**Yogakshema**' — the **welfare of the people** — was the ultimate goal of any ruler or government. Good governance was the means to reach it.\n"
 "- Yet **Yogakshema**, and good governance with it, was not limited to material **welfare of the people** — the social, political, and economic side. It took in spiritual and moral well-being as well.")

card(673, 'polished',
 introduction="**Gandhi's moral philosophy fused ethical absolutism with spiritual activism.** For him, **truth (Satya)** and **non-violence (Ahimsa)** were not just ideals — they were working instruments of civil resistance and human dignity.",
 examples="- The **Salt March** was **ethical protest** in place of violent agitation.\n"
 "- **Trusteeship theory** pointed towards **compassionate capitalism**.\n"
 "- His influence on civil rights movements worldwide gave Indian values their **global ethical resonance**.",
 conclusion="**Gandhi turned morality into mass action** — values became the driving force of national and global change.")

card(674, 'polished',
 detail="- What we need, as Gandhi stressed, is schooling that educates mind, body, and soul — physical, mental and spiritual development. This is his '**NAI TALIM**' concept.")

card(675, 'untouched')

card(676, 'untouched')

build('/home/z/my-project/raw_batch26.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch26_cards657-676.md')
print('built batch 26: 20 cards')
