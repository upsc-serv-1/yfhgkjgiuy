import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(737, 'polished',
 introduction="**Probity is the philosophical face of moral uprightness in public life.** Where **virtue, truth, and transparency** converge, governance becomes not just lawful but ethically legitimate.",
 examples="- In the **Arthashastra**, **Kautilya** pressed for the **ethical conduct of rajadharma (king's duty)**.\n"
 "- **Sardar Patel's** stress on impartial civil services showed **value-centric governance**.\n"
 "- **Anti-corruption laws** make **ethical behaviour** a normative expectation.",
 conclusion="**Governance without probity breeds legalism without legitimacy** — compliance remains, conscience collapses.")

card(738, 'polished',
 examples="- Eg: the **Singapore** model — political will and **probity** together drove **corruption** down to zero.")

card(739, 'polished',
 introduction="**Quality of service delivery** asks how effectively, fairly, and empathetically public goods and services reach beneficiaries — a measure of **procedural efficiency and moral inclusiveness**.",
 examples="- **Mohalla Clinics in Delhi** bring **accessible and timely health services**.\n"
 "- The **Jan Dhan-Aadhaar-Mobile (JAM) trinity** keeps **benefit transfers leakage-free**.\n"
 "- **One Nation One Ration Card** adds **portability to delivery**.",
 conclusion="**Service quality turns citizens from beneficiaries into stakeholders** — inclusion and trust deepen together.")

card(740, 'untouched')

card(741, 'polished',
 introduction="**Transparency in governance means proactively disclosing institutional processes, decisions, and performance.** Through **openness, visibility, and participative accountability**, the public can scrutinise and trust.",
 examples="- The **RTI Act** gave citizens access to decision-making.\n"
 "- **Digital dashboards** (e.g., **PM Gati Shakti**) sharpen **real-time transparency**.\n"
 "- The **e-Samiksha portal** tracks government work with **inter-ministerial openness**.",
 conclusion="**Transparency turns secrecy into service** — state power then works under the light of public awareness.")

card(742, 'polished',
 introduction="**The Right to Information is a legal and ethical tool: it turns passive subjects into active citizens.** People can then question, audit, and engage with the machinery of governance.",
 examples="- **RTI** laid bare the **Adarsh housing scam** and **many recruitment irregularities**.\n"
 "- **RTI filings** revealed **Public Distribution System leakages**.\n"
 "- Whistleblowers like **RTI activist Amit Jethwa** exposed **environmental violations**.",
 conclusion="**RTI makes democratic ethics institutional** — governance shifts from monologue to monitored dialogue.")

card(743, 'untouched')

card(744, 'untouched')

card(745, 'polished',
 examples="- **Transparency** and **accountability** stand institutionalised — cf. self-disclosure under **RTI**, citizen charters, digi bonds.")

card(746, 'polished',
 examples="- Eg: **Jan sunwai**, **Citizen's charter**, **RTI**.",
 detail="- Where **probity** is upheld, **Transparency** prevails.")

card(747, 'polished',
 detail="- The diagram maps the flow: Communication, Openness, **Accountability** → **Transparency** → **Ethical** Gov, Participative Gov → GOOD GOVERNANCE.")

card(748, 'polished',
 introduction="**Utilizing public funds** means allocating, spending, and monitoring taxpayer resources ethically — securing **efficiency, equity, and integrity in financial stewardship**.",
 examples="- **CAG audits** have exposed misuse in **MPLADS** and **MNREGA**.\n"
 "- **Direct Benefit Transfers** cut leakages in subsidies.\n"
 "- The **PFMS platform** follows fund flows in real time.",
 conclusion="**Fiscal probity holds up public faith** — every rupee spent should reflect responsibility, not recklessness.")

card(749, 'polished',
 introduction="**Work culture in governance is the collective ethos, values, and behavioural norms that shape how public duties are performed**; it drives the **efficiency, accountability, and ethical climate** of institutions.",
 examples="- **Kerala's** decentralised planning grows from a **collaborative and responsive work culture**.\n"
 "- **E. Sreedharan's** Metro team lived **professional punctuality**.\n"
 "- Citizen feedback on the **SPARSH platform** lifts the **attitudinal ethos**.",
 conclusion="**Work culture is governance's silent ethic** — it shapes daily performance more than any rule.")

card(750, 'polished',
 detail="- For a civil-services question's conclusion, remember: Professional work culture ensures democratic decision making, a flatter hierarchy, self **accountability** and **effectiveness**.")

card(751, 'polished',
 detail="- Interventions that work for a **Professional** work culture: **Ethical** competency training (the Kiran Aggarwal committee).")

card(752, 'polished',
 detail="- **Max Weber** says a Bureaucratic work culture has: 1) division of work 2) hierarchy of authority 3) rule-based order 4) merit-based succession 5) top-down structure.")

card(753, 'polished',
 examples="- **Human capital** — after WW2, the Japanese put in extra hours to rebuild\n"
 "- the Japanese are punctual")

card(754, 'polished',
 examples="- **IAS Pulkit Singh** — upheld discipline with a carrot-and-stick approach\n"
 "- turned punctual himself\n"
 "- an innovation: he uploaded a picture with the newspaper on reaching office")

card(755, 'polished',
 introduction="**The status of ethics in governance** shows how deeply moral reasoning has sunk into administrative behaviour, political culture, and institutional decision-making. Justice, transparency, and restraint are the benchmarks.",
 examples="- Recurring **high-level scams** reveal the **ethical vulnerability** of governance.\n"
 "- **Restoring institutional morality** is the aim of the **RTI Act** and the **Lokpal**.\n"
 "- From within the system, whistleblowing in the **Vyapam** and coal block cases asserted ethics.",
 conclusion="What makes a government ethical is its **daily conduct**, not its constitutional promises or public declarations.")

card(756, 'polished',
 introduction="**Accountability is governance's moral architecture**: authority is exercised under **scrutiny, answerability, and consequence**, so public power lines up with ethical performance.",
 examples="- Citizens see administrative transparency through the **RTI**.\n"
 "- Misuse of public funds comes to light in **CAG** reports.\n"
 "- **Community-level accountability** becomes possible through **social audits in MGNREGA**.",
 conclusion="**Accountability builds humility into governance** — power turns from privilege into public stewardship.")

build('/home/z/my-project/raw_batch30.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch30_cards737-756.md')
print('built batch 30: 20 cards')
