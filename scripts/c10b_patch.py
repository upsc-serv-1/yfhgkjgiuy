#!/usr/bin/env python3
"""Repair the three quote-mangled lines in c10b_rebuilds.py (robust escaping)."""
PATH = "/home/z/my-project/scripts/c10b_rebuilds.py"
sq, dq = chr(39), chr(34)  # ' "

def lit(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def pyline(label, old, new):
    return f'rep("{label}", {lit(old)}, {lit(new)})'

fixes = {
    "0581+0582 plato": pyline("0581+0582 plato",
        "is **cultivated there**" + sq + "." + dq + ".",
        "is **cultivated there**" + sq + "." + dq),
    "0638 divya": pyline("0638 divya",
        "to **solve their concerns**." + dq + ".",
        "to **solve their concerns**." + dq),
    "0759 social audit": pyline("0759 social audit",
        "30,000 government officials involved in **corruption**." + dq + ".",
        "30,000 government officials involved in **corruption**." + dq),
}

lines = open(PATH, encoding="utf-8").read().splitlines()
hit = 0
for i, ln in enumerate(lines):
    for label, newline in fixes.items():
        if f'"{label}"' in ln and ln.strip().startswith("rep("):
            lines[i] = newline
            hit += 1
open(PATH, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"patched {hit} lines")
