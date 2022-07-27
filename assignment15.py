import unittest
import time
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

class Assignment15(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def test_405(self): 
    
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/login")
        time.sleep(3)

        response_data = browser.find_element(By.TAG_NAME,"h1").text
        response_message = browser.find_element(By.TAG_NAME,"p").text

        self.assertEqual(response_data, 'Method Not Allowed')
        self.assertEqual(response_message, 'The method is not allowed for the requested URL.')  
   
    def test_404(self): 
    
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/abc")
        time.sleep(3)

        response_data = browser.find_element(By.TAG_NAME,"h1").text
        response_message = browser.find_element(By.TAG_NAME,"p").text

        self.assertEqual(response_data, 'Not Found')
        self.assertEqual(response_message, 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.')        
        
    def test_a_success_login(self): 
    
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_a_failed_login_with_wrong_email_and_wrong_password(self): 

        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("e0337884@u.nus.edu")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("123456")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_a_failed_login_with_right_email_and_wrong_password(self): 

        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("098764")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_saucedemo_locked_out_user(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com")
        time.sleep(5)
        browser.find_element(By.NAME,"user-name").send_keys("locked_out_user")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        response_message = browser.find_element(By.CLASS_NAME, "error-message-container").text

        self.assertEqual(response_message, 'Epic sadface: Sorry, this user has been locked out.')   

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()