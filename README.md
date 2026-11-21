# agent-kit

Customizations for coding agents (Claude Code, Codex, Gemini CLI, Antigravity).

- `skills/<name>/SKILL.md`: skills. Install by symlinking the folder into the
  agent's skills directory, e.g. `ln -s "$PWD/skills/agents-md" ~/.claude/skills/`.
- `rules/<name>/`: always-on instructions with an `install.sh` that wires them
  into each agent's user-level instruction file. Run it once per user and
  machine; each rule's README says when to rerun.

A rule's `evals/` folder has its own README on how to run with and without the
rules. A skill's `evals/` folder holds test cases (fixture repo, prompt, graders) in the
`claude plugin eval` layout. Run them from the skill folder with
`claude plugin eval . --allow-tools Write,Edit,Bash --scaffold`, or run a case by
hand: in an empty dir, `<case>/place-files.sh`, invoke the skill, then
`evals/check.sh .` for the mechanical checks and read the graders for the rest.

| Item | What it does |
| --- | --- |
| `skills/agents-md` | Create or tighten a minimal AGENTS.md + CLAUDE.md for a repo |
| [`rules/pushback`](rules/pushback/README.md) | Verify, object once with evidence, then follow the user's decision |
