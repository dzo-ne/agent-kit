import unittest

from pricing import discount


class DiscountTest(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(discount(200, 25), 150)


if __name__ == "__main__":
    unittest.main()
