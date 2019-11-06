from selenium import webdriver
import unittest

class TestCase():

    def setUp(self):
        super().setUp()

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by XPATH")

if __name__ == '__main__':
    unittest.main(verbosity=2)
    result = unittest.TestResult()