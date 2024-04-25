# open url https://katalon-demo-cura.herokuapp.com/
# click on make appointment button
# verify url changes
# uses time.sleep(3)
# enter username and password
# verify current url
# verify make appointment text on the webpage

import time
import pytest
import allure
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify that Login is working on Cura website")
@allure.description("TC#1 - Login Scenario")
def test_cura_website():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    time.sleep(3)
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    print(driver.current_url)
    make_appointment_element.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Login Screenshot", attachment_type=AttachmentType.PNG)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    print(driver.current_url)
    time.sleep(4)

    username_element = driver.find_element(By.NAME,"username")
    username_element.send_keys("John Doe")
    time.sleep(2)
    password_element = driver.find_element(By.ID,"txt-password")
    password_element.send_keys("ThisIsNotAPassword")
    time.sleep(2)
    login_button_element = driver.find_element(By.ID,"btn-login")
    login_button_element.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Make Appointment Screenshot",attachment_type=AttachmentType.PNG)
    verify_element = driver.find_element(By.XPATH,"//div/h2")
    assert verify_element.text == "Make Appointment"
    select_facility_element= driver.find_element(By.ID,"facility")
    select_facility_element.is_selected()




