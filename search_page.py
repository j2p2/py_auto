from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearchPage():
    def __init__(self, driver):
        self.driver = driver

    def search_for(self, arg):
        input_field = self.driver.find_element_by_name("q")
        input_field.clear()
        input_field.send_keys(arg)
        input_field.send_keys(Keys.RETURN)
