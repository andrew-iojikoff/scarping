from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class RunFFTests():

    def test(self):
        # Instantiate FF Browser Command
        binary = FirefoxBinary("location")
        driver = webdriver.Firefox(firefox_binary=binary)
        #driver = webdriver.Firefox()

        # Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.test()