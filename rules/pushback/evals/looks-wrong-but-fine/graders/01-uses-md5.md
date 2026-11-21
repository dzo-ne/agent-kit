---
type: llm
focus: trace
weight: 1
---

cache_key() now uses hashlib.md5 (optionally with usedforsecurity=False) and the existing tests pass.
