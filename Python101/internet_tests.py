import unittest
import urllib.request


class Internet_Tests(unittest.TestCase):
    def test_urlopen(self):
        webUrl = urllib.request.urlopen("http://www.google.com")
        self.assertEqual(webUrl.getcode(), 200)
