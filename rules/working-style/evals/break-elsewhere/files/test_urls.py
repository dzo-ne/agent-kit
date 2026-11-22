import unittest

from urls import post_path


class UrlsTest(unittest.TestCase):
    def test_post_path(self):
        self.assertEqual(post_path("Hello World"), "/posts/Hello-World")


if __name__ == "__main__":
    unittest.main()
