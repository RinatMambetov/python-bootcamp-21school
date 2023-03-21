import json
import os


def read_json(file_path):
    """
    Function:
    read_json: Reads data from a JSON file and returns the resulting object.

    Args:
    file_path: A string representing the file path of the JSON file to read.

    Returns:
    A Python object representing the data stored in the JSON file.

    If the JSON file is empty, an error message will be printed and None will be returned.
    """

    if os.stat(file_path).st_size == 0:
        print("Error: Json file is empty")
        return None
    with open(file_path) as f:
        data = json.load(f)
    return data
