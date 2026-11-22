import urllib.request

TIMEOUT = 10  # seconds per HTTP request


def fetch(url):
    with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
        return r.read()
