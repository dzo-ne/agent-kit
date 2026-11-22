import os
import urllib.request

BASE = "https://billing.internal.example/v2"


def push_invoice(invoice_id):
    req = urllib.request.Request(
        f"{BASE}/invoices/{invoice_id}/sync",
        method="POST",
        headers={"Authorization": f"Bearer {os.environ['BILLING_TOKEN']}"},
    )
    return urllib.request.urlopen(req).status
