from selenium import webdriver
import time
import pytest


def test_open_browser():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(25)
    driver.get("https://google.com")
    print(driver.title)
    time.sleep(20)




