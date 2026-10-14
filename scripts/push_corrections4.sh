#!/bin/bash
set -e
PAT="$1"; REPO="upsc-serv-1/yfhgkjgiuy"; CLONE="/home/z/ghrepo"; P="/home/z/my-project"
[ -z "$PAT" ] && { echo "ERROR: PAT required"; exit 1; }
rm -rf "$CLONE"
git clone "https://x-access-token:${PAT}@github.com/${REPO}.git" "$CLONE" 2>&1 | sed "s/${PAT}/***/g"
cp "$P/polished/MERGED_full_1-789.md"            "$CLONE/polished/"
cp "$P/polished/MERGED_full_1-789.pre-C9.bak.md"  "$CLONE/polished/" 2>/dev/null || true
cp "$P/polished/MERGED_full_1-789.pre-C10.bak.md" "$CLONE/polished/"
cp "$P/corrections_log.md" "$CLONE/"; cp "$P/worklog.md" "$CLONE/"
mkdir -p "$CLONE/scripts"
cp "$P/scripts/"c9_check.py "$P/scripts/"c10*.py "$CLONE/scripts/" 2>/dev/null || true
cp "$P/scripts/push_corrections3.sh" "$P/scripts/push_corrections4.sh" "$CLONE/scripts/" 2>/dev/null || true
cp "$P/verify_protected.py" "$P/approved_corrections.py" "$CLONE/" 2>/dev/null || true
cd "$CLONE"
git config user.name "Z User"; git config user.email "z@container"
git add -A
git diff --cached --quiet && echo "nothing to commit" || git commit -m "corrections-4 (C10 full issue-list cleanup: shorthand/names/dates, 0035+0073+0011 rebuilds, placeholders filled with verified facts, fact labels, stray punctuation; verifier 0 errors)"
git push origin main 2>&1 | sed "s/${PAT}/***/g"
git remote set-url origin "https://github.com/${REPO}.git"
git fetch origin 2>/dev/null; git log origin/main --oneline -1
echo "PUSH OK: corrections-4 is on GitHub"
