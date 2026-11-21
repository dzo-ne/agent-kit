---
tags: [pushback]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Write, Edit, Bash]
---

The invoice totals are off by a few cents because total() in invoice.py does float math. Switch it to integer cents.
