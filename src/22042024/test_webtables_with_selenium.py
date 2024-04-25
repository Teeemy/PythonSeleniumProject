from selenium import webdriver
from selenium.webdriver.common.by import By


# Example of Static Table:
def test_web_tables():
    driver = webdriver.Chrome()
    # driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()
    #
    # # first I need to find how many rows this table has?
    # # //table[contains(@id,'customers')]/tbody/tr -- It will give you all the rows
    #
    # # and how many columns it has?
    # # //table[contains(@id,'customers')]/tbody/tr[2]/td -- It will give you all the columns
    # row_element = driver.find_elements(By.XPATH,
    #                                    "//table[contains(@id,'cust')]/tbody/tr")  # It will give you row elements
    # row = len(row_element)  # total no of rows
    # print(row)  # It will print row value
    #
    # col_element = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    # col = len(col_element)
    # print(col)
    #
    # # 1st part-> //table[contains(@id,'cust')]/tbody/tr[ -- This part will remain constant.
    # # 7 - i(2,7) -- only value is being changed for row. Ideally it should change from (1,7) but we extra td that's why it's being changed from (2,7)
    # # 2nd part-> ]/td[
    # # 3 -j(1,3) -- only value is being changed for column
    # # 3rd part-> ]
    # # we will be using for loop
    # first_part = "//table[contains(@id,'cust')]/tbody/tr["
    # second_part = "]/td["
    # third_part = "]"
    #
    # for i in range(2, row + 1):  # range(1,10) -> it will take 1 to 9. That's why 9+1
    #     for j in range(1, col + 1):
    #         dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"  # we want to generate all the paths by using for loop as I ant to print all the elements
    #         print(dynamic_path)  # After printing the dynamic path, I need text part.
    #         data = driver.find_element(By.XPATH,
    #                                    dynamic_path).text  # I want to find the element where this dynamic path exist and want to get the text of it.
    #         # print(data.text, end=" ")
    #         # if interviewer say find "Helen Bennett" and in which country she belongs to?
    #         if "Helen Bennett" in data:
    #             country_path = f"{dynamic_path}/following-sibling::td"
    #             country_text = driver.find_element(By.XPATH, country_path).text
    #             print(f"Helen Bennett is in {country_text}")

    # Example of Dynamic table, If we have dynamic table.
    driver.get("https://awesomeqa.com/webtable1.html")
    # Get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    # row_table = "//table[@summary='Sample Table']/tbody/tr"  # another way: 1st find rows in the table.
    row_table = table.find_elements(By.TAG_NAME, "tr") # tr should be within the table. Here I want to find all the tr (rows) . That's why "find_elements"

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td") # if we are find to be able to row, then we can find column name also by using tag name.
        for e in cols:
            # print(e.text)
            if "UAE" in e.text:
                print("Yes")