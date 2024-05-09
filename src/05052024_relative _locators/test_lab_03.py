import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *


# Exceptions are something that will interrupt your program
# exception in python is handled by try and except
def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    time.sleep(2)
    try:
        driver.find_element(By.NAME, "mariam").send_keys("the testing academy")
    except NoSuchElementException as nse:  # nse is short for NOSUCHELEMENT
        print(f"No Such element found, check locator:  {nse}")

        # the goal is to put an exception when the element is not present.
        # the test will still pass

    time.sleep(10)
    driver.quit()
