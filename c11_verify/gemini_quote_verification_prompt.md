# Quote-attribution verification request for Google Gemini

## Task

You are a research assistant verifying quotes in a UPSC exam-prep ebook. The book's enrichment layer invented or mis-attributed many quotes; we are correcting them.

For EACH quote below, **web-search the exact quote text** (use quotation marks around the quote) and decide one of three verdicts:

- **VERIFIED_CORRECT** — the quote text appears in an independent, authoritative source (Wikipedia/Wikiquote, news site, government/institutional site, scholarly article, court judgment, book) AND the source credits the SAME author as the booklet claims.
- **VERIFIED_MISATTRIBUTED** — the quote text appears in an independent source, but the source credits a DIFFERENT author than the booklet claims. Identify the real author.
- **UNVERIFIABLE** — you cannot find the quote text in any independent source, or the only matches are copies of the booklet itself (Scribd/Slideshare mirrors of "GS-2 Ready-Made Introductions & Conclusions" / "UPSC GS-3 Intro & Conclusion Guide" / similar X-IAS titles).

### Important rules

1. **Never trust the booklet or its mirrors** as a source. The booklet is at https://www.scribd.com/document/909691889/Gs-2-Intro-Conclusions-by-x-Ias and similar. Copies of it do NOT confirm the attribution.
2. **Quote text is protected.** Do not propose changing the quote text itself. Only the attribution label (`— Author Name`) is in question.
3. **Be strict.** A Wikipedia article ABOUT the person does not verify the quote. The source must contain the actual quote text.
4. **For Indian court judgments / committee reports** (Delhi HC, Second ARC, Law Commission, ECI, CAG, etc.): try to locate the original judgment or report. If the exact phrasing isn't in the published judgment/report, mark UNVERIFIABLE even if the gist matches.
5. **Social-media posts (Facebook, Instagram, Quora, Reddit, Pinterest) are NOT authoritative.** Use them only as leads, not as confirmation.
6. **If you find a misattribution, give the real author and a verifiable URL.** Do not guess.

## Reply format (strict — I will parse it)

For EACH quote in the list below, output exactly one block. Use the heading level `###` and the field names exactly as shown. Use Markdown bullet list with `- key: value`. Leave one blank line between entries. Do not add prose outside these blocks.

### VERIFIED_CORRECT
- card_ids: 0003
- quote_text: "Buddha's teachings can solve most contemporary global problems"
- claimed_author: PM Modi
- actual_author: PM Modi
- source_url: https://www.thehindu.com/news/national/buddhas-teachings-can-solve-most-contemporary-global-problems-pm-modi/article66721324.ece
- source_snippet: "Buddha's teachings can solve most contemporary global problems: PM Modi. India has been following the path shown by the Buddha..."
- notes: optional short note (omit if none)

### VERIFIED_MISATTRIBUTED
- card_ids: 0230
- quote_text: "Sunlight is the best disinfectant."
- claimed_author: 2nd ARC
- actual_author: Justice Louis Brandeis (1913)
- source_url: https://en.wikipedia.org/wiki/Louis_Brandeis#Sunlight_is_the_best_of_disinfectants
- source_snippet: "Brandeis made his famous statement that 'sunlight is said to be the best of disinfectants' in a 1913 Harper's Weekly article, entitled 'What Publicity Can Do'."
- notes: 2nd ARC's RTI report quoted Brandeis; booklet presented it as 2nd ARC's own line.

### UNVERIFIABLE
- card_ids: 0184
- quote_text: "Like a cancer, eating into the vitals of a democracy."
- claimed_author: Delhi HC 2018
- searched_queries: "Like a cancer eating into the vitals of a democracy", "Delhi High Court 2018 cancer democracy electoral bonds"
- notes: no independent source confirms the exact phrasing. NLU Delhi document uses similar but different wording.

## Reply must include every one of the 128 quotes below

Process them in order. If you cannot decide, mark UNVERIFIABLE. **Do not skip any.**

---

## Quotes to verify (128 unique quote texts across Tiers A + B + C)

### 1. card_ids: 0003
- quote_text: ""Buddha's teachings can solve most contemporary global problems" — PM Modi"
- claimed_author: PM Modi
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: www.thehindu.com, www.zenithacademy.com, en.wikipedia.org, edurev.in

