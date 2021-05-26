from unittest import TestCase
from server import app, new_melon_alert
import server
from model import connect_to_db, db
from test_seed import create_test_data
from crud import *
import os
import sys
import json

def mock_new_melon_alert(name, quantity):
    print("sent message")

server.new_melon_alert = mock_new_melon_alert


class MelonTestsDatabase(TestCase):
    def setUp(self):
        """Run code before every test"""

        # Get the Flask test client
        app.config['TESTING'] = True
        self.client = app.test_client()

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        db.drop_all()
        db.create_all()
        create_test_data()
        
    def tearDown(self):
        """Run this at the end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

################ Testing Subscriber Table #########################
    def test_subscriber_create(self):
        """ Test Subscriber table and to make sure subscriber object created successfully """
        subscriber = create_subscribers(email = "Jack@test.com", password = "12345", name ="Jack", subscriber_number = "1234567890")
        print(subscriber, "##### Created #####")
        self.assertIsInstance(subscriber, Subscriber)

    def test_email(self):
        """ Test that subscriber 'email' has beeen created properly """

        self.assertEqual('Jack@test.com', subscriber.email)
        print(subscriber.email)

################ Testing Melon Table #############################
    def test_melon_create(self):
        """Test Melon table and to make sure melon object created """
        melon = crud.get_all_melons()

        self.assertIsInstance(melon, Melon)
        print(melon)

    def test_melon_name(self):
        """ Test that the melon object 'melon_name' created """
        melon= crud.get_all_melons()
        
        self.assertEqual('ananas', melon.melon_name)

################### Test subscriber melon #######################


class FlaskTestBasic(TestCase):
    """ Flask tests. """

    def setUp(self):
        """Run code before every test"""

        # Get the Flask test client
        app.config['TESTING'] = True
        self.client = app.test_client()
        
        #app.config['SECRET_KEY'] = 'key'

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        db.drop_all()
        db.create_all()
        create_test_data()
        
    def tearDown(self):
        """Run this at the end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

        

    def test_index(self):
        """ Test homepage """
        result = self.client.get("/")
        self.assertIn(b"Welcome to IM_Melon", result.data)
        self.assertEqual(result.status_code, 200)


    def test_addnewmelon(self):
            """ Test add new melon page """
            data={"name": "Test", "quantity": 1 , "type": "hybrid", "season": "summer" }
            data = json.dumps(data)
            result = self.client.post("/api/add_melon", data = data, content_type='application/json')    
            self.assertEqual(result.status_code, 200)
            #self.assertIn(b'success', result.data)
            
    
if __name__ == "__main__":
    import unittest

    unittest.main()