import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Alerts in selenium is a small window that appears on top of a web page
# and displays a message to the user. most times, alert are
# used to show important info or ask user for info
def test_01_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    button.click()
    time.sleep(5)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Oyinkan")
    alert.accept()
    # alert.dismiss()
    time.sleep(3)

    # popups -> model or html popup, alert - this how handle
    # wait for the model to come and click on the escape button, or close button
    result = driver.find_element(By.ID, "result")
    print(result.text)
    assert "Oyinkan" in result.text