### 2. card_ids: 0004
- quote_text: ""The story of India is written in stone." – John Marshall"
- claimed_author: John Marshall
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 3. card_ids: 0008
- quote_text: ""Vikas Bhi Virasat Bhi" — PM Modi"
- claimed_author: PM Modi
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: vikasvirasat.netlify.app, newsonair.gov.in, library.bjp.org, www.scribd.com

### 4. card_ids: 0008
- quote_text: ""Culture, Creativity, Commerce and Collaboration" — PM Modi"
- claimed_author: PM Modi
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: openstreamsfoundation.org, www.pib.gov.in, www.hindustantimes.com, x.com

### 5. card_ids: 0008
- quote_text: ""Technology as an ally of culture" — PM Modi"
- claimed_author: PM Modi
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.youtube.com, www.pib.gov.in, timesofindia.indiatimes.com, newsonair.gov.in

### 6. card_ids: 0020
- quote_text: ""Dance is the joy of the soul expressed through movement." — Rabindranath Tagore"
- claimed_author: Rabindranath Tagore
- my_preliminary_z-ai_search: z-ai: 9 results from hosts: www.instagram.com, www.facebook.com, www.scribd.com, www.flame.edu.in

### 7. card_ids: 0024
- quote_text: ""Indian music is a meditation, not a performance." — Pandit Ravi Shankar"
- claimed_author: Pandit Ravi Shankar
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.facebook.com, studsterkel.wfmt.com, www.philipgoldberg.com

### 8. card_ids: 0025
- quote_text: ""A nation’s folk music is its heartbeat." — Jawaharlal Nehru"
- claimed_author: Jawaharlal Nehru
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.facebook.com, speakola.com, nehruarchive.in

### 9. card_ids: 0026
- quote_text: "“Theatre mirrors society and transforms it.” — Habib Tanvir"
- claimed_author: Habib Tanvir
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.facebook.com, www.amazon.com, www.academia.edu

### 10. card_ids: 0027
- quote_text: "“In puppetry, silent hands speak louder than words.” — Satyajit Ray"
- claimed_author: Satyajit Ray
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.facebook.com, www.artforum.com, en.wikipedia.org

### 11. card_ids: 0028
- quote_text: ""Martial arts train the body to protect and the mind to persevere." — Bruce Lee"
- claimed_author: Bruce Lee
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.facebook.com, www.quora.com, cheungsmartialarts.com

### 12. card_ids: 0037
- quote_text: ""The Vedas are not books of theology but records of spiritual discovery." – Sarvepalli Radhakrishnan"
- claimed_author: Sarvepalli Radhakrishnan
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, iep.utm.edu, www.vifindia.org, www.facebook.com

### 13. card_ids: 0038
- quote_text: ""Sangam poetry is not just emotion  it is geography, economy, and politics in verse." – A.K. Ramanujan"
- claimed_author: A.K. Ramanujan
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 1 results returned total)

### 14. card_ids: 0039
- quote_text: ""Silence and simplicity are the roots of liberation." – Mahavira"
- claimed_author: Mahavira
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, m.facebook.com, www.jaina.org, www.cs.colostate.edu

### 15. card_ids: 0040
- quote_text: ""Persian in India was not just a language, it was the canvas for Indo-Islamic creativity." – Muzaffar Alam"
- claimed_author: Muzaffar Alam
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, salc.uchicago.edu, sijmds.com, archive.org

### 16. card_ids: 0041
- quote_text: ""A nation is built by those who write its soul into words." – Rabindranath Tagore"
- claimed_author: Rabindranath Tagore
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.facebook.com, theanarchistlibrary.org, tagoreanworld.co.uk

### 17. card_ids: 0045
- quote_text: "“It is our duty to pay for our liberty with our own blood.” — Subhas Chandra Bose"
- claimed_author: Subhas Chandra Bose
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: www.azquotes.com, www.facebook.com, www.knowledgeboat.com, quotefancy.com

### 18. card_ids: 0046
- quote_text: "“Freedom is not given, it is taken.” — Subhas Chandra Bose"
- claimed_author: Subhas Chandra Bose
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: www.news18.com, www.facebook.com, allauthor.com, x.com

### 19. card_ids: 0047
- quote_text: ""The diverse threads of society wove together in the fabric of the freedom struggle." — Bipin Chandra Pal"
- claimed_author: Bipin Chandra Pal
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 20. card_ids: 0047
- quote_text: ""Unfortunately, tribals have not got the place they should have in the pages of history." — PM Modi"
- claimed_author: PM Modi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 5 results returned total)

