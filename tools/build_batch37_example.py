import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    pid = ('GS1-HIST-%04d' if i <= 85 else 'GS1-SOCI-%04d') % i
    P[pid] = (status, blocks)

card(81, 'polished',
 introduction="The revolutions in America, France, and Haiti redefined governance — monarchy and slavery were challenged, and people's sovereignty became institutional. Modern democracies and anti-colonial struggles across continents drew inspiration from them.",
 examples="- School civics curricula in India now include modules on the Haitian and French Revolutions as roots of the global rights discourse\n"
 "- A **UN Democracy Dialogue** cited American revolutionary ideals while discussing voter apathy and democratic backsliding",
 conclusion="These revolutions turned abstract ideals into institutions. Their values still benchmark justice, rights, and people-led governance.")

card(82, 'polished',
 introduction="Colonialism plundered wealth and agency alike. Decolonisation rose on local movements, post-war fatigue, and global solidarity — shaping today's South–South cooperation and identity politics.",
 examples="- An **India–African Union** joint statement called for the restitution of cultural artefacts from former colonial powers\n"
 "- The **South-South Knowledge Exchange Platform** shared post-colonial development models from Asia, Africa, and Latin America",
 conclusion="Decolonisation ended foreign rule, but the colonial mindset lingers. True freedom means reclaiming cultural, economic, and intellectual sovereignty.")

card(83, 'needs_review',
 introduction="Modern ideologies — capitalism, socialism, fascism — answered questions of inequality, freedom, and authority. They still steer debates on welfare, authoritarianism, and economic justice across global democracies.",
 examples="- A **G7** academic roundtable debated AI governance through capitalist and socialist frameworks\n"
 "- An Indian civil service ethics module compares **Marx, Smith**, and totalitarian regimes to assess leadership philosophies",
 conclusion="Ideologies shape laws and lives. Understanding their roots is vital to balance liberty, equity, and power in today's multipolar world. Great! Here's a continuation of the same refined and UPSC-relevant format for: III.INDIAN SOCIETY")

card(84, 'polished',
 introduction="The Industrial Revolution changed economies and labour — but also widened inequality and colonial dependence. It sowed capitalism, environmental degradation, and the modern labour movement.",
 examples="- The **Global South Climate Consortium** flagged industrial-era emissions as the root of today's carbon imbalance\n"
 "- India's **G20** summit agenda tied labour rights to ethical production chains in post-industrial economies",
 conclusion="It mechanised growth yet dehumanised labour. Its legacy presses us to balance innovation with justice and sustainability in a changing world.")

card(85, 'polished',
 introduction="The World Wars redrew geopolitics, collapsed empires, and built global institutions. They also pushed colonies to question imperialism and produced multilateral peace frameworks like the **United Nations**.",
 examples="- A **UN General Assembly** resolution recalled the **League of Nations'** failures while debating Security Council representation reforms\n"
 "- The **India-Europe Peace Forum** drew lessons from both World Wars for managing refugee crises",
 conclusion="War left scars and systems alike. Peace now needs more than deterrence — it needs inclusive diplomacy and justice.")

card(86, 'polished',
 introduction="With Unity in Diversity as its soul, India is a mosaic of languages, faiths, ethnicities, and regional identities. This diversity is more than co-existence — it anchors India's democratic vibrancy.",
 examples="- **Ek Bharat Shreshtha Bharat** promotes cultural exchanges between linguistically and ethnically diverse states\n"
 "- The **PM Vishwakarma Yojana** empowers traditional artisans across cultural communities, preserving pluralistic heritage",
 conclusion="Through inclusive policy, India turns difference into strength — a lesson for the world's multicultural democracies.")

card(87, 'polished',
 introduction="- Ethnicity is a **shared cultural heritage** — language, religion, traditions, historical experiences — that shapes a group's identity within a larger society.\n"
 "- It is a social construct; it drives people's **sense of belonging** and colours their perspectives and interactions.",
 data="- Issues: Anti-semitism, violence, Xenophobia, Ethno-centrism.\n"
 "- Conflicts: ethnic. Intra-ethnic — shia vs sunni. Inter-ethnic — assamese vs bengali. Ethnic group vs state: naga mvmt; khalisatn.\n"
 "- **Basis of conflict:**\n"
 "  - Language: tamil vs hindi\n"
 "  - Religion: tribals vs christian missionaries\n"
 "  - Race: Naga\n"
 "- **Bez Baruah committee:**\n"
 "  - 1. Stringent laws.\n"
 "  - 2. Legal awareness.\n"
 "  - 3. Fast-track courts.",
 conclusion="- Solution:\n"
 "  - 1. **Cultural sensitisation**; govt **ek bharat shresth bharat.**\n"
 "  - 2. The **Kashi Tamil Sangamam**. Schedule 6. Inclusive growth and participative governance. Dropadi murmu: 1st tribal women president.")

