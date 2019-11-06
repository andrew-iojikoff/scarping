from selenium import webdriver
from selenium.webdriver.common.by import By
from base.guibasetestcase import GUIBaseTestCase
from base.basetestcase import BaseTestCase
import time
import unittest

class TestClass1(BaseTestCase):

    def __init__(self, browser, os):
        self.browser = browser
        self.os = os

    @classmethod
    def setUpClass(self):
        super(TestClass1, self).setUpClass()

    def test_methodA(self):
        loginLink = self.driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = self.driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = self.driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")


    def test_methodB(self):
        time.sleep(3)
        emailField = self.driver.find_element(By.ID, "user_email")
        emailField.clear()
        time.sleep(3)
        emailField.send_keys("test")
        
    @classmethod
    def tearDownClass(self):
        super(TestClass1, self).tearDownClass()


if __name__ == '__main__':
    unittest.main(verbosity=2)