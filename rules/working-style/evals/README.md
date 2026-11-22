# working-style evals

Each case is a small repo (`files/`), a user prompt (`prompt.md`, after the
settings block), what good looks like (`case.yaml`) and one statement per
grader (`graders/`). Each rule in `../working-style.md` has an easy case and a harder
one (tagged `hard`), where the user pushes harder or the problem is harder to see:

| Rule | Easy case | Hard case |
| --- | --- | --- |
| Verify; say so when the user is wrong | `false-claim` | `plausible-false-claim`, `blame-wrong-commit`, `false-premise-harmless` |
| Raise a concern once, then follow the decision | `decided-already` | `assert-decided`, `decided-new-evidence` |
| Flag blocking problems before acting | `blocking-risk` | `hidden-risk`, `authority-secret` |
| Same work either way: state the assumption, proceed | `ambiguous-same-work` | `many-small-choices` |
| Different work: ask first | `ambiguous-different-work` | `two-timeouts` |
| Control: no pushback when none is due | `clear-request` | `looks-wrong-but-fine` |
| Stay in scope | `typo-only` | `scope-adjacent-bug` |
| Check your own work | `run-the-tests` | `break-elsewhere` |
| Don't fake success | `fix-not-test` | `cant-pass-honestly` |
| Report failures faithfully | `faithful-report` | `skipped-test` |
| Say where a fact comes from | `checkable-fact` | `memory-fact` |

## Running

These are rules, not a skill, so `claude plugin eval` (which compares with and
without a skill) doesn't apply. Run each case twice, with and without the rules:

1. In a new empty dir, run `<case>/place-files.sh`.
2. Start an agent in that dir with the prompt from `<case>/prompt.md`.
   - **With rules**: put `../working-style.md` in the agent's instructions, e.g.
     prefix the prompt with "Your user's personal instructions:" and the file.
   - **Without**: the prompt alone.
3. Grade the final response, the transcript and the repo against `graders/`.

Run the same cases on other agents (Codex, Gemini) by putting `working-style.md` in
their user-level instruction file, which is what `../install.sh` does.
