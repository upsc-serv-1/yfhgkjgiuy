#!/usr/bin/env python3
"""C10 audit: check each user-reported issue against current MERGED_full_1-789.md."""
import re, sys

PATH = "/home/z/my-project/polished/MERGED_full_1-789.md"
text = open(PATH, encoding="utf-8").read()

# Split into cards keyed by numeric suffix
cards = {}
for m in re.finditer(r"^id: ([A-Z0-9-]+-(\d{4}))$", text, re.M):
    cards[int(m.group(2))] = m.group(1)

def card_body(n):
    """Return full card text for numeric id n."""
    cid = cards.get(n)
    if not cid:
        return f"<<CARD {n} NOT FOUND>>"
    nxt = None
    for k in sorted(cards):
        if k > n:
            nxt = cards[k]
            break
    start = text.index(f"id: {cid}")
    end = text.index(f"id: {nxt}") if nxt else len(text)
    return text[start:end]

checks = [
    ("0764 Justice Kurien",        lambda b: "Kurien" in b, 764),
    ("0116 Natnl",                 lambda b: "Natnl" in b, 116),
    ("0106 Natl",                  lambda b: "Natl" in b, 106),
    ("0148 intricate",             lambda b: "intricate" in b, 148),
    ("0116 underscores",           lambda b: "underscore" in b.lower(), 116),
    ("0141 underscoring",          lambda b: "underscore" in b.lower(), 141),
    ("0095 synergy",               lambda b: "synergy" in b, 95),
    ("0108 govt's",                lambda b: "govt" in b.lower(), 108),
    ("0089 Govt",                  lambda b: "Govt" in b, 89),
    ("0536 Whole of Govt",         lambda b: "Whole of Govt" in b, 536),
    ("0107 invt/Auth",             lambda b: re.search(r"\b(invt|Auth)\b", b), 107),
    ("0110 shorthand",             lambda b: re.search(r"\b(Natl|invt|Auth)\b", b), 110),
    ("0132 shorthand",             lambda b: re.search(r"\b(Natl|invt|Auth|mvmt)\b", b), 132),
    ("0123 Envt",                  lambda b: "Envt" in b, 123),
    ("0087 mvmt",                  lambda b: "mvmt" in b, 87),
    ("0102 lowercase names",       lambda b: re.search(r"vidharba|khalistan|belgaum|cauvery|greater nagalim", b, re.I) and re.search(r"vidharba|khalistan|belgaum|cauvery|greater nagalim", b), 102),
    ("0030 table",                 lambda b: re.search(r"\btable\b", b, re.I), 30),
    ("0056 noy",                   lambda b: "noy " in b, 56),
    ("0610 BUFFET",                lambda b: "BUFFET" in b, 610),
    ("0656 BUFFET",                lambda b: "BUFFET" in b, 656),
    ("0606 CORNERSTONE",           lambda b: "CORNERSTONE" in b, 606),
    ("0719 Rajawat/Rajavat",       lambda b: re.search(r"Rajaw|Vat\b", b), 719),
    ("0720 Rajawat/Rajavat",       lambda b: re.search(r"Rajaw|Vat\b", b), 720),
    ("0197 Megha Chandra",         lambda b: "Megha" in b, 197),
    ("0183 Meghachandra",          lambda b: "Megha" in b, 183),
    ("0113 Khambat",               lambda b: "Khamb" in b, 113),
    ("0032 CE BC",                 lambda b: re.search(r"CE BC|BC CE|CE AD", b), 32),
    ("0033 CE BC",                 lambda b: re.search(r"CE BC|BC CE|CE AD", b), 33),
    ("0034 CE AD",                 lambda b: re.search(r"CE BC|BC CE|CE AD", b), 34),
    ("0361 1,2,1,2 numbering",     lambda b: re.search(r"1\..*2\..*1\..*2\.", b, re.S), 361),
    ("0154 indent",                lambda b: b.count("- ") > 0, 154),
    ("0090 truncated line",        lambda b: "Visits by all religions and..." in b, 90),
    ("0394 UMANG no number",       lambda b: "UMANG" in b, 394),
    ("0451 forest 21.7",           lambda b: "21.7" in b, 451),
    ("0121 forest 24.62",          lambda b: "24.62" in b, 121),
    ("0177 O ACS",                 lambda b: "ACS" in b, 177),
    ("0284 O ACS",                 lambda b: "ACS" in b, 284),
    ("0392 $500 Bn",               lambda b: "500" in b, 392),
    ("0351 gas 3.9",               lambda b: "3.9" in b, 351),
    ("0110 gas 3.9",               lambda b: "3.9" in b, 110),
]

print("== STRING CHECKS (True = issue still present) ==")
for name, fn, n in checks:
    b = card_body(n)
    try:
        hit = fn(b)
    except Exception as e:
        hit = f"ERR {e}"
    print(f"{'STILL PRESENT' if hit is True else ('clean' if hit is False else hit)}  |  {name}")

# behavior/offense global scan
print("\n== GLOBAL behavior/offense scan (US spellings in body) ==")
for i, line in enumerate(text.splitlines(), 1):
    if re.search(r"\bbehavior(s|al)?\b|\boffense(s)?\b", line):
        print(f"  line {i}: {line.strip()[:120]}")

# titles of 0065/0067, bodies of 0034/0035, data of 0073, conclusion of 0010/0011, 0243
for n in (65, 67, 34, 35, 73, 10, 11, 243, 30, 56, 102, 4, 75, 172, 264, 279, 280, 284, 292, 296, 414, 424, 509, 529, 531, 430, 394, 183, 218, 535, 177, 284, 392, 351, 110, 109, 119, 121, 451, 361, 154, 90, 106, 107, 113, 197, 720):
    b = card_body(n)
    print(f"\n========== CARD {n} ({cards.get(n)}) ==========")
    print(b[:2600])
