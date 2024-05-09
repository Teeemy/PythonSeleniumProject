# Relative locators supports above,below,leftof,rightof,near.
# it simply finds locators of an element within the sal]me elements
# it is not mostly  use

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_practice_relative_locators():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    # Xpath Axes -> are Relatives or Siblings by using that mechanism.
    # Following sib, parent, child.

    driver.maximize_window()
    driver.find_element(
        locate_with(By.ID, "exp-3").to_right_of({By.XPATH: "//span[text()='Years of Experience']"})).click()

    time.sleep(10)
    driver.quit()
