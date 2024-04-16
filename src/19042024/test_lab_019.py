# Xpath-> is a querry language for selecting nodes from an HTML/XML document
# The core logic of xpath is //tagName[@attribute="Value"]

# //a[@id="btn-make-appointment"] it means find all the anchor tags where id is equal to make appointment.it will
# return a unique element

# xpath format are
# # //input[@id='login-username']
# # //input[@name='username']
# # //input[@class="text-input W(800%)"] - not recommended
# # //input[@type ="email"] not recommended
# # //input[@data-qa="hocewoqisi"] - custom xpath


import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify that Login is working on app_vwo website")
@allure.description("TC#1 - Simple login Scenario")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("admin")

    password = driver.find_element(By.XPATH, "txt-password")
    password.send_keys("ThisIsNotAPassword")

    time.sleep(10)
