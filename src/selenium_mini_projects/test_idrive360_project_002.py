# Selenium project 2
# open url https://www.idrive360.com/enterprise/login
# Enter the useraname and password
# Verify the trial is finished and
# Verify current  url
# Add a logic to add allure screenshot for the trial end

import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.title("Verify Verify the trial is finished on idrive360 website ")
@allure.description("TC#1 - Simple login Scenario on idrive360 website ")
def test_idrive360_website():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    enter_username = driver.find_element(By.XPATH, "//input[@name='username']")
    enter_username.send_keys("augtest_040823@idrive.com")

    enter_password = driver.find_element(By.XPATH, "//input[@name='password']")
    enter_password.send_keys("123456")

    submit_button = driver.find_element(By.ID, "frm-btn")
    submit_button.click()

    time.sleep(12)

    verify_element = driver.find_element(By.XPATH, "//div/h5")
    assert verify_element.text == "Your free trial has expired"
    print(verify_element.text)
    allure.attach(driver.get_screenshot_as_png(), name="Trial Expired  Screenshot", attachment_type=AttachmentType.PNG)


    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    print(driver.current_url)
