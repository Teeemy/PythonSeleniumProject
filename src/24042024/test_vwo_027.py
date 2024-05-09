# time.sleep(5) # This is not a selenium wait. it is just python interpreter wait.
# it is the worst type of wait. so the best thing is to use webdriver for wait action
# and not python interpreter
#
# Wait in selenium are
# Implicit Wait-> implicit basically means Internal.implicit wait basically mean webdriver should wait
# for certain duration time when trying to find an element before moving to the next one but the issue with
# implicit wait is,the global settings is applicable to all elements.i.e telling every elements to wait
# if element is not found,
# it throws an exception known as no such element
# Implicit wait is not the best wait method.
# it is usually use when the environment is slow like in QA env not in prod env
import os
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import os


@pytest.mark.smoke
@allure.title("Verify error message is displayed")
@allure.description("TC#1 - Wrong username and password")
def test_vwologin_negative_scenario():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # webdriver wait for all the elements
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    email_input.send_keys("admin123@gmail.com")

    password_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    password_input.send_keys("admin12345")

    submit_button = driver.find_element(By.ID, "js-login-btn")
    submit_button.click()

# Explicit Wait
# Fluent Wait
