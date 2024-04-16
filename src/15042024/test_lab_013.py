from selenium import webdriver
import time
import pytest

# Navigate commands are not present in python only :
def test_open_browser():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(10)
    driver.back()
    driver.get("https://www.bing.com")
    time.sleep(5)
    print(driver.title)

    driver.forward()
    print(driver.title)

    driver.back()
    print(driver.title)
    driver.refresh()

    time.sleep(5)
    driver.quit()
