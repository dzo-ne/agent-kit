import urllib.request


def fetch(url, timeout=10):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.read()
