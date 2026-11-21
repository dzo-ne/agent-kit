# pushback evals

Each case is a small repo (`files/`), a user prompt (`prompt.md`, after the
settings block), what good looks like (`case.yaml`) and one statement per
grader (`graders/`). Seven cases, one or two per rule in `../pushback.md`:

| Case | Rule it tests |
| --- | --- |
| `false-claim` | Verify before objecting; say so when the user is wrong |
| `decided-already` | Raise a concern once, then follow the decision |
| `blocking-risk` | Flag blocking problems (data loss) before acting |
| `ambiguous-same-work` | Readings lead to the same work: state the assumption, proceed |
| `ambiguous-different-work` | Readings lead to different work: ask first |
| `clear-request` | Control: no pushback when none is due |
| `faithful-report` | Report failures instead of claiming success |

## Running

These are rules, not a skill, so `claude plugin eval` (which compares with and
without a skill) doesn't apply. Run each case twice, with and without the rules:

1. In a new empty dir, run `<case>/place-files.sh`.
2. Start an agent in that dir with the prompt from `<case>/prompt.md`.
   - **With rules**: put `../pushback.md` in the agent's instructions, e.g.
     prefix the prompt with "Your user's personal instructions:" and the file.
   - **Without**: the prompt alone.
3. Grade the final response, the transcript and the repo against `graders/`.

Run the same cases on other agents (Codex, Gemini) by putting `pushback.md` in
their user-level instruction file, which is what `../install.sh` does.
