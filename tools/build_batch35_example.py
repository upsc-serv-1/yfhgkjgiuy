import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS1-HIST-%04d' % i] = (status, blocks)

card(41, 'needs_review',
 introduction="Modern Indian literature grew through the Bengal Renaissance and then flowered regionally, carrying reformist ideas, nationalism, and social realism — a bridge from colonial critique to cultural awakening.",
 examples="- The **Sahitya Akademi's Bhasha Samman** honours work in tribal and regional languages\n"
 "- The **Ek Bharat Shreshtha Bharat** initiative drives inter-state literary exchanges",
 conclusion="Contemporary Indian literature must weigh rooted identity against cosmopolitan values while building the nation. Topic C: Architecture")

card(42, 'needs_review',
 introduction="Same as music.",
 examples="- **ANCIENT** — not just religion, but also realism and moral values: drama, prose, laws, epics, secular Sanskrit Lit.\n"
 "- Religious: the Vedas — 'Vasudev Kutumbakam'.",
 conclusion="- **YUVA 2.0** (Young, Upcoming and Versatile Authors) — the Prime Minister's Scheme for Mentoring Young Authors — promotes reading, writing and book culture, along with preserving old translations and digitisation.")

card(43, 'needs_review',
 introduction="From the IVC to today, India has turned stone and metal into sublime expressions of devotion, beauty, and transcendence.",
 examples="- **Post-Maurya Stone:** Gandhara, Mathura, Amravati. **Maurya stone:** the yakshi, capitals.\n"
 "- **Bronzes:** IVC; Jain — Chausa (BH): Adinath with long hair; Akota (Vadodara): all 24 on thrones.\n"
 "- Shashandevi/yakshini — Chakreshwari — Adinath.\n"
 "- Dilwara — Buddhist.\n"
 "- Dhanesar Khera — Mathura style.\n"
 "- Sultanganj — Sarnath style — foldless drapery.\n"
 "- Vakatakas — Amravati style — Poophnar (MH).\n"
 "- Portable — Gupta, Vakataka time.\n"
 "- Nalanda — Avalokiteshvara, Tara\n"
 "- Hills — JK, HP: Buddha + Ganesha, Shiva\n"
 "- Chaturanana Vishnu, Narsimha, Mahishasura Mardini Durga",
 conclusion="The legacy continues at a renewed scale — Statute of Unity, Statute of Equality (Ramanujacharya, Hyd), etc.")

card(44, 'polished',
 data="- **GOI Act 1909 (Montford)** — afforded no answer, and could not afford any answer, to Indian problems.\n"
 "- **GOI Act 1919** — It is a method of draining India of its wealth further and prolonging her servitude.\n"
 "- **Rowlatt** — na appeal, na vakeel, na daleel.\n"
 "- **GOI Act 1935** — Nehru: a car with all brakes and no engine. Vs Linlithgow: the GOI Act 1935 was the best way of maintaining British influence in India.\n"
 "- **August Offer** — dead as a door-nail (Nehru).\n"
 "- **Cripps** — a Post dated cheque on a failing bank.")

card(45, 'polished',
 introduction="National icons led ideologically. But it was regional leaders and revolutionaries who lit local rebellions and fired grassroots nationalism — decentralising the freedom movement into a truly people's struggle.",
 examples="- The **PM Janman Yojana** focuses on Particularly Vulnerable Tribal Groups, echoing **Birsa Munda's** legacy of tribal assertion\n"
 "- The **Digital Museum of Unsung Heroes** honours figures like **Kanaklata Barua** and **Veer Surendra Sai**, filling gaps in popular memory",
 conclusion="Commemorating them democratises history and revives collective memory — freedom becomes not the tale of a few but the legacy of many.")

card(46, 'polished',
 introduction="From Bengal's intellectual fervour to Punjab's martyrdom, from South India's press to the Northeast's uprisings — every region added its own rhythm to India's anthem of resistance.",
 examples="- **Freedom Trail Programmes** in Northeast India map regional heroes like **Rani Gaidinliu** and **Kanaklata Barua**\n"
 "- **Heritage City walks** in Tamil Nadu revive freedom-era printing presses and underground networks",
 conclusion="India's freedom was a chorus, not a solo. Recognising each region's part enriches our pluralistic legacy and strengthens national integration.")

