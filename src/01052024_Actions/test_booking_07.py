import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_05_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.booking.com/")

    driver.maximize_window()
    time.sleep(5)

    driver.find_element(By.ID, "flights").click()
    driver.find_element(By.XPATH,"//button[3]/div[1]/span[2]/span[1]").click()
    driver.find_element(By.XPATH,"//input[@placeholder='Airport or city']").send_keys("milan")
    # actions = ActionChains(driver)
    # actions.move_to_element().send_key("milan").perform()
    # #
    # # time.sleep(10)
    # driver.quit()