card(88, 'polished',
 introduction="Characteristics: **geographic isolation, shyness of contact, economic backwardness, primitive traits, distinct culture**.",
 data="- Positive changes today: women wrestlers in Haryana, intercaste marriages, revival of +ve traditions — the **Kaktiya mission**; Draupadi Murmu: 1st tribal women president.\n"
 "- **Demographics:** **8.6%** tribals.\n"
 "- **Poverty:**\n"
 "  - 1. Disproportionately high in STs.\n"
 "  - 2. The **11.28% national multidimensional poverty average (NITI Aayog MPI)**.\n"
 "- **Representation:** Only 4 GoI secretaries from SC/ST (the **Xaxa commission**).\n"
 "- **Education:** **75%** dropouts in class 10.\n"
 "- **Legislation:**\n"
 "  - 1. **PESA**.\n"
 "  - 2. **FRA**.\n"
 "  - 3. The Prevention of atrocities act; locally recruited teachers; a tribal dictionary. The Pathalgadi movement (JH).\n"
 "- **XAXA committee:** the rayagada model — the Dangar path (traditional knowledge) and the Kagaz path (English fluency). Tribal panchsheel. Repeal the Habitual offenders act.",
 conclusion="- Confused modernity: technology for sex selective abortion; social media for hate speech; caste-based recruitment for sanitation work; low preference for inter-caste matches on matrimony websites.\n"
 "- The **Dhebar commission (1961)**: integrate tribal knowledge and language into the curriculum. The OD model.")

card(89, 'polished',
 introduction="- Promoting tolerance. Positive values:\n"
 "  - 1. **Anekantwad, Sarva dharam sambhav, Vasudev kutumbakam**. Modern secular education. A secular state: the Preamble.\n"
 "  - 2. Article 15.\n"
 "  - 3. Article 16.\n"
 "  - 4. Articles 25-28: 44. Urbanisation, the Judiciary.\n"
 "  - 5. Civil society, modern spiritualism.\n"
 "- Customs — positive:\n"
 "  - 1. Sacred groves; traditional water harvesting systems: the Baoli.\n"
 "  - 2. Rani ki vav, ayurveda, scientific architecture: the jantar mantar.\n"
 "- Negative: the mensuration taboo, genital mutilation among the dawoodi bohras, the devdasi system, untouchability, made snana, animal sacrifice.",
 data="- **Examples of tolerance:**\n"
 "  - The **Karwa-e-Mohabbat**: a rally against hate crime.\n"
 "  - Visits by all religions and communities to the Golden Temple.\n"
 "  - 1. The Mahim church.\n"
 "  - 2. Ajmer Sharif.\n"
 "  - The Vaver mosque visit is an integral part of the sabrimala pilgrimage.\n"
 "- **Govt steps:**\n"
 "  - 1. The Van Dhan scheme.\n"
 "  - 2. The Eklavya model.\n"
 "  - 3. TriFed.\n"
 "  - 4. Aspirational blocks. 338A.\n"
 "  - 5. The 5/6th schedule.\n"
 "  - 6. Articles 29-30,46.",
 conclusion="- Intolerance examples:\n"
 "  - 1. The 2020 Delhi riots; the tanishq ad with a muslim family organising a baby shower for a daughter-in-law; the Dabur ad with a homosexual couple celebrating karwa chauth; the murder of rationalist narender Dabholkar.\n"
 "  - 2. Gauri lankesh.")

card(90, 'needs_review',
 introduction="- Promoting tolerance — positive values\n"
 "- **Anekantwad**",
 examples="- Examples of tolerance\n"
 "- The **Karwa-e-Mohabbat**: a rally against hate crime\n"
 "- Visits by all religions and...",
 conclusion="- Intolerance examples\n"
 "- The 2020 Delhi riots\n"
 "- The tanishq ad: a muslim family organising a baby...")

card(91, 'needs_review',
 introduction="India's demographic transition — from burden to dividend — is unfolding. Under the **Amrit Kaal** vision, managing population growth and migration is crucial for equitable development.",
 examples="- The **Viksit Bharat Sankalp Yatra** focuses on saturating schemes in high-population districts\n"
 "- The **Aspirational Districts Programme** uses population data to cut migration through local development",
 conclusion="Harnessing the demographic dividend requires investing in mobility, skills, and balanced urban-rural growth. Poverty & Development")

card(92, 'needs_review',
 introduction="From Vedic scholars to constitutional framers, Indian women have shaped history. The journey from **Stree Shakti** to the **Nari Shakti Vandan Adhiniyam** shows a society reclaiming gender equity.",
 examples="- **Women's Reservation** in Parliament was passed to ensure greater representation in lawmaking\n"
 "- Over **70%** of **Self-Help Group Bank Linkage Programme** beneficiaries are women, redefining economic independence",
 conclusion="Real empowerment translates rights into realities — through laws, leadership, and lasting social change. Gender Disparity & Laws/Reforms")

card(93, 'polished',
 introduction="India's legal framework aims at equality, yet the gaps in education, health, and employment show **Beti Bachao Beti Padhao** remains a mission, not a milestone.",
 examples="- The **STEM for Girls** initiative tackles educational inequity in science and tech\n"
 "- **Mission Shakti** brings safety, rehabilitation, and empowerment for women under one umbrella",
 conclusion="Laws can trigger change; societal mindsets must evolve for true gender justice.")

