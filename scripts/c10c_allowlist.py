#!/usr/bin/env python3
"""C10c — append C10 approved-correction entries to approved_corrections.py."""
import sys, re, json
sys.path.insert(0, "/home/z/my-project")
import convert

def split_cards(md):
    cards = {}
    for chunk in re.split(r"(?m)^---\nid: ", md)[1:]:
        cid = chunk.split("\n", 1)[0].strip()
        head, body = chunk.split("\n---\n", 1)
        cards[cid] = body
    return cards

def blocks(body):
    return {(m.group(1), m.group(2) or ""): m.group(3).strip() for m in
            re.finditer(r'(?ms)^:::(\w+)(?: label="([^"]*)")?\n(.*?)\n:::', body)}

def plain(t): return re.sub(r"[\s*]+", " ", t).strip()

MERGED = "/home/z/my-project/polished/MERGED_full_1-789.md"
ACPATH = "/home/z/my-project/approved_corrections.py"

# 1) compute full-quote (old, new) plain pairs for quote-changed cards
QUOTE_CARDS = ["GS1-HIST-0056", "GS1-GEOG-0153", "GS1-GEOG-0155", "GS4-ETHI-0581",
               "GS4-ETHI-0582", "GS4-ETHI-0657", "GS4-ETHI-0658", "GS4-ETHI-0743",
               "GS4-ETHI-0787"]
REASONS = {
    "GS1-HIST-0056": "C10: obvious typo 'noy'->'not' inside quote, substance unchanged",
    "GS1-GEOG-0153": "C9: user-directed hard-word fix in unattributed placeholder quote",
    "GS1-GEOG-0155": "C9: user-directed hard-word fix in unattributed placeholder quote",
    "GS4-ETHI-0581": "C10: stray quote punctuation artefact removed",
    "GS4-ETHI-0582": "C10: stray quote punctuation artefact removed",
    "GS4-ETHI-0657": "C10: stray quote punctuation artefacts removed (MLK/Kalam line)",
    "GS4-ETHI-0658": "C10: obvious misspelling 'conscient'->'conscience' in Kalam quote",
    "GS4-ETHI-0743": "C10: stray quote punctuation artefact removed (Annan quote)",
    "GS4-ETHI-0787": "C10: stray quote punctuation artefact removed (marital-rape quote)",
}
d = json_data = None
import json
d = json.load(open(convert.SRC))
pol = split_cards(open(MERGED, encoding="utf-8", newline="").read().replace("\r\n", "\n"))

quote_entries = {}
for cid in QUOTE_CARDS:
    i = int(cid.rsplit("-", 1)[1])
    obody = convert.convert(i, d[i - 1]).split("\n---\n", 1)[1]
    oq = blocks(obody)[("quote", "")]
    pq = blocks(pol[cid].split("\n", 1)[1])[("quote", "")]
    quote_entries[cid] = {"quote": (plain(oq), plain(pq), REASONS[cid])}

