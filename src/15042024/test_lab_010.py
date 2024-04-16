from selenium import webdriver
import time
import pytest


def test_open_vwologin():
    driver = webdriver.Chrome()  # post request. here session is created.session is a unique 16digit numbers
    ## the moment we type webdriver .chrome,a fresh copy of browser is created,in
    # that browser, url and new tab can be open which is diff from normal bro

    driver.get("https://app.vwo.com")
    print(driver.title)
    print(driver.session_id)
    driver.maximize_window()
    assert driver.title == "Login - VWO"

    driver.close()

    # driver.close()-> it will only close current window or tab
    # session_id is not null i.e invalid
    time.sleep(10)
