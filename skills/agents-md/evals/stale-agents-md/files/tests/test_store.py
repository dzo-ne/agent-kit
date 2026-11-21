import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from feedsync.store import save


class StoreTest(unittest.TestCase):
    def test_save(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "items.json"
            save([1], p)
            self.assertEqual(p.read_text(), "[1]")


if __name__ == "__main__":
    unittest.main()
