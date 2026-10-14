#!/usr/bin/env python3
"""C9 verification: card count + ::: pairing check for MERGED_full_1-789.md."""
import sys

PATH = "/home/z/my-project/polished/MERGED_full_1-789.md"

with open(PATH, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

cards = 0
open_count = 0
close_count = 0
errors = []

in_frontmatter = False
current_card = None
open_tag = None  # line no. of current unclosed opening fence

for i, raw in enumerate(lines, 1):
    line = raw.rstrip("\r")
    stripped = line.strip()

    # Count card ids (YAML 'id:' lives between the --- delimiters)
    if stripped.startswith("id: ") and in_frontmatter:
        cards += 1
        current_card = stripped[4:].strip()
        if open_tag is not None:
            errors.append(f"line {i}: card {current_card} starts while block from line {open_tag} still open")
            open_tag = None

    # Track YAML frontmatter delimiters (only '---' lines)
    if stripped == "---":
        in_frontmatter = not in_frontmatter
        continue

    if in_frontmatter:
        continue

    if stripped.startswith(":::"):
        body = stripped[3:].strip()
        if body == "":
            # closing fence
            close_count += 1
            if open_tag is None:
                errors.append(f"line {i}: closing ':::' without an open block (card {current_card})")
            else:
                open_tag = None
        else:
            # opening fence like :::quote or :::detail label="..."
            open_count += 1
            if open_tag is not None:
                errors.append(f"line {i}: opening '{stripped}' while block from line {open_tag} still open (card {current_card})")
            open_tag = i

if open_tag is not None:
    errors.append(f"EOF: block opened at line {open_tag} never closed")

print(f"cards: {cards}")
print(f"opening fences: {open_count}")
print(f"closing fences: {close_count}")
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors:
        print("  " + e)
    sys.exit(1)
print("pairing: OK - every opening ::: is closed, no stray closings")
