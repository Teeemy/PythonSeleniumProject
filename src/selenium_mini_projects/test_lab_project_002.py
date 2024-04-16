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


@pytest.mark.smoke
@allure.title("Verify Verify the trial is finished on idrive360 website ")
@allure.description("TC#1 - Simple login Scenario on idrive360 website ")
def test_idrive360_website():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    make_appointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")