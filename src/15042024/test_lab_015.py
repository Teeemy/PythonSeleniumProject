import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_vwologin_negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

# attributes ->
# < input
# type = "email"
# class ="text-input W(100%)"
# name="username"
# id="login-username"
# data-qa="hocewoqisi" >

    email_element = driver.find_element(By.NAME,"username")# NAME is always uppercase in python
    email_element.send_keys("admin") # used to enter input in a textbox

    time.sleep(10)
    #< input
    #type = "password"
    #class ="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe" aria-autocomplete="list" >

    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys("admin")

    # < button
    # type = "submit"
    # id = "js-login-btn"
    # class ="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)" onclick="login.login(event)" data-qa="sibequkica" >
    # < span
    # class ="icon loader hidden" data-qa="zuyezasugu" > < / span >
    # < span
    # data - qa = "ezazsuguuy" > Sign in < / span >
    # < / button >

    button_submit_element = driver.find_element(By.ID,"js-login-btn")
    button_submit_element.click()

    time.sleep(5)

    # div
    # class ="notification-box-description"
    # id="js-notification-box-msg" data-qa="rixawilomi" >
    # Your email, password, IP address or location did not match
    # < / div >

    error_msg_element = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()