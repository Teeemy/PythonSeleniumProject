# Selenium automates browser
# selenium architecture-> code get converted to API request and Api send to browserdriver
# and browserdriver basically opens the url. that is how the architecture works
# Selenim 3 uses json wire protocol, and it is used by 20%
# Selenium 4 uses w3c protocol and selenium manager.itis used by 70%

# pip install selenium -> 4.x-> you don't have to setup the browser drivers

# when using selenium 3, you need to set the driver_path first, but we
# no longer use selenium 3 but selenium 4

from selenium import webdriver

# selenium 3 format


def test_open_website():
    pass
    # driver_path = '/Users/Ola/Downloads/edge/msedgedriver'
    # driver = webdriver.EdgeService(executable_path=driver_path)
    driver.get("https://app.vwo.com")
