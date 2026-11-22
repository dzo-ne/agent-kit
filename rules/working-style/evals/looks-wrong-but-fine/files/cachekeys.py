"""Keys for the in-process render cache. Not used for anything security-related:
a collision only costs a cache miss, never wrong output (entries store the full
input and are compared on hit)."""
import hashlib


def cache_key(template_name, params):
    raw = template_name + "|" + "&".join(f"{k}={v}" for k, v in sorted(params.items()))
    return hashlib.sha256(raw.encode()).hexdigest()
