#!/usr/bin/env python3
"""C5: inline cross-references + complete truncated cards (user-approved).
Sources: original PDFs (P1/GS1) for referenced text; standard subject knowledge
for intelligent completions where the PDF itself ended mid-sentence."""
import re

PATH = '/home/z/my-project/polished/MERGED_full_1-789.md'
book = open(PATH).read()
log = []

def rep(old, new, why, expect=1):
    global book
    n = book.count(old)
    if n != expect:
        log.append(f"SKIP (found {n}, expected {expect}): {why}")
        return
    book = book.replace(old, new)
    log.append(f"OK {why}")

# --- 0011 Mughal Architecture: dangling intro fragment + same-as-above conclusion ---
rep(":::introduction\n**Golden period**.\n:::",
    ":::introduction\nThe Mughal period is regarded as the **golden period** of Indian medieval architecture.\n:::",
    "0011 intro fragment completed (standard art-history fact)")

rep(":::conclusion\n(Same as above).\n:::\n\n---\nid: GS1-HIST-0012",
    ":::conclusion\n- A living proof of the harmonious blend of **cultural diversity & artistic ingenuity** that shaped India's architectural landscape.\n- Adaptation to local traditions — temple elements like the **bell & chain, lotus, lintels in mihrabs, toranas**.\n:::\n\n---\nid: GS1-HIST-0012",
    "0011 conclusion inlined from card 0010 (Indo-Islamic architecture, as the source intended)")

# --- 0138 earthquakes/volcanoes: complete truncated conclusion from the general geophysical conclusion ---
rep(":::conclusion\nSame as geophysical phenomena (understanding the distribution of __ coupled with monitoring, modeling, interdisciplinary - can help us",
    ":::conclusion\nAs with geophysical phenomena generally: understanding the distribution of such events, coupled with monitoring, modelling and interdisciplinary collaboration, helps us better predict and address them",
    "0138 truncated conclusion completed from the book's general geophysical conclusion (P1 PDF page 1)")

# --- 0139 Ring of Fire: same as above -> inlined 0138 conclusion ---
rep(":::conclusion\nSame as above.\n:::\n\n---\nid: GS1-GEOG-0140",
    ":::conclusion\nAs with geophysical phenomena generally: understanding the distribution of such events, coupled with monitoring, modelling and interdisciplinary collaboration, helps us better predict and address them.\n:::\n\n---\nid: GS1-GEOG-0140",
    "0139 'Same as above' inlined from 0138")

# --- 0146 El Nino/La Nina: conclusion ends mid-sentence in the source PDF itself ---
rep("- While La Nina benefits the Indian monsoon, the unpredictable & disruptive alternation of **El Ninos** can...",
    "- While La Nina benefits the Indian monsoon, the unpredictable and disruptive alternation of **El Nino** events can still unsettle agriculture and rural livelihoods.",
    "0146 conclusion completed (source PDF itself ends mid-sentence)")

# --- 0147 ENSO: same as El Nino/La Nina -> 0146's conclusion ---
rep(":::conclusion\n(Same as El Nino/La Nina).\n:::",
    ":::conclusion\n- El Nino's disruption of the monsoon can **severely jeopardize Indian agriculture & food security** — adaptive strategies and resilient farming practices are urgently needed.\n- La Nina benefits the monsoon, but the unpredictable alternation of **El Nino** events can still unsettle rural livelihoods.\n:::",
    "0147 'Same as El Nino/La Nina' inlined from 0146")

# --- 0148 IOD: same as ocean currents -> 0150's conclusion ---
rep(":::conclusion\n(Same as ocean currents).\n:::",
    ":::conclusion\nOcean currents — **the Earth's silent climate conductors** — call for focused research and global collaboration to unravel their intricate roles.\n:::",
    "0148 'Same as ocean currents' inlined from 0150")

# --- 0144 Sea-floor spreading: same as CDT -> relevant bullet from 0143 ---
rep(":::conclusion\n(Same as Continental Drift theory).\n:::",
    ":::conclusion\n- These theories, combined with modern tech advances, help humankind **predict disasters more efficiently** — making lives safer and the economy more resilient.\n:::",
    "0144 'Same as Continental Drift theory' inlined from 0143")

# --- 0126 Cobalt: same as strategic minerals -> 0124 Rare Earth mission line ---
rep(":::conclusion\n(Same as strategic minerals).\n:::",
    ":::conclusion\nSet up strategic-mineral missions on the lines of the semiconductor mission (e.g. an **Indian Rare Earth Mission**), to promote exploration & self-sufficiency.\n:::",
    "0126 'Same as strategic minerals' inlined from 0124")

# --- 0156 Samudrayaan: same as above -> 0155's conclusion ---
rep(":::conclusion\nSame as above.\n:::\n\n---\nid: GS2-POLI-0157",
    ":::conclusion\n**Neel Kranti se arth kranti** — the blue-economy transformation the Deep Ocean Mission and Samudrayaan aim to deliver.\n:::\n\n---\nid: GS2-POLI-0157",
    "0156 'Same as above' inlined from 0155 (Deep Ocean Mission)")

# --- 0175 RPA: cross-reference -> common elections conclusion content ---
rep(":::conclusion\n(Refer to common elections conclusion — Jimmy Carter quote.)\n:::",
    ":::conclusion\n- Free and fair elections are the **lifeblood of any democracy** (Jimmy Carter) — India, the **Mother of Democracy**, must keep strengthening them.\n:::",
    "0175 cross-reference inlined from the common elections conclusion (0178)")

# --- 0235 ECI: cross-reference -> common elections conclusion content ---
rep(":::conclusion\n(Refer to common elections conclusion.)\n:::",
    ":::conclusion\n- Free and fair elections at the Centre and in the States are the **lifeblood of any democracy** (Jimmy Carter) — the common conclusion the book returns to.\n:::",
    "0235 cross-reference inlined from the common elections conclusion (0178)")

# --- 0255 CVC: 'Same as NCM' -> real conclusion; CPI rank fix (same as 0250) ---
rep(":::conclusion\nSame as NCM - needs to be **strengthened**.\n:::",
    ":::conclusion\nIt should be strengthened with **more teeth, operational independence and active participation by stakeholders**.\n:::",
    "0255 'Same as NCM' inlined from 0248/0253")

rep("India’s rank in the Corruption Perception Index is **86th**.",
    "India’s rank in the Corruption Perception Index is **91st out of 182 (CPI 2025, Transparency International)**.",
    "0255 CPI rank updated to CPI 2025 (same verified fix as 0250/0232/0724)")

# --- 0402 NFT: 'Same as Cryptocurrency card' -> real conclusion ---
rep(":::conclusion\nSame as Cryptocurrency card.\n:::",
    ":::conclusion\nRegulation must strike a balance between **innovation and investor protection**; India's approach (CFSP/CBDC work) is heading in the right direction.\n:::",
    "0402 'Same as Cryptocurrency card' inlined from 0401's (completed) conclusion")

# --- 0401 Cryptocurrency: complete truncated conclusion (source ends 'a balance…') ---
rep("Regulation must strike a balance… and **CBDC is heading in the right direction**.",
    "Regulation must strike a balance between **innovation and investor protection**, and the **CBDC** is heading in the right direction.",
    "0401 truncated conclusion completed")

open(PATH, 'w').write(book)
print('\n'.join(log))
