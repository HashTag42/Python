import unittest
import urllib.request


url = "https://google.com"
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)


class Internet_Tests(unittest.TestCase):
    def test_urlopen(self):
        with urllib.request.urlopen(req) as response:
            self.assertEqual(response.getcode(), 200)
