from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()# post request
    driver.get("https://app.vwo.com") # Get request #the page automatically close back. this is done by python execusion because there is no next command
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(5)