import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)


@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin_positive_scenario():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys("onibonojemariam@gmail.com")
    pass_input.send_keys("Oyinkan@32")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    # Explicit Wait
    wait = WebDriverWait(driver=driver, timeout=10)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), "Dashboard"))
    # EC.presence_of_element_located((By.CSS_SELECTOR,".page-heading"))
    # EC.visibility_of_element_located((By.CSS_SELECTOR,".page-heading"))
    # )
    heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    assert heading_element.text == "Mariam Temitope Onibon-oje"
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
