import unittest

from shapes import circle_area, rect_area, triangle_area


class ShapesTest(unittest.TestCase):
    def test_areas(self):
        self.assertEqual(rect_area(2, 3), 6)
        self.assertEqual(triangle_area(4, 3), 6)
        self.assertAlmostEqual(circle_area(1), 3.14159, places=4)


if __name__ == "__main__":
    unittest.main()
