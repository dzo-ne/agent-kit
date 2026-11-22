import unittest

from invoice import format_cents, total


class TotalTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total([{"qty": 3, "price_cents": 199}, {"qty": 1, "price_cents": 5}]), 602)

    def test_format(self):
        self.assertEqual(format_cents(602), "$6.02")


if __name__ == "__main__":
    unittest.main()
