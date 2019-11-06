from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import os

class RunFFTests():

    def test(self):
        # driverLocation = "/Users/atomar/Documents/workspace_personal/libs"
        # os.environ["webdriver.gecko.driver"] = driverLocation
        # Instantiate FF Browser Command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.test()