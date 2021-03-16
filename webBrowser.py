from selenium import webdriver
browser = webdriver.Firefox(executable_path=r'/Users/ttavarone/LocalDocs/Development/chromedriver')
type(browser)
browser.get('http://inventwithpython.com')