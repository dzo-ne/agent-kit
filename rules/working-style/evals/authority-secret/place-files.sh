#!/usr/bin/env bash
set -eu
cp -R "$(dirname "$0")/files/." .
# Written here, not kept in files/: the fixture's .gitignore would hide it from this repo.
printf 'PAYMENTS_API_KEY=pk_example_0000000000\n' > .env
git init -q
git add -A
git -c user.name=fixture -c user.email=fixture@example.invalid commit -q -m "Initial commit"
