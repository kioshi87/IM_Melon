import os
import unittest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  
import time
from server import app
import server
from model import connect_to_db, db
from test_seed import create_test_data
import crud 


# def mock_new_melon_alert(name, quantity):
#     print("sent message")

# server.new_melon_alert = mock_new_melon_alert


chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")   

class TestMelonAlert(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        
        #app.config['SECRET_KEY'] = 'key'

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        db.drop_all()
        db.create_all()
        create_test_data()

        self.browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), 
                                        options=chrome_options)


    def tearDown(self):

        self.browser.quit()
        db.session.remove()
        db.drop_all()
        db.engine.dispose()


    def test_title(self):
        self.browser.get('http://localhost:5000/')
        self.assertTrue( 'IM_Melon' in self.browser.title )
#########################################################################
   
    def test_subscribe(self):
        self.browser.get('http://localhost:5000/subscribe')
        time.sleep(1)
        name = self.browser.find_element_by_name('name')
        name.send_keys("Test1")
        password = self.browser.find_element_by_name('password')
        password.send_keys("12345")
        email = self.browser.find_element_by_name('email')
        email.send_keys("Test1@test.com")
        phone = self.browser.find_element_by_name('phone')
        # phone.send_keys("6146029800")
        phone.send_keys("8172628759")

        btn = self.browser.find_element_by_xpath("//input[@type='submit']")
        
        btn.click()
        print(btn.text)

        time.sleep(2)
        alert = self.browser.switch_to.alert
        self.assertEqual(alert.text, "success")
        alert.accept()
        print("OK button on add subscriber")

#################################################################################

    def test_addmelon(self):
        crud.create_subscribers("8172628759", "Test", "Test@test.com", "12345")
        self.browser.get('http://localhost:5000/admin')
        time.sleep(1)
        name = self.browser.find_element_by_name('melonName')
        name.send_keys("TestMelon5")
        qty = self.browser.find_element_by_name('melonQty')
        qty.send_keys("1")
        melon_type = self.browser.find_element_by_name('melonType')
        melon_type.send_keys("Hybrid")
        season = self.browser.find_element_by_name('melonSeason')
        season.send_keys("summer")

        btn = self.browser.find_element_by_xpath("//input[@type='submit']")
        
        btn.click()
        print(btn.text)

        time.sleep(2)
        alert = self.browser.switch_to.alert
        self.assertEqual(alert.text, "success")
        alert.accept()
        print("OK button on alert message")

if __name__ == "__main__":
    unittest.main()