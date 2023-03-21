import unittest


def squeak(func):
    def wrapper(*args, **kwargs):
        print("SQUEAK")
        return func(*args, **kwargs)

    return wrapper


@squeak
def add_ingot(purse):
    new_purse = dict(purse)
    if "gold_ingots" in new_purse:
        new_purse["gold_ingots"] += 1
    else:
        new_purse["gold_ingots"] = 1
    return new_purse


@squeak
def get_ingot(purse):
    new_purse = dict(purse)
    if "gold_ingots" in new_purse and new_purse["gold_ingots"] > 0:
        new_purse["gold_ingots"] -= 1
    return new_purse


@squeak
def empty(purse):
    return {}


class TestPurse(unittest.TestCase):
    def test_add_ingot(self):
        purse = {"gold_ingots": 5}
        expected = {"gold_ingots": 6}
        self.assertEqual(add_ingot(purse), expected)

    def test_get_ingot(self):
        purse = {"gold_ingots": 5}
        expected = {"gold_ingots": 4}
        self.assertEqual(get_ingot(purse), expected)

    def test_empty(self):
        purse = {"gold_ingots": 5, "silver_ingots": 3}
        expected = {}
        self.assertEqual(empty(purse), expected)


if __name__ == '__main__':
    unittest.main()
