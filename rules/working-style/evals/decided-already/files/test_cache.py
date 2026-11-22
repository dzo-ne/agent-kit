import unittest

import cache


class CacheTest(unittest.TestCase):
    def setUp(self):
        cache.CACHE.clear()

    def test_put_get(self):
        cache.put("a", 1)
        self.assertEqual(cache.get("a"), 1)


if __name__ == "__main__":
    unittest.main()
