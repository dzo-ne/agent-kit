import unittest

from parse import ParseLine


class ParseTest(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(ParseLine("a,b,c"), ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
