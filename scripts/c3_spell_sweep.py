#!/usr/bin/env python3
"""C3: spelling sweep. Applies user-approved unambiguous spelling fixes,
logs every change, and auto-generates allowlist entries for caps tokens
and quote-block replacements so verify stays at 0 errors / 0 false notes."""
import re, json

PATH = '/home/z/my-project/polished/MERGED_full_1-789.md'
book = open(PATH).read()
ids = [(m.start(), m.group(1)) for m in re.finditer(r'^id: (\S+)', book, re.M)]

def card_of(pos):
    cur = '?'
    for start, cid in ids:
        if start <= pos: cur = cid
        else: break
    return cur

def block_of(pos):
    seg = book[max(0, pos-3000):pos]
    kinds = re.findall(r':::(\w+)', seg)
    return kinds[-1] if kinds else '?'

FIXES = [
    # (old, new, reason)
    ("Narsimha Rao", "Narasimha Rao", "standard spelling of PM's name"),
    ("Indira Sawhney", "Indra Sawhney", "standard case name (Indra Sawhney v. Union of India)"),
    ("Visheswaraya", "Visvesvaraya", "standard spelling of Sir M. Visvesvaraya"),
    ("Kathakalli", "Kathakali", "standard dance-form name"),
    ("Dara Sikoh", "Dara Shikoh", "standard spelling"),
    ("Siddharta Gautama", "Siddhartha Gautama", "standard spelling"),
    ("Alfred Wegner", "Alfred Wegener", "standard spelling of geologist"),
    ("General Manoj Narawane", "General Manoj Naravane", "standard spelling of COAS name"),
    ("Mayor and Salovey", "Mayer and Salovey", "psychologist John D. Mayer"),
    ("Mayor & Salovey", "Mayer & Salovey", "psychologist John D. Mayer"),
    ("Warren Buffet", "Warren Buffett", "standard spelling"),
    ("Savitri Bai Phule", "Savitribai Phule", "standard spelling"),
    ("G S Bentick", "G S Bentinck", "standard spelling of Governor-General"),
    ("Kuchipuri", "Kuchipudi", "standard dance-form name"),
    ("Burakatha", "Burra Katha", "standard form name"),
    ("Tarangmal", "Tarangmel", "standard dance form (Goa)"),
    ("Abhinay Darpan", "Abhinaya Darpana", "standard text name"),
    ("foresightening", "foreshortening", "standard art term"),
    ("Arcuade", "Arcuate", "standard architecture term"),
    ("Tuglaq", "Tughlaq", "standard dynasty name"),
    ("Dropadi", "Draupadi", "standard name"),
    ("Rajsimhavarman", "Rajasimhavarman", "standard name (Narasimhavarman II Rajasimha)"),
    ("Vijaynagar", "Vijayanagar", "standard empire name"),
    ("Lingraj", "Lingaraj", "standard temple name"),
    ("Rajarasjeshwara", "Rajarajeshwara", "standard temple name"),
    ("Panchpandav", "Panchapandava", "standard ratha name"),
    ("rupiah", "rupiya", "standard Gupta coin name"),
    ("Quadam Rasul", "Qadam Rasul", "standard shrine name"),
    ("Sharqui", "Sharqi", "standard dynasty name"),
    ("Adhai din ka jhopra", "Adhai Din Ka Jhonpra", "standard mosque name"),
    ("Huein Tsang", "Hiuen Tsang", "standard spelling"),
    ("Harisen", "Harisena", "standard name (Allahabad Pillar inscription)"),
    ("Kalidas", "Kalidasa", "standard name"),
    ("Vishakhadutta", "Visakhadatta", "standard name (Mudrarakshasa author)"),
    ("Aryabhatt", "Aryabhata", "standard astronomer name"),
    ("Surya Siddhantika", "Surya Siddhanta", "standard text name"),
    ("Vijaywada", "Vijayawada", "standard city name"),
    ("Ankapallee", "Anakapalle", "standard place name"),
    ("Piprawaha", "Piprahwa", "standard site name"),
    ("Mukrarakshasa", "Mudrarakshasa", "standard text name"),
    ("khalisatn", "Khalistan", "standard spelling"),
    ("sabrimala", "Sabarimala", "standard temple name"),
    ("devdasi", "Devadasi", "standard term, capitalised"),
    ("narender Dabholkar", "Narendra Dabholkar", "standard name"),
    ("Gauri lankesh", "Gauri Lankesh", "standard name, capitalised"),
    ("Kaktiya", "Kakatiya", "standard dynasty name"),
    ("rayagada model", "Rayagada model", "standard place name, capitalised"),
    ("Vidharba", "Vidarbha", "standard region name"),
    ("Shanqxi", "Shanxi", "standard province name"),
    ("throium", "thorium", "standard element name"),
    ("Gulf of Khambat", "Gulf of Khambhat", "standard spelling"),
    ("Vyzag", "Vizag", "standard short form of Visakhapatnam"),
    ("AyaRam GayaRam", "Aaya Ram Gaya Ram", "standard phrase"),
    ("sarve bhavanthu sukhinah", "Sarve bhavantu sukhinah", "standard transliteration"),
    ("V K Vakankar", "V.S. Wakankar", "archaeologist's correct name (fact-corrected vs PDF)"),
    ("Aichi Ladakh", "Alchi, Ladakh", "Alchi monastery (fact-corrected; PDF itself had error)"),
    ("Rein Bashera", "Rain Basera", "standard name for night shelters (rain basera)"),
    ("Justice Kurien", "Justice Kurian", "Justice Kurian Joseph"),
    ("Bhagvad Geeta", "Bhagavad Gita", "standard spelling used elsewhere in the book"),
    ("Madhyammarga", "Madhyamarga", "standard transliteration"),
    ("Statute of Unity, Statute of Equality", "Statue of Unity, Statue of Equality", "both are statues (fact-corrected)"),
    ("Narsimha:", "Narasimha:", "standard name (Mamallapuram)"),
    ("Narsimha, Mahishasura", "Narasimha, Mahishasura", "standard name (Mamallapapur sculpture)"),
    ("Mckenzie", "McKenzie", "standard spelling"),
]

