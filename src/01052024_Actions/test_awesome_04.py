import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_04_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    # to make sure the first letter is  capital and others are small letters

    actions = ActionChains(driver=driver)  # obj creation then perform key actions
    (actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "a")
     .key_up(Keys.SHIFT)
     .send_keys("s")
     .key_up(Keys.SHIFT)
     .key_down("h")
     .key_up(Keys.SHIFT)
     .send_keys("a")
     .key_up(Keys.SHIFT)
     .send_keys("b")
     .key_up(Keys.SHIFT)
     .send_keys("i").perform())
    print(first_name.text)
    last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
    # last_name.send_keys("")

    time.sleep(10)
    driver.quit()
