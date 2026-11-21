def _zero_pad(n):
    return f"{n:02d}"


def parse_date(s):
    """Parse 'YYYY-MM-DD' into (year, month, day)."""
    y, m, d = s.split("-")
    return int(y), int(m) - 1, int(d)


def format_date(y, m, d):
    return f"{y}-{_zero_pad(m)}-{_zero_pad(d)}"
