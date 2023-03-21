import json
import pytest
import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '../src')
sys.path.append(mymodule_dir)

from json_reader import read_json


def test_read_json():
    """Tests the read_json function with different scenarios."""

    # Test reading a valid JSON file
    expected_data = {'key': 'value'}
    with open('test_data.json', 'w') as f:
        json.dump(expected_data, f)
    assert read_json('test_data.json') == expected_data

    # Test reading an invalid JSON file
    with open('test_data.json', 'w') as f:
        f.write('invalid json')
    with pytest.raises(json.JSONDecodeError):
        read_json('test_data.json')

    # Test reading a non-existent file
    with pytest.raises(FileNotFoundError):
        read_json('nonexistent_file.json')


if __name__ == '__main__':
    test_read_json()