### 21. card_ids: 0049
- quote_text: "“The seeds of freedom must be sown in the soil of unity.” — Gopal Krishna Gokhale"
- claimed_author: Gopal Krishna Gokhale
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 5 results returned total)

### 22. card_ids: 0050
- quote_text: "“You may never know what results come of your actions, but if you do nothing, there will be no result.” — Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: dehfoundation.org, www.facebook.com, medium.com, www.scribd.com

### 23. card_ids: 0051
- quote_text: "“They may kill me, but they cannot kill my ideas.” — Bhagat Singh"
- claimed_author: Bhagat Singh
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: www.facebook.com, rethinkindia.substack.com, www.azquotes.com, quotefancy.com

### 24. card_ids: 0052
- quote_text: "“The soul of India lives in its villages.” — Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: satvikamahapatra.medium.com, www.facebook.com, www.azquotes.com, www.clraindia.org

### 25. card_ids: 0054
- quote_text: ""Bengal united is power. Divided it will pull in several different ways." — L Risley"
- claimed_author: L Risley
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 26. card_ids: 0081
- quote_text: "“Liberty, equality, fraternity these are not mere words, they are our guiding principles.” — Nelson Mandela"
- claimed_author: Nelson Mandela
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.nelsonmandela.org, www.humanrightscareers.com, artsandculture.google.com

### 27. card_ids: 0082
- quote_text: "“The sun never set on the British Empire but it never rose on its justice.” — Shashi Tharoor"
- claimed_author: Shashi Tharoor
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, x.com, www.facebook.com, www.reddit.com

### 28. card_ids: 0083
- quote_text: "“Democracy is the worst form of government except for all the others.” — Winston Churchill"
- claimed_author: Winston Churchill
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: richardlangworth.com, www.reddit.com, www.goodreads.com, blogs.fcdo.gov.uk

### 29. card_ids: 0084
- quote_text: "“The factory system was the beginning of man being reduced to a number.” — Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.mkgandhi.org, www.gandhiserve.net, gandhi.study

### 30. card_ids: 0085, 0085
- quote_text: "“Those who cannot remember the past are condemned to repeat it.” — George Santayana"
- claimed_author: George Santayana
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: americanart.si.edu, en.wikipedia.org, iep.utm.edu, www.reddit.com

### 31. card_ids: 0086
- quote_text: ""India is a garden of many flowers — each one beautiful, each one unique." — Jawaharlal Nehru"
- claimed_author: each one beautiful, each one unique." — Jawaharlal Nehru
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: www.adfindia.org, www.facebook.com, askfilo.com, www.scribd.com

### 32. card_ids: 0088
- quote_text: ""It is good to swim in the waters of tradition but to sink in them is suicide" — Gandhi"
- claimed_author: Gandhi
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: x.com, www.mkgandhi.org, www.gandhi-manibhavan.org, www.instagram.com

