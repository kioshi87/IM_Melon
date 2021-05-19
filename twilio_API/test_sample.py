from unittest import TestCase
from server import app
#from model import connect_to_db, db
from flask import session

# import test_seed
import server

class FlaskTestBasic(TestCase):
    """ Flask tests. """

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        
        #connect_to_db(app, "postgresql:///testdb")
        #db.create_all()
        #test_seed.create_example_data()

    def test_addnewmelon(self):
            """ Test signup page """
            result = self.client.post("/add_new_melon",
                                    data={"name": "Test", "qty": "2", "mel_type": "hybrid", "mel_season": "mel_season" },
                                    follow_redirects=True)
            self.assertEqual(result.status_code, 200)
            #self.assertIn(b"Yummy Recipe", result.data)
    
if __name__ == "__main__":
    import unittest

    unittest.main()