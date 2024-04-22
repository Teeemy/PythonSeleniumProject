import time

from selenium import webdriver
from selenium.webdriver.common.by import By
 

def test_open_cura_website():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

                    #by ID
    # driver.find_element(By.ID,"btn-make-appointment").click()

    # By.Link Text-> will always give exact or full match with the text
    # it is always with an anchor tag i.e <a /a>
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment / is the link text
    # </a>
# if there are two or more link text, it will always return the first one
# if there is no link text, it will not be able to find the element
                #BY Link
    # first mechanism to link text
#     make_appointment_btn = driver.find_element(By.LINK_TEXT,"Make Appointment")
#     make_appointment_btn.click()
    # second mechanism is partial Text or partial match . it is also with anchor tag
    # Partial_link_text also gives a part of the text e.g it can give appointment, or make alone
   # or app, or appoint. it contains keyword. it finds the first unique element

   # make_appointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    #     make_appointment_btn.click()

                # By Tag <a/a> i.e anchor tag
    list_of_a_tags = driver.find_elements(By.TAG_NAME, 'a') #list is used because tag name give alot of alphapets with a
    make_appointment_btn=list_of_a_tags[5]# indext start from 0, so sixth element is 5
    make_appointment_btn.click()

    time.sleep(10)

   # assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()
