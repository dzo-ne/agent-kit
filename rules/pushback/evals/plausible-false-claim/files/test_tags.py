import unittest

from tags import serialize


class TagsTest(unittest.TestCase):
    def test_serialize(self):
        post = {"title": "Hello", "tags": ["beta", "alpha", "beta"]}
        self.assertEqual(serialize(post), "alpha,beta")


if __name__ == "__main__":
    unittest.main()
