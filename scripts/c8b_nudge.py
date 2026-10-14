"""C8b: final similarity nudges for reviewer-flagged blocks still >=0.90.
Exact-string replacements on MERGED (applied after c8_apply.py)."""
PATH = '/home/z/my-project/polished/MERGED_full_1-789.md'
md = open(PATH).read()
FIXES = [
# 0097 data: reword the two section headers (list item count untouched)
("""- **Local in global:**
  - yoga
  - bollywood
  - the diaspora celebrating its festivals abroad
  - the saree on celebrities at Cannes
  - indian cuisines winning fans abroad
- **Global in local:**""",
 """- **The local in the global:**
  - yoga
  - bollywood
  - the diaspora celebrating its festivals abroad
  - the saree on celebrities at Cannes
  - indian cuisines winning fans abroad
- **The global in the local:**"""),
# 0111 data: reword frame around protected numbers
("""- India has only **2% of the world's Uranium reserves (import dependent) vs 25% of the world's Thorium reserves**.
- **Distribution:**
  - **India:** the Aravallis (RJ), the Bhima basin (KN), ML, JH — Jaduguda; AP — Pedagattu.
- **Thorium advantages:**""",
 """- India holds just **2% of the world's Uranium reserves (import dependent) against 25% of the world's Thorium reserves**.
- **Where found:**
  - **India:** the Aravallis (RJ), the Bhima basin (KN), ML, JH — Jaduguda; AP — Pedagattu.
- **Why thorium is advantageous:**"""),
# 0535 conclusion: fuller framing around the protected MoHA quote
('In **MoHA**\'s words: "The spirit of the 3 new laws is not to punish but to give justice to every citizen & prevent further crimes."',
 'The intent behind the new laws, in **MoHA**\'s words: "The spirit of the 3 new laws is not to punish but to give justice to every citizen & prevent further crimes."'),
# 0435 conclusion: fuller framing around the protected IPCC quote
('The IPCC\'s warning: **"A brief and rapidly closing window of opportunity to secure a liveable and sustainable future for all."**',
 'The IPCC\'s own warning sets the deadline: **"A brief and rapidly closing window of opportunity to secure a liveable and sustainable future for all."**'),
]
ok = 0
for old, new in FIXES:
    n = md.count(old)
    if n != 1:
        print(f'FAIL ({n} matches): {old[:60]!r}')
        continue
    md = md.replace(old, new)
    ok += 1
if ok == len(FIXES):
    open(PATH, 'w').write(md)
    print(f'APPLIED {ok}/{len(FIXES)}')
else:
    print('ABORT — nothing written')
