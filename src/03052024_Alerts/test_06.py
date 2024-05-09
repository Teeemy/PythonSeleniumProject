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
def test_01_shadowDOM_scroll_type():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")

    div = driver.find_element(By.XPATH, "//div[@class='jackPart']")

    # Scroll to View to DIV,and find the pizza element and type farmhouse
    driver.execute_script("arguments[0].scrollIntoView(true);", div)

    time.sleep(2)

    pizza = driver.execute_script(
        "return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
    pizza.send_keys("Farmhouse")

    # pizza = driver.find_element(By.ID, "pizza")
    # pizza.send_keys("Farmhouse")

    time.sleep(10)
    driver.quit()