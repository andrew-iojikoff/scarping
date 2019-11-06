from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.select import Select

class AirbnbExercise1():

    def test(self):
        baseUrl = "https://www.airbnb.com/"
        #driver = webdriver.Firefox()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # This element has changed on Airbnb website after the lecture was made
        searchBox = driver.find_element(By.ID, "search-location")
        searchBox.send_keys("Hawaii")

        checkIn = driver.find_element(By.ID, "startDate")
        checkIn.send_keys("12/20/2016")

        checkOut = driver.find_element(By.ID, "endDate")
        checkOut.send_keys("12/31/2016")

        # This element has changed on Airbnb website after the lecture was made
        dropdownElement = driver.find_element(By.XPATH,
                                              "//button[@class='GuestPickerTrigger__button']")
        #sel = Select(dropdownElement)
        #sel.select_by_visible_text("2 Guests")
        # It is updated to <button> tag
        # We can only use Select Class with <select> tag
        dropdownElement.click()
        adultPlusButton = driver.find_element(By.XPATH,
                                              "//button[contains(@aria-label,'1 adult (+)') or contains(@aria-label,'Increment number of adults')]")
        adultPlusButton.click()
        # You might have issues because of slow connection that you might not even notice
        # Try to run files multiple times

        time.sleep(2)

        # This element has changed on Airbnb website after the lecture was made
        searchButton = driver.find_element(By.XPATH,
                                           "//span[contains(@class,'SearchForm__submit-text')]//parent::div")
        searchButton.click()

ff = AirbnbExercise1()
ff.test()