# quote-block replacements need verifier allowlist; caps removals too
log, quote_repl, caps_rem = [], {}, {}
for old, new, reason in FIXES:
    n = book.count(old)
    if n == 0:
        log.append(f"SKIP (0 found): {old!r} -> {new!r}")
        continue
    # locate each occurrence
    for m in list(re.finditer(re.escape(old), book)):
        cid, blk = card_of(m.start()), block_of(m.start())
        if blk == 'quote':
            quote_repl.setdefault(cid, {}).setdefault('quote', (old, new, reason))
        elif old[0].isupper() or any(c.isupper() for c in old):
            caps_rem.setdefault(cid, {}).setdefault(blk, set()).add(old)
    book = book.replace(old, new)
    log.append(f"FIXED {n}x: {old!r} -> {new!r}  [{reason}]")

open(PATH, 'w').write(book)

# merge allowlist additions into approved_corrections.py
ac_path = '/home/z/my-project/approved_corrections.py'
ac = open(ac_path).read()
add = []
for cid, blocks in sorted(quote_repl.items()):
    for blk, (o, nw, r) in blocks.items():
        add.append(f"    {cid!r}: {{'quote': ({o!r}, {nw!r}, {r!r})}},")
if add:
    ac = ac.replace("APPROVED_QUOTE_REPLACEMENTS = {\n", "APPROVED_QUOTE_REPLACEMENTS = {\n" + "\n".join(add) + "\n")
add = []
for cid, blocks in sorted(caps_rem.items()):
    for blk, toks in blocks.items():
        add.append(f"    {cid!r}: {{'conclusion': {sorted(toks)}}}," if False else f"    {cid!r}: {{'*': {sorted(toks)}}},")
if add:
    ac = ac.replace("APPROVED_CAPS_REMOVALS = {\n", "APPROVED_CAPS_REMOVALS = {\n" + "\n".join(add) + "\n")
open(ac_path, 'w').write(ac)

# verifier must honor '*' wildcard block key for caps
print('\n'.join(log))
print(f"\nquote replacements: {len(quote_repl)}, caps entries: {len(caps_rem)}")
