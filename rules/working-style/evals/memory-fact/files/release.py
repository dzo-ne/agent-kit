import json
import urllib.request


def latest_tags(repo):
    """List tags of a GitHub repo. Called once per package during a release."""
    with urllib.request.urlopen(f"https://api.github.com/repos/{repo}/tags") as r:
        return [t["name"] for t in json.load(r)]