card(94, 'needs_review',
 introduction="India has halved multidimensional poverty through schemes like the **National Food Security Act** and **Direct Benefit Transfer**. Yet inequality demands reimagining growth as inclusive and sustainable.",
 examples="- The **PM Janman Yojana** targets vulnerable tribal groups often left out of development narratives\n"
 "- **One Nation One Ration Card** has improved food access for the mobile poor",
 conclusion="A just society is judged not by affluence but by how the poorest live — policy must reflect that truth. Perfect! Continuing in the same enriched, UPSC-relevant style with:")

card(95, 'needs_review',
 introduction="Globalisation has reshaped India's economy and aspirations — pulling it into global value chains while stirring debates on cultural identity and job displacement.",
 examples="- **PLI Schemes** attract foreign investment while boosting domestic manufacturing and job creation\n"
 "- The **Startup India-Digital India** synergy is making global entrepreneurs of small-town founders, reshaping societal structures",
 conclusion="India must embrace globalisation on its own terms — rooted in values, ready for change. 11-A.Social Empowerment")

card(96, 'polished',
 introduction="India's democracy is social, not just political — as the Constitution's vision of \"economic and social justice\" echoes. Social empowerment ensures dignity and opportunity beyond representation.",
 examples="- The **PM Vishwakarma Yojana** empowers traditional artisans from Scheduled Castes and Other Backward Classes with modern tools and training\n"
 "- The **National Action Plan for Transgender Persons** institutionalises inclusion via healthcare, shelter, and employment support",
 conclusion="True empowerment goes beyond schemes — it shows in voices heard, opportunities shared, and dignity restored.")

card(97, 'polished',
 introduction="- It is the process by which economies and societies became **increasingly integrated and interdependent**.\n"
 "- **Global village. Borderless world. Compression in space and time**.",
 data="- **Local in global:**\n"
 "  - yoga\n"
 "  - bollywood\n"
 "  - the diaspora celebrating festivals\n"
 "  - the saree worn by celebrities in Cannes\n"
 "  - indian cuisines abroad\n"
 "- **Global in local:**\n"
 "  - Hinglish\n"
 "  - McDonald serving veg during navaratri\n"
 "  - remakes of global films: forest gump remade as laal singh chaddha; religion:\n"
 "    - 1. E darshan.\n"
 "    - 2. Live telecast of gurbani.\n"
 "  - chinese lights vs diyas",
 conclusion="- Dimensions:\n"
 "  - 1. Education - GIAN.\n"
 "  - 2. Brain drain; economy - choice.\n"
 "  - 3. SoL.\n"
 "  - 4. GVC.\n"
 "  - 5. Tech; women; environment - SUP.\n"
 "  - 6. Invasive species.\n"
 "  - 7. Bio diversity.\n"
 "  - 8. Eco tourism; culture — cultural imperialism, tribals and traditions, elderly.")

card(98, 'needs_review',
 introduction="The process by which economies and societies became **increasingly integrated and interdependent**. Global village. Borderless world. Compression in space and time.",
 examples="- Local in global: yoga; bollywood; the diaspora celebrating festivals; the saree worn by celebrities in Cannes; indian cuisines abroad\n"
 "- Global in local: Hinglish; McDonald serving veg during navaratri; remakes of global films — forest gump remade as laal singh chaddha; religion — e darshan; live telecast of gurbani; chinese lights vs diyas",
 conclusion="- Dimensions\n"
 "- education — GIAN; brain drain\n"
 "- economy — choice; SoL; GVC; tech\n"
 "- women\n"
 "- environment — SUP; invasive species; bio diversity; eco tourism\n"
 "- culture: cultural imperialism\n"
 "- tribals and traditions\n"
 "- elderly")

card(99, 'polished',
 introduction="India's unity rests on its plurality — and communalism threatens to fracture it. Communal violence flows not from faith but from politicised narratives and failing institutions.",
 examples="- The **One Nation, One Police Reform Agenda** focuses on neutralising bias in local policing to contain communal flare-ups\n"
 "- Social media monitoring cells across states counter the hate speech and misinformation that fuel communal tensions",
 conclusion="Countering communalism needs more than control — it needs the cultivation of harmony, shared spaces, and a common national belonging.")

card(100, 'polished',
 introduction="India's diversity is its strength — but when regional pride hardens into regionalism, it can strain the nation's integrative ethos. Balancing identity with unity is a democratic tightrope.",
 examples="- **Special Development Councils** in tribal-majority states celebrate regional culture while ensuring equitable development\n"
 "- Recent peaceful statehood movements have chosen democratic methods over disruptive agitation",
 conclusion="A strong India makes room for local identity — but never at the cost of national integrity.")

build('/home/z/my-project/raw_batch37.md', P,
      '/home/z/my-project/polished/GS1_HIST-SOCI_batch37_cards0081-0100.md')
print('built batch 37: 20 cards')
