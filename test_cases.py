import unittest
from main import sort

class TestPackageSorter(unittest.TestCase):
  def test_sort_standard(self):
    self.assertEqual(sort(10, 10, 10, 10), "STANDARD")

  def test_sort_special(self):
    # bulky because of width
    self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")
    # bulky because of height
    self.assertEqual(sort(10, 150, 10, 10), "SPECIAL")
    # bulky because of length
    self.assertEqual(sort(10, 10, 150, 10), "SPECIAL")
    # bulky because of volume
    self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    # heavy
    self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

  def test_sort_rejected(self):
    self.assertEqual(sort(150, 10, 10, 20), "REJECTED")

if __name__ == '__main__':
  unittest.main()
