#project 4
# Open ebay.com.
# Search for the "16 gb"
# Print all the Top 60 Results with their Names and price.
# Give me the cheapest one from the list.

import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
@pytest.mark.smoke
@allure.title("verify ebay login page")
@allure.description("TC#1 - Search for the 16 gb and Print all the Top 60 Results with their Names and price")
def test_ebay_login():
    driver= webdriver.Chrome()
    driver.get("https://www.ebay.com")
    time.sleep(5)

    assert driver.current_url == "https://www.ebay.com/"
    print(driver.current_url)

    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']")

    search_box.send_keys("16 gb")
    time.sleep(5)

    search_btn = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_btn.click()

    list_results = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in list_results:
        print(i.text)

    time.sleep(5) # in Future we will remove this



    time.sleep(5)
    driver.quit()