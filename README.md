# agent-kit

Customizations for coding agents (Claude Code, Codex, Gemini CLI, Antigravity).

- `skills/<name>/SKILL.md`: skills. Install by symlinking the folder into the
  agent's skills directory, e.g. `ln -s "$PWD/skills/agents-md" ~/.claude/skills/`.
- `rules/<name>/`: always-on instructions with an `install.sh` that wires them
  into each agent's user-level instruction file. Run it once.

| Item | What it does |
| --- | --- |
| `skills/agents-md` | Create or tighten a minimal AGENTS.md + CLAUDE.md for a repo |
| `rules/pushback` | Verify, object once with evidence, then follow the user's decision |
