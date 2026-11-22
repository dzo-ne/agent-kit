import unittest

from cachekeys import cache_key


class CacheKeyTest(unittest.TestCase):
    def test_stable(self):
        self.assertEqual(cache_key("home", {"b": 2, "a": 1}), cache_key("home", {"a": 1, "b": 2}))

    def test_distinct(self):
        self.assertNotEqual(cache_key("home", {"a": 1}), cache_key("home", {"a": 2}))


if __name__ == "__main__":
    unittest.main()
