import unittest

from text import slug


class SlugTest(unittest.TestCase):
    def test_spaces(self):
        self.assertEqual(slug("  a  b "), "a-b")


if __name__ == "__main__":
    unittest.main()
