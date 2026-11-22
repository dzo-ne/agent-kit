import csv
from pathlib import Path

RATES_FILE = Path(__file__).parent / "data" / "rates.csv"


def load_rates():
    """Exchange rates exported nightly from the finance system (not in git)."""
    with open(RATES_FILE, newline="") as f:
        return {row["currency"]: float(row["rate"]) for row in csv.DictReader(f)}


def convert(amount, currency):
    return round(amount * load_rates()[currency], 2)
