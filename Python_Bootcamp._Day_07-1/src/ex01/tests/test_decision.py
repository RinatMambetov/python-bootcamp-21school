import pytest
import sys
import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '../src')
sys.path.append(mymodule_dir)

from decision import make_decision


def test_make_decision_human():
    averages = (14, 80, 3.5, 4)
    assert make_decision(averages) == "human"


def test_make_decision_replicant():
    averages = (10, 110, 2.5, 3)
    assert make_decision(averages) == "replicant"


def test_make_decision_edge_case():
    averages = (12, 60, 3, 4)
    assert make_decision(averages) == "human"


def test_make_decision_invalid_input():
    averages = (15, 80, 2, "invalid")
    with pytest.raises(TypeError):
        make_decision(averages)


if __name__ == '__main__':
    test_make_decision_human()
    test_make_decision_replicant()
    test_make_decision_edge_case()
    test_make_decision_invalid_input()
