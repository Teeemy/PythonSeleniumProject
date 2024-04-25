#project 3
# Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
# Enter all the fields excepts the username
# Verify that the error message comes when you click on the submit button.

import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
@pytest.mark.smoke
@allure.title("Verify that the error message comes when you click on the submit button")
@allure.description("TC#1 -enter password and leave username field empty")
def test_open_website():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")

    driver.switch_to.frame(driver.find_element(By.ID, "result"))

    email_address = driver.find_element(By.XPATH,"//input[@id='email']")
    email_address.send_keys("tidibot344@huizk.com")

    password_element = driver.find_element(By.XPATH, "//input[@id='password']")
    password_element.send_keys("1234567")

    password_element2 = driver.find_element(By.XPATH, "//input[@id='password2']")
    password_element2.send_keys("1234567")

    submit_element = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_element.click()

    allure.attach(driver.get_screenshot_as_png(), name="empty-username", attachment_type=AttachmentType.PNG)
    error_message = driver.find_element(By.XPATH, "//input[@id='username']//following::small").text
    print(error_message)
    time.sleep(4)
    assert (error_message == "Username must be at least 3 characters")

    driver.quit()

