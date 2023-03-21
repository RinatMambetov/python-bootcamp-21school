import json
import os


def read_json(file_path):
    if os.stat(file_path).st_size == 0:
        print("Error: Json file is empty")
        return None
    with open(file_path) as f:
        data = json.load(f)
    return data
