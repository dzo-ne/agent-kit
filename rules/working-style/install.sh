#!/usr/bin/env bash
# Install working-style.md into each coding agent's user-level instructions.
# Claude Code and Gemini CLI import it, Antigravity symlinks it, so edits to
# working-style.md apply without reinstalling. Codex gets a copy: rerun after edits.
#
# Usage: install.sh [--uninstall]   (asks before touching each tool)
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
rules="$here/working-style.md"
start='<!-- working-style:start -->'
end='<!-- working-style:end -->'
codex_home="${CODEX_HOME:-$HOME/.codex}"
agy_plugin="$HOME/.gemini/config/plugins/working-style"
# These rules used to be called "pushback"; installs from then are cleaned up.
legacy_start='<!-- pushback:start -->'
legacy_end='<!-- pushback:end -->'
legacy_agy_plugin="$HOME/.gemini/config/plugins/pushback"

uninstall=false
case "${1:-}" in
  --uninstall) uninstall=true ;;
  "") ;;
  *) echo "usage: $0 [--uninstall]" >&2; exit 2 ;;
esac

ask() {
  local reply
  read -r -p "$1 [Y/n] " reply || reply=n
  [[ -z $reply || $reply == [yY]* ]]
}

# Remove a marked block (markers $2..$3) from a file, keeping everything else.
strip_block() {
  [[ -f $1 ]] || return 0
  local tmp
  tmp="$(mktemp)"
  awk -v s="${2:-$start}" -v e="${3:-$end}" '
    $0 == s { skip = 1; next }
    skip { if ($0 == e) skip = 0; next }
    /^$/ { blank++; next }
    { while (blank > 0) { print ""; blank-- } print }
  ' "$1" > "$tmp"
  cat "$tmp" > "$1"
  rm -f "$tmp"
}

# Replace (or append) our marked block in a file, dropping any legacy block.
put_block() {
  local file=$1 body=$2
  mkdir -p "$(dirname "$file")"
  strip_block "$file"
  strip_block "$file" "$legacy_start" "$legacy_end"
  { [[ -s $file ]] && echo; echo "$start"; printf '%s\n' "$body"; echo "$end"; } >> "$file"
}

# Warn about existing instructions that tell the agent not to push back.
warn_conflicts() {
  [[ -f $1 ]] || return 0
  grep -n -i -E "(never|don't|do not) (question|push back|argue|challenge)|blindly (follow|trust)" "$1" \
    | sed "s|^|  conflict? $1:|" || true
}

# Install or remove our block in one tool's instruction file.
handle_file() {
  local name=$1 file=$2 body=$3
  if $uninstall; then
    [[ -f $file ]] && grep -qF -e "$start" -e "$legacy_start" "$file" || return 0
    ask "Remove working-style from $name ($file)?" || return 0
    strip_block "$file"
    strip_block "$file" "$legacy_start" "$legacy_end"
    [[ -s $file ]] || rm -f "$file"
    echo "  removed from $file"
  else
    ask "Install working-style for $name ($file)?" || { echo "  skipped $name"; return 0; }
    put_block "$file" "$body"
    echo "  wrote $file"
    warn_conflicts "$file"
  fi
}

# The legacy plugin is ours only if its manifest says so.
remove_legacy_plugin() {
  if grep -qs '"name": "pushback"' "$legacy_agy_plugin/plugin.json"; then
    rm -rf "$legacy_agy_plugin"
    echo "  removed old $legacy_agy_plugin"
  fi
}

handle_antigravity() {
  if $uninstall; then
    [[ -d $agy_plugin || -d $legacy_agy_plugin ]] || return 0
    ask "Remove the Antigravity plugin ($agy_plugin)?" || return 0
    rm -rf "$agy_plugin"
    remove_legacy_plugin
    echo "  removed $agy_plugin"
  else
    ask "Install working-style for Antigravity ($agy_plugin)?" || { echo "  skipped Antigravity"; return 0; }
    mkdir -p "$agy_plugin/rules"
    printf '{"name": "working-style"}\n' > "$agy_plugin/plugin.json"
    ln -sfn "$rules" "$agy_plugin/rules/AGENTS.md"
    echo "  linked $agy_plugin/rules/AGENTS.md -> $rules"
    remove_legacy_plugin
  fi
}

found=false
if [[ -d $HOME/.claude ]]; then
  found=true; handle_file "Claude Code" "$HOME/.claude/CLAUDE.md" "@$rules"
fi
if [[ -d $codex_home ]]; then
  found=true; handle_file "Codex" "$codex_home/AGENTS.md" "$(cat "$rules")"
fi
if [[ -f $HOME/.gemini/settings.json ]] || command -v gemini >/dev/null; then
  found=true; handle_file "Gemini CLI" "$HOME/.gemini/GEMINI.md" "@$rules"
fi
if [[ -d $HOME/.gemini/config ]]; then
  found=true; handle_antigravity
fi
if [[ -d $HOME/.cursor ]] && ! $uninstall; then
  found=true
  echo "Cursor has no user-level rules file: paste $rules into Settings > Rules > User Rules."
fi
$found || echo "No supported agents found."
