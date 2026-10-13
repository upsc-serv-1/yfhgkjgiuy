import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(597, 'polished',
 detail="- **Constitutional values: FD (Fundamental Duties)** — to promote **harmony and the spirit of common brotherhood**\n"
 "- FD — strive towards excellence in all spheres of individual and collective activity")

card(598, 'polished',
 detail="- **Anekantavada** — **multiple truths** lead to **tolerance**")

card(599, 'polished',
 detail="- Nishkaam karma, **Altruism**/sewa, Compassion, Trusteeship, Dedication, Antyodaya, Dedication to public service\n"
 "- **Kautilya**'s Yogakshema\n"
 "- **Buddha**'s 8-fold path to alleviate suffering\n"
 "- Vivekananda's Daridra Narayan")

card(600, 'polished',
 examples="- **Spirit of service**\n"
 "- an IAS officer who went and lived with the **Naxalites**\n"
 "- IAS G Rajamanikyan and IAS NSK Umesh carried rice bags to flood-hit remote areas")

card(601, 'polished',
 examples="- **IPS Manju Nath** — **transferred 39 times** in a 40-year service\n"
 "- Spirit of duty: one Lady IAS officer rejoined within days of her delivery")

card(602, 'polished',
 introduction="**Impartiality** decides without prejudice or personal bias; **non-partisanship** keeps its **distance from political influence**.",
 examples="- During polls, **Election Commission officers** show **non-partisan duty**, holding firm under **political pressure**.\n"
 "- In sensitive cases, **Supreme Court rulings** often strengthen **institutional impartiality**.\n"
 "- When scams reach the politically connected, **whistleblowing** takes **ethical courage above party lines**.",
 conclusion="When **impartiality and non-partisanship hold the Constitution above convenience**, justice arrives with no fear, favour, or faction.")

card(603, 'untouched')

card(604, 'polished',
 introduction="**Integrity is the unwavering consistency between one's values, words, and actions — even with no **external scrutiny** around.** It is the ethical anchor of public trust and the mark of true character.",
 examples="- **S. Manjunath** and **Satyendra Dubey** gave their lives upholding **professional integrity**.\n"
 "- Again and again **Ashok Khemka** was transferred — his stand against systemic malpractice was the reason.\n"
 "- **T.N. Seshan's** election reforms were **fearless**; a **non-negotiable integrity of purpose** drove them.",
 conclusion="**Integrity transforms authority into trust**, so governance is not just lawful but morally credible.")

card(605, 'untouched')

card(606, 'polished',
 detail="- **Intro:** — Integrity is the **cornerstone of all ethical values**\n"
 "- Success needs intelligence and energy; yet the discipline and consistency to act in the right direction stay guarded by **integrity**")

card(607, 'untouched')

card(608, 'polished',
 examples="- Students who never cheat, even on high-stakes exams where they could otherwise fail")

card(609, 'polished',
 examples="- **Josef Mengele - Auschwitz camp doctor** — his competence served the job of exterminating Jews")

card(610, 'untouched')

card(611, 'polished',
 examples="- **Kalam** (the Missile Man) put his emphasis on education; **Dr Fakhrizadeh** stands accused of building nuclear weapons\n"
 "- **Md Yunus** on one side, **Harshad Mehta** on the other\n"
 "- on the wrong side: technical frauds, governance frauds")

card(612, 'polished',
 examples="- When all 3 **values** align positively: IIT and IIM students designed a **low cost ventilator**.\n"
 "- During the 26/11 attack, **Taj Mahal palace** employees safely evacuated all the hostages.")

card(613, 'polished',
 examples="- with LAS, **Stephen Hawking** still lived 76 years\n"
 "- **2 transgenders** found place in her office — **Ira Singhal**, the 1st IAS officer to do so\n"
 "- **COVID 19** brought **extreme stress** — IAS Rajendra Bharud, Nandur Madhameshwar\n"
 "- an IAS chose to stay with the Naxalites\n"
 "- sharing meals with Dalits — **Rahul Kumar**")

card(614, 'untouched')

card(615, 'polished',
 detail="- Initiatives at personal level: a strong personal **code of ethics**; Harmony among thoughts, words and actions; Transparent and accountable conduct; Keep confidences safe; Set boundaries and respect them; Serve others with no expectation of rewards; Show reliability in action; Keep every commitment")

card(616, 'polished',
 examples="- Ways to prove trustworthy\n"
 "- **Kautilya**'s 2 lamps — one lamp for the state's work, one for personal work\n"
 "- Mother Teresa, serving selflessly\n"
 "- **Sachin** — present at work even when a close relative or friend had died")

build('/home/z/my-project/raw_batch23.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch23_cards597-616.md')

# 0599 has a second detail block (Concept) that bb.build cannot target; patch it directly.
_out = '/home/z/my-project/polished/GS4_ETHI_batch23_cards597-616.md'
_t = open(_out).read()
_old = "- Common thread of philosophers inquiry is to understand one's purpose, one's true nature\n- Religion, education, experimentation have been recommended. Gandhi recommends selfless service"
_new = "- The common thread in philosophers' inquiry: understanding one's purpose and one's true nature\n- They have recommended religion, education, experimentation; Gandhi recommends selfless service"
assert _old in _t, '0599 concept block not found'
open(_out, 'w').write(_t.replace(_old, _new, 1))
print('built batch 23: 20 cards')
