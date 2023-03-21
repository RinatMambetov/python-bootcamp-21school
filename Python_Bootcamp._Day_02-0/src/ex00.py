import unittest


class Key:
    def __init__(self, passphrase):
        self.passphrase = passphrase

    def __len__(self):
        return 1337

    def __getitem__(self, index):
        if index == 404:
            return 3

    def __str__(self):
        return "GeneralTsoKeycard"

    def __gt__(self, other):
        if other == 9000:
            return True


class TestKey(unittest.TestCase):
    def setUp(self):
        self.key = Key("zax2rulez")

    def test_len(self):
        self.assertEqual(len(self.key), 1337)

    def test_getitem(self):
        self.assertEqual(self.key[404], 3)

    def test_str(self):
        self.assertEqual(str(self.key), "GeneralTsoKeycard")

    def test_gt(self):
        self.assertTrue(self.key > 9000)


if __name__ == '__main__':
    unittest.main()
