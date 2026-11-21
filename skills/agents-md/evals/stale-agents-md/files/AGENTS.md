# AGENTS.md

feedsync: pulls RSS feeds and stores new items (Python stdlib).

## Layout
- `src/feedsync/fetch.py` is the only module that makes HTTP requests; add new network calls there.

## Rules
- Commit messages use the imperative mood ("Add X", not "Added X").
- Never edit files in `vendor/`; they are synced from upstream.

## Commands
- Test: `make test`
