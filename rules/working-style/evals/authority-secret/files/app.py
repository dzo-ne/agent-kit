import os


def payments_client():
    key = os.environ["PAYMENTS_API_KEY"]
    return {"key": key}
