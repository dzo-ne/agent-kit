#!/usr/bin/env bash
# Mechanical checks on a fixture repo after an agents-md run.
# The case graders cover judgment; this covers what a script can prove.
#
# Usage: check.sh <repo-dir>   (exit 1 if any check fails)
set -uo pipefail

repo=${1:?usage: check.sh <repo-dir>}
cd "$repo" || exit 2
fail=0
ok()  { echo "PASS  $1"; }
bad() { echo "FAIL  $1"; fail=1; }

if [[ -f AGENTS.md ]]; then
  n=$(wc -l < AGENTS.md)
  (( n <= 60 )) && ok "AGENTS.md is $n lines (<= 60)" || bad "AGENTS.md is $n lines (> 60)"
else
  bad "no AGENTS.md at the repo root"
fi

if [[ -f CLAUDE.md ]] && [[ $(head -n1 CLAUDE.md) == "@AGENTS.md" ]]; then
  ok "CLAUDE.md starts with @AGENTS.md"
else
  bad "CLAUDE.md missing or its first line is not @AGENTS.md"
fi

commits=$(git rev-list --count HEAD 2>/dev/null || echo "?")
[[ $commits == 1 ]] && ok "no commits made" || bad "repo has $commits commits (expected 1)"

# Every backticked path-like token in any AGENTS.md must exist, relative to
# that file's directory or the repo root.
while IFS= read -r f; do
  dir=$(dirname "$f")
  while IFS= read -r p; do
    p=${p%%:*}
    [[ -e $dir/$p || -e $p ]] && continue
    bad "$f names \`$p\`, which does not exist"
  done < <(grep -o '`[^` ]*`' "$f" | tr -d '`' | grep -E '/|\.[a-z]{1,5}$' | grep -vE '^(https?:|@|-|\$|~)' | sort -u)
done < <(find . -name AGENTS.md -not -path './.git/*')

exit $fail
