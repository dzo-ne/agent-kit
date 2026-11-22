# working-style

Ten always-on rules for how a coding agent works with you, like a careful
colleague: check before objecting, raise a concern once with evidence and then
follow your decision, stay in scope, check its own work, never fake a passing
result, and say whether a fact was checked or recalled from memory. The rules
are in [`working-style.md`](working-style.md).

It isn't a skill or a plugin. It's a rules file plus an installer that adds it
to each agent's user-level instructions, so it applies in every repo you open.
(For Antigravity the installer creates a small plugin, since that's how
Antigravity loads global rules.)

## Install

Run once per user account, on each machine:

```bash
rules/working-style/install.sh
```

It finds the agents you have installed and asks before touching each one.
Rerunning is safe: it replaces its own block instead of adding a second copy.

| Agent | What the installer does | After editing `working-style.md` |
| --- | --- | --- |
| Claude Code | Adds `@<path>/working-style.md` to `~/.claude/CLAUDE.md` | Applies in new sessions |
| Gemini CLI | Adds the same import to `~/.gemini/GEMINI.md` | Applies in new sessions |
| Antigravity | Creates `~/.gemini/config/plugins/working-style/`, with `rules/AGENTS.md` symlinked to `working-style.md` | Applies in new sessions |
| Codex | Copies the rules into `~/.codex/AGENTS.md` (Codex has no imports) | Rerun the installer |
| Cursor | Prints the file path to paste into Settings > Rules > User Rules | Paste again |

Also rerun it after installing a new agent, or after moving this repo: the
imports and the symlink use absolute paths.

These rules used to be called `pushback`. Running the installer replaces an old
`pushback` install: it removes the old block from each instruction file and the
old Antigravity plugin.

The installer also warns if your existing instructions contradict the rules,
for example a line telling the agent never to question you.

## Uninstall

```bash
rules/working-style/install.sh --uninstall
```

This removes only what the installer added: the marked block in each
instruction file (and the file itself if nothing else is left in it), and the
Antigravity plugin folder.

## Shared repos

The installer only writes user-level files. If you want a repo's own agent
instructions to include these rules, paste `working-style.md` into its
AGENTS.md by hand. That applies them to everyone's agent in that repo, so check
with your team first.

## Tests

[`evals/`](evals/) has 26 cases, at least one easy and one hard case per rule,
and explains how to run them with and without the rules. On Claude the rules
mostly match what it already does. The one clear difference so far: without
them, Claude repeated a concern the user had already overruled. Each case has
only been run a few times, and the other agents haven't been tested yet.
