import locale


def to_fixed(x, places=2):
    """Format x with `places` decimals, rounding half up."""
    scale = 10 ** places
    return f"{int(x * scale) / scale:.{places}f}"


def format_price(x):
    """Locale-aware price, e.g. '1,24' under de_DE."""
    return locale.format_string("%.2f", float(to_fixed(x)))
