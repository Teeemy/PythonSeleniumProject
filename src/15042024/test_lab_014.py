import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# interacting with html elements
# to recognise html elements is through (TAG ->H1-H5,title) (ATTRIBUTES-> these are key value pair
# that helps to find elements eg id,Href,class)
# locator is a way of identifying an element on a web page so that it can be
# interacted with. Locators in selenium include

# ID,NAME,CLASS NAME,TAG NAME,LINK TEXT,(CSS SELECTOR,XPATH are easy
# short way to find elements in html unlike ID, NAME AND others,


def test_open_url():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    element = driver.find_element(By.ID,"btn-make-appointment") # used to find element with a strategy(by.either ID< TAG or others)
    time.sleep(10)
    element.click() # web element with function of click

    time.sleep(25)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()

#find_element/find_elements are diff. element without s will return one element,while
# with s will return a list of elements

    # < a
# id = "btn-make-appointment"
# href = "./profile.php#login"
# class ="btn btn-dark btn-lg"
# >
# Make Appointment
# < / a >

# Find the element where the anchor tag  button <a is located and click on it

# when checking for an element, make sure it is unique.i.e 1of 1
