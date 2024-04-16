from selenium import webdriver
import time
#import pytest
import logging


# @pytest.mark.smoke
def test_open_vwologin():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()# post request
    driver.get("https://app.vwo.com") # Get request #the page automatically close back. this is done by python execusion because there is no next command
    driver.maximize_window()
    print(driver.title)
    LOGGER.info(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(5)