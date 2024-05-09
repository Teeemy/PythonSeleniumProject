import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Shadowdom is a custom element
def test_01_shadowDOM_scroll():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(2)
    div = driver.find_element(By.XPATH, "//div[@class='jackPart']")

    # Scroll to View to DIV,and find the pizza element
    js_ex = driver.execute_script
    js_ex("arguments[0].scrollIntoView(true);", div)


    # pizza = driver.find_element(By.ID, "pizza")
    # pizza.send_keys("Farmhouse")

    time.sleep(10)
    driver.quit()