### 33. card_ids: 0091
- quote_text: ""Population, when unchecked, increases in a geometrical ratio." — Thomas Malthus"
- claimed_author: Thomas Malthus
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 34. card_ids: 0092
- quote_text: ""There is no chance for the welfare of the world unless the condition of women is improved." — Swami Vivekananda"
- claimed_author: Swami Vivekananda
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 35. card_ids: 0093
- quote_text: ""A gender-equal society would be one where the word ‘gender’ does not exist." — Gloria Steinem"
- claimed_author: Gloria Steinem
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 36. card_ids: 0094
- quote_text: ""Poverty is the worst form of violence." — Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 37. card_ids: 0095
- quote_text: ""Think globally, act locally." — Patrick Geddes"
- claimed_author: Patrick Geddes
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 38. card_ids: 0096
- quote_text: ""Social justice is the first condition of humanity." — B. R. Ambedkar"
- claimed_author: B. R. Ambedkar
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 39. card_ids: 0099
- quote_text: ""Religion is a personal matter, not a political weapon." — Jawaharlal Nehru"
- claimed_author: Jawaharlal Nehru
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 40. card_ids: 0100
- quote_text: ""India is a union of states, not a confederation of ambitions." — Sardar Patel"
- claimed_author: Sardar Patel
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 41. card_ids: 0103
- quote_text: ""Secularism is the soul of the Indian Constitution." — Rajendra Prasad"
- claimed_author: Rajendra Prasad
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 42. card_ids: 0104
- quote_text: ""A developed country is not a place where the poor have cars. It’s where the rich use public transportation." — Enrique Peñalosa"
- claimed_author: Enrique Peñalosa
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 43. card_ids: 0105
- quote_text: ""Urban governance is not just administration  it is transformation." — E. Sreedharan"
- claimed_author: E. Sreedharan
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 44. card_ids: 0107
- quote_text: ""Energy is necessary for development & sustainable energy is necessary for sustainable development" — Tim Wirth"
- claimed_author: Tim Wirth
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 45. card_ids: 0120
- quote_text: ""Resources are not, they become.""
- claimed_author: (no attribution in booklet)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 46. card_ids: 0131
- quote_text: ""The environment and the economy are really both two sides of the same coin. You cannot sustain the economy if you don't take care of the environment." — Bruce Lipton"
- claimed_author: Bruce Lipton
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 47. card_ids: 0133
- quote_text: ""Industries go where they are wanted, and stay where they are treated well." — Ronald Reagan"
- claimed_author: Ronald Reagan
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 48. card_ids: 0134
- quote_text: ""We do not inherit the Earth from our ancestors; we borrow it from our children."  Native American Proverb"
- claimed_author: (no attribution in booklet)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 49. card_ids: 0142
- quote_text: ""Nature does not hurry, yet everything is accomplished.""
- claimed_author: (no attribution in booklet)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 50. card_ids: 0157
- quote_text: ""While we borrowed from many, we built for Bharat." — Dr. B.R. Ambedkar"
- claimed_author: Dr. B.R. Ambedkar
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 51. card_ids: 0158
- quote_text: ""Parliamentary democracy is the bedrock of India's governance, where diverse voices converge to shape the nation's destiny." — ABV (Atal Bihari Vajpayee)"
- claimed_author: ABV (Atal Bihari Vajpayee)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 52. card_ids: 0159
- quote_text: ""Amendment is the lifeline of a living Constitution." — Nani Palkhivala"
- claimed_author: Nani Palkhivala
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 53. card_ids: 0171
- quote_text: ""UCC should apply only for those who are prepared to be bound by it." — Ambedkar"
- claimed_author: Ambedkar
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 54. card_ids: 0178
- quote_text: ""Free & Fair elections are the lifeblood of any democracy." — Jimmy Carter"
- claimed_author: Jimmy Carter
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 55. card_ids: 0179
- quote_text: ""When the power of a vote is diluted through opacity in political funding, democracy loses its intrinsic value." — Ornit Shani"
- claimed_author: Ornit Shani
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 56. card_ids: 0181
- quote_text: ""Free & Fair elections are lifeblood of any democracy" — Jimmy Carter"
- claimed_author: Jimmy Carter
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 57. card_ids: 0184
- quote_text: ""Like a cancer, eating into the vitals of a democracy." — Delhi HC 2018"
- claimed_author: Delhi HC 2018
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.facebook.com, nludelhi.ac.in, documents1.worldbank.org

