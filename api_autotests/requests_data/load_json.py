import json


def load_json(filepath):
    with open(filepath) as f:
        return json.load(f)