card(47, 'polished',
 introduction="The freedom struggle was a mass mobilisation that wove diverse sections of society together — moving from \"History to Herstory\" as the crucial **impact of women in the freedom struggle** won recognition.",
 examples="- **Documentation & Repositories:**\n"
 "  - *National Digital District Repositories:* used to document the local contributions of various sections to the freedom struggle.\n"
 "- **Tribal Contributions & Recognition:**\n"
 "  - *Birsa Munda's birth anniversary:* celebrated as *Adivasi Gaurav Diwas* to honour tribal freedom fighters.\n"
 "  - *Adivasi Museums & Digital Repositories:* set up across districts to preserve tribal history.\n"
 "  - *Aadi Mahotsav:* a national tribal festival promoting tribal culture, crafts, and heritage.",
 conclusion="Recognising the parts played by Northeast India, women, foreigners, capitalists, socialists, and tribals gives India's freedom struggle its complete story.")

card(48, 'needs_review',
 conclusion="Show the relevance/legacy of their ideas today or for the movement — Ex: Tilak's press freedom and community festivals; the foundation he laid for Gandhian politics.")

card(49, 'polished',
 introduction="The early nationalist phase laid India's constitutional foundations, debating reform vs resistance. From the 1857 rebellion to the INC's formation, India woke to political consciousness.",
 examples="- **Azadi Ka Amrit Mahotsav** exhibitions at museums now highlight early moderates and leaders like **Dadabhai Naoroji**\n"
 "- The **Indian Council of Historical Research** recently funded studies reframing 1857 as the \"First War of Independence\" for school curricula",
 conclusion="Incremental though it was, this phase lit national identity and political awareness — the intellectual bedrock for the mass resistance ahead.")

card(50, 'polished',
 introduction="Gandhi turned politics into mass participation — from salt to the spinning wheel, India's fight became moral, inclusive, and decentralised: the freedom struggle re-made as a people's movement.",
 examples="- **Khadi Mahotsav** campaigns use digital storytelling to spread Gandhian economic self-reliance\n"
 "- The **National Digital Archives** added new modules on the Dandi March and Quit India for school outreach",
 conclusion="The Gandhian phase made ahimsa a strategy and swaraj a vision — sowing the values that anchor India's democratic soul today.")

card(51, 'polished',
 introduction="When moderation failed, revolutionaries lit the fire. Their sacrifices — from bomb factories to courtrooms — shook colonial arrogance and voiced the young's urgency for complete independence.",
 examples="- A **Digital Museum on Revolutionaries** opened in Delhi, featuring rare **HSRA** manifestos\n"
 "- Statues of **Chandrasekhar Azad** and **Ashfaqulla Khan** joined revamped public history trails",
 conclusion="Short-lived though they were, these movements brought unmatched moral courage — the empire had to face the cost of denying Indian freedom.")

card(52, 'polished',
 introduction="Beyond the elite platforms, peasants, tribals, women, and Dalits carried the struggle into forests, fields, and homes — freedom became a lived, local resistance to colonial and social oppression alike.",
 examples="- **Tribal Freedom Fighter Museum** initiatives narrate unsung uprisings like the **Santhal** and **Bhil** revolts\n"
 "- **Mera Gaon, Mera Gaurav** uses village-level storytelling to document women and lower-caste leaders in local archives",
 conclusion="True freedom grew not only from speeches but from the subalterns' sweat — their legacy must sit at the centre of national memory.")

card(53, 'polished',
 conclusion="**SC Bose:** the revolutionaries' ultimate aim is not terror, but to **install a national government**.")

card(54, 'untouched')

card(55, 'polished',
 data="- **R.P. Dutt's conspiracy theory:** the INC's formation was a plot to suppress a popular uprising in India, and the bourgeois (middle-class) leaders were complicit.")

card(56, 'polished',
 introduction="- Use the **12MPRO framework** to structure historical analysis:\n"
 "- **Ideologies**: Moderates, extremists, revolutionaries, socialists, communists, liberals, conservatives.\n"
 "- **International events**: the World wars, the Great Depression, the French Revolution, the Industrial Revolution.\n"
 "- **M - Movements**: Swadeshi, NCM, CDM, Quit India.\n"
 "- **P - Participants**: Women, intelligentsia, workers, peasants, tribals, foreigners, capitalists, Muslims, civil society.\n"
 "- **R - Rule through**: the Land revenue system (Ryotwari, Mahalwari, Zamindari), Brain Drain, Education, Admin, Press, Acts.\n"
 "- **O - Opposition to INC**: the Muslim League, Princely states, etc.",
 conclusion="Emphasise **Article 51 A - Moral Duty**: cherishing the noble ideals of the freedom struggle.")

card(57, 'untouched')

card(58, 'untouched')

card(59, 'untouched')

card(60, 'untouched')

build('/home/z/my-project/raw_batch35.md', P,
      '/home/z/my-project/polished/GS1_HIST_batch35_cards0041-0060.md')
print('built batch 35: 20 cards')
