# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest
import mymath

class TestMyMath(unittest.TestCase):
  def test_correct(self):
    self.assertEqual(mymath.subtract_divide(10, 4, 2), 5)

  def test_error(self):
    with self.assertRaises(mymath.CustomZeroDivsionError):
      mymath.subtract_divide(10, 2, 2)

if __name__ == "__main__":
  unittest.main()