# 2) number / list entries
num_add = {
    "GS1-HIST-0035": {"10": "rebuild: 4th-10th CE Western Gangas", "3": "rebuild: 3rd-X CE dynasty date ranges",
                      "4": "rebuild: 3rd/4th/6th CE date ranges", "5": "rebuild: 3rd-5th CE Vakatakas",
                      "6": "rebuild: 4th-6th CE Kadambas", "7": "rebuild: 3rd-7th CE Kalabhras",
                      "983": "rebuild: Gomateshwara erected c. 983 CE"},
    "GS1-HIST-0073": {"10": "1857 rebuild: Meerut outbreak 10 May 1857", "1848": "Doctrine of Lapse: Satara 1848",
                      "1853": "Jhansi annexation 1853", "1856": "Awadh annexation + General Service Enlistment Act 1856",
                      "1857": "1857 revolt year / Barrackpore / Meerut", "1858": "GoI Act 1858 + Queen's Proclamation 1858"},
    "GS1-HIST-0075": {"19": "19th-century reform movements intro added"},
    "GS1-GEOG-0110": {"6": "energy-mix share ~6% clarifier (distinct from 3.9% capacity share)"},
    "GS1-GEOG-0121": {"21.71%": "forest-cover-only figure added to separate the two measures"},
    "GS2-POLI-0172": {"153": "IPC 153A", "267": "Law Commission 267th Report", "295": "IPC 295A", "505": "IPC 505"},
    "GS2-GOVE-0243": {"2000": "IT Act 2000", "2008": "IT Act amendment 2008", "4": "I4C cyber centre"},
    "GS2-GOVE-0264": {"3": "3F (funds, functionaries, functions) reference"},
    "GS2-SOCI-0279": {"2020": "NEP 2020", "3": "5+3+3+4 school design", "4": "5+3+3+4 school design",
                      "5": "5+3+3+4 school design", "6": "NEP 6% of GDP public-spending goal"},
    "GS2-SOCI-0280": {"2.5%": "NHP 2017 2.5% GDP target", "2017": "National Health Policy 2017"},
    "GS2-SOCI-0284": {"38": "Art. 38 welfare state", "46": "Art. 46 weaker sections"},
    "GS3-AGRI-0361": {"3": "Mihir Shah list renumbered 1,2,1,2 -> 1,2,3,4", "4": "Mihir Shah list renumbered"},
    "GS3-SCIE-0392": {"10%": "~10% of $5 tn target retained", "2022": "NASSCOM AI Adoption Index 2022",
                      "450": "NASSCOM $450-500 Bn range", "5": "$5 tn economy target"},
    "GS3-SCIE-0414": {"2035": "Bharatiya Antariksh Station roadmap (announced)", "2040": "Indian on Moon roadmap (announced)"},
    "GS3-SCIE-0424": {"1990": "technology denial episode of the 1990s", "2014": "GSLV-D5 indigenous cryogenic success",
                      "5": "GSLV-D5"},
    "GS3-ENVI-0451": {"24.62%": "forest+tree cover figure added to separate the two measures"},
    "GS3-INTE-0535": {"1": "new criminal laws in force 1 July 2024", "2024": "in force 1 July 2024"},
}
num_rm = {
    "GS1-HIST-0035": {"8": "Samudragupta 8 coin-types detail removed in rebuild",
                      "10": "Cave 10 detail removed in rebuild", "16": "Cave 16 detail removed in rebuild",
                      "34": "Ellora 34 caves detail removed in rebuild"},
    "GS3-AGRI-0361": {"1": "duplicate list number removed (1,2,1,2 -> 1,2,3,4)",
                      "2": "duplicate list number removed (1,2,1,2 -> 1,2,3,4)"},
    "GS3-SCIE-0392": {"2018": "NITI Aayog 2018 attribution removed; figure re-sourced to NASSCOM 2022 (web-verified)"},
    "GS3-SCIE-0414": {"1": "Aditya L1 placeholder conclusion replaced with real Gaganyaan conclusion"},
}
list_ch = {
    "GS1-HIST-0011": (9, 10, "Regional styles line restored from source PDF p.17"),
    "GS1-HIST-0073": (4, 14, "12MPRO framework notes replaced with real 1857 content (causes/centres/aftermath)"),
}

# 3) emit the append block
def pydict(d, indent=4):
    import pprint
    return pprint.pformat(d, width=100, sort_dicts=False)

block = f"""

# ---------------------------------------------------------------------------
# C10 - THIRD-PASS ISSUE CLEANUP (user-reported list; web-verified facts where added)
# Generated by scripts/c10c_allowlist.py - full-quote pairs computed from the
# original JSON via convert.py so the verifier's single-replace check passes.
APPROVED_QUOTE_REPLACEMENTS.update({pydict(quote_entries)})

APPROVED_NUMBER_ADDITIONS.update({pydict(num_add)})

APPROVED_NUMBER_REMOVALS.update({pydict(num_rm)})

APPROVED_LIST_CHANGES.update({pydict(list_ch)})
"""
with open(ACPATH, "a", encoding="utf-8") as f:
    f.write(block)
print("allowlist entries appended")
