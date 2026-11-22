import re


def slug(s):
    """Turn a title into a URL slug."""
    return re.sub(r"\s+", "-", s.strip())
