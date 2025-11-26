import unittest
import urllib.request


url = "https://example.com"


class Internet_Tests(unittest.TestCase):
    def test_urlopen(self):
        with urllib.request.urlopen(url) as response:
            self.assertEqual(response.getcode(), 200)
