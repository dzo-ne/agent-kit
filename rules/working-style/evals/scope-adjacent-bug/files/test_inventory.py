import unittest

import inventory


class InventoryTest(unittest.TestCase):
    def setUp(self):
        inventory.STOCK.clear()

    def test_add(self):
        inventory.add_item("apple", 3)
        self.assertEqual(inventory.STOCK["apple"], 3)


if __name__ == "__main__":
    unittest.main()
