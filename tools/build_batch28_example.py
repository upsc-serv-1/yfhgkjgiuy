import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import build

P = {}
def card(i, status, **blocks):
    P['GS4-ETHI-%04d' % i] = (status, blocks)

card(697, 'polished',
 detail="- Thus **Buddha**'s 'Madhyammarga' — the middle path — should guide us, and restrictions must stay reasonable. The **Puttaswamy** 3-point categorisation of reasonableness highlights this.")

card(698, 'polished',
 examples="- Leadership and Courage in one frame: **Sanjukta Parashar** (IPS) taking on Bodo militants.")

card(699, 'polished',
 examples="- **Improve quality of life of people - Eg** — **V. Kurien** empathised with farmers and women alike, and the milk revolution succeeded.")

card(700, 'untouched')

card(701, 'polished',
 detail="- the Bangladeshi economist who pioneered microfinance and SHGs")

card(702, 'untouched')

card(703, 'polished',
 detail="- a warning against orthodoxy and the ills of democracy")

card(704, 'untouched')

card(705, 'untouched')

card(706, 'untouched')

card(707, 'untouched')

card(708, 'untouched')

card(709, 'polished',
 detail="- **JS Mill on liberty** — people may act as they wish unless they harm someone (the '**harm principle**')")

card(710, 'untouched')

card(711, 'polished',
 detail="- **Ethical egoism** — no moral obligation towards others; **Ayn Rand**'s position")

card(712, 'untouched')

card(713, 'untouched')

card(714, 'untouched')

card(715, 'untouched')

card(716, 'untouched')

build('/home/z/my-project/raw_batch28.md', P,
      '/home/z/my-project/polished/GS4_ETHI_batch28_cards697-716.md')
print('built batch 28: 20 cards')
