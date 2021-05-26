import unittest
from server import app
from model import db

class simpleTest(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn(b"IM_Melon", result.data)
    
if __name__ == "__main__":
    unittest.main()