### 58. card_ids: 0185
- quote_text: ""When the power of a vote is diluted through opacity in political funding, democracy loses its intrinsic value" — Ornit Shani"
- claimed_author: Ornit Shani
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 59. card_ids: 0186
- quote_text: ""Democracy at the grassroots is democracy at its strongest." — Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 60. card_ids: 0189
- quote_text: ""Cooperative federalism is not a choice; it is a constitutional compulsion." — PM Narendra Modi"
- claimed_author: PM Narendra Modi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 61. card_ids: 0193
- quote_text: ""RS may be the second house but no one should think of it as a secondary house." — ABV"
- claimed_author: ABV
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 62. card_ids: 0199
- quote_text: ""A free press should neither be an ally nor an adversary but a constructive critic." — Gandhiji"
- claimed_author: Gandhiji
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 63. card_ids: 0200
- quote_text: ""Social media is a double-edged sword." — Noam Chomsky"
- claimed_author: Noam Chomsky
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 64. card_ids: 0201
- quote_text: ""In democracy, even silence can organise into influence." — Granville Austin"
- claimed_author: Granville Austin
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 65. card_ids: 0209
- quote_text: ""Governor's actions must be tempered with caution, dictated by reason & activated in good faith." — Sarkaria Commission"
- claimed_author: Sarkaria Commission
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 66. card_ids: 0211
- quote_text: ""Justice is not simply punishing the guilty, but also defending the innocent and ensuring due process for all." — Kofi Annan"
- claimed_author: Kofi Annan
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 67. card_ids: 0216
- quote_text: ""Accountability & integrity increase a court's prestige & faith rather than reducing it." — Justice Hidayatullah, in Naresh Sridhar Case"
- claimed_author: Justice Hidayatullah, in Naresh Sridhar Case
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 68. card_ids: 0225
- quote_text: ""Civil servants are the steel frame but must also be the spinal nerve of reform." — Sardar Patel"
- claimed_author: Sardar Patel
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 69. card_ids: 0226
- quote_text: ""Civil servants are the silent architects of a nation's progress, dedicated to translating policies into actions that shape the destiny of India." — Dr. APJ Abdul Kalam"
- claimed_author: Dr. APJ Abdul Kalam
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 70. card_ids: 0226
- quote_text: ""Civil servants are the bridge that connects government policies with the aspirations and welfare of the people they serve." — NR Narayana Murthy"
- claimed_author: NR Narayana Murthy
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 71. card_ids: 0229, 0233
- quote_text: ""Without accountability, resources are wasted, corruption flourishes, and trust in institutions is eroded." — Ban Ki-moon"
- claimed_author: Ban Ki-moon
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 72. card_ids: 0230
- quote_text: ""RTI is the most important legislation since independence. It marks the beginning of an era of dawn & ends the era of darkness." — ARC 2"
- claimed_author: ARC 2
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 5 results returned total)

### 73. card_ids: 0230
- quote_text: ""Sunlight is the best disinfectant." — 2nd ARC"
- claimed_author: 2nd ARC
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: en.wiktionary.org, alasdairroberts.ca, archives.cpajournal.com, www.reddit.com

### 74. card_ids: 0230
- quote_text: ""Corruption thrives in secret places — avoids open spaces." — Woodrow Wilson"
- claimed_author: avoids open spaces." — Woodrow Wilson
- my_preliminary_z-ai_search: z-ai: 10 results from hosts: www.azquotes.com, standardebooks.org, palipost.com, kwize.com

### 75. card_ids: 0231
- quote_text: ""Social audit is not just an evaluation of programs; it's an assertion of people's rights to dignity, transparency, and accountable governance." — Aruna Roy"
- claimed_author: Aruna Roy
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 76. card_ids: 0233
- quote_text: ""You are not only responsible for what you say but also for what you do not say." — Martin Luther King Jr."
- claimed_author: Martin Luther King Jr.
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 77. card_ids: 0237
- quote_text: ""The CAG is the conscience keeper of government finances, ensuring that taxpayer money is used judiciously and efficiently." — Rajiv Mehrishi (former Finance Secretary)"
- claimed_author: Rajiv Mehrishi (former Finance Secretary)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 78. card_ids: 0244
- quote_text: ""Without strong watchdog institutions, impunity becomes the very foundation on which systems of corruption are built." — Rigoberta Menchú Tum"
- claimed_author: Rigoberta Menchú Tum
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 79. card_ids: 0263
- quote_text: ""Good policies fail with bad implementation; bad policies fail faster." – Second ARC"
- claimed_author: Second ARC
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.linkedin.com, www.researchgate.net, cardinalpointadvisors.net

### 80. card_ids: 0268
- quote_text: ""The development sector is not third sector it is the frontline of inclusive governance." – Abhijit Banerjee"
- claimed_author: Abhijit Banerjee
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 81. card_ids: 0282
- quote_text: ""An educated, healthy population is not a burden it is the foundation of any civilised society." – Amartya Sen"
- claimed_author: Amartya Sen
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 82. card_ids: 0287
- quote_text: ""The test of good governance is how it treats its weakest citizens." — Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 83. card_ids: 0289
- quote_text: ""The Constitution is a transformative document it enshrines not charity but rights." – Justice Indu Malhotra"
- claimed_author: Justice Indu Malhotra
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 84. card_ids: 0295
- quote_text: ""A budget tells us what we value as a society." — UN Women"
- claimed_author: UN Women
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, www.unwomen.org, www.facebook.com, www.iadb.org

