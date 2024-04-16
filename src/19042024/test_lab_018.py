import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify that Login is working on Cura website")
@allure.description("TC#1 - Simple login Scenario")
def test_open_cura_website():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    make_appointment_btn.click()

    #driver.attach(driver.get_screenshot_as_png().name="Screenshot")

    print(driver.current_url)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    username = driver.find_element(By.NAME,"username")
    username.send_keys("John Doe")

    password = driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")

    submit_btn = driver.find_element(By.ID,"btn-login")
    submit_btn.click()

   # allure.attach(driver.get_screenshot_as_png(), name="Login Screenshot", attachment_type=AttachmentType.PNG)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(5)