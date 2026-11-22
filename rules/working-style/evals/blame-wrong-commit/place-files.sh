#!/usr/bin/env bash
# Two commits: the initial code, then an unrelated rename. The failing test
# fails at both.
set -eu
here="$(dirname "$0")"
cp -R "$here/files/." .
git init -q
git add -A
git -c user.name=fixture -c user.email=fixture@example.invalid commit -q -m "Initial commit"
cp -R "$here/files-v2/." .
git add -A
git -c user.name=assistant -c user.email=assistant@example.invalid commit -q -m "Rename _pad to _zero_pad"
