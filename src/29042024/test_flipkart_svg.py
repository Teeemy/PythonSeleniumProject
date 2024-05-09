import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.title("Search for an item on flipkart")
@allure.description("TC#1 Verify Login with credential and add a user.")
def test_flipkart():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    search_box = driver.find_element(By.XPATH,"//input[@name='q']")
    search_box.send_keys("AC")
    time.sleep(5)

    svg_list = driver.find_elements(By.XPATH, "//*[name()='svg']")
    svg_list[0].click()

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="flipkart-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()