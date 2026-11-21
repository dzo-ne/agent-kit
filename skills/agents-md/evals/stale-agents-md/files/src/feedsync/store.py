import json
import pathlib


def save(items, path="items.json"):
    pathlib.Path(path).write_text(json.dumps(items))
