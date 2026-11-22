import unittest

from rates import convert, load_rates


class RatesTest(unittest.TestCase):
    def test_convert_uses_current_rate(self):
        rate = load_rates()["EUR"]
        self.assertEqual(convert(100, "EUR"), round(100 * rate, 2))


if __name__ == "__main__":
    unittest.main()
