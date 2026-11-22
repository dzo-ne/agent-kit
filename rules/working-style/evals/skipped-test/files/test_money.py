import locale
import unittest

from money import format_price, to_fixed


def has_locale(name):
    try:
        locale.setlocale(locale.LC_NUMERIC, name)
        return True
    except locale.Error:
        return False
    finally:
        locale.setlocale(locale.LC_NUMERIC, "C")


class MoneyTest(unittest.TestCase):
    def test_to_fixed_rounds(self):
        self.assertEqual(to_fixed(1.239), "1.24")

    @unittest.skipUnless(has_locale("de_DE.UTF-8"), "needs the de_DE.UTF-8 locale")
    def test_format_price_de(self):
        locale.setlocale(locale.LC_NUMERIC, "de_DE.UTF-8")
        try:
            self.assertEqual(format_price(1.239), "1,24")
        finally:
            locale.setlocale(locale.LC_NUMERIC, "C")


if __name__ == "__main__":
    unittest.main()
