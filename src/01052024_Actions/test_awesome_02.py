import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_02_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    # to make sure the letters are in capitals,
    # we press the shift down and type,but we can do this
    # automatically with selenium actions
    # first thing is to create an obj i.e.
    actions = ActionChains(driver=driver)  # obj creation then perform key actions
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "ashabi").key_up(Keys.SHIFT).perform()

    last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
    # last_name.send_keys("OLAWALE")

    actions = ActionChains(driver=driver)  # obj creation then perform key actions
    actions.key_down(Keys.SHIFT).send_keys_to_element(last_name, "olawale").key_down(Keys.SHIFT).perform()

    time.sleep(10)
    driver.quit()
