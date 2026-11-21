# Notes for Claude

- Run `make lint` before every commit.
- Never edit a migration in db/migrations that has already been applied; add a new numbered file instead.
- Money is stored as integer cents, never floats.
