# Web Tables in Selenium
# Web Table is a way of representing data in rows and columns.
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()
    time.sleep(5)

    # find how many rows and column awesomeqa website
    # //table[contains(@id,"cust")]/tbody/tr -> xpath for the rows
    # //table[contains(@id,"cust")]/tbody/tr[2]/td -> xpath for the column

    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)

    column_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    column = len(column_elements)
    print(column)

    ## //table[contains(@id,'cust')]/tbody/tr
    # [7] THis is the table row. it changes. it is dynamic in nature
    # /td
    # [3] This is the table data. it is dynamic in nature

    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    # There are two types of tables: we have dynamic and static table
    # In static tables both row and column are same

    # for loop is used to print all the elements/path

    # for i in range(2,row + 1): # range from 1-10, takes from 1-9 in python, that is why we need to do +1
    #     for j in range(1,column + 1):
    #         dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}" # "f" means we are using a formating
    #         data = driver.find_element(By.XPATH, dynamic_path)
    #         print(data.text, end=" ")

    # find Helen Bennett in the table and which country she belongs to

    for i in range(2, row + 1):  # range from 1-10, takes from 1-9 in python, that is why we need to do +1
        for j in range(1, column + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennett is in {country_text} ")

        # In dynamic tables rows and column can be different i.e rows can be 4 while coulmn is 3
        # viseversa

        driver.get("https://awesomeqa.com/webtable.html")
        # get the Table
        table = driver.find_elements(By.XPATH, "//table[@summary='Sample Table']/tbody")
        row_table = "//table[@summary='Sample Table]/tbody/tr" #table.find_element(By.TAG_NAME, "tr")
        print(row_table)
