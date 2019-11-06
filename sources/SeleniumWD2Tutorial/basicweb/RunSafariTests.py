from selenium import webdriver
import os

class RunSafariTests():
    # https://github.com/SeleniumHQ/selenium/wiki/SafariDriver
    # http://selenium-release.storage.googleapis.com/index.html

    def test(self):
        serverLocation = "/Users/atomar/Documents/workspace_personal/libs/selenium-server-standalone-3.0.1.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation
        # Instantiate Safari Browser Command
        driver = webdriver.Safari(quiet=True)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()

safari = RunSafariTests()
safari.test()