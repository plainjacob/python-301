# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import math
import unittest

class TestMath(unittest.TestCase):
  def test_e(self):
    self.assertEqual(math.e, 2.718281828459045)

  def test_pi(self):
    self.assertEqual(math.pi, 3.141592653589793)

if __name__ == "__main__":
  unittest.main()