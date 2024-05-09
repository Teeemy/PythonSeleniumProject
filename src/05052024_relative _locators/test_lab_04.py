import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *


def test_exception_refresh():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    time.sleep(3)
    try:
        textarea = driver.find_element(By.NAME, "q")
        # textarea
        driver.refresh()
        # once u refresh, all Dom elements changes.so we need to find the elements again
        # DOM elements - refreshed
        # // Refresh will  Navigate to other Page, change in DOM elements (Ajax Calls) - VueJS, AngularJS
        # and this get webdriver confused, and it gives a stale element exception

        # driver.switch_to.alert

        # After refresh, you find the elements again to not give error

        textarea = driver.find_element(By.NAME, "q")
        textarea.send_keys("the testing academy")
        # NoAlertPresentException
    except StaleElementReferenceException as see:
        print(see)

    time.sleep(10)
    driver.quit()
