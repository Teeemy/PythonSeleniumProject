import pytest
import allure
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
import os
import time


# Data Driven Test Cases for Login Page
# scenario is to check invalid login for vwo.com


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({
            "username": username,
            "password": password
        })
    return credentials


file_path_fromos = os.getcwd() + r"\py2xtestdata.xlsx"
print(file_path_fromos)


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(file_path_fromos))
@allure.title("Verify the Invalid login with the Excel Testdata")
@allure.description("TC#1 - 10 invalid logins verification for vwo.com.")
def test_vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    vwo_login(username=username,password=password)


def vwo_login_positive_scenario(username, password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys(username)
    pass_input.send_keys(password)

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    time.sleep(5)

    result = driver.current_url

    print(result)
    if result != "https://app.vwo.com/#/dashboard":
        ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

        wait = WebDriverWait(driver, timeout=60, poll_frequency=1, ignored_exceptions=ignore_list)
        wait.until(  # timeout is in seconds
            EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
        )
        error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
        print(error_msg_element.text)
        assert error_msg_element.text == "Your email, password, IP address or location did not match"

    else:
        wait = WebDriverWait(driver=driver, timeout=15)
        wait.until(

            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), "Dashboard")

        )

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-qa='lufexuloga']")))

        heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']");
        assert heading_element.text == "Mariam Temitope Onibon-oje"

        driver.quit()
