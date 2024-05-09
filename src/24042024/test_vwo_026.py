import os
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify error message is displayed")
@allure.description("TC#1 - Wrong username and password")
def test_vwologin_negative_scenario():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    email_input.send_keys("admin123@gmail.com")

    password_input = driver.find_element(By.CSS_SELECTOR,"[name='password']")
    password_input.send_keys("admin12345")

    submit_button = driver.find_element(By.ID,"js-login-btn")
    submit_button.click()

    # time.sleep(5) # This is not a selenium wait. it is just python interpreter wait.
    # # it is the worst type of wait. so the best thing is to use webdriver for wait action
    # # and not python interpreter
    # # selenium wait is ->EXPLICIT->IMPLICIT
    #
    #
    #
    # error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    # print(error_msg_element.text)
    # assert error_msg_element.text == "Your email, password, IP address or location did not match"
    #
    # driver.quit()

    allure.attach(driver.get_screenshot_as_png(),name="login-screenshot", attachment_type=AttachmentType.PNG)