### 85. card_ids: 0301
- quote_text: ""The world order is militarily unipolar, economically multipolar and politically confused." — Shiv Shankar Menon (SSM)"
- claimed_author: Shiv Shankar Menon (SSM)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 86. card_ids: 0301
- quote_text: ""In a world full of fault lines and rifts, we need to build a shared future." — Modi"
- claimed_author: Modi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 87. card_ids: 0301
- quote_text: ""We are headed for a poorer, meaner and smaller world." — SSM"
- claimed_author: SSM
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 88. card_ids: 0301
- quote_text: ""Globalisation is irreversible." — Tony Blair"
- claimed_author: Tony Blair
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 89. card_ids: 0301
- quote_text: ""India has entered a phase of energetic foreign policy where it is not anymore a passive recipient of global happenings." — S. Jaishankar"
- claimed_author: S. Jaishankar
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 90. card_ids: 0304
- quote_text: ""The Indian Ocean, with its critical sea lanes and vast reservoir of resources, will be a highway to prosperity and a theatre of rivalry." — C. Raja Mohan"
- claimed_author: C. Raja Mohan
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 91. card_ids: 0305
- quote_text: ""In the information age, a nation's power is increasingly defined by its ability to influence as much as to militarily and economically dominate." — Shashi Tharoor"
- claimed_author: Shashi Tharoor
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 92. card_ids: 0320
- quote_text: ""A nation's destiny is shaped by its geography but defined by its diplomacy." — Shyam Saran"
- claimed_author: Shyam Saran
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 93. card_ids: 0324
- quote_text: ""Relationship with India is our most important relationship, period." — Milinda Moragoda, SL High Commissioner (after India's cooperation in crisis)"
- claimed_author: Milinda Moragoda, SL High Commissioner (after India's cooperation in crisis)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 94. card_ids: 0324
- quote_text: ""Focus must be on elevating the bilateral ties from the current 'transactional' phase to one that is more 'strategic'." — Milinda Moragoda"
- claimed_author: Milinda Moragoda
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 95. card_ids: 0326
- quote_text: ""India's vision is a Sovereign, United, Stable, Plural and Democratic Afghanistan." — Former diplomat Rakesh Sood"
- claimed_author: Former diplomat Rakesh Sood
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 96. card_ids: 0333
- quote_text: ""A budget is not just numbers on a page, it is an embodiment of our values." – Barack Obama"
- claimed_author: Barack Obama
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 97. card_ids: 0341
- quote_text: ""A vision without a plan is just a wish." – Narendra Modi"
- claimed_author: Narendra Modi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 98. card_ids: 0346
- quote_text: ""Employment is not just about income—it’s about identity and dignity." — World Bank"
- claimed_author: World Bank
- my_preliminary_z-ai_search: z-ai: 6 results from hosts: www.scribd.com, blogs.worldbank.org, www.worldbank.org, www.facebook.com

### 99. card_ids: 0385
- quote_text: ""The future depends on what we do in the present." — Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 100. card_ids: 0385
- quote_text: ""Jai Jawan, Jai Vigyan, Jai Anusandhan." — PM Modi"
- claimed_author: PM Modi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 101. card_ids: 0442
- quote_text: ""The only thing that displaced more people than war is wildlife conservation." — Mark Dowie"
- claimed_author: Mark Dowie
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 102. card_ids: 0528
- quote_text: ""Underdevelopment and inequality — hence need to imbibe Tribal Panchsheel principles in bringing peace & participative governance." — Antonio Guterres"
- claimed_author: hence need to imbibe Tribal Panchsheel principles in bringing peace & participative governance." — Antonio Guterres
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 103. card_ids: 0560
- quote_text: "“Public service must be more than doing a job efficiently; it must be a complete dedication to the people.” – Sardar Vallabhbhai Patel"
- claimed_author: Sardar Vallabhbhai Patel
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 104. card_ids: 0584
- quote_text: "“A nation's greatness is measured by how it treats its weakest members.” – Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 105. card_ids: 0590
- quote_text: "“Excellence happens not by accident. It is a process.” – Dr. A.P.J. Abdul Kalam"
- claimed_author: Dr. A.P.J. Abdul Kalam
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 106. card_ids: 0591
- quote_text: "“Facts are sacred; opinion is free.” – Jawaharlal Nehru"
- claimed_author: Jawaharlal Nehru
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 107. card_ids: 0592
- quote_text: "“The best way to find yourself is to lose yourself in the service of others.” – Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 108. card_ids: 0593
- quote_text: "“Tolerance and patience are much stronger than brute force.” – Subhas Chandra Bose"
- claimed_author: Subhas Chandra Bose
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 109. card_ids: 0602
- quote_text: "“A public servant belongs to the people, not to a party.” – Sardar Vallabhbhai Patel"
- claimed_author: Sardar Vallabhbhai Patel
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 110. card_ids: 0604
- quote_text: "“It is easy to stand with the crowd. It takes courage to stand alone.” – Dr. A.P.J. Abdul Kalam"
- claimed_author: Dr. A.P.J. Abdul Kalam
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 111. card_ids: 0607
- quote_text: ""CS Lewis: Integrity is doing the right thing even when no one is watching.""
- claimed_author: (no attribution in booklet)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 112. card_ids: 0610
- quote_text: ""In looking for people to hire, you look for three qualities: integrity, intelligence and energy. And if they don't have the first, the other two will kill you.""
- claimed_author: (no attribution in booklet)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 113. card_ids: 0614
- quote_text: ""Frank Crane - 'you may be deceived if you trust too much, but you will live in torment if you don't trust enough'""
- claimed_author: 'you may be deceived if you trust too much, but you will live in torment if you don't trust enough'"
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 114. card_ids: 0620
- quote_text: "“Watch your thoughts, they become words... your destiny.” – Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 115. card_ids: 0624
- quote_text: "“Action is the real measure of intelligence.” – Napoleon Hill"
- claimed_author: Napoleon Hill
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 116. card_ids: 0628
- quote_text: "“A man is but the product of his thoughts and the environment he lives in.” – Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 117. card_ids: 0629
- quote_text: "“You can change people’s minds by touching their hearts.” – Dr. A.P.J. Abdul Kalam"
- claimed_author: Dr. A.P.J. Abdul Kalam
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 118. card_ids: 0657
- quote_text: ""We must remember, what Martin Luther King Jr. said, 'We must learn to live together as brothers, or die together as fools'." 'Let us sacrifice our today so that our children can have a better tomorrow', A.P.J. Abdul Kalam.""
- claimed_author: (no attribution in booklet)
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 119. card_ids: 0661
- quote_text: "“Moral excellence is not an act, but a habit.” – Aristotle"
- claimed_author: Aristotle
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 120. card_ids: 0715
- quote_text: ""Voltaire - 'I may not agree with what you say but I will fight to death your right to say it'""
- claimed_author: 'I may not agree with what you say but I will fight to death your right to say it'"
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 121. card_ids: 0722
- quote_text: ""CORRUPTION IS PAID BY THE POOR. - Pope Francis" "Results in collusive corruption paid for by the poor. - Pope Francis""
- claimed_author: Pope Francis" "Results in collusive corruption paid for by the poor. - Pope Francis"
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 122. card_ids: 0730
- quote_text: "“The true ruler is the one who serves his people best.” – Chanakya"
- claimed_author: Chanakya
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 123. card_ids: 0732
- quote_text: "“Ethics is knowing the difference between what you have a right to do and what is right to do.” – Potter Stewart"
- claimed_author: Potter Stewart
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 124. card_ids: 0736
- quote_text: "“Public service must be more than doing a job efficiently and honestly. It must be a complete dedication to the people.” – Margaret Chase Smith"
- claimed_author: Margaret Chase Smith
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 125. card_ids: 0739
- quote_text: "“The customer is the most important visitor on our premises.” – Mahatma Gandhi"
- claimed_author: Mahatma Gandhi
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 126. card_ids: 0755
- quote_text: "“A person who is morally educated will be a lot better equipped to move up the ladder of life.” – Dr. A.P.J. Abdul Kalam"
- claimed_author: Dr. A.P.J. Abdul Kalam
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 127. card_ids: 0756
- quote_text: "“Power must always be accompanied by responsibility.” – Pandit Jawaharlal Nehru"
- claimed_author: Pandit Jawaharlal Nehru
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)

### 128. card_ids: 0776
- quote_text: "“The line between right and wrong is often drawn by self-interest.” – Nani Palkhivala"
- claimed_author: Nani Palkhivala
- my_preliminary_z-ai_search: z-ai: error (likely rate-limit; 0 results returned total)
