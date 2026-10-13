import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(777, 'polished',
 introduction="**Ethical guidance flows from codified rules, constitutional ideals, social norms, and inner conscience.** Together they give **external direction and internal restraint** when decisions get ambiguous.",
 examples="- The **All India Services** Conduct Rules put ethical standards in writing.\n"
 "- Judicial calls to **constitutional morality** rise above mere legality.\n"
 "- Grassroots movements like **RTI** voice the public's moral expectations.",
 conclusion="Law, role, and inner conscience — when they converge, **ethics becomes sustainable**, steering action under uncertainty.")

card(778, 'untouched')

card(779, 'untouched')

card(780, 'untouched')

card(781, 'polished',
 detail="- Law Clearly states right and wrong; Ethics stays Vague\n"
 "- Law brings Punishment on violation; Ethics works by Social sanction\n"
 "- **Law Fixed for a given society** — IPC in India; Ethics May vary with person and time — lying\n"
 "- Law Evolution happens through legislation and judicial pronouncements - Art 377, adultery; Ethics Organically grows with society - Sati\n"
 "- Law Gives the basic minimum of behaviour – don't kill; Ethics Enshrines the highest ideals one must strive for – always be truthful")

card(782, 'polished',
 examples="- Legal but unethical\n"
 "- denying **PDS** ration over a failed biometric authentication alone\n"
 "- leaving an accident victim behind and rushing to one's own commitments")

card(783, 'polished',
 introduction="**Public service values are abstract ethical benchmarks; they turn bureaucratic power into moral authority.** They steer officials towards **duty, fairness, empathy, and institutional loyalty** in complex governance settings.",
 examples="- **T.N. Seshan's** electoral reforms carried **integrity and fearlessness**.\n"
 "- **E. Sreedharan's** Delhi Metro leadership showed **excellence and punctuality**.\n"
 "- **Mission Karmayogi** builds **value-based bureaucratic capacity**.",
 conclusion="**Values are administration's ethical compass**: efficiency never outpaces accountability, and authority stays anchored in legitimacy.")

card(784, 'polished',
 detail="- A **Code of Ethics** for Politicians, to better the politician-bureaucrat relationship.\n"
 "- Stronger institutions to enforce **ethical** behaviour — eg a Committee system to select the **CEC**.\n"
 "- Better **accountability**: focus on 360° performance appraisal, strengthen **RTI**, e-governance and so on.")

card(785, 'polished',
 detail="- **Mission Karmayogi**, **NITI Aayog** and the **Hota committee** speak of a SMART Bureaucracy — sensitive, mobile, alert, responsive and tech-savvy.")

card(786, 'polished',
 examples="- **Asit Kumar Pandey** — turned river cleaning into a people's movement")

card(787, 'untouched')

card(788, 'polished',
 examples="- **Spying and intelligence agencies** — the case of **Sehmat Khan**")

card(789, 'untouched')

build('/home/z/my-project/raw_batch32.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch32_cards777-789.md')
print('built batch 32: 13 cards')
