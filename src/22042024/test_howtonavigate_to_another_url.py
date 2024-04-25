# How to navigate to another URL? by using get command but there is no any navigation command in python.
# Navigation commands are very popular in JAVA.

import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By  # Imported By from common


@pytest.mark.smoke
@allure.title("Verify that login is working in cura website")
@allure.description("TC#1 - Simple Login check on CURA katalon website.")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    # //*[@id='btn-make-apgyeewgh9899'] -- It means find everywhere (*) where id='btn-make-apgyeewgh9899'. --> 1st way
    # This is called * wild card. Find id='btn-make-apgyeewgh9899' in all the TagNames. This will be slow path.

    # //a[@id='btn-make-appointment'] -- If we know the tag name then we can mention. --> 2nd way
    # both will give you unique element but 2nd will be a fast way as we have specified with a tag.
    # means from the tag find the id.

    # //a[text()= 'Make Appointment'] -- Any element where text()= 'Make Appointment' -- we will be able to find it by using text().
    # text() -> Problem is it will give you exact match. Suppose a developer mention 'Appointments' instead of 'Appointment' then in
    # that case, it won't work and then we need partial text.
    Make_Appointment_btn = driver.find_element(By.XPATH, "//a[text()= 'Make Appointment']")

    # Partial Text() - contains():
    # //a[contains(text(),'Make Appointment')]
    # //a[contains(text(),'Appointment')]
    # //a[contains(text(),'Make')]
    # //a[contains(text(),'Ma')]
    # //a[contains(text(),'App')] - This may fail if there are 1 or more tag with 'App'. There can be multiple elements.

    # //a[starts-with(text(),'Make')]

    # <a rel="https://google.com"/> -- rel is relative attribute. It is a custom attribute.

    # Suppose we have dynamic element, we will use multiple elements and we will combine them by using AND condition like below:
    # //a[text()='Make Appointment' and contains (@id,'btn-make-appointment')]

    # For eg: if we have a, first we will say contains id AND href AND class
    # By above-mentioned eg, we will find a unique element.
    # //a[text()='Make Appointment' and contains (@id,'btn-make-appointment') and contains (@href,'./profile.php#login')]

    # The best way, if you find one element and then you can find all the elements in the same page.

    # CSS Selector:
    # CSS Selector can also pass the page which means directly we can use # with id attribute.
    # # corresponds to id.
    # . (when we see spaces, instead of spaces, use dot) corresponds to class.
    Make_Appointment_btn = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    Make_Appointment_css_btn_list= driver.find_elements(By.CSS_SELECTOR, ".btn.btn-dark.btn-lg") # but it's not
    # unique. It will provide a list.

    # Take below example and convert into CSS selector and XPATH:
    # CSS Selector: header#top>div
    # XPATH: //header[@id='top']/div


    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)

    driver.quit()
# There is no best way which should we use either XPATH or CSS Selector. In whatever we comfortable, we can use.
# For eg:

# When we use CSS selector in Automation for 1000 TCs, with 32GB RAM and will take 30 mins to execute.
# When we use XPATH in Automation for 1000 TCs, with 32GB RAM and will take 30.34 mins to execute.
# Hence, there is no big difference. Very low difference

# The moment we increase the RAM
# When we use CSS selector in Automation for 1000 TCs, with 64GB RAM and will take 15 mins to execute.
# When we use XPATH in Automation for 1000 TCs, with 64GB RAM and will take 15 mins to execute.
# The more memory we have, the difference between "CSS selector" and "XPATH" is almost same.

# Difference is when
# When we use CSS selector in Automation for 1000 TCs, with 4GB RAM and will take 30 mins to execute.
# When we use XPATH in Automation for 1000 TCs, with 4GB RAM and will take 36 mins to execute.