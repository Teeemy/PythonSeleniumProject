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

    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("admin")

    email_address = driver.find_element(By.ID,"email")
    email_address.send_keys("tidibot344@huizk.com")

    time.sleep(4)