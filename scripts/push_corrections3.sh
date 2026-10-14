#!/bin/bash
# corrections-3 (C9) push — takes GitHub PAT as $1
# Usage: bash /home/z/my-project/scripts/push_corrections3.sh <PAT>
set -e

PAT="$1"
if [ -z "$PAT" ]; then echo "ERROR: PAT required as first argument"; exit 1; fi
REPO="upsc-serv-1/yfhgkjgiuy"
CLONE="/home/z/ghrepo"
P="/home/z/my-project"

rm -rf "$CLONE"
echo "--- cloning $REPO ---"
if ! git clone "https://x-access-token:${PAT}@github.com/${REPO}.git" "$CLONE" 2>&1 | sed "s/${PAT}/***PAT***/g"; then
  echo "ERROR: clone failed (bad PAT or no access)"; exit 1
fi

echo "--- copying C9 files ---"
cp "$P/polished/MERGED_full_1-789.md"            "$CLONE/polished/"
cp "$P/polished/MERGED_full_1-789.pre-C9.bak.md" "$CLONE/polished/"
cp "$P/corrections_log.md"                       "$CLONE/"
cp "$P/worklog.md"                               "$CLONE/"
mkdir -p "$CLONE/scripts"
cp "$P/scripts/c9_check.py"                      "$CLONE/scripts/"

cd "$CLONE"
git config user.name  "Z User"
git config user.email "z@container"
git add polished/MERGED_full_1-789.md polished/MERGED_full_1-789.pre-C9.bak.md corrections_log.md worklog.md scripts/c9_check.py
if git diff --cached --quiet; then echo "nothing to commit"; else
  git commit -m "corrections-3 (C9 third-pass cleanup: 16 exact-word line edits; 789 cards, all fences closed, diff verified)"
fi

echo "--- pushing ---"
git push origin main 2>&1 | sed "s/${PAT}/***PAT***/g"
git remote set-url origin "https://github.com/${REPO}.git"   # scrub token from config

echo "--- verify ---"
git fetch origin 2>/dev/null
git log origin/main --oneline -1
git status -sb | head -1
echo "PUSH OK: corrections-3 is on GitHub"
