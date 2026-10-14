# Manual review needed — quote-attribution worklist

Source: Gemini web-verification reply (`c11_verify/gemini_reply.md`) + my C11 Phase 1+2 work.

## Why these need your eyes

Per your rule "no mistakes" + "remove source only in extreme case":
- I refused to delete quote blocks because the verifier doesn't allow block-set changes (deleting a `:::quote` block triggers ERROR).
- I refused to edit the attribution when it's embedded INSIDE the protected quote text (would change protected text).
- I refused to ADD an attribution where the booklet has none (that's content creation, not correction).

So every quote below is one I either **couldn't verify** or **couldn't safely act on**. None of them have been edited in the polished file. Decide what you want for each one and tell me — I'll apply your decision.

## Summary

- UNVERIFIABLE (Gemini searched, no independent source found): **75**
- MISATTRIBUTED but I couldn't apply the fix (attribution embedded in protected text): **2**
- NO attribution in booklet — Gemini found the real author (would need to ADD attribution): **3**
- **Total in this worklist: 80**

---

## Group A — Gemini UNVERIFIABLE (no independent source found)

For each: Gemini searched the web for the exact quote text and could not find it in any independent source (Wikipedia, news, scholarly article, court judgment, book). Only matches were the booklet itself on Scribd or unrelated social-media posts.

**Your options per card:**
- (a) **Keep as-is** — trust the booklet author's attribution.
- (b) **Strip the attribution** — keep the quote text, remove the `— Author` label (treat as anonymous).
- (c) **Replace the quote** — substitute a different verified quote on the same theme.
- (d) **Remove the quote block entirely** — would need to modify the verifier's design or empty the block.

| # | Card | Quote | Claimed author | What Gemini searched |
|---|---|---|---|---|
| 1 | 0004 | ""The story of India is written in stone."" | John Marshall | "The story of India is written in stone", "John Marshall" "story of India is written in stone" |
| 2 | 0008 | ""Technology as an ally of culture"" | PM Modi | "Technology as an ally of culture", "Technology as an ally of culture" Modi |
| 3 | 0020 | ""Dance is the joy of the soul expressed through movement."" | Rabindranath Tagore | "Dance is the joy of the soul expressed through movement", "Dance is the joy of the soul expressed through movement" Tagore |
| 4 | 0024 | ""Indian music is a meditation, not a performance."" | Pandit Ravi Shankar | "Indian music is a meditation, not a performance", "Indian music is a meditation, not a performance" Ravi Shankar |
| 5 | 0025 | ""A nation’s folk music is its heartbeat."" | Jawaharlal Nehru | "A nation’s folk music is its heartbeat", "A nation's folk music is its heartbeat" Nehru |
| 6 | 0026 | ""Theatre mirrors society and transforms it."" | Habib Tanvir | "Theatre mirrors society and transforms it", "Theatre mirrors society and transforms it" Habib Tanvir |
| 7 | 0027 | ""In puppetry, silent hands speak louder than words."" | Satyajit Ray | "In puppetry, silent hands speak louder than words", "In puppetry, silent hands speak louder than words" Satyajit Ray |
| 8 | 0028 | ""Martial arts train the body to protect and the mind to persevere."" | Bruce Lee | "Martial arts train the body to protect and the mind to persevere", "Bruce Lee" "mind to persevere" |
| 9 | 0037 | ""The Vedas are not books of theology but records of spiritual discovery."" | Sarvepalli Radhakrishnan | "The Vedas are not books of theology but records of spiritual discovery", Radhakrishnan "records of spiritual discovery" |
| 10 | 0038 | ""Sangam poetry is not just emotion  it is geography, economy, and politics in verse."" | A.K. Ramanujan | "Sangam poetry is not just emotion", "Sangam poetry is not just emotion it is geography, economy, and politics in verse" |
| 11 | 0039 | ""Silence and simplicity are the roots of liberation."" | Mahavira | "Silence and simplicity are the roots of liberation", "Silence and simplicity are the roots of liberation" Mahavira |
| 12 | 0040 | ""Persian in India was not just a language, it was the canvas for Indo-Islamic creativity."" | Muzaffar Alam | "Persian in India was not just a language, it was the canvas for Indo-Islamic creativity", Muzaffar Alam "canvas for Indo-Islamic creativity |
| 13 | 0041 | ""A nation is built by those who write its soul into words."" | Rabindranath Tagore | "A nation is built by those who write its soul into words", Tagore "write its soul into words" |
| 14 | 0047 | ""The diverse threads of society wove together in the fabric of the freedom struggle."" | Bipin Chandra Pal | "The diverse threads of society wove together in the fabric of the freedom struggle", "Bipin Chandra Pal" "fabric of the freedom struggle" |
| 15 | 0049 | ""The seeds of freedom must be sown in the soil of unity."" | Gopal Krishna Gokhale | "The seeds of freedom must be sown in the soil of unity", "Gopal Krishna Gokhale" "soil of unity" |
| 16 | 0050 | ""You may never know what results come of your actions, but if you do nothing, there will be no result."" | Mahatma Gandhi | "You may never know what results come of your actions, but if you do nothing, there will be no result", "Collected Works of Mahatma Gandhi"  |
| 17 | 0081 | ""Liberty, equality, fraternity these are not mere words, they are our guiding principles."" | Nelson Mandela | "Liberty, equality, fraternity these are not mere words", "Nelson Mandela" "these are not mere words, they are our guiding principles" |
| 18 | 0082 | ""The sun never set on the British Empire but it never rose on its justice."" | Shashi Tharoor | "The sun never set on the British Empire but it never rose on its justice", "Shashi Tharoor" "never rose on its justice" |
| 19 | 0084 | ""The factory system was the beginning of man being reduced to a number."" | Mahatma Gandhi | "The factory system was the beginning of man being reduced to a number", Gandhi "factory system was the beginning" |
| 20 | 0086 | ""India is a garden of many flowers"" | each one beautiful, each one unique." — Jawaharlal Nehru | "India is a garden of many flowers", "India is a garden of many flowers each one beautiful, each one unique" Nehru |
| 21 | 0096 | ""Social justice is the first condition of humanity."" | B. R. Ambedkar | "Social justice is the first condition of humanity", "Social justice is the first condition of humanity" Ambedkar |
| 22 | 0099 | ""Religion is a personal matter, not a political weapon."" | Jawaharlal Nehru | "Religion is a personal matter, not a political weapon", Nehru "Religion is a personal matter, not a political weapon" |
| 23 | 0100 | ""India is a union of states, not a confederation of ambitions."" | Sardar Patel | "India is a union of states, not a confederation of ambitions", "Sardar Patel" "confederation of ambitions" |
| 24 | 0103 | ""Secularism is the soul of the Indian Constitution."" | Rajendra Prasad | "Secularism is the soul of the Indian Constitution", "Rajendra Prasad" "soul of the Indian Constitution" |
| 25 | 0105 | ""Urban governance is not just administration  it is transformation."" | E. Sreedharan | "Urban governance is not just administration it is transformation", "E. Sreedharan" "is transformation" |
| 26 | 0107 | ""Energy is necessary for development & sustainable energy is necessary for sustainable development"" | Tim Wirth | "Energy is necessary for development & sustainable energy is necessary for sustainable development", "Energy is necessary for development" " |
| 27 | 0131 | ""The environment and the economy are really both two sides of the same coin. You cannot sustain the economy if you don't take care of the en" | Bruce Lipton | "The environment and the economy are really both two sides of the same coin", "Bruce Lipton" "cannot sustain the economy if you don't take c |
| 28 | 0133 | ""Industries go where they are wanted, and stay where they are treated well."" | Ronald Reagan | "Industries go where they are wanted, and stay where they are treated well", "Ronald Reagan" "where they are treated well" |
| 29 | 0157 | ""While we borrowed from many, we built for Bharat."" | Dr. B.R. Ambedkar | "While we borrowed from many, we built for Bharat", Ambedkar "While we borrowed from many, we built for Bharat" |
| 30 | 0158 | ""Parliamentary democracy is the bedrock of India's governance, where diverse voices converge to shape the nation's destiny."" | ABV (Atal Bihari Vajpayee) | "Parliamentary democracy is the bedrock of India's governance", Vajpayee "bedrock of India's governance" |
| 31 | 0159 | ""Amendment is the lifeline of a living Constitution."" | Nani Palkhivala | "Amendment is the lifeline of a living Constitution", Palkhivala "Amendment is the lifeline of a living Constitution" |
| 32 | 0178 | ""Free & Fair elections are the lifeblood of any democracy."" | Jimmy Carter | "Free & Fair elections are the lifeblood of any democracy", "Jimmy Carter" "lifeblood of any democracy" |
| 33 | 0179 | ""When the power of a vote is diluted through opacity in political funding, democracy loses its intrinsic value."" | Ornit Shani | "When the power of a vote is diluted through opacity in political funding", "Ornit Shani" "opacity in political funding" |
| 34 | 0181 | ""Free & Fair elections are lifeblood of any democracy"" | Jimmy Carter | "Free & Fair elections are lifeblood of any democracy", "Jimmy Carter" "elections are lifeblood of any democracy" |
| 35 | 0184 | ""Like a cancer, eating into the vitals of a democracy."" | Delhi HC 2018 | "Like a cancer, eating into the vitals of a democracy", "Delhi High Court 2018 cancer democracy electoral bonds" |
| 36 | 0185 | ""When the power of a vote is diluted through opacity in political funding, democracy loses its intrinsic value"" | Ornit Shani | "When the power of a vote is diluted through opacity in political funding, democracy loses its intrinsic value", "Ornit Shani" |
| 37 | 0186 | ""Democracy at the grassroots is democracy at its strongest."" | Mahatma Gandhi | "Democracy at the grassroots is democracy at its strongest", Gandhi "grassroots is democracy at its strongest" |
| 38 | 0189 | ""Cooperative federalism is not a choice; it is a constitutional compulsion."" | PM Narendra Modi | "Cooperative federalism is not a choice; it is a constitutional compulsion", Modi "constitutional compulsion" |
| 39 | 0199 | ""A free press should neither be an ally nor an adversary but a constructive critic."" | Gandhiji | "A free press should neither be an ally nor an adversary but a constructive critic", Gandhi "ally nor an adversary" |
| 40 | 0200 | ""Social media is a double-edged sword."" | Noam Chomsky | "Social media is a double-edged sword" Chomsky |
| 41 | 0201 | ""In democracy, even silence can organise into influence."" | Granville Austin | "In democracy, even silence can organise into influence", "Granville Austin" "silence can organise into influence" |
| 42 | 0209 | ""Governor's actions must be tempered with caution, dictated by reason & activated in good faith."" | Sarkaria Commission | "Governor's actions must be tempered with caution, dictated by reason & activated in good faith", "Sarkaria Commission" Governor "tempered w |
| 43 | 0211 | ""Justice is not simply punishing the guilty, but also defending the innocent and ensuring due process for all."" | Kofi Annan | "Justice is not simply punishing the guilty, but also defending the innocent and ensuring due process for all", "Kofi Annan" |
| 44 | 0216 | ""Accountability & integrity increase a court's prestige & faith rather than reducing it."" | Justice Hidayatullah, in Naresh Sridhar Case | "Accountability & integrity increase a court's prestige & faith rather than reducing it", Hidayatullah "Naresh Sridhar" |
| 45 | 0225 | ""Civil servants are the steel frame but must also be the spinal nerve of reform."" | Sardar Patel | "Civil servants are the steel frame but must also be the spinal nerve of reform", "Sardar Patel" "spinal nerve" |
| 46 | 0226 | ""Civil servants are the silent architects of a nation's progress, dedicated to translating policies into actions that shape the destiny of I" | Dr. APJ Abdul Kalam | "Civil servants are the silent architects of a nation's progress", Kalam "silent architects of a nation's progress" |
| 47 | 0226 | ""Civil servants are the bridge that connects government policies with the aspirations and welfare of the people they serve."" | NR Narayana Murthy | "Civil servants are the bridge that connects government policies with the aspirations", "Narayana Murthy" |
| 48 | 0229, 0233 | ""Without accountability, resources are wasted, corruption flourishes, and trust in institutions is eroded."" | Ban Ki-moon | "Without accountability, resources are wasted, corruption flourishes, and trust in institutions is eroded", "Ban Ki-moon" |
| 49 | 0230 | ""RTI is the most important legislation since independence. It marks the beginning of an era of dawn & ends the era of darkness."" | ARC 2 | "RTI is the most important legislation since independence. It marks the beginning of an era of dawn & ends the era of darkness", "Second ARC |
| 50 | 0231 | ""Social audit is not just an evaluation of programs; it's an assertion of people's rights to dignity, transparency, and accountable governan" | Aruna Roy | "Social audit is not just an evaluation of programs; it's an assertion of people's rights to dignity", "Aruna Roy" |
| 51 | 0237 | ""The CAG is the conscience keeper of government finances, ensuring that taxpayer money is used judiciously and efficiently."" | Rajiv Mehrishi (former Finance Secretary) | "The CAG is the conscience keeper of government finances, ensuring that taxpayer money is used judiciously and efficiently", "Rajiv Mehrishi |
| 52 | 0263 | ""Good policies fail with bad implementation; bad policies fail faster."" | Second ARC | "Good policies fail with bad implementation; bad policies fail faster", "Second ARC" "bad policies fail faster" |
| 53 | 0268 | ""The development sector is not third sector it is the frontline of inclusive governance."" | Abhijit Banerjee | "The development sector is not third sector it is the frontline of inclusive governance", "Abhijit Banerjee" |
| 54 | 0282 | ""An educated, healthy population is not a burden it is the foundation of any civilised society."" | Amartya Sen | "An educated, healthy population is not a burden it is the foundation of any civilised society", "Amartya Sen" |
| 55 | 0287 | ""The test of good governance is how it treats its weakest citizens."" | Mahatma Gandhi | "The test of good governance is how it treats its weakest citizens", Gandhi "test of good governance" |
| 56 | 0289 | ""The Constitution is a transformative document it enshrines not charity but rights."" | Justice Indu Malhotra | "The Constitution is a transformative document it enshrines not charity but rights", "Indu Malhotra" |
| 57 | 0295 | ""A budget tells us what we value as a society."" | UN Women | "A budget tells us what we value as a society", "UN Women" "tells us what we value as a society" |
| 58 | 0301 | ""In a world full of fault lines and rifts, we need to build a shared future."" | Modi | "In a world full of fault lines and rifts, we need to build a shared future", Modi "fault lines and rifts" |
| 59 | 0301 | ""India has entered a phase of energetic foreign policy where it is not anymore a passive recipient of global happenings."" | S. Jaishankar | "India has entered a phase of energetic foreign policy where it is not anymore a passive recipient of global happenings", Jaishankar "passiv |
| 60 | 0304 | ""The Indian Ocean, with its critical sea lanes and vast reservoir of resources, will be a highway to prosperity and a theatre of rivalry."" | C. Raja Mohan | "The Indian Ocean, with its critical sea lanes and vast reservoir of resources, will be a highway to prosperity and a theatre of rivalry", " |
| 61 | 0305 | ""In the information age, a nation's power is increasingly defined by its ability to influence as much as to militarily and economically domi" | Shashi Tharoor | "In the information age, a nation's power is increasingly defined by its ability to influence as much as to militarily and economically domi |
| 62 | 0320 | ""A nation's destiny is shaped by its geography but defined by its diplomacy."" | Shyam Saran | "A nation's destiny is shaped by its geography but defined by its diplomacy", "Shyam Saran" |
| 63 | 0333 | ""A budget is not just numbers on a page, it is an embodiment of our values."" | Barack Obama | "A budget is not just numbers on a page, it is an embodiment of our values" Obama, "A budget is not just numbers on a page, it is an embodim |
| 64 | 0341 | ""A vision without a plan is just a wish."" | Narendra Modi | "A vision without a plan is just a wish" Modi, "A vision without a plan is just a wish" |
| 65 | 0346 | ""Employment is not just about income—it’s about identity and dignity."" | World Bank | "Employment is not just about income—it’s about identity and dignity" "World Bank", "Employment is not just about income" "identity and dign |
| 66 | 0528 | ""Underdevelopment and inequality"" | hence need to imbibe Tribal Panchsheel principles in bringing peace & participative governance." — Antonio Guterres | "Tribal Panchsheel" "Antonio Guterres", "hence need to imbibe Tribal Panchsheel principles" Guterres |
| 67 | 0593 | ""Tolerance and patience are much stronger than brute force."" | Subhas Chandra Bose | "Tolerance and patience are much stronger than brute force", "Subhas Chandra Bose" "patience are much stronger than brute force" |
| 68 | 0602 | ""A public servant belongs to the people, not to a party."" | Sardar Vallabhbhai Patel | "A public servant belongs to the people, not to a party", "Sardar Vallabhbhai Patel" "belongs to the people, not to a party" |
| 69 | 0604 | ""It is easy to stand with the crowd. It takes courage to stand alone."" | Dr. A.P.J. Abdul Kalam | "It is easy to stand with the crowd. It takes courage to stand alone" Kalam, "It is easy to stand with the crowd. It takes courage to stand  |
| 70 | 0628 | ""A man is but the product of his thoughts and the environment he lives in."" | Mahatma Gandhi | "A man is but the product of his thoughts and the environment he lives in", Gandhi "product of his thoughts and the environment he lives in" |
| 71 | 0629 | ""You can change people’s minds by touching their hearts."" | Dr. A.P.J. Abdul Kalam | "You can change people’s minds by touching their hearts", "You can change people's minds by touching their hearts" Kalam |
| 72 | 0730 | ""The true ruler is the one who serves his people best."" | Chanakya | "The true ruler is the one who serves his people best", Chanakya "true ruler is the one who serves" |
| 73 | 0755 | ""A person who is morally educated will be a lot better equipped to move up the ladder of life."" | Dr. A.P.J. Abdul Kalam | "A person who is morally educated will be a lot better equipped to move up the ladder of life", Kalam "ladder of life" |
| 74 | 0756 | ""Power must always be accompanied by responsibility."" | Pandit Jawaharlal Nehru | "Power must always be accompanied by responsibility", Nehru "Power must always be accompanied by responsibility" |
| 75 | 0776 | ""The line between right and wrong is often drawn by self-interest."" | Nani Palkhivala | "The line between right and wrong is often drawn by self-interest", Palkhivala "drawn by self-interest" |

### Full details for Group A

#### A1. Card 0004
- **Quote:** "The story of India is written in stone."
- **Claimed author (booklet):** John Marshall
- **Gemini searched:** "The story of India is written in stone", "John Marshall" "story of India is written in stone"
- **Gemini notes:** No independent or authoritative historical source attributes this exact phrasing to archaeologist John Marshall.

#### A2. Card 0008
- **Quote:** "Technology as an ally of culture"
- **Claimed author (booklet):** PM Modi
- **Gemini searched:** "Technology as an ally of culture", "Technology as an ally of culture" Modi
- **Gemini notes:** No independent transcript or official speech records this phrase as a verbatim quote from PM Modi.

#### A3. Card 0020
- **Quote:** "Dance is the joy of the soul expressed through movement."
- **Claimed author (booklet):** Rabindranath Tagore
- **Gemini searched:** "Dance is the joy of the soul expressed through movement", "Dance is the joy of the soul expressed through movement" Tagore
- **Gemini notes:** Not found in Rabindranath Tagore's collected writings or lectures; matches only coaching booklet copies on Scribd.

#### A4. Card 0024
- **Quote:** "Indian music is a meditation, not a performance."
- **Claimed author (booklet):** Pandit Ravi Shankar
- **Gemini searched:** "Indian music is a meditation, not a performance", "Indian music is a meditation, not a performance" Ravi Shankar
- **Gemini notes:** Matches only the UPSC exam-prep booklet on Scribd; not found in any published writings, interviews, or biographies of Pandit Ravi Shankar.

#### A5. Card 0025
- **Quote:** "A nation’s folk music is its heartbeat."
- **Claimed author (booklet):** Jawaharlal Nehru
- **Gemini searched:** "A nation’s folk music is its heartbeat", "A nation's folk music is its heartbeat" Nehru
- **Gemini notes:** Not found in the Selected Works of Jawaharlal Nehru; appears only in coaching booklet mirrors.

#### A6. Card 0026
- **Quote:** "Theatre mirrors society and transforms it."
- **Claimed author (booklet):** Habib Tanvir
- **Gemini searched:** "Theatre mirrors society and transforms it", "Theatre mirrors society and transforms it" Habib Tanvir
- **Gemini notes:** Not found in published works or archival interviews of theatre director Habib Tanvir; exists only in the coaching booklet.

#### A7. Card 0027
- **Quote:** "In puppetry, silent hands speak louder than words."
- **Claimed author (booklet):** Satyajit Ray
- **Gemini searched:** "In puppetry, silent hands speak louder than words", "In puppetry, silent hands speak louder than words" Satyajit Ray
- **Gemini notes:** No published essays or interviews of Satyajit Ray contain this line; matches only the Scribd booklet.

#### A8. Card 0028
- **Quote:** "Martial arts train the body to protect and the mind to persevere."
- **Claimed author (booklet):** Bruce Lee
- **Gemini searched:** "Martial arts train the body to protect and the mind to persevere", "Bruce Lee" "mind to persevere"
- **Gemini notes:** Not found in Bruce Lee's writings (e.g. Tao of Jeet Kune Do) or estate archives; appears only in the Scribd booklet.

#### A9. Card 0037
- **Quote:** "The Vedas are not books of theology but records of spiritual discovery."
- **Claimed author (booklet):** Sarvepalli Radhakrishnan
- **Gemini searched:** "The Vedas are not books of theology but records of spiritual discovery", Radhakrishnan "records of spiritual discovery"
- **Gemini notes:** Not found in Sarvepalli Radhakrishnan's philosophical treatises; appears only in the coaching booklet.

#### A10. Card 0038
- **Quote:** "Sangam poetry is not just emotion  it is geography, economy, and politics in verse."
- **Claimed author (booklet):** A.K. Ramanujan
- **Gemini searched:** "Sangam poetry is not just emotion", "Sangam poetry is not just emotion it is geography, economy, and politics in verse"
- **Gemini notes:** Not found in A.K. Ramanujan's translations or scholarship (such as The Interior Landscape or Poems of Love and War); exists only in the coaching booklet.

#### A11. Card 0039
- **Quote:** "Silence and simplicity are the roots of liberation."
- **Claimed author (booklet):** Mahavira
- **Gemini searched:** "Silence and simplicity are the roots of liberation", "Silence and simplicity are the roots of liberation" Mahavira
- **Gemini notes:** Not found in Jain canonical literature or scholarly translations of Mahavira's teachings; appears only in the coaching booklet.

#### A12. Card 0040
- **Quote:** "Persian in India was not just a language, it was the canvas for Indo-Islamic creativity."
- **Claimed author (booklet):** Muzaffar Alam
- **Gemini searched:** "Persian in India was not just a language, it was the canvas for Indo-Islamic creativity", Muzaffar Alam "canvas for Indo-Islamic creativity"
- **Gemini notes:** Not found in historian Muzaffar Alam's published scholarship; appears only in the coaching booklet.

#### A13. Card 0041
- **Quote:** "A nation is built by those who write its soul into words."
- **Claimed author (booklet):** Rabindranath Tagore
- **Gemini searched:** "A nation is built by those who write its soul into words", Tagore "write its soul into words"
- **Gemini notes:** Not found in Rabindranath Tagore's writings; appears only in the coaching booklet.

#### A14. Card 0047
- **Quote:** "The diverse threads of society wove together in the fabric of the freedom struggle."
- **Claimed author (booklet):** Bipin Chandra Pal
- **Gemini searched:** "The diverse threads of society wove together in the fabric of the freedom struggle", "Bipin Chandra Pal" "fabric of the freedom struggle"
- **Gemini notes:** Not found in the historical speeches or writings of Bipin Chandra Pal; appears only in the coaching booklet.

#### A15. Card 0049
- **Quote:** "The seeds of freedom must be sown in the soil of unity."
- **Claimed author (booklet):** Gopal Krishna Gokhale
- **Gemini searched:** "The seeds of freedom must be sown in the soil of unity", "Gopal Krishna Gokhale" "soil of unity"
- **Gemini notes:** Not found in speeches or writings of Gopal Krishna Gokhale; exists only in the coaching booklet.

#### A16. Card 0050
- **Quote:** "You may never know what results come of your actions, but if you do nothing, there will be no result."
- **Claimed author (booklet):** Mahatma Gandhi
- **Gemini searched:** "You may never know what results come of your actions, but if you do nothing, there will be no result", "Collected Works of Mahatma Gandhi" "results come of your actions"
- **Gemini notes:** Popular internet quote frequently misattributed to Gandhi on quote blogs, but absent from the 100 volumes of The Collected Works of Mahatma Gandhi.

#### A17. Card 0081
- **Quote:** "Liberty, equality, fraternity these are not mere words, they are our guiding principles."
- **Claimed author (booklet):** Nelson Mandela
- **Gemini searched:** "Liberty, equality, fraternity these are not mere words", "Nelson Mandela" "these are not mere words, they are our guiding principles"
- **Gemini notes:** Not found in Nelson Mandela's archive of speeches, letters, or presidential addresses; matches only the Scribd booklet.

#### A18. Card 0082
- **Quote:** "The sun never set on the British Empire but it never rose on its justice."
- **Claimed author (booklet):** Shashi Tharoor
- **Gemini searched:** "The sun never set on the British Empire but it never rose on its justice", "Shashi Tharoor" "never rose on its justice"
- **Gemini notes:** Not found in Shashi Tharoor's books (such as Inglorious Empire / An Era of Darkness) or speeches; matches only the Scribd booklet.

#### A19. Card 0084
- **Quote:** "The factory system was the beginning of man being reduced to a number."
- **Claimed author (booklet):** Mahatma Gandhi
- **Gemini searched:** "The factory system was the beginning of man being reduced to a number", Gandhi "factory system was the beginning"
- **Gemini notes:** Not found in Mahatma Gandhi's collected works or writings on machinery and industrialism; appears only in the Scribd booklet.

#### A20. Card 0086
- **Quote:** "India is a garden of many flowers"
- **Claimed author (booklet):** each one beautiful, each one unique." — Jawaharlal Nehru
- **Gemini searched:** "India is a garden of many flowers", "India is a garden of many flowers each one beautiful, each one unique" Nehru
- **Gemini notes:** Not found in the Selected Works of Jawaharlal Nehru; matches only the coaching booklet mirrors.

#### A21. Card 0096
- **Quote:** "Social justice is the first condition of humanity."
- **Claimed author (booklet):** B. R. Ambedkar
- **Gemini searched:** "Social justice is the first condition of humanity", "Social justice is the first condition of humanity" Ambedkar
- **Gemini notes:** Not found in Dr. B.R. Ambedkar's writings and speeches published by the Government of India or MEA; appears only in coaching booklet text.

#### A22. Card 0099
- **Quote:** "Religion is a personal matter, not a political weapon."
- **Claimed author (booklet):** Jawaharlal Nehru
- **Gemini searched:** "Religion is a personal matter, not a political weapon", Nehru "Religion is a personal matter, not a political weapon"
- **Gemini notes:** Not found in Jawaharlal Nehru's published works or speeches; matches only the Scribd booklet.

#### A23. Card 0100
- **Quote:** "India is a union of states, not a confederation of ambitions."
- **Claimed author (booklet):** Sardar Patel
- **Gemini searched:** "India is a union of states, not a confederation of ambitions", "Sardar Patel" "confederation of ambitions"
- **Gemini notes:** Not found in Sardar Vallabhbhai Patel's speeches or correspondence; appears only in the Scribd booklet.

#### A24. Card 0103
- **Quote:** "Secularism is the soul of the Indian Constitution."
- **Claimed author (booklet):** Rajendra Prasad
- **Gemini searched:** "Secularism is the soul of the Indian Constitution", "Rajendra Prasad" "soul of the Indian Constitution"
- **Gemini notes:** Not found in Dr. Rajendra Prasad's Constituent Assembly addresses or presidential speeches; appears only in coaching booklet notes.

#### A25. Card 0105
- **Quote:** "Urban governance is not just administration  it is transformation."
- **Claimed author (booklet):** E. Sreedharan
- **Gemini searched:** "Urban governance is not just administration it is transformation", "E. Sreedharan" "is transformation"
- **Gemini notes:** Not found in any speeches, writings, or interviews of 'Metro Man' E. Sreedharan; matches only the Scribd booklet.

#### A26. Card 0107
- **Quote:** "Energy is necessary for development & sustainable energy is necessary for sustainable development"
- **Claimed author (booklet):** Tim Wirth
- **Gemini searched:** "Energy is necessary for development & sustainable energy is necessary for sustainable development", "Energy is necessary for development" "Tim Wirth"
- **Gemini notes:** No authoritative record or transcript confirms this exact verbatim phrasing by Timothy Wirth; matches only the coaching booklet.

#### A27. Card 0131
- **Quote:** "The environment and the economy are really both two sides of the same coin. You cannot sustain the economy if you don't take care of the environment."
- **Claimed author (booklet):** Bruce Lipton
- **Gemini searched:** "The environment and the economy are really both two sides of the same coin", "Bruce Lipton" "cannot sustain the economy if you don't take care of the environment"
- **Gemini notes:** Not found in biologist Bruce Lipton's published works or lectures; exists only in the coaching booklet.

#### A28. Card 0133
- **Quote:** "Industries go where they are wanted, and stay where they are treated well."
- **Claimed author (booklet):** Ronald Reagan
- **Gemini searched:** "Industries go where they are wanted, and stay where they are treated well", "Ronald Reagan" "where they are treated well"
- **Gemini notes:** Traditional American economic adage / chambers of commerce slogan, not found in Ronald Reagan's presidential papers or speeches; appears only in the Scribd booklet.

#### A29. Card 0157
- **Quote:** "While we borrowed from many, we built for Bharat."
- **Claimed author (booklet):** Dr. B.R. Ambedkar
- **Gemini searched:** "While we borrowed from many, we built for Bharat", Ambedkar "While we borrowed from many, we built for Bharat"
- **Gemini notes:** Not found in the Constituent Assembly Debates or Dr. Ambedkar's writings; matches only the Scribd booklet.

#### A30. Card 0158
- **Quote:** "Parliamentary democracy is the bedrock of India's governance, where diverse voices converge to shape the nation's destiny."
- **Claimed author (booklet):** ABV (Atal Bihari Vajpayee)
- **Gemini searched:** "Parliamentary democracy is the bedrock of India's governance", Vajpayee "bedrock of India's governance"
- **Gemini notes:** Not found in Atal Bihari Vajpayee's parliamentary speeches or collected works; appears only in the Scribd booklet.

#### A31. Card 0159
- **Quote:** "Amendment is the lifeline of a living Constitution."
- **Claimed author (booklet):** Nani Palkhivala
- **Gemini searched:** "Amendment is the lifeline of a living Constitution", Palkhivala "Amendment is the lifeline of a living Constitution"
- **Gemini notes:** Not found in Nani Palkhivala's 'We, the People' or 'We, the Nation'; appears only in the Scribd booklet.

#### A32. Card 0178
- **Quote:** "Free & Fair elections are the lifeblood of any democracy."
- **Claimed author (booklet):** Jimmy Carter
- **Gemini searched:** "Free & Fair elections are the lifeblood of any democracy", "Jimmy Carter" "lifeblood of any democracy"
- **Gemini notes:** Not found verbatim in Jimmy Carter's speeches or Carter Center publications; matches only coaching booklet mirrors.

#### A33. Card 0179
- **Quote:** "When the power of a vote is diluted through opacity in political funding, democracy loses its intrinsic value."
- **Claimed author (booklet):** Ornit Shani
- **Gemini searched:** "When the power of a vote is diluted through opacity in political funding", "Ornit Shani" "opacity in political funding"
- **Gemini notes:** Not found in historian Ornit Shani's book 'How India Became Democratic' or scholarly articles; appears only in the Scribd booklet.

#### A34. Card 0181
- **Quote:** "Free & Fair elections are lifeblood of any democracy"
- **Claimed author (booklet):** Jimmy Carter
- **Gemini searched:** "Free & Fair elections are lifeblood of any democracy", "Jimmy Carter" "elections are lifeblood of any democracy"
- **Gemini notes:** Identical to quote 54; not found in authoritative sources for Jimmy Carter, appears only in the Scribd booklet.

#### A35. Card 0184
- **Quote:** "Like a cancer, eating into the vitals of a democracy."
- **Claimed author (booklet):** Delhi HC 2018
- **Gemini searched:** "Like a cancer, eating into the vitals of a democracy", "Delhi High Court 2018 cancer democracy electoral bonds"
- **Gemini notes:** No independent source confirms the exact phrasing. NLU Delhi document uses similar but different wording.

#### A36. Card 0185
- **Quote:** "When the power of a vote is diluted through opacity in political funding, democracy loses its intrinsic value"
- **Claimed author (booklet):** Ornit Shani
- **Gemini searched:** "When the power of a vote is diluted through opacity in political funding, democracy loses its intrinsic value", "Ornit Shani"
- **Gemini notes:** Identical to quote 55; no independent source confirms this phrasing for Ornit Shani.

#### A37. Card 0186
- **Quote:** "Democracy at the grassroots is democracy at its strongest."
- **Claimed author (booklet):** Mahatma Gandhi
- **Gemini searched:** "Democracy at the grassroots is democracy at its strongest", Gandhi "grassroots is democracy at its strongest"
- **Gemini notes:** Not found in Mahatma Gandhi's writings on Panchayati Raj or Gram Swaraj; appears only in the Scribd booklet.

#### A38. Card 0189
- **Quote:** "Cooperative federalism is not a choice; it is a constitutional compulsion."
- **Claimed author (booklet):** PM Narendra Modi
- **Gemini searched:** "Cooperative federalism is not a choice; it is a constitutional compulsion", Modi "constitutional compulsion"
- **Gemini notes:** Not found in PM Narendra Modi's official speeches or PIB releases; matches only the Scribd booklet.

#### A39. Card 0199
- **Quote:** "A free press should neither be an ally nor an adversary but a constructive critic."
- **Claimed author (booklet):** Gandhiji
- **Gemini searched:** "A free press should neither be an ally nor an adversary but a constructive critic", Gandhi "ally nor an adversary"
- **Gemini notes:** Not found in Mahatma Gandhi's writings on journalism or Indian Opinion; exists only in the coaching booklet.

#### A40. Card 0200
- **Quote:** "Social media is a double-edged sword."
- **Claimed author (booklet):** Noam Chomsky
- **Gemini searched:** "Social media is a double-edged sword" Chomsky
- **Gemini notes:** Generic cliché not found in Noam Chomsky's published writings or lectures on media and propaganda.

#### A41. Card 0201
- **Quote:** "In democracy, even silence can organise into influence."
- **Claimed author (booklet):** Granville Austin
- **Gemini searched:** "In democracy, even silence can organise into influence", "Granville Austin" "silence can organise into influence"
- **Gemini notes:** Not found in constitutional historian Granville Austin's 'The Indian Constitution: Cornerstone of a Nation' or 'Working a Democratic Constitution'; appears only in the Scribd booklet.

#### A42. Card 0209
- **Quote:** "Governor's actions must be tempered with caution, dictated by reason & activated in good faith."
- **Claimed author (booklet):** Sarkaria Commission
- **Gemini searched:** "Governor's actions must be tempered with caution, dictated by reason & activated in good faith", "Sarkaria Commission" Governor "tempered with caution"
- **Gemini notes:** Not found in the official 1988 Sarkaria Commission Report on Centre-State Relations; appears only in the Scribd booklet.

#### A43. Card 0211
- **Quote:** "Justice is not simply punishing the guilty, but also defending the innocent and ensuring due process for all."
- **Claimed author (booklet):** Kofi Annan
- **Gemini searched:** "Justice is not simply punishing the guilty, but also defending the innocent and ensuring due process for all", "Kofi Annan"
- **Gemini notes:** Not found in Kofi Annan's UN speeches, reports, or memoirs; appears only in the Scribd booklet.

#### A44. Card 0216
- **Quote:** "Accountability & integrity increase a court's prestige & faith rather than reducing it."
- **Claimed author (booklet):** Justice Hidayatullah, in Naresh Sridhar Case
- **Gemini searched:** "Accountability & integrity increase a court's prestige & faith rather than reducing it", Hidayatullah "Naresh Sridhar"
- **Gemini notes:** Not found in Justice Hidayatullah's judgment in Naresh Shridhar Mirajkar v. State of Maharashtra (1966 3 SCR 744); exists only in the coaching booklet.

#### A45. Card 0225
- **Quote:** "Civil servants are the steel frame but must also be the spinal nerve of reform."
- **Claimed author (booklet):** Sardar Patel
- **Gemini searched:** "Civil servants are the steel frame but must also be the spinal nerve of reform", "Sardar Patel" "spinal nerve"
- **Gemini notes:** Patel coined the term 'steel frame' for civil servants in 1947, but the second half ('spinal nerve of reform') is an unverified modern invention appearing only in the Scribd booklet.

#### A46. Card 0226
- **Quote:** "Civil servants are the silent architects of a nation's progress, dedicated to translating policies into actions that shape the destiny of India."
- **Claimed author (booklet):** Dr. APJ Abdul Kalam
- **Gemini searched:** "Civil servants are the silent architects of a nation's progress", Kalam "silent architects of a nation's progress"
- **Gemini notes:** Not found in Dr. A.P.J. Abdul Kalam's books or speeches; appears only in the Scribd booklet.

#### A47. Card 0226
- **Quote:** "Civil servants are the bridge that connects government policies with the aspirations and welfare of the people they serve."
- **Claimed author (booklet):** NR Narayana Murthy
- **Gemini searched:** "Civil servants are the bridge that connects government policies with the aspirations", "Narayana Murthy"
- **Gemini notes:** Not found in N.R. Narayana Murthy's speeches or books; appears only in the Scribd booklet.

#### A48. Card 0229, 0233
- **Quote:** "Without accountability, resources are wasted, corruption flourishes, and trust in institutions is eroded."
- **Claimed author (booklet):** Ban Ki-moon
- **Gemini searched:** "Without accountability, resources are wasted, corruption flourishes, and trust in institutions is eroded", "Ban Ki-moon"
- **Gemini notes:** Not found in Ban Ki-moon's UN addresses or official statements; appears only in the Scribd booklet.

#### A49. Card 0230
- **Quote:** "RTI is the most important legislation since independence. It marks the beginning of an era of dawn & ends the era of darkness."
- **Claimed author (booklet):** ARC 2
- **Gemini searched:** "RTI is the most important legislation since independence. It marks the beginning of an era of dawn & ends the era of darkness", "Second ARC" RTI
- **Gemini notes:** Not found in the Second Administrative Reforms Commission's First Report 'Right to Information: Master Key to Good Governance'; matches only the Scribd booklet.

#### A50. Card 0231
- **Quote:** "Social audit is not just an evaluation of programs; it's an assertion of people's rights to dignity, transparency, and accountable governance."
- **Claimed author (booklet):** Aruna Roy
- **Gemini searched:** "Social audit is not just an evaluation of programs; it's an assertion of people's rights to dignity", "Aruna Roy"
- **Gemini notes:** Not found verbatim in activist Aruna Roy's published writings or MKSS documentation; appears only in the Scribd booklet.

#### A51. Card 0237
- **Quote:** "The CAG is the conscience keeper of government finances, ensuring that taxpayer money is used judiciously and efficiently."
- **Claimed author (booklet):** Rajiv Mehrishi (former Finance Secretary)
- **Gemini searched:** "The CAG is the conscience keeper of government finances, ensuring that taxpayer money is used judiciously and efficiently", "Rajiv Mehrishi"
- **Gemini notes:** Not found in speeches or press statements of former CAG Rajiv Mehrishi; appears only in the Scribd booklet.

#### A52. Card 0263
- **Quote:** "Good policies fail with bad implementation; bad policies fail faster."
- **Claimed author (booklet):** Second ARC
- **Gemini searched:** "Good policies fail with bad implementation; bad policies fail faster", "Second ARC" "bad policies fail faster"
- **Gemini notes:** Not found in any of the 15 reports of the Second Administrative Reforms Commission; appears only in the Scribd booklet.

#### A53. Card 0268
- **Quote:** "The development sector is not third sector it is the frontline of inclusive governance."
- **Claimed author (booklet):** Abhijit Banerjee
- **Gemini searched:** "The development sector is not third sector it is the frontline of inclusive governance", "Abhijit Banerjee"
- **Gemini notes:** Not found in Nobel laureate Abhijit Banerjee's books (such as Poor Economics / Good Economics for Hard Times); appears only in the Scribd booklet.

#### A54. Card 0282
- **Quote:** "An educated, healthy population is not a burden it is the foundation of any civilised society."
- **Claimed author (booklet):** Amartya Sen
- **Gemini searched:** "An educated, healthy population is not a burden it is the foundation of any civilised society", "Amartya Sen"
- **Gemini notes:** Not found in Amartya Sen's books (such as Development as Freedom) or academic papers; appears only in the Scribd booklet.

#### A55. Card 0287
- **Quote:** "The test of good governance is how it treats its weakest citizens."
- **Claimed author (booklet):** Mahatma Gandhi
- **Gemini searched:** "The test of good governance is how it treats its weakest citizens", Gandhi "test of good governance"
- **Gemini notes:** A rephrasing of the common maxim, but not found in Mahatma Gandhi's collected works; appears only in the Scribd booklet.

#### A56. Card 0289
- **Quote:** "The Constitution is a transformative document it enshrines not charity but rights."
- **Claimed author (booklet):** Justice Indu Malhotra
- **Gemini searched:** "The Constitution is a transformative document it enshrines not charity but rights", "Indu Malhotra"
- **Gemini notes:** Not found in Justice Indu Malhotra's Supreme Court opinions (such as Navtej Singh Johar or Sabarimala); exists only in the coaching booklet.

#### A57. Card 0295
- **Quote:** "A budget tells us what we value as a society."
- **Claimed author (booklet):** UN Women
- **Gemini searched:** "A budget tells us what we value as a society", "UN Women" "tells us what we value as a society"
- **Gemini notes:** Paraphrase of Joe Biden's / Paul Wellstone's budget quote ('Show me your budget, and I will tell you what you value'), not found verbatim in UN Women publications.

#### A58. Card 0301
- **Quote:** "In a world full of fault lines and rifts, we need to build a shared future."
- **Claimed author (booklet):** Modi
- **Gemini searched:** "In a world full of fault lines and rifts, we need to build a shared future", Modi "fault lines and rifts"
- **Gemini notes:** PM Modi spoke on the Davos 2018 theme 'Creating a Shared Future in a Fractured World' and referenced fractures, but this exact phrasing is not found in official transcripts.

#### A59. Card 0301
- **Quote:** "India has entered a phase of energetic foreign policy where it is not anymore a passive recipient of global happenings."
- **Claimed author (booklet):** S. Jaishankar
- **Gemini searched:** "India has entered a phase of energetic foreign policy where it is not anymore a passive recipient of global happenings", Jaishankar "passive recipient of global happenings"
- **Gemini notes:** Not found in EAM S. Jaishankar's speeches or his book 'The India Way'; exists only in the Scribd booklet.

#### A60. Card 0304
- **Quote:** "The Indian Ocean, with its critical sea lanes and vast reservoir of resources, will be a highway to prosperity and a theatre of rivalry."
- **Claimed author (booklet):** C. Raja Mohan
- **Gemini searched:** "The Indian Ocean, with its critical sea lanes and vast reservoir of resources, will be a highway to prosperity and a theatre of rivalry", "C. Raja Mohan" "theatre of rivalry"
- **Gemini notes:** Not found in strategic analyst C. Raja Mohan's published columns or books (such as Samudra Manthan); appears only in the Scribd booklet.

#### A61. Card 0305
- **Quote:** "In the information age, a nation's power is increasingly defined by its ability to influence as much as to militarily and economically dominate."
- **Claimed author (booklet):** Shashi Tharoor
- **Gemini searched:** "In the information age, a nation's power is increasingly defined by its ability to influence as much as to militarily and economically dominate", "Shashi Tharoor"
- **Gemini notes:** Not found in Shashi Tharoor's writings on soft power or foreign policy (such as Pax Indica); appears only in the Scribd booklet.

#### A62. Card 0320
- **Quote:** "A nation's destiny is shaped by its geography but defined by its diplomacy."
- **Claimed author (booklet):** Shyam Saran
- **Gemini searched:** "A nation's destiny is shaped by its geography but defined by its diplomacy", "Shyam Saran"
- **Gemini notes:** Not found in former Foreign Secretary Shyam Saran's 'How India Sees the World'; matches only the Scribd booklet.

#### A63. Card 0333
- **Quote:** "A budget is not just numbers on a page, it is an embodiment of our values."
- **Claimed author (booklet):** Barack Obama
- **Gemini searched:** "A budget is not just numbers on a page, it is an embodiment of our values" Obama, "A budget is not just numbers on a page, it is an embodiment of our values"
- **Gemini notes:** President Obama frequently described budgets as 'values statements', but this exact wording is not verified in presidential transcripts; appears only in the Scribd booklet.

#### A64. Card 0341
- **Quote:** "A vision without a plan is just a wish."
- **Claimed author (booklet):** Narendra Modi
- **Gemini searched:** "A vision without a plan is just a wish" Modi, "A vision without a plan is just a wish"
- **Gemini notes:** Popular management proverb (often attributed to Antoine de Saint-Exupéry or Larry Elder as 'A goal without a plan is just a wish'); not found in PM Modi's official speeches.

#### A65. Card 0346
- **Quote:** "Employment is not just about income—it’s about identity and dignity."
- **Claimed author (booklet):** World Bank
- **Gemini searched:** "Employment is not just about income—it’s about identity and dignity" "World Bank", "Employment is not just about income" "identity and dignity"
- **Gemini notes:** World Development Report 2013 on Jobs discusses jobs, identity, and dignity, but this exact quote sentence does not appear in World Bank publications.

#### A66. Card 0528
- **Quote:** "Underdevelopment and inequality"
- **Claimed author (booklet):** hence need to imbibe Tribal Panchsheel principles in bringing peace & participative governance." — Antonio Guterres
- **Gemini searched:** "Tribal Panchsheel" "Antonio Guterres", "hence need to imbibe Tribal Panchsheel principles" Guterres
- **Gemini notes:** Tribal Panchsheel is Jawaharlal Nehru's 1950s policy framework; UN Secretary-General António Guterres has no record of invoking Nehru's Tribal Panchsheel principles.

#### A67. Card 0593
- **Quote:** "Tolerance and patience are much stronger than brute force."
- **Claimed author (booklet):** Subhas Chandra Bose
- **Gemini searched:** "Tolerance and patience are much stronger than brute force", "Subhas Chandra Bose" "patience are much stronger than brute force"
- **Gemini notes:** Not found in Netaji's collected speeches or writings; appears only in the Scribd booklet.

#### A68. Card 0602
- **Quote:** "A public servant belongs to the people, not to a party."
- **Claimed author (booklet):** Sardar Vallabhbhai Patel
- **Gemini searched:** "A public servant belongs to the people, not to a party", "Sardar Vallabhbhai Patel" "belongs to the people, not to a party"
- **Gemini notes:** Not found in Sardar Patel's address to the Indian Administrative Service probationers at Metcalf House (April 1947); exists only in the coaching booklet.

#### A69. Card 0604
- **Quote:** "It is easy to stand with the crowd. It takes courage to stand alone."
- **Claimed author (booklet):** Dr. A.P.J. Abdul Kalam
- **Gemini searched:** "It is easy to stand with the crowd. It takes courage to stand alone" Kalam, "It is easy to stand with the crowd. It takes courage to stand alone"
- **Gemini notes:** Internet inspirational quote attributed to various figures; not verified in Dr. APJ Abdul Kalam's published books or speeches.

#### A70. Card 0628
- **Quote:** "A man is but the product of his thoughts and the environment he lives in."
- **Claimed author (booklet):** Mahatma Gandhi
- **Gemini searched:** "A man is but the product of his thoughts and the environment he lives in", Gandhi "product of his thoughts and the environment he lives in"
- **Gemini notes:** Gandhi's authentic statement in Ethical Religion (1922) is 'A man is but the product of his thoughts. What he thinks, he becomes.' The modified text adding 'and the environment he lives in' does not appear in Gandhi's writings.

#### A71. Card 0629
- **Quote:** "You can change people’s minds by touching their hearts."
- **Claimed author (booklet):** Dr. A.P.J. Abdul Kalam
- **Gemini searched:** "You can change people’s minds by touching their hearts", "You can change people's minds by touching their hearts" Kalam
- **Gemini notes:** Not found in Dr. A.P.J. Abdul Kalam's books, speeches, or quotes; appears only in the Scribd booklet.

#### A72. Card 0730
- **Quote:** "The true ruler is the one who serves his people best."
- **Claimed author (booklet):** Chanakya
- **Gemini searched:** "The true ruler is the one who serves his people best", Chanakya "true ruler is the one who serves"
- **Gemini notes:** While Chanakya's Arthashastra contains the maxim 'In the happiness of his subjects lies the king's happiness', the exact phrasing 'The true ruler is the one who serves his people best' is an unverified modern paraphrase appearing only in the Scribd booklet.

#### A73. Card 0755
- **Quote:** "A person who is morally educated will be a lot better equipped to move up the ladder of life."
- **Claimed author (booklet):** Dr. A.P.J. Abdul Kalam
- **Gemini searched:** "A person who is morally educated will be a lot better equipped to move up the ladder of life", Kalam "ladder of life"
- **Gemini notes:** Not found in Dr. A.P.J. Abdul Kalam's books or speeches; exists only in the coaching booklet.

#### A74. Card 0756
- **Quote:** "Power must always be accompanied by responsibility."
- **Claimed author (booklet):** Pandit Jawaharlal Nehru
- **Gemini searched:** "Power must always be accompanied by responsibility", Nehru "Power must always be accompanied by responsibility"
- **Gemini notes:** Variant of the classic 'With great power comes great responsibility' adage; not found in Jawaharlal Nehru's speeches or writings, appears only in the Scribd booklet.

#### A75. Card 0776
- **Quote:** "The line between right and wrong is often drawn by self-interest."
- **Claimed author (booklet):** Nani Palkhivala
- **Gemini searched:** "The line between right and wrong is often drawn by self-interest", Palkhivala "drawn by self-interest"
- **Gemini notes:** Not found in Nani Palkhivala's speeches, essays, or legal writings; exists only in the coaching booklet.

---

## Group B — MISATTRIBUTED, but I couldn't safely apply the fix

Gemini verified the attribution is WRONG and identified the real author. But the wrong attribution (`CS Lewis:` or `Voltaire -`) is **embedded inside the protected quote text**. Removing it would require editing the protected text, which the user rule forbids.

**Your options per card:**
- (a) **Replace the entire quote block** with a different verified quote on the same theme.
- (b) **Replace the quote text** with a real CS Lewis / Voltaire quote (requires approve-listing the new text).
- (c) **Empty the quote block** (leave `:::quote\n:::` shell).
- (d) **Leave as-is** (accept the embedded misattribution).

### B1. Card 0607
- **Quote (as it appears in booklet):** "CS Lewis: Integrity is doing the right thing even when no one is watching."
- **Claimed author (booklet):** (no attribution in booklet)
- **Actual author (Gemini-verified):** Anonymous / J. C. Watts (popularly misattributed to C.S. Lewis)
- **Source:** https://www.samyoung.co.nz/2016/03/integrity-is-doing-right-thing-even.html
- **Source snippet:** "The saying, 'Integrity is doing the right thing, even when no one is watching' is often misattributed to C. S. Lewis, even referenced to his books... And we know it is not in C. S. Lewis's writings."
- **Notes:** Booklet incorporated 'CS Lewis:' into the quote text without a separate attribution field. The quote is a widespread misattribution not found in any of C.S. Lewis's works.

### B2. Card 0715
- **Quote (as it appears in booklet):** "Voltaire"
- **Claimed author (booklet):** 'I may not agree with what you say but I will fight to death your right to say it'"
- **Actual author (Gemini-verified):** Evelyn Beatrice Hall (1906)
- **Source:** https://en.wikipedia.org/wiki/Evelyn_Beatrice_Hall
- **Source snippet:** "In The Friends of Voltaire (1906), Hall wrote: 'I disapprove of what you say, but I will defend to the death your right to say it' as an illustration of Voltaire's beliefs."
- **Notes:** Booklet attributed the quote to Voltaire. Coined by English biographer Evelyn Beatrice Hall (writing under the pseudonym S. G. Tallentyre) to summarize Voltaire's attitude towards Claude Adrien Helvétius.

---

## Group C — Booklet has NO attribution; Gemini found the real author

The booklet left these quotes unattributed. Gemini's web search identified the actual author. Adding the attribution would be **creating new content** (not correcting a wrong attribution), so per your rule I did not act.

**Your options per card:**
- (a) **Add the attribution** — change `"Quote text"` to `"Quote text" — Author (year)`.
- (b) **Leave unattributed** — keep as the booklet author chose.

### C1. Card 0120
- **Quote:** "Resources are not, they become."
- **Booklet (current):** no attribution
- **Actual author (Gemini-verified):** Erich Walter Zimmermann (1933)
- **Source:** https://circulareconomyasia.org/resources/
- **Source snippet:** "According to Eric Walter Zimmermann, a German resource economist, 'resources are not, they become.'"
- **Notes:** Booklet included the quote with no author attribution. Famous aphorism from Erich W. Zimmermann's seminal 1933 treatise 'World Resources and Industries'.

### C2. Card 0142
- **Quote:** "Nature does not hurry, yet everything is accomplished."
- **Booklet (current):** no attribution
- **Actual author (Gemini-verified):** Lao Tzu
- **Source:** https://medium.com/@patrickbyron/nature-does-not-hurry-yet-everything-is-accomplished-lao-tzu-5f405c3e4769
- **Source snippet:** "Nature does not hurry, yet everything is accomplished. ― Lao Tzu"
- **Notes:** Booklet provided no attribution. The line is a classic English rendering of Lao Tzu's Daoist principle of Wu Wei from the Tao Te Ching.

### C3. Card 0610
- **Quote:** "In looking for people to hire, you look for three qualities: integrity, intelligence and energy. And if they don't have the first, the other two will kill you."
- **Booklet (current):** no attribution
- **Actual author (Gemini-verified):** Warren Buffett
- **Source:** https://www.goodreads.com/quotes/76790-somebody-once-said-that-in-looking-for-people-to-hire
- **Source snippet:** "Somebody once said that in looking for people to hire, you look for three qualities: integrity, intelligence, and energy. And if you don't have the first, the other two will kill you. — Warren Buffett"
- **Notes:** Booklet provided no attribution. The famous hiring maxim was popularized by Warren Buffett in his speeches to business school students and Berkshire Hathaway shareholder meetings.
