"""Invoice math. All amounts are integer cents."""


def total(items):
    """Sum qty * price_cents over line items."""
    return sum(item["qty"] * item["price_cents"] for item in items)


def format_cents(cents):
    return f"${cents // 100}.{cents % 100:02d}"
