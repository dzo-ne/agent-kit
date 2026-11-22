import re


def slugify(n):
    """Lowercase, replace runs of non-alphanumerics with '-', trim dashes."""
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")
