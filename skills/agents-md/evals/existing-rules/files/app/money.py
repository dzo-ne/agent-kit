"""Amounts are integer cents everywhere; convert only at the API boundary."""


def to_cents(amount: str) -> int:
    whole, _, frac = amount.partition(".")
    return int(whole) * 100 + int((frac + "00")[:2])
