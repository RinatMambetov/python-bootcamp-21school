import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '../src')
sys.path.append(mymodule_dir)

from calculation import calculate_averages


def test_calculate_averages():
    """Tests the calculate_averages function with a list of variables and expected output."""

    variables = [(10, 60, 3, 4), (12, 65, 4, 5), (8, 70, 2, 3)]
    expected_output = (10.0, 65.0, 3.0, 4.0)
    assert calculate_averages(variables) == expected_output


def test_calculate_averages_empty_list():
    """Tests the calculate_averages function with an empty list of variables and expected output."""

    variables = []
    expected_output = (0, 0, 0, 0)
    assert calculate_averages(variables) == expected_output


def test_calculate_averages_single_variable():
    """Tests the calculate_averages function with a single variable and expected output."""

    variables = [(10, 60, 3, 4)]
    expected_output = (10, 60, 3, 4)
    assert calculate_averages(variables) == expected_output


if __name__ == '__main__':
    test_calculate_averages()
    test_calculate_averages_empty_list()
    test_calculate_averages_single_variable()
