from selenium import webdriver
import os
import tkinter as tk


class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "/Users/atomar/Documents/workspace_personal/libs/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)

        # Get Screen Resolution
        screen = tk.Tk()

        width = screen.winfo_screenwidth()
        height = screen.winfo_screenheight()

        driver.set_window_size(width, height)

        # Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = RunChromeTests()
ff.test()