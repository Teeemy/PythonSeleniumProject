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
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # click and hold -> means to click and hold without releasing

    driver.find_element(By.ID, "click").click()
    # a_tag = driver.find_element(By.ID,"click")
    # actions = ActionChains(driver)
    # actions.click_and_hold(a_tag)
    time.sleep(2)

    # action builder means to use mouse to go back
    actions = ActionBuilder(driver)
    actions.pointer_action.pointer_up(MouseButton.BACK)
    actions.perform()

    time.sleep(5)
    driver.quit()
