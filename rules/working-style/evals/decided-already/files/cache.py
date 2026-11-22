"""Process-wide memo cache."""

CACHE = {}


def get(key, default=None):
    return CACHE.get(key, default)


def put(key, value):
    CACHE[key] = value
