import unittest

from dates import format_date, parse_date


class DatesTest(unittest.TestCase):
    def test_parse_date(self):
        self.assertEqual(parse_date("2024-03-05"), (2024, 3, 5))

    def test_format_date(self):
        self.assertEqual(format_date(2024, 3, 5), "2024-03-05")


if __name__ == "__main__":
    unittest.main()
