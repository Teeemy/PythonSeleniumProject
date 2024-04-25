# Xpath-> is a querry language for selecting nodes from an HTML/XML document
# The core logic of xpath is //tagName[@attribute="Value"]

# //a[@id="btn-make-appointment"] it means find all the anchor tags where id is equal to make appointment.it will
# return a unique element

# xpath logic are
# # //input[@id='login-username']
# # //input[@name='username']
# # //input[@class="text-input W(100%)"] - not recommended
# # //input[@type ="email"] not recommended
# # //input[@data-qa="hocewoqisi"] - custom attribute. user self unique identifier
# All these type of xpath are relative xpath
# we have two types of xpath i.e relative and absolute xpath
# // input is the tagName
# Different types of html tag are -h1,p,input,a,form,img,video
# audio,button,table,ul,li,tr,div,select,span


import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify that Login is working on app_vwo website")
@allure.description("TC#1 - Simple login Scenario")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    make_appointment_btn = driver.find_element(By.XPATH,"//input[@name='username']")
    make_appointment_btn.send_keys("admin")

    # password = driver.find_element(By.XPATH, "txt-password")
    # password.send_keys("ThisIsNotAPassword")

    time.sleep(10)
