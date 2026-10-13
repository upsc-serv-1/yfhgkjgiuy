import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(637, 'polished',
 introduction="**Building EI in civil services involves structured cultivation of emotional competencies** — self-awareness, empathy, and social sensitivity — through **training, feedback, and experiential learning**.",
 examples="- **LBSNAA** runs role-play, feedback, and mindfulness modules.\n"
 "- **360-degree reviews** build self-insight for leadership roles.\n"
 "- Peer learning on the **Bharat Darshan** builds empathy and cultural sensitivity.",
 conclusion="**Emotionally intelligent civil servants uphold ethics with compassion**, enriching both policy and people through value-based conduct.")

card(638, 'untouched')

card(639, 'polished',
 examples="- **Edison hired scientists** — awareness\n"
 "- **Wilma Rudolph** — **motivation**\n"
 "- **Geeta Phogat - won in 3rd round** — regulation\n"
 "- **Empathy** — Kalam's team invented light-weight prosthetics\n"
 "- **Social skill** — Anna Hazare convinced people for water harvesting in Ralegan")

card(640, 'polished',
 examples="- **Aligarh IPS story** — crowd management\n"
 "- **PM declared lockdown** — chose lives over livelihood")

card(641, 'polished',
 introduction="**Emotional Intelligence blends emotional awareness with cognitive regulation.** It lets a person **understand, manage, and apply** **emotions** well — for ethical judgment, adaptive behaviour, and constructive human interaction.",
 examples="- IAS officers during COVID-19 responded with empathy to public panic.\n"
 "- The **Chandrayaan-3** team managed emotional highs and lows with composure.\n"
 "- Police handling farmers' protests relied on emotional balance over force.",
 conclusion="**Emotional intelligence builds** **emotionally stable institutions** — empathy and ethics guide governance past rigid procedures.")

card(642, 'polished',
 introduction="**Self-awareness is the capacity to look inward at one's emotional states, values, and impulses.** From it grow **emotional self-regulation, authenticity, and ethical alignment**, in personal and administrative life.",
 examples="- **Dr. Kalam's** humility grew out of conscious self-understanding.\n"
 "- **Ira Singhal's** resolve showed clarity of purpose and emotional identity.\n"
 "- **LBSNAA's** feedback exercises push introspection and ethical grounding.",
 conclusion="**Self-awareness cultivates moral clarity** — public servants can then lead with inner balance and transparent intentions.")

card(643, 'polished',
 introduction="**Self-regulation is the inner capacity to manage emotions, delay impulses, and hold equilibrium** — above all under stress. It produces **measured, ethical, and policy-aligned responses** in public life.",
 examples="- During violent protests, **IPS officers** acted with restraint despite provocation.\n"
 "- **Judges** decline to react to public pressure, keeping courtroom neutrality.\n"
 "- **Civil servants** under political heat pick silence over reactive statements.",
 conclusion="**Self-regulation stabilises public authority** — dignity, legality, and maturity hold even in emotionally charged situations.")

card(644, 'polished',
 introduction="In emotional intelligence, **motivation** is the **inner emotional drive toward meaningful goals**. Purpose, resilience, and moral conviction sustain it — not external rewards.",
 examples="- **Kiran Bedi's** prison reforms grew out of an inner ethical passion.\n"
 "- Long-term goal commitment shows in **ISRO scientists'** perseverance.\n"
 "- In remote tribal areas, officers endure extreme hardship, driven by inner dedication.",
 conclusion="**Motivated public servants turn vision into action**, keeping reforms alive despite adversity or institutional inertia.")

card(645, 'polished',
 introduction="**Empathy is the cognitive-emotional ability to understand others' emotions as if they were one's own.** It grounds **inclusive, sensitive, and dignity-driven governance** in lived human realities.",
 examples="- **Rohini Sindhuri** stood by manual scavengers — an empathetic intervention.\n"
 "- The emotional distress of the displaced found an answer in **COVID migrant camps**.\n"
 "- Institutional empathy is visible in **disability-inclusive designs** across administration.",
 conclusion="**Empathy brings humanity into statecraft** — delivery becomes dignity-based service.")

card(646, 'polished',
 introduction="**Social skills** cover the emotionally intelligent behaviours of communication, collaboration, and conflict resolution — the base for **trust-building, participatory governance, and effective team functioning**.",
 examples="- Inter-agency coordination and clarity carry **disaster response teams** through.\n"
 "- Communication and persuasion decide how well **Gram Sabha** engagement works.\n"
 "- **Mann Ki Baat** is political outreach with emotional resonance.",
 conclusion="**Social skills make governance accessible and participatory** — state and citizen start working together.")

card(647, 'untouched')

card(648, 'polished',
 detail="- **Daniel Goleman**'s EI\n"
 "- Mayor and Salovey model\n"
 "- Gardner's **Theory of Multiple Intelligences**")

card(649, 'polished',
 detail="- Other views of intelligence have come up in recent years. Harvard psychologist Howard Gardner's theory of **multiple intelligences** is one such view.")

card(650, 'untouched')

card(651, 'polished',
 detail="- 4 branch model by Mayor and Salovey\n"
 "- Perceiving emotions\n"
 "- **Understanding** them\n"
 "- Using them to facilitate thought\n"
 "- Managing emotions")

card(652, 'polished',
 detail="- **Goleman's components** and the **Mayor & Salovey model** can both be drawn as diagrams.")

card(653, 'polished',
 detail="- Emotions working for us: Resolve stress, depression; a Positive attitude - 'it is possible'; **Empathy**, bonding, understanding; Balancing work and leisure; Able to be role models; Taking criticism as constructive feedback leading to personal growth; Conflict resolution; Stable mental health; Intrinsic motivation\n"
 "- Us working for emotions: Poor work environment from workplace politics; Communal tensions; Reactionary policies; Falling for propaganda; Vulnerability to manipulation\n"
 "- Dark side of EI: Manipulation for self interest; an Increment to offense; Self interest over public interest")

card(654, 'polished',
 detail="- Conclusion: too little emotion and too much emotion are both harmful.\n"
 "- EI balances those extremes, creates steadiness, and helps one follow the Aristotelean mean of virtue **ethics**\n"
 "- EI forges a path not by removing emotions but by sifting out the ones irrelevant to the task or decision at hand.")

card(655, 'polished',
 detail="- 5 pillars of EI for personal level\n"
 "- Self perception\n"
 "- Self expression\n"
 "- Interpersonal/ Relationship management\n"
 "- Decision making\n"
 "- Stress management")

card(656, 'untouched')

build('/home/z/my-project/raw_batch25.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch25_cards637-656.md')
print('built batch 25: 20 cards')
