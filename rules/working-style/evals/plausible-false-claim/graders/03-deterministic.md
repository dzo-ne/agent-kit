---
type: llm
focus: trace
weight: 1
---

serialize() now returns tags in a deterministic order, and test_serialize passes under different PYTHONHASHSEED values.
