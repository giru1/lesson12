import json


def read_file(file):
    with open(file, encoding="utf-8") as f:
        result = json.load(f)
    return result
