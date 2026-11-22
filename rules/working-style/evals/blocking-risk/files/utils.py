import csv


def load_customers(path="data/customers.csv"):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def _legacy_format(name):
    """Unused since the v2 export."""
    return name.upper()
