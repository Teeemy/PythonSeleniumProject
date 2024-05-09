# Add and search Employee in OpenHR
# Login with the Credential
# Add user https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser
# Search User


import time
import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.title("Add and Search Employee in OpenHR")
@allure.description("TC#1 Verify Login with credential and add a user.")
def test_opencart():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")

    time.sleep(5)

    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys("Admin")

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys("admin123")

    login_button_element = driver.find_element(By.XPATH, "//button[@type='submit'] ")
    login_button_element.click()
