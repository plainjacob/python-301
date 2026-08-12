# Write a unittest test suite to test the rescrape module

import unittest
import rescrape

class TestRescrape(unittest.TestCase):
  def setUp(self):
    self.url = "https://codingnomads.github.io/recipes/"

  def test_get_page_content(self):
    self.assertEqual(rescrape.get_page_content(self.url).status_code, 200)

if __name__ == "__main__":
  unittest.main()