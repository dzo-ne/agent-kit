import unittest

from netutil import parse_host, parse_port


class NetutilTest(unittest.TestCase):
    def test_host(self):
        self.assertEqual(parse_host(" Example.COM "), "example.com")

    def test_port(self):
        self.assertEqual(parse_port("8080"), 8080)


if __name__ == "__main__":
    unittest.main()
