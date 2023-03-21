def add_ingot(purse):
    new_purse = dict(purse)
    if "gold_ingots" in new_purse:
        new_purse["gold_ingots"] += 1
    else:
        new_purse["gold_ingots"] = 1
    return new_purse


def get_ingot(purse):
    new_purse = dict(purse)
    if "gold_ingots" in new_purse and new_purse["gold_ingots"] > 0:
        new_purse["gold_ingots"] -= 1
    return new_purse


def empty(purse):
    return {}


if __name__ == '__main__':
    def test_add_ingot():
        purse = {}
        expected = {"gold_ingots": 1}
        assert add_ingot(purse) == expected

        purse = {"gold_ingots": 2}
        expected = {"gold_ingots": 3}
        assert add_ingot(purse) == expected


    def test_get_ingot():
        purse = {}
        expected = {}
        assert get_ingot(purse) == expected

        purse = {"gold_ingots": 2}
        expected = {"gold_ingots": 1}
        assert get_ingot(purse) == expected

        purse = {"gold_ingots": 0}
        expected = {"gold_ingots": 0}
        assert get_ingot(purse) == expected


    def test_empty():
        purse = {}
        expected = {}
        assert empty(purse) == expected

        purse = {"gold_ingots": 2, "silver_ingots": 3}
        expected = {}
        assert empty(purse) == expected


    def test_russian_doll():
        purse = {}
        expected = {"gold_ingots": 1}
        assert add_ingot(get_ingot(add_ingot(empty(purse)))) == expected


    test_add_ingot()
    test_get_ingot()
    test_empty()
    test_russian_doll()
