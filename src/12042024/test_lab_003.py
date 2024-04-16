# using selenium 4 without setting driver_path
import time

from selenium import webdriver
# webdriver is directly used in selenium 4 unlike 3 that you need to set driver path

def test_open_vwologin():
    driver = webdriver.Chrome()# post request
    driver.get("https://app.vwo.com") # Get request #the page automatically close back. this is done by python execusion because there is no next command
    time.sleep(5)