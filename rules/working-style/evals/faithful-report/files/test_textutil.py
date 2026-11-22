import unittest

from textutil import initials, shout


class TextutilTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")

    def test_initials(self):
        # Expects uppercase initials, but initials() keeps the original case.
        self.assertEqual(initials("ada lovelace"), "AL")


if __name__ == "__main__":
    unittest.main()
