import unittest

from ex00 import add_ingot
from ex00 import empty


def split_booty(*purses):
    total_ingots = sum(purse.get("gold_ingots", 0) for purse in purses)
    num_ingots_per_purse = total_ingots // 3
    num_purses_with_extra = total_ingots % 3

    booty = [empty({}) for _ in range(3)]
    for i in range(num_ingots_per_purse * 3):
        purse_index = i // num_ingots_per_purse
        booty[purse_index] = add_ingot(booty[purse_index])

    for i in range(num_purses_with_extra):
        booty[i] = add_ingot(booty[i])

    return booty


class TestSplitBooty(unittest.TestCase):

    def test_split_booty_equal_purses(self):
        purses = [{"gold_ingots": 3}]
        expected_booty = [{"gold_ingots": 3}, {"gold_ingots": 3}, {"gold_ingots": 3}]
        self.assertEqual(split_booty(*purses), expected_booty)

    # def test_split_booty_extra_ingots(self):
    #     purses = [{"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10}]
    #     expected_booty = [{"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1}]
    #     self.assertEqual(split_booty(*purses), expected_booty)
    #
    # def test_split_booty_empty_purses(self):
    #     purses = [{}, {}, {}]
    #     expected_booty = [{}, {}, {}]
    #     self.assertEqual(split_booty(*purses), expected_booty)
    #
    # def test_split_booty_no_gold_ingots(self):
    #     purses = [{"silver_ingots": 3}, {"copper_ingots": 3}, {"platinum_ingots": 3}]
    #     expected_booty = [{}, {}, {}]
    #     self.assertEqual(split_booty(*purses), expected_booty)


if __name__ == '__main__':
    unittest